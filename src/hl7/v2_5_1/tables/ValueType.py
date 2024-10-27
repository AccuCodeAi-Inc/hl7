from ...base import HL7Table

"""
HL7 Version: 2.5.1
Value type - 0125
Table Type: HL7
"""


class ValueType(HL7Table):
    """
    Value type - 0125 // HL7 table type
    - ADDRESS
    - CODED_ENTRY
    - CODED_ELEMENT_WITH_FORMATTED_VALUES
    - COMPOSITE_ID_WITH_CHECK_DIGIT
    - COMPOSITE_ID_AND_NAME
    - COMPOSITE_PRICE
    - EXTENDED_COMPOSITE_ID_WITH_CHECK_DIGIT
    - DATE
    - ENCAPSULATED_DATA
    - FORMATTED_TEXT
    - MONEY
    - NUMERIC
    - PERSON_NAME
    - REFERENCE_POINTER
    - STRUCTURED_NUMERIC
    - STRING_DATA
    - TIME
    - TELEPHONE_NUMBER
    - TIME_STAMP
    - TEXT_DATA
    - EXTENDED_ADDRESS
    - EXTENDED_COMPOSITE_NAME_AND_NUMBER_FOR_PERSONS
    - EXTENDED_COMPOSITE_NAME_AND_NUMBER_FOR_ORGANIZATIONS
    - EXTENDED_PERSON_NAME
    - EXTENDED_TELECOMMUNICATIONS_NUMBER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0125
    """

    ADDRESS = "AD"
    """Address"""
    CODED_ENTRY = "CE"
    """Coded Entry"""
    CODED_ELEMENT_WITH_FORMATTED_VALUES = "CF"
    """Coded Element With Formatted Values"""
    COMPOSITE_ID_WITH_CHECK_DIGIT = "CK"
    """Composite ID With Check Digit"""
    COMPOSITE_ID_AND_NAME = "CN"
    """Composite ID And Name"""
    COMPOSITE_PRICE = "CP"
    """Composite Price"""
    EXTENDED_COMPOSITE_ID_WITH_CHECK_DIGIT = "CX"
    """Extended Composite ID With Check Digit"""
    DATE = "DT"
    """Date"""
    ENCAPSULATED_DATA = "ED"
    """Encapsulated Data"""
    FORMATTED_TEXT = "FT"
    """Formatted Text (Display)"""
    MONEY = "MO"
    """Money"""
    NUMERIC = "NM"
    """Numeric"""
    PERSON_NAME = "PN"
    """Person Name"""
    REFERENCE_POINTER = "RP"
    """Reference Pointer"""
    STRUCTURED_NUMERIC = "SN"
    """Structured Numeric"""
    STRING_DATA = "ST"
    """String Data."""
    TIME = "TM"
    """Time"""
    TELEPHONE_NUMBER = "TN"
    """Telephone Number"""
    TIME_STAMP = "TS"
    """Time Stamp (Date &amp; Time)"""
    TEXT_DATA = "TX"
    """Text Data (Display)"""
    EXTENDED_ADDRESS = "XAD"
    """Extended Address"""
    EXTENDED_COMPOSITE_NAME_AND_NUMBER_FOR_PERSONS = "XCN"
    """Extended Composite Name And Number For Persons"""
    EXTENDED_COMPOSITE_NAME_AND_NUMBER_FOR_ORGANIZATIONS = "XON"
    """Extended Composite Name And Number For Organizations"""
    EXTENDED_PERSON_NAME = "XPN"
    """Extended Person Name"""
    EXTENDED_TELECOMMUNICATIONS_NUMBER = "XTN"
    """Extended Telecommunications Number"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ValueType.ADDRESS: "Address",
    ValueType.CODED_ENTRY: "Coded Entry",
    ValueType.CODED_ELEMENT_WITH_FORMATTED_VALUES: "Coded Element With Formatted Values",
    ValueType.COMPOSITE_ID_WITH_CHECK_DIGIT: "Composite ID With Check Digit",
    ValueType.COMPOSITE_ID_AND_NAME: "Composite ID And Name",
    ValueType.COMPOSITE_PRICE: "Composite Price",
    ValueType.EXTENDED_COMPOSITE_ID_WITH_CHECK_DIGIT: "Extended Composite ID With Check Digit",
    ValueType.DATE: "Date",
    ValueType.ENCAPSULATED_DATA: "Encapsulated Data",
    ValueType.FORMATTED_TEXT: "Formatted Text (Display)",
    ValueType.MONEY: "Money",
    ValueType.NUMERIC: "Numeric",
    ValueType.PERSON_NAME: "Person Name",
    ValueType.REFERENCE_POINTER: "Reference Pointer",
    ValueType.STRUCTURED_NUMERIC: "Structured Numeric",
    ValueType.STRING_DATA: "String Data.",
    ValueType.TIME: "Time",
    ValueType.TELEPHONE_NUMBER: "Telephone Number",
    ValueType.TIME_STAMP: "Time Stamp (Date &amp; Time)",
    ValueType.TEXT_DATA: "Text Data (Display)",
    ValueType.EXTENDED_ADDRESS: "Extended Address",
    ValueType.EXTENDED_COMPOSITE_NAME_AND_NUMBER_FOR_PERSONS: "Extended Composite Name And Number For Persons",
    ValueType.EXTENDED_COMPOSITE_NAME_AND_NUMBER_FOR_ORGANIZATIONS: "Extended Composite Name And Number For Organizations",
    ValueType.EXTENDED_PERSON_NAME: "Extended Person Name",
    ValueType.EXTENDED_TELECOMMUNICATIONS_NUMBER: "Extended Telecommunications Number",
}
