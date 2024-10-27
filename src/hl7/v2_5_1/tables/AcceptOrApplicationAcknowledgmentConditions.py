from ...base import HL7Table

"""
HL7 Version: 2.5.1
Accept/application acknowledgment conditions - 0155
Table Type: HL7
"""


class AcceptOrApplicationAcknowledgmentConditions(HL7Table):
    """
    Accept/application acknowledgment conditions - 0155 // HL7 table type
    - ALWAYS
    - ERROR_OR_REJECT_CONDITIONS_ONLY
    - NEVER
    - SUCCESSFUL_COMPLETION_ONLY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0155
    """

    ALWAYS = "AL"
    """Always"""
    ERROR_OR_REJECT_CONDITIONS_ONLY = "ER"
    """Error/reject conditions only"""
    NEVER = "NE"
    """Never"""
    SUCCESSFUL_COMPLETION_ONLY = "SU"
    """Successful completion only"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AcceptOrApplicationAcknowledgmentConditions.ALWAYS: "Always",
    AcceptOrApplicationAcknowledgmentConditions.ERROR_OR_REJECT_CONDITIONS_ONLY: "Error/reject conditions only",
    AcceptOrApplicationAcknowledgmentConditions.NEVER: "Never",
    AcceptOrApplicationAcknowledgmentConditions.SUCCESSFUL_COMPLETION_ONLY: "Successful completion only",
}
