from ...base import HL7Table

"""
HL7 Version: 2.5.1
Overall Claim Disposition Code - 0457
Table Type: User
"""


class OverallClaimDispositionCode(HL7Table):
    """
    Overall Claim Disposition Code - 0457 // User table type
    - NO_EDITS_PRESENT_ON_CLAIM
    - ONLY_EDITS_PRESENT_ARE_FOR_LINE_ITEM_DENIAL_OR_REJECTION
    - MULTIPLE_DAY_CLAIM_WITH_ONE_OR_MORE_DAYS_DENIED_OR_REJECTED
    - CLAIM_DENIED_REJECTED_SUSPENDED_OR_RETURNED_TO_PROVIDER_WITH_ONLY_POST_PAYMENT_EDITS
    - CLAIM_DENIED_REJECTED_SUSPENDED_OR_RETURNED_TO_PROVIDER_WITH_ONLY_PRE_PAYMENT_EDITS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0457
    """

    NO_EDITS_PRESENT_ON_CLAIM = "0"
    """No edits present on claim"""
    ONLY_EDITS_PRESENT_ARE_FOR_LINE_ITEM_DENIAL_OR_REJECTION = "1"
    """Only edits present are for line item denial or rejection"""
    MULTIPLE_DAY_CLAIM_WITH_ONE_OR_MORE_DAYS_DENIED_OR_REJECTED = "2"
    """Multiple-day claim with one or more days denied or rejected"""
    CLAIM_DENIED_REJECTED_SUSPENDED_OR_RETURNED_TO_PROVIDER_WITH_ONLY_POST_PAYMENT_EDITS = "3"
    """Claim denied, rejected, suspended or returned to provider with only post payment edits"""
    CLAIM_DENIED_REJECTED_SUSPENDED_OR_RETURNED_TO_PROVIDER_WITH_ONLY_PRE_PAYMENT_EDITS = "4"
    """Claim denied, rejected, suspended or returned to provider with only pre payment edits"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OverallClaimDispositionCode.NO_EDITS_PRESENT_ON_CLAIM: "No edits present on claim",
    OverallClaimDispositionCode.ONLY_EDITS_PRESENT_ARE_FOR_LINE_ITEM_DENIAL_OR_REJECTION: "Only edits present are for line item denial or rejection",
    OverallClaimDispositionCode.MULTIPLE_DAY_CLAIM_WITH_ONE_OR_MORE_DAYS_DENIED_OR_REJECTED: "Multiple-day claim with one or more days denied or rejected",
    OverallClaimDispositionCode.CLAIM_DENIED_REJECTED_SUSPENDED_OR_RETURNED_TO_PROVIDER_WITH_ONLY_POST_PAYMENT_EDITS: "Claim denied, rejected, suspended or returned to provider with only post payment edits",
    OverallClaimDispositionCode.CLAIM_DENIED_REJECTED_SUSPENDED_OR_RETURNED_TO_PROVIDER_WITH_ONLY_PRE_PAYMENT_EDITS: "Claim denied, rejected, suspended or returned to provider with only pre payment edits",
}
