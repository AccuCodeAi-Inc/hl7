from ...base import HL7Table

"""
HL7 Version: 2.5.1
Case Category Code - 0423
Table Type: User
"""


class CaseCategoryCode(HL7Table):
    """
    Case Category Code - 0423 // User table type
    - DOCTORS_OFFICE_CLOSED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0423
    """

    DOCTORS_OFFICE_CLOSED = "D"
    """Doctors Office Closed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CaseCategoryCode.DOCTORS_OFFICE_CLOSED: "Doctors Office Closed",
}
