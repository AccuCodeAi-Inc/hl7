from ...base import HL7Table

"""
HL7 Version: 2.5.1
Administrative Sex - 0001
Table Type: User
"""


class AdministrativeSex(HL7Table):
    """
    Administrative Sex - 0001 // User table type
    - AMBIGUOUS
    - FEMALE
    - MALE
    - NOT_APPLICABLE
    - OTHER
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0001
    """

    AMBIGUOUS = "A"
    """Ambiguous"""
    FEMALE = "F"
    """Female"""
    MALE = "M"
    """Male"""
    NOT_APPLICABLE = "N"
    """Not applicable"""
    OTHER = "O"
    """Other"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdministrativeSex.AMBIGUOUS: "Ambiguous",
    AdministrativeSex.FEMALE: "Female",
    AdministrativeSex.MALE: "Male",
    AdministrativeSex.NOT_APPLICABLE: "Not applicable",
    AdministrativeSex.OTHER: "Other",
    AdministrativeSex.UNKNOWN: "Unknown",
}
