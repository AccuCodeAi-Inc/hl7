from ...base import HL7Table

"""
HL7 Version: 2.5.1
Alert level - 0367
Table Type: HL7
"""


class AlertLevel(HL7Table):
    """
    Alert level - 0367 // HL7 table type
    - CRITICAL
    - NORMAL
    - SERIOUS
    - WARNING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0367
    """

    CRITICAL = "C"  # Shut Down, Fix Problem and Re-init
    """Critical"""
    NORMAL = "N"  # No Corrective Action Needed
    """Normal"""
    SERIOUS = "S"  # Corrective Action Required
    """Serious"""
    WARNING = "W"  # Corrective Action Anticipated
    """Warning"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AlertLevel.CRITICAL: "Critical",
    AlertLevel.NORMAL: "Normal",
    AlertLevel.SERIOUS: "Serious",
    AlertLevel.WARNING: "Warning",
}
