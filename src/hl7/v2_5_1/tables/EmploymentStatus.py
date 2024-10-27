from ...base import HL7Table

"""
HL7 Version: 2.5.1
Employment Status - 0066
Table Type: User
"""


class EmploymentStatus(HL7Table):
    """
    Employment Status - 0066 // User table type
    - FULL_TIME_EMPLOYED
    - PART_TIME_EMPLOYED
    - UNEMPLOYED
    - SELF_EMPLOYED
    - RETIRED
    - ON_ACTIVE_MILITARY_DUTY
    - UNKNOWN
    - CONTRACT_PER_DIEM
    - LEAVE_OF_ABSENCE
    - OTHER
    - TEMPORARILY_UNEMPLOYED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0066
    """

    FULL_TIME_EMPLOYED = "1"
    """Full time employed"""
    PART_TIME_EMPLOYED = "2"
    """Part time employed"""
    UNEMPLOYED = "3"
    """Unemployed"""
    SELF_EMPLOYED = "4"
    """Self-employed,"""
    RETIRED = "5"
    """Retired"""
    ON_ACTIVE_MILITARY_DUTY = "6"
    """On active military duty"""
    UNKNOWN = "9"
    """Unknown"""
    CONTRACT_PER_DIEM = "C"
    """Contract, per diem"""
    LEAVE_OF_ABSENCE = "L"
    """Leave of absence (e.g. Family leave, sabbatical, etc.)"""
    OTHER = "O"
    """Other"""
    TEMPORARILY_UNEMPLOYED = "T"
    """Temporarily unemployed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EmploymentStatus.FULL_TIME_EMPLOYED: "Full time employed",
    EmploymentStatus.PART_TIME_EMPLOYED: "Part time employed",
    EmploymentStatus.UNEMPLOYED: "Unemployed",
    EmploymentStatus.SELF_EMPLOYED: "Self-employed,",
    EmploymentStatus.RETIRED: "Retired",
    EmploymentStatus.ON_ACTIVE_MILITARY_DUTY: "On active military duty",
    EmploymentStatus.UNKNOWN: "Unknown",
    EmploymentStatus.CONTRACT_PER_DIEM: "Contract, per diem",
    EmploymentStatus.LEAVE_OF_ABSENCE: "Leave of absence (e.g. Family leave, sabbatical, etc.)",
    EmploymentStatus.OTHER: "Other",
    EmploymentStatus.TEMPORARILY_UNEMPLOYED: "Temporarily unemployed",
}
