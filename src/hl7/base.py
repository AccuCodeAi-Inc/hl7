import re
from abc import abstractmethod
from enum import Enum
from typing import Any, Generic, Protocol, TypeVar


class HL7:
    _rpt = "~"
    _esc = "\\"
    _sep = "^"
    _sub = "&"
    _delim = "NotImplemented"

    @abstractmethod
    def __init__(self):
        self._c_attrs = ()  # auto populated by codegen; references to setters/getters on self
        self._c_data = []  # length & default vals initialized by code gen
        self._hl7_id = "base"

    @classmethod
    def _escape(cls, value: str) -> str:
        if not value:
            return ""
        for char in (cls._sep, cls._rpt, cls._esc, cls._sub, cls._delim):
            value = value.replace(char, f"\\{char}")
        return value

    def _build_component(self, component) -> str:
        escaped_values = []
        for value in component:
            if isinstance(value, HL7):
                escaped_values.append(value._serialize())
            else:
                escaped_values.append(self._escape(value))
        return self._rpt.join(escaped_values)

    def _serialize(self) -> str:
        return self._delim.join(
            self._build_component(component) for component in self._c_data
        )

    def __len__(self):
        def _len(val):
            if isinstance(val, list):
                return sum(_len(v) for v in val)
            return len(val)

        return _len(self._c_data)

    def __getitem__(self, item: int | type[str]):
        return self._c_attrs[item]

    def __setitem__(self, idx: int, item: str):
        self._c_attrs[idx]

    def __iter__(self):
        for v in self._c_attrs:
            yield v


class HL7Segment(HL7):
    _delim = "|"

    def to_hl7(self) -> str:
        return f"{self._hl7_id}|{self._serialize()}"


class HL7TriggerEvent(HL7):
    _delim = "\n"

    def to_hl7(self) -> str:
        return self._serialize()


class HL7SegmentGroup(HL7TriggerEvent): ...


# class HL7Field(HL7):
#     _delim = "|"
#     def to_hl7(self) -> str:
#         return self._serialize()


class HL7Component(HL7):
    _delim = "^"

    def to_hl7(self, sep="^") -> str:
        return self._serialize()


class DataType(HL7Component): ...


class HL7Subcomponent(HL7):
    _delim = "&"

    def to_hl7(self, sep="%") -> str:
        return self._serialize()


class HL7Exception(Exception): ...


class HL7TriggerEventValidationException(ValueError, HL7Exception): ...


class HL7TableParseException(ValueError, HL7Exception): ...


class HL7PrimitiveParseException(ValueError, HL7Exception): ...


class EnumParser(Protocol):
    """
    EnumParser implementations are any callable which take three arguments:

        1. the input value,
        2. list of enum member names
        3. list of enum member descriptions

    and returns:

        1. a string representing the target enum member name or None, if there are no good choices

      EXAMPLE:
          from openai import OpenAI
          def llm_parser(raw_value: str, choices: list[str], descriptions: list[str]) -> str:
                fmt_choices = "\n".join([f"choice: '{c}', description: '{d}'" for c, d in zip(choices, descriptions)])
                prompt = "you are a enum parser... here is a list of choices: {fmt_choices}... choose only one"
                result = openai.completions...etc etc...
                assert result in choices
                return result
    """

    def __call__(
        self, raw_value: Any, choices: list[str], descriptions: list[str]
    ) -> str | None: ...


E = TypeVar("E", bound=Enum)


class HL7Table(Generic[E], Enum):
    @classmethod
    def parse(cls: type[E], value: Any, *, using: EnumParser) -> E:
        """
        Parse a value into an HL7 Table value (enum member) `using` a higher-order function.

        This method attempts to convert the given value into an enum member of the class.
        The `using` function will be used to preprocess the input value
        before attempting to create the enum member.

        :param value: The value to be parsed into an enum member.
        :param using: A callable implementing the EnumParser Protocol to preprocess the input value,
                      which takes two arguments:
                          1. the input value,
                          2. list of tuples containing the enum member name and docstring
                      and should return:
                          1. a string representing the target enum member name
        :return: An enum member of the class.
        :raises HL7ParseException: If the value cannot be parsed into a valid enum member.
        """
        try:
            raw_value = str(value)
            choices = [x.value for x in cls]
            descriptions = [cls(x).description for x in cls]
            return cls(using(raw_value, choices, descriptions))
        except ValueError as e:
            raise HL7TableParseException from e


class StrParser(Protocol):
    """
    StrParser implementations are any callable which take two arguments:

      1. the raw text input value (raw_value)
      2. the docstrings of the subclass containing a description of the data_type (type_description)

    and returns:

      1. a well-structured string according to the description (type_description) of the data_type

      EXAMPLE:
          from openai import OpenAI
          def llm_parser(raw_value: str, type_description: str) -> str:
                prompt = "you are a string parser..."
                openai.completions...
                etc etc...
                return "Parsed Result"
    """

    def __call__(self, raw_value: Any, type_description: str) -> str: ...


class StrValidator(Protocol):
    r"""
    StrValidator implementations are any callable which take one argument:

      1. the formatted text input value (formatted_value)

    and returns:

      1. a boolean representing whether or not the input value is valid or not.

    EXAMPLE:
        def phone_validator(phone_no: str) -> bool:
            m = re.match(r"(\d\d\d)-(\d\d)-(\d\d)-(\d\d)", phone_no)
            return bool(m)

    USAGE EXAMPLE:
        validated_st = (
            ST.parse("Hello World", using=llm_parser)
              .validate_or_raise(using=str.is_title)
        )
    """

    def __call__(self, formatted_value: str) -> bool: ...


S = TypeVar("S", bound=str)


class HL7Primitive(Generic[S]):
    def validate(
        self: S, *, using: StrValidator = None, regex: str | re.Pattern = None
    ) -> bool:
        """
        Validate an HL7 primitive using a StrValidator callable OR regex pattern.
        """
        if regex:
            if isinstance(regex, str):
                m = re.compile(regex).match(str(self))
                return bool(m)
            if isinstance(regex, re.Pattern):
                return bool(regex.match(str(self)))

        if callable(using):
            return using(str(self))

        return True

    def validate_or_raise(
        self: S, *, using: StrValidator = None, regex: str | re.Pattern = None
    ) -> S:
        if not all((self.validate(regex=regex), self.validate(using=using))):
            raise HL7PrimitiveParseException(f"{self.__name__} failed validation")
        return self

    @classmethod
    def parse(cls: type[S], value: str, *, using: StrParser) -> S:
        """
        Parse a value into an HL7 primitive data_type `using` a higher-order function.

        This method attempts to convert the given value into well-structured primitive datatype.
        The `using` function will be used to preprocess the input value
        before attempting to create the primitive data_type.

        :param value: The value to be parsed into an enum member.
        :param using: A function to preprocess the raw text input value into formatted output value
        :return: An enum member of the class.
        :raises HL7ParseException: If the value cannot be parsed into a valid enum member.
        """
        return cls(using(value, cls.__doc__))
