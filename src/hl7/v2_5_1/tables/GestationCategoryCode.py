from ...base import HL7Table

"""
HL7 Version: 2.5.1
Gestation Category Code - 0424
Table Type: User
"""


class GestationCategoryCode(HL7Table):
    """
    Gestation Category Code - 0424 // User table type
    - PREMATURE_OR_PRE_TERM
    - FULL_TERM
    - OVERDUE_OR_POST_TERM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0424
    """

    PREMATURE_OR_PRE_TERM = "1"
    """Premature / Pre-term"""
    FULL_TERM = "2"
    """Full Term"""
    OVERDUE_OR_POST_TERM = "3"
    """Overdue / Post-term"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    GestationCategoryCode.PREMATURE_OR_PRE_TERM: "Premature / Pre-term",
    GestationCategoryCode.FULL_TERM: "Full Term",
    GestationCategoryCode.OVERDUE_OR_POST_TERM: "Overdue / Post-term",
}
