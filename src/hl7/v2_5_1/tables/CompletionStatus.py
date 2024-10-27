from ...base import HL7Table

"""
HL7 Version: 2.5.1
Completion Status - 0322
Table Type: HL7
"""


class CompletionStatus(HL7Table):
    """
    Completion Status - 0322 // HL7 table type
    - COMPLETE
    - NOT_ADMINISTERED
    - PARTIALLY_ADMINISTERED
    - REFUSED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0322
    """

    COMPLETE = "CP"
    """Complete"""
    NOT_ADMINISTERED = "NA"
    """Not Administered"""
    PARTIALLY_ADMINISTERED = "PA"
    """Partially Administered"""
    REFUSED = "RE"
    """Refused"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CompletionStatus.COMPLETE: "Complete",
    CompletionStatus.NOT_ADMINISTERED: "Not Administered",
    CompletionStatus.PARTIALLY_ADMINISTERED: "Partially Administered",
    CompletionStatus.REFUSED: "Refused",
}
