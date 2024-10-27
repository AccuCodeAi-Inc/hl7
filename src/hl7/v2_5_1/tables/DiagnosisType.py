from ...base import HL7Table

"""
HL7 Version: 2.5.1
Diagnosis Type - 0052
Table Type: User
"""


class DiagnosisType(HL7Table):
    """
    Diagnosis Type - 0052 // User table type
    - ADMITTING
    - FINAL
    - WORKING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0052
    """

    ADMITTING = "A"
    """Admitting"""
    FINAL = "F"
    """Final"""
    WORKING = "W"
    """Working"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DiagnosisType.ADMITTING: "Admitting",
    DiagnosisType.FINAL: "Final",
    DiagnosisType.WORKING: "Working",
}
