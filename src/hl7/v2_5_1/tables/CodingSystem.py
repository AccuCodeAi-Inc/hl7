from ...base import HL7Table

"""
HL7 Version: 2.5.1
Coding system - 0396
Table Type: HL7
"""


class CodingSystem(HL7Table):
    """
    Coding system - 0396 // HL7 table type
    - LOCAL_GENERAL_CODE
    - AMERICAN_COLLEGE_OF_RADIOLOGY_FINDING_CODES
    - HL7_SET_OF_UNITS_OF_MEASURE
    - WHO_ADVERSE_REACTION_TERMS
    - ASTM_E1238_OR_E1467_UNIVERSAL
    - AS4_NEUROPHYSIOLOGY_CODES
    - AMERICAN_TYPE_CULTURE_COLLECTION
    - CPT_4
    - CPT_5
    - CHEMICAL_ABSTRACT_CODES
    - CDT_2_CODES
    - CDC_ANALYTE_CODES
    - CDC_METHODS_OR_INSTRUMENTS_CODES
    - CDC_SURVEILLANCE
    - CEN_ECG_DIAGNOSTIC_CODES
    - CLIP
    - CPT_MODIFIER_CODE
    - COSTART
    - CDC_VACCINE_CODES
    - DICOM_CONTROLLED_TERMINOLOGY
    - EUCLIDES
    - EUCLIDES_QUANTITY_CODES
    - EUCLIDES_LAB_METHOD_CODES
    - EUCLIDES_LAB_EQUIPMENT_CODES
    - ENZYME_CODES
    - FIRST_DATABANK_DRUG_CODES
    - FIRST_DATABANK_DIAGNOSTIC_CODES
    - FDA_K10
    - HIBCC
    - CMS
    - HEALTH_CARE_PROVIDER_TAXONOMY
    - HOME_HEALTH_CARE
    - HEALTH_OUTCOMES
    - HL7_DEFINED_CODES_WHERE_NNNN_IS_THE_HL7_TABLE_NUMBER
    - JAPANESE_NATIONWIDE_MEDICINE_CODE
    - HPC
    - ICD_10
    - ICD_10_PROCEDURE_CODES
    - ICD9
    - ICD_9CM
    - ISBT
    - ISBT_128_CODES_WHERE_NNNN_SPECIFIES_A_SPECIFIC_TABLE_WITHIN_ISBT_128
    - ICHPPC_2
    - ICD_10_AUSTRALIAN_MODIFICATION
    - ICD_10_CANADA
    - INTERNATIONAL_CLASSIFICATION_OF_DISEASES_FOR_ONCOLOGY
    - ICCS
    - INTERNATIONAL_CLASSIFICATION_OF_SLEEP_DISORDERS
    - ISO_2955_83
    - ISO_DEFINED_CODES_WHERE_NNNN_IS_THE_ISO_TABLE_NUMBER
    - IUPAC_OR_IFCC_COMPONENT_CODES
    - IUPAC_OR_IFCC_PROPERTY_CODES
    - JLAC_OR_JSLM_NATIONWIDE_LABORATORY_CODE
    - JAPANESE_CHEMISTRY
    - JAPANESE_IMAGE_EXAMINATION_CACHE
    - LOCAL_BILLING_CODE
    - LOGICAL_OBSERVATION_IDENTIFIER_NAMES_AND_CODES
    - MEDICAID
    - MEDICARE
    - MEDISPAN_DIAGNOSTIC_CODES
    - MEDICAL_ECONOMICS_DRUG_CODES
    - MEDICAL_DICTIONARY_FOR_DRUG_REGULATORY_AFFAIRS
    - MEDICAL_ECONOMICS_DIAGNOSTIC_CODES
    - MEDISPAN_GPI
    - CDC_VACCINE_MANUFACTURER_CODES
    - NANDA
    - NATIONAL_DRUG_CODES
    - NURSING_INTERVENTIONS_CLASSIFICATION
    - NATIONAL_PROVIDER_IDENTIFIER
    - NATIONAL_UNIFORM_BILLING_COMMITTEE_CODE
    - OMAHA_SYSTEM
    - OMAHA
    - POS_CODES
    - READ_CLASSIFICATION
    - SNOMED_DICOM_MICROGLOSSARY
    - SYSTEMIZED_NOMENCLATURE_OF_MEDICINE
    - SNOMED_INTERNATIONAL
    - SNOMED_TOPOLOGY_CODES
    - UCDS
    - MDNS
    - UNIFIED_MEDICAL_LANGUAGE
    - UNIVERSAL_PRODUCT_CODE
    - UPIN
    - UNITED_STATES_POSTAL_SERVICE
    - WHO_RECORD_POUND_DRUG_CODES
    - W2
    - WHO_RECORD_POUND_CODE_WITH_ASTM_EXTENSION
    - WHO_ATC
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0396
    """

    LOCAL_GENERAL_CODE = "99zzz or L"  # Locally defined codes for purpose of sender or receiver. Local codes can be identified by L (for backward compatibility) or 99zzz (where z is an alphanumeric character).
    """Local general code (where z is an alphanumeric character)"""
    AMERICAN_COLLEGE_OF_RADIOLOGY_FINDING_CODES = "ACR"  # Index for Radiological Diagnosis Revised, 3rd Edition 1986, American College of Radiology, Reston, VA.
    """American College of Radiology finding codes"""
    HL7_SET_OF_UNITS_OF_MEASURE = "ANS+"  # HL7 set of units of measure based upon ANSI X3.50 - 1986, ISO 2988-83, and US customary units / see chapter 7, section 7.4.2.6.
    """HL7 set of units of measure"""
    WHO_ADVERSE_REACTION_TERMS = "ART"  # WHO Collaborating Centre for International Drug Monitoring, Box 26, S-751 03, Uppsala, Sweden.
    """WHO Adverse Reaction Terms"""
    ASTM_E1238_OR_E1467_UNIVERSAL = "AS4"  # American Society for Testing &amp; Materials and CPT4 (see Appendix X1 of Specification E1238 and Appendix X2 of Specification E1467).
    """ASTM E1238/ E1467 Universal"""
    AS4_NEUROPHYSIOLOGY_CODES = "AS4E"  # ASTM’s diagnostic codes and test result coding/grading systems for clinical neurophysiology. See ASTM Specification E1467, Appendix 2.
    """AS4 Neurophysiology Codes"""
    AMERICAN_TYPE_CULTURE_COLLECTION = "ATC"  # Reference cultures (microorganisms, tissue cultures, etc.), related biological materials and associated data. American Type Culture Collection, 12301 Parklawn Dr, Rockville MD, 20852. (301) 881-2600. http://www.atcc.org
    """American Type Culture Collection"""
    CPT_4 = "C4"  # American Medical Association, P.O. Box 10946, Chicago IL  60610.
    """CPT-4"""
    CPT_5 = "C5"  # (under development - same contact as above)
    """CPT-5"""
    CHEMICAL_ABSTRACT_CODES = "CAS"  # These include unique codes for each unique chemical, including all generic drugs. The codes do not distinguish among different dosing forms. When multiple equivalent CAS numbers exist, use the first one listed in USAN. USAN 1990 and the USP dictionary of drug names, William M. Heller, Ph.D., Executive Editor, United States Pharmacopeial Convention, Inc., 12601 Twinbrook Parkway, Rockville, MD 20852.
    """Chemical abstract codes"""
    CDT_2_CODES = "CD2"  # American Dental Association’s Current Dental Terminology (CDT-2) code. American Dental Association, 211 E. Chicago Avenue,. Chicago, Illinois 60611.
    """CDT-2 Codes"""
    CDC_ANALYTE_CODES = "CDCA"  # As above, for CDCM
    """CDC Analyte Codes"""
    CDC_METHODS_OR_INSTRUMENTS_CODES = "CDCM"  # Public Health Practice Program Office, Centers for Disease Control and Prevention, 4770 Buford Highway, Atlanta, GA, 30421. Also available via FTP: ftp://ftp.cdc.gov/pub/laboratory_info/CLIA/.
    """CDC Methods/Instruments Codes"""
    CDC_SURVEILLANCE = "CDS"  # CDC Surveillance Codes. For data unique to specific public health surveillance requirements. Epidemiology Program Office, Centers for Disease Control and Prevention, 1600 Clifton Rd, Atlanta, GA, 30333. (404) 639-3661.
    """CDC Surveillance"""
    CEN_ECG_DIAGNOSTIC_CODES = "CE"  # CEN PT007. A quite comprehensive set of ECG diagnostic codes (abbreviations) and descriptions published as a pre-standard by CEN TC251. Available from CEN TC251 secretariat, c/o Georges DeMoor, State University Hospital Gent, De Pintelaan 185-5K3, 9000 Gent, Belgium or Jos Willems, University of Gathuisberg, 49 Herestraat, 3000 Leuven, Belgium.
    """CEN ECG diagnostic codes"""
    CLIP = "CLP"  # Simon Leeming, Beth Israel Hospital, Boston MA. Codes for radiology reports.
    """CLIP"""
    CPT_MODIFIER_CODE = "CPTM"  # Available for the AMA at the address listed for CPT above. These codes are found in Appendix A of CPT 2000 Standard Edition. (CPT 2000 Standard Edition, American Medical Association, Chicago, IL).
    """CPT Modifier Code"""
    COSTART = "CST"  # International coding system for adverse drug reactions. In the USA, maintained by the FDA, Rockville, MD.
    """COSTART"""
    CDC_VACCINE_CODES = "CVX"  # National Immunization Program, Centers for Disease Control and Prevention, 1660 Clifton Road, Atlanta, GA, 30333
    """CDC Vaccine Codes"""
    DICOM_CONTROLLED_TERMINOLOGY = "DCM"  # Codes defined in DICOM Content Mapping Resource. Digital Imaging and Communications in Medicine (DICOM). NEMA Publication PS-3.16 National Electrical Manufacturers Association (NEMA). Rosslyn, VA, 22209. Available at: http://medical.nema.org
    """DICOM Controlled Terminology"""
    EUCLIDES = "E"  # Available from Euclides Foundation International nv, Excelsiorlaan 4A, B-1930 Zaventem, Belgium; Phone: 32 2 720 90 60.
    """EUCLIDES"""
    EUCLIDES_QUANTITY_CODES = (
        "E5"  # Available from Euclides Foundation International nv (see above)
    )
    """Euclides quantity codes"""
    EUCLIDES_LAB_METHOD_CODES = "E6"  # Available from Euclides Foundation International nv, Excelsiorlaan 4A, B-1930 Zaventem, Belgium; Phone : 32 2 720 90 60.
    """Euclides Lab method codes"""
    EUCLIDES_LAB_EQUIPMENT_CODES = (
        "E7"  # Available from Euclides Foundation International nv (see above)
    )
    """Euclides Lab equipment codes"""
    ENZYME_CODES = "ENZC"  # Enzyme Committee of the International Union of Biochemistry and Molecular Biology. Enzyme Nomenclature: Recommendations on the Nomenclature and Classification of Enzyme-Catalysed Reactions. London: Academic Press, 1992.
    """Enzyme Codes"""
    FIRST_DATABANK_DRUG_CODES = "FDDC"  # National Drug Data File. Proprietary product of First DataBank, Inc. (800) 633-3453, or http://www.firstdatabank.com.
    """First DataBank Drug Codes"""
    FIRST_DATABANK_DIAGNOSTIC_CODES = "FDDX"  # Used for drug-diagnosis interaction checking. Proprietary product of First DataBank, Inc. As above for FDDC.
    """First DataBank Diagnostic Codes"""
    FDA_K10 = "FDK"  # Dept. of Health &amp; Human Services, Food &amp; Drug Administration, Rockville, MD 20857. (device &amp; analyte process codes).
    """FDA K10"""
    HIBCC = "HB"  # Health Industry Business Communications Council, 5110 N. 40th St., Ste 120, Phoenix, AZ 85018.
    """HIBCC"""
    CMS = "HCPCS"  # HCPCS: contains codes for medical equipment, injectable drugs, transportation services, and other services not found in CPT4.[7]
    """CMS (formerly HCFA) Common Procedure Coding System"""
    HEALTH_CARE_PROVIDER_TAXONOMY = "HCPT"  # The Blue Cross and Blue Shield Association will act as the administrator of the Provider Taxonomy so that the code structure is classified as external to X12. Ongoing maintenance is solely the responsibility of Workgroup 15 (Provider Information) within ANSI ASC X12N, or the work group’s successor.  Blue Cross and Blue Shield Association, 225 North Michigan Avenue, Chicago, IL 60601, Attention: ITS Department, ECNS Unit. http://www.wpc-edi.com/taxonomy/ Primary distribution is the responsibility of Washington Publishing Company, through its World Wide Web Site, at the same web site.
    """Health Care Provider Taxonomy"""
    HOME_HEALTH_CARE = "HHC"  # Home Health Care Classification System; Virginia Saba, EdD, RN; Georgetown University School of Nursing; Washington, DC.
    """Home Health Care"""
    HEALTH_OUTCOMES = "HI"  # Health Outcomes Institute codes for outcome variables available (with responses) from Stratis Health (formerly Foundation for Health Care Evaluation and Health Outcomes Institute), 2901 Metro Drive, Suite 400, Bloomington, MN, 55425-1525; (612) 854-3306 (voice); (612) 853-8503 (fax); info@stratishealth.org. See examples in the Implementation Guide.
    """Health Outcomes"""
    HL7_DEFINED_CODES_WHERE_NNNN_IS_THE_HL7_TABLE_NUMBER = (
        "HL7nnnn"  # Health Level Seven where nnnn is the HL7 table number
    )
    """HL7 Defined Codes where nnnn is the HL7 table number"""
    JAPANESE_NATIONWIDE_MEDICINE_CODE = "HOT"
    """Japanese Nationwide Medicine Code"""
    HPC = "HPC"  # Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS) including modifiers.[8]http://www.cms.hhs.gov/MedHCPCSGenInfo/
    """CMS (formerly HCFA )Procedure Codes (HCPCS)"""
    ICD_10 = "I10"  # World Health Publications, Albany, NY.
    """ICD-10"""
    ICD_10_PROCEDURE_CODES = "I10P"  # Procedure Coding System (ICD-10-PCS.)  See http://www.cms.hhs.gov/ICD9ProviderDiagnosticCodes/08_ICD10.aspfor more information.
    """ICD-10 Procedure Codes"""
    ICD9 = "I9"  # World Health Publications, Albany, NY.
    """ICD9"""
    ICD_9CM = "I9C"  # Commission on Professional and Hospital Activities, 1968 Green Road, Ann Arbor, MI 48105 (includes all procedures and diagnostic tests).
    """ICD-9CM"""
    ISBT = "IBT"  # Retained for backward compatibility only as of v 2.5. This code value has been superceded by IBTnnnn. International Society of Blood Transfusion. Blood Group Terminology 1990. VOX Sanquines 1990 58(2):152-169.
    """ISBT"""
    ISBT_128_CODES_WHERE_NNNN_SPECIFIES_A_SPECIFIC_TABLE_WITHIN_ISBT_128 = "IBTnnnn"  # International Society of Blood Transfusion. (specific contact information will be supplied to editor.) The variable suffix (nnnn) identifies a specific table within ISBT 128.
    """ISBT 128 codes where nnnn specifies a specific table within ISBT 128."""
    ICHPPC_2 = "IC2"  # International Classification of Health Problems in Primary Care, Classification Committee of World Organization of National Colleges, Academies and Academic Associations of General Practitioners (WONCA), 3rd edition. An adaptation of ICD9 intended for use in General Medicine, Oxford University Press.
    """ICHPPC-2"""
    ICD_10_AUSTRALIAN_MODIFICATION = "ICD10AM"
    """ICD-10 Australian modification"""
    ICD_10_CANADA = "ICD10CA"
    """ICD-10 Canada"""
    INTERNATIONAL_CLASSIFICATION_OF_DISEASES_FOR_ONCOLOGY = "ICDO"  # International Classification of Diseases for Oncology, 2nd Edition. World Health Organization: Geneva, Switzerland, 1990. Order from: College of American Pathologists, 325 Waukegan Road, Northfield, IL, 60093-2750. (847) 446-8800.
    """International Classification of Diseases for Oncology"""
    ICCS = "ICS"  # Commission on Professional and Hospital Activities, 1968 Green Road, Ann Arbor, MI 48105.
    """ICCS"""
    INTERNATIONAL_CLASSIFICATION_OF_SLEEP_DISORDERS = "ICSD"  # International Classification of Sleep Disorders Diagnostic and Coding Manual, 1990, available from American Sleep Disorders Association, 604 Second Street SW, Rochester, MN  55902
    """International Classification of Sleep Disorders"""
    ISO_2955_83 = "ISO+"  # See chapter 7, section 7.4.2.6
    """ISO 2955.83 (units of measure) with HL7 extensions"""
    ISO_DEFINED_CODES_WHERE_NNNN_IS_THE_ISO_TABLE_NUMBER = "ISOnnnn"  # International Standards Organization where nnnn is the ISO table number
    """ISO Defined Codes where nnnn is the ISO table number"""
    IUPAC_OR_IFCC_COMPONENT_CODES = "IUPC"  # Codes used by IUPAC/IFF to identify the component (analyte) measured. Contact Henrik Olesen, as above for IUPP.
    """IUPAC/IFCC Component Codes"""
    IUPAC_OR_IFCC_PROPERTY_CODES = "IUPP"  # International Union of Pure and Applied Chemistry/International Federation of Clinical Chemistry. The Silver Book: Compendium of terminology and nomenclature of properties in clinical laboratory sciences. Oxford: Blackwell Scientific Publishers, 1995. Henrik Olesen, M.D., D.M.Sc., Chairperson, Department of Clinical Chemistry, KK76.4.2, Rigshospitalet, University Hospital of Copenhagen, DK-2200, Copenhagen.
    """IUPAC/IFCC Property Codes"""
    JLAC_OR_JSLM_NATIONWIDE_LABORATORY_CODE = "JC10"  # Source: Classification &amp;Coding for Clinical Laboratory. Japanese Society of Laboratory Medicine(JSLM, Old:Japan Society of Clinical Pathology). Version 10, 1997. A multiaxial code  including a analyte code (e.g., Rubella = 5f395), identification code (e.g., virus ab IGG=1431), a specimen code (e.g., serum =023) and a method code (e.g., ELISA = 022)
    """JLAC/JSLM, nationwide laboratory code"""
    JAPANESE_CHEMISTRY = "JC8"  # Clinical examination classification code. Japan Association of Clinical Pathology. Version 8, 1990. A multiaxial code  includ ing a subject code (e.g., Rubella = 5f395, identification code (e.g., virus ab IGG), a specimen code (e.g., serum =023) and a method code (e.g., ELISA = 022)
    """Japanese Chemistry"""
    JAPANESE_IMAGE_EXAMINATION_CACHE = "JJ1017"
    """Japanese Image Examination Cache"""
    LOCAL_BILLING_CODE = "LB"  # Local billing codes/names (with extensions if needed).
    """Local billing code"""
    LOGICAL_OBSERVATION_IDENTIFIER_NAMES_AND_CODES = "LN"  # Regenstrief Institute, c/o LOINC, 1050 Wishard Blvd., 5th floor, Indianapolis, IN  46202. 317/630-7433. Available from the Regenstrief Institute server at http://www.Regenstrief.org/loinc/loinc.htm.
    """Logical Observation Identifier Names and Codes (LOINC)"""
    MEDICAID = "MCD"  # Medicaid billing codes/names.
    """Medicaid"""
    MEDICARE = "MCR"  # Medicare billing codes/names.
    """Medicare"""
    MEDISPAN_DIAGNOSTIC_CODES = "MDDX"  # Codes Used for drug-diagnosis interaction checking. Proprietary product. Hierarchical drug codes for identifying drugs down to manufacturer and pill size. MediSpan, Inc., 8425 Woodfield Crossing Boulevard, Indianapolis, IN 46240. Tel: (800) 428-4495. http://www.medispan.com/Products/index.aspx?cat=1  as above for MGPI.
    """Medispan Diagnostic Codes"""
    MEDICAL_ECONOMICS_DRUG_CODES = "MEDC"  # Proprietary Codes for identifying drugs. Proprietary product of Medical Economics Data, Inc. (800) 223-0581.
    """Medical Economics Drug Codes"""
    MEDICAL_DICTIONARY_FOR_DRUG_REGULATORY_AFFAIRS = "MEDR"  # Dr. Louise Wood, Medicines Control Agency, Market Towers, 1 Nine Elms Lane, London SW85NQ, UK   Tel: (44)0 171-273-0000   http://www.meddramsso.com/MSSOWeb/index.htm
    """Medical Dictionary for Drug Regulatory Affairs (MEDDRA)"""
    MEDICAL_ECONOMICS_DIAGNOSTIC_CODES = "MEDX"  # Used for drug-diagnosis interaction checking. Proprietary product of Medical Economics Data, Inc. (800) 223-0581.
    """Medical Economics Diagnostic Codes"""
    MEDISPAN_GPI = "MGPI"  # Medispan hierarchical drug codes for identifying drugs down to manufacturer and pill size. Proprietary product of MediSpan, Inc., 8425 Woodfield Crossing Boulevard, Indianapolis, IN 46240. Tel: (800) 428-4495.
    """Medispan GPI"""
    CDC_VACCINE_MANUFACTURER_CODES = "MVX"  # As above, for CVX
    """CDC Vaccine Manufacturer Codes"""
    NANDA = "NDA"  # North American Nursing Diagnosis Association, Philadelphia, PA.
    """NANDA"""
    NATIONAL_DRUG_CODES = "NDC"  # These provide unique codes for each distinct drug, dosing form, manufacturer, and packaging. (Available from the National Drug Code Directory, FDA, Rockville, MD, and other sources.)
    """National drug codes"""
    NURSING_INTERVENTIONS_CLASSIFICATION = "NIC"  # Iowa Intervention Project, College of Nursing, University of Iowa, Iowa City, Iowa
    """Nursing Interventions Classification"""
    NATIONAL_PROVIDER_IDENTIFIER = "NPI"  # Health Care Finance Administration, US Dept. of Health and Human Services, 7500 Security Blvd., Baltimore, MD 21244.
    """National Provider Identifier"""
    NATIONAL_UNIFORM_BILLING_COMMITTEE_CODE = "NUBC"
    """National Uniform Billing Committee Code"""
    OMAHA_SYSTEM = "OHA"  # Omaha Visiting Nurse Association, Omaha, NB.
    """Omaha System"""
    OMAHA = "OHA"  # Omaha Visiting Nurse Association, Omaha, NB.
    """Omaha"""
    POS_CODES = "POS"  # HCFA Place of Service Codes for Professional Claims (See http://www.cms.hhs.gov/PlaceofServiceCodes/
    """POS Codes"""
    READ_CLASSIFICATION = "RC"  # The Read Clinical Classification of Medicine, Park View Surgery, 26 Leicester Rd., Loughborough LE11 2AG (includes drug procedure and other codes, as well as diagnostic codes).
    """Read Classification"""
    SNOMED_DICOM_MICROGLOSSARY = "SDM"  # College of American Pathologists, Skokie, IL, 60077-1034. (formerly designated as 99SDM).
    """SNOMED- DICOM Microglossary"""
    SYSTEMIZED_NOMENCLATURE_OF_MEDICINE = "SNM"  # Systemized Nomenclature of Medicine, 2nd Edition 1984 Vols 1, 2, College of American Pathologists, Skokie, IL.
    """Systemized Nomenclature of Medicine (SNOMED)"""
    SNOMED_INTERNATIONAL = "SNM3"  # SNOMED International, 1993 Vols 1-4, College of American Pathologists, Skokie, IL, 60077-1034.
    """SNOMED International"""
    SNOMED_TOPOLOGY_CODES = "SNT"  # College of American Pathologists, 5202 Old Orchard Road, Skokie, IL 60077-1034.
    """SNOMED topology codes (anatomic sites)"""
    UCDS = "UC"  # Uniform Clinical Data Systems. Ms. Michael McMullan, Office of Peer Review Health Care Finance Administration, The Meadows East Bldg., 6325 Security Blvd., Baltimore, MD 21207; (301) 966 6851.
    """UCDS"""
    MDNS = "UMD"  # Universal Medical Device Nomenclature System. ECRI, 5200 Butler Pike, Plymouth Meeting, PA  19462 USA. Phone: 215-825-600 0, Fax: 215-834-1275.
    """MDNS"""
    UNIFIED_MEDICAL_LANGUAGE = (
        "UML"  # National Library of Medicine, 8600 Rockville Pike, Bethesda, MD 20894.
    )
    """Unified Medical Language"""
    UNIVERSAL_PRODUCT_CODE = "UPC"  # The Uniform Code Council. 8163 Old Yankee Road, Suite J, Dayton, OH  45458; (513) 435 3070
    """Universal Product Code"""
    UPIN = "UPIN"  # Medicare/CMS s (formerly HCFA)  universal physician identification numbers, available from Health Care Financing Administration, U.S. Dept. of Health and Human Services, Bureau of Program Operations, 6325 Security Blvd., Meadows East Bldg., Room 300, Baltimore, MD 21207
    """UPIN"""
    UNITED_STATES_POSTAL_SERVICE = "USPS"  # Two Letter State and Possession Abbreviations are listed in  Publication 28, Postal Addressing Standards which can be obtained from Address Information Products, National Address Information Center, 6060 Primacy Parkway, Suite 101, Memphis, Tennessee  38188-0001 Questions of comments regarding the publication should be addressed to the Office of Address and Customer Information Systems, Customer and Automation Service Department, US Postal Service, 475 Lenfant Plaza SW Rm 7801, Washington, DC  20260-5902
    """United States Postal Service"""
    WHO_RECORD_POUND_DRUG_CODES = "W1"  # World Health organization record number code. A unique sequential number is assigned to each unique single component drug and to each multi-component drug. Eight digits are allotted to each such code, six to identify the active agent, and 2 to identify the salt, of single content drugs. Six digits are assigned to each unique combination of drugs in a dispensing unit. The six digit code is identified by W1, the 8 digit code by W2.
    """WHO record # drug codes (6 digit)"""
    W2 = "W2"  # World Health organization record number code. A unique sequential number is assigned to each unique single component drug and to each multi-component drug. Eight digits are allotted to each such code, six to identify the active agent, and 2 to identify the salt, of single content drugs. Six digits are assigned to each unique combination of drugs in a dispensing unit. The six digit code is identified by W1, the 8 digit code by W2.
    """WHO record # drug codes (8 digit)"""
    WHO_RECORD_POUND_CODE_WITH_ASTM_EXTENSION = "W4"  # With ASTM extensions (see Implementation Guide), the WHO codes can be used to report serum (and other) levels, patient compliance with drug usage instructions, average daily doses and more (see Appendix X1 the Implementation Guide).
    """WHO record # code with ASTM extension"""
    WHO_ATC = "WC"  # WHO’s ATC codes provide a hierarchical classification of drugs by therapeutic class. They are linked to the record number codes listed above.
    """WHO ATC"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CodingSystem.LOCAL_GENERAL_CODE: "Local general code (where z is an alphanumeric character)",
    CodingSystem.AMERICAN_COLLEGE_OF_RADIOLOGY_FINDING_CODES: "American College of Radiology finding codes",
    CodingSystem.HL7_SET_OF_UNITS_OF_MEASURE: "HL7 set of units of measure",
    CodingSystem.WHO_ADVERSE_REACTION_TERMS: "WHO Adverse Reaction Terms",
    CodingSystem.ASTM_E1238_OR_E1467_UNIVERSAL: "ASTM E1238/ E1467 Universal",
    CodingSystem.AS4_NEUROPHYSIOLOGY_CODES: "AS4 Neurophysiology Codes",
    CodingSystem.AMERICAN_TYPE_CULTURE_COLLECTION: "American Type Culture Collection",
    CodingSystem.CPT_4: "CPT-4",
    CodingSystem.CPT_5: "CPT-5",
    CodingSystem.CHEMICAL_ABSTRACT_CODES: "Chemical abstract codes",
    CodingSystem.CDT_2_CODES: "CDT-2 Codes",
    CodingSystem.CDC_ANALYTE_CODES: "CDC Analyte Codes",
    CodingSystem.CDC_METHODS_OR_INSTRUMENTS_CODES: "CDC Methods/Instruments Codes",
    CodingSystem.CDC_SURVEILLANCE: "CDC Surveillance",
    CodingSystem.CEN_ECG_DIAGNOSTIC_CODES: "CEN ECG diagnostic codes",
    CodingSystem.CLIP: "CLIP",
    CodingSystem.CPT_MODIFIER_CODE: "CPT Modifier Code",
    CodingSystem.COSTART: "COSTART",
    CodingSystem.CDC_VACCINE_CODES: "CDC Vaccine Codes",
    CodingSystem.DICOM_CONTROLLED_TERMINOLOGY: "DICOM Controlled Terminology",
    CodingSystem.EUCLIDES: "EUCLIDES",
    CodingSystem.EUCLIDES_QUANTITY_CODES: "Euclides quantity codes",
    CodingSystem.EUCLIDES_LAB_METHOD_CODES: "Euclides Lab method codes",
    CodingSystem.EUCLIDES_LAB_EQUIPMENT_CODES: "Euclides Lab equipment codes",
    CodingSystem.ENZYME_CODES: "Enzyme Codes",
    CodingSystem.FIRST_DATABANK_DRUG_CODES: "First DataBank Drug Codes",
    CodingSystem.FIRST_DATABANK_DIAGNOSTIC_CODES: "First DataBank Diagnostic Codes",
    CodingSystem.FDA_K10: "FDA K10",
    CodingSystem.HIBCC: "HIBCC",
    CodingSystem.CMS: "CMS (formerly HCFA) Common Procedure Coding System",
    CodingSystem.HEALTH_CARE_PROVIDER_TAXONOMY: "Health Care Provider Taxonomy",
    CodingSystem.HOME_HEALTH_CARE: "Home Health Care",
    CodingSystem.HEALTH_OUTCOMES: "Health Outcomes",
    CodingSystem.HL7_DEFINED_CODES_WHERE_NNNN_IS_THE_HL7_TABLE_NUMBER: "HL7 Defined Codes where nnnn is the HL7 table number",
    CodingSystem.JAPANESE_NATIONWIDE_MEDICINE_CODE: "Japanese Nationwide Medicine Code",
    CodingSystem.HPC: "CMS (formerly HCFA )Procedure Codes (HCPCS)",
    CodingSystem.ICD_10: "ICD-10",
    CodingSystem.ICD_10_PROCEDURE_CODES: "ICD-10 Procedure Codes",
    CodingSystem.ICD9: "ICD9",
    CodingSystem.ICD_9CM: "ICD-9CM",
    CodingSystem.ISBT: "ISBT",
    CodingSystem.ISBT_128_CODES_WHERE_NNNN_SPECIFIES_A_SPECIFIC_TABLE_WITHIN_ISBT_128: "ISBT 128 codes where nnnn specifies a specific table within ISBT 128.",
    CodingSystem.ICHPPC_2: "ICHPPC-2",
    CodingSystem.ICD_10_AUSTRALIAN_MODIFICATION: "ICD-10 Australian modification",
    CodingSystem.ICD_10_CANADA: "ICD-10 Canada",
    CodingSystem.INTERNATIONAL_CLASSIFICATION_OF_DISEASES_FOR_ONCOLOGY: "International Classification of Diseases for Oncology",
    CodingSystem.ICCS: "ICCS",
    CodingSystem.INTERNATIONAL_CLASSIFICATION_OF_SLEEP_DISORDERS: "International Classification of Sleep Disorders",
    CodingSystem.ISO_2955_83: "ISO 2955.83 (units of measure) with HL7 extensions",
    CodingSystem.ISO_DEFINED_CODES_WHERE_NNNN_IS_THE_ISO_TABLE_NUMBER: "ISO Defined Codes where nnnn is the ISO table number",
    CodingSystem.IUPAC_OR_IFCC_COMPONENT_CODES: "IUPAC/IFCC Component Codes",
    CodingSystem.IUPAC_OR_IFCC_PROPERTY_CODES: "IUPAC/IFCC Property Codes",
    CodingSystem.JLAC_OR_JSLM_NATIONWIDE_LABORATORY_CODE: "JLAC/JSLM, nationwide laboratory code",
    CodingSystem.JAPANESE_CHEMISTRY: "Japanese Chemistry",
    CodingSystem.JAPANESE_IMAGE_EXAMINATION_CACHE: "Japanese Image Examination Cache",
    CodingSystem.LOCAL_BILLING_CODE: "Local billing code",
    CodingSystem.LOGICAL_OBSERVATION_IDENTIFIER_NAMES_AND_CODES: "Logical Observation Identifier Names and Codes (LOINC)",
    CodingSystem.MEDICAID: "Medicaid",
    CodingSystem.MEDICARE: "Medicare",
    CodingSystem.MEDISPAN_DIAGNOSTIC_CODES: "Medispan Diagnostic Codes",
    CodingSystem.MEDICAL_ECONOMICS_DRUG_CODES: "Medical Economics Drug Codes",
    CodingSystem.MEDICAL_DICTIONARY_FOR_DRUG_REGULATORY_AFFAIRS: "Medical Dictionary for Drug Regulatory Affairs (MEDDRA)",
    CodingSystem.MEDICAL_ECONOMICS_DIAGNOSTIC_CODES: "Medical Economics Diagnostic Codes",
    CodingSystem.MEDISPAN_GPI: "Medispan GPI",
    CodingSystem.CDC_VACCINE_MANUFACTURER_CODES: "CDC Vaccine Manufacturer Codes",
    CodingSystem.NANDA: "NANDA",
    CodingSystem.NATIONAL_DRUG_CODES: "National drug codes",
    CodingSystem.NURSING_INTERVENTIONS_CLASSIFICATION: "Nursing Interventions Classification",
    CodingSystem.NATIONAL_PROVIDER_IDENTIFIER: "National Provider Identifier",
    CodingSystem.NATIONAL_UNIFORM_BILLING_COMMITTEE_CODE: "National Uniform Billing Committee Code",
    CodingSystem.OMAHA_SYSTEM: "Omaha System",
    CodingSystem.OMAHA: "Omaha",
    CodingSystem.POS_CODES: "POS Codes",
    CodingSystem.READ_CLASSIFICATION: "Read Classification",
    CodingSystem.SNOMED_DICOM_MICROGLOSSARY: "SNOMED- DICOM Microglossary",
    CodingSystem.SYSTEMIZED_NOMENCLATURE_OF_MEDICINE: "Systemized Nomenclature of Medicine (SNOMED)",
    CodingSystem.SNOMED_INTERNATIONAL: "SNOMED International",
    CodingSystem.SNOMED_TOPOLOGY_CODES: "SNOMED topology codes (anatomic sites)",
    CodingSystem.UCDS: "UCDS",
    CodingSystem.MDNS: "MDNS",
    CodingSystem.UNIFIED_MEDICAL_LANGUAGE: "Unified Medical Language",
    CodingSystem.UNIVERSAL_PRODUCT_CODE: "Universal Product Code",
    CodingSystem.UPIN: "UPIN",
    CodingSystem.UNITED_STATES_POSTAL_SERVICE: "United States Postal Service",
    CodingSystem.WHO_RECORD_POUND_DRUG_CODES: "WHO record # drug codes (6 digit)",
    CodingSystem.W2: "WHO record # drug codes (8 digit)",
    CodingSystem.WHO_RECORD_POUND_CODE_WITH_ASTM_EXTENSION: "WHO record # code with ASTM extension",
    CodingSystem.WHO_ATC: "WHO ATC",
}
