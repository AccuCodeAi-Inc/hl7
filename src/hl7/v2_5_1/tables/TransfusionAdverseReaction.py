from ...base import HL7Table

"""
HL7 Version: 2.5.1
Transfusion Adverse Reaction - 0514
Table Type: User
"""


class TransfusionAdverseReaction(HL7Table):
    """
    Transfusion Adverse Reaction - 0514 // User table type
    - ABO_INCOMPATIBLE_TRANSFUSION_REACTION
    - ACUTE_HEMOLYTIC_TRANSFUSION_REACTION
    - ALLERGIC_REACTION_FIRST
    - ALLERGIC_REACTION_RECURRENT
    - ALLERGIC_REACTION_REPEATING
    - ANAPHYLACTIC_REACTION
    - REACTION_TO_BACTERIAL_CONTAMINATION
    - DELAYED_HEMOLYTIC_TRANSFUSION_REACTION
    - DELAYED_SEROLOGICAL_TRANSFUSION_REACTION
    - GRAFT_VS_HOST_DISEASE_TRANSFUSION_ASSOCIATED
    - NON_HEMOLYTIC_HYPOTENSIVE_REACTION
    - NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_FIRST
    - NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_RECURRENT
    - NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_REPEATING
    - NON_IMMUNE_HEMOLYSIS
    - NON_SPECIFIC_NON_HEMOLYTIC_TRANSFUSION_REACTION
    - NO_EVIDENCE_OF_TRANSFUSION_REACTION
    - POSTTRANSFUSION_PURPURA
    - SYMPTOMS_MOST_LIKELY_DUE_TO_VOLUME_OVERLOAD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0514
    """

    ABO_INCOMPATIBLE_TRANSFUSION_REACTION = "ABOINC"
    """ABO Incompatible Transfusion Reaction"""
    ACUTE_HEMOLYTIC_TRANSFUSION_REACTION = "ACUTHEHTR"
    """Acute Hemolytic Transfusion Reaction"""
    ALLERGIC_REACTION_FIRST = "ALLERGIC1"
    """Allergic Reaction - First"""
    ALLERGIC_REACTION_RECURRENT = "ALLERGIC2"
    """Allergic Reaction - Recurrent"""
    ALLERGIC_REACTION_REPEATING = "ALLERGICR"
    """Allergic Reaction - Repeating"""
    ANAPHYLACTIC_REACTION = "ANAPHYLAC"
    """Anaphylactic Reaction"""
    REACTION_TO_BACTERIAL_CONTAMINATION = "BACTCONTAM"
    """Reaction to Bacterial Contamination"""
    DELAYED_HEMOLYTIC_TRANSFUSION_REACTION = "DELAYEDHTR"
    """Delayed Hemolytic Transfusion Reaction"""
    DELAYED_SEROLOGICAL_TRANSFUSION_REACTION = "DELAYEDSTR"
    """Delayed Serological Transfusion Reaction"""
    GRAFT_VS_HOST_DISEASE_TRANSFUSION_ASSOCIATED = "GVHD"
    """Graft vs Host Disease - Transfusion - Associated"""
    NON_HEMOLYTIC_HYPOTENSIVE_REACTION = "HYPOTENS"
    """Non-hemolytic Hypotensive Reaction"""
    NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_FIRST = "NONHTR1"
    """Non-Hemolytic Fever Chill Transfusion Reaction - First"""
    NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_RECURRENT = "NONHTR2"
    """Non-Hemolytic Fever Chill Transfusion Reaction - Recurrent"""
    NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_REPEATING = "NONHTRREC"
    """Non-Hemolytic Fever Chill Transfusion Reaction - Repeating"""
    NON_IMMUNE_HEMOLYSIS = "NONIMMUNE"
    """Non-Immune Hemolysis"""
    NON_SPECIFIC_NON_HEMOLYTIC_TRANSFUSION_REACTION = "NONSPEC"
    """Non-Specific, Non-Hemolytic Transfusion Reaction"""
    NO_EVIDENCE_OF_TRANSFUSION_REACTION = "NORXN"
    """No Evidence of Transfusion Reaction"""
    POSTTRANSFUSION_PURPURA = "PTP"
    """Posttransfusion Purpura"""
    SYMPTOMS_MOST_LIKELY_DUE_TO_VOLUME_OVERLOAD = "VOLOVER"
    """Symptoms most likely due to volume overload"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TransfusionAdverseReaction.ABO_INCOMPATIBLE_TRANSFUSION_REACTION: "ABO Incompatible Transfusion Reaction",
    TransfusionAdverseReaction.ACUTE_HEMOLYTIC_TRANSFUSION_REACTION: "Acute Hemolytic Transfusion Reaction",
    TransfusionAdverseReaction.ALLERGIC_REACTION_FIRST: "Allergic Reaction - First",
    TransfusionAdverseReaction.ALLERGIC_REACTION_RECURRENT: "Allergic Reaction - Recurrent",
    TransfusionAdverseReaction.ALLERGIC_REACTION_REPEATING: "Allergic Reaction - Repeating",
    TransfusionAdverseReaction.ANAPHYLACTIC_REACTION: "Anaphylactic Reaction",
    TransfusionAdverseReaction.REACTION_TO_BACTERIAL_CONTAMINATION: "Reaction to Bacterial Contamination",
    TransfusionAdverseReaction.DELAYED_HEMOLYTIC_TRANSFUSION_REACTION: "Delayed Hemolytic Transfusion Reaction",
    TransfusionAdverseReaction.DELAYED_SEROLOGICAL_TRANSFUSION_REACTION: "Delayed Serological Transfusion Reaction",
    TransfusionAdverseReaction.GRAFT_VS_HOST_DISEASE_TRANSFUSION_ASSOCIATED: "Graft vs Host Disease - Transfusion - Associated",
    TransfusionAdverseReaction.NON_HEMOLYTIC_HYPOTENSIVE_REACTION: "Non-hemolytic Hypotensive Reaction",
    TransfusionAdverseReaction.NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_FIRST: "Non-Hemolytic Fever Chill Transfusion Reaction - First",
    TransfusionAdverseReaction.NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_RECURRENT: "Non-Hemolytic Fever Chill Transfusion Reaction - Recurrent",
    TransfusionAdverseReaction.NON_HEMOLYTIC_FEVER_CHILL_TRANSFUSION_REACTION_REPEATING: "Non-Hemolytic Fever Chill Transfusion Reaction - Repeating",
    TransfusionAdverseReaction.NON_IMMUNE_HEMOLYSIS: "Non-Immune Hemolysis",
    TransfusionAdverseReaction.NON_SPECIFIC_NON_HEMOLYTIC_TRANSFUSION_REACTION: "Non-Specific, Non-Hemolytic Transfusion Reaction",
    TransfusionAdverseReaction.NO_EVIDENCE_OF_TRANSFUSION_REACTION: "No Evidence of Transfusion Reaction",
    TransfusionAdverseReaction.POSTTRANSFUSION_PURPURA: "Posttransfusion Purpura",
    TransfusionAdverseReaction.SYMPTOMS_MOST_LIKELY_DUE_TO_VOLUME_OVERLOAD: "Symptoms most likely due to volume overload",
}
