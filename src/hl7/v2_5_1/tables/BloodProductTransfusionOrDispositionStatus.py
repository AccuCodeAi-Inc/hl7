from ...base import HL7Table

"""
HL7 Version: 2.5.1
Blood Product Transfusion/Disposition Status - 0513
Table Type: HL7
"""


class BloodProductTransfusionOrDispositionStatus(HL7Table):
    """
    Blood Product Transfusion/Disposition Status - 0513 // HL7 table type
    - RETURNED_UNUSED_OR_NO_LONGER_NEEDED
    - RETURNED_UNUSED_OR_KEEP_LINKED_TO_PATIENT_FOR_POSSIBLE_USE_LATER
    - TRANSFUSED_WITH_ADVERSE_REACTION
    - TRANSFUSED
    - WASTED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0513
    """

    RETURNED_UNUSED_OR_NO_LONGER_NEEDED = "RA"
    """Returned unused/no longer needed"""
    RETURNED_UNUSED_OR_KEEP_LINKED_TO_PATIENT_FOR_POSSIBLE_USE_LATER = "RL"
    """Returned unused/keep linked to patient for possible use later"""
    TRANSFUSED_WITH_ADVERSE_REACTION = "TR"
    """Transfused with adverse reaction"""
    TRANSFUSED = "TX"
    """Transfused"""
    WASTED = "WA"
    """Wasted (product no longer viable)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BloodProductTransfusionOrDispositionStatus.RETURNED_UNUSED_OR_NO_LONGER_NEEDED: "Returned unused/no longer needed",
    BloodProductTransfusionOrDispositionStatus.RETURNED_UNUSED_OR_KEEP_LINKED_TO_PATIENT_FOR_POSSIBLE_USE_LATER: "Returned unused/keep linked to patient for possible use later",
    BloodProductTransfusionOrDispositionStatus.TRANSFUSED_WITH_ADVERSE_REACTION: "Transfused with adverse reaction",
    BloodProductTransfusionOrDispositionStatus.TRANSFUSED: "Transfused",
    BloodProductTransfusionOrDispositionStatus.WASTED: "Wasted (product no longer viable)",
}
