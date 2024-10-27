from ...base import HL7Table

"""
HL7 Version: 2.5.1
Patient Class - 0004
Table Type: User
"""


class PatientClass(HL7Table):
    """
    Patient Class - 0004 // User table type
    - OBSTETRICS
    - COMMERCIAL_ACCOUNT
    - EMERGENCY
    - INPATIENT
    - NOT_APPLICABLE
    - OUTPATIENT
    - PREADMIT
    - RECURRING_PATIENT
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0004
    """

    OBSTETRICS = "B"
    """Obstetrics"""
    COMMERCIAL_ACCOUNT = "C"
    """Commercial Account"""
    EMERGENCY = "E"
    """Emergency"""
    INPATIENT = "I"
    """Inpatient"""
    NOT_APPLICABLE = "N"
    """Not Applicable"""
    OUTPATIENT = "O"
    """Outpatient"""
    PREADMIT = "P"
    """Preadmit"""
    RECURRING_PATIENT = "R"
    """Recurring patient"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PatientClass.OBSTETRICS: "Obstetrics",
    PatientClass.COMMERCIAL_ACCOUNT: "Commercial Account",
    PatientClass.EMERGENCY: "Emergency",
    PatientClass.INPATIENT: "Inpatient",
    PatientClass.NOT_APPLICABLE: "Not Applicable",
    PatientClass.OUTPATIENT: "Outpatient",
    PatientClass.PREADMIT: "Preadmit",
    PatientClass.RECURRING_PATIENT: "Recurring patient",
    PatientClass.UNKNOWN: "Unknown",
}
