from ...base import HL7Table

"""
HL7 Version: 2.5.1
Primary Observer's Qualification - 0242
Table Type: HL7
"""


class PrimaryObserverSQualification(HL7Table):
    """
    Primary Observer's Qualification - 0242 // HL7 table type
    - HEALTH_CARE_CONSUMER_OR_PATIENT
    - OTHER_HEALTH_PROFESSIONAL
    - LAWYER_OR_ATTORNEY
    - MID_LEVEL_PROFESSIONAL
    - OTHER_NON_HEALTH_PROFESSIONAL
    - PHYSICIAN
    - PHARMACIST
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0242
    """

    HEALTH_CARE_CONSUMER_OR_PATIENT = "C"
    """Health care consumer/patient"""
    OTHER_HEALTH_PROFESSIONAL = "H"
    """Other health professional"""
    LAWYER_OR_ATTORNEY = "L"
    """Lawyer/attorney"""
    MID_LEVEL_PROFESSIONAL = "M"
    """Mid-level professional (nurse, nurse practitioner, physicians assistant)"""
    OTHER_NON_HEALTH_PROFESSIONAL = "O"
    """Other non-health professional"""
    PHYSICIAN = "P"
    """Physician (osteopath, homeopath)"""
    PHARMACIST = "R"
    """Pharmacist"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PrimaryObserverSQualification.HEALTH_CARE_CONSUMER_OR_PATIENT: "Health care consumer/patient",
    PrimaryObserverSQualification.OTHER_HEALTH_PROFESSIONAL: "Other health professional",
    PrimaryObserverSQualification.LAWYER_OR_ATTORNEY: "Lawyer/attorney",
    PrimaryObserverSQualification.MID_LEVEL_PROFESSIONAL: "Mid-level professional (nurse, nurse practitioner, physicians assistant)",
    PrimaryObserverSQualification.OTHER_NON_HEALTH_PROFESSIONAL: "Other non-health professional",
    PrimaryObserverSQualification.PHYSICIAN: "Physician (osteopath, homeopath)",
    PrimaryObserverSQualification.PHARMACIST: "Pharmacist",
}
