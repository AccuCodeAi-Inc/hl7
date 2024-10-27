from ...base import HL7Table

"""
HL7 Version: 2.5.1
Additive/Preservative - 0371
Table Type: HL7
"""


class AdditiveOrPreservative(HL7Table):
    """
    Additive/Preservative - 0371 // HL7 table type
    - ACD_SOLUTION_A
    - ACD_SOLUTION_B
    - ACETIC_ACID
    - AMIES_TRANSPORT_MEDIUM
    - BACTERIAL_TRANSPORT_MEDIUM
    - BUFFERED_10_PERCENT_FORMALIN
    - BORATE_BORIC_ACID
    - BOUINS_SOLUTION
    - BUFFERED_SKIM_MILK
    - _3_2_PERCENT_CITRATE
    - _3_8_PERCENT_CITRATE
    - CARSONS_MODIFIED_10_PERCENT_FORMALIN
    - CARY_BLAIR_MEDIUM
    - CHLAMYDIA_TRANSPORT_MEDIUM
    - CTAD
    - POTASSIUM_OR_K_EDTA
    - POTASSIUM_OR_K_EDTA_15_PERCENT
    - POTASSIUM_OR_K_EDTA_7_5_PERCENT
    - SODIUM_OR_NA_EDTA
    - ENTERIC_BACTERIA_TRANSPORT_MEDIUM
    - ENTERIC_PLUS
    - _10_PERCENT_FORMALIN
    - THROMBIN_NIH_SOYBEAN_TRYPSIN_INHIBITOR
    - SODIUM_FLUORIDE_10MG
    - SODIUM_FLUORIDE_100MG
    - _6N_HCL
    - AMMONIUM_HEPARIN
    - LITHIUM_OR_LI_HEPARIN
    - SODIUM_OR_NA_HEPARIN
    - NITRIC_ACID
    - JONES_KENDRICK_MEDIUM
    - KARNOVSKYS_FIXATIVE
    - POTASSIUM_OXALATE
    - LITHIUM_IODOACETATE
    - M4
    - M4_RT
    - M5
    - MICHELS_TRANSPORT_MEDIUM
    - MMD_TRANSPORT_MEDIUM
    - SODIUM_FLUORIDE
    - SODIUM_POLYANETHOL_SULFONATE_0_35_PERCENT_IN_0_85_PERCENT_SODIUM_CHLORIDE
    - NONE
    - PAGESS_SALINE
    - PHENOL
    - PVA
    - REAGAN_LOWE_MEDIUM
    - SILICEOUS_EARTH_12_MG
    - SPS
    - SERUM_SEPARATOR_TUBE
    - STUART_TRANSPORT_MEDIUM
    - THROMBIN
    - THYMOL
    - THYOGLYCOLLATE_BROTH
    - TOLUENE
    - UREAPLASMA_TRANSPORT_MEDIUM
    - VIRAL_TRANSPORT_MEDIUM
    - BUFFERED_CITRATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0371
    """

    ACD_SOLUTION_A = "ACDA"  # Yellow top tube
    """ACD Solution A"""
    ACD_SOLUTION_B = "ACDB"  # Yellow top tube
    """ACD Solution B"""
    ACETIC_ACID = "ACET"  # Urine preservative
    """Acetic Acid"""
    AMIES_TRANSPORT_MEDIUM = "AMIES"  # Protozoa
    """Amies transport medium"""
    BACTERIAL_TRANSPORT_MEDIUM = "BACTM"  # Microbiological culture
    """Bacterial Transport medium"""
    BUFFERED_10_PERCENT_FORMALIN = "BF10"  # Tissue
    """Buffered 10% formalin"""
    BORATE_BORIC_ACID = "BOR"  # 24HR Urine Additive
    """Borate Boric Acid"""
    BOUINS_SOLUTION = "BOUIN"  # Tissue
    """Bouins solution"""
    BUFFERED_SKIM_MILK = "BSKM"  # Viral isolation
    """Buffered skim milk"""
    _3_2_PERCENT_CITRATE = "C32"  # Blue top tube
    """3.2% Citrate"""
    _3_8_PERCENT_CITRATE = "C38"  # Blue top tube
    """3.8% Citrate"""
    CARSONS_MODIFIED_10_PERCENT_FORMALIN = "CARS"  # Tissue
    """Carsons Modified 10% formalin"""
    CARY_BLAIR_MEDIUM = "CARY"  # Stool Cultures
    """Cary Blair Medium"""
    CHLAMYDIA_TRANSPORT_MEDIUM = "CHLTM"  # Chlamydia culture
    """Chlamydia transport medium"""
    CTAD = "CTAD"  # Blue top tube
    """CTAD (this should be spelled out if not universally understood)"""
    POTASSIUM_OR_K_EDTA = "EDTK"  # Deprecated. Replaced by EDTK15 and EDTK75
    """Potassium/K EDTA"""
    POTASSIUM_OR_K_EDTA_15_PERCENT = "EDTK15"  # Purple top tube
    """Potassium/K EDTA 15%"""
    POTASSIUM_OR_K_EDTA_7_5_PERCENT = "EDTK75"  # Purple top tube
    """Potassium/K EDTA 7.5%"""
    SODIUM_OR_NA_EDTA = "EDTN"  # Dark Blue top tube
    """Sodium/Na EDTA"""
    ENTERIC_BACTERIA_TRANSPORT_MEDIUM = "ENT"  # Bacterial culture
    """Enteric bacteria transport medium"""
    ENTERIC_PLUS = "ENT+"  # Stool Cultures
    """Enteric plus"""
    _10_PERCENT_FORMALIN = "F10"  # Tissue preservative
    """10% Formalin"""
    THROMBIN_NIH_SOYBEAN_TRYPSIN_INHIBITOR = "FDP"  # Dark Blue top tube
    """Thrombin NIH; soybean trypsin inhibitor (Fibrin Degradation Products)"""
    SODIUM_FLUORIDE_10MG = "FL10"  # Urine
    """Sodium Fluoride, 10mg"""
    SODIUM_FLUORIDE_100MG = "FL100"  # Urine
    """Sodium Fluoride, 100mg"""
    _6N_HCL = "HCL6"  # 24 HR Urine Additive
    """6N HCL"""
    AMMONIUM_HEPARIN = "HEPA"  # Green top tube
    """Ammonium heparin"""
    LITHIUM_OR_LI_HEPARIN = "HEPL"  # Green top tube
    """Lithium/Li Heparin"""
    SODIUM_OR_NA_HEPARIN = "HEPN"  # Green top tube
    """Sodium/Na Heparin"""
    NITRIC_ACID = "HNO3"  # Urine
    """Nitric Acid"""
    JONES_KENDRICK_MEDIUM = "JKM"  # Bordetella pertussis
    """Jones Kendrick Medium"""
    KARNOVSKYS_FIXATIVE = "KARN"  # Tissue
    """Karnovskys fixative"""
    POTASSIUM_OXALATE = "KOX"  # Gray top tube
    """Potassium Oxalate"""
    LITHIUM_IODOACETATE = "LIA"  # Gray top tube
    """Lithium iodoacetate"""
    M4 = "M4"  # Microbiological culture
    """M4"""
    M4_RT = "M4RT"  # Microbiological culture
    """M4-RT"""
    M5 = "M5"  # Microbiological culture
    """M5"""
    MICHELS_TRANSPORT_MEDIUM = "MICHTM"  # IF tests
    """Michels transport medium"""
    MMD_TRANSPORT_MEDIUM = "MMDTM"  # Immunofluorescence
    """MMD transport medium"""
    SODIUM_FLUORIDE = "NAF"  # Gray top tube
    """Sodium Fluoride"""
    SODIUM_POLYANETHOL_SULFONATE_0_35_PERCENT_IN_0_85_PERCENT_SODIUM_CHLORIDE = (
        "NAPS"  # Yellow (Blood Culture)
    )
    """Sodium polyanethol sulfonate 0.35% in 0.85% sodium chloride"""
    NONE = "NONE"  # Red or Pink top tube
    """None"""
    PAGESS_SALINE = "PAGE"  # Acanthaoemba
    """Pagess Saline"""
    PHENOL = "PHENOL"  # 24 Hr Urine Additive
    """Phenol"""
    PVA = "PVA"  # O&amp;P
    """PVA (polyvinylalcohol)"""
    REAGAN_LOWE_MEDIUM = "RLM"  # Bordetella pertussis cultures
    """Reagan Lowe Medium"""
    SILICEOUS_EARTH_12_MG = "SILICA"  # Gray top tube
    """Siliceous earth, 12 mg"""
    SPS = "SPS"  # Anticoagulant w/o bacteriocidal properties
    """SPS(this should be spelled out if not universally understood)"""
    SERUM_SEPARATOR_TUBE = "SST"  # ‘Tiger’ Top tube
    """Serum Separator Tube (Polymer Gel)"""
    STUART_TRANSPORT_MEDIUM = "STUTM"  # Bacterial culture
    """Stuart transport medium"""
    THROMBIN = "THROM"  # Orange or Grey/Yellow (STAT Chem)
    """Thrombin"""
    THYMOL = "THYMOL"  # 24 Hr Urine Additive
    """Thymol"""
    THYOGLYCOLLATE_BROTH = "THYO"  # Bacterial Isolation
    """Thyoglycollate broth"""
    TOLUENE = "TOLU"  # 24 Hr Urine Additive
    """Toluene"""
    UREAPLASMA_TRANSPORT_MEDIUM = "URETM"  # Ureaplasma culture
    """Ureaplasma transport medium"""
    VIRAL_TRANSPORT_MEDIUM = "VIRTM"  # Virus cultures
    """Viral Transport medium"""
    BUFFERED_CITRATE = "WEST"  # Black top tube
    """Buffered Citrate (Westergren Sedimentation Rate)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AdditiveOrPreservative.ACD_SOLUTION_A: "ACD Solution A",
    AdditiveOrPreservative.ACD_SOLUTION_B: "ACD Solution B",
    AdditiveOrPreservative.ACETIC_ACID: "Acetic Acid",
    AdditiveOrPreservative.AMIES_TRANSPORT_MEDIUM: "Amies transport medium",
    AdditiveOrPreservative.BACTERIAL_TRANSPORT_MEDIUM: "Bacterial Transport medium",
    AdditiveOrPreservative.BUFFERED_10_PERCENT_FORMALIN: "Buffered 10% formalin",
    AdditiveOrPreservative.BORATE_BORIC_ACID: "Borate Boric Acid",
    AdditiveOrPreservative.BOUINS_SOLUTION: "Bouins solution",
    AdditiveOrPreservative.BUFFERED_SKIM_MILK: "Buffered skim milk",
    AdditiveOrPreservative._3_2_PERCENT_CITRATE: "3.2% Citrate",
    AdditiveOrPreservative._3_8_PERCENT_CITRATE: "3.8% Citrate",
    AdditiveOrPreservative.CARSONS_MODIFIED_10_PERCENT_FORMALIN: "Carsons Modified 10% formalin",
    AdditiveOrPreservative.CARY_BLAIR_MEDIUM: "Cary Blair Medium",
    AdditiveOrPreservative.CHLAMYDIA_TRANSPORT_MEDIUM: "Chlamydia transport medium",
    AdditiveOrPreservative.CTAD: "CTAD (this should be spelled out if not universally understood)",
    AdditiveOrPreservative.POTASSIUM_OR_K_EDTA: "Potassium/K EDTA",
    AdditiveOrPreservative.POTASSIUM_OR_K_EDTA_15_PERCENT: "Potassium/K EDTA 15%",
    AdditiveOrPreservative.POTASSIUM_OR_K_EDTA_7_5_PERCENT: "Potassium/K EDTA 7.5%",
    AdditiveOrPreservative.SODIUM_OR_NA_EDTA: "Sodium/Na EDTA",
    AdditiveOrPreservative.ENTERIC_BACTERIA_TRANSPORT_MEDIUM: "Enteric bacteria transport medium",
    AdditiveOrPreservative.ENTERIC_PLUS: "Enteric plus",
    AdditiveOrPreservative._10_PERCENT_FORMALIN: "10% Formalin",
    AdditiveOrPreservative.THROMBIN_NIH_SOYBEAN_TRYPSIN_INHIBITOR: "Thrombin NIH; soybean trypsin inhibitor (Fibrin Degradation Products)",
    AdditiveOrPreservative.SODIUM_FLUORIDE_10MG: "Sodium Fluoride, 10mg",
    AdditiveOrPreservative.SODIUM_FLUORIDE_100MG: "Sodium Fluoride, 100mg",
    AdditiveOrPreservative._6N_HCL: "6N HCL",
    AdditiveOrPreservative.AMMONIUM_HEPARIN: "Ammonium heparin",
    AdditiveOrPreservative.LITHIUM_OR_LI_HEPARIN: "Lithium/Li Heparin",
    AdditiveOrPreservative.SODIUM_OR_NA_HEPARIN: "Sodium/Na Heparin",
    AdditiveOrPreservative.NITRIC_ACID: "Nitric Acid",
    AdditiveOrPreservative.JONES_KENDRICK_MEDIUM: "Jones Kendrick Medium",
    AdditiveOrPreservative.KARNOVSKYS_FIXATIVE: "Karnovskys fixative",
    AdditiveOrPreservative.POTASSIUM_OXALATE: "Potassium Oxalate",
    AdditiveOrPreservative.LITHIUM_IODOACETATE: "Lithium iodoacetate",
    AdditiveOrPreservative.M4: "M4",
    AdditiveOrPreservative.M4_RT: "M4-RT",
    AdditiveOrPreservative.M5: "M5",
    AdditiveOrPreservative.MICHELS_TRANSPORT_MEDIUM: "Michels transport medium",
    AdditiveOrPreservative.MMD_TRANSPORT_MEDIUM: "MMD transport medium",
    AdditiveOrPreservative.SODIUM_FLUORIDE: "Sodium Fluoride",
    AdditiveOrPreservative.SODIUM_POLYANETHOL_SULFONATE_0_35_PERCENT_IN_0_85_PERCENT_SODIUM_CHLORIDE: "Sodium polyanethol sulfonate 0.35% in 0.85% sodium chloride",
    AdditiveOrPreservative.NONE: "None",
    AdditiveOrPreservative.PAGESS_SALINE: "Pagess Saline",
    AdditiveOrPreservative.PHENOL: "Phenol",
    AdditiveOrPreservative.PVA: "PVA (polyvinylalcohol)",
    AdditiveOrPreservative.REAGAN_LOWE_MEDIUM: "Reagan Lowe Medium",
    AdditiveOrPreservative.SILICEOUS_EARTH_12_MG: "Siliceous earth, 12 mg",
    AdditiveOrPreservative.SPS: "SPS(this should be spelled out if not universally understood)",
    AdditiveOrPreservative.SERUM_SEPARATOR_TUBE: "Serum Separator Tube (Polymer Gel)",
    AdditiveOrPreservative.STUART_TRANSPORT_MEDIUM: "Stuart transport medium",
    AdditiveOrPreservative.THROMBIN: "Thrombin",
    AdditiveOrPreservative.THYMOL: "Thymol",
    AdditiveOrPreservative.THYOGLYCOLLATE_BROTH: "Thyoglycollate broth",
    AdditiveOrPreservative.TOLUENE: "Toluene",
    AdditiveOrPreservative.UREAPLASMA_TRANSPORT_MEDIUM: "Ureaplasma transport medium",
    AdditiveOrPreservative.VIRAL_TRANSPORT_MEDIUM: "Viral Transport medium",
    AdditiveOrPreservative.BUFFERED_CITRATE: "Buffered Citrate (Westergren Sedimentation Rate)",
}
