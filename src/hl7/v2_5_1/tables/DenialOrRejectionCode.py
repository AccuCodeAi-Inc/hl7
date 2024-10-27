from ...base import HL7Table

"""
HL7 Version: 2.5.1
Denial or Rejection Code - 0460
Table Type: User
"""


class DenialOrRejectionCode(HL7Table):
    """
    Denial or Rejection Code - 0460 // User table type
    - LINE_ITEM_NOT_DENIED_OR_REJECTED
    - LINE_ITEM_DENIED_OR_REJECTED
    - LINE_ITEM_IS_ON_A_MULTIPLE_DAY_CLAIM_THE_LINE_ITEM_IS_NOT_DENIED_OR_REJECTED_BUT_OCCURS_ON_A_DAY_THAT_HAS_BEEN_DENIED_OR_REJECTED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0460
    """

    LINE_ITEM_NOT_DENIED_OR_REJECTED = "0"
    """Line item not denied or rejected"""
    LINE_ITEM_DENIED_OR_REJECTED = "1"
    """Line item denied or rejected"""
    LINE_ITEM_IS_ON_A_MULTIPLE_DAY_CLAIM_THE_LINE_ITEM_IS_NOT_DENIED_OR_REJECTED_BUT_OCCURS_ON_A_DAY_THAT_HAS_BEEN_DENIED_OR_REJECTED = "2"
    """Line item is on a multiple-day claim. The line item is not denied or rejected, but occurs on a day that has been denied or rejected."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DenialOrRejectionCode.LINE_ITEM_NOT_DENIED_OR_REJECTED: "Line item not denied or rejected",
    DenialOrRejectionCode.LINE_ITEM_DENIED_OR_REJECTED: "Line item denied or rejected",
    DenialOrRejectionCode.LINE_ITEM_IS_ON_A_MULTIPLE_DAY_CLAIM_THE_LINE_ITEM_IS_NOT_DENIED_OR_REJECTED_BUT_OCCURS_ON_A_DAY_THAT_HAS_BEEN_DENIED_OR_REJECTED: "Line item is on a multiple-day claim. The line item is not denied or rejected, but occurs on a day that has been denied or rejected.",
}
