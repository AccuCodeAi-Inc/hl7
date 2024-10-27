from ...base import HL7Table

"""
HL7 Version: 2.5.1
Signature Code - 0535
Table Type: User
"""


class SignatureCode(HL7Table):
    """
    Signature Code - 0535 // User table type
    - SIGNED_CMS_1500_CLAIM_FORM_ON_FILE_E_G_AUTHORIZATION_FOR_RELEASE_OF_ANY_MEDICAL_OR_OTHER_INFORMATION_NECESSARY_TO_PROCESS_THIS_CLAIM_AND_ASSIGNMENT_OF_BENEFITS
    - SIGNED_AUTHORIZATION_FOR_ASSIGNMENT_OF_BENEFITS_ON_FILE
    - SIGNATURE_GENERATED_BY_PROVIDER_BECAUSE_THE_PATIENT_WAS_NOT_PHYSICALLY_PRESENT_FOR_SERVICES
    - SIGNED_AUTHORIZATION_FOR_RELEASE_OF_ANY_MEDICAL_OR_OTHER_INFORMATION_NECESSARY_TO_PROCESS_THIS_CLAIM_ON_FILE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0535
    """

    SIGNED_CMS_1500_CLAIM_FORM_ON_FILE_E_G_AUTHORIZATION_FOR_RELEASE_OF_ANY_MEDICAL_OR_OTHER_INFORMATION_NECESSARY_TO_PROCESS_THIS_CLAIM_AND_ASSIGNMENT_OF_BENEFITS = "C"
    """Signed CMS-1500 claim form on file, e.g. authorization for release of any medical or other information necessary to process this claim and assignment of benefits."""
    SIGNED_AUTHORIZATION_FOR_ASSIGNMENT_OF_BENEFITS_ON_FILE = "M"
    """Signed authorization for assignment of benefits on file."""
    SIGNATURE_GENERATED_BY_PROVIDER_BECAUSE_THE_PATIENT_WAS_NOT_PHYSICALLY_PRESENT_FOR_SERVICES = "P"
    """Signature generated by provider because the patient was not physically present for services."""
    SIGNED_AUTHORIZATION_FOR_RELEASE_OF_ANY_MEDICAL_OR_OTHER_INFORMATION_NECESSARY_TO_PROCESS_THIS_CLAIM_ON_FILE = "S"
    """Signed authorization for release of any medical or other information necessary to process this claim on file."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SignatureCode.SIGNED_CMS_1500_CLAIM_FORM_ON_FILE_E_G_AUTHORIZATION_FOR_RELEASE_OF_ANY_MEDICAL_OR_OTHER_INFORMATION_NECESSARY_TO_PROCESS_THIS_CLAIM_AND_ASSIGNMENT_OF_BENEFITS: "Signed CMS-1500 claim form on file, e.g. authorization for release of any medical or other information necessary to process this claim and assignment of benefits.",
    SignatureCode.SIGNED_AUTHORIZATION_FOR_ASSIGNMENT_OF_BENEFITS_ON_FILE: "Signed authorization for assignment of benefits on file.",
    SignatureCode.SIGNATURE_GENERATED_BY_PROVIDER_BECAUSE_THE_PATIENT_WAS_NOT_PHYSICALLY_PRESENT_FOR_SERVICES: "Signature generated by provider because the patient was not physically present for services.",
    SignatureCode.SIGNED_AUTHORIZATION_FOR_RELEASE_OF_ANY_MEDICAL_OR_OTHER_INFORMATION_NECESSARY_TO_PROCESS_THIS_CLAIM_ON_FILE: "Signed authorization for release of any medical or other information necessary to process this claim on file.",
}