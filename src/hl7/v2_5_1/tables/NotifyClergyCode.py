from ...base import HL7Table

"""
HL7 Version: 2.5.1
Notify Clergy Code - 0534
Table Type: User
"""


class NotifyClergyCode(HL7Table):
    """
    Notify Clergy Code - 0534 // User table type
    - LAST_RITES_ONLY
    - NO
    - OTHER
    - UNKNOWN
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0534
    """

    LAST_RITES_ONLY = "L"
    """Last Rites only"""
    NO = "N"
    """No"""
    OTHER = "O"
    """Other"""
    UNKNOWN = "U"
    """Unknown"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NotifyClergyCode.LAST_RITES_ONLY: "Last Rites only",
    NotifyClergyCode.NO: "No",
    NotifyClergyCode.OTHER: "Other",
    NotifyClergyCode.UNKNOWN: "Unknown",
    NotifyClergyCode.YES: "Yes",
}
