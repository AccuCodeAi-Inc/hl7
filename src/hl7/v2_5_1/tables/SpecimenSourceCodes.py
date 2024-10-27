from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Source Codes - 0070
Table Type: HL7
"""


class SpecimenSourceCodes(HL7Table):
    """
    Specimen Source Codes - 0070 // HL7 table type
    - ABSCESS
    - TISSUE_ACNE
    - FLUID_ACNE
    - AIR_SAMPLE
    - ALLOGRAFT
    - AMNIOTIC_FLUID
    - AMPUTATION
    - CATHETER_TIP_ANGIO
    - CATHETER_TIP_ARTERIAL
    - SERUM_ACUTE
    - ASPIRATE
    - ENVIRONMENTAL_AUTOCLAVE_AMPULE
    - ENVIRONMENT_ATTEST
    - AUTOPSY
    - BLOOD_BAG
    - CYST_BAKERS
    - WHOLE_BODY
    - BILE_FLUID
    - BITE
    - WHOLE_BLOOD
    - BLOOD_ARTERIAL
    - BLOOD_CAPILLARY
    - CORD_BLOOD
    - BLOOD_VENOUS
    - BLEB
    - BLISTER
    - BOIL
    - BONE
    - BOWEL_CONTENTS
    - BASOPHILS
    - BLOOD_PRODUCT_UNIT
    - BURN
    - BRONCHIAL
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
    - CARDIAC_MUSCLE
    - CLIPPINGS
    - CONJUNCTIVA
    - CANNULA
    - COLOSTRUM
    - BIOSPY_CONE
    - SCRATCH_CAT
    - SERUM_CONVALESCENT
    - CEREBRAL_SPINAL_FLUID
    - CATHETER_INSERTION_SITE
    - FLUID_CYSTOSTOMY_TUBE
    - FLUID_CYST
    - BLOOD_CELL_SAVER
    - CATHETER_TIP
    - CURETTAGE
    - CERVICAL_MUCUS
    - SITE_CVP
    - CATHETER_TIP_CVP
    - CERVIX
    - NODULE_CYSTIC
    - CYST
    - BITE_DOG
    - SPUTUM_DEEP_COUGH
    - ULCER_DECUBITUS
    - ENVIRONMENTAL_WATER
    - DIALYSATE
    - DIALYSIS_FLUID
    - DISCHARGE
    - DIVERTICULUM
    - DOSE_MED_OR_SUBSTANCE
    - DRAIN
    - DRAINAGE_TUBE
    - DRAINAGE_PENROSE
    - DUODENAL_FLUID
    - EAR
    - EAR_WAX
    - BRUSH_ESOPHAGEAL
    - ENVIRONMENTAL_EYE_WASH
    - ENVIRONMENTAL_EFFLUENT
    - EFFUSION
    - ENVIRONMENTAL_FOOD
    - ENVIRONMENTAL_ISOLETTE
    - ELECTRODE
    - ENDOCARDIUM
    - ENDOMETRIUM
    - ENVIRONMENTAL_UNIDENTIFIED_SUBSTANCE
    - EOSINOPHILS
    - ENVIRONMENTAL_OTHER_SUBSTANCE
    - ENVIRONMENTAL_SOIL
    - ENVIRONMENTAL_SOLUTION
    - ASPIRATE_ENDOTRACH
    - CATHETER_TIP_ENDOTRACHEAL
    - TUBE_ENDOTRACHEAL
    - ENVIRONMENTAL_WHIRLPOOL
    - EXHALED_GAS
    - SHUNT_EXTERNAL
    - EXUDATE
    - EYE
    - FAW
    - BLOOD_FETAL
    - FLUID_ABDOMEN
    - FIBROBLASTS
    - FISTULA
    - FLUID_OTHER
    - FILTER
    - BODY_FLUID_UNSP
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
    - GENITAL
    - GENITAL_CERVIX
    - GENITAL_LOCHIA
    - GENITAL_VAGINAL
    - GRAFT
    - GRANULOMA
    - CATHETER_GROSHONG
    - SOLUTION_GASTROSTOMY
    - BIOPSY_GASTRIC
    - TUBE_GASTRIC
    - DRAINAGE_TUBE_DRAINAGE
    - HAIR
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
    - ISOLATE
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
    - LAMELLA
    - LAVAGE_BRONHIAL
    - LAVAGE_GASTRIC
    - LAVAGE_PERITONEAL
    - LAVAGE_PRE_BRONCH
    - CONTACT_LENS
    - CONTACT_LENS_CASE
    - LESION
    - LIQUID_NOS
    - LIQUID_OTHER
    - LINE
    - LINE_ARTERIAL
    - LINE_VENOUS
    - FLUID_LUMBAR_SAC
    - LYMPHOCYTES
    - MACROPHAGES
    - CATHETER_TIP_MAKURKOUR
    - MARROW
    - MASS
    - BLOOD_MENSTRUAL
    - MECONIUM
    - BREAST_MILK
    - MILK
    - MUCOSA
    - MUCUS
    - NAIL
    - DRAINAGE_NASAL
    - NEEDLE
    - SITE_NEPHROSTOMY
    - ASPIRATE_NASOGASTRIC
    - DRAINAGE_NASOGASTRIC
    - SITE_NASO_OR_GASTRIC
    - NODULE
    - NOSE
    - SECRETION_NASAL
    - OTHER
    - LESION_ORAL
    - SOURCE_OTHER
    - PACEMAKER
    - PANCREATIC_FLUID
    - PATIENT
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
    - PLACENTA
    - SERUM_PEAK_LEVEL
    - PLEURAL_FLUID
    - POLYMORPHONUCLEAR_NEUTROPHILS
    - DRAINAGE_PENILE
    - POLYPS
    - GRAFT_SITE_POPLITEAL
    - GRAFT_POPLITEAL
    - SITE_POPLITEAL_VEIN
    - CATHETER_PORTA
    - PLATELET_POOR_PLASMA
    - PROSTHETIC_DEVICE
    - PLATELET_RICH_PLASMA
    - PERITONEAL_FLUID_OR_ASCITES
    - PSEUDOCYST
    - WOUND_PUNCTURE
    - PUS
    - PUSTULE
    - PUST
    - QUALITY_CONTROL
    - URINE_RANDOM
    - ERYTHROCYTES
    - BITE_REPTILE
    - DRAINAGE_RECTAL
    - ABSCESS_RECTAL
    - CYST_RENAL
    - FLUID_RENAL_CYST
    - RESPIRATORY
    - ROUTE_OF_MEDICINE
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
    - SKELETAL_MUSCLE
    - SKIN
    - MASS_SUB_MANDIBULAR
    - SEMINAL_FLUID
    - SYNOVIAL_FLUID
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
    - STONE
    - STONE_KIDNEY
    - ABSCESS_SUBMANDIBULAR
    - ABSCESS_SUBMAXILLARY
    - DRAINAGE_SUMP
    - SUPRAPUBIC_TAP
    - SUTURE
    - CATHETER_TIP_SWAN_GANTZ
    - SWEAT
    - ASPIRATE_TRACHEAL
    - TEARS
    - THROMBOCYTE
    - THROAT
    - TISSUE_GALL_BLADDER
    - TISSUE_PLACENTA
    - TISSUE
    - TISSUE_ULCER
    - CATHETHER_TIP_TRIPLE_LUMEN
    - TISSUE_LARGE_INTESTINE
    - TISSUE_LUNG
    - SITE_TRACHEOSTOMY
    - TRANSUDATE
    - SERUM_TROUGH
    - TISSUE_SMALL_INTESTINE
    - ABSCESS_TESTICULAR
    - ASPIRATE_TRANSTRACHEAL
    - TUBE_NOS
    - TUBES
    - TUMOR
    - SMEAR_TZANCK
    - SOURCE_UNIDENTIFIED
    - ULCER
    - UMBILICAL_BLOOD
    - UNKNOWN_MEDICINE
    - URINE
    - URINE_CLEAN_CATCH
    - URINE_BLADDER_WASHINGS
    - URINE_CATHETERIZED
    - URINE_MIDSTREAM
    - URINE_NEPHROSTOMY
    - URINE_PEDIBAG
    - URINE_SEDIMENT
    - URINE_CATHETER
    - URETHRA
    - URINE_CYSTOSCOPY
    - SOURCE_UNSPECIFIED
    - UNKNOWN_SUBSTANCE
    - CATHETER_TIP_VAS
    - CATHETER_TIP_VENTRICULAR
    - VITREOUS_FLUID
    - VOMITUS
    - WASH
    - WASHING_E_G_BRONCHIAL_WASHING
    - WATER
    - BLOOD_WHOLE
    - LEUKOCYTES
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
    - TO_BE_SPECIFIED_IN_ANOTHER_PART_OF_THE_MESSAGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0070
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
    AMNIOTIC_FLUID = "AMN"
    """Amniotic fluid"""
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
    ENVIRONMENTAL_AUTOCLAVE_AMPULE = "ATTE"
    """Environmental, Autoclave Ampule"""
    ENVIRONMENT_ATTEST = "AUTOC"
    """Environment, Attest"""
    AUTOPSY = "AUTP"
    """Autopsy"""
    BLOOD_BAG = "BBL"
    """Blood bag"""
    CYST_BAKERS = "BCYST"
    """Cyst, Bakers"""
    WHOLE_BODY = "BDY"
    """Whole body"""
    BILE_FLUID = "BIFL"
    """Bile fluid"""
    BITE = "BITE"
    """Bite"""
    WHOLE_BLOOD = "BLD"
    """Whole blood"""
    BLOOD_ARTERIAL = "BLDA"
    """Blood arterial"""
    BLOOD_CAPILLARY = "BLDC"
    """Blood capillary"""
    CORD_BLOOD = "BLDCO"
    """Cord blood"""
    BLOOD_VENOUS = "BLDV"
    """Blood venous"""
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
    BASOPHILS = "BPH"
    """Basophils"""
    BLOOD_PRODUCT_UNIT = "BPU"
    """Blood product unit"""
    BURN = "BRN"
    """Burn"""
    BRONCHIAL = "BRO"
    """Bronchial"""
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
    CARDIAC_MUSCLE = "CDM"
    """Cardiac muscle"""
    CLIPPINGS = "CLIPP"
    """Clippings"""
    CONJUNCTIVA = "CNJT"
    """Conjunctiva"""
    CANNULA = "CNL"
    """Cannula"""
    COLOSTRUM = "COL"
    """Colostrum"""
    BIOSPY_CONE = "CONE"
    """Biospy, Cone"""
    SCRATCH_CAT = "CSCR"
    """Scratch, Cat"""
    SERUM_CONVALESCENT = "CSERU"
    """Serum, Convalescent"""
    CEREBRAL_SPINAL_FLUID = "CSF"
    """Cerebral spinal fluid"""
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
    CURETTAGE = "CUR"
    """Curettage"""
    CERVICAL_MUCUS = "CVM"
    """Cervical mucus"""
    SITE_CVP = "CVPS"
    """Site, CVP"""
    CATHETER_TIP_CVP = "CVPT"
    """Catheter Tip, CVP"""
    CERVIX = "CVX"
    """Cervix"""
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
    DIALYSIS_FLUID = "DIAF"
    """Dialysis fluid"""
    DISCHARGE = "DISCHG"
    """Discharge"""
    DIVERTICULUM = "DIV"
    """Diverticulum"""
    DOSE_MED_OR_SUBSTANCE = "DOSE"
    """Dose med or substance"""
    DRAIN = "DRN"
    """Drain"""
    DRAINAGE_TUBE = "DRNG"
    """Drainage, Tube"""
    DRAINAGE_PENROSE = "DRNGP"
    """Drainage, Penrose"""
    DUODENAL_FLUID = "DUFL"
    """Duodenal fluid"""
    EAR = "EAR"
    """Ear"""
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
    ENDOCARDIUM = "ENDC"
    """Endocardium"""
    ENDOMETRIUM = "ENDM"
    """Endometrium"""
    ENVIRONMENTAL_UNIDENTIFIED_SUBSTANCE = "ENVIR"
    """Environmental, Unidentified Substance"""
    EOSINOPHILS = "EOS"
    """Eosinophils"""
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
    EXHALED_GAS = "EXG"
    """Exhaled gas (=breath)"""
    SHUNT_EXTERNAL = "EXS"
    """Shunt, External"""
    EXUDATE = "EXUDTE"
    """Exudate"""
    EYE = "EYE"
    """Eye"""
    FAW = "FAW"
    """Environmental, Water (Well)"""
    BLOOD_FETAL = "FBLOOD"
    """Blood, Fetal"""
    FLUID_ABDOMEN = "FGA"
    """Fluid, Abdomen"""
    FIBROBLASTS = "FIB"
    """Fibroblasts"""
    FISTULA = "FIST"
    """Fistula"""
    FLUID_OTHER = "FLD"
    """Fluid, Other"""
    FILTER = "FLT"
    """Filter"""
    BODY_FLUID_UNSP = "FLU"
    """Body fluid, unsp"""
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
    GENITAL = "GEN"
    """Genital"""
    GENITAL_CERVIX = "GENC"
    """Genital cervix"""
    GENITAL_LOCHIA = "GENL"
    """Genital lochia"""
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
    HAIR = "HAR"
    """Hair"""
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
    ISOLATE = "ISLT"
    """Isolate"""
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
    LAMELLA = "LAM"
    """Lamella"""
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
    LIQUID_NOS = "LIQ"
    """Liquid NOS"""
    LIQUID_OTHER = "LIQO"
    """Liquid, Other"""
    LINE = "LN"
    """Line"""
    LINE_ARTERIAL = "LNA"
    """Line arterial"""
    LINE_VENOUS = "LNV"
    """Line venous"""
    FLUID_LUMBAR_SAC = "LSAC"
    """Fluid, Lumbar Sac"""
    LYMPHOCYTES = "LYM"
    """Lymphocytes"""
    MACROPHAGES = "MAC"
    """Macrophages"""
    CATHETER_TIP_MAKURKOUR = "MAHUR"
    """Catheter Tip, Makurkour"""
    MARROW = "MAR"
    """Marrow"""
    MASS = "MASS"
    """Mass"""
    BLOOD_MENSTRUAL = "MBLD"
    """Blood, Menstrual"""
    MECONIUM = "MEC"
    """Meconium"""
    BREAST_MILK = "MILK"
    """Breast milk"""
    MILK = "MLK"
    """Milk"""
    MUCOSA = "MUCOS"
    """Mucosa"""
    MUCUS = "MUCUS"
    """Mucus"""
    NAIL = "NAIL"
    """Nail"""
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
    NOSE = "NOS"
    """Nose (nasal passage)"""
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
    PANCREATIC_FLUID = "PAFL"
    """Pancreatic fluid"""
    PATIENT = "PAT"
    """Patient"""
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
    PLACENTA = "PLC"
    """Placenta"""
    SERUM_PEAK_LEVEL = "PLEVS"
    """Serum, Peak Level"""
    PLEURAL_FLUID = "PLR"
    """Pleural fluid (thoracentesis fld)"""
    POLYMORPHONUCLEAR_NEUTROPHILS = "PMN"
    """Polymorphonuclear neutrophils"""
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
    PLATELET_POOR_PLASMA = "PPP"
    """Platelet poor plasma"""
    PROSTHETIC_DEVICE = "PROST"
    """Prosthetic Device"""
    PLATELET_RICH_PLASMA = "PRP"
    """Platelet rich plasma"""
    PERITONEAL_FLUID_OR_ASCITES = "PRT"
    """Peritoneal fluid /ascites"""
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
    ERYTHROCYTES = "RBC"
    """Erythrocytes"""
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
    ROUTE_OF_MEDICINE = "RT"
    """Route of medicine"""
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
    SKELETAL_MUSCLE = "SKM"
    """Skeletal muscle"""
    SKIN = "SKN"
    """Skin"""
    MASS_SUB_MANDIBULAR = "SMM"
    """Mass, Sub-Mandibular"""
    SEMINAL_FLUID = "SMN"
    """Seminal fluid"""
    SYNOVIAL_FLUID = "SNV"
    """Synovial fluid (Joint fluid)"""
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
    STONE = "STON"
    """Stone (use CALC)"""
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
    SWEAT = "SWT"
    """Sweat"""
    ASPIRATE_TRACHEAL = "TASP"
    """Aspirate, Tracheal"""
    TEARS = "TEAR"
    """Tears"""
    THROMBOCYTE = "THRB"
    """Thrombocyte (platelet)"""
    THROAT = "THRT"
    """Throat"""
    TISSUE_GALL_BLADDER = "TISG"
    """Tissue gall bladder"""
    TISSUE_PLACENTA = "TISPL"
    """Tissue placenta"""
    TISSUE = "TISS"
    """Tissue"""
    TISSUE_ULCER = "TISU"
    """Tissue ulcer"""
    CATHETHER_TIP_TRIPLE_LUMEN = "TLC"
    """Cathether Tip, Triple Lumen"""
    TISSUE_LARGE_INTESTINE = "TLGI"
    """Tissue large intestine"""
    TISSUE_LUNG = "TLNG"
    """Tissue lung"""
    SITE_TRACHEOSTOMY = "TRAC"
    """Site, Tracheostomy"""
    TRANSUDATE = "TRANS"
    """Transudate"""
    SERUM_TROUGH = "TSERU"
    """Serum, Trough"""
    TISSUE_SMALL_INTESTINE = "TSMI"
    """Tissue small intestine"""
    ABSCESS_TESTICULAR = "TSTES"
    """Abscess, Testicular"""
    ASPIRATE_TRANSTRACHEAL = "TTRA"
    """Aspirate, Transtracheal"""
    TUBE_NOS = "TUB"
    """Tube NOS"""
    TUBES = "TUBES"
    """Tubes"""
    TUMOR = "TUMOR"
    """Tumor"""
    SMEAR_TZANCK = "TZANC"
    """Smear, Tzanck"""
    SOURCE_UNIDENTIFIED = "UDENT"
    """Source, Unidentified"""
    ULCER = "ULC"
    """Ulcer"""
    UMBILICAL_BLOOD = "UMB"
    """Umbilical blood"""
    UNKNOWN_MEDICINE = "UMED"
    """Unknown medicine"""
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
    URINE_SEDIMENT = "URNS"
    """Urine sediment"""
    URINE_CATHETER = "URT"
    """Urine catheter"""
    URETHRA = "URTH"
    """Urethra"""
    URINE_CYSTOSCOPY = "USCOP"
    """Urine, Cystoscopy"""
    SOURCE_UNSPECIFIED = "USPEC"
    """Source, Unspecified"""
    UNKNOWN_SUBSTANCE = "USUB"
    """Unknown substance"""
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
    LEUKOCYTES = "WBC"
    """Leukocytes"""
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
    TO_BE_SPECIFIED_IN_ANOTHER_PART_OF_THE_MESSAGE = "XXX"
    """To be specified in another part of the message"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenSourceCodes.ABSCESS: "Abscess",
    SpecimenSourceCodes.TISSUE_ACNE: "Tissue, Acne",
    SpecimenSourceCodes.FLUID_ACNE: "Fluid, Acne",
    SpecimenSourceCodes.AIR_SAMPLE: "Air Sample",
    SpecimenSourceCodes.ALLOGRAFT: "Allograft",
    SpecimenSourceCodes.AMNIOTIC_FLUID: "Amniotic fluid",
    SpecimenSourceCodes.AMPUTATION: "Amputation",
    SpecimenSourceCodes.CATHETER_TIP_ANGIO: "Catheter Tip, Angio",
    SpecimenSourceCodes.CATHETER_TIP_ARTERIAL: "Catheter Tip, Arterial",
    SpecimenSourceCodes.SERUM_ACUTE: "Serum, Acute",
    SpecimenSourceCodes.ASPIRATE: "Aspirate",
    SpecimenSourceCodes.ENVIRONMENTAL_AUTOCLAVE_AMPULE: "Environmental, Autoclave Ampule",
    SpecimenSourceCodes.ENVIRONMENT_ATTEST: "Environment, Attest",
    SpecimenSourceCodes.AUTOPSY: "Autopsy",
    SpecimenSourceCodes.BLOOD_BAG: "Blood bag",
    SpecimenSourceCodes.CYST_BAKERS: "Cyst, Bakers",
    SpecimenSourceCodes.WHOLE_BODY: "Whole body",
    SpecimenSourceCodes.BILE_FLUID: "Bile fluid",
    SpecimenSourceCodes.BITE: "Bite",
    SpecimenSourceCodes.WHOLE_BLOOD: "Whole blood",
    SpecimenSourceCodes.BLOOD_ARTERIAL: "Blood arterial",
    SpecimenSourceCodes.BLOOD_CAPILLARY: "Blood capillary",
    SpecimenSourceCodes.CORD_BLOOD: "Cord blood",
    SpecimenSourceCodes.BLOOD_VENOUS: "Blood venous",
    SpecimenSourceCodes.BLEB: "Bleb",
    SpecimenSourceCodes.BLISTER: "Blister",
    SpecimenSourceCodes.BOIL: "Boil",
    SpecimenSourceCodes.BONE: "Bone",
    SpecimenSourceCodes.BOWEL_CONTENTS: "Bowel contents",
    SpecimenSourceCodes.BASOPHILS: "Basophils",
    SpecimenSourceCodes.BLOOD_PRODUCT_UNIT: "Blood product unit",
    SpecimenSourceCodes.BURN: "Burn",
    SpecimenSourceCodes.BRONCHIAL: "Bronchial",
    SpecimenSourceCodes.BRUSH: "Brush",
    SpecimenSourceCodes.BREATH: "Breath (use EXHLD)",
    SpecimenSourceCodes.BRUSHING: "Brushing",
    SpecimenSourceCodes.BUBO: "Bubo",
    SpecimenSourceCodes.BULLA_OR_BULLAE: "Bulla/Bullae",
    SpecimenSourceCodes.BIOPSY: "Biopsy",
    SpecimenSourceCodes.CALCULUS: "Calculus (=Stone)",
    SpecimenSourceCodes.CARBUNCLE: "Carbuncle",
    SpecimenSourceCodes.CATHETER: "Catheter",
    SpecimenSourceCodes.BITE_CAT: "Bite, Cat",
    SpecimenSourceCodes.CARDIAC_MUSCLE: "Cardiac muscle",
    SpecimenSourceCodes.CLIPPINGS: "Clippings",
    SpecimenSourceCodes.CONJUNCTIVA: "Conjunctiva",
    SpecimenSourceCodes.CANNULA: "Cannula",
    SpecimenSourceCodes.COLOSTRUM: "Colostrum",
    SpecimenSourceCodes.BIOSPY_CONE: "Biospy, Cone",
    SpecimenSourceCodes.SCRATCH_CAT: "Scratch, Cat",
    SpecimenSourceCodes.SERUM_CONVALESCENT: "Serum, Convalescent",
    SpecimenSourceCodes.CEREBRAL_SPINAL_FLUID: "Cerebral spinal fluid",
    SpecimenSourceCodes.CATHETER_INSERTION_SITE: "Catheter Insertion Site",
    SpecimenSourceCodes.FLUID_CYSTOSTOMY_TUBE: "Fluid, Cystostomy Tube",
    SpecimenSourceCodes.FLUID_CYST: "Fluid, Cyst",
    SpecimenSourceCodes.BLOOD_CELL_SAVER: "Blood, Cell Saver",
    SpecimenSourceCodes.CATHETER_TIP: "Catheter tip",
    SpecimenSourceCodes.CURETTAGE: "Curettage",
    SpecimenSourceCodes.CERVICAL_MUCUS: "Cervical mucus",
    SpecimenSourceCodes.SITE_CVP: "Site, CVP",
    SpecimenSourceCodes.CATHETER_TIP_CVP: "Catheter Tip, CVP",
    SpecimenSourceCodes.CERVIX: "Cervix",
    SpecimenSourceCodes.NODULE_CYSTIC: "Nodule, Cystic",
    SpecimenSourceCodes.CYST: "Cyst",
    SpecimenSourceCodes.BITE_DOG: "Bite, Dog",
    SpecimenSourceCodes.SPUTUM_DEEP_COUGH: "Sputum, Deep Cough",
    SpecimenSourceCodes.ULCER_DECUBITUS: "Ulcer, Decubitus",
    SpecimenSourceCodes.ENVIRONMENTAL_WATER: "Environmental, Water (Deionized)",
    SpecimenSourceCodes.DIALYSATE: "Dialysate",
    SpecimenSourceCodes.DIALYSIS_FLUID: "Dialysis fluid",
    SpecimenSourceCodes.DISCHARGE: "Discharge",
    SpecimenSourceCodes.DIVERTICULUM: "Diverticulum",
    SpecimenSourceCodes.DOSE_MED_OR_SUBSTANCE: "Dose med or substance",
    SpecimenSourceCodes.DRAIN: "Drain",
    SpecimenSourceCodes.DRAINAGE_TUBE: "Drainage, Tube",
    SpecimenSourceCodes.DRAINAGE_PENROSE: "Drainage, Penrose",
    SpecimenSourceCodes.DUODENAL_FLUID: "Duodenal fluid",
    SpecimenSourceCodes.EAR: "Ear",
    SpecimenSourceCodes.EAR_WAX: "Ear wax (cerumen)",
    SpecimenSourceCodes.BRUSH_ESOPHAGEAL: "Brush, Esophageal",
    SpecimenSourceCodes.ENVIRONMENTAL_EYE_WASH: "Environmental, Eye Wash",
    SpecimenSourceCodes.ENVIRONMENTAL_EFFLUENT: "Environmental, Effluent",
    SpecimenSourceCodes.EFFUSION: "Effusion",
    SpecimenSourceCodes.ENVIRONMENTAL_FOOD: "Environmental, Food",
    SpecimenSourceCodes.ENVIRONMENTAL_ISOLETTE: "Environmental, Isolette",
    SpecimenSourceCodes.ELECTRODE: "Electrode",
    SpecimenSourceCodes.ENDOCARDIUM: "Endocardium",
    SpecimenSourceCodes.ENDOMETRIUM: "Endometrium",
    SpecimenSourceCodes.ENVIRONMENTAL_UNIDENTIFIED_SUBSTANCE: "Environmental, Unidentified Substance",
    SpecimenSourceCodes.EOSINOPHILS: "Eosinophils",
    SpecimenSourceCodes.ENVIRONMENTAL_OTHER_SUBSTANCE: "Environmental, Other Substance",
    SpecimenSourceCodes.ENVIRONMENTAL_SOIL: "Environmental, Soil",
    SpecimenSourceCodes.ENVIRONMENTAL_SOLUTION: "Environmental, Solution (Sterile)",
    SpecimenSourceCodes.ASPIRATE_ENDOTRACH: "Aspirate, Endotrach",
    SpecimenSourceCodes.CATHETER_TIP_ENDOTRACHEAL: "Catheter Tip, Endotracheal",
    SpecimenSourceCodes.TUBE_ENDOTRACHEAL: "Tube, Endotracheal",
    SpecimenSourceCodes.ENVIRONMENTAL_WHIRLPOOL: "Environmental, Whirlpool",
    SpecimenSourceCodes.EXHALED_GAS: "Exhaled gas (=breath)",
    SpecimenSourceCodes.SHUNT_EXTERNAL: "Shunt, External",
    SpecimenSourceCodes.EXUDATE: "Exudate",
    SpecimenSourceCodes.EYE: "Eye",
    SpecimenSourceCodes.FAW: "Environmental, Water (Well)",
    SpecimenSourceCodes.BLOOD_FETAL: "Blood, Fetal",
    SpecimenSourceCodes.FLUID_ABDOMEN: "Fluid, Abdomen",
    SpecimenSourceCodes.FIBROBLASTS: "Fibroblasts",
    SpecimenSourceCodes.FISTULA: "Fistula",
    SpecimenSourceCodes.FLUID_OTHER: "Fluid, Other",
    SpecimenSourceCodes.FILTER: "Filter",
    SpecimenSourceCodes.BODY_FLUID_UNSP: "Body fluid, unsp",
    SpecimenSourceCodes.FLUID: "Fluid",
    SpecimenSourceCodes.CATHETER_TIP_FOLEY: "Catheter Tip, Foley",
    SpecimenSourceCodes.FLUID_RESPIRATORY: "Fluid, Respiratory",
    SpecimenSourceCodes.SCALP_FETAL: "Scalp, Fetal",
    SpecimenSourceCodes.FURUNCLE: "Furuncle",
    SpecimenSourceCodes.GAS: "Gas",
    SpecimenSourceCodes.ASPIRATE_GASTRIC: "Aspirate, Gastric",
    SpecimenSourceCodes.ANTRUM_GASTRIC: "Antrum, Gastric",
    SpecimenSourceCodes.BRUSHING_GASTRIC: "Brushing, Gastric",
    SpecimenSourceCodes.DRAINAGE_GASTRIC: "Drainage, Gastric",
    SpecimenSourceCodes.FLUID_OR_CONTENTS_GASTRIC: "Fluid/contents, Gastric",
    SpecimenSourceCodes.GENITAL: "Genital",
    SpecimenSourceCodes.GENITAL_CERVIX: "Genital cervix",
    SpecimenSourceCodes.GENITAL_LOCHIA: "Genital lochia",
    SpecimenSourceCodes.GENITAL_VAGINAL: "Genital vaginal",
    SpecimenSourceCodes.GRAFT: "Graft",
    SpecimenSourceCodes.GRANULOMA: "Granuloma",
    SpecimenSourceCodes.CATHETER_GROSHONG: "Catheter, Groshong",
    SpecimenSourceCodes.SOLUTION_GASTROSTOMY: "Solution, Gastrostomy",
    SpecimenSourceCodes.BIOPSY_GASTRIC: "Biopsy, Gastric",
    SpecimenSourceCodes.TUBE_GASTRIC: "Tube, Gastric",
    SpecimenSourceCodes.DRAINAGE_TUBE_DRAINAGE: "Drainage Tube, Drainage (Gastrostomy)",
    SpecimenSourceCodes.HAIR: "Hair",
    SpecimenSourceCodes.BITE_HUMAN: "Bite, Human",
    SpecimenSourceCodes.BLOOD_AUTOPSY: "Blood, Autopsy",
    SpecimenSourceCodes.CATHETER_TIP_HEMAQUIT: "Catheter Tip, Hemaquit",
    SpecimenSourceCodes.CATHETER_TIP_HEMOVAC: "Catheter Tip, Hemovac",
    SpecimenSourceCodes.TISSUE_HERNIATED: "Tissue, Herniated",
    SpecimenSourceCodes.DRAIN_HEMOVAC: "Drain, Hemovac",
    SpecimenSourceCodes.CATHETER_HICKMAN: "Catheter, Hickman",
    SpecimenSourceCodes.FLUID_HYDROCELE: "Fluid, Hydrocele",
    SpecimenSourceCodes.BITE_INSECT: "Bite, Insect",
    SpecimenSourceCodes.CYST_INCLUSION: "Cyst, Inclusion",
    SpecimenSourceCodes.CATHETER_TIP_INDWELLING: "Catheter Tip, Indwelling",
    SpecimenSourceCodes.GAS_INHALED: "Gas, Inhaled",
    SpecimenSourceCodes.DRAINAGE_ILEOSTOMY: "Drainage, Ileostomy",
    SpecimenSourceCodes.SOURCE_OF_SPECIMEN_IS_ILLEGIBLE: "Source of Specimen Is Illegible",
    SpecimenSourceCodes.IMPLANT: "Implant",
    SpecimenSourceCodes.SITE_INCISION_OR_SURGICAL: "Site, Incision/Surgical",
    SpecimenSourceCodes.INFILTRATE: "Infiltrate",
    SpecimenSourceCodes.INSECT: "Insect",
    SpecimenSourceCodes.CATHETER_TIP_INTRODUCER: "Catheter Tip, Introducer",
    SpecimenSourceCodes.ISOLATE: "Isolate",
    SpecimenSourceCodes.INTUBATION_TUBE: "Intubation tube",
    SpecimenSourceCodes.INTRAUTERINE_DEVICE: "Intrauterine Device",
    SpecimenSourceCodes.CATHETER_TIP_IV: "Catheter Tip, IV",
    SpecimenSourceCodes.FLUID_IV: "Fluid, IV",
    SpecimenSourceCodes.TUBING_TIP_IV: "Tubing Tip, IV",
    SpecimenSourceCodes.DRAINAGE_JEJUNAL: "Drainage, Jejunal",
    SpecimenSourceCodes.FLUID_JOINT: "Fluid, Joint",
    SpecimenSourceCodes.DRAINAGE_JACKSON_PRATT: "Drainage, Jackson Pratt",
    SpecimenSourceCodes.LAVAGE: "Lavage",
    SpecimenSourceCodes.FLUID_KIDNEY: "Fluid, Kidney",
    SpecimenSourceCodes.LAMELLA: "Lamella",
    SpecimenSourceCodes.LAVAGE_BRONHIAL: "Lavage, Bronhial",
    SpecimenSourceCodes.LAVAGE_GASTRIC: "Lavage, Gastric",
    SpecimenSourceCodes.LAVAGE_PERITONEAL: "Lavage, Peritoneal",
    SpecimenSourceCodes.LAVAGE_PRE_BRONCH: "Lavage, Pre-Bronch",
    SpecimenSourceCodes.CONTACT_LENS: "Contact Lens",
    SpecimenSourceCodes.CONTACT_LENS_CASE: "Contact Lens Case",
    SpecimenSourceCodes.LESION: "Lesion",
    SpecimenSourceCodes.LIQUID_NOS: "Liquid NOS",
    SpecimenSourceCodes.LIQUID_OTHER: "Liquid, Other",
    SpecimenSourceCodes.LINE: "Line",
    SpecimenSourceCodes.LINE_ARTERIAL: "Line arterial",
    SpecimenSourceCodes.LINE_VENOUS: "Line venous",
    SpecimenSourceCodes.FLUID_LUMBAR_SAC: "Fluid, Lumbar Sac",
    SpecimenSourceCodes.LYMPHOCYTES: "Lymphocytes",
    SpecimenSourceCodes.MACROPHAGES: "Macrophages",
    SpecimenSourceCodes.CATHETER_TIP_MAKURKOUR: "Catheter Tip, Makurkour",
    SpecimenSourceCodes.MARROW: "Marrow",
    SpecimenSourceCodes.MASS: "Mass",
    SpecimenSourceCodes.BLOOD_MENSTRUAL: "Blood, Menstrual",
    SpecimenSourceCodes.MECONIUM: "Meconium",
    SpecimenSourceCodes.BREAST_MILK: "Breast milk",
    SpecimenSourceCodes.MILK: "Milk",
    SpecimenSourceCodes.MUCOSA: "Mucosa",
    SpecimenSourceCodes.MUCUS: "Mucus",
    SpecimenSourceCodes.NAIL: "Nail",
    SpecimenSourceCodes.DRAINAGE_NASAL: "Drainage, Nasal",
    SpecimenSourceCodes.NEEDLE: "Needle",
    SpecimenSourceCodes.SITE_NEPHROSTOMY: "Site, Nephrostomy",
    SpecimenSourceCodes.ASPIRATE_NASOGASTRIC: "Aspirate, Nasogastric",
    SpecimenSourceCodes.DRAINAGE_NASOGASTRIC: "Drainage, Nasogastric",
    SpecimenSourceCodes.SITE_NASO_OR_GASTRIC: "Site, Naso/Gastric",
    SpecimenSourceCodes.NODULE: "Nodule(s)",
    SpecimenSourceCodes.NOSE: "Nose (nasal passage)",
    SpecimenSourceCodes.SECRETION_NASAL: "Secretion, Nasal",
    SpecimenSourceCodes.OTHER: "Other",
    SpecimenSourceCodes.LESION_ORAL: "Lesion, Oral",
    SpecimenSourceCodes.SOURCE_OTHER: "Source, Other",
    SpecimenSourceCodes.PACEMAKER: "Pacemaker",
    SpecimenSourceCodes.PANCREATIC_FLUID: "Pancreatic fluid",
    SpecimenSourceCodes.PATIENT: "Patient",
    SpecimenSourceCodes.FLUID_PERICARDIAL: "Fluid, Pericardial",
    SpecimenSourceCodes.SITE_PERITONEAL_DIALYSIS: "Site, Peritoneal Dialysis",
    SpecimenSourceCodes.SITE_PERITONEAL_DIALYSIS_TUNNEL: "Site, Peritoneal Dialysis Tunnel",
    SpecimenSourceCodes.ABSCESS_PELVIC: "Abscess, Pelvic",
    SpecimenSourceCodes.LESION_PENILE: "Lesion, Penile",
    SpecimenSourceCodes.ABSCESS_PERIANAL: "Abscess, Perianal",
    SpecimenSourceCodes.CYST_PILONIDAL: "Cyst, Pilonidal",
    SpecimenSourceCodes.SITE_PIN: "Site, Pin",
    SpecimenSourceCodes.SITE_PACEMAKER_INSETION: "Site, Pacemaker Insetion",
    SpecimenSourceCodes.PLANT_MATERIAL: "Plant Material",
    SpecimenSourceCodes.PLASMA: "Plasma",
    SpecimenSourceCodes.PLASMA_BAG: "Plasma bag",
    SpecimenSourceCodes.PLACENTA: "Placenta",
    SpecimenSourceCodes.SERUM_PEAK_LEVEL: "Serum, Peak Level",
    SpecimenSourceCodes.PLEURAL_FLUID: "Pleural fluid (thoracentesis fld)",
    SpecimenSourceCodes.POLYMORPHONUCLEAR_NEUTROPHILS: "Polymorphonuclear neutrophils",
    SpecimenSourceCodes.DRAINAGE_PENILE: "Drainage, Penile",
    SpecimenSourceCodes.POLYPS: "Polyps",
    SpecimenSourceCodes.GRAFT_SITE_POPLITEAL: "Graft Site, Popliteal",
    SpecimenSourceCodes.GRAFT_POPLITEAL: "Graft, Popliteal",
    SpecimenSourceCodes.SITE_POPLITEAL_VEIN: "Site, Popliteal Vein",
    SpecimenSourceCodes.CATHETER_PORTA: "Catheter, Porta",
    SpecimenSourceCodes.PLATELET_POOR_PLASMA: "Platelet poor plasma",
    SpecimenSourceCodes.PROSTHETIC_DEVICE: "Prosthetic Device",
    SpecimenSourceCodes.PLATELET_RICH_PLASMA: "Platelet rich plasma",
    SpecimenSourceCodes.PERITONEAL_FLUID_OR_ASCITES: "Peritoneal fluid /ascites",
    SpecimenSourceCodes.PSEUDOCYST: "Pseudocyst",
    SpecimenSourceCodes.WOUND_PUNCTURE: "Wound, Puncture",
    SpecimenSourceCodes.PUS: "Pus",
    SpecimenSourceCodes.PUSTULE: "Pustule",
    SpecimenSourceCodes.PUST: "Pus",
    SpecimenSourceCodes.QUALITY_CONTROL: "Quality Control",
    SpecimenSourceCodes.URINE_RANDOM: "Urine, Random",
    SpecimenSourceCodes.ERYTHROCYTES: "Erythrocytes",
    SpecimenSourceCodes.BITE_REPTILE: "Bite, Reptile",
    SpecimenSourceCodes.DRAINAGE_RECTAL: "Drainage, Rectal",
    SpecimenSourceCodes.ABSCESS_RECTAL: "Abscess, Rectal",
    SpecimenSourceCodes.CYST_RENAL: "Cyst, Renal",
    SpecimenSourceCodes.FLUID_RENAL_CYST: "Fluid, Renal Cyst",
    SpecimenSourceCodes.RESPIRATORY: "Respiratory",
    SpecimenSourceCodes.ROUTE_OF_MEDICINE: "Route of medicine",
    SpecimenSourceCodes.SALIVA: "Saliva",
    SpecimenSourceCodes.TISSUE_KELOID: "Tissue, Keloid (Scar)",
    SpecimenSourceCodes.CATHETER_TIP_SUBCLAVIAN: "Catheter Tip, Subclavian",
    SpecimenSourceCodes.ABSCESS_SCROTAL: "Abscess, Scrotal",
    SpecimenSourceCodes.SECRETION: "Secretion(s)",
    SpecimenSourceCodes.SERUM: "Serum",
    SpecimenSourceCodes.SITE_SHUNT: "Site, Shunt",
    SpecimenSourceCodes.FLUID_SHUNT: "Fluid, Shunt",
    SpecimenSourceCodes.SHUNT: "Shunt",
    SpecimenSourceCodes.SITE: "Site",
    SpecimenSourceCodes.BIOPSY_SKIN: "Biopsy, Skin",
    SpecimenSourceCodes.SKELETAL_MUSCLE: "Skeletal muscle",
    SpecimenSourceCodes.SKIN: "Skin",
    SpecimenSourceCodes.MASS_SUB_MANDIBULAR: "Mass, Sub-Mandibular",
    SpecimenSourceCodes.SEMINAL_FLUID: "Seminal fluid",
    SpecimenSourceCodes.SYNOVIAL_FLUID: "Synovial fluid (Joint fluid)",
    SpecimenSourceCodes.SPERMATOZOA: "Spermatozoa",
    SpecimenSourceCodes.CATHETER_TIP_SUPRAPUBIC: "Catheter Tip, Suprapubic",
    SpecimenSourceCodes.CATHETHER_TIP_SUPRAPUBIC: "Cathether Tip, Suprapubic",
    SpecimenSourceCodes.ENVIRONMENTAL_SPORE_STRIP: "Environmental, Spore Strip",
    SpecimenSourceCodes.SPUTUM: "Sputum",
    SpecimenSourceCodes.SPUTUM_COUGHED: "Sputum - coughed",
    SpecimenSourceCodes.SPUTUM_TRACHEAL_ASPIRATE: "Sputum - tracheal aspirate",
    SpecimenSourceCodes.SPUTUM_SIMULATED: "Sputum, Simulated",
    SpecimenSourceCodes.SPUTUM_INDUCTED: "Sputum, Inducted",
    SpecimenSourceCodes.SPUTUM_SPONTANEOUS: "Sputum, Spontaneous",
    SpecimenSourceCodes.ENVIRONMENTAL_STERRAD: "Environmental, Sterrad",
    SpecimenSourceCodes.STOOL_EQUALS_FECAL: "Stool = Fecal",
    SpecimenSourceCodes.STONE: "Stone (use CALC)",
    SpecimenSourceCodes.STONE_KIDNEY: "Stone, Kidney",
    SpecimenSourceCodes.ABSCESS_SUBMANDIBULAR: "Abscess, Submandibular",
    SpecimenSourceCodes.ABSCESS_SUBMAXILLARY: "Abscess, Submaxillary",
    SpecimenSourceCodes.DRAINAGE_SUMP: "Drainage, Sump",
    SpecimenSourceCodes.SUPRAPUBIC_TAP: "Suprapubic Tap",
    SpecimenSourceCodes.SUTURE: "Suture",
    SpecimenSourceCodes.CATHETER_TIP_SWAN_GANTZ: "Catheter Tip, Swan Gantz",
    SpecimenSourceCodes.SWEAT: "Sweat",
    SpecimenSourceCodes.ASPIRATE_TRACHEAL: "Aspirate, Tracheal",
    SpecimenSourceCodes.TEARS: "Tears",
    SpecimenSourceCodes.THROMBOCYTE: "Thrombocyte (platelet)",
    SpecimenSourceCodes.THROAT: "Throat",
    SpecimenSourceCodes.TISSUE_GALL_BLADDER: "Tissue gall bladder",
    SpecimenSourceCodes.TISSUE_PLACENTA: "Tissue placenta",
    SpecimenSourceCodes.TISSUE: "Tissue",
    SpecimenSourceCodes.TISSUE_ULCER: "Tissue ulcer",
    SpecimenSourceCodes.CATHETHER_TIP_TRIPLE_LUMEN: "Cathether Tip, Triple Lumen",
    SpecimenSourceCodes.TISSUE_LARGE_INTESTINE: "Tissue large intestine",
    SpecimenSourceCodes.TISSUE_LUNG: "Tissue lung",
    SpecimenSourceCodes.SITE_TRACHEOSTOMY: "Site, Tracheostomy",
    SpecimenSourceCodes.TRANSUDATE: "Transudate",
    SpecimenSourceCodes.SERUM_TROUGH: "Serum, Trough",
    SpecimenSourceCodes.TISSUE_SMALL_INTESTINE: "Tissue small intestine",
    SpecimenSourceCodes.ABSCESS_TESTICULAR: "Abscess, Testicular",
    SpecimenSourceCodes.ASPIRATE_TRANSTRACHEAL: "Aspirate, Transtracheal",
    SpecimenSourceCodes.TUBE_NOS: "Tube NOS",
    SpecimenSourceCodes.TUBES: "Tubes",
    SpecimenSourceCodes.TUMOR: "Tumor",
    SpecimenSourceCodes.SMEAR_TZANCK: "Smear, Tzanck",
    SpecimenSourceCodes.SOURCE_UNIDENTIFIED: "Source, Unidentified",
    SpecimenSourceCodes.ULCER: "Ulcer",
    SpecimenSourceCodes.UMBILICAL_BLOOD: "Umbilical blood",
    SpecimenSourceCodes.UNKNOWN_MEDICINE: "Unknown medicine",
    SpecimenSourceCodes.URINE: "Urine",
    SpecimenSourceCodes.URINE_CLEAN_CATCH: "Urine clean catch",
    SpecimenSourceCodes.URINE_BLADDER_WASHINGS: "Urine, Bladder Washings",
    SpecimenSourceCodes.URINE_CATHETERIZED: "Urine, Catheterized",
    SpecimenSourceCodes.URINE_MIDSTREAM: "Urine, Midstream",
    SpecimenSourceCodes.URINE_NEPHROSTOMY: "Urine, Nephrostomy",
    SpecimenSourceCodes.URINE_PEDIBAG: "Urine, Pedibag",
    SpecimenSourceCodes.URINE_SEDIMENT: "Urine sediment",
    SpecimenSourceCodes.URINE_CATHETER: "Urine catheter",
    SpecimenSourceCodes.URETHRA: "Urethra",
    SpecimenSourceCodes.URINE_CYSTOSCOPY: "Urine, Cystoscopy",
    SpecimenSourceCodes.SOURCE_UNSPECIFIED: "Source, Unspecified",
    SpecimenSourceCodes.UNKNOWN_SUBSTANCE: "Unknown substance",
    SpecimenSourceCodes.CATHETER_TIP_VAS: "Catheter Tip, Vas",
    SpecimenSourceCodes.CATHETER_TIP_VENTRICULAR: "Catheter Tip, Ventricular",
    SpecimenSourceCodes.VITREOUS_FLUID: "Vitreous Fluid",
    SpecimenSourceCodes.VOMITUS: "Vomitus",
    SpecimenSourceCodes.WASH: "Wash",
    SpecimenSourceCodes.WASHING_E_G_BRONCHIAL_WASHING: "Washing, e.g. bronchial washing",
    SpecimenSourceCodes.WATER: "Water",
    SpecimenSourceCodes.BLOOD_WHOLE: "Blood, Whole",
    SpecimenSourceCodes.LEUKOCYTES: "Leukocytes",
    SpecimenSourceCodes.WEN: "Wen",
    SpecimenSourceCodes.WICK: "Wick",
    SpecimenSourceCodes.WOUND: "Wound",
    SpecimenSourceCodes.WOUND_ABSCESS: "Wound abscess",
    SpecimenSourceCodes.WOUND_DRAINAGE: "Wound drainage",
    SpecimenSourceCodes.WOUND_EXUDATE: "Wound exudate",
    SpecimenSourceCodes.WORM: "Worm",
    SpecimenSourceCodes.WART: "Wart",
    SpecimenSourceCodes.WWA: "Environmental, Water",
    SpecimenSourceCodes.WWO: "Environmental, Water (Ocean)",
    SpecimenSourceCodes.WWT: "Environmental, Water (Tap)",
    SpecimenSourceCodes.TO_BE_SPECIFIED_IN_ANOTHER_PART_OF_THE_MESSAGE: "To be specified in another part of the message",
}
