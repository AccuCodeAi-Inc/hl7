from ...base import HL7Table

"""
HL7 Version: 2.5.1
Certification patient type - 0150
Table Type: User
"""


class CertificationPatientType(HL7Table):
    """
    Certification patient type - 0150 // User table type
    - EMERGENCY
    - INPATIENT_ELECTIVE
    - OUTPATIENT_ELECTIVE
    - URGENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0150
    """

    EMERGENCY = "ER"
    """Emergency"""
    INPATIENT_ELECTIVE = "IPE"
    """Inpatient elective"""
    OUTPATIENT_ELECTIVE = "OPE"
    """Outpatient elective"""
    URGENT = "UR"
    """Urgent"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CertificationPatientType.EMERGENCY: "Emergency",
    CertificationPatientType.INPATIENT_ELECTIVE: "Inpatient elective",
    CertificationPatientType.OUTPATIENT_ELECTIVE: "Outpatient elective",
    CertificationPatientType.URGENT: "Urgent",
}
