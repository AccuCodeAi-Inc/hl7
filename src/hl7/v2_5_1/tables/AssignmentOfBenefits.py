from ...base import HL7Table

"""
HL7 Version: 2.5.1
Assignment of Benefits - 0135
Table Type: User
"""


class AssignmentOfBenefits(HL7Table):
    """
    Assignment of Benefits - 0135 // User table type
    - MODIFIED_ASSIGNMENT
    - NO
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0135
    """

    MODIFIED_ASSIGNMENT = "M"
    """Modified assignment"""
    NO = "N"
    """No"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AssignmentOfBenefits.MODIFIED_ASSIGNMENT: "Modified assignment",
    AssignmentOfBenefits.NO: "No",
    AssignmentOfBenefits.YES: "Yes",
}
