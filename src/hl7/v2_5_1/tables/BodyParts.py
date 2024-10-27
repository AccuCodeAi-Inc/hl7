from ...base import HL7Table

"""
HL7 Version: 2.5.1
Body Parts - 0550
Table Type: HL7
"""


class BodyParts(HL7Table):
    """
    Body Parts - 0550 // HL7 table type
    - ACETABULUM
    - ACHILLES
    - ABDOMEN
    - ADENOIDS
    - ADRENAL
    - AMNIOTIC_FLUID
    - AMNIOTIC_SAC
    - ANAL
    - ANKLE
    - ANTECUBITAL
    - ANTECUBITAL_FOSSA
    - ANTRUM
    - ANUS
    - AORTA
    - APPENDIX
    - AORTIC_RIM
    - AREOLA
    - ARM
    - ARTERY
    - ASCITES
    - ASCITIC_FLUID
    - ATRIUM
    - AURICULAR
    - AORTIC_VALVE
    - AXILLA
    - BACK
    - BARTHOLIN_DUCT
    - BARTHOLIN_GLAND
    - BRAIN_CYST_FLUID
    - BODY_WHOLE
    - BILE_DUCT
    - BILE_FLUID
    - BLADDER
    - BLOOD_WHOLE
    - BLOOD_ARTERIAL
    - BLOOD_CAPILLARY
    - BLOOD_VENOUS
    - BLOOD
    - BONE_MARROW
    - BONE
    - BOWEL
    - BOWEL_LARGE
    - BOWEL_SMALL
    - BASOPHILS
    - BRACHIAL
    - BRAIN
    - BRONCHIAL
    - BRONCHIOLE_OR_BRONCHIOLAR
    - BRONCHUS_OR_BRONCHIAL
    - EYEBROW
    - BREAST
    - BREAST_FLUID
    - BARTHOLIN_GLAND_FLUID
    - BROVIAC
    - BUCCAL
    - BURSA
    - BURSA_FLUID
    - BUTTOCKS
    - CALF
    - CANAL
    - CANALICULIS
    - CANTHUS
    - CAROTID
    - CARPAL
    - CAVITY
    - BLOOD_CORD
    - CARDIAC_MUSCLE
    - COMMON_DUCT
    - CECUM_OR_CECAL
    - CERVIX_OR_UTERUS
    - CAVITY_CHEST
    - CHEEK
    - CHEST
    - CHEST_TUBE
    - CHIN
    - CIRCUMCISION_SITE
    - CLAVICLE_OR_CLAVICULAR
    - CLITORIS
    - CLITORAL
    - CANNULA
    - COCCYGEAL
    - COCCYX
    - COLON
    - COLOSTOMY
    - CONJUNCTIVA
    - CORD
    - CORAL
    - CORD_BLOOD
    - CORNEA
    - COLOSTOMY_STOMA
    - CRANIUM_ETHMOID
    - CRANIUM_FRONTAL
    - CRANIUM_OCCIPITAL
    - CRANIUM_PARIETAL
    - CRANIUM_SPHENOID
    - CRANIUM_TEMPORAL
    - CEREBRAL_SPINAL_FLUID
    - CUBITUS
    - CUFF
    - CUL_DE_SAC
    - CULDOCENTESIS
    - CERVIX
    - DELTOID
    - DENTAL_GINGIVA
    - DENTAL
    - DIALYSIS_FLUID
    - DIGIT
    - DISC
    - DORSUM_OR_DORSAL
    - DIAPHRAGM
    - DUODENAL_FLUID
    - DUODENUM_OR_DUODENAL
    - DURA
    - EAR
    - EAR_BONE_INCUS
    - EAR_BONE_MALLEUS
    - EAR_BONE_STAPES
    - EAR_LOBE
    - ENDOCERVICAL
    - ELBOW
    - ELBOW_JOINT
    - ENDOCARDIUM
    - ENDOMETRIUM
    - ENDOLPTHAMITIS
    - EOSINOPHILS
    - EPIDIDYMIS
    - EPICARDIAL
    - EPICARDIUM
    - EPIDURAL
    - EPIGLOTTIS
    - ESOPHAGUS
    - ESOPHAGEAL
    - ENDOTRACHEAL
    - ETHMOID
    - ENDOURETHRAL
    - EYE
    - EYELID
    - FACE
    - FALLOPIAN_TUBE
    - FACIAL_BONE_INFERIOR_NASAL_CONCHA
    - FACIAL_BONE_LACRIMAL
    - FACIAL_BONE_MAXILLA
    - FACIAL_BONE_NASAL
    - FACIAL_BONE_PALATINE
    - FACIAL_BONE_VOMER
    - FACIAL_BONE_ZYGOMATIC
    - FEMORAL
    - FEMUR
    - FETUS
    - FIBULA
    - FINGER
    - FINGER_NAIL
    - FEMORAL_HEAD
    - FOLLICLE
    - FOOT
    - FOREARM
    - FOREHEAD
    - FORESKIN
    - FOURCHETTE
    - GALL_BLADDER
    - GENITAL
    - GENITAL_CERVIX
    - GENITAL_LOCHIA
    - GENITAL_LESION
    - GLAND
    - GLANS
    - GLUTEUS
    - GLUTEAL
    - GLUTEUS_MEDIUS
    - GROIN
    - GUM
    - GENITAL_VULVA
    - HALLUX
    - HAND
    - HAIR
    - HEART
    - HEAD
    - HEEL
    - HEMORRHOID
    - HIP
    - HIP_JOINT
    - HUMERUS
    - HEART_VALVE
    - HEART_VALVE_BICUSPID
    - HEART_VALVE_TRICUSPID
    - HYMEN
    - INTRACERVICAL
    - ILEAL_CONDUIT
    - ILICAL_CONDUIT
    - ILIAC_CREST
    - ILEAL_LOOP
    - ILEOSTOMY
    - ILEUM
    - ILIAC
    - INTRANASAL
    - INGUINAL
    - INTESTINE_LARGE
    - INTESTINE_SMALL
    - INTESTINE
    - INTROITUS
    - INTRAUTERINE
    - ISCHIUM
    - LOOP_ISHIAL
    - JAW
    - JUGULAR_INTERNAL
    - KIDNEY
    - KNEE
    - KNEE_FLUID
    - KNEE_JOINT
    - LABIA
    - LABIA_MAJORA
    - LABIA_MINORA
    - LACRIMAL
    - LAMELLA
    - LARYNX
    - LEG
    - LENS
    - LINGUAL
    - LINGULA
    - LIP
    - LIVER
    - LUMEN
    - LYMPH_NODE
    - LYMPH_NODE_GROIN
    - LOBE
    - LOCHIA
    - LUMBAR
    - LUNG
    - LYMPHOCYTES
    - MACROPHAGES
    - MALLEOLUS
    - MANDIBLE_OR_MANDIBULAR
    - MARROW
    - MASTOID
    - MAXILLA_OR_MAXILLARY
    - MAXILLARY_SINUS
    - MEATUS
    - MECONIUM
    - MEDIASTINUM
    - MEDULLARY
    - METACARPAL
    - METATARSAL
    - MILK_BREAST
    - MITRAL_VALVE
    - MOLAR
    - MONS_URETERIS
    - MONS_VENERIS
    - MEMBRANE
    - MOUTH
    - MONS_PUBIS
    - MENINGES
    - MRSA
    - MYOCARDIUM
    - NAIL
    - NAIL_BED
    - NAIL_FINGER
    - NAIL_TOE
    - NARES
    - NASAL
    - NAVEL
    - NECK
    - NERVE
    - NIPPLE
    - NASOLACRIMAL
    - NOSE
    - NOSE_
    - NOSE__
    - NOSTRIL
    - NASOPHARYNGEAL
    - NASOPHARYNX
    - NASAL_SEPTUM
    - NASOTRACHEAL
    - OCCIPITAL
    - OLECRANON
    - OMENTUM
    - ORBIT_OR_ORBITAL
    - OROPHARYNX
    - OS_COXA
    - OVARY
    - PANCREATIC_FLUID
    - PALATE
    - PALM
    - PERIANAL_OR_PERIRECTAL
    - PANCREAS
    - PARATRACHEAL
    - PARIETAL
    - PARONYCHIA
    - PAROTID
    - PAROTID_GLAND
    - PARASTERNAL
    - PATELLA
    - PERICARDIUM
    - PERICLITORAL
    - PELVIS
    - PENIS
    - PENILE_SHAFT
    - PERITONEAL
    - PERICARDIAL_FLUID
    - PERIHEPATIC
    - PERINEAL_ABSCESS
    - PERISPLENIC
    - PERITONEUM
    - PERIURETHAL
    - PERIVESICULAR
    - PERIRECTAL
    - PERITONEAL_FLUID
    - PHALANYX
    - PILONIDAL
    - PINNA
    - PLACENTA
    - PLACM
    - PLANTAR
    - PALATE_HARD
    - PALATE_SOFT
    - PLC
    - PLEURAL_FLUID
    - PLEURA
    - PLR
    - PERINEAL
    - PERINEPHRIC
    - PERINEUM
    - POPLITEAL
    - PERIORBITAL
    - PREAURICULAR
    - PRERENAL
    - PROSTATIC_FLUID
    - PROSTATE_GLAND
    - PERITONSILLAR
    - PUBIC
    - PULMONARY_ARTERY
    - RADIAL
    - RADIUS
    - RED_BLOOD_CELLS
    - RECTAL
    - RECTUM
    - RENAL
    - RIB
    - RENAL_PELVIS
    - RETROPERITONEAL
    - UTERINE_CUL_OR_DE_OR_SAC
    - SACROILIAC
    - SACRAL
    - SACROCOCCYGEAL
    - SACRUM
    - SALIVARY_GLAND
    - SCALP
    - SCAPULA_OR_SCAPULAR
    - SUPRACLAVICLE_OR_SUPRACLAVICULAR
    - SCLERA
    - SUB_CLAVIAN
    - SCROTUM_OR_SCROTAL
    - SUBDIAPHRAMATIC
    - SEMINAL_FLUID
    - SEMEN
    - SEPTUM_OR_SEPTAL
    - SEROMA
    - SUBGALEAL_FLUID
    - SHIN
    - SHOULDER
    - SHOLDER_JOINT
    - SIGMOID
    - SINUS
    - SKENES_GLAND
    - SKELETAL_MUSCLE
    - SKULL
    - SOLE
    - SPINAL_CORD
    - SPHENOID
    - SPLEEN
    - SPERMATOZOA
    - SUPRA_CERVICAL
    - STERNUM_OR_STERNAL
    - STOMA
    - STOMACH
    - LIQUID_STOOL
    - STUMP
    - SUBDURAL
    - SUBDURAL_FLUID
    - SUBMANDIBULAR
    - SUBMENTAL
    - SUBPHRENIC
    - SUBMAXILLARY
    - SUPRAPUBIC_SPECIMEN
    - SUPRAPUBIC
    - SWEAT
    - SWEAT_GLAND
    - SYNOVIAL_FLUID
    - SYNOVIAL
    - SYNOVIUM
    - TARSAL
    - TRANSBRONCHIAL
    - TRANSCARINA_ASP
    - TEAR_DUCT
    - TEARS
    - TEMPLE
    - TEMPORAL
    - TESTICLE
    - THIGH
    - THYMUS
    - THORACENTESIS
    - THORAX_OR_THORACIC
    - THROAT
    - THUMB
    - THYROID
    - TIBIA
    - TEMPORAL_LOBE
    - THUMBNAIL
    - TOE
    - TOE_NAIL
    - TONGUE
    - TONSIL
    - TOOTH
    - TRACHEA_OR_TRACHEAL
    - TOOTH_SOCKET
    - ULNA_OR_ULNAR
    - UMBILICAL_BLOOD
    - UMBILICUS
    - UMBILICUS_OR_UMBILICAL
    - URETER
    - URETHRA
    - STOMA_URINARY
    - UTERUS
    - UTERINE
    - VAGINA_OR_VAGINAL
    - VALVE
    - VAS_DEFERENS
    - VASTUS_LATERALIS
    - VAULT
    - VENTRICULAR_CSF
    - VAGINAL_CUFF
    - VEIN
    - VENTRAGLUTEAL
    - VERMIS_CEREBELLI
    - VERTEBRA_CERVICAL
    - VERTEBRA_LUMBAR
    - VERTEBRA_THORACIC
    - VESICULAR
    - VESICULAR_FLUID
    - VESICLE
    - VESTIBULE
    - VAGINAL_VAULT
    - VITREOUS_FLUID
    - VOCAL_CORD
    - VULVA
    - LEUKOCYTES
    - WRIST
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0550
    """

    ACETABULUM = "ACET"
    """Acetabulum"""
    ACHILLES = "ACHIL"
    """Achilles"""
    ABDOMEN = "ADB"
    """Abdomen"""
    ADENOIDS = "ADE"
    """Adenoids"""
    ADRENAL = "ADR"
    """Adrenal"""
    AMNIOTIC_FLUID = "AMN"
    """Amniotic fluid"""
    AMNIOTIC_SAC = "AMS"
    """Amniotic Sac"""
    ANAL = "ANAL"
    """Anal"""
    ANKLE = "ANKL"
    """Ankle"""
    ANTECUBITAL = "ANTEC"
    """Antecubital"""
    ANTECUBITAL_FOSSA = "ANTECF"
    """Antecubital Fossa"""
    ANTRUM = "ANTR"
    """Antrum"""
    ANUS = "ANUS"
    """Anus"""
    AORTA = "AORTA"
    """Aorta"""
    APPENDIX = "APDX"
    """Appendix"""
    AORTIC_RIM = "AR"
    """Aortic Rim"""
    AREOLA = "AREO"
    """Areola"""
    ARM = "ARM"
    """Arm"""
    ARTERY = "ARTE"
    """Artery"""
    ASCITES = "ASCIT"
    """Ascites"""
    ASCITIC_FLUID = "ASCT"
    """Ascitic Fluid"""
    ATRIUM = "ATR"
    """Atrium"""
    AURICULAR = "AURI"
    """Auricular"""
    AORTIC_VALVE = "AV"
    """Aortic Valve"""
    AXILLA = "AXI"
    """Axilla"""
    BACK = "BACK"
    """Back"""
    BARTHOLIN_DUCT = "BARTD"
    """Bartholin Duct"""
    BARTHOLIN_GLAND = "BARTG"
    """Bartholin Gland"""
    BRAIN_CYST_FLUID = "BCYS"
    """Brain Cyst Fluid"""
    BODY_WHOLE = "BDY"
    """Body, Whole"""
    BILE_DUCT = "BID"
    """Bile Duct"""
    BILE_FLUID = "BIFL"
    """Bile fluid"""
    BLADDER = "BLAD"
    """Bladder"""
    BLOOD_WHOLE = "BLD"
    """Blood, Whole"""
    BLOOD_ARTERIAL = "BLDA"
    """Blood, Arterial"""
    BLOOD_CAPILLARY = "BLDC"
    """Blood, Capillary"""
    BLOOD_VENOUS = "BLDV"
    """Blood, Venous"""
    BLOOD = "BLOOD"
    """Blood"""
    BONE_MARROW = "BMAR"
    """Bone marrow"""
    BONE = "BON"
    """Bone"""
    BOWEL = "BOWEL"
    """Bowel"""
    BOWEL_LARGE = "BOWLA"
    """Bowel, Large"""
    BOWEL_SMALL = "BOWSM"
    """Bowel, Small"""
    BASOPHILS = "BPH"
    """Basophils"""
    BRACHIAL = "BRA"
    """Brachial"""
    BRAIN = "BRAIN"
    """Brain"""
    BRONCHIAL = "BRO"
    """Bronchial"""
    BRONCHIOLE_OR_BRONCHIOLAR = "BROCH"
    """Bronchiole/Bronchiolar"""
    BRONCHUS_OR_BRONCHIAL = "BRONC"
    """Bronchus/Bronchial"""
    EYEBROW = "BROW"
    """Eyebrow"""
    BREAST = "BRST"
    """Breast"""
    BREAST_FLUID = "BRSTFL"
    """Breast fluid"""
    BARTHOLIN_GLAND_FLUID = "BRTGF"
    """Bartholin Gland Fluid"""
    BROVIAC = "BRV"
    """Broviac"""
    BUCCAL = "BUCCA"
    """Buccal"""
    BURSA = "BURSA"
    """Bursa"""
    BURSA_FLUID = "BURSF"
    """Bursa Fluid"""
    BUTTOCKS = "BUTT"
    """Buttocks"""
    CALF = "CALF"
    """Calf"""
    CANAL = "CANAL"
    """Canal"""
    CANALICULIS = "CANLI"
    """Canaliculis"""
    CANTHUS = "CANTH"
    """Canthus"""
    CAROTID = "CARO"
    """Carotid"""
    CARPAL = "CARP"
    """Carpal"""
    CAVITY = "CAVIT"
    """Cavity"""
    BLOOD_CORD = "CBLD"
    """Blood, Cord"""
    CARDIAC_MUSCLE = "CDM"
    """Cardiac Muscle"""
    COMMON_DUCT = "CDUCT"
    """Common Duct"""
    CECUM_OR_CECAL = "CECUM"
    """Cecum/Cecal"""
    CERVIX_OR_UTERUS = "CERVUT"
    """Cervix/Uterus"""
    CAVITY_CHEST = "CHE"
    """Cavity, Chest"""
    CHEEK = "CHEEK"
    """Cheek"""
    CHEST = "CHES"
    """Chest"""
    CHEST_TUBE = "CHEST"
    """Chest Tube"""
    CHIN = "CHIN"
    """Chin"""
    CIRCUMCISION_SITE = "CIRCU"
    """Circumcision Site"""
    CLAVICLE_OR_CLAVICULAR = "CLAVI"
    """Clavicle/Clavicular"""
    CLITORIS = "CLIT"
    """Clitoris"""
    CLITORAL = "CLITO"
    """Clitoral"""
    CANNULA = "CNL"
    """Cannula"""
    COCCYGEAL = "COCCG"
    """Coccygeal"""
    COCCYX = "COCCY"
    """Coccyx"""
    COLON = "COLON"
    """Colon"""
    COLOSTOMY = "COLOS"
    """Colostomy"""
    CONJUNCTIVA = "CONJ"
    """Conjunctiva"""
    CORD = "COR"
    """Cord"""
    CORAL = "CORAL"
    """Coral"""
    CORD_BLOOD = "CORD"
    """Cord Blood"""
    CORNEA = "CORN"
    """Cornea"""
    COLOSTOMY_STOMA = "COS"
    """Colostomy Stoma"""
    CRANIUM_ETHMOID = "CRANE"
    """Cranium, ethmoid"""
    CRANIUM_FRONTAL = "CRANF"
    """Cranium, frontal"""
    CRANIUM_OCCIPITAL = "CRANO"
    """Cranium, occipital"""
    CRANIUM_PARIETAL = "CRANP"
    """Cranium, parietal"""
    CRANIUM_SPHENOID = "CRANS"
    """Cranium, sphenoid"""
    CRANIUM_TEMPORAL = "CRANT"
    """Cranium, temporal"""
    CEREBRAL_SPINAL_FLUID = "CSF"
    """Cerebral Spinal Fluid"""
    CUBITUS = "CUBIT"
    """Cubitus"""
    CUFF = "CUFF"
    """Cuff"""
    CUL_DE_SAC = "CULD"
    """Cul De Sac"""
    CULDOCENTESIS = "CULDO"
    """Culdocentesis"""
    CERVIX = "CVX"
    """Cervix"""
    DELTOID = "DELT"
    """Deltoid"""
    DENTAL_GINGIVA = "DEN"
    """Dental Gingiva"""
    DENTAL = "DENTA"
    """Dental"""
    DIALYSIS_FLUID = "DIAF"
    """Dialysis Fluid"""
    DIGIT = "DIGIT"
    """Digit"""
    DISC = "DISC"
    """Disc"""
    DORSUM_OR_DORSAL = "DORS"
    """Dorsum/Dorsal"""
    DIAPHRAGM = "DPH"
    """Diaphragm"""
    DUODENAL_FLUID = "DUFL"
    """Duodenal Fluid"""
    DUODENUM_OR_DUODENAL = "DUODE"
    """Duodenum/Duodenal"""
    DURA = "DUR"
    """Dura"""
    EAR = "EAR"
    """Ear"""
    EAR_BONE_INCUS = "EARBI"
    """Ear bone, incus"""
    EAR_BONE_MALLEUS = "EARBM"
    """Ear bone, malleus"""
    EAR_BONE_STAPES = "EARBS"
    """Ear bone,stapes"""
    EAR_LOBE = "EARLO"
    """Ear Lobe"""
    ENDOCERVICAL = "EC"
    """Endocervical"""
    ELBOW = "ELBOW"
    """Elbow"""
    ELBOW_JOINT = "ELBOWJ"
    """Elbow Joint"""
    ENDOCARDIUM = "ENDC"
    """Endocardium"""
    ENDOMETRIUM = "ENDM"
    """Endometrium"""
    ENDOLPTHAMITIS = "EOLPH"
    """endolpthamitis"""
    EOSINOPHILS = "EOS"
    """Eosinophils"""
    EPIDIDYMIS = "EPD"
    """Epididymis"""
    EPICARDIAL = "EPICA"
    """Epicardial"""
    EPICARDIUM = "EPICM"
    """Epicardium"""
    EPIDURAL = "EPIDU"
    """Epidural"""
    EPIGLOTTIS = "EPIGL"
    """Epiglottis"""
    ESOPHAGUS = "ESO"
    """Esophagus"""
    ESOPHAGEAL = "ESOPG"
    """Esophageal"""
    ENDOTRACHEAL = "ET"
    """Endotracheal"""
    ETHMOID = "ETHMO"
    """Ethmoid"""
    ENDOURETHRAL = "EUR"
    """Endourethral"""
    EYE = "EYE"
    """Eye"""
    EYELID = "EYELI"
    """Eyelid"""
    FACE = "FACE"
    """Face"""
    FALLOPIAN_TUBE = "FALLT"
    """Fallopian Tube"""
    FACIAL_BONE_INFERIOR_NASAL_CONCHA = "FBINC"
    """Facial bone, inferior nasal concha"""
    FACIAL_BONE_LACRIMAL = "FBLAC"
    """Facial bone, lacrimal"""
    FACIAL_BONE_MAXILLA = "FBMAX"
    """Facial bone, maxilla"""
    FACIAL_BONE_NASAL = "FBNAS"
    """Facial bone, nasal"""
    FACIAL_BONE_PALATINE = "FBPAL"
    """Facial bone, palatine"""
    FACIAL_BONE_VOMER = "FBVOM"
    """Facial bone, vomer"""
    FACIAL_BONE_ZYGOMATIC = "FBZYG"
    """Facial bone, zygomatic"""
    FEMORAL = "FEMOR"
    """Femoral"""
    FEMUR = "FEMUR"
    """Femur"""
    FETUS = "FET"
    """Fetus"""
    FIBULA = "FIBU"
    """Fibula"""
    FINGER = "FING"
    """Finger"""
    FINGER_NAIL = "FINGN"
    """Finger Nail"""
    FEMORAL_HEAD = "FMH"
    """Femoral Head"""
    FOLLICLE = "FOL"
    """Follicle"""
    FOOT = "FOOT"
    """Foot"""
    FOREARM = "FOREA"
    """Forearm"""
    FOREHEAD = "FOREH"
    """Forehead"""
    FORESKIN = "FORES"
    """Foreskin"""
    FOURCHETTE = "FOURC"
    """Fourchette"""
    GALL_BLADDER = "GB"
    """Gall Bladder"""
    GENITAL = "GEN"
    """Genital"""
    GENITAL_CERVIX = "GENC"
    """Genital Cervix"""
    GENITAL_LOCHIA = "GENL"
    """Genital Lochia"""
    GENITAL_LESION = "GL"
    """Genital Lesion"""
    GLAND = "GLAND"
    """Gland"""
    GLANS = "GLANS"
    """Glans"""
    GLUTEUS = "GLUT"
    """Gluteus"""
    GLUTEAL = "GLUTE"
    """Gluteal"""
    GLUTEUS_MEDIUS = "GLUTM"
    """Gluteus Medius"""
    GROIN = "GROIN"
    """Groin"""
    GUM = "GUM"
    """Gum"""
    GENITAL_VULVA = "GVU"
    """Genital - Vulva"""
    HALLUX = "HAL"
    """Hallux"""
    HAND = "HAND"
    """Hand"""
    HAIR = "HAR"
    """Hair"""
    HEART = "HART"
    """Heart"""
    HEAD = "HEAD"
    """Head"""
    HEEL = "HEEL"
    """Heel"""
    HEMORRHOID = "HEM"
    """Hemorrhoid"""
    HIP = "HIP"
    """Hip"""
    HIP_JOINT = "HIPJ"
    """Hip Joint"""
    HUMERUS = "HUMER"
    """Humerus"""
    HEART_VALVE = "HV"
    """Heart Valve"""
    HEART_VALVE_BICUSPID = "HVB"
    """Heart Valve, Bicuspid"""
    HEART_VALVE_TRICUSPID = "HVT"
    """Heart Valve, Tricuspid"""
    HYMEN = "HYMEN"
    """Hymen"""
    INTRACERVICAL = "ICX"
    """Intracervical"""
    ILEAL_CONDUIT = "ILC"
    """Ileal Conduit"""
    ILICAL_CONDUIT = "ILCON"
    """Ilical Conduit"""
    ILIAC_CREST = "ILCR"
    """Iliac Crest"""
    ILEAL_LOOP = "ILE"
    """Ileal Loop"""
    ILEOSTOMY = "ILEOS"
    """Ileostomy"""
    ILEUM = "ILEUM"
    """Ileum"""
    ILIAC = "ILIAC"
    """Iliac"""
    INTRANASAL = "INASA"
    """Intranasal"""
    INGUINAL = "INGUI"
    """Inguinal"""
    INTESTINE_LARGE = "INSTL"
    """Intestine, Large"""
    INTESTINE_SMALL = "INSTS"
    """Intestine, Small"""
    INTESTINE = "INT"
    """Intestine"""
    INTROITUS = "INTRO"
    """Introitus"""
    INTRAUTERINE = "INTRU"
    """Intrauterine"""
    ISCHIUM = "ISCHI"
    """Ischium"""
    LOOP_ISHIAL = "ISH"
    """Loop, Ishial"""
    JAW = "JAW"
    """Jaw"""
    JUGULAR_INTERNAL = "JUGI"
    """Jugular, Internal"""
    KIDNEY = "KIDN"
    """Kidney"""
    KNEE = "KNEE"
    """Knee"""
    KNEE_FLUID = "KNEEF"
    """Knee Fluid"""
    KNEE_JOINT = "KNEEJ"
    """Knee Joint"""
    LABIA = "LABIA"
    """Labia"""
    LABIA_MAJORA = "LABMA"
    """Labia Majora"""
    LABIA_MINORA = "LABMI"
    """Labia Minora"""
    LACRIMAL = "LACRI"
    """Lacrimal"""
    LAMELLA = "LAM"
    """Lamella"""
    LARYNX = "LARYN"
    """Larynx"""
    LEG = "LEG"
    """Leg"""
    LENS = "LENS"
    """Lens"""
    LINGUAL = "LING"
    """Lingual"""
    LINGULA = "LINGU"
    """Lingula"""
    LIP = "LIP"
    """Lip"""
    LIVER = "LIVER"
    """Liver"""
    LUMEN = "LMN"
    """Lumen"""
    LYMPH_NODE = "LN"
    """Lymph Node"""
    LYMPH_NODE_GROIN = "LNG"
    """Lymph Node, Groin"""
    LOBE = "LOBE"
    """Lobe"""
    LOCHIA = "LOCH"
    """Lochia"""
    LUMBAR = "LUMBA"
    """Lumbar"""
    LUNG = "LUNG"
    """Lung"""
    LYMPHOCYTES = "LYM"
    """Lymphocytes"""
    MACROPHAGES = "MAC"
    """Macrophages"""
    MALLEOLUS = "MALLE"
    """Malleolus"""
    MANDIBLE_OR_MANDIBULAR = "MANDI"
    """Mandible/Mandibular"""
    MARROW = "MAR"
    """Marrow"""
    MASTOID = "MAST"
    """Mastoid"""
    MAXILLA_OR_MAXILLARY = "MAXIL"
    """Maxilla/Maxillary"""
    MAXILLARY_SINUS = "MAXS"
    """Maxillary Sinus"""
    MEATUS = "MEATU"
    """Meatus"""
    MECONIUM = "MEC"
    """Meconium"""
    MEDIASTINUM = "MEDST"
    """Mediastinum"""
    MEDULLARY = "MEDU"
    """Medullary"""
    METACARPAL = "METAC"
    """Metacarpal"""
    METATARSAL = "METAT"
    """Metatarsal"""
    MILK_BREAST = "MILK"
    """Milk, Breast"""
    MITRAL_VALVE = "MITRL"
    """Mitral Valve"""
    MOLAR = "MOLAR"
    """Molar"""
    MONS_URETERIS = "MONSU"
    """Mons Ureteris"""
    MONS_VENERIS = "MONSV"
    """Mons Veneris(Mons Pubis)"""
    MEMBRANE = "MOU"
    """Membrane"""
    MOUTH = "MOUTH"
    """Mouth"""
    MONS_PUBIS = "MP"
    """Mons Pubis"""
    MENINGES = "MPB"
    """Meninges"""
    MRSA = "MRSA2"
    """Mrsa:"""
    MYOCARDIUM = "MYO"
    """Myocardium"""
    NAIL = "NAIL"
    """Nail"""
    NAIL_BED = "NAILB"
    """Nail Bed"""
    NAIL_FINGER = "NAILF"
    """Nail, Finger"""
    NAIL_TOE = "NAILT"
    """Nail, Toe"""
    NARES = "NARES"
    """Nares"""
    NASAL = "NASL"
    """Nasal"""
    NAVEL = "NAVEL"
    """Navel"""
    NECK = "NECK"
    """Neck"""
    NERVE = "NERVE"
    """Nerve"""
    NIPPLE = "NIPPL"
    """Nipple"""
    NASOLACRIMAL = "NLACR"
    """Nasolacrimal"""
    NOSE = "NOS"
    """Nose (Nasal Passage)"""
    NOSE_ = "NOSE"
    """Nose"""
    NOSE__ = "NOSE"
    """Nose(Outside)"""
    NOSTRIL = "NOSTR"
    """Nostril"""
    NASOPHARYNGEAL = "NP"
    """Nasopharyngeal"""
    NASOPHARYNX = "NP"
    """Nasopharynx"""
    NASAL_SEPTUM = "NSS"
    """Nasal Septum"""
    NASOTRACHEAL = "NTRAC"
    """Nasotracheal"""
    OCCIPITAL = "OCCIP"
    """Occipital"""
    OLECRANON = "OLECR"
    """Olecranon"""
    OMENTUM = "OMEN"
    """Omentum"""
    ORBIT_OR_ORBITAL = "ORBIT"
    """Orbit/Orbital"""
    OROPHARYNX = "ORO"
    """Oropharynx"""
    OS_COXA = "OSCOX"
    """Os coxa (pelvic girdle)"""
    OVARY = "OVARY"
    """Ovary"""
    PANCREATIC_FLUID = "PAFL"
    """Pancreatic Fluid"""
    PALATE = "PALAT"
    """Palate"""
    PALM = "PALM"
    """Palm"""
    PERIANAL_OR_PERIRECTAL = "PANAL"
    """Perianal/Perirectal"""
    PANCREAS = "PANCR"
    """Pancreas"""
    PARATRACHEAL = "PARAT"
    """Paratracheal"""
    PARIETAL = "PARIE"
    """Parietal"""
    PARONYCHIA = "PARON"
    """Paronychia"""
    PAROTID = "PAROT"
    """Parotid"""
    PAROTID_GLAND = "PAROT"
    """Parotid Gland"""
    PARASTERNAL = "PAS"
    """Parasternal"""
    PATELLA = "PATEL"
    """Patella"""
    PERICARDIUM = "PCARD"
    """Pericardium"""
    PERICLITORAL = "PCLIT"
    """Periclitoral"""
    PELVIS = "PELV"
    """Pelvis"""
    PENIS = "PENIS"
    """Penis"""
    PENILE_SHAFT = "PENSH"
    """Penile Shaft"""
    PERITONEAL = "PER"
    """Peritoneal"""
    PERICARDIAL_FLUID = "PERI"
    """Pericardial Fluid"""
    PERIHEPATIC = "PERIH"
    """Perihepatic"""
    PERINEAL_ABSCESS = "PERIN"
    """Perineal Abscess"""
    PERISPLENIC = "PERIS"
    """Perisplenic"""
    PERITONEUM = "PERIT"
    """Peritoneum"""
    PERIURETHAL = "PERIU"
    """Periurethal"""
    PERIVESICULAR = "PERIV"
    """Perivesicular"""
    PERIRECTAL = "PERRA"
    """Perirectal"""
    PERITONEAL_FLUID = "PERT"
    """Peritoneal Fluid"""
    PHALANYX = "PHALA"
    """Phalanyx"""
    PILONIDAL = "PILO"
    """Pilonidal"""
    PINNA = "PINNA"
    """Pinna"""
    PLACENTA = "PLACF"
    """Placenta (Fetal Side)"""
    PLACM = "PLACM"
    """Placenta (Maternal Side)"""
    PLANTAR = "PLANT"
    """Plantar"""
    PALATE_HARD = "PLATH"
    """Palate, Hard"""
    PALATE_SOFT = "PLATS"
    """Palate, Soft"""
    PLC = "PLC"
    """Placenta"""
    PLEURAL_FLUID = "PLEU"
    """Pleural Fluid"""
    PLEURA = "PLEUR"
    """Pleura"""
    PLR = "PLR"
    """Pleural Fluid (Thoracentesis Fld)"""
    PERINEAL = "PNEAL"
    """Perineal"""
    PERINEPHRIC = "PNEPH"
    """Perinephric"""
    PERINEUM = "PNM"
    """Perineum"""
    POPLITEAL = "POPLI"
    """Popliteal"""
    PERIORBITAL = "PORBI"
    """Periorbital"""
    PREAURICULAR = "PREAU"
    """Preauricular"""
    PRERENAL = "PRERE"
    """Prerenal"""
    PROSTATIC_FLUID = "PROS"
    """Prostatic Fluid"""
    PROSTATE_GLAND = "PRST"
    """Prostate Gland"""
    PERITONSILLAR = "PTONS"
    """Peritonsillar"""
    PUBIC = "PUBIC"
    """Pubic"""
    PULMONARY_ARTERY = "PUL"
    """Pulmonary Artery"""
    RADIAL = "RADI"
    """Radial"""
    RADIUS = "RADIUS"
    """Radius"""
    RED_BLOOD_CELLS = "RBC"
    """Red Blood Cells"""
    RECTAL = "RECTL"
    """Rectal"""
    RECTUM = "RECTU"
    """Rectum"""
    RENAL = "RENL"
    """Renal"""
    RIB = "RIB"
    """Rib"""
    RENAL_PELVIS = "RNP"
    """Renal Pelvis"""
    RETROPERITONEAL = "RPERI"
    """Retroperitoneal"""
    UTERINE_CUL_OR_DE_OR_SAC = "SAC"
    """Uterine Cul/De/Sac"""
    SACROILIAC = "SACIL"
    """Sacroiliac"""
    SACRAL = "SACRA"
    """Sacral"""
    SACROCOCCYGEAL = "SACRO"
    """Sacrococcygeal"""
    SACRUM = "SACRU"
    """Sacrum"""
    SALIVARY_GLAND = "SALGL"
    """Salivary Gland"""
    SCALP = "SCALP"
    """Scalp"""
    SCAPULA_OR_SCAPULAR = "SCAPU"
    """Scapula/Scapular"""
    SUPRACLAVICLE_OR_SUPRACLAVICULAR = "SCLAV"
    """Supraclavicle/Supraclavicular"""
    SCLERA = "SCLER"
    """Sclera"""
    SUB_CLAVIAN = "SCLV"
    """Sub Clavian"""
    SCROTUM_OR_SCROTAL = "SCROT"
    """Scrotum/Scrotal"""
    SUBDIAPHRAMATIC = "SDP"
    """Subdiaphramatic"""
    SEMINAL_FLUID = "SEM"
    """Seminal Fluid"""
    SEMEN = "SEMN"
    """Semen"""
    SEPTUM_OR_SEPTAL = "SEPTU"
    """Septum/Septal"""
    SEROMA = "SEROM"
    """Seroma"""
    SUBGALEAL_FLUID = "SGF"
    """Subgaleal Fluid"""
    SHIN = "SHIN"
    """Shin"""
    SHOULDER = "SHOL"
    """Shoulder"""
    SHOLDER_JOINT = "SHOLJ"
    """Sholder Joint"""
    SIGMOID = "SIGMO"
    """Sigmoid"""
    SINUS = "SINUS"
    """Sinus"""
    SKENES_GLAND = "SKENE"
    """Skenes Gland"""
    SKELETAL_MUSCLE = "SKM"
    """Skeletal Muscle"""
    SKULL = "SKULL"
    """Skull"""
    SOLE = "SOLE"
    """Sole"""
    SPINAL_CORD = "SPCOR"
    """Spinal Cord"""
    SPHENOID = "SPHEN"
    """Sphenoid"""
    SPLEEN = "SPLN"
    """Spleen"""
    SPERMATOZOA = "SPRM"
    """Spermatozoa"""
    SUPRA_CERVICAL = "SPX"
    """Supra Cervical"""
    STERNUM_OR_STERNAL = "STER"
    """Sternum/Sternal"""
    STOMA = "STOM"
    """Stoma"""
    STOMACH = "STOMA"
    """Stomach"""
    LIQUID_STOOL = "STOOLL"
    """Liquid Stool"""
    STUMP = "STUMP"
    """Stump"""
    SUBDURAL = "SUB"
    """Subdural"""
    SUBDURAL_FLUID = "SUBD"
    """Subdural Fluid"""
    SUBMANDIBULAR = "SUBM"
    """Submandibular"""
    SUBMENTAL = "SUBME"
    """Submental"""
    SUBPHRENIC = "SUBPH"
    """Subphrenic"""
    SUBMAXILLARY = "SUBX"
    """Submaxillary"""
    SUPRAPUBIC_SPECIMEN = "SUPB"
    """Suprapubic Specimen"""
    SUPRAPUBIC = "SUPRA"
    """Suprapubic"""
    SWEAT = "SWT"
    """Sweat"""
    SWEAT_GLAND = "SWTG"
    """Sweat Gland"""
    SYNOVIAL_FLUID = "SYN"
    """Synovial Fluid"""
    SYNOVIAL = "SYNOL"
    """Synovial"""
    SYNOVIUM = "SYNOV"
    """Synovium"""
    TARSAL = "TARS"
    """Tarsal"""
    TRANSBRONCHIAL = "TBRON"
    """Transbronchial"""
    TRANSCARINA_ASP = "TCN"
    """Transcarina Asp"""
    TEAR_DUCT = "TDUCT"
    """Tear Duct"""
    TEARS = "TEAR"
    """Tears"""
    TEMPLE = "TEMPL"
    """Temple"""
    TEMPORAL = "TEMPO"
    """Temporal"""
    TESTICLE = "TESTI"
    """Testicle(Testis)"""
    THIGH = "THIGH"
    """Thigh"""
    THYMUS = "THM"
    """Thymus"""
    THORACENTESIS = "THORA"
    """Thoracentesis"""
    THORAX_OR_THORACIC = "THORA"
    """Thorax/Thoracic"""
    THROAT = "THRB"
    """Throat"""
    THUMB = "THUMB"
    """Thumb"""
    THYROID = "THYRD"
    """Thyroid"""
    TIBIA = "TIBIA"
    """Tibia"""
    TEMPORAL_LOBE = "TML"
    """Temporal Lobe"""
    THUMBNAIL = "TNL"
    """Thumbnail"""
    TOE = "TOE"
    """Toe"""
    TOE_NAIL = "TOEN"
    """Toe Nail"""
    TONGUE = "TONG"
    """Tongue"""
    TONSIL = "TONS"
    """Tonsil"""
    TOOTH = "TOOTH"
    """Tooth"""
    TRACHEA_OR_TRACHEAL = "TRCHE"
    """Trachea/Tracheal"""
    TOOTH_SOCKET = "TSK"
    """Tooth Socket"""
    ULNA_OR_ULNAR = "ULNA"
    """Ulna/Ulnar"""
    UMBILICAL_BLOOD = "UMB"
    """Umbilical Blood"""
    UMBILICUS = "UMBL"
    """Umbilicus"""
    UMBILICUS_OR_UMBILICAL = "UMBL"
    """Umbilicus/Umbilical"""
    URETER = "URET"
    """Ureter"""
    URETHRA = "URTH"
    """Urethra"""
    STOMA_URINARY = "USTOM"
    """Stoma, Urinary"""
    UTERUS = "UTER"
    """Uterus"""
    UTERINE = "UTERI"
    """Uterine"""
    VAGINA_OR_VAGINAL = "VAGIN"
    """Vagina/Vaginal"""
    VALVE = "VAL"
    """Valve"""
    VAS_DEFERENS = "VAS"
    """Vas Deferens"""
    VASTUS_LATERALIS = "VASTL"
    """Vastus Lateralis"""
    VAULT = "VAULT"
    """Vault"""
    VENTRICULAR_CSF = "VCSF"
    """Ventricular CSF"""
    VAGINAL_CUFF = "VCUFF"
    """Vaginal Cuff"""
    VEIN = "VEIN"
    """Vein"""
    VENTRAGLUTEAL = "VENTG"
    """Ventragluteal"""
    VERMIS_CEREBELLI = "VERMI"
    """Vermis Cerebelli"""
    VERTEBRA_CERVICAL = "VERTC"
    """Vertebra, cervical"""
    VERTEBRA_LUMBAR = "VERTL"
    """Vertebra, lumbar"""
    VERTEBRA_THORACIC = "VERTT"
    """Vertebra, thoracic"""
    VESICULAR = "VESCL"
    """Vesicular"""
    VESICULAR_FLUID = "VESFLD"
    """Vesicular Fluid"""
    VESICLE = "VESI"
    """Vesicle"""
    VESTIBULE = "VESTI"
    """Vestibule(Genital)"""
    VAGINAL_VAULT = "VGV"
    """Vaginal Vault"""
    VITREOUS_FLUID = "VITR"
    """Vitreous Fluid"""
    VOCAL_CORD = "VOC"
    """Vocal Cord"""
    VULVA = "VULVA"
    """Vulva"""
    LEUKOCYTES = "WBC"
    """Leukocytes"""
    WRIST = "WRIST"
    """Wrist"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BodyParts.ACETABULUM: "Acetabulum",
    BodyParts.ACHILLES: "Achilles",
    BodyParts.ABDOMEN: "Abdomen",
    BodyParts.ADENOIDS: "Adenoids",
    BodyParts.ADRENAL: "Adrenal",
    BodyParts.AMNIOTIC_FLUID: "Amniotic fluid",
    BodyParts.AMNIOTIC_SAC: "Amniotic Sac",
    BodyParts.ANAL: "Anal",
    BodyParts.ANKLE: "Ankle",
    BodyParts.ANTECUBITAL: "Antecubital",
    BodyParts.ANTECUBITAL_FOSSA: "Antecubital Fossa",
    BodyParts.ANTRUM: "Antrum",
    BodyParts.ANUS: "Anus",
    BodyParts.AORTA: "Aorta",
    BodyParts.APPENDIX: "Appendix",
    BodyParts.AORTIC_RIM: "Aortic Rim",
    BodyParts.AREOLA: "Areola",
    BodyParts.ARM: "Arm",
    BodyParts.ARTERY: "Artery",
    BodyParts.ASCITES: "Ascites",
    BodyParts.ASCITIC_FLUID: "Ascitic Fluid",
    BodyParts.ATRIUM: "Atrium",
    BodyParts.AURICULAR: "Auricular",
    BodyParts.AORTIC_VALVE: "Aortic Valve",
    BodyParts.AXILLA: "Axilla",
    BodyParts.BACK: "Back",
    BodyParts.BARTHOLIN_DUCT: "Bartholin Duct",
    BodyParts.BARTHOLIN_GLAND: "Bartholin Gland",
    BodyParts.BRAIN_CYST_FLUID: "Brain Cyst Fluid",
    BodyParts.BODY_WHOLE: "Body, Whole",
    BodyParts.BILE_DUCT: "Bile Duct",
    BodyParts.BILE_FLUID: "Bile fluid",
    BodyParts.BLADDER: "Bladder",
    BodyParts.BLOOD_WHOLE: "Blood, Whole",
    BodyParts.BLOOD_ARTERIAL: "Blood, Arterial",
    BodyParts.BLOOD_CAPILLARY: "Blood, Capillary",
    BodyParts.BLOOD_VENOUS: "Blood, Venous",
    BodyParts.BLOOD: "Blood",
    BodyParts.BONE_MARROW: "Bone marrow",
    BodyParts.BONE: "Bone",
    BodyParts.BOWEL: "Bowel",
    BodyParts.BOWEL_LARGE: "Bowel, Large",
    BodyParts.BOWEL_SMALL: "Bowel, Small",
    BodyParts.BASOPHILS: "Basophils",
    BodyParts.BRACHIAL: "Brachial",
    BodyParts.BRAIN: "Brain",
    BodyParts.BRONCHIAL: "Bronchial",
    BodyParts.BRONCHIOLE_OR_BRONCHIOLAR: "Bronchiole/Bronchiolar",
    BodyParts.BRONCHUS_OR_BRONCHIAL: "Bronchus/Bronchial",
    BodyParts.EYEBROW: "Eyebrow",
    BodyParts.BREAST: "Breast",
    BodyParts.BREAST_FLUID: "Breast fluid",
    BodyParts.BARTHOLIN_GLAND_FLUID: "Bartholin Gland Fluid",
    BodyParts.BROVIAC: "Broviac",
    BodyParts.BUCCAL: "Buccal",
    BodyParts.BURSA: "Bursa",
    BodyParts.BURSA_FLUID: "Bursa Fluid",
    BodyParts.BUTTOCKS: "Buttocks",
    BodyParts.CALF: "Calf",
    BodyParts.CANAL: "Canal",
    BodyParts.CANALICULIS: "Canaliculis",
    BodyParts.CANTHUS: "Canthus",
    BodyParts.CAROTID: "Carotid",
    BodyParts.CARPAL: "Carpal",
    BodyParts.CAVITY: "Cavity",
    BodyParts.BLOOD_CORD: "Blood, Cord",
    BodyParts.CARDIAC_MUSCLE: "Cardiac Muscle",
    BodyParts.COMMON_DUCT: "Common Duct",
    BodyParts.CECUM_OR_CECAL: "Cecum/Cecal",
    BodyParts.CERVIX_OR_UTERUS: "Cervix/Uterus",
    BodyParts.CAVITY_CHEST: "Cavity, Chest",
    BodyParts.CHEEK: "Cheek",
    BodyParts.CHEST: "Chest",
    BodyParts.CHEST_TUBE: "Chest Tube",
    BodyParts.CHIN: "Chin",
    BodyParts.CIRCUMCISION_SITE: "Circumcision Site",
    BodyParts.CLAVICLE_OR_CLAVICULAR: "Clavicle/Clavicular",
    BodyParts.CLITORIS: "Clitoris",
    BodyParts.CLITORAL: "Clitoral",
    BodyParts.CANNULA: "Cannula",
    BodyParts.COCCYGEAL: "Coccygeal",
    BodyParts.COCCYX: "Coccyx",
    BodyParts.COLON: "Colon",
    BodyParts.COLOSTOMY: "Colostomy",
    BodyParts.CONJUNCTIVA: "Conjunctiva",
    BodyParts.CORD: "Cord",
    BodyParts.CORAL: "Coral",
    BodyParts.CORD_BLOOD: "Cord Blood",
    BodyParts.CORNEA: "Cornea",
    BodyParts.COLOSTOMY_STOMA: "Colostomy Stoma",
    BodyParts.CRANIUM_ETHMOID: "Cranium, ethmoid",
    BodyParts.CRANIUM_FRONTAL: "Cranium, frontal",
    BodyParts.CRANIUM_OCCIPITAL: "Cranium, occipital",
    BodyParts.CRANIUM_PARIETAL: "Cranium, parietal",
    BodyParts.CRANIUM_SPHENOID: "Cranium, sphenoid",
    BodyParts.CRANIUM_TEMPORAL: "Cranium, temporal",
    BodyParts.CEREBRAL_SPINAL_FLUID: "Cerebral Spinal Fluid",
    BodyParts.CUBITUS: "Cubitus",
    BodyParts.CUFF: "Cuff",
    BodyParts.CUL_DE_SAC: "Cul De Sac",
    BodyParts.CULDOCENTESIS: "Culdocentesis",
    BodyParts.CERVIX: "Cervix",
    BodyParts.DELTOID: "Deltoid",
    BodyParts.DENTAL_GINGIVA: "Dental Gingiva",
    BodyParts.DENTAL: "Dental",
    BodyParts.DIALYSIS_FLUID: "Dialysis Fluid",
    BodyParts.DIGIT: "Digit",
    BodyParts.DISC: "Disc",
    BodyParts.DORSUM_OR_DORSAL: "Dorsum/Dorsal",
    BodyParts.DIAPHRAGM: "Diaphragm",
    BodyParts.DUODENAL_FLUID: "Duodenal Fluid",
    BodyParts.DUODENUM_OR_DUODENAL: "Duodenum/Duodenal",
    BodyParts.DURA: "Dura",
    BodyParts.EAR: "Ear",
    BodyParts.EAR_BONE_INCUS: "Ear bone, incus",
    BodyParts.EAR_BONE_MALLEUS: "Ear bone, malleus",
    BodyParts.EAR_BONE_STAPES: "Ear bone,stapes",
    BodyParts.EAR_LOBE: "Ear Lobe",
    BodyParts.ENDOCERVICAL: "Endocervical",
    BodyParts.ELBOW: "Elbow",
    BodyParts.ELBOW_JOINT: "Elbow Joint",
    BodyParts.ENDOCARDIUM: "Endocardium",
    BodyParts.ENDOMETRIUM: "Endometrium",
    BodyParts.ENDOLPTHAMITIS: "endolpthamitis",
    BodyParts.EOSINOPHILS: "Eosinophils",
    BodyParts.EPIDIDYMIS: "Epididymis",
    BodyParts.EPICARDIAL: "Epicardial",
    BodyParts.EPICARDIUM: "Epicardium",
    BodyParts.EPIDURAL: "Epidural",
    BodyParts.EPIGLOTTIS: "Epiglottis",
    BodyParts.ESOPHAGUS: "Esophagus",
    BodyParts.ESOPHAGEAL: "Esophageal",
    BodyParts.ENDOTRACHEAL: "Endotracheal",
    BodyParts.ETHMOID: "Ethmoid",
    BodyParts.ENDOURETHRAL: "Endourethral",
    BodyParts.EYE: "Eye",
    BodyParts.EYELID: "Eyelid",
    BodyParts.FACE: "Face",
    BodyParts.FALLOPIAN_TUBE: "Fallopian Tube",
    BodyParts.FACIAL_BONE_INFERIOR_NASAL_CONCHA: "Facial bone, inferior nasal concha",
    BodyParts.FACIAL_BONE_LACRIMAL: "Facial bone, lacrimal",
    BodyParts.FACIAL_BONE_MAXILLA: "Facial bone, maxilla",
    BodyParts.FACIAL_BONE_NASAL: "Facial bone, nasal",
    BodyParts.FACIAL_BONE_PALATINE: "Facial bone, palatine",
    BodyParts.FACIAL_BONE_VOMER: "Facial bone, vomer",
    BodyParts.FACIAL_BONE_ZYGOMATIC: "Facial bone, zygomatic",
    BodyParts.FEMORAL: "Femoral",
    BodyParts.FEMUR: "Femur",
    BodyParts.FETUS: "Fetus",
    BodyParts.FIBULA: "Fibula",
    BodyParts.FINGER: "Finger",
    BodyParts.FINGER_NAIL: "Finger Nail",
    BodyParts.FEMORAL_HEAD: "Femoral Head",
    BodyParts.FOLLICLE: "Follicle",
    BodyParts.FOOT: "Foot",
    BodyParts.FOREARM: "Forearm",
    BodyParts.FOREHEAD: "Forehead",
    BodyParts.FORESKIN: "Foreskin",
    BodyParts.FOURCHETTE: "Fourchette",
    BodyParts.GALL_BLADDER: "Gall Bladder",
    BodyParts.GENITAL: "Genital",
    BodyParts.GENITAL_CERVIX: "Genital Cervix",
    BodyParts.GENITAL_LOCHIA: "Genital Lochia",
    BodyParts.GENITAL_LESION: "Genital Lesion",
    BodyParts.GLAND: "Gland",
    BodyParts.GLANS: "Glans",
    BodyParts.GLUTEUS: "Gluteus",
    BodyParts.GLUTEAL: "Gluteal",
    BodyParts.GLUTEUS_MEDIUS: "Gluteus Medius",
    BodyParts.GROIN: "Groin",
    BodyParts.GUM: "Gum",
    BodyParts.GENITAL_VULVA: "Genital - Vulva",
    BodyParts.HALLUX: "Hallux",
    BodyParts.HAND: "Hand",
    BodyParts.HAIR: "Hair",
    BodyParts.HEART: "Heart",
    BodyParts.HEAD: "Head",
    BodyParts.HEEL: "Heel",
    BodyParts.HEMORRHOID: "Hemorrhoid",
    BodyParts.HIP: "Hip",
    BodyParts.HIP_JOINT: "Hip Joint",
    BodyParts.HUMERUS: "Humerus",
    BodyParts.HEART_VALVE: "Heart Valve",
    BodyParts.HEART_VALVE_BICUSPID: "Heart Valve, Bicuspid",
    BodyParts.HEART_VALVE_TRICUSPID: "Heart Valve, Tricuspid",
    BodyParts.HYMEN: "Hymen",
    BodyParts.INTRACERVICAL: "Intracervical",
    BodyParts.ILEAL_CONDUIT: "Ileal Conduit",
    BodyParts.ILICAL_CONDUIT: "Ilical Conduit",
    BodyParts.ILIAC_CREST: "Iliac Crest",
    BodyParts.ILEAL_LOOP: "Ileal Loop",
    BodyParts.ILEOSTOMY: "Ileostomy",
    BodyParts.ILEUM: "Ileum",
    BodyParts.ILIAC: "Iliac",
    BodyParts.INTRANASAL: "Intranasal",
    BodyParts.INGUINAL: "Inguinal",
    BodyParts.INTESTINE_LARGE: "Intestine, Large",
    BodyParts.INTESTINE_SMALL: "Intestine, Small",
    BodyParts.INTESTINE: "Intestine",
    BodyParts.INTROITUS: "Introitus",
    BodyParts.INTRAUTERINE: "Intrauterine",
    BodyParts.ISCHIUM: "Ischium",
    BodyParts.LOOP_ISHIAL: "Loop, Ishial",
    BodyParts.JAW: "Jaw",
    BodyParts.JUGULAR_INTERNAL: "Jugular, Internal",
    BodyParts.KIDNEY: "Kidney",
    BodyParts.KNEE: "Knee",
    BodyParts.KNEE_FLUID: "Knee Fluid",
    BodyParts.KNEE_JOINT: "Knee Joint",
    BodyParts.LABIA: "Labia",
    BodyParts.LABIA_MAJORA: "Labia Majora",
    BodyParts.LABIA_MINORA: "Labia Minora",
    BodyParts.LACRIMAL: "Lacrimal",
    BodyParts.LAMELLA: "Lamella",
    BodyParts.LARYNX: "Larynx",
    BodyParts.LEG: "Leg",
    BodyParts.LENS: "Lens",
    BodyParts.LINGUAL: "Lingual",
    BodyParts.LINGULA: "Lingula",
    BodyParts.LIP: "Lip",
    BodyParts.LIVER: "Liver",
    BodyParts.LUMEN: "Lumen",
    BodyParts.LYMPH_NODE: "Lymph Node",
    BodyParts.LYMPH_NODE_GROIN: "Lymph Node, Groin",
    BodyParts.LOBE: "Lobe",
    BodyParts.LOCHIA: "Lochia",
    BodyParts.LUMBAR: "Lumbar",
    BodyParts.LUNG: "Lung",
    BodyParts.LYMPHOCYTES: "Lymphocytes",
    BodyParts.MACROPHAGES: "Macrophages",
    BodyParts.MALLEOLUS: "Malleolus",
    BodyParts.MANDIBLE_OR_MANDIBULAR: "Mandible/Mandibular",
    BodyParts.MARROW: "Marrow",
    BodyParts.MASTOID: "Mastoid",
    BodyParts.MAXILLA_OR_MAXILLARY: "Maxilla/Maxillary",
    BodyParts.MAXILLARY_SINUS: "Maxillary Sinus",
    BodyParts.MEATUS: "Meatus",
    BodyParts.MECONIUM: "Meconium",
    BodyParts.MEDIASTINUM: "Mediastinum",
    BodyParts.MEDULLARY: "Medullary",
    BodyParts.METACARPAL: "Metacarpal",
    BodyParts.METATARSAL: "Metatarsal",
    BodyParts.MILK_BREAST: "Milk, Breast",
    BodyParts.MITRAL_VALVE: "Mitral Valve",
    BodyParts.MOLAR: "Molar",
    BodyParts.MONS_URETERIS: "Mons Ureteris",
    BodyParts.MONS_VENERIS: "Mons Veneris(Mons Pubis)",
    BodyParts.MEMBRANE: "Membrane",
    BodyParts.MOUTH: "Mouth",
    BodyParts.MONS_PUBIS: "Mons Pubis",
    BodyParts.MENINGES: "Meninges",
    BodyParts.MRSA: "Mrsa:",
    BodyParts.MYOCARDIUM: "Myocardium",
    BodyParts.NAIL: "Nail",
    BodyParts.NAIL_BED: "Nail Bed",
    BodyParts.NAIL_FINGER: "Nail, Finger",
    BodyParts.NAIL_TOE: "Nail, Toe",
    BodyParts.NARES: "Nares",
    BodyParts.NASAL: "Nasal",
    BodyParts.NAVEL: "Navel",
    BodyParts.NECK: "Neck",
    BodyParts.NERVE: "Nerve",
    BodyParts.NIPPLE: "Nipple",
    BodyParts.NASOLACRIMAL: "Nasolacrimal",
    BodyParts.NOSE: "Nose (Nasal Passage)",
    BodyParts.NOSE_: "Nose",
    BodyParts.NOSE__: "Nose(Outside)",
    BodyParts.NOSTRIL: "Nostril",
    BodyParts.NASOPHARYNGEAL: "Nasopharyngeal",
    BodyParts.NASOPHARYNX: "Nasopharynx",
    BodyParts.NASAL_SEPTUM: "Nasal Septum",
    BodyParts.NASOTRACHEAL: "Nasotracheal",
    BodyParts.OCCIPITAL: "Occipital",
    BodyParts.OLECRANON: "Olecranon",
    BodyParts.OMENTUM: "Omentum",
    BodyParts.ORBIT_OR_ORBITAL: "Orbit/Orbital",
    BodyParts.OROPHARYNX: "Oropharynx",
    BodyParts.OS_COXA: "Os coxa (pelvic girdle)",
    BodyParts.OVARY: "Ovary",
    BodyParts.PANCREATIC_FLUID: "Pancreatic Fluid",
    BodyParts.PALATE: "Palate",
    BodyParts.PALM: "Palm",
    BodyParts.PERIANAL_OR_PERIRECTAL: "Perianal/Perirectal",
    BodyParts.PANCREAS: "Pancreas",
    BodyParts.PARATRACHEAL: "Paratracheal",
    BodyParts.PARIETAL: "Parietal",
    BodyParts.PARONYCHIA: "Paronychia",
    BodyParts.PAROTID: "Parotid",
    BodyParts.PAROTID_GLAND: "Parotid Gland",
    BodyParts.PARASTERNAL: "Parasternal",
    BodyParts.PATELLA: "Patella",
    BodyParts.PERICARDIUM: "Pericardium",
    BodyParts.PERICLITORAL: "Periclitoral",
    BodyParts.PELVIS: "Pelvis",
    BodyParts.PENIS: "Penis",
    BodyParts.PENILE_SHAFT: "Penile Shaft",
    BodyParts.PERITONEAL: "Peritoneal",
    BodyParts.PERICARDIAL_FLUID: "Pericardial Fluid",
    BodyParts.PERIHEPATIC: "Perihepatic",
    BodyParts.PERINEAL_ABSCESS: "Perineal Abscess",
    BodyParts.PERISPLENIC: "Perisplenic",
    BodyParts.PERITONEUM: "Peritoneum",
    BodyParts.PERIURETHAL: "Periurethal",
    BodyParts.PERIVESICULAR: "Perivesicular",
    BodyParts.PERIRECTAL: "Perirectal",
    BodyParts.PERITONEAL_FLUID: "Peritoneal Fluid",
    BodyParts.PHALANYX: "Phalanyx",
    BodyParts.PILONIDAL: "Pilonidal",
    BodyParts.PINNA: "Pinna",
    BodyParts.PLACENTA: "Placenta (Fetal Side)",
    BodyParts.PLACM: "Placenta (Maternal Side)",
    BodyParts.PLANTAR: "Plantar",
    BodyParts.PALATE_HARD: "Palate, Hard",
    BodyParts.PALATE_SOFT: "Palate, Soft",
    BodyParts.PLC: "Placenta",
    BodyParts.PLEURAL_FLUID: "Pleural Fluid",
    BodyParts.PLEURA: "Pleura",
    BodyParts.PLR: "Pleural Fluid (Thoracentesis Fld)",
    BodyParts.PERINEAL: "Perineal",
    BodyParts.PERINEPHRIC: "Perinephric",
    BodyParts.PERINEUM: "Perineum",
    BodyParts.POPLITEAL: "Popliteal",
    BodyParts.PERIORBITAL: "Periorbital",
    BodyParts.PREAURICULAR: "Preauricular",
    BodyParts.PRERENAL: "Prerenal",
    BodyParts.PROSTATIC_FLUID: "Prostatic Fluid",
    BodyParts.PROSTATE_GLAND: "Prostate Gland",
    BodyParts.PERITONSILLAR: "Peritonsillar",
    BodyParts.PUBIC: "Pubic",
    BodyParts.PULMONARY_ARTERY: "Pulmonary Artery",
    BodyParts.RADIAL: "Radial",
    BodyParts.RADIUS: "Radius",
    BodyParts.RED_BLOOD_CELLS: "Red Blood Cells",
    BodyParts.RECTAL: "Rectal",
    BodyParts.RECTUM: "Rectum",
    BodyParts.RENAL: "Renal",
    BodyParts.RIB: "Rib",
    BodyParts.RENAL_PELVIS: "Renal Pelvis",
    BodyParts.RETROPERITONEAL: "Retroperitoneal",
    BodyParts.UTERINE_CUL_OR_DE_OR_SAC: "Uterine Cul/De/Sac",
    BodyParts.SACROILIAC: "Sacroiliac",
    BodyParts.SACRAL: "Sacral",
    BodyParts.SACROCOCCYGEAL: "Sacrococcygeal",
    BodyParts.SACRUM: "Sacrum",
    BodyParts.SALIVARY_GLAND: "Salivary Gland",
    BodyParts.SCALP: "Scalp",
    BodyParts.SCAPULA_OR_SCAPULAR: "Scapula/Scapular",
    BodyParts.SUPRACLAVICLE_OR_SUPRACLAVICULAR: "Supraclavicle/Supraclavicular",
    BodyParts.SCLERA: "Sclera",
    BodyParts.SUB_CLAVIAN: "Sub Clavian",
    BodyParts.SCROTUM_OR_SCROTAL: "Scrotum/Scrotal",
    BodyParts.SUBDIAPHRAMATIC: "Subdiaphramatic",
    BodyParts.SEMINAL_FLUID: "Seminal Fluid",
    BodyParts.SEMEN: "Semen",
    BodyParts.SEPTUM_OR_SEPTAL: "Septum/Septal",
    BodyParts.SEROMA: "Seroma",
    BodyParts.SUBGALEAL_FLUID: "Subgaleal Fluid",
    BodyParts.SHIN: "Shin",
    BodyParts.SHOULDER: "Shoulder",
    BodyParts.SHOLDER_JOINT: "Sholder Joint",
    BodyParts.SIGMOID: "Sigmoid",
    BodyParts.SINUS: "Sinus",
    BodyParts.SKENES_GLAND: "Skenes Gland",
    BodyParts.SKELETAL_MUSCLE: "Skeletal Muscle",
    BodyParts.SKULL: "Skull",
    BodyParts.SOLE: "Sole",
    BodyParts.SPINAL_CORD: "Spinal Cord",
    BodyParts.SPHENOID: "Sphenoid",
    BodyParts.SPLEEN: "Spleen",
    BodyParts.SPERMATOZOA: "Spermatozoa",
    BodyParts.SUPRA_CERVICAL: "Supra Cervical",
    BodyParts.STERNUM_OR_STERNAL: "Sternum/Sternal",
    BodyParts.STOMA: "Stoma",
    BodyParts.STOMACH: "Stomach",
    BodyParts.LIQUID_STOOL: "Liquid Stool",
    BodyParts.STUMP: "Stump",
    BodyParts.SUBDURAL: "Subdural",
    BodyParts.SUBDURAL_FLUID: "Subdural Fluid",
    BodyParts.SUBMANDIBULAR: "Submandibular",
    BodyParts.SUBMENTAL: "Submental",
    BodyParts.SUBPHRENIC: "Subphrenic",
    BodyParts.SUBMAXILLARY: "Submaxillary",
    BodyParts.SUPRAPUBIC_SPECIMEN: "Suprapubic Specimen",
    BodyParts.SUPRAPUBIC: "Suprapubic",
    BodyParts.SWEAT: "Sweat",
    BodyParts.SWEAT_GLAND: "Sweat Gland",
    BodyParts.SYNOVIAL_FLUID: "Synovial Fluid",
    BodyParts.SYNOVIAL: "Synovial",
    BodyParts.SYNOVIUM: "Synovium",
    BodyParts.TARSAL: "Tarsal",
    BodyParts.TRANSBRONCHIAL: "Transbronchial",
    BodyParts.TRANSCARINA_ASP: "Transcarina Asp",
    BodyParts.TEAR_DUCT: "Tear Duct",
    BodyParts.TEARS: "Tears",
    BodyParts.TEMPLE: "Temple",
    BodyParts.TEMPORAL: "Temporal",
    BodyParts.TESTICLE: "Testicle(Testis)",
    BodyParts.THIGH: "Thigh",
    BodyParts.THYMUS: "Thymus",
    BodyParts.THORACENTESIS: "Thoracentesis",
    BodyParts.THORAX_OR_THORACIC: "Thorax/Thoracic",
    BodyParts.THROAT: "Throat",
    BodyParts.THUMB: "Thumb",
    BodyParts.THYROID: "Thyroid",
    BodyParts.TIBIA: "Tibia",
    BodyParts.TEMPORAL_LOBE: "Temporal Lobe",
    BodyParts.THUMBNAIL: "Thumbnail",
    BodyParts.TOE: "Toe",
    BodyParts.TOE_NAIL: "Toe Nail",
    BodyParts.TONGUE: "Tongue",
    BodyParts.TONSIL: "Tonsil",
    BodyParts.TOOTH: "Tooth",
    BodyParts.TRACHEA_OR_TRACHEAL: "Trachea/Tracheal",
    BodyParts.TOOTH_SOCKET: "Tooth Socket",
    BodyParts.ULNA_OR_ULNAR: "Ulna/Ulnar",
    BodyParts.UMBILICAL_BLOOD: "Umbilical Blood",
    BodyParts.UMBILICUS: "Umbilicus",
    BodyParts.UMBILICUS_OR_UMBILICAL: "Umbilicus/Umbilical",
    BodyParts.URETER: "Ureter",
    BodyParts.URETHRA: "Urethra",
    BodyParts.STOMA_URINARY: "Stoma, Urinary",
    BodyParts.UTERUS: "Uterus",
    BodyParts.UTERINE: "Uterine",
    BodyParts.VAGINA_OR_VAGINAL: "Vagina/Vaginal",
    BodyParts.VALVE: "Valve",
    BodyParts.VAS_DEFERENS: "Vas Deferens",
    BodyParts.VASTUS_LATERALIS: "Vastus Lateralis",
    BodyParts.VAULT: "Vault",
    BodyParts.VENTRICULAR_CSF: "Ventricular CSF",
    BodyParts.VAGINAL_CUFF: "Vaginal Cuff",
    BodyParts.VEIN: "Vein",
    BodyParts.VENTRAGLUTEAL: "Ventragluteal",
    BodyParts.VERMIS_CEREBELLI: "Vermis Cerebelli",
    BodyParts.VERTEBRA_CERVICAL: "Vertebra, cervical",
    BodyParts.VERTEBRA_LUMBAR: "Vertebra, lumbar",
    BodyParts.VERTEBRA_THORACIC: "Vertebra, thoracic",
    BodyParts.VESICULAR: "Vesicular",
    BodyParts.VESICULAR_FLUID: "Vesicular Fluid",
    BodyParts.VESICLE: "Vesicle",
    BodyParts.VESTIBULE: "Vestibule(Genital)",
    BodyParts.VAGINAL_VAULT: "Vaginal Vault",
    BodyParts.VITREOUS_FLUID: "Vitreous Fluid",
    BodyParts.VOCAL_CORD: "Vocal Cord",
    BodyParts.VULVA: "Vulva",
    BodyParts.LEUKOCYTES: "Leukocytes",
    BodyParts.WRIST: "Wrist",
}
