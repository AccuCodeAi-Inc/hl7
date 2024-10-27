from ...base import HL7Table

"""
HL7 Version: 2.5.1
Consent Type - 0496
Table Type: User
"""


class ConsentType(HL7Table):
    """
    Consent Type - 0496 // User table type
    - RELEASE_OF_INFORMATION_OR_MR_OR_AUTHORIZATION_TO_DISCLOSURE_PROTECTED_HEALTH_INFORMATION
    - MEDICAL_PROCEDURE
    - ACKNOWLEDGE_RECEIPT_OF_PRIVACY_NOTICE
    - ABORTION
    - ABORTION_OR_LAMINARIA
    - ACCUTANE_INFORMATION
    - ACCUTANE_WOMAN
    - ADVANCED_BENEFICIARY_NOTICE
    - AFP
    - AMNIOCENTESIS
    - ANATOMICAL_GIFT
    - ANESTHESIA_COMPLICATIONS
    - ANESTHESIA_QUESTIONNAIRE
    - ANGIOGRAM
    - ANGIOPLASTY
    - ANTICANCER_DRUGS
    - ANTIPSYCHOTIC_MEDICATIONS
    - ARTHROGRAM
    - AUTOPSY
    - AZT_THERAPY
    - BILIARY_DRAINAGE
    - BILIARY_STONE_EXTRACTION
    - BIOPSY
    - BLEEDING_TIME_TEST
    - BRONCHOGRAM
    - CARDIAC_CATHETERIZATION
    - CORONARY_ANGIOGRAPHY
    - W_OR_O_SURGERY_CAPABILITY
    - CATARACT_OP_OR_IMPLANT_OF_FDA_APRVD_LENS
    - CATARACT_OP_OR_IMPLANT_OF_INVESTIGATIONAL_LENS
    - CATARACT_SURGERY
    - CHOLERA_IMMUNIZATION
    - CHOLESTEROL_SCREENING
    - CIRCUMCISION_NEWBORN
    - COLONOSCOPY
    - CONTACT_LENSES
    - CT_SCAN_CERVICAL_AND_LUMBAR
    - CT_SCAN_W_OR_IV_CONTRAST_MEDIA_INTO_VEIN
    - CVS
    - CYSTOSPY
    - DISCLOSURE_OF_PROTECTED_HEALTH_INFORMATION_TO_FAMILY_OR_FRIENDS
    - D_AND_C_AND_CONIZATION
    - DACRYOCYSTOGRAM
    - DIAGNOSTIC_ISOTOPE
    - DRAINAGE_OF_AN_ABSCESS
    - DRUG_SCREENING
    - ELECTRONIC_MONITORING_OF_LABOR_REFUSAL
    - ENDOMETRIAL_BIOPSY
    - ENDOSCOPY_OR_SCLEROSIS_OF_ESOPHAGEAL_VARICES
    - ERCP
    - EXPOSURE_TO_REPORTABLE_COMMUNICABLE_DISEASE
    - EXTERNAL_VERSION
    - FLUORESCEIN_ANGIOSCOPY
    - HEPATITIS_B_CONSENT_OR_DECLINATION
    - HERNIOGRAM
    - HIV_TEST_CONSENT_REFUSAL
    - HIV_TEST_DISCLOSURE
    - HIV_TEST_PRENATAL
    - HOME_IV_TREATMENT_PROGRAM
    - HOME_PARENTERAL_TREATMENT_PROGRAM
    - HYSTERECTOMY
    - HYSTEROSALPINGOGRAM
    - INJECTION_SLIP_OR_CONSENT
    - INTRAUTERINE_DEVICE
    - INTRAUTERINE_DEVICE_OR_STERILIZATION
    - INTRAVASCULAR_INFUSION_OF_STREPTOKINASE_OR_UROKINASE
    - INTRAVENOUS_CHOLANGIOGRAM
    - INTRAVENOUS_DIGITAL_ANGIOGRAPHY
    - IODINE_ADMINISTRATION
    - ISG
    - IVP
    - LASER_PHOTOCOAGULATION
    - LASER_TREATMENT
    - LITHIUM_CARBONATE
    - LIVER_BIOPSY
    - LUMBAR_PUNCTURE
    - LYMPHANGIOGRAM
    - MAO_INHIBITORS
    - MED_PSYCH_AND_OR_OR_DRUG_OR_ALCOHOL
    - MEDICAL_TREATMENT_REFUSAL
    - MORNING_AFTER_PILL
    - MRI_ADULT
    - MRI_PEDIATRIC
    - MYELOGRAM
    - NEEDLE_BIOPSY
    - NEEDLE_BIOPSY_OF_LUNG
    - NEWBORN_TREATMENT_AND_RELEASE
    - NORPLANT_SUBDERMAL_BIRTH_CONTROL_IMPLANT
    - OPERATIONS_ANESTHESIA_TRANSFUSIONS
    - ORAL_CONTRACEPTIVES
    - ORGAN_DONATION
    - PATIENT_PERMITS_CONSENTS
    - PATIENT_TREATMENT_PERMIT_RELEASE_AND_ADMISSION
    - PENILE_INJECTIONS
    - PERCUTANEOUS_NEPHROSTOMY
    - PERCUTANEOUS_TRANSHEPATIC_CHOLANGIOGRAM
    - PHOTOGRAPHS
    - PHOTOGRAPHS_EMPLOYEE
    - PHOTOGRAPHS_MEDICAL_RESEARCH
    - PHOTOGRAPHS_NEWS_MEDIA
    - PSYCHIATRIC_ADMISSION_NEXT_OF_KIN
    - PSYCHIATRIC_INFORMATION_DURING_HOSPITAL_STAY
    - PUBLIC_RELEASE_OF_INFORMATION
    - RADIOLOGIC_PROCEDURE
    - REFUSAL_OF_TREATMENT
    - RELEASE_OF_BODY
    - RELEASE_OF_LIMB
    - RH_IMMUNE_GLOBULIN
    - RIGHTS_OF_MEDICAL_RESEARCH_PARTICIPANTS
    - REQUEST_TO_RESTRICT_ACCESS_OR_DISCLOSURE_TO_MEDICAL_RECORD_OR_PROTECTED_HEALTH_INFORMATION
    - REQUEST_FOR_REMAIN_ANONYMOUS
    - SEAT_BELT_EXEMPTION
    - SIALOGRAM
    - VOIDING_CYSTOGRAM
    - SIGMOIDOSCOPY
    - STERILIZATION_ANESTHESIA_AND_MEDICAL_SERVICES
    - STERILIZATION_FEDERALLY_FUNDED
    - STERILIZATION_FEMALE
    - STERILIZATION_LAPAROSCOPY_OR_POMEROY
    - STERILIZATION_NON_FEDERALLY_FUNDED
    - STERILIZATION_SECONDARY
    - TRANQUILIZERS
    - TRANSFER_ACKNOWLEDGEMENT
    - TRANSFER_AUTHORIZATION
    - TRANSFER_CERTIFICATION_PHYSICIAN
    - TRANSFER_OR_DISCHARGE_REQUEST
    - TRANSFER_FOR_NON_MEDICAL_REASONS
    - TRANSFER_INTERFACULTY_NEONATAL
    - TRANSFER_REFUSAL
    - TRANSFER_REFUSAL_OF_FURTHER_TREATMENT
    - TREADMILL_AND_EKG
    - TREADMILL_THALLIUM_201
    - TYPHOID
    - USE_OF_INVESTIGATIONAL_DEVICE
    - USE_OF_INVESTIGATIONAL_DRUG
    - VENOGRAM
    - VIDEOTAPE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0496
    """

    RELEASE_OF_INFORMATION_OR_MR_OR_AUTHORIZATION_TO_DISCLOSURE_PROTECTED_HEALTH_INFORMATION = "001"  # Release of Info/ Disclosure
    """Release of Information/MR / Authorization to Disclosure Protected Health Information"""
    MEDICAL_PROCEDURE = "002"  # Medical Treatment/ Procedure
    """Medical Procedure (invasive)"""
    ACKNOWLEDGE_RECEIPT_OF_PRIVACY_NOTICE = "003"  # Acknowledgement/ Notification
    """Acknowledge Receipt of Privacy Notice"""
    ABORTION = "004"  # Medical Treatment/ Procedure
    """Abortion"""
    ABORTION_OR_LAMINARIA = "005"  # Medical Treatment/ Procedure
    """Abortion/Laminaria"""
    ACCUTANE_INFORMATION = "006"  # Medical Treatment/ Procedure
    """Accutane - Information"""
    ACCUTANE_WOMAN = "007"  # Medical Treatment/ Procedure
    """Accutane - Woman"""
    ADVANCED_BENEFICIARY_NOTICE = "008"  # Acknowledgement/ Notification
    """Advanced Beneficiary Notice"""
    AFP = "009"  # Medical Treatment/ Procedure
    """AFP (Alpha Fetoprotein) Screening"""
    AMNIOCENTESIS = "010"  # Medical Treatment/ Procedure
    """Amniocentesis (consent &amp; refusal)"""
    ANATOMICAL_GIFT = "011"  # Administrative
    """Anatomical Gift (organ donation)"""
    ANESTHESIA_COMPLICATIONS = "012"  # Medical Treatment/ Procedure
    """Anesthesia - Complications"""
    ANESTHESIA_QUESTIONNAIRE = "013"  # Medical Treatment/ Procedure
    """Anesthesia - Questionnaire"""
    ANGIOGRAM = "014"  # Medical Treatment/ Procedure
    """Angiogram"""
    ANGIOPLASTY = "015"  # Medical Treatment/ Procedure
    """Angioplasty"""
    ANTICANCER_DRUGS = "016"  # Medical Treatment/ Procedure
    """Anticancer Drugs"""
    ANTIPSYCHOTIC_MEDICATIONS = "017"  # Medical Treatment/ Procedure
    """Antipsychotic Medications"""
    ARTHROGRAM = "018"  # Medical Treatment/ Procedure
    """Arthrogram"""
    AUTOPSY = "019"  # Administrative
    """Autopsy"""
    AZT_THERAPY = "020"  # Medical Treatment/ Procedure
    """AZT Therapy"""
    BILIARY_DRAINAGE = "021"  # Medical Treatment/ Procedure
    """Biliary Drainage"""
    BILIARY_STONE_EXTRACTION = "022"  # Medical Treatment/ Procedure
    """Biliary Stone Extraction"""
    BIOPSY = "023"  # Medical Treatment/ Procedure
    """Biopsy"""
    BLEEDING_TIME_TEST = "024"  # Medical Treatment/ Procedure
    """Bleeding Time Test"""
    BRONCHOGRAM = "025"  # Medical Treatment/ Procedure
    """Bronchogram"""
    CARDIAC_CATHETERIZATION = "026"  # Medical Treatment/ Procedure
    """Cardiac Catheterization"""
    CORONARY_ANGIOGRAPHY = "027"  # Medical Treatment/ Procedure
    """Coronary Angiography"""
    W_OR_O_SURGERY_CAPABILITY = "028"  # Medical Treatment/ Procedure
    """w/o Surgery Capability"""
    CATARACT_OP_OR_IMPLANT_OF_FDA_APRVD_LENS = "029"  # Medical Treatment/ Procedure
    """Cataract Op/Implant of FDA Aprvd Lens"""
    CATARACT_OP_OR_IMPLANT_OF_INVESTIGATIONAL_LENS = (
        "030"  # Medical Treatment/ Procedure
    )
    """Cataract Op/Implant of Investigational Lens"""
    CATARACT_SURGERY = "031"  # Medical Treatment/ Procedure
    """Cataract Surgery"""
    CHOLERA_IMMUNIZATION = "032"  # Medical Treatment/ Procedure
    """Cholera Immunization"""
    CHOLESTEROL_SCREENING = "033"  # Medical Treatment/ Procedure
    """Cholesterol Screening"""
    CIRCUMCISION_NEWBORN = "034"  # Medical Treatment/ Procedure
    """Circumcision - Newborn"""
    COLONOSCOPY = "035"  # Medical Treatment/ Procedure
    """Colonoscopy"""
    CONTACT_LENSES = "036"  # Medical Treatment/ Procedure
    """Contact Lenses"""
    CT_SCAN_CERVICAL_AND_LUMBAR = "037"  # Medical Treatment/ Procedure
    """CT Scan - Cervical &amp; Lumbar"""
    CT_SCAN_W_OR_IV_CONTRAST_MEDIA_INTO_VEIN = "038"  # Medical Treatment/ Procedure
    """CT Scan w/ IV Contrast Media into Vein"""
    CVS = "039"  # Medical Treatment/ Procedure
    """CVS (Chorionic Villus) Sampling"""
    CYSTOSPY = "040"  # Medical Treatment/ Procedure
    """Cystospy"""
    DISCLOSURE_OF_PROTECTED_HEALTH_INFORMATION_TO_FAMILY_OR_FRIENDS = (
        "041"  # Release of Info/ Disclosure
    )
    """Disclosure of Protected Health Information to Family/Friends"""
    D_AND_C_AND_CONIZATION = "042"  # Medical Treatment/ Procedure
    """D &amp; C and Conization"""
    DACRYOCYSTOGRAM = "043"  # Medical Treatment/ Procedure
    """Dacryocystogram"""
    DIAGNOSTIC_ISOTOPE = "044"  # Medical Treatment/ Procedure
    """Diagnostic Isotope"""
    DRAINAGE_OF_AN_ABSCESS = "045"  # Medical Treatment/ Procedure
    """Drainage of an Abscess"""
    DRUG_SCREENING = "046"  # Medical Treatment/ Procedure
    """Drug Screening"""
    ELECTRONIC_MONITORING_OF_LABOR_REFUSAL = "047"  # Medical Treatment/ Procedure
    """Electronic Monitoring of Labor - Refusal"""
    ENDOMETRIAL_BIOPSY = "048"  # Medical Treatment/ Procedure
    """Endometrial Biopsy"""
    ENDOSCOPY_OR_SCLEROSIS_OF_ESOPHAGEAL_VARICES = "049"  # Medical Treatment/ Procedure
    """Endoscopy/Sclerosis of Esophageal Varices"""
    ERCP = "050"  # Medical Treatment/ Procedure
    """ERCP"""
    EXPOSURE_TO_REPORTABLE_COMMUNICABLE_DISEASE = "051"  # Medical Treatment/ Procedure
    """Exposure to reportable Communicable Disease"""
    EXTERNAL_VERSION = "052"  # Medical Treatment/ Procedure
    """External Version"""
    FLUORESCEIN_ANGIOSCOPY = "053"  # Medical Treatment/ Procedure
    """Fluorescein Angioscopy"""
    HEPATITIS_B_CONSENT_OR_DECLINATION = "054"  # Medical Treatment/ Procedure
    """Hepatitis B - Consent/Declination"""
    HERNIOGRAM = "055"  # Medical Treatment/ Procedure
    """Herniogram"""
    HIV_TEST_CONSENT_REFUSAL = "056"  # Medical Treatment/ Procedure
    """HIV Test - Consent Refusal"""
    HIV_TEST_DISCLOSURE = "057"  # Medical Treatment/ Procedure
    """HIV Test - Disclosure"""
    HIV_TEST_PRENATAL = "058"  # Medical Treatment/ Procedure
    """HIV Test - Prenatal"""
    HOME_IV_TREATMENT_PROGRAM = "059"  # Medical Treatment/ Procedure
    """Home IV Treatment Program"""
    HOME_PARENTERAL_TREATMENT_PROGRAM = "060"  # Medical Treatment/ Procedure
    """Home Parenteral Treatment Program"""
    HYSTERECTOMY = "061"  # Medical Treatment/ Procedure
    """Hysterectomy"""
    HYSTEROSALPINGOGRAM = "062"  # Medical Treatment/ Procedure
    """Hysterosalpingogram"""
    INJECTION_SLIP_OR_CONSENT = "063"  # Medical Treatment/ Procedure
    """Injection Slip/ Consent"""
    INTRAUTERINE_DEVICE = "064"  # Medical Treatment/ Procedure
    """Intrauterine Device"""
    INTRAUTERINE_DEVICE_OR_STERILIZATION = "065"  # Medical Treatment/ Procedure
    """Intrauterine Device/Sterilization"""
    INTRAVASCULAR_INFUSION_OF_STREPTOKINASE_OR_UROKINASE = (
        "066"  # Medical Treatment/ Procedure
    )
    """Intravascular Infusion of Streptokinase/Urokinase"""
    INTRAVENOUS_CHOLANGIOGRAM = "067"  # Medical Treatment/ Procedure
    """Intravenous Cholangiogram"""
    INTRAVENOUS_DIGITAL_ANGIOGRAPHY = "068"  # Medical Treatment/ Procedure
    """Intravenous Digital Angiography"""
    IODINE_ADMINISTRATION = "069"  # Medical Treatment/ Procedure
    """Iodine Administration"""
    ISG = "070"  # Medical Treatment/ Procedure
    """ISG"""
    IVP = "071"  # Medical Treatment/ Procedure
    """IVP"""
    LASER_PHOTOCOAGULATION = "072"  # Medical Treatment/ Procedure
    """Laser Photocoagulation"""
    LASER_TREATMENT = "073"  # Medical Treatment/ Procedure
    """Laser treatment"""
    LITHIUM_CARBONATE = "074"  # Medical Treatment/ Procedure
    """Lithium Carbonate"""
    LIVER_BIOPSY = "075"  # Medical Treatment/ Procedure
    """Liver Biopsy"""
    LUMBAR_PUNCTURE = "076"  # Medical Treatment/ Procedure
    """Lumbar Puncture"""
    LYMPHANGIOGRAM = "077"  # Medical Treatment/ Procedure
    """Lymphangiogram"""
    MAO_INHIBITORS = "078"  # Medical Treatment/ Procedure
    """MAO Inhibitors"""
    MED_PSYCH_AND_OR_OR_DRUG_OR_ALCOHOL = "079"  # Release of Info/ Disclosure
    """Med, Psych, and/or Drug/Alcohol"""
    MEDICAL_TREATMENT_REFUSAL = "080"  # Administrative
    """Medical Treatment - Refusal"""
    MORNING_AFTER_PILL = "081"  # Medical Treatment/ Procedure
    """Morning-after Pill"""
    MRI_ADULT = "082"  # Medical Treatment/ Procedure
    """MRI - Adult"""
    MRI_PEDIATRIC = "083"  # Medical Treatment/ Procedure
    """MRI - Pediatric"""
    MYELOGRAM = "084"  # Medical Treatment/ Procedure
    """Myelogram"""
    NEEDLE_BIOPSY = "085"  # Medical Treatment/ Procedure
    """Needle Biopsy"""
    NEEDLE_BIOPSY_OF_LUNG = "086"  # Medical Treatment/ Procedure
    """Needle Biopsy of Lung"""
    NEWBORN_TREATMENT_AND_RELEASE = "087"  # Medical Treatment/ Procedure
    """Newborn Treatment and Release"""
    NORPLANT_SUBDERMAL_BIRTH_CONTROL_IMPLANT = "088"  # Medical Treatment/ Procedure
    """Norplant Subdermal Birth Control Implant"""
    OPERATIONS_ANESTHESIA_TRANSFUSIONS = "089"  # Medical Treatment/ Procedure
    """Operations, Anesthesia, Transfusions"""
    ORAL_CONTRACEPTIVES = "090"  # Medical Treatment/ Procedure
    """Oral Contraceptives"""
    ORGAN_DONATION = "091"  # Administrative
    """Organ Donation"""
    PATIENT_PERMITS_CONSENTS = "092"  # Administrative
    """Patient Permits, Consents"""
    PATIENT_TREATMENT_PERMIT_RELEASE_AND_ADMISSION = "093"  # Administrative
    """Patient Treatment Permit, Release &amp; Admission"""
    PENILE_INJECTIONS = "094"  # Medical Treatment/ Procedure
    """Penile Injections"""
    PERCUTANEOUS_NEPHROSTOMY = "095"  # Medical Treatment/ Procedure
    """Percutaneous Nephrostomy"""
    PERCUTANEOUS_TRANSHEPATIC_CHOLANGIOGRAM = "096"  # Medical Treatment/ Procedure
    """Percutaneous Transhepatic Cholangiogram"""
    PHOTOGRAPHS = "097"  # Release of Info/ Disclosure
    """Photographs"""
    PHOTOGRAPHS_EMPLOYEE = "098"  # Release of Info/ Disclosure
    """Photographs - Employee"""
    PHOTOGRAPHS_MEDICAL_RESEARCH = "099"  # Release of Info/ Disclosure
    """Photographs - Medical Research"""
    PHOTOGRAPHS_NEWS_MEDIA = "100"  # Release of Info/ Disclosure
    """Photographs - news Media"""
    PSYCHIATRIC_ADMISSION_NEXT_OF_KIN = "101"  # Medical Treatment/ Procedure
    """Psychiatric Admission - Next of Kin"""
    PSYCHIATRIC_INFORMATION_DURING_HOSPITAL_STAY = "102"  # Release of Info/ Disclosure
    """Psychiatric Information During Hospital Stay"""
    PUBLIC_RELEASE_OF_INFORMATION = "103"  # Release of Info/ Disclosure
    """Public Release of Information"""
    RADIOLOGIC_PROCEDURE = "104"  # Medical Treatment/ Procedure
    """Radiologic Procedure"""
    REFUSAL_OF_TREATMENT = "105"  # Administrative
    """Refusal of Treatment"""
    RELEASE_OF_BODY = "106"  # Administrative
    """Release of Body"""
    RELEASE_OF_LIMB = "107"  # Administrative
    """Release of Limb"""
    RH_IMMUNE_GLOBULIN = "108"  # Medical Treatment/ Procedure
    """Rh Immune Globulin"""
    RIGHTS_OF_MEDICAL_RESEARCH_PARTICIPANTS = "109"  # Administrative
    """Rights of Medical Research Participants"""
    REQUEST_TO_RESTRICT_ACCESS_OR_DISCLOSURE_TO_MEDICAL_RECORD_OR_PROTECTED_HEALTH_INFORMATION = "110"  # Release of Info/ Disclosure
    """Request to Restrict Access/Disclosure to Medical Record/Protected Health Information"""
    REQUEST_FOR_REMAIN_ANONYMOUS = "111"  # Release of Info/ Disclosure
    """Request for Remain Anonymous"""
    SEAT_BELT_EXEMPTION = "112"  # Administrative
    """Seat Belt Exemption"""
    SIALOGRAM = "113"  # Medical Treatment/ Procedure
    """Sialogram"""
    VOIDING_CYSTOGRAM = "1137"  # Medical Treatment/ Procedure
    """Voiding Cystogram"""
    SIGMOIDOSCOPY = "114"  # Medical Treatment/ Procedure
    """Sigmoidoscopy"""
    STERILIZATION_ANESTHESIA_AND_MEDICAL_SERVICES = (
        "115"  # Medical Treatment/ Procedure
    )
    """Sterilization - Anesthesia &amp; Medical Services"""
    STERILIZATION_FEDERALLY_FUNDED = "116"  # Medical Treatment/ Procedure
    """Sterilization -Federally Funded"""
    STERILIZATION_FEMALE = "117"  # Medical Treatment/ Procedure
    """Sterilization - Female"""
    STERILIZATION_LAPAROSCOPY_OR_POMEROY = "118"  # Medical Treatment/ Procedure
    """Sterilization - Laparoscopy/Pomeroy"""
    STERILIZATION_NON_FEDERALLY_FUNDED = "119"  # Medical Treatment/ Procedure
    """Sterilization - Non-Federally Funded"""
    STERILIZATION_SECONDARY = "120"  # Medical Treatment/ Procedure
    """Sterilization - Secondary"""
    TRANQUILIZERS = "121"  # Medical Treatment/ Procedure
    """Tranquilizers"""
    TRANSFER_ACKNOWLEDGEMENT = "122"  # Medical Treatment/ Procedure
    """Transfer - Acknowledgement"""
    TRANSFER_AUTHORIZATION = "123"  # Medical Treatment/ Procedure
    """Transfer - Authorization"""
    TRANSFER_CERTIFICATION_PHYSICIAN = "124"  # Medical Treatment/ Procedure
    """Transfer Certification - Physician"""
    TRANSFER_OR_DISCHARGE_REQUEST = "125"  # Medical Treatment/ Procedure
    """Transfer/Discharge Request"""
    TRANSFER_FOR_NON_MEDICAL_REASONS = "126"  # Medical Treatment/ Procedure
    """Transfer for Non-Medical Reasons"""
    TRANSFER_INTERFACULTY_NEONATAL = "127"  # Medical Treatment/ Procedure
    """Transfer - Interfaculty Neonatal"""
    TRANSFER_REFUSAL = "128"  # Medical Treatment/ Procedure
    """Transfer Refusal"""
    TRANSFER_REFUSAL_OF_FURTHER_TREATMENT = "129"  # Medical Treatment/ Procedure
    """Transfer Refusal of Further Treatment"""
    TREADMILL_AND_EKG = "130"  # Medical Treatment/ Procedure
    """Treadmill &amp; EKG"""
    TREADMILL_THALLIUM_201 = "131"  # Medical Treatment/ Procedure
    """Treadmill, Thallium-201"""
    TYPHOID = "132"  # Medical Treatment/ Procedure
    """Typhoid"""
    USE_OF_INVESTIGATIONAL_DEVICE = "133"  # Medical Treatment/ Procedure
    """Use of Investigational Device"""
    USE_OF_INVESTIGATIONAL_DRUG = "134"  # Medical Treatment/ Procedure
    """Use of Investigational Drug"""
    VENOGRAM = "135"  # Medical Treatment/ Procedure
    """Venogram"""
    VIDEOTAPE = "136"  # Release of Info/ Disclosure
    """Videotape"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConsentType.RELEASE_OF_INFORMATION_OR_MR_OR_AUTHORIZATION_TO_DISCLOSURE_PROTECTED_HEALTH_INFORMATION: "Release of Information/MR / Authorization to Disclosure Protected Health Information",
    ConsentType.MEDICAL_PROCEDURE: "Medical Procedure (invasive)",
    ConsentType.ACKNOWLEDGE_RECEIPT_OF_PRIVACY_NOTICE: "Acknowledge Receipt of Privacy Notice",
    ConsentType.ABORTION: "Abortion",
    ConsentType.ABORTION_OR_LAMINARIA: "Abortion/Laminaria",
    ConsentType.ACCUTANE_INFORMATION: "Accutane - Information",
    ConsentType.ACCUTANE_WOMAN: "Accutane - Woman",
    ConsentType.ADVANCED_BENEFICIARY_NOTICE: "Advanced Beneficiary Notice",
    ConsentType.AFP: "AFP (Alpha Fetoprotein) Screening",
    ConsentType.AMNIOCENTESIS: "Amniocentesis (consent &amp; refusal)",
    ConsentType.ANATOMICAL_GIFT: "Anatomical Gift (organ donation)",
    ConsentType.ANESTHESIA_COMPLICATIONS: "Anesthesia - Complications",
    ConsentType.ANESTHESIA_QUESTIONNAIRE: "Anesthesia - Questionnaire",
    ConsentType.ANGIOGRAM: "Angiogram",
    ConsentType.ANGIOPLASTY: "Angioplasty",
    ConsentType.ANTICANCER_DRUGS: "Anticancer Drugs",
    ConsentType.ANTIPSYCHOTIC_MEDICATIONS: "Antipsychotic Medications",
    ConsentType.ARTHROGRAM: "Arthrogram",
    ConsentType.AUTOPSY: "Autopsy",
    ConsentType.AZT_THERAPY: "AZT Therapy",
    ConsentType.BILIARY_DRAINAGE: "Biliary Drainage",
    ConsentType.BILIARY_STONE_EXTRACTION: "Biliary Stone Extraction",
    ConsentType.BIOPSY: "Biopsy",
    ConsentType.BLEEDING_TIME_TEST: "Bleeding Time Test",
    ConsentType.BRONCHOGRAM: "Bronchogram",
    ConsentType.CARDIAC_CATHETERIZATION: "Cardiac Catheterization",
    ConsentType.CORONARY_ANGIOGRAPHY: "Coronary Angiography",
    ConsentType.W_OR_O_SURGERY_CAPABILITY: "w/o Surgery Capability",
    ConsentType.CATARACT_OP_OR_IMPLANT_OF_FDA_APRVD_LENS: "Cataract Op/Implant of FDA Aprvd Lens",
    ConsentType.CATARACT_OP_OR_IMPLANT_OF_INVESTIGATIONAL_LENS: "Cataract Op/Implant of Investigational Lens",
    ConsentType.CATARACT_SURGERY: "Cataract Surgery",
    ConsentType.CHOLERA_IMMUNIZATION: "Cholera Immunization",
    ConsentType.CHOLESTEROL_SCREENING: "Cholesterol Screening",
    ConsentType.CIRCUMCISION_NEWBORN: "Circumcision - Newborn",
    ConsentType.COLONOSCOPY: "Colonoscopy",
    ConsentType.CONTACT_LENSES: "Contact Lenses",
    ConsentType.CT_SCAN_CERVICAL_AND_LUMBAR: "CT Scan - Cervical &amp; Lumbar",
    ConsentType.CT_SCAN_W_OR_IV_CONTRAST_MEDIA_INTO_VEIN: "CT Scan w/ IV Contrast Media into Vein",
    ConsentType.CVS: "CVS (Chorionic Villus) Sampling",
    ConsentType.CYSTOSPY: "Cystospy",
    ConsentType.DISCLOSURE_OF_PROTECTED_HEALTH_INFORMATION_TO_FAMILY_OR_FRIENDS: "Disclosure of Protected Health Information to Family/Friends",
    ConsentType.D_AND_C_AND_CONIZATION: "D &amp; C and Conization",
    ConsentType.DACRYOCYSTOGRAM: "Dacryocystogram",
    ConsentType.DIAGNOSTIC_ISOTOPE: "Diagnostic Isotope",
    ConsentType.DRAINAGE_OF_AN_ABSCESS: "Drainage of an Abscess",
    ConsentType.DRUG_SCREENING: "Drug Screening",
    ConsentType.ELECTRONIC_MONITORING_OF_LABOR_REFUSAL: "Electronic Monitoring of Labor - Refusal",
    ConsentType.ENDOMETRIAL_BIOPSY: "Endometrial Biopsy",
    ConsentType.ENDOSCOPY_OR_SCLEROSIS_OF_ESOPHAGEAL_VARICES: "Endoscopy/Sclerosis of Esophageal Varices",
    ConsentType.ERCP: "ERCP",
    ConsentType.EXPOSURE_TO_REPORTABLE_COMMUNICABLE_DISEASE: "Exposure to reportable Communicable Disease",
    ConsentType.EXTERNAL_VERSION: "External Version",
    ConsentType.FLUORESCEIN_ANGIOSCOPY: "Fluorescein Angioscopy",
    ConsentType.HEPATITIS_B_CONSENT_OR_DECLINATION: "Hepatitis B - Consent/Declination",
    ConsentType.HERNIOGRAM: "Herniogram",
    ConsentType.HIV_TEST_CONSENT_REFUSAL: "HIV Test - Consent Refusal",
    ConsentType.HIV_TEST_DISCLOSURE: "HIV Test - Disclosure",
    ConsentType.HIV_TEST_PRENATAL: "HIV Test - Prenatal",
    ConsentType.HOME_IV_TREATMENT_PROGRAM: "Home IV Treatment Program",
    ConsentType.HOME_PARENTERAL_TREATMENT_PROGRAM: "Home Parenteral Treatment Program",
    ConsentType.HYSTERECTOMY: "Hysterectomy",
    ConsentType.HYSTEROSALPINGOGRAM: "Hysterosalpingogram",
    ConsentType.INJECTION_SLIP_OR_CONSENT: "Injection Slip/ Consent",
    ConsentType.INTRAUTERINE_DEVICE: "Intrauterine Device",
    ConsentType.INTRAUTERINE_DEVICE_OR_STERILIZATION: "Intrauterine Device/Sterilization",
    ConsentType.INTRAVASCULAR_INFUSION_OF_STREPTOKINASE_OR_UROKINASE: "Intravascular Infusion of Streptokinase/Urokinase",
    ConsentType.INTRAVENOUS_CHOLANGIOGRAM: "Intravenous Cholangiogram",
    ConsentType.INTRAVENOUS_DIGITAL_ANGIOGRAPHY: "Intravenous Digital Angiography",
    ConsentType.IODINE_ADMINISTRATION: "Iodine Administration",
    ConsentType.ISG: "ISG",
    ConsentType.IVP: "IVP",
    ConsentType.LASER_PHOTOCOAGULATION: "Laser Photocoagulation",
    ConsentType.LASER_TREATMENT: "Laser treatment",
    ConsentType.LITHIUM_CARBONATE: "Lithium Carbonate",
    ConsentType.LIVER_BIOPSY: "Liver Biopsy",
    ConsentType.LUMBAR_PUNCTURE: "Lumbar Puncture",
    ConsentType.LYMPHANGIOGRAM: "Lymphangiogram",
    ConsentType.MAO_INHIBITORS: "MAO Inhibitors",
    ConsentType.MED_PSYCH_AND_OR_OR_DRUG_OR_ALCOHOL: "Med, Psych, and/or Drug/Alcohol",
    ConsentType.MEDICAL_TREATMENT_REFUSAL: "Medical Treatment - Refusal",
    ConsentType.MORNING_AFTER_PILL: "Morning-after Pill",
    ConsentType.MRI_ADULT: "MRI - Adult",
    ConsentType.MRI_PEDIATRIC: "MRI - Pediatric",
    ConsentType.MYELOGRAM: "Myelogram",
    ConsentType.NEEDLE_BIOPSY: "Needle Biopsy",
    ConsentType.NEEDLE_BIOPSY_OF_LUNG: "Needle Biopsy of Lung",
    ConsentType.NEWBORN_TREATMENT_AND_RELEASE: "Newborn Treatment and Release",
    ConsentType.NORPLANT_SUBDERMAL_BIRTH_CONTROL_IMPLANT: "Norplant Subdermal Birth Control Implant",
    ConsentType.OPERATIONS_ANESTHESIA_TRANSFUSIONS: "Operations, Anesthesia, Transfusions",
    ConsentType.ORAL_CONTRACEPTIVES: "Oral Contraceptives",
    ConsentType.ORGAN_DONATION: "Organ Donation",
    ConsentType.PATIENT_PERMITS_CONSENTS: "Patient Permits, Consents",
    ConsentType.PATIENT_TREATMENT_PERMIT_RELEASE_AND_ADMISSION: "Patient Treatment Permit, Release &amp; Admission",
    ConsentType.PENILE_INJECTIONS: "Penile Injections",
    ConsentType.PERCUTANEOUS_NEPHROSTOMY: "Percutaneous Nephrostomy",
    ConsentType.PERCUTANEOUS_TRANSHEPATIC_CHOLANGIOGRAM: "Percutaneous Transhepatic Cholangiogram",
    ConsentType.PHOTOGRAPHS: "Photographs",
    ConsentType.PHOTOGRAPHS_EMPLOYEE: "Photographs - Employee",
    ConsentType.PHOTOGRAPHS_MEDICAL_RESEARCH: "Photographs - Medical Research",
    ConsentType.PHOTOGRAPHS_NEWS_MEDIA: "Photographs - news Media",
    ConsentType.PSYCHIATRIC_ADMISSION_NEXT_OF_KIN: "Psychiatric Admission - Next of Kin",
    ConsentType.PSYCHIATRIC_INFORMATION_DURING_HOSPITAL_STAY: "Psychiatric Information During Hospital Stay",
    ConsentType.PUBLIC_RELEASE_OF_INFORMATION: "Public Release of Information",
    ConsentType.RADIOLOGIC_PROCEDURE: "Radiologic Procedure",
    ConsentType.REFUSAL_OF_TREATMENT: "Refusal of Treatment",
    ConsentType.RELEASE_OF_BODY: "Release of Body",
    ConsentType.RELEASE_OF_LIMB: "Release of Limb",
    ConsentType.RH_IMMUNE_GLOBULIN: "Rh Immune Globulin",
    ConsentType.RIGHTS_OF_MEDICAL_RESEARCH_PARTICIPANTS: "Rights of Medical Research Participants",
    ConsentType.REQUEST_TO_RESTRICT_ACCESS_OR_DISCLOSURE_TO_MEDICAL_RECORD_OR_PROTECTED_HEALTH_INFORMATION: "Request to Restrict Access/Disclosure to Medical Record/Protected Health Information",
    ConsentType.REQUEST_FOR_REMAIN_ANONYMOUS: "Request for Remain Anonymous",
    ConsentType.SEAT_BELT_EXEMPTION: "Seat Belt Exemption",
    ConsentType.SIALOGRAM: "Sialogram",
    ConsentType.VOIDING_CYSTOGRAM: "Voiding Cystogram",
    ConsentType.SIGMOIDOSCOPY: "Sigmoidoscopy",
    ConsentType.STERILIZATION_ANESTHESIA_AND_MEDICAL_SERVICES: "Sterilization - Anesthesia &amp; Medical Services",
    ConsentType.STERILIZATION_FEDERALLY_FUNDED: "Sterilization -Federally Funded",
    ConsentType.STERILIZATION_FEMALE: "Sterilization - Female",
    ConsentType.STERILIZATION_LAPAROSCOPY_OR_POMEROY: "Sterilization - Laparoscopy/Pomeroy",
    ConsentType.STERILIZATION_NON_FEDERALLY_FUNDED: "Sterilization - Non-Federally Funded",
    ConsentType.STERILIZATION_SECONDARY: "Sterilization - Secondary",
    ConsentType.TRANQUILIZERS: "Tranquilizers",
    ConsentType.TRANSFER_ACKNOWLEDGEMENT: "Transfer - Acknowledgement",
    ConsentType.TRANSFER_AUTHORIZATION: "Transfer - Authorization",
    ConsentType.TRANSFER_CERTIFICATION_PHYSICIAN: "Transfer Certification - Physician",
    ConsentType.TRANSFER_OR_DISCHARGE_REQUEST: "Transfer/Discharge Request",
    ConsentType.TRANSFER_FOR_NON_MEDICAL_REASONS: "Transfer for Non-Medical Reasons",
    ConsentType.TRANSFER_INTERFACULTY_NEONATAL: "Transfer - Interfaculty Neonatal",
    ConsentType.TRANSFER_REFUSAL: "Transfer Refusal",
    ConsentType.TRANSFER_REFUSAL_OF_FURTHER_TREATMENT: "Transfer Refusal of Further Treatment",
    ConsentType.TREADMILL_AND_EKG: "Treadmill &amp; EKG",
    ConsentType.TREADMILL_THALLIUM_201: "Treadmill, Thallium-201",
    ConsentType.TYPHOID: "Typhoid",
    ConsentType.USE_OF_INVESTIGATIONAL_DEVICE: "Use of Investigational Device",
    ConsentType.USE_OF_INVESTIGATIONAL_DRUG: "Use of Investigational Drug",
    ConsentType.VENOGRAM: "Venogram",
    ConsentType.VIDEOTAPE: "Videotape",
}
