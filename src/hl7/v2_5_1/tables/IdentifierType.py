from ...base import HL7Table

"""
HL7 Version: 2.5.1
Identifier type - 0203
Table Type: HL7
"""


class IdentifierType(HL7Table):
    """
    Identifier type - 0203 // HL7 table type
    - AMERICAN_EXPRESS
    - ACCOUNT_NUMBER
    - ACCOUNT_NUMBER_CREDITOR
    - ACCOUNT_NUMBER_DEBITOR
    - ANONYMOUS_IDENTIFIER
    - TEMPORARY_ACCOUNT_NUMBER
    - ADVANCED_PRACTICE_REGISTERED_NURSE_NUMBER
    - BANK_ACCOUNT_NUMBER
    - BANK_CARD_NUMBER
    - BIRTH_REGISTRY_NUMBER
    - BREED_REGISTRY_NUMBER
    - COST_CENTER_NUMBER
    - COUNTY_NUMBER
    - DENTIST_LICENSE_NUMBER
    - DRUG_ENFORCEMENT_ADMINISTRATION_REGISTRATION_NUMBER
    - DRUG_FURNISHING_OR_PRESCRIPTIVE_AUTHORITY_NUMBER
    - DINERS_CLUB_CARD
    - DRIVERS_LICENSE_NUMBER
    - DOCTOR_NUMBER
    - OSTEOPATHIC_LICENSE_NUMBER
    - PODIATRIST_LICENSE_NUMBER
    - DONOR_REGISTRATION_NUMBER
    - DISCOVER_CARD
    - EMPLOYEE_NUMBER
    - EMPLOYER_NUMBER
    - FACILITY_ID
    - GUARANTOR_INTERNAL_IDENTIFIER
    - GENERAL_LEDGER_NUMBER
    - GUARANTOR_EXTERNAL_IDENTIFIER
    - HEALTH_CARD_NUMBER
    - INDIGENOUS_OR_ABORIGINAL
    - JURISDICTIONAL_HEALTH_NUMBER
    - LABOR_AND_INDUSTRIES_NUMBER
    - LICENSE_NUMBER
    - LOCAL_REGISTRY_ID
    - PATIENT_MEDICAID_NUMBER
    - MEMBER_NUMBER
    - PATIENTS_MEDICARE_NUMBER
    - PRACTITIONER_MEDICAID_NUMBER
    - MICROCHIP_NUMBER
    - PRACTITIONER_MEDICARE_NUMBER
    - MEDICAL_LICENSE_NUMBER
    - MILITARY_ID_NUMBER
    - MEDICAL_RECORD_NUMBER
    - TEMPORARY_MEDICAL_RECORD_NUMBER
    - MASTERCARD
    - NATIONAL_EMPLOYER_IDENTIFIER
    - NATIONAL_HEALTH_PLAN_IDENTIFIER
    - NATIONAL_UNIQUE_INDIVIDUAL_IDENTIFIER
    - NATIONAL_INSURANCE_ORGANIZATION_IDENTIFIER
    - NATIONAL_INSURANCE_PAYOR_IDENTIFIER
    - NATIONAL_PERSON_IDENTIFIER_WHERE_THE_XXX_IS_THE_ISO_TABLE_3166_3_CHARACTER
    - NURSE_PRACTITIONER_NUMBER
    - NATIONAL_PROVIDER_IDENTIFIER
    - OPTOMETRIST_LICENSE_NUMBER
    - PHYSICIAN_ASSISTANT_NUMBER
    - PENITENTIARY_OR_CORRECTIONAL_INSTITUTION_NUMBER
    - LIVING_SUBJECT_ENTERPRISE_NUMBER
    - PENSION_NUMBER
    - PATIENT_INTERNAL_IDENTIFIER
    - PERSON_NUMBER
    - TEMPORARY_LIVING_SUBJECT_NUMBER
    - PASSPORT_NUMBER
    - PERMANENT_RESIDENT_CARD_NUMBER
    - PROVIDER_NUMBER
    - PATIENT_EXTERNAL_IDENTIFIER
    - QA_NUMBER
    - RESOURCE_IDENTIFIER
    - REGISTERED_NURSE_NUMBER
    - PHARMACIST_LICENSE_NUMBER
    - RAILROAD_RETIREMENT_NUMBER
    - REGIONAL_REGISTRY_ID
    - STATE_LICENSE
    - SUBSCRIBER_NUMBER
    - STATE_REGISTRY_ID
    - SOCIAL_SECURITY_NUMBER
    - TAX_ID_NUMBER
    - TREATY_NUMBER_OR
    - UNSPECIFIED_IDENTIFIER
    - MEDICARE_OR_CMS
    - VISIT_NUMBER
    - VISA
    - WIC_IDENTIFIER
    - WORKERS_COMP_NUMBER
    - ORGANIZATION_IDENTIFIER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0203
    """

    AMERICAN_EXPRESS = "AM"  # Deprecated and replaced by BC in v 2.5.
    """American Express"""
    ACCOUNT_NUMBER = "AN"  # An identifier that is unique to an account.
    """Account number"""
    ACCOUNT_NUMBER_CREDITOR = "ANC"  # Class: Financial A more precise definition of an account number: sometimes two distinct account numbers must be transmitted in the same message, one as the creditor, the other as the debitor. Kreditorenkontonummer
    """Account number Creditor"""
    ACCOUNT_NUMBER_DEBITOR = "AND"  # Class: Financial A more precise definition of an account number: sometimes two distinct account numbers must be transmitted in the same message, one as the creditor, the other as the debitor. Debitorenkontonummer
    """Account number debitor"""
    ANONYMOUS_IDENTIFIER = "ANON"  # An identifier for a living subject whose real identity is protected or suppressed Justification: For public health reporting purposes, anonymous identifiers are occasionally used for protecting patient identity in reporting certain results. For instance, a state health department may choose to use a scheme for generating an anonymous identifier for reporting a patient that has had a positive human immunodeficiency virus antibody test. Anonymous identifiers can be used in PID 3 by replacing the medical record number or other non-anonymous identifier. The assigning authority for an anonymous identifier would be the state/local health department.
    """Anonymous identifier"""
    TEMPORARY_ACCOUNT_NUMBER = "ANT"  # Class: FinancialTemporary version of an Account Number. Use Case: An ancillary system that does not normally assign account numbers is the first time to register a patient. This ancillary system will generate a temporary account number that will only be used until an official account number is assigned.
    """Temporary Account Number"""
    ADVANCED_PRACTICE_REGISTERED_NURSE_NUMBER = "APRN"  # An identifier that is unique to an advanced practice registered nurse within the jurisdiction of a certifying board
    """Advanced Practice Registered Nurse number"""
    BANK_ACCOUNT_NUMBER = "BA"  # Class: Financial
    """Bank Account Number"""
    BANK_CARD_NUMBER = "BC"  # Class: Financial An identifier that is unique to a person’s bank card. Replaces AM, DI, DS, MS, and VS beginning in v 2.5.
    """Bank Card Number"""
    BIRTH_REGISTRY_NUMBER = "BR"
    """Birth registry number"""
    BREED_REGISTRY_NUMBER = "BRN"
    """Breed Registry Number"""
    COST_CENTER_NUMBER = "CC"  # Class: Financial Use Case: needed especially for transmitting information about invoices.
    """Cost Center number"""
    COUNTY_NUMBER = "CY"
    """County number"""
    DENTIST_LICENSE_NUMBER = "DDS"  # An identifier that is unique to a dentist within the jurisdiction of the licensing board
    """Dentist license number"""
    DRUG_ENFORCEMENT_ADMINISTRATION_REGISTRATION_NUMBER = "DEA"  # An identifier for an individual or organization relative to controlled substance regulation and transactions. Use case: This is a registration number that identifies an individual or organization relative to controlled substance regulation and transactions. A DEA number has a very precise and widely accepted meaning within the United States. Surprisingly, the US Drug Enforcement Administration does not solely assign DEA numbers in the United States. Hospitals have the authority to issue DEA numbers to their medical residents. These DEA numbers are based upon the hospital’s DEA number, but the authority rests with the hospital on the assignment to the residents. Thus, DEA as an Identifier Type is necessary in addition to DEA as an Assigning Authority.
    """Drug Enforcement Administration registration number"""
    DRUG_FURNISHING_OR_PRESCRIPTIVE_AUTHORITY_NUMBER = "DFN"  # An identifier issued to a health care provider authorizing the person to write drug orders Use Case: A nurse practitioner has authorization to furnish or prescribe pharmaceutical substances; this identifier is in component 1.
    """Drug Furnishing or prescriptive authority Number"""
    DINERS_CLUB_CARD = "DI"  # Deprecated and replaced by BC in v 2.5.
    """Diners Club card"""
    DRIVERS_LICENSE_NUMBER = "DL"
    """Drivers license number"""
    DOCTOR_NUMBER = "DN"
    """Doctor number"""
    OSTEOPATHIC_LICENSE_NUMBER = "DO"  # An identifier that is unique to an osteopath within the jurisdiction of a licensing board.
    """Osteopathic License number"""
    PODIATRIST_LICENSE_NUMBER = "DPM"  # An identifier that is unique to a podiatrist within the jurisdiction of the licensing board.
    """Podiatrist license number"""
    DONOR_REGISTRATION_NUMBER = "DR"
    """Donor Registration Number"""
    DISCOVER_CARD = "DS"  # Deprecated and replaced by BC in v 2.5.
    """Discover Card"""
    EMPLOYEE_NUMBER = (
        "EI"  # A number that uniquely identifies an employee to an employer.
    )
    """Employee number"""
    EMPLOYER_NUMBER = "EN"
    """Employer number"""
    FACILITY_ID = "FI"
    """Facility ID"""
    GUARANTOR_INTERNAL_IDENTIFIER = "GI"  # Class: Financial
    """Guarantor internal identifier"""
    GENERAL_LEDGER_NUMBER = "GL"  # Class: Financial
    """General ledger number"""
    GUARANTOR_EXTERNAL_IDENTIFIER = "GN"  # Class: Financial
    """Guarantor external identifier"""
    HEALTH_CARD_NUMBER = "HC"
    """Health Card Number"""
    INDIGENOUS_OR_ABORIGINAL = "IND"  # A number assigned to a member of an indigenous or aboriginal group outside of Canada.
    """Indigenous/Aboriginal"""
    JURISDICTIONAL_HEALTH_NUMBER = "JHN"  # Class: Insurance 2 uses: a) UK jurisdictional CHI number; b) Canadian provincial health card number:
    """Jurisdictional health number (Canada)"""
    LABOR_AND_INDUSTRIES_NUMBER = "LI"
    """Labor and industries number"""
    LICENSE_NUMBER = "LN"
    """License number"""
    LOCAL_REGISTRY_ID = "LR"
    """Local Registry ID"""
    PATIENT_MEDICAID_NUMBER = "MA"  # Class: Insurance
    """Patient Medicaid number"""
    MEMBER_NUMBER = "MB"  # An identifier for the insured of an insurance policy (this insured always has a subscriber), usually assigned by the insurance carrier. Use Case: Person is covered by an insurance policy. This person may or may not be the subscriber of the policy.
    """Member Number"""
    PATIENTS_MEDICARE_NUMBER = "MC"  # Class: Insurance
    """Patients Medicare number"""
    PRACTITIONER_MEDICAID_NUMBER = "MCD"  # Class: Insurance
    """Practitioner Medicaid number"""
    MICROCHIP_NUMBER = "MCN"
    """Microchip Number"""
    PRACTITIONER_MEDICARE_NUMBER = "MCR"  # Class: Insurance
    """Practitioner Medicare number"""
    MEDICAL_LICENSE_NUMBER = "MD"  # An identifier that is unique to a medical doctor within the jurisdiction of a licensing board. Use Case: These license numbers are sometimes used as identifiers. In some states, the same authority issues all three identifiers, e.g., medical, osteopathic, and physician assistant licenses all issued by one state medical board. For this case, the CX data type requires distinct identifier types to accurately interpret component 1. Additionally, the distinction among these license types is critical in most health care settings (this is not to convey full licensing information, which requires a segment to support all related attributes).
    """Medical License number"""
    MILITARY_ID_NUMBER = "MI"  # A number assigned to an individual who has had military duty, but is not currently on active duty. The number is assigned by the DOD or Veterans’ Affairs (VA).
    """Military ID number"""
    MEDICAL_RECORD_NUMBER = "MR"  # An identifier that is unique to a patient within a set of medical records, not necessarily unique within an application.
    """Medical record number"""
    TEMPORARY_MEDICAL_RECORD_NUMBER = "MRT"  # Temporary version of a Medical Record Number Use Case: An ancillary system that does not normally assign medical record numbers is the first time to register a patient. This ancillary system will generate a temporary medical record number that will only be used until an official medical record number is assigned.
    """Temporary Medical Record Number"""
    MASTERCARD = "MS"  # Deprecated and replaced by BC in v 2.5.
    """MasterCard"""
    NATIONAL_EMPLOYER_IDENTIFIER = "NE"  # In the US, the Assigning Authority for this value is typically CMS, but it may be used by all providers and insurance companies in HIPAA related transactions.
    """National employer identifier"""
    NATIONAL_HEALTH_PLAN_IDENTIFIER = "NH"  # Class: InsuranceUsed for the UK NHS national identifier. In the US, the Assigning Authority for this value is typically CMS, but it may be used by all providers and insurance companies in HIPAA related transactions.
    """National Health Plan Identifier"""
    NATIONAL_UNIQUE_INDIVIDUAL_IDENTIFIER = "NI"  # Class: Insurance In the US, the Assigning Authority for this value is typically CMS, but it may be used by all providers and insurance companies in HIPAA related transactions.
    """National unique individual identifier"""
    NATIONAL_INSURANCE_ORGANIZATION_IDENTIFIER = "NII"  # Class: Insurance In Germany a national identifier for an insurance company. It is printed on the insurance card (health card). It is not to be confused with the health card number itself. Krankenkassen-ID der KV-Karte
    """National Insurance Organization Identifier"""
    NATIONAL_INSURANCE_PAYOR_IDENTIFIER = "NIIP"  # Class: Insurance In Germany the insurance identifier addressed as the payor. Krankenkassen-ID des Rechnungsempfängers Use case: a subdivision issues the card with their identifier, but the main division is going to pay the invoices.
    """National Insurance Payor Identifier (Payor)"""
    NATIONAL_PERSON_IDENTIFIER_WHERE_THE_XXX_IS_THE_ISO_TABLE_3166_3_CHARACTER = "NNxxx"
    """National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code"""
    NURSE_PRACTITIONER_NUMBER = "NP"  # An identifier that is unique to a nurse practitioner within the jurisdiction of a certifying board.
    """Nurse practitioner number"""
    NATIONAL_PROVIDER_IDENTIFIER = "NPI"  # Class: Insurance In the US, the Assigning Authority for this value is typically CMS, but it may be used by all providers and insurance companies in HIPAA related transactions.
    """National provider identifier"""
    OPTOMETRIST_LICENSE_NUMBER = "OD"  # A number that is unique to an individual optometrist within the jurisdiction of the licensing board.
    """Optometrist license number"""
    PHYSICIAN_ASSISTANT_NUMBER = "PA"  # An identifier that is unique to a physician assistant within the jurisdiction of a licensing board
    """Physician Assistant number"""
    PENITENTIARY_OR_CORRECTIONAL_INSTITUTION_NUMBER = (
        "PCN"  # A number assigned to individual who is incarcerated.
    )
    """Penitentiary/correctional institution Number"""
    LIVING_SUBJECT_ENTERPRISE_NUMBER = "PE"  # An identifier that is unique to a living subject within an enterprise (as identified by the Assigning Authority).
    """Living Subject Enterprise Number"""
    PENSION_NUMBER = "PEN"
    """Pension Number"""
    PATIENT_INTERNAL_IDENTIFIER = (
        "PI"  # A number that is unique to a patient within an Assigning Authority.
    )
    """Patient internal identifier"""
    PERSON_NUMBER = "PN"  # A number that is unique to a living subject within an Assigning Authority.
    """Person number"""
    TEMPORARY_LIVING_SUBJECT_NUMBER = (
        "PNT"  # Temporary version of a Lining Subject Number.
    )
    """Temporary Living Subject Number"""
    PASSPORT_NUMBER = "PPN"  # A unique number assigned to the document affirming that a person is a citizen of the country. In the US this number is issued only by the State Department.
    """Passport number"""
    PERMANENT_RESIDENT_CARD_NUMBER = "PRC"
    """Permanent Resident Card Number"""
    PROVIDER_NUMBER = "PRN"  # A number that is unique to an individual provider, a provider group or an organization within an Assigning Authority. Use case: This allows PRN to represent either an individual (a nurse) or a group/organization (orthopedic surgery team).
    """Provider number"""
    PATIENT_EXTERNAL_IDENTIFIER = "PT"
    """Patient external identifier"""
    QA_NUMBER = "QA"
    """QA number"""
    RESOURCE_IDENTIFIER = "RI"  # A generalized resource identifier. Use Case: An identifier type is needed to accommodate what are commonly known as resources. The resources can include human (e.g. a respiratory therapist), non-human (e.g., a companion animal), inanimate object (e.g., an exam room), organization (e.g., diabetic education class) or any other physical or logical entity.
    """Resource identifier"""
    REGISTERED_NURSE_NUMBER = "RN"  # An identifier that is unique to a registered nurse within the jurisdiction of the licensing board.
    """Registered Nurse Number"""
    PHARMACIST_LICENSE_NUMBER = "RPH"  # An identifier that is unique to a pharmacist within the jurisdiction of the licensing board.
    """Pharmacist license number"""
    RAILROAD_RETIREMENT_NUMBER = "RR"
    """Railroad Retirement number"""
    REGIONAL_REGISTRY_ID = "RRI"
    """Regional registry ID"""
    STATE_LICENSE = "SL"
    """State license"""
    SUBSCRIBER_NUMBER = "SN"  # Class: Insurance An identifier for a subscriber of an insurance policy which is unique for, and usually assigned by, the insurance carrier. Use Case: A person is the subscriber of an insurance policy. The person’s family may be plan members, but are not the subscriber.
    """Subscriber Number"""
    STATE_REGISTRY_ID = "SR"
    """State registry ID"""
    SOCIAL_SECURITY_NUMBER = "SS"
    """Social Security number"""
    TAX_ID_NUMBER = "TAX"
    """Tax ID number"""
    TREATY_NUMBER_OR = "TN"  # A number assigned to a member of an indigenous group in Canada. Use Case: First Nation.
    """Treaty Number/ (Canada)"""
    UNSPECIFIED_IDENTIFIER = "U"
    """Unspecified identifier"""
    MEDICARE_OR_CMS = "UPIN"  # Class: Insurance
    """Medicare/CMS (formerly HCFA)s Universal Physician Identification numbers"""
    VISIT_NUMBER = "VN"
    """Visit number"""
    VISA = "VS"  # Deprecated and replaced by BC in v 2.5.
    """VISA"""
    WIC_IDENTIFIER = "WC"
    """WIC identifier"""
    WORKERS_COMP_NUMBER = "WCN"
    """Workers Comp Number"""
    ORGANIZATION_IDENTIFIER = "XX"
    """Organization identifier"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    IdentifierType.AMERICAN_EXPRESS: "American Express",
    IdentifierType.ACCOUNT_NUMBER: "Account number",
    IdentifierType.ACCOUNT_NUMBER_CREDITOR: "Account number Creditor",
    IdentifierType.ACCOUNT_NUMBER_DEBITOR: "Account number debitor",
    IdentifierType.ANONYMOUS_IDENTIFIER: "Anonymous identifier",
    IdentifierType.TEMPORARY_ACCOUNT_NUMBER: "Temporary Account Number",
    IdentifierType.ADVANCED_PRACTICE_REGISTERED_NURSE_NUMBER: "Advanced Practice Registered Nurse number",
    IdentifierType.BANK_ACCOUNT_NUMBER: "Bank Account Number",
    IdentifierType.BANK_CARD_NUMBER: "Bank Card Number",
    IdentifierType.BIRTH_REGISTRY_NUMBER: "Birth registry number",
    IdentifierType.BREED_REGISTRY_NUMBER: "Breed Registry Number",
    IdentifierType.COST_CENTER_NUMBER: "Cost Center number",
    IdentifierType.COUNTY_NUMBER: "County number",
    IdentifierType.DENTIST_LICENSE_NUMBER: "Dentist license number",
    IdentifierType.DRUG_ENFORCEMENT_ADMINISTRATION_REGISTRATION_NUMBER: "Drug Enforcement Administration registration number",
    IdentifierType.DRUG_FURNISHING_OR_PRESCRIPTIVE_AUTHORITY_NUMBER: "Drug Furnishing or prescriptive authority Number",
    IdentifierType.DINERS_CLUB_CARD: "Diners Club card",
    IdentifierType.DRIVERS_LICENSE_NUMBER: "Drivers license number",
    IdentifierType.DOCTOR_NUMBER: "Doctor number",
    IdentifierType.OSTEOPATHIC_LICENSE_NUMBER: "Osteopathic License number",
    IdentifierType.PODIATRIST_LICENSE_NUMBER: "Podiatrist license number",
    IdentifierType.DONOR_REGISTRATION_NUMBER: "Donor Registration Number",
    IdentifierType.DISCOVER_CARD: "Discover Card",
    IdentifierType.EMPLOYEE_NUMBER: "Employee number",
    IdentifierType.EMPLOYER_NUMBER: "Employer number",
    IdentifierType.FACILITY_ID: "Facility ID",
    IdentifierType.GUARANTOR_INTERNAL_IDENTIFIER: "Guarantor internal identifier",
    IdentifierType.GENERAL_LEDGER_NUMBER: "General ledger number",
    IdentifierType.GUARANTOR_EXTERNAL_IDENTIFIER: "Guarantor external identifier",
    IdentifierType.HEALTH_CARD_NUMBER: "Health Card Number",
    IdentifierType.INDIGENOUS_OR_ABORIGINAL: "Indigenous/Aboriginal",
    IdentifierType.JURISDICTIONAL_HEALTH_NUMBER: "Jurisdictional health number (Canada)",
    IdentifierType.LABOR_AND_INDUSTRIES_NUMBER: "Labor and industries number",
    IdentifierType.LICENSE_NUMBER: "License number",
    IdentifierType.LOCAL_REGISTRY_ID: "Local Registry ID",
    IdentifierType.PATIENT_MEDICAID_NUMBER: "Patient Medicaid number",
    IdentifierType.MEMBER_NUMBER: "Member Number",
    IdentifierType.PATIENTS_MEDICARE_NUMBER: "Patients Medicare number",
    IdentifierType.PRACTITIONER_MEDICAID_NUMBER: "Practitioner Medicaid number",
    IdentifierType.MICROCHIP_NUMBER: "Microchip Number",
    IdentifierType.PRACTITIONER_MEDICARE_NUMBER: "Practitioner Medicare number",
    IdentifierType.MEDICAL_LICENSE_NUMBER: "Medical License number",
    IdentifierType.MILITARY_ID_NUMBER: "Military ID number",
    IdentifierType.MEDICAL_RECORD_NUMBER: "Medical record number",
    IdentifierType.TEMPORARY_MEDICAL_RECORD_NUMBER: "Temporary Medical Record Number",
    IdentifierType.MASTERCARD: "MasterCard",
    IdentifierType.NATIONAL_EMPLOYER_IDENTIFIER: "National employer identifier",
    IdentifierType.NATIONAL_HEALTH_PLAN_IDENTIFIER: "National Health Plan Identifier",
    IdentifierType.NATIONAL_UNIQUE_INDIVIDUAL_IDENTIFIER: "National unique individual identifier",
    IdentifierType.NATIONAL_INSURANCE_ORGANIZATION_IDENTIFIER: "National Insurance Organization Identifier",
    IdentifierType.NATIONAL_INSURANCE_PAYOR_IDENTIFIER: "National Insurance Payor Identifier (Payor)",
    IdentifierType.NATIONAL_PERSON_IDENTIFIER_WHERE_THE_XXX_IS_THE_ISO_TABLE_3166_3_CHARACTER: "National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code",
    IdentifierType.NURSE_PRACTITIONER_NUMBER: "Nurse practitioner number",
    IdentifierType.NATIONAL_PROVIDER_IDENTIFIER: "National provider identifier",
    IdentifierType.OPTOMETRIST_LICENSE_NUMBER: "Optometrist license number",
    IdentifierType.PHYSICIAN_ASSISTANT_NUMBER: "Physician Assistant number",
    IdentifierType.PENITENTIARY_OR_CORRECTIONAL_INSTITUTION_NUMBER: "Penitentiary/correctional institution Number",
    IdentifierType.LIVING_SUBJECT_ENTERPRISE_NUMBER: "Living Subject Enterprise Number",
    IdentifierType.PENSION_NUMBER: "Pension Number",
    IdentifierType.PATIENT_INTERNAL_IDENTIFIER: "Patient internal identifier",
    IdentifierType.PERSON_NUMBER: "Person number",
    IdentifierType.TEMPORARY_LIVING_SUBJECT_NUMBER: "Temporary Living Subject Number",
    IdentifierType.PASSPORT_NUMBER: "Passport number",
    IdentifierType.PERMANENT_RESIDENT_CARD_NUMBER: "Permanent Resident Card Number",
    IdentifierType.PROVIDER_NUMBER: "Provider number",
    IdentifierType.PATIENT_EXTERNAL_IDENTIFIER: "Patient external identifier",
    IdentifierType.QA_NUMBER: "QA number",
    IdentifierType.RESOURCE_IDENTIFIER: "Resource identifier",
    IdentifierType.REGISTERED_NURSE_NUMBER: "Registered Nurse Number",
    IdentifierType.PHARMACIST_LICENSE_NUMBER: "Pharmacist license number",
    IdentifierType.RAILROAD_RETIREMENT_NUMBER: "Railroad Retirement number",
    IdentifierType.REGIONAL_REGISTRY_ID: "Regional registry ID",
    IdentifierType.STATE_LICENSE: "State license",
    IdentifierType.SUBSCRIBER_NUMBER: "Subscriber Number",
    IdentifierType.STATE_REGISTRY_ID: "State registry ID",
    IdentifierType.SOCIAL_SECURITY_NUMBER: "Social Security number",
    IdentifierType.TAX_ID_NUMBER: "Tax ID number",
    IdentifierType.TREATY_NUMBER_OR: "Treaty Number/ (Canada)",
    IdentifierType.UNSPECIFIED_IDENTIFIER: "Unspecified identifier",
    IdentifierType.MEDICARE_OR_CMS: "Medicare/CMS (formerly HCFA)s Universal Physician Identification numbers",
    IdentifierType.VISIT_NUMBER: "Visit number",
    IdentifierType.VISA: "VISA",
    IdentifierType.WIC_IDENTIFIER: "WIC identifier",
    IdentifierType.WORKERS_COMP_NUMBER: "Workers Comp Number",
    IdentifierType.ORGANIZATION_IDENTIFIER: "Organization identifier",
}
