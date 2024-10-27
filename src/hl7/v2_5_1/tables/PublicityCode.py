from ...base import HL7Table

"""
HL7 Version: 2.5.1
Publicity Code - 0215
Table Type: User
"""


class PublicityCode(HL7Table):
    """
    Publicity Code - 0215 // User table type
    - FAMILY_ONLY
    - NO_PUBLICITY
    - OTHER
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0215
    """

    FAMILY_ONLY = "F"
    """Family only"""
    NO_PUBLICITY = "N"
    """No Publicity"""
    OTHER = "O"
    """Other"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PublicityCode.FAMILY_ONLY: "Family only",
    PublicityCode.NO_PUBLICITY: "No Publicity",
    PublicityCode.OTHER: "Other",
    PublicityCode.UNKNOWN: "Unknown",
}
