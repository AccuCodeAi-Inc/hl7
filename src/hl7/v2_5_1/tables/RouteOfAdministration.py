from ...base import HL7Table

"""
HL7 Version: 2.5.1
Route of Administration - 0162
Table Type: User
"""


class RouteOfAdministration(HL7Table):
    """
    Route of Administration - 0162 // User table type
    - APPLY_EXTERNALLY
    - BUCCAL
    - DENTAL
    - EPIDURAL
    - ENDOTRACHIAL_TUBE_STAR
    - GASTROSTOMY_TUBE
    - GU_IRRIGANT
    - INTRA_ARTERIAL
    - INTRABURSAL
    - INTRACARDIAC
    - INTRACERVICAL
    - INTRADERMAL
    - INHALATION
    - INTRAHEPATIC_ARTERY
    - INTRAMUSCULAR
    - IMMERSE
    - INTRANASAL
    - INTRAOCULAR
    - INTRAPERITONEAL
    - INTRASYNOVIAL
    - INTRATHECAL
    - INTRAUTERINE
    - INTRAVENOUS
    - MUCOUS_MEMBRANE
    - MOUTH_OR_THROAT
    - NASOGASTRIC
    - NASAL_PRONGS_STAR
    - NASAL
    - NASOTRACHIAL_TUBE
    - OPHTHALMIC
    - OTIC
    - OTHER_OR_MISCELLANEOUS
    - PERFUSION
    - ORAL
    - RECTAL
    - REBREATHER_MASK_STAR
    - SUBCUTANEOUS
    - SOAKED_DRESSING
    - SUBLINGUAL
    - TRANSDERMAL
    - TRANSLINGUAL
    - TOPICAL
    - TRACHEOSTOMY_STAR
    - URETHRAL
    - VAGINAL
    - VENTIMASK
    - WOUND
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0162
    """

    APPLY_EXTERNALLY = "AP"
    """Apply Externally"""
    BUCCAL = "B"
    """Buccal"""
    DENTAL = "DT"
    """Dental"""
    EPIDURAL = "EP"
    """Epidural"""
    ENDOTRACHIAL_TUBE_STAR = (
        "ET"  # used primarily for respiratory therapy and anesthesia delivery
    )
    """Endotrachial Tube*"""
    GASTROSTOMY_TUBE = "GTT"
    """Gastrostomy Tube"""
    GU_IRRIGANT = "GU"
    """GU Irrigant"""
    INTRA_ARTERIAL = "IA"
    """Intra-arterial"""
    INTRABURSAL = "IB"
    """Intrabursal"""
    INTRACARDIAC = "IC"
    """Intracardiac"""
    INTRACERVICAL = "ICV"
    """Intracervical (uterus)"""
    INTRADERMAL = "ID"
    """Intradermal"""
    INHALATION = "IH"
    """Inhalation"""
    INTRAHEPATIC_ARTERY = "IHA"
    """Intrahepatic Artery"""
    INTRAMUSCULAR = "IM"
    """Intramuscular"""
    IMMERSE = "IMR"
    """Immerse (Soak) Body Part"""
    INTRANASAL = "IN"
    """Intranasal"""
    INTRAOCULAR = "IO"
    """Intraocular"""
    INTRAPERITONEAL = "IP"
    """Intraperitoneal"""
    INTRASYNOVIAL = "IS"
    """Intrasynovial"""
    INTRATHECAL = "IT"
    """Intrathecal"""
    INTRAUTERINE = "IU"
    """Intrauterine"""
    INTRAVENOUS = "IV"
    """Intravenous"""
    MUCOUS_MEMBRANE = "MM"
    """Mucous Membrane"""
    MOUTH_OR_THROAT = "MTH"
    """Mouth/Throat"""
    NASOGASTRIC = "NG"
    """Nasogastric"""
    NASAL_PRONGS_STAR = (
        "NP"  # used primarily for respiratory therapy and anesthesia delivery
    )
    """Nasal Prongs*"""
    NASAL = "NS"
    """Nasal"""
    NASOTRACHIAL_TUBE = "NT"
    """Nasotrachial Tube"""
    OPHTHALMIC = "OP"
    """Ophthalmic"""
    OTIC = "OT"
    """Otic"""
    OTHER_OR_MISCELLANEOUS = "OTH"
    """Other/Miscellaneous"""
    PERFUSION = "PF"
    """Perfusion"""
    ORAL = "PO"
    """Oral"""
    RECTAL = "PR"
    """Rectal"""
    REBREATHER_MASK_STAR = (
        "RM"  # used primarily for respiratory therapy and anesthesia delivery
    )
    """Rebreather Mask*"""
    SUBCUTANEOUS = "SC"
    """Subcutaneous"""
    SOAKED_DRESSING = "SD"
    """Soaked Dressing"""
    SUBLINGUAL = "SL"
    """Sublingual"""
    TRANSDERMAL = "TD"
    """Transdermal"""
    TRANSLINGUAL = "TL"
    """Translingual"""
    TOPICAL = "TP"
    """Topical"""
    TRACHEOSTOMY_STAR = (
        "TRA"  # used primarily for respiratory therapy and anesthesia delivery
    )
    """Tracheostomy*"""
    URETHRAL = "UR"
    """Urethral"""
    VAGINAL = "VG"
    """Vaginal"""
    VENTIMASK = "VM"
    """Ventimask"""
    WOUND = "WND"
    """Wound"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RouteOfAdministration.APPLY_EXTERNALLY: "Apply Externally",
    RouteOfAdministration.BUCCAL: "Buccal",
    RouteOfAdministration.DENTAL: "Dental",
    RouteOfAdministration.EPIDURAL: "Epidural",
    RouteOfAdministration.ENDOTRACHIAL_TUBE_STAR: "Endotrachial Tube*",
    RouteOfAdministration.GASTROSTOMY_TUBE: "Gastrostomy Tube",
    RouteOfAdministration.GU_IRRIGANT: "GU Irrigant",
    RouteOfAdministration.INTRA_ARTERIAL: "Intra-arterial",
    RouteOfAdministration.INTRABURSAL: "Intrabursal",
    RouteOfAdministration.INTRACARDIAC: "Intracardiac",
    RouteOfAdministration.INTRACERVICAL: "Intracervical (uterus)",
    RouteOfAdministration.INTRADERMAL: "Intradermal",
    RouteOfAdministration.INHALATION: "Inhalation",
    RouteOfAdministration.INTRAHEPATIC_ARTERY: "Intrahepatic Artery",
    RouteOfAdministration.INTRAMUSCULAR: "Intramuscular",
    RouteOfAdministration.IMMERSE: "Immerse (Soak) Body Part",
    RouteOfAdministration.INTRANASAL: "Intranasal",
    RouteOfAdministration.INTRAOCULAR: "Intraocular",
    RouteOfAdministration.INTRAPERITONEAL: "Intraperitoneal",
    RouteOfAdministration.INTRASYNOVIAL: "Intrasynovial",
    RouteOfAdministration.INTRATHECAL: "Intrathecal",
    RouteOfAdministration.INTRAUTERINE: "Intrauterine",
    RouteOfAdministration.INTRAVENOUS: "Intravenous",
    RouteOfAdministration.MUCOUS_MEMBRANE: "Mucous Membrane",
    RouteOfAdministration.MOUTH_OR_THROAT: "Mouth/Throat",
    RouteOfAdministration.NASOGASTRIC: "Nasogastric",
    RouteOfAdministration.NASAL_PRONGS_STAR: "Nasal Prongs*",
    RouteOfAdministration.NASAL: "Nasal",
    RouteOfAdministration.NASOTRACHIAL_TUBE: "Nasotrachial Tube",
    RouteOfAdministration.OPHTHALMIC: "Ophthalmic",
    RouteOfAdministration.OTIC: "Otic",
    RouteOfAdministration.OTHER_OR_MISCELLANEOUS: "Other/Miscellaneous",
    RouteOfAdministration.PERFUSION: "Perfusion",
    RouteOfAdministration.ORAL: "Oral",
    RouteOfAdministration.RECTAL: "Rectal",
    RouteOfAdministration.REBREATHER_MASK_STAR: "Rebreather Mask*",
    RouteOfAdministration.SUBCUTANEOUS: "Subcutaneous",
    RouteOfAdministration.SOAKED_DRESSING: "Soaked Dressing",
    RouteOfAdministration.SUBLINGUAL: "Sublingual",
    RouteOfAdministration.TRANSDERMAL: "Transdermal",
    RouteOfAdministration.TRANSLINGUAL: "Translingual",
    RouteOfAdministration.TOPICAL: "Topical",
    RouteOfAdministration.TRACHEOSTOMY_STAR: "Tracheostomy*",
    RouteOfAdministration.URETHRAL: "Urethral",
    RouteOfAdministration.VAGINAL: "Vaginal",
    RouteOfAdministration.VENTIMASK: "Ventimask",
    RouteOfAdministration.WOUND: "Wound",
}
