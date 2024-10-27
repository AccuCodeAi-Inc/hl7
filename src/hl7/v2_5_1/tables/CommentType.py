from ...base import HL7Table

"""
HL7 Version: 2.5.1
Comment type - 0364
Table Type: User
"""


class CommentType(HL7Table):
    """
    Comment type - 0364 // User table type
    - PRIMARY_REASON
    - SECONDARY_REASON
    - ANCILLARY_INSTRUCTIONS
    - DUPLICATE_OR_INTERACTION_REASON
    - GENERAL_INSTRUCTIONS
    - GENERAL_REASON
    - PATIENT_INSTRUCTIONS
    - REMARK
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0364
    """

    PRIMARY_REASON = "1R"
    """Primary Reason"""
    SECONDARY_REASON = "2R"
    """Secondary Reason"""
    ANCILLARY_INSTRUCTIONS = "AI"
    """Ancillary Instructions"""
    DUPLICATE_OR_INTERACTION_REASON = "DR"
    """Duplicate/Interaction Reason"""
    GENERAL_INSTRUCTIONS = "GI"
    """General Instructions"""
    GENERAL_REASON = "GR"
    """General Reason"""
    PATIENT_INSTRUCTIONS = "PI"
    """Patient Instructions"""
    REMARK = "RE"
    """Remark"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CommentType.PRIMARY_REASON: "Primary Reason",
    CommentType.SECONDARY_REASON: "Secondary Reason",
    CommentType.ANCILLARY_INSTRUCTIONS: "Ancillary Instructions",
    CommentType.DUPLICATE_OR_INTERACTION_REASON: "Duplicate/Interaction Reason",
    CommentType.GENERAL_INSTRUCTIONS: "General Instructions",
    CommentType.GENERAL_REASON: "General Reason",
    CommentType.PATIENT_INSTRUCTIONS: "Patient Instructions",
    CommentType.REMARK: "Remark",
}
