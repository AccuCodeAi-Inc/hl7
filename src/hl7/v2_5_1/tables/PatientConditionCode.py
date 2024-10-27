from ...base import HL7Table

"""
HL7 Version: 2.5.1
Patient Condition Code - 0434
Table Type: User
"""


class PatientConditionCode(HL7Table):
    """
    Patient Condition Code - 0434 // User table type
    - SATISFACTORY
    - CRITICAL
    - OTHER
    - POOR
    - STABLE
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0434
    """

    SATISFACTORY = "A"
    """Satisfactory"""
    CRITICAL = "C"
    """Critical"""
    OTHER = "O"
    """Other"""
    POOR = "P"
    """Poor"""
    STABLE = "S"
    """Stable"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PatientConditionCode.SATISFACTORY: "Satisfactory",
    PatientConditionCode.CRITICAL: "Critical",
    PatientConditionCode.OTHER: "Other",
    PatientConditionCode.POOR: "Poor",
    PatientConditionCode.STABLE: "Stable",
    PatientConditionCode.UNKNOWN: "Unknown",
}
