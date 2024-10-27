from ...base import HL7Table

"""
HL7 Version: 2.5.1
Referral disposition - 0282
Table Type: User
"""


class ReferralDisposition(HL7Table):
    """
    Referral disposition - 0282 // User table type
    - ASSUME_MANAGEMENT
    - RETURN_PATIENT_AFTER_EVALUATION
    - SECOND_OPINION
    - SEND_WRITTEN_REPORT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0282
    """

    ASSUME_MANAGEMENT = "AM"
    """Assume Management"""
    RETURN_PATIENT_AFTER_EVALUATION = "RP"
    """Return Patient After Evaluation"""
    SECOND_OPINION = "SO"
    """Second Opinion"""
    SEND_WRITTEN_REPORT = "WR"
    """Send Written Report"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReferralDisposition.ASSUME_MANAGEMENT: "Assume Management",
    ReferralDisposition.RETURN_PATIENT_AFTER_EVALUATION: "Return Patient After Evaluation",
    ReferralDisposition.SECOND_OPINION: "Second Opinion",
    ReferralDisposition.SEND_WRITTEN_REPORT: "Send Written Report",
}
