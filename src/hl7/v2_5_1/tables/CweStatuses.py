from ...base import HL7Table

"""
HL7 Version: 2.5.1
CWE statuses - 0353
Table Type: HL7
"""


class CweStatuses(HL7Table):
    """
    CWE statuses - 0353 // HL7 table type
    - NOT_APPLICABLE
    - NOT_ASKED
    - NOT_AVAILABLE
    - UNKNOWN
    - ASKED_BUT_UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0353
    """

    NOT_APPLICABLE = "NA"
    """Not applicable"""
    NOT_ASKED = "NASK"
    """Not asked"""
    NOT_AVAILABLE = "NAV"
    """Not available"""
    UNKNOWN = "U"
    """Unknown"""
    ASKED_BUT_UNKNOWN = "UASK"
    """Asked but Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CweStatuses.NOT_APPLICABLE: "Not applicable",
    CweStatuses.NOT_ASKED: "Not asked",
    CweStatuses.NOT_AVAILABLE: "Not available",
    CweStatuses.UNKNOWN: "Unknown",
    CweStatuses.ASKED_BUT_UNKNOWN: "Asked but Unknown",
}
