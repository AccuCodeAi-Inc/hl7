from ...base import HL7Table

"""
HL7 Version: 2.5.1
Special Program Code - 0214
Table Type: User
"""


class SpecialProgramCode(HL7Table):
    """
    Special Program Code - 0214 // User table type
    - CHILD_HEALTH_ASSISTANCE
    - ELECTIVE_SURGERY_PROGRAM
    - FAMILY_PLANNING
    - OTHER
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0214
    """

    CHILD_HEALTH_ASSISTANCE = "CH"
    """Child Health Assistance"""
    ELECTIVE_SURGERY_PROGRAM = "ES"
    """Elective Surgery Program"""
    FAMILY_PLANNING = "FP"
    """Family Planning"""
    OTHER = "O"
    """Other"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecialProgramCode.CHILD_HEALTH_ASSISTANCE: "Child Health Assistance",
    SpecialProgramCode.ELECTIVE_SURGERY_PROGRAM: "Elective Surgery Program",
    SpecialProgramCode.FAMILY_PLANNING: "Family Planning",
    SpecialProgramCode.OTHER: "Other",
    SpecialProgramCode.UNKNOWN: "Unknown",
}
