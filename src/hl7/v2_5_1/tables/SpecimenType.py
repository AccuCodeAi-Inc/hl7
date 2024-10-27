from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Type - 0487
Table Type: HL7
"""


class SpecimenType(HL7Table):
    """
    Specimen Type - 0487 // HL7 table type
    - ABSCESS
    - TISSUE_ACNE
    - FLUID_ACNE
    - AIR_SAMPLE
    - ALLOGRAFT
    - AMPUTATION
    - CATHETER_TIP_ANGIO
    - CATHETER_TIP_ARTERIAL
    - SERUM_ACUTE
    - ASPIRATE
    - ENVIRONMENT_ATTEST
    - ENVIRONMENTAL_AUTOCLAVE_CAPSULE
    - AUTOPSY
    - BLOOD_BAG
    - CYST_BAKERS
    - BITE
    - BLEB
    - BLISTER
    - BOIL
    - BONE
    - BOWEL_CONTENTS
    - BLOOD_PRODUCT_UNIT
    - BURN
    - BRUSH
    - BREATH
    - BRUSHING
    - BUBO
    - BULLA_OR_BULLAE
    - BIOPSY
    - CALCULUS
    - CARBUNCLE
    - CATHETER
    - BITE_CAT
    - CLIPPINGS
    - CONJUNCTIVA
    - COLOSTRUM
    - BIOSPY_CONE
    - SCRATCH_CAT
    - SERUM_CONVALESCENT
    - CATHETER_INSERTION_SITE
    - FLUID_CYSTOSTOMY_TUBE
    - FLUID_CYST
    - BLOOD_CELL_SAVER
    - CATHETER_TIP
    - SITE_CVP
    - CATHETER_TIP_CVP
    - NODULE_CYSTIC
    - CYST
    - BITE_DOG
    - SPUTUM_DEEP_COUGH
    - ULCER_DECUBITUS
    - ENVIRONMENTAL_WATER
    - DIALYSATE
    - DISCHARGE
    - DIVERTICULUM
    - DRAIN
    - DRAINAGE_TUBE
    - DRAINAGE_PENROSE
    - EAR_WAX
    - BRUSH_ESOPHAGEAL
    - ENVIRONMENTAL_EYE_WASH
    - ENVIRONMENTAL_EFFLUENT
    - EFFUSION
    - ENVIRONMENTAL_FOOD
    - ENVIRONMENTAL_ISOLETTE
    - ELECTRODE
    - ENVIRONMENTAL_UNIDENTIFIED_SUBSTANCE
    - ENVIRONMENTAL_OTHER_SUBSTANCE
    - ENVIRONMENTAL_SOIL
    - ENVIRONMENTAL_SOLUTION
    - ASPIRATE_ENDOTRACH
    - CATHETER_TIP_ENDOTRACHEAL
    - TUBE_ENDOTRACHEAL
    - ENVIRONMENTAL_WHIRLPOOL
    - GAS_EXHALED
    - SHUNT_EXTERNAL
    - EXUDATE
    - FAW
    - BLOOD_FETAL
    - FLUID_ABDOMEN
    - FISTULA
    - FLUID_OTHER
    - FILTER
    - FLUID_BODY_UNSP
    - FLUID
    - CATHETER_TIP_FOLEY
    - FLUID_RESPIRATORY
    - SCALP_FETAL
    - FURUNCLE
    - GAS
    - ASPIRATE_GASTRIC
    - ANTRUM_GASTRIC
    - BRUSHING_GASTRIC
    - DRAINAGE_GASTRIC
    - FLUID_OR_CONTENTS_GASTRIC
    - GENITAL_VAGINAL
    - GRAFT
    - GRANULOMA
    - CATHETER_GROSHONG
    - SOLUTION_GASTROSTOMY
    - BIOPSY_GASTRIC
    - TUBE_GASTRIC
    - DRAINAGE_TUBE_DRAINAGE
    - BITE_HUMAN
    - BLOOD_AUTOPSY
    - CATHETER_TIP_HEMAQUIT
    - CATHETER_TIP_HEMOVAC
    - TISSUE_HERNIATED
    - DRAIN_HEMOVAC
    - CATHETER_HICKMAN
    - FLUID_HYDROCELE
    - BITE_INSECT
    - CYST_INCLUSION
    - CATHETER_TIP_INDWELLING
    - GAS_INHALED
    - DRAINAGE_ILEOSTOMY
    - SOURCE_OF_SPECIMEN_IS_ILLEGIBLE
    - IMPLANT
    - SITE_INCISION_OR_SURGICAL
    - INFILTRATE
    - INSECT
    - CATHETER_TIP_INTRODUCER
    - INTUBATION_TUBE
    - INTRAUTERINE_DEVICE
    - CATHETER_TIP_IV
    - FLUID_IV
    - TUBING_TIP_IV
    - DRAINAGE_JEJUNAL
    - FLUID_JOINT
    - DRAINAGE_JACKSON_PRATT
    - LAVAGE
    - FLUID_KIDNEY
    - LAVAGE_BRONHIAL
    - LAVAGE_GASTRIC
    - LAVAGE_PERITONEAL
    - LAVAGE_PRE_BRONCH
    - CONTACT_LENS
    - CONTACT_LENS_CASE
    - LESION
    - LIQUID_UNSPECIFIED
    - LIQUID_OTHER
    - FLUID_LUMBAR_SAC
    - CATHETER_TIP_MAKURKOUR
    - MASS
    - BLOOD_MENSTRUAL
    - MUCOSA
    - MUCUS
    - DRAINAGE_NASAL
    - NEEDLE
    - SITE_NEPHROSTOMY
    - ASPIRATE_NASOGASTRIC
    - DRAINAGE_NASOGASTRIC
    - SITE_NASO_OR_GASTRIC
    - NODULE
    - SECRETION_NASAL
    - OTHER
    - LESION_ORAL
    - SOURCE_OTHER
    - PACEMAKER
    - FLUID_PERICARDIAL
    - SITE_PERITONEAL_DIALYSIS
    - SITE_PERITONEAL_DIALYSIS_TUNNEL
    - ABSCESS_PELVIC
    - LESION_PENILE
    - ABSCESS_PERIANAL
    - CYST_PILONIDAL
    - SITE_PIN
    - SITE_PACEMAKER_INSETION
    - PLANT_MATERIAL
    - PLASMA
    - PLASMA_BAG
    - SERUM_PEAK_LEVEL
    - DRAINAGE_PENILE
    - POLYPS
    - GRAFT_SITE_POPLITEAL
    - GRAFT_POPLITEAL
    - SITE_POPLITEAL_VEIN
    - CATHETER_PORTA
    - PLASMA_PLATELET_POOR
    - PROSTHETIC_DEVICE
    - PLASMA_PLATELET_RICH
    - PSEUDOCYST
    - WOUND_PUNCTURE
    - PUS
    - PUSTULE
    - PUST
    - QUALITY_CONTROL
    - URINE_RANDOM
    - BITE_REPTILE
    - DRAINAGE_RECTAL
    - ABSCESS_RECTAL
    - CYST_RENAL
    - FLUID_RENAL_CYST
    - RESPIRATORY
    - SALIVA
    - TISSUE_KELOID
    - CATHETER_TIP_SUBCLAVIAN
    - ABSCESS_SCROTAL
    - SECRETION
    - SERUM
    - SITE_SHUNT
    - FLUID_SHUNT
    - SHUNT
    - SITE
    - BIOPSY_SKIN
    - SKIN
    - MASS_SUB_MANDIBULAR
    - FLUID_SYNOVIAL
    - SPERMATOZOA
    - CATHETER_TIP_SUPRAPUBIC
    - CATHETHER_TIP_SUPRAPUBIC
    - ENVIRONMENTAL_SPORE_STRIP
    - SPUTUM
    - SPUTUM_COUGHED
    - SPUTUM_TRACHEAL_ASPIRATE
    - SPUTUM_SIMULATED
    - SPUTUM_INDUCTED
    - SPUTUM_SPONTANEOUS
    - ENVIRONMENTAL_STERRAD
    - STOOL_EQUALS_FECAL
    - STONE_KIDNEY
    - ABSCESS_SUBMANDIBULAR
    - ABSCESS_SUBMAXILLARY
    - DRAINAGE_SUMP
    - SUPRAPUBIC_TAP
    - SUTURE
    - CATHETER_TIP_SWAN_GANTZ
    - ASPIRATE_TRACHEAL
    - TISSUE
    - TISSUE_ULCER
    - CATHETHER_TIP_TRIPLE_LUMEN
    - SITE_TRACHEOSTOMY
    - TRANSUDATE
    - SERUM_TROUGH
    - ABSCESS_TESTICULAR
    - ASPIRATE_TRANSTRACHEAL
    - TUBES
    - TUMOR
    - SMEAR_TZANCK
    - SOURCE_UNIDENTIFIED
    - URINE
    - URINE_CLEAN_CATCH
    - URINE_BLADDER_WASHINGS
    - URINE_CATHETERIZED
    - URINE_MIDSTREAM
    - URINE_NEPHROSTOMY
    - URINE_PEDIBAG
    - URINE_CATHETER
    - URINE_CYSTOSCOPY
    - SOURCE_UNSPECIFIED
    - CATHETER_TIP_VAS
    - CATHETER_TIP_VENTRICULAR
    - VITREOUS_FLUID
    - VOMITUS
    - WASH
    - WASHING_E_G_BRONCHIAL_WASHING
    - WATER
    - BLOOD_WHOLE
    - WEN
    - WICK
    - WOUND
    - WOUND_ABSCESS
    - WOUND_DRAINAGE
    - WOUND_EXUDATE
    - WORM
    - WART
    - WWA
    - WWO
    - WWT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0487
    """

    ABSCESS = "ABS"
    """Abscess"""
    TISSUE_ACNE = "ACNE"
    """Tissue, Acne"""
    FLUID_ACNE = "ACNFLD"
    """Fluid, Acne"""
    AIR_SAMPLE = "AIRS"
    """Air Sample"""
    ALLOGRAFT = "ALL"
    """Allograft"""
    AMPUTATION = "AMP"
    """Amputation"""
    CATHETER_TIP_ANGIO = "ANGI"
    """Catheter Tip, Angio"""
    CATHETER_TIP_ARTERIAL = "ARTC"
    """Catheter Tip, Arterial"""
    SERUM_ACUTE = "ASERU"
    """Serum, Acute"""
    ASPIRATE = "ASP"
    """Aspirate"""
    ENVIRONMENT_ATTEST = "ATTE"
    """Environment, Attest"""
    ENVIRONMENTAL_AUTOCLAVE_CAPSULE = "AUTOC"
    """Environmental, Autoclave Capsule"""
    AUTOPSY = "AUTP"
    """Autopsy"""
    BLOOD_BAG = "BBL"
    """Blood bag"""
    CYST_BAKERS = "BCYST"
    """Cyst, Bakers"""
    BITE = "BITE"
    """Bite"""
    BLEB = "BLEB"
    """Bleb"""
    BLISTER = "BLIST"
    """Blister"""
    BOIL = "BOIL"
    """Boil"""
    BONE = "BON"
    """Bone"""
    BOWEL_CONTENTS = "BOWL"
    """Bowel contents"""
    BLOOD_PRODUCT_UNIT = "BPU"
    """Blood product unit"""
    BURN = "BRN"
    """Burn"""
    BRUSH = "BRSH"
    """Brush"""
    BREATH = "BRTH"
    """Breath (use EXHLD)"""
    BRUSHING = "BRUS"
    """Brushing"""
    BUBO = "BUB"
    """Bubo"""
    BULLA_OR_BULLAE = "BULLA"
    """Bulla/Bullae"""
    BIOPSY = "BX"
    """Biopsy"""
    CALCULUS = "CALC"
    """Calculus (=Stone)"""
    CARBUNCLE = "CARBU"
    """Carbuncle"""
    CATHETER = "CAT"
    """Catheter"""
    BITE_CAT = "CBITE"
    """Bite, Cat"""
    CLIPPINGS = "CLIPP"
    """Clippings"""
    CONJUNCTIVA = "CNJT"
    """Conjunctiva"""
    COLOSTRUM = "COL"
    """Colostrum"""
    BIOSPY_CONE = "CONE"
    """Biospy, Cone"""
    SCRATCH_CAT = "CSCR"
    """Scratch, Cat"""
    SERUM_CONVALESCENT = "CSERU"
    """Serum, Convalescent"""
    CATHETER_INSERTION_SITE = "CSITE"
    """Catheter Insertion Site"""
    FLUID_CYSTOSTOMY_TUBE = "CSMY"
    """Fluid, Cystostomy Tube"""
    FLUID_CYST = "CST"
    """Fluid, Cyst"""
    BLOOD_CELL_SAVER = "CSVR"
    """Blood, Cell Saver"""
    CATHETER_TIP = "CTP"
    """Catheter tip"""
    SITE_CVP = "CVPS"
    """Site, CVP"""
    CATHETER_TIP_CVP = "CVPT"
    """Catheter Tip, CVP"""
    NODULE_CYSTIC = "CYN"
    """Nodule, Cystic"""
    CYST = "CYST"
    """Cyst"""
    BITE_DOG = "DBITE"
    """Bite, Dog"""
    SPUTUM_DEEP_COUGH = "DCS"
    """Sputum, Deep Cough"""
    ULCER_DECUBITUS = "DEC"
    """Ulcer, Decubitus"""
    ENVIRONMENTAL_WATER = "DEION"
    """Environmental, Water (Deionized)"""
    DIALYSATE = "DIA"
    """Dialysate"""
    DISCHARGE = "DISCHG"
    """Discharge"""
    DIVERTICULUM = "DIV"
    """Diverticulum"""
    DRAIN = "DRN"
    """Drain"""
    DRAINAGE_TUBE = "DRNG"
    """Drainage, Tube"""
    DRAINAGE_PENROSE = "DRNGP"
    """Drainage, Penrose"""
    EAR_WAX = "EARW"
    """Ear wax (cerumen)"""
    BRUSH_ESOPHAGEAL = "EBRUSH"
    """Brush, Esophageal"""
    ENVIRONMENTAL_EYE_WASH = "EEYE"
    """Environmental, Eye Wash"""
    ENVIRONMENTAL_EFFLUENT = "EFF"
    """Environmental, Effluent"""
    EFFUSION = "EFFUS"
    """Effusion"""
    ENVIRONMENTAL_FOOD = "EFOD"
    """Environmental, Food"""
    ENVIRONMENTAL_ISOLETTE = "EISO"
    """Environmental, Isolette"""
    ELECTRODE = "ELT"
    """Electrode"""
    ENVIRONMENTAL_UNIDENTIFIED_SUBSTANCE = "ENVIR"
    """Environmental, Unidentified Substance"""
    ENVIRONMENTAL_OTHER_SUBSTANCE = "EOTH"
    """Environmental, Other Substance"""
    ENVIRONMENTAL_SOIL = "ESOI"
    """Environmental, Soil"""
    ENVIRONMENTAL_SOLUTION = "ESOS"
    """Environmental, Solution (Sterile)"""
    ASPIRATE_ENDOTRACH = "ETA"
    """Aspirate, Endotrach"""
    CATHETER_TIP_ENDOTRACHEAL = "ETTP"
    """Catheter Tip, Endotracheal"""
    TUBE_ENDOTRACHEAL = "ETTUB"
    """Tube, Endotracheal"""
    ENVIRONMENTAL_WHIRLPOOL = "EWHI"
    """Environmental, Whirlpool"""
    GAS_EXHALED = "EXG"
    """Gas, exhaled (=breath)"""
    SHUNT_EXTERNAL = "EXS"
    """Shunt, External"""
    EXUDATE = "EXUDTE"
    """Exudate"""
    FAW = "FAW"
    """Environmental, Water (Well)"""
    BLOOD_FETAL = "FBLOOD"
    """Blood, Fetal"""
    FLUID_ABDOMEN = "FGA"
    """Fluid, Abdomen"""
    FISTULA = "FIST"
    """Fistula"""
    FLUID_OTHER = "FLD"
    """Fluid, Other"""
    FILTER = "FLT"
    """Filter"""
    FLUID_BODY_UNSP = "FLU"
    """Fluid, Body unsp"""
    FLUID = "FLUID"
    """Fluid"""
    CATHETER_TIP_FOLEY = "FOLEY"
    """Catheter Tip, Foley"""
    FLUID_RESPIRATORY = "FRS"
    """Fluid, Respiratory"""
    SCALP_FETAL = "FSCLP"
    """Scalp, Fetal"""
    FURUNCLE = "FUR"
    """Furuncle"""
    GAS = "GAS"
    """Gas"""
    ASPIRATE_GASTRIC = "GASA"
    """Aspirate, Gastric"""
    ANTRUM_GASTRIC = "GASAN"
    """Antrum, Gastric"""
    BRUSHING_GASTRIC = "GASBR"
    """Brushing, Gastric"""
    DRAINAGE_GASTRIC = "GASD"
    """Drainage, Gastric"""
    FLUID_OR_CONTENTS_GASTRIC = "GAST"
    """Fluid/contents, Gastric"""
    GENITAL_VAGINAL = "GENV"
    """Genital vaginal"""
    GRAFT = "GRAFT"
    """Graft"""
    GRANULOMA = "GRANU"
    """Granuloma"""
    CATHETER_GROSHONG = "GROSH"
    """Catheter, Groshong"""
    SOLUTION_GASTROSTOMY = "GSOL"
    """Solution, Gastrostomy"""
    BIOPSY_GASTRIC = "GSPEC"
    """Biopsy, Gastric"""
    TUBE_GASTRIC = "GT"
    """Tube, Gastric"""
    DRAINAGE_TUBE_DRAINAGE = "GTUBE"
    """Drainage Tube, Drainage (Gastrostomy)"""
    BITE_HUMAN = "HBITE"
    """Bite, Human"""
    BLOOD_AUTOPSY = "HBLUD"
    """Blood, Autopsy"""
    CATHETER_TIP_HEMAQUIT = "HEMAQ"
    """Catheter Tip, Hemaquit"""
    CATHETER_TIP_HEMOVAC = "HEMO"
    """Catheter Tip, Hemovac"""
    TISSUE_HERNIATED = "HERNI"
    """Tissue, Herniated"""
    DRAIN_HEMOVAC = "HEV"
    """Drain, Hemovac"""
    CATHETER_HICKMAN = "HIC"
    """Catheter, Hickman"""
    FLUID_HYDROCELE = "HYDC"
    """Fluid, Hydrocele"""
    BITE_INSECT = "IBITE"
    """Bite, Insect"""
    CYST_INCLUSION = "ICYST"
    """Cyst, Inclusion"""
    CATHETER_TIP_INDWELLING = "IDC"
    """Catheter Tip, Indwelling"""
    GAS_INHALED = "IHG"
    """Gas, Inhaled"""
    DRAINAGE_ILEOSTOMY = "ILEO"
    """Drainage, Ileostomy"""
    SOURCE_OF_SPECIMEN_IS_ILLEGIBLE = "ILLEG"
    """Source of Specimen Is Illegible"""
    IMPLANT = "IMP"
    """Implant"""
    SITE_INCISION_OR_SURGICAL = "INCI"
    """Site, Incision/Surgical"""
    INFILTRATE = "INFIL"
    """Infiltrate"""
    INSECT = "INS"
    """Insect"""
    CATHETER_TIP_INTRODUCER = "INTRD"
    """Catheter Tip, Introducer"""
    INTUBATION_TUBE = "IT"
    """Intubation tube"""
    INTRAUTERINE_DEVICE = "IUD"
    """Intrauterine Device"""
    CATHETER_TIP_IV = "IVCAT"
    """Catheter Tip, IV"""
    FLUID_IV = "IVFLD"
    """Fluid, IV"""
    TUBING_TIP_IV = "IVTIP"
    """Tubing Tip, IV"""
    DRAINAGE_JEJUNAL = "JEJU"
    """Drainage, Jejunal"""
    FLUID_JOINT = "JNTFLD"
    """Fluid, Joint"""
    DRAINAGE_JACKSON_PRATT = "JP"
    """Drainage, Jackson Pratt"""
    LAVAGE = "KELOI"
    """Lavage"""
    FLUID_KIDNEY = "KIDFLD"
    """Fluid, Kidney"""
    LAVAGE_BRONHIAL = "LAVG"
    """Lavage, Bronhial"""
    LAVAGE_GASTRIC = "LAVGG"
    """Lavage, Gastric"""
    LAVAGE_PERITONEAL = "LAVGP"
    """Lavage, Peritoneal"""
    LAVAGE_PRE_BRONCH = "LAVPG"
    """Lavage, Pre-Bronch"""
    CONTACT_LENS = "LENS1"
    """Contact Lens"""
    CONTACT_LENS_CASE = "LENS2"
    """Contact Lens Case"""
    LESION = "LESN"
    """Lesion"""
    LIQUID_UNSPECIFIED = "LIQ"
    """Liquid, Unspecified"""
    LIQUID_OTHER = "LIQO"
    """Liquid, Other"""
    FLUID_LUMBAR_SAC = "LSAC"
    """Fluid, Lumbar Sac"""
    CATHETER_TIP_MAKURKOUR = "MAHUR"
    """Catheter Tip, Makurkour"""
    MASS = "MASS"
    """Mass"""
    BLOOD_MENSTRUAL = "MBLD"
    """Blood, Menstrual"""
    MUCOSA = "MUCOS"
    """Mucosa"""
    MUCUS = "MUCUS"
    """Mucus"""
    DRAINAGE_NASAL = "NASDR"
    """Drainage, Nasal"""
    NEEDLE = "NEDL"
    """Needle"""
    SITE_NEPHROSTOMY = "NEPH"
    """Site, Nephrostomy"""
    ASPIRATE_NASOGASTRIC = "NGASP"
    """Aspirate, Nasogastric"""
    DRAINAGE_NASOGASTRIC = "NGAST"
    """Drainage, Nasogastric"""
    SITE_NASO_OR_GASTRIC = "NGS"
    """Site, Naso/Gastric"""
    NODULE = "NODUL"
    """Nodule(s)"""
    SECRETION_NASAL = "NSECR"
    """Secretion, Nasal"""
    OTHER = "ORH"
    """Other"""
    LESION_ORAL = "ORL"
    """Lesion, Oral"""
    SOURCE_OTHER = "OTH"
    """Source, Other"""
    PACEMAKER = "PACEM"
    """Pacemaker"""
    FLUID_PERICARDIAL = "PCFL"
    """Fluid, Pericardial"""
    SITE_PERITONEAL_DIALYSIS = "PDSIT"
    """Site, Peritoneal Dialysis"""
    SITE_PERITONEAL_DIALYSIS_TUNNEL = "PDTS"
    """Site, Peritoneal Dialysis Tunnel"""
    ABSCESS_PELVIC = "PELVA"
    """Abscess, Pelvic"""
    LESION_PENILE = "PENIL"
    """Lesion, Penile"""
    ABSCESS_PERIANAL = "PERIA"
    """Abscess, Perianal"""
    CYST_PILONIDAL = "PILOC"
    """Cyst, Pilonidal"""
    SITE_PIN = "PINS"
    """Site, Pin"""
    SITE_PACEMAKER_INSETION = "PIS"
    """Site, Pacemaker Insetion"""
    PLANT_MATERIAL = "PLAN"
    """Plant Material"""
    PLASMA = "PLAS"
    """Plasma"""
    PLASMA_BAG = "PLB"
    """Plasma bag"""
    SERUM_PEAK_LEVEL = "PLEVS"
    """Serum, Peak Level"""
    DRAINAGE_PENILE = "PND"
    """Drainage, Penile"""
    POLYPS = "POL"
    """Polyps"""
    GRAFT_SITE_POPLITEAL = "POPGS"
    """Graft Site, Popliteal"""
    GRAFT_POPLITEAL = "POPLG"
    """Graft, Popliteal"""
    SITE_POPLITEAL_VEIN = "POPLV"
    """Site, Popliteal Vein"""
    CATHETER_PORTA = "PORTA"
    """Catheter, Porta"""
    PLASMA_PLATELET_POOR = "PPP"
    """Plasma, Platelet poor"""
    PROSTHETIC_DEVICE = "PROST"
    """Prosthetic Device"""
    PLASMA_PLATELET_RICH = "PRP"
    """Plasma, Platelet rich"""
    PSEUDOCYST = "PSC"
    """Pseudocyst"""
    WOUND_PUNCTURE = "PUNCT"
    """Wound, Puncture"""
    PUS = "PUS"
    """Pus"""
    PUSTULE = "PUSFR"
    """Pustule"""
    PUST = "PUST"
    """Pus"""
    QUALITY_CONTROL = "QC3"
    """Quality Control"""
    URINE_RANDOM = "RANDU"
    """Urine, Random"""
    BITE_REPTILE = "RBITE"
    """Bite, Reptile"""
    DRAINAGE_RECTAL = "RECT"
    """Drainage, Rectal"""
    ABSCESS_RECTAL = "RECTA"
    """Abscess, Rectal"""
    CYST_RENAL = "RENALC"
    """Cyst, Renal"""
    FLUID_RENAL_CYST = "RENC"
    """Fluid, Renal Cyst"""
    RESPIRATORY = "RES"
    """Respiratory"""
    SALIVA = "SAL"
    """Saliva"""
    TISSUE_KELOID = "SCAR"
    """Tissue, Keloid (Scar)"""
    CATHETER_TIP_SUBCLAVIAN = "SCLV"
    """Catheter Tip, Subclavian"""
    ABSCESS_SCROTAL = "SCROA"
    """Abscess, Scrotal"""
    SECRETION = "SECRE"
    """Secretion(s)"""
    SERUM = "SER"
    """Serum"""
    SITE_SHUNT = "SHU"
    """Site, Shunt"""
    FLUID_SHUNT = "SHUNF"
    """Fluid, Shunt"""
    SHUNT = "SHUNT"
    """Shunt"""
    SITE = "SITE"
    """Site"""
    BIOPSY_SKIN = "SKBP"
    """Biopsy, Skin"""
    SKIN = "SKN"
    """Skin"""
    MASS_SUB_MANDIBULAR = "SMM"
    """Mass, Sub-Mandibular"""
    FLUID_SYNOVIAL = "SNV"
    """Fluid, synovial (Joint fluid)"""
    SPERMATOZOA = "SPRM"
    """Spermatozoa"""
    CATHETER_TIP_SUPRAPUBIC = "SPRP"
    """Catheter Tip, Suprapubic"""
    CATHETHER_TIP_SUPRAPUBIC = "SPRPB"
    """Cathether Tip, Suprapubic"""
    ENVIRONMENTAL_SPORE_STRIP = "SPS"
    """Environmental, Spore Strip"""
    SPUTUM = "SPT"
    """Sputum"""
    SPUTUM_COUGHED = "SPTC"
    """Sputum - coughed"""
    SPUTUM_TRACHEAL_ASPIRATE = "SPTT"
    """Sputum - tracheal aspirate"""
    SPUTUM_SIMULATED = "SPUT1"
    """Sputum, Simulated"""
    SPUTUM_INDUCTED = "SPUTIN"
    """Sputum, Inducted"""
    SPUTUM_SPONTANEOUS = "SPUTSP"
    """Sputum, Spontaneous"""
    ENVIRONMENTAL_STERRAD = "STER"
    """Environmental, Sterrad"""
    STOOL_EQUALS_FECAL = "STL"
    """Stool = Fecal"""
    STONE_KIDNEY = "STONE"
    """Stone, Kidney"""
    ABSCESS_SUBMANDIBULAR = "SUBMA"
    """Abscess, Submandibular"""
    ABSCESS_SUBMAXILLARY = "SUBMX"
    """Abscess, Submaxillary"""
    DRAINAGE_SUMP = "SUMP"
    """Drainage, Sump"""
    SUPRAPUBIC_TAP = "SUP"
    """Suprapubic Tap"""
    SUTURE = "SUTUR"
    """Suture"""
    CATHETER_TIP_SWAN_GANTZ = "SWGZ"
    """Catheter Tip, Swan Gantz"""
    ASPIRATE_TRACHEAL = "TASP"
    """Aspirate, Tracheal"""
    TISSUE = "TISS"
    """Tissue"""
    TISSUE_ULCER = "TISU"
    """Tissue ulcer"""
    CATHETHER_TIP_TRIPLE_LUMEN = "TLC"
    """Cathether Tip, Triple Lumen"""
    SITE_TRACHEOSTOMY = "TRAC"
    """Site, Tracheostomy"""
    TRANSUDATE = "TRANS"
    """Transudate"""
    SERUM_TROUGH = "TSERU"
    """Serum, Trough"""
    ABSCESS_TESTICULAR = "TSTES"
    """Abscess, Testicular"""
    ASPIRATE_TRANSTRACHEAL = "TTRA"
    """Aspirate, Transtracheal"""
    TUBES = "TUBES"
    """Tubes"""
    TUMOR = "TUMOR"
    """Tumor"""
    SMEAR_TZANCK = "TZANC"
    """Smear, Tzanck"""
    SOURCE_UNIDENTIFIED = "UDENT"
    """Source, Unidentified"""
    URINE = "UR"
    """Urine"""
    URINE_CLEAN_CATCH = "URC"
    """Urine clean catch"""
    URINE_BLADDER_WASHINGS = "URINB"
    """Urine, Bladder Washings"""
    URINE_CATHETERIZED = "URINC"
    """Urine, Catheterized"""
    URINE_MIDSTREAM = "URINM"
    """Urine, Midstream"""
    URINE_NEPHROSTOMY = "URINN"
    """Urine, Nephrostomy"""
    URINE_PEDIBAG = "URINP"
    """Urine, Pedibag"""
    URINE_CATHETER = "URT"
    """Urine catheter"""
    URINE_CYSTOSCOPY = "USCOP"
    """Urine, Cystoscopy"""
    SOURCE_UNSPECIFIED = "USPEC"
    """Source, Unspecified"""
    CATHETER_TIP_VAS = "VASTIP"
    """Catheter Tip, Vas"""
    CATHETER_TIP_VENTRICULAR = "VENT"
    """Catheter Tip, Ventricular"""
    VITREOUS_FLUID = "VITF"
    """Vitreous Fluid"""
    VOMITUS = "VOM"
    """Vomitus"""
    WASH = "WASH"
    """Wash"""
    WASHING_E_G_BRONCHIAL_WASHING = "WASI"
    """Washing, e.g. bronchial washing"""
    WATER = "WAT"
    """Water"""
    BLOOD_WHOLE = "WB"
    """Blood, Whole"""
    WEN = "WEN"
    """Wen"""
    WICK = "WICK"
    """Wick"""
    WOUND = "WND"
    """Wound"""
    WOUND_ABSCESS = "WNDA"
    """Wound abscess"""
    WOUND_DRAINAGE = "WNDD"
    """Wound drainage"""
    WOUND_EXUDATE = "WNDE"
    """Wound exudate"""
    WORM = "WORM"
    """Worm"""
    WART = "WRT"
    """Wart"""
    WWA = "WWA"
    """Environmental, Water"""
    WWO = "WWO"
    """Environmental, Water (Ocean)"""
    WWT = "WWT"
    """Environmental, Water (Tap)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenType.ABSCESS: "Abscess",
    SpecimenType.TISSUE_ACNE: "Tissue, Acne",
    SpecimenType.FLUID_ACNE: "Fluid, Acne",
    SpecimenType.AIR_SAMPLE: "Air Sample",
    SpecimenType.ALLOGRAFT: "Allograft",
    SpecimenType.AMPUTATION: "Amputation",
    SpecimenType.CATHETER_TIP_ANGIO: "Catheter Tip, Angio",
    SpecimenType.CATHETER_TIP_ARTERIAL: "Catheter Tip, Arterial",
    SpecimenType.SERUM_ACUTE: "Serum, Acute",
    SpecimenType.ASPIRATE: "Aspirate",
    SpecimenType.ENVIRONMENT_ATTEST: "Environment, Attest",
    SpecimenType.ENVIRONMENTAL_AUTOCLAVE_CAPSULE: "Environmental, Autoclave Capsule",
    SpecimenType.AUTOPSY: "Autopsy",
    SpecimenType.BLOOD_BAG: "Blood bag",
    SpecimenType.CYST_BAKERS: "Cyst, Bakers",
    SpecimenType.BITE: "Bite",
    SpecimenType.BLEB: "Bleb",
    SpecimenType.BLISTER: "Blister",
    SpecimenType.BOIL: "Boil",
    SpecimenType.BONE: "Bone",
    SpecimenType.BOWEL_CONTENTS: "Bowel contents",
    SpecimenType.BLOOD_PRODUCT_UNIT: "Blood product unit",
    SpecimenType.BURN: "Burn",
    SpecimenType.BRUSH: "Brush",
    SpecimenType.BREATH: "Breath (use EXHLD)",
    SpecimenType.BRUSHING: "Brushing",
    SpecimenType.BUBO: "Bubo",
    SpecimenType.BULLA_OR_BULLAE: "Bulla/Bullae",
    SpecimenType.BIOPSY: "Biopsy",
    SpecimenType.CALCULUS: "Calculus (=Stone)",
    SpecimenType.CARBUNCLE: "Carbuncle",
    SpecimenType.CATHETER: "Catheter",
    SpecimenType.BITE_CAT: "Bite, Cat",
    SpecimenType.CLIPPINGS: "Clippings",
    SpecimenType.CONJUNCTIVA: "Conjunctiva",
    SpecimenType.COLOSTRUM: "Colostrum",
    SpecimenType.BIOSPY_CONE: "Biospy, Cone",
    SpecimenType.SCRATCH_CAT: "Scratch, Cat",
    SpecimenType.SERUM_CONVALESCENT: "Serum, Convalescent",
    SpecimenType.CATHETER_INSERTION_SITE: "Catheter Insertion Site",
    SpecimenType.FLUID_CYSTOSTOMY_TUBE: "Fluid, Cystostomy Tube",
    SpecimenType.FLUID_CYST: "Fluid, Cyst",
    SpecimenType.BLOOD_CELL_SAVER: "Blood, Cell Saver",
    SpecimenType.CATHETER_TIP: "Catheter tip",
    SpecimenType.SITE_CVP: "Site, CVP",
    SpecimenType.CATHETER_TIP_CVP: "Catheter Tip, CVP",
    SpecimenType.NODULE_CYSTIC: "Nodule, Cystic",
    SpecimenType.CYST: "Cyst",
    SpecimenType.BITE_DOG: "Bite, Dog",
    SpecimenType.SPUTUM_DEEP_COUGH: "Sputum, Deep Cough",
    SpecimenType.ULCER_DECUBITUS: "Ulcer, Decubitus",
    SpecimenType.ENVIRONMENTAL_WATER: "Environmental, Water (Deionized)",
    SpecimenType.DIALYSATE: "Dialysate",
    SpecimenType.DISCHARGE: "Discharge",
    SpecimenType.DIVERTICULUM: "Diverticulum",
    SpecimenType.DRAIN: "Drain",
    SpecimenType.DRAINAGE_TUBE: "Drainage, Tube",
    SpecimenType.DRAINAGE_PENROSE: "Drainage, Penrose",
    SpecimenType.EAR_WAX: "Ear wax (cerumen)",
    SpecimenType.BRUSH_ESOPHAGEAL: "Brush, Esophageal",
    SpecimenType.ENVIRONMENTAL_EYE_WASH: "Environmental, Eye Wash",
    SpecimenType.ENVIRONMENTAL_EFFLUENT: "Environmental, Effluent",
    SpecimenType.EFFUSION: "Effusion",
    SpecimenType.ENVIRONMENTAL_FOOD: "Environmental, Food",
    SpecimenType.ENVIRONMENTAL_ISOLETTE: "Environmental, Isolette",
    SpecimenType.ELECTRODE: "Electrode",
    SpecimenType.ENVIRONMENTAL_UNIDENTIFIED_SUBSTANCE: "Environmental, Unidentified Substance",
    SpecimenType.ENVIRONMENTAL_OTHER_SUBSTANCE: "Environmental, Other Substance",
    SpecimenType.ENVIRONMENTAL_SOIL: "Environmental, Soil",
    SpecimenType.ENVIRONMENTAL_SOLUTION: "Environmental, Solution (Sterile)",
    SpecimenType.ASPIRATE_ENDOTRACH: "Aspirate, Endotrach",
    SpecimenType.CATHETER_TIP_ENDOTRACHEAL: "Catheter Tip, Endotracheal",
    SpecimenType.TUBE_ENDOTRACHEAL: "Tube, Endotracheal",
    SpecimenType.ENVIRONMENTAL_WHIRLPOOL: "Environmental, Whirlpool",
    SpecimenType.GAS_EXHALED: "Gas, exhaled (=breath)",
    SpecimenType.SHUNT_EXTERNAL: "Shunt, External",
    SpecimenType.EXUDATE: "Exudate",
    SpecimenType.FAW: "Environmental, Water (Well)",
    SpecimenType.BLOOD_FETAL: "Blood, Fetal",
    SpecimenType.FLUID_ABDOMEN: "Fluid, Abdomen",
    SpecimenType.FISTULA: "Fistula",
    SpecimenType.FLUID_OTHER: "Fluid, Other",
    SpecimenType.FILTER: "Filter",
    SpecimenType.FLUID_BODY_UNSP: "Fluid, Body unsp",
    SpecimenType.FLUID: "Fluid",
    SpecimenType.CATHETER_TIP_FOLEY: "Catheter Tip, Foley",
    SpecimenType.FLUID_RESPIRATORY: "Fluid, Respiratory",
    SpecimenType.SCALP_FETAL: "Scalp, Fetal",
    SpecimenType.FURUNCLE: "Furuncle",
    SpecimenType.GAS: "Gas",
    SpecimenType.ASPIRATE_GASTRIC: "Aspirate, Gastric",
    SpecimenType.ANTRUM_GASTRIC: "Antrum, Gastric",
    SpecimenType.BRUSHING_GASTRIC: "Brushing, Gastric",
    SpecimenType.DRAINAGE_GASTRIC: "Drainage, Gastric",
    SpecimenType.FLUID_OR_CONTENTS_GASTRIC: "Fluid/contents, Gastric",
    SpecimenType.GENITAL_VAGINAL: "Genital vaginal",
    SpecimenType.GRAFT: "Graft",
    SpecimenType.GRANULOMA: "Granuloma",
    SpecimenType.CATHETER_GROSHONG: "Catheter, Groshong",
    SpecimenType.SOLUTION_GASTROSTOMY: "Solution, Gastrostomy",
    SpecimenType.BIOPSY_GASTRIC: "Biopsy, Gastric",
    SpecimenType.TUBE_GASTRIC: "Tube, Gastric",
    SpecimenType.DRAINAGE_TUBE_DRAINAGE: "Drainage Tube, Drainage (Gastrostomy)",
    SpecimenType.BITE_HUMAN: "Bite, Human",
    SpecimenType.BLOOD_AUTOPSY: "Blood, Autopsy",
    SpecimenType.CATHETER_TIP_HEMAQUIT: "Catheter Tip, Hemaquit",
    SpecimenType.CATHETER_TIP_HEMOVAC: "Catheter Tip, Hemovac",
    SpecimenType.TISSUE_HERNIATED: "Tissue, Herniated",
    SpecimenType.DRAIN_HEMOVAC: "Drain, Hemovac",
    SpecimenType.CATHETER_HICKMAN: "Catheter, Hickman",
    SpecimenType.FLUID_HYDROCELE: "Fluid, Hydrocele",
    SpecimenType.BITE_INSECT: "Bite, Insect",
    SpecimenType.CYST_INCLUSION: "Cyst, Inclusion",
    SpecimenType.CATHETER_TIP_INDWELLING: "Catheter Tip, Indwelling",
    SpecimenType.GAS_INHALED: "Gas, Inhaled",
    SpecimenType.DRAINAGE_ILEOSTOMY: "Drainage, Ileostomy",
    SpecimenType.SOURCE_OF_SPECIMEN_IS_ILLEGIBLE: "Source of Specimen Is Illegible",
    SpecimenType.IMPLANT: "Implant",
    SpecimenType.SITE_INCISION_OR_SURGICAL: "Site, Incision/Surgical",
    SpecimenType.INFILTRATE: "Infiltrate",
    SpecimenType.INSECT: "Insect",
    SpecimenType.CATHETER_TIP_INTRODUCER: "Catheter Tip, Introducer",
    SpecimenType.INTUBATION_TUBE: "Intubation tube",
    SpecimenType.INTRAUTERINE_DEVICE: "Intrauterine Device",
    SpecimenType.CATHETER_TIP_IV: "Catheter Tip, IV",
    SpecimenType.FLUID_IV: "Fluid, IV",
    SpecimenType.TUBING_TIP_IV: "Tubing Tip, IV",
    SpecimenType.DRAINAGE_JEJUNAL: "Drainage, Jejunal",
    SpecimenType.FLUID_JOINT: "Fluid, Joint",
    SpecimenType.DRAINAGE_JACKSON_PRATT: "Drainage, Jackson Pratt",
    SpecimenType.LAVAGE: "Lavage",
    SpecimenType.FLUID_KIDNEY: "Fluid, Kidney",
    SpecimenType.LAVAGE_BRONHIAL: "Lavage, Bronhial",
    SpecimenType.LAVAGE_GASTRIC: "Lavage, Gastric",
    SpecimenType.LAVAGE_PERITONEAL: "Lavage, Peritoneal",
    SpecimenType.LAVAGE_PRE_BRONCH: "Lavage, Pre-Bronch",
    SpecimenType.CONTACT_LENS: "Contact Lens",
    SpecimenType.CONTACT_LENS_CASE: "Contact Lens Case",
    SpecimenType.LESION: "Lesion",
    SpecimenType.LIQUID_UNSPECIFIED: "Liquid, Unspecified",
    SpecimenType.LIQUID_OTHER: "Liquid, Other",
    SpecimenType.FLUID_LUMBAR_SAC: "Fluid, Lumbar Sac",
    SpecimenType.CATHETER_TIP_MAKURKOUR: "Catheter Tip, Makurkour",
    SpecimenType.MASS: "Mass",
    SpecimenType.BLOOD_MENSTRUAL: "Blood, Menstrual",
    SpecimenType.MUCOSA: "Mucosa",
    SpecimenType.MUCUS: "Mucus",
    SpecimenType.DRAINAGE_NASAL: "Drainage, Nasal",
    SpecimenType.NEEDLE: "Needle",
    SpecimenType.SITE_NEPHROSTOMY: "Site, Nephrostomy",
    SpecimenType.ASPIRATE_NASOGASTRIC: "Aspirate, Nasogastric",
    SpecimenType.DRAINAGE_NASOGASTRIC: "Drainage, Nasogastric",
    SpecimenType.SITE_NASO_OR_GASTRIC: "Site, Naso/Gastric",
    SpecimenType.NODULE: "Nodule(s)",
    SpecimenType.SECRETION_NASAL: "Secretion, Nasal",
    SpecimenType.OTHER: "Other",
    SpecimenType.LESION_ORAL: "Lesion, Oral",
    SpecimenType.SOURCE_OTHER: "Source, Other",
    SpecimenType.PACEMAKER: "Pacemaker",
    SpecimenType.FLUID_PERICARDIAL: "Fluid, Pericardial",
    SpecimenType.SITE_PERITONEAL_DIALYSIS: "Site, Peritoneal Dialysis",
    SpecimenType.SITE_PERITONEAL_DIALYSIS_TUNNEL: "Site, Peritoneal Dialysis Tunnel",
    SpecimenType.ABSCESS_PELVIC: "Abscess, Pelvic",
    SpecimenType.LESION_PENILE: "Lesion, Penile",
    SpecimenType.ABSCESS_PERIANAL: "Abscess, Perianal",
    SpecimenType.CYST_PILONIDAL: "Cyst, Pilonidal",
    SpecimenType.SITE_PIN: "Site, Pin",
    SpecimenType.SITE_PACEMAKER_INSETION: "Site, Pacemaker Insetion",
    SpecimenType.PLANT_MATERIAL: "Plant Material",
    SpecimenType.PLASMA: "Plasma",
    SpecimenType.PLASMA_BAG: "Plasma bag",
    SpecimenType.SERUM_PEAK_LEVEL: "Serum, Peak Level",
    SpecimenType.DRAINAGE_PENILE: "Drainage, Penile",
    SpecimenType.POLYPS: "Polyps",
    SpecimenType.GRAFT_SITE_POPLITEAL: "Graft Site, Popliteal",
    SpecimenType.GRAFT_POPLITEAL: "Graft, Popliteal",
    SpecimenType.SITE_POPLITEAL_VEIN: "Site, Popliteal Vein",
    SpecimenType.CATHETER_PORTA: "Catheter, Porta",
    SpecimenType.PLASMA_PLATELET_POOR: "Plasma, Platelet poor",
    SpecimenType.PROSTHETIC_DEVICE: "Prosthetic Device",
    SpecimenType.PLASMA_PLATELET_RICH: "Plasma, Platelet rich",
    SpecimenType.PSEUDOCYST: "Pseudocyst",
    SpecimenType.WOUND_PUNCTURE: "Wound, Puncture",
    SpecimenType.PUS: "Pus",
    SpecimenType.PUSTULE: "Pustule",
    SpecimenType.PUST: "Pus",
    SpecimenType.QUALITY_CONTROL: "Quality Control",
    SpecimenType.URINE_RANDOM: "Urine, Random",
    SpecimenType.BITE_REPTILE: "Bite, Reptile",
    SpecimenType.DRAINAGE_RECTAL: "Drainage, Rectal",
    SpecimenType.ABSCESS_RECTAL: "Abscess, Rectal",
    SpecimenType.CYST_RENAL: "Cyst, Renal",
    SpecimenType.FLUID_RENAL_CYST: "Fluid, Renal Cyst",
    SpecimenType.RESPIRATORY: "Respiratory",
    SpecimenType.SALIVA: "Saliva",
    SpecimenType.TISSUE_KELOID: "Tissue, Keloid (Scar)",
    SpecimenType.CATHETER_TIP_SUBCLAVIAN: "Catheter Tip, Subclavian",
    SpecimenType.ABSCESS_SCROTAL: "Abscess, Scrotal",
    SpecimenType.SECRETION: "Secretion(s)",
    SpecimenType.SERUM: "Serum",
    SpecimenType.SITE_SHUNT: "Site, Shunt",
    SpecimenType.FLUID_SHUNT: "Fluid, Shunt",
    SpecimenType.SHUNT: "Shunt",
    SpecimenType.SITE: "Site",
    SpecimenType.BIOPSY_SKIN: "Biopsy, Skin",
    SpecimenType.SKIN: "Skin",
    SpecimenType.MASS_SUB_MANDIBULAR: "Mass, Sub-Mandibular",
    SpecimenType.FLUID_SYNOVIAL: "Fluid, synovial (Joint fluid)",
    SpecimenType.SPERMATOZOA: "Spermatozoa",
    SpecimenType.CATHETER_TIP_SUPRAPUBIC: "Catheter Tip, Suprapubic",
    SpecimenType.CATHETHER_TIP_SUPRAPUBIC: "Cathether Tip, Suprapubic",
    SpecimenType.ENVIRONMENTAL_SPORE_STRIP: "Environmental, Spore Strip",
    SpecimenType.SPUTUM: "Sputum",
    SpecimenType.SPUTUM_COUGHED: "Sputum - coughed",
    SpecimenType.SPUTUM_TRACHEAL_ASPIRATE: "Sputum - tracheal aspirate",
    SpecimenType.SPUTUM_SIMULATED: "Sputum, Simulated",
    SpecimenType.SPUTUM_INDUCTED: "Sputum, Inducted",
    SpecimenType.SPUTUM_SPONTANEOUS: "Sputum, Spontaneous",
    SpecimenType.ENVIRONMENTAL_STERRAD: "Environmental, Sterrad",
    SpecimenType.STOOL_EQUALS_FECAL: "Stool = Fecal",
    SpecimenType.STONE_KIDNEY: "Stone, Kidney",
    SpecimenType.ABSCESS_SUBMANDIBULAR: "Abscess, Submandibular",
    SpecimenType.ABSCESS_SUBMAXILLARY: "Abscess, Submaxillary",
    SpecimenType.DRAINAGE_SUMP: "Drainage, Sump",
    SpecimenType.SUPRAPUBIC_TAP: "Suprapubic Tap",
    SpecimenType.SUTURE: "Suture",
    SpecimenType.CATHETER_TIP_SWAN_GANTZ: "Catheter Tip, Swan Gantz",
    SpecimenType.ASPIRATE_TRACHEAL: "Aspirate, Tracheal",
    SpecimenType.TISSUE: "Tissue",
    SpecimenType.TISSUE_ULCER: "Tissue ulcer",
    SpecimenType.CATHETHER_TIP_TRIPLE_LUMEN: "Cathether Tip, Triple Lumen",
    SpecimenType.SITE_TRACHEOSTOMY: "Site, Tracheostomy",
    SpecimenType.TRANSUDATE: "Transudate",
    SpecimenType.SERUM_TROUGH: "Serum, Trough",
    SpecimenType.ABSCESS_TESTICULAR: "Abscess, Testicular",
    SpecimenType.ASPIRATE_TRANSTRACHEAL: "Aspirate, Transtracheal",
    SpecimenType.TUBES: "Tubes",
    SpecimenType.TUMOR: "Tumor",
    SpecimenType.SMEAR_TZANCK: "Smear, Tzanck",
    SpecimenType.SOURCE_UNIDENTIFIED: "Source, Unidentified",
    SpecimenType.URINE: "Urine",
    SpecimenType.URINE_CLEAN_CATCH: "Urine clean catch",
    SpecimenType.URINE_BLADDER_WASHINGS: "Urine, Bladder Washings",
    SpecimenType.URINE_CATHETERIZED: "Urine, Catheterized",
    SpecimenType.URINE_MIDSTREAM: "Urine, Midstream",
    SpecimenType.URINE_NEPHROSTOMY: "Urine, Nephrostomy",
    SpecimenType.URINE_PEDIBAG: "Urine, Pedibag",
    SpecimenType.URINE_CATHETER: "Urine catheter",
    SpecimenType.URINE_CYSTOSCOPY: "Urine, Cystoscopy",
    SpecimenType.SOURCE_UNSPECIFIED: "Source, Unspecified",
    SpecimenType.CATHETER_TIP_VAS: "Catheter Tip, Vas",
    SpecimenType.CATHETER_TIP_VENTRICULAR: "Catheter Tip, Ventricular",
    SpecimenType.VITREOUS_FLUID: "Vitreous Fluid",
    SpecimenType.VOMITUS: "Vomitus",
    SpecimenType.WASH: "Wash",
    SpecimenType.WASHING_E_G_BRONCHIAL_WASHING: "Washing, e.g. bronchial washing",
    SpecimenType.WATER: "Water",
    SpecimenType.BLOOD_WHOLE: "Blood, Whole",
    SpecimenType.WEN: "Wen",
    SpecimenType.WICK: "Wick",
    SpecimenType.WOUND: "Wound",
    SpecimenType.WOUND_ABSCESS: "Wound abscess",
    SpecimenType.WOUND_DRAINAGE: "Wound drainage",
    SpecimenType.WOUND_EXUDATE: "Wound exudate",
    SpecimenType.WORM: "Worm",
    SpecimenType.WART: "Wart",
    SpecimenType.WWA: "Environmental, Water",
    SpecimenType.WWO: "Environmental, Water (Ocean)",
    SpecimenType.WWT: "Environmental, Water (Tap)",
}
