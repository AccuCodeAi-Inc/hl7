from ...base import HL7Table

"""
HL7 Version: 2.5.1
Government reimbursement program - 0401
Table Type: User
"""


class GovernmentReimbursementProgram(HL7Table):
    """
    Government reimbursement program - 0401 // User table type
    - MEDI_CAL
    - MEDICARE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0401
    """

    MEDI_CAL = "C"
    """Medi-Cal"""
    MEDICARE = "MM"
    """Medicare"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    GovernmentReimbursementProgram.MEDI_CAL: "Medi-Cal",
    GovernmentReimbursementProgram.MEDICARE: "Medicare",
}
