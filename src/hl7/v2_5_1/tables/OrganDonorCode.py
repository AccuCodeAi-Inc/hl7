from ...base import HL7Table

"""
HL7 Version: 2.5.1
Organ Donor Code - 0316
Table Type: User
"""


class OrganDonorCode(HL7Table):
    """
    Organ Donor Code - 0316 // User table type
    - YES_PATIENT_IS_A_DOCUMENTED_DONOR_BUT_DOCUMENTATION_IS_NOT_ON_FILE
    - NO_PATIENT_IS_NOT_A_DOCUMENTED_DONOR_BUT_INFORMATION_WAS_PROVIDED
    - NO_PATIENT_HAS_NOT_AGREED_TO_BE_A_DONOR
    - PATIENT_LEAVES_ORGAN_DONATION_DECISION_TO_A_SPECIFIC_PERSON
    - PATIENT_LEAVES_ORGAN_DONATION_DECISION_TO_RELATIVES
    - UNKNOWN
    - YES_PATIENT_IS_A_DOCUMENTED_DONOR_AND_DOCUMENTATION_IS_ON_FILE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0316
    """

    YES_PATIENT_IS_A_DOCUMENTED_DONOR_BUT_DOCUMENTATION_IS_NOT_ON_FILE = "F"
    """Yes, patient is a documented donor, but documentation is not on file"""
    NO_PATIENT_IS_NOT_A_DOCUMENTED_DONOR_BUT_INFORMATION_WAS_PROVIDED = "I"
    """No, patient is not a documented donor, but information was provided"""
    NO_PATIENT_HAS_NOT_AGREED_TO_BE_A_DONOR = "N"
    """No, patient has not agreed to be a donor"""
    PATIENT_LEAVES_ORGAN_DONATION_DECISION_TO_A_SPECIFIC_PERSON = "P"
    """Patient leaves organ donation decision to a specific person"""
    PATIENT_LEAVES_ORGAN_DONATION_DECISION_TO_RELATIVES = "R"
    """Patient leaves organ donation decision to relatives"""
    UNKNOWN = "U"
    """Unknown"""
    YES_PATIENT_IS_A_DOCUMENTED_DONOR_AND_DOCUMENTATION_IS_ON_FILE = "Y"
    """Yes, patient is a documented donor and documentation is on file"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OrganDonorCode.YES_PATIENT_IS_A_DOCUMENTED_DONOR_BUT_DOCUMENTATION_IS_NOT_ON_FILE: "Yes, patient is a documented donor, but documentation is not on file",
    OrganDonorCode.NO_PATIENT_IS_NOT_A_DOCUMENTED_DONOR_BUT_INFORMATION_WAS_PROVIDED: "No, patient is not a documented donor, but information was provided",
    OrganDonorCode.NO_PATIENT_HAS_NOT_AGREED_TO_BE_A_DONOR: "No, patient has not agreed to be a donor",
    OrganDonorCode.PATIENT_LEAVES_ORGAN_DONATION_DECISION_TO_A_SPECIFIC_PERSON: "Patient leaves organ donation decision to a specific person",
    OrganDonorCode.PATIENT_LEAVES_ORGAN_DONATION_DECISION_TO_RELATIVES: "Patient leaves organ donation decision to relatives",
    OrganDonorCode.UNKNOWN: "Unknown",
    OrganDonorCode.YES_PATIENT_IS_A_DOCUMENTED_DONOR_AND_DOCUMENTATION_IS_ON_FILE: "Yes, patient is a documented donor and documentation is on file",
}
