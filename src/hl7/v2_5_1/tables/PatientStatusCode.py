from ...base import HL7Table

"""
HL7 Version: 2.5.1
Patient Status Code - 0216
Table Type: User
"""


class PatientStatusCode(HL7Table):
    """
    Patient Status Code - 0216 // User table type
    - ACTIVE_INPATIENT
    - DISCHARGED_INPATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0216
    """

    ACTIVE_INPATIENT = "AI"
    """Active Inpatient"""
    DISCHARGED_INPATIENT = "DI"
    """Discharged Inpatient"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PatientStatusCode.ACTIVE_INPATIENT: "Active Inpatient",
    PatientStatusCode.DISCHARGED_INPATIENT: "Discharged Inpatient",
}
