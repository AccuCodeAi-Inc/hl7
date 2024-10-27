from ...base import HL7Table

"""
HL7 Version: 2.5.1
Admission Level of Care Code - 0432
Table Type: User
"""


class AdmissionLevelOfCareCode(HL7Table):
    """
    Admission Level of Care Code - 0432 // User table type
    - ACUTE
    - CHRONIC
    - COMATOSE
    - CRITICAL
    - IMPROVED
    - MORIBUND
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0432
    """

    ACUTE = "AC"
    """Acute"""
    CHRONIC = "CH"
    """Chronic"""
    COMATOSE = "CO"
    """Comatose"""
    CRITICAL = "CR"
    """Critical"""
    IMPROVED = "IM"
    """Improved"""
    MORIBUND = "MO"
    """Moribund"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdmissionLevelOfCareCode.ACUTE: "Acute",
    AdmissionLevelOfCareCode.CHRONIC: "Chronic",
    AdmissionLevelOfCareCode.COMATOSE: "Comatose",
    AdmissionLevelOfCareCode.CRITICAL: "Critical",
    AdmissionLevelOfCareCode.IMPROVED: "Improved",
    AdmissionLevelOfCareCode.MORIBUND: "Moribund",
}
