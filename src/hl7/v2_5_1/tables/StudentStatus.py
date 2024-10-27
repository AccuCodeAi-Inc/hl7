from ...base import HL7Table

"""
HL7 Version: 2.5.1
Student Status - 0231
Table Type: User
"""


class StudentStatus(HL7Table):
    """
    Student Status - 0231 // User table type
    - FULL_TIME_STUDENT
    - NOT_A_STUDENT
    - PART_TIME_STUDENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0231
    """

    FULL_TIME_STUDENT = "F"
    """Full-time student"""
    NOT_A_STUDENT = "N"
    """Not a student"""
    PART_TIME_STUDENT = "P"
    """Part-time student"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    StudentStatus.FULL_TIME_STUDENT: "Full-time student",
    StudentStatus.NOT_A_STUDENT: "Not a student",
    StudentStatus.PART_TIME_STUDENT: "Part-time student",
}
