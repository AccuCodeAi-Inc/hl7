import re
from abc import abstractmethod
from enum import Enum
from typing import Any, Generic, Protocol, TypeVar


class DELIM:
    seg = "\n"
    fld = "|"
    com = "^"
    rep = "~"
    esc = "\\"
    sub = "&"


class HL7:
    def __str__(self):
        return str(self.to_hl7()) if self else ""

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.to_hl7() if self else ""}')"

    def __iter__(self):
        for attr_name in self._c_attrs:
            yield getattr(self, attr_name)

    def __eq__(self, other: str):
        return str(self).strip() == str(other).strip()


class HL7Segment(HL7):
    # TODO: validate & escape

    def to_hl7(self, delim=DELIM) -> str:
        buf = []
        buf.append(self._hl7_id)
        is_msh = self._hl7_id == "MSH"
        for i, rpt in enumerate(self):
            match rpt:
                case _ if is_msh and i == 0:
                    delim.fld = rpt
                case _ if is_msh and i == 1:
                    assert len(rpt) == 4, f"invalid MSH.2 field separators: {rpt}"
                    delim.com, delim.rpt, delim.esc, delim.sub = (
                        rpt[0],
                        rpt[1],
                        rpt[2],
                        rpt[3],
                    )
                    buf.append(rpt)
                case None:
                    buf.append("")
                case str():
                    buf.append(str(rpt))
                case tuple():
                    reps = [c.to_hl7(delim) if c else "" for c in rpt]
                    val = delim.rep.join(reps).rstrip(delim.rep)
                    buf.append(val)
                case _:
                    buf.append(rpt.to_hl7(delim))

        return delim.fld.join(buf).rstrip(delim.fld)

    @classmethod
    def from_hl7[T](cls: type[T], hl7_str: str, delim=DELIM) -> T:
        if hl7_str.startswith("MSH"):
            h = hl7_str
            delim.fld, delim.com, delim.rpt, delim.esc, delim.sub = (
                h[3],
                h[4],
                h[5],
                h[6],
                h[7],
            )
            hl7_str = hl7_str.replace(f"MSH{delim.fld}", f"MSH{delim.fld*2}")

        s = hl7_str.split(delim.fld)
        s[1] = delim.fld
        assert (
            s[0] == cls._hl7_id
        ), f"invalid segment target: {s[0]} for segment {cls._hl7_id}"

        kwargs = {}
        for attr_name, component, attr_val in zip(
            cls._c_attrs, cls._c_components, s[1:]
        ):
            if not attr_val:
                continue
            if delim.rep in attr_val:
                rep_vals = attr_val.split(delim.rep)
                kwargs[attr_name] = (
                    component.from_hl7(rep_val, delim) for rep_val in rep_vals
                )
            else:
                kwargs[attr_name] = component.from_hl7(attr_val, delim)
        return cls(**kwargs)


class DataType(HL7):
    def to_hl7(self, delim=DELIM, is_subcomponent=False) -> str:
        buf = []
        for rpt in self:
            match rpt:
                case None:
                    buf.append("")
                case str():
                    buf.append(str(rpt))
                case tuple():
                    reps = [
                        c.to_hl7(delim, is_subcomponent=True) if c else "" for c in rpt
                    ]
                    val = delim.rep.join(reps).rstrip(delim.rep)
                    buf.append(val)
                case _:
                    buf.append(rpt.to_hl7(delim, is_subcomponent=True))

        if is_subcomponent:
            return delim.sub.join(buf).rstrip(delim.sub)
        return delim.com.join(buf).rstrip(delim.com)

    @classmethod
    def from_hl7[T](
        cls: type[T], hl7_str: str, delim=DELIM, is_subcomponent=False
    ) -> T:
        d = delim.com if not is_subcomponent else delim.sub
        s = hl7_str.split(d)
        kwargs = {}
        for attr_name, component, attr_val in zip(cls._c_attrs, cls._c_components, s):
            if not attr_val:
                continue
            if delim.rep in attr_val:
                rep_vals = attr_val.split(delim.rep)
                kwargs[attr_name] = (
                    component.from_hl7(
                        rep_val, delim, is_subcomponent=delim.sub in rep_val
                    )
                    for rep_val in rep_vals
                )
            else:
                kwargs[attr_name] = component.from_hl7(
                    attr_val, delim, is_subcomponent=delim.sub in attr_val
                )
        return cls(**kwargs)


class HL7TriggerEvent(HL7):
    def to_hl7(self, delim=DELIM, is_subcomponent=False) -> str:
        buf = []
        for rpt in self:
            match rpt:
                case None:
                    buf.append("")
                case str():
                    buf.append(str(rpt))
                case tuple():
                    reps = [c.to_hl7(delim) if c else "" for c in rpt]
                    val = delim.rep.join(reps).rstrip(delim.rep)
                    buf.append(val)
                case _:
                    buf.append(rpt.to_hl7(delim))

        return delim.seg.join(buf).rstrip(delim.seg)

    # TODO: finish parsing method handling for segment groups
    # @classmethod
    # def from_hl7[T](cls: type[T], hl7_str: str, delim=DELIM) -> T:
    #     kwargs = {}
    #     for attr_name, component, attr_val in zip(cls._c_attrs, cls._c_components, hl7_str.split("\n")):
    #         if attr_val:
    #             kwargs[attr_name] = component.from_hl7(attr_val, delim)
    #     return cls(**kwargs)


class HL7SegmentGroup(HL7TriggerEvent):
    # @classmethod
    # def from_hl7[T](cls: type[T], hl7_str: str, delim=DELIM) -> T | tuple[T]:
    #     kwargs = {}
    #     for attr_name, component, attr_val in zip(cls._c_attrs, cls._c_components, hl7_str.split("\n")):
    #         if attr_val:
    #             kwargs[attr_name] = component.from_hl7(attr_val)
    #     return cls(**kwargs)

    def to_hl7(self, delim=DELIM, is_subcomponent=False) -> str:
        from itertools import chain

        buf = []
        for rpt in self:
            if isinstance(rpt, tuple):
                for r in rpt:
                    buf.append(r.to_hl7(delim))
            else:
                buf.append(rpt.to_hl7(delim))

        return delim.seg.join(buf).rstrip(delim.seg)


class HL7Exception(Exception): ...


class HL7ExcessiveRepetition(IndexError, HL7Exception): ...


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
    def __str__(self):
        return str(self.value) if self.value else ""

    def __repr__(self):
        return f"{self.__class__.__name__}('{str(self)}')"

    def to_hl7(self, delim=DELIM, is_subcomponent=False) -> str:
        return str(self.value) if self else ""

    @classmethod
    def from_hl7(cls: type[E], hl7_str: str, delim=DELIM, is_subcomponent=False) -> E:
        return cls(hl7_str)

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
    def __eq__(self, other: str):
        return str(self).strip() == str(other).strip()

    def __str__(self):
        return self.to_hl7()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.to_hl7() if self else ""}')"

    def to_hl7(self, delim=DELIM, is_subcomponent=False) -> str:
        return str(self) if self else ""

    @classmethod
    def from_hl7(cls: type[E], hl7_str: str, delim=DELIM, is_subcomponent=False) -> E:
        return cls(hl7_str)

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

    # @classmethod
    # def aparse(cls, value: str, *, using):
    #     """Async version of parse. Call HL7._resolve_deferred() after HL7.__init__()"""
    #     async def wrapper():
    #         return await cls.parse(value, using=using)
    #     return asyncio.create_task(wrapper())
