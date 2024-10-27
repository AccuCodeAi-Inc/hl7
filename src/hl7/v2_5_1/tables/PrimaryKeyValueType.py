from ...base import HL7Table

"""
HL7 Version: 2.5.1
Primary key value type - 0355
Table Type: HL7
"""


class PrimaryKeyValueType(HL7Table):
    """
    Primary key value type - 0355 // HL7 table type
    - CODED_ELEMENT
    - PERSON_LOCATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0355
    """

    CODED_ELEMENT = "CE"
    """Coded element"""
    PERSON_LOCATION = "PL"
    """Person location"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PrimaryKeyValueType.CODED_ELEMENT: "Coded element",
    PrimaryKeyValueType.PERSON_LOCATION: "Person location",
}
