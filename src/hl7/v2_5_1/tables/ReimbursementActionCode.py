from ...base import HL7Table

"""
HL7 Version: 2.5.1
Reimbursement Action Code - 0459
Table Type: User
"""


class ReimbursementActionCode(HL7Table):
    """
    Reimbursement Action Code - 0459 // User table type
    - OCE_LINE_ITEM_DENIAL_OR_REJECTION_IS_NOT_IGNORED
    - OCE_LINE_ITEM_DENIAL_OR_REJECTION_IS_IGNORED
    - EXTERNAL_LINE_ITEM_DENIAL_LINE_ITEM_IS_DENIED_EVEN_IF_NO_OCE_EDITS
    - EXTERNAL_LINE_ITEM_REJECTION_LINE_ITEM_IS_REJECTED_EVEN_IF_NO_OCE_EDITS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0459
    """

    OCE_LINE_ITEM_DENIAL_OR_REJECTION_IS_NOT_IGNORED = "0"
    """OCE line item denial or rejection is not ignored"""
    OCE_LINE_ITEM_DENIAL_OR_REJECTION_IS_IGNORED = "1"
    """OCE line item denial or rejection is ignored"""
    EXTERNAL_LINE_ITEM_DENIAL_LINE_ITEM_IS_DENIED_EVEN_IF_NO_OCE_EDITS = "2"
    """External line item denial. Line item is denied even if no OCE edits"""
    EXTERNAL_LINE_ITEM_REJECTION_LINE_ITEM_IS_REJECTED_EVEN_IF_NO_OCE_EDITS = "3"
    """External line item rejection. Line item is rejected even if no OCE edits"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReimbursementActionCode.OCE_LINE_ITEM_DENIAL_OR_REJECTION_IS_NOT_IGNORED: "OCE line item denial or rejection is not ignored",
    ReimbursementActionCode.OCE_LINE_ITEM_DENIAL_OR_REJECTION_IS_IGNORED: "OCE line item denial or rejection is ignored",
    ReimbursementActionCode.EXTERNAL_LINE_ITEM_DENIAL_LINE_ITEM_IS_DENIED_EVEN_IF_NO_OCE_EDITS: "External line item denial. Line item is denied even if no OCE edits",
    ReimbursementActionCode.EXTERNAL_LINE_ITEM_REJECTION_LINE_ITEM_IS_REJECTED_EVEN_IF_NO_OCE_EDITS: "External line item rejection. Line item is rejected even if no OCE edits",
}
