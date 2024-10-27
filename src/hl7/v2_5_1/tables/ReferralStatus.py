from ...base import HL7Table

"""
HL7 Version: 2.5.1
Referral status - 0283
Table Type: User
"""


class ReferralStatus(HL7Table):
    """
    Referral status - 0283 // User table type
    - ACCEPTED
    - EXPIRED
    - PENDING
    - REJECTED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0283
    """

    ACCEPTED = "A"
    """Accepted"""
    EXPIRED = "E"
    """Expired"""
    PENDING = "P"
    """Pending"""
    REJECTED = "R"
    """Rejected"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReferralStatus.ACCEPTED: "Accepted",
    ReferralStatus.EXPIRED: "Expired",
    ReferralStatus.PENDING: "Pending",
    ReferralStatus.REJECTED: "Rejected",
}
