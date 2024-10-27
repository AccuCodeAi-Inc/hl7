from ...base import HL7Table

"""
HL7 Version: 2.5.1
Error severity - 0516
Table Type: HL7
"""


class ErrorSeverity(HL7Table):
    """
    Error severity - 0516 // HL7 table type
    - ERROR
    - INFORMATION
    - WARNING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0516
    """

    ERROR = "E"  # Transaction was unsuccessful
    """Error"""
    INFORMATION = (
        "I"  # Transaction was successful but includes information e.g., inform patient
    )
    """Information"""
    WARNING = "W"  # Transaction successful, but there may issues
    """Warning"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ErrorSeverity.ERROR: "Error",
    ErrorSeverity.INFORMATION: "Information",
    ErrorSeverity.WARNING: "Warning",
}
