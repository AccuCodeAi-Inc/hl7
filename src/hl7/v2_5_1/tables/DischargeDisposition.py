from ...base import HL7Table

"""
HL7 Version: 2.5.1
Discharge Disposition - 0112
Table Type: User
"""


class DischargeDisposition(HL7Table):
    """
    Discharge Disposition - 0112 // User table type
    - DISCHARGED_TO_HOME_OR_SELF_CARE
    - DISCHARGED_OR_TRANSFERRED_TO_ANOTHER_SHORT_TERM_GENERAL_HOSPITAL_FOR_INPATIENT_CARE
    - DISCHARGED_OR_TRANSFERRED_TO_SKILLED_NURSING_FACILITY
    - DISCHARGED_OR_TRANSFERRED_TO_AN_INTERMEDIATE_CARE_FACILITY
    - DISCHARGED_OR_TRANSFERRED_TO_ANOTHER_TYPE_OF_INSTITUTION_FOR_INPATIENT_CARE_OR_REFERRED_FOR_OUTPATIENT_SERVICES_TO_ANOTHER_INSTITUTION
    - DISCHARGED_OR_TRANSFERRED_TO_HOME_UNDER_CARE_OF_ORGANIZED_HOME_HEALTH_SERVICE_ORGANIZATION
    - LEFT_AGAINST_MEDICAL_ADVICE_OR_DISCONTINUED_CARE
    - DISCHARGED_OR_TRANSFERRED_TO_HOME_UNDER_CARE_OF_HOME_IV_PROVIDER
    - ADMITTED_AS_AN_INPATIENT_TO_THIS_HOSPITAL
    - DISCHARGE_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY
    - EXPIRED
    - EXPIRED_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY
    - STILL_PATIENT_OR_EXPECTED_TO_RETURN_FOR_OUTPATIENT_SERVICES
    - STILL_PATIENT_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY
    - _40
    - _41
    - _42
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0112
    """

    DISCHARGED_TO_HOME_OR_SELF_CARE = "01"
    """Discharged to home or self care (routine discharge)"""
    DISCHARGED_OR_TRANSFERRED_TO_ANOTHER_SHORT_TERM_GENERAL_HOSPITAL_FOR_INPATIENT_CARE = "02"
    """Discharged/transferred to another short term general hospital for inpatient care"""
    DISCHARGED_OR_TRANSFERRED_TO_SKILLED_NURSING_FACILITY = "03"
    """Discharged/transferred to skilled nursing facility (SNF)"""
    DISCHARGED_OR_TRANSFERRED_TO_AN_INTERMEDIATE_CARE_FACILITY = "04"
    """Discharged/transferred to an intermediate care facility (ICF)"""
    DISCHARGED_OR_TRANSFERRED_TO_ANOTHER_TYPE_OF_INSTITUTION_FOR_INPATIENT_CARE_OR_REFERRED_FOR_OUTPATIENT_SERVICES_TO_ANOTHER_INSTITUTION = "05"
    """Discharged/transferred to another type of institution for inpatient care or referred for outpatient services to another institution"""
    DISCHARGED_OR_TRANSFERRED_TO_HOME_UNDER_CARE_OF_ORGANIZED_HOME_HEALTH_SERVICE_ORGANIZATION = "06"
    """Discharged/transferred to home under care of organized home health service organization"""
    LEFT_AGAINST_MEDICAL_ADVICE_OR_DISCONTINUED_CARE = "07"
    """Left against medical advice or discontinued care"""
    DISCHARGED_OR_TRANSFERRED_TO_HOME_UNDER_CARE_OF_HOME_IV_PROVIDER = "08"
    """Discharged/transferred to home under care of Home IV provider"""
    ADMITTED_AS_AN_INPATIENT_TO_THIS_HOSPITAL = "09"
    """Admitted as an inpatient to this hospital"""
    DISCHARGE_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY = "10 …19"
    """Discharge to be defined at state level, if necessary"""
    EXPIRED = "20"
    """Expired (i.e. dead)"""
    EXPIRED_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY = "21 ... 29"
    """Expired to be defined at state level, if necessary"""
    STILL_PATIENT_OR_EXPECTED_TO_RETURN_FOR_OUTPATIENT_SERVICES = "30"
    """Still patient or expected to return for outpatient services (i.e. still a patient)"""
    STILL_PATIENT_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY = "31 … 39"
    """Still patient to be defined at state level, if necessary (i.e. still a patient)"""
    _40 = "40"
    """Expired (i.e. died) at home"""
    _41 = "41"
    """Expired (i.e. died) in a medical facility; e.g., hospital, SNF, ICF, or free standing hospice"""
    _42 = "42"
    """Expired (i.e. died) - place unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DischargeDisposition.DISCHARGED_TO_HOME_OR_SELF_CARE: "Discharged to home or self care (routine discharge)",
    DischargeDisposition.DISCHARGED_OR_TRANSFERRED_TO_ANOTHER_SHORT_TERM_GENERAL_HOSPITAL_FOR_INPATIENT_CARE: "Discharged/transferred to another short term general hospital for inpatient care",
    DischargeDisposition.DISCHARGED_OR_TRANSFERRED_TO_SKILLED_NURSING_FACILITY: "Discharged/transferred to skilled nursing facility (SNF)",
    DischargeDisposition.DISCHARGED_OR_TRANSFERRED_TO_AN_INTERMEDIATE_CARE_FACILITY: "Discharged/transferred to an intermediate care facility (ICF)",
    DischargeDisposition.DISCHARGED_OR_TRANSFERRED_TO_ANOTHER_TYPE_OF_INSTITUTION_FOR_INPATIENT_CARE_OR_REFERRED_FOR_OUTPATIENT_SERVICES_TO_ANOTHER_INSTITUTION: "Discharged/transferred to another type of institution for inpatient care or referred for outpatient services to another institution",
    DischargeDisposition.DISCHARGED_OR_TRANSFERRED_TO_HOME_UNDER_CARE_OF_ORGANIZED_HOME_HEALTH_SERVICE_ORGANIZATION: "Discharged/transferred to home under care of organized home health service organization",
    DischargeDisposition.LEFT_AGAINST_MEDICAL_ADVICE_OR_DISCONTINUED_CARE: "Left against medical advice or discontinued care",
    DischargeDisposition.DISCHARGED_OR_TRANSFERRED_TO_HOME_UNDER_CARE_OF_HOME_IV_PROVIDER: "Discharged/transferred to home under care of Home IV provider",
    DischargeDisposition.ADMITTED_AS_AN_INPATIENT_TO_THIS_HOSPITAL: "Admitted as an inpatient to this hospital",
    DischargeDisposition.DISCHARGE_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY: "Discharge to be defined at state level, if necessary",
    DischargeDisposition.EXPIRED: "Expired (i.e. dead)",
    DischargeDisposition.EXPIRED_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY: "Expired to be defined at state level, if necessary",
    DischargeDisposition.STILL_PATIENT_OR_EXPECTED_TO_RETURN_FOR_OUTPATIENT_SERVICES: "Still patient or expected to return for outpatient services (i.e. still a patient)",
    DischargeDisposition.STILL_PATIENT_TO_BE_DEFINED_AT_STATE_LEVEL_IF_NECESSARY: "Still patient to be defined at state level, if necessary (i.e. still a patient)",
    DischargeDisposition._40: "Expired (i.e. died) at home",
    DischargeDisposition._41: "Expired (i.e. died) in a medical facility; e.g., hospital, SNF, ICF, or free standing hospice",
    DischargeDisposition._42: "Expired (i.e. died) - place unknown",
}
