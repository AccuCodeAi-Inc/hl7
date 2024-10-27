from ...base import HL7Table

"""
HL7 Version: 2.5.1
Advanced Beneficiary Notice Code - 0339
Table Type: User
"""


class AdvancedBeneficiaryNoticeCode(HL7Table):
    """
    Advanced Beneficiary Notice Code - 0339 // User table type
    - SERVICE_IS_SUBJECT_TO_MEDICAL_NECESSITY_PROCEDURES
    - PATIENT_HAS_BEEN_INFORMED_OF_RESPONSIBILITY_AND_AGREES_TO_PAY_FOR_SERVICE
    - PATIENT_HAS_BEEN_INFORMED_OF_RESPONSIBILITY_AND_ASKS_THAT_THE_PAYER_BE_BILLED
    - ADVANCED_BENEFICIARY_NOTICE_HAS_NOT_BEEN_SIGNED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0339
    """

    SERVICE_IS_SUBJECT_TO_MEDICAL_NECESSITY_PROCEDURES = "1"
    """Service is subject to medical necessity procedures"""
    PATIENT_HAS_BEEN_INFORMED_OF_RESPONSIBILITY_AND_AGREES_TO_PAY_FOR_SERVICE = "2"
    """Patient has been informed of responsibility, and agrees to pay for service"""
    PATIENT_HAS_BEEN_INFORMED_OF_RESPONSIBILITY_AND_ASKS_THAT_THE_PAYER_BE_BILLED = "3"
    """Patient has been informed of responsibility, and asks that the payer be billed"""
    ADVANCED_BENEFICIARY_NOTICE_HAS_NOT_BEEN_SIGNED = "4"
    """Advanced Beneficiary Notice has not been signed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdvancedBeneficiaryNoticeCode.SERVICE_IS_SUBJECT_TO_MEDICAL_NECESSITY_PROCEDURES: "Service is subject to medical necessity procedures",
    AdvancedBeneficiaryNoticeCode.PATIENT_HAS_BEEN_INFORMED_OF_RESPONSIBILITY_AND_AGREES_TO_PAY_FOR_SERVICE: "Patient has been informed of responsibility, and agrees to pay for service",
    AdvancedBeneficiaryNoticeCode.PATIENT_HAS_BEEN_INFORMED_OF_RESPONSIBILITY_AND_ASKS_THAT_THE_PAYER_BE_BILLED: "Patient has been informed of responsibility, and asks that the payer be billed",
    AdvancedBeneficiaryNoticeCode.ADVANCED_BENEFICIARY_NOTICE_HAS_NOT_BEEN_SIGNED: "Advanced Beneficiary Notice has not been signed",
}
