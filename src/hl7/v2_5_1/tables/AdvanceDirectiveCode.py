from ...base import HL7Table

"""
HL7 Version: 2.5.1
Advance Directive Code - 0435
Table Type: User
"""


class AdvanceDirectiveCode(HL7Table):
    """
    Advance Directive Code - 0435 // User table type
    - DO_NOT_RESUSCITATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0435
    """

    DO_NOT_RESUSCITATE = "DNR"
    """Do not resuscitate"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdvanceDirectiveCode.DO_NOT_RESUSCITATE: "Do not resuscitate",
}
