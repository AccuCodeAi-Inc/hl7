from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event Seriousness - 0238
Table Type: HL7
"""


class EventSeriousness(HL7Table):
    """
    Event Seriousness - 0238 // HL7 table type
    - NO
    - SIGNIFICANT
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0238
    """

    NO = "N"
    """No"""
    SIGNIFICANT = "S"
    """Significant"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventSeriousness.NO: "No",
    EventSeriousness.SIGNIFICANT: "Significant",
    EventSeriousness.YES: "Yes",
}
