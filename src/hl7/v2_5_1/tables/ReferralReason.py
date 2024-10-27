from ...base import HL7Table

"""
HL7 Version: 2.5.1
Referral reason - 0336
Table Type: User
"""


class ReferralReason(HL7Table):
    """
    Referral reason - 0336 // User table type
    - PROVIDER_ORDERED
    - PATIENT_PREFERENCE
    - SECOND_OPINION
    - WORK_LOAD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0336
    """

    PROVIDER_ORDERED = "O"
    """Provider Ordered"""
    PATIENT_PREFERENCE = "P"
    """Patient Preference"""
    SECOND_OPINION = "S"
    """Second Opinion"""
    WORK_LOAD = "W"
    """Work Load"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReferralReason.PROVIDER_ORDERED: "Provider Ordered",
    ReferralReason.PATIENT_PREFERENCE: "Patient Preference",
    ReferralReason.SECOND_OPINION: "Second Opinion",
    ReferralReason.WORK_LOAD: "Work Load",
}
