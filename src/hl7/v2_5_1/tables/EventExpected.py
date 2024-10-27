from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event Expected - 0239
Table Type: HL7
"""


class EventExpected(HL7Table):
    """
    Event Expected - 0239 // HL7 table type
    - NO
    - UNKNOWN
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0239
    """

    NO = "N"
    """No"""
    UNKNOWN = "U"
    """Unknown"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventExpected.NO: "No",
    EventExpected.UNKNOWN: "Unknown",
    EventExpected.YES: "Yes",
}
