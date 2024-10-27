from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.JCC import JCC
from ..data_types.PTA import PTA
from ..data_types.XTN import XTN
from ..data_types.ST import ST
from ..data_types.CX import CX
from ..data_types.CE import CE
from ..data_types.XPN import XPN
from ..data_types.RMC import RMC
from ..data_types.DT import DT
from ..data_types.IS import IS
from ..data_types.XCN import XCN
from ..data_types.DDI import DDI
from ..data_types.XON import XON
from ..tables.EthnicGroup import EthnicGroup
from ..tables.MaritalStatus import MaritalStatus
from ..tables.PatientSRelationshipToInsured import PatientSRelationshipToInsured
from ..tables.JobStatus import JobStatus
from ..tables.PolicySource import PolicySource
from ..tables.LivingArrangement import LivingArrangement
from ..tables.Religion import Religion
from ..tables.InsuranceCompanyContactReason import InsuranceCompanyContactReason
from ..tables.MilitaryStatus import MilitaryStatus
from ..tables.ContactReason import ContactReason
from ..tables.AmbulatoryStatus import AmbulatoryStatus
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.MilitaryRankOrGrade import MilitaryRankOrGrade
from ..tables.EmployerInformationData import EmployerInformationData
from ..tables.MilitaryRecipient import MilitaryRecipient
from ..tables.StudentStatus import StudentStatus
from ..tables.NonCoveredInsuranceCode import NonCoveredInsuranceCode
from ..tables.Citizenship import Citizenship
from ..tables.PublicityCode import PublicityCode
from ..tables.MilitaryHandicappedProgramCode import MilitaryHandicappedProgramCode
from ..tables.MilitaryService import MilitaryService
from ..tables.EligibilitySource import EligibilitySource
from ..tables.PrimaryLanguage import PrimaryLanguage
from ..tables.Race import Race
from ..tables.MailClaimParty import MailClaimParty
from ..tables.PolicyScope import PolicyScope
from ..tables.Nationality import Nationality
from ..tables.Relationship import Relationship
from ..tables.LivingDependency import LivingDependency


"""
Insurance Additional Information - IN2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::IN2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    IN2,
    ID, JCC, PTA, XTN, ST, CX, CE, XPN, RMC, DT, IS, XCN, DDI, XON
)

in2 = IN2(  #  - The IN2 segment contains additional insurance policy coverage and benefit information necessary for proper billing and reimbursement
    insureds_employee_id=None,  # CX(...) 
    insureds_social_security_number=None,  # ST(...) 
    insureds_employers_name_and_id=None,  # XCN(...) 
    employer_information_data=None,  # IS(...) 
    mail_claim_party=None,  # IS(...) 
    medicare_health_ins_card_number=None,  # ST(...) 
    medicaid_case_name=None,  # XPN(...) 
    medicaid_case_number=None,  # ST(...) 
    military_sponsor_name=None,  # XPN(...) 
    military_id_number=None,  # ST(...) 
    dependent_of_military_recipient=None,  # CE(...) 
    military_organization=None,  # ST(...) 
    military_station=None,  # ST(...) 
    military_service=None,  # IS(...) 
    military_rank_or_grade=None,  # IS(...) 
    military_status=None,  # IS(...) 
    military_retire_date=None,  # DT(...) 
    military_non_avail_cert_on_file=None,  # ID(...) 
    baby_coverage=None,  # ID(...) 
    combine_baby_bill=None,  # ID(...) 
    blood_deductible=None,  # ST(...) 
    special_coverage_approval_name=None,  # XPN(...) 
    special_coverage_approval_title=None,  # ST(...) 
    non_covered_insurance_code=None,  # IS(...) 
    payor_id=None,  # CX(...) 
    payor_subscriber_id=None,  # CX(...) 
    eligibility_source=None,  # IS(...) 
    room_coverage_type_or_amount=None,  # RMC(...) 
    policy_type_or_amount=None,  # PTA(...) 
    daily_deductible=None,  # DDI(...) 
    living_dependency=None,  # IS(...) 
    ambulatory_status=None,  # IS(...) 
    citizenship=None,  # CE(...) 
    primary_language=None,  # CE(...) 
    living_arrangement=None,  # IS(...) 
    publicity_code=None,  # CE(...) 
    protection_indicator=None,  # ID(...) 
    student_indicator=None,  # IS(...) 
    religion=None,  # CE(...) 
    mothers_maiden_name=None,  # XPN(...) 
    nationality=None,  # CE(...) 
    ethnic_group=None,  # CE(...) 
    marital_status=None,  # CE(...) 
    insureds_employment_start_date=None,  # DT(...) 
    employment_stop_date=None,  # DT(...) 
    job_title=None,  # ST(...) 
    job_code_or_class=None,  # JCC(...) 
    job_status=None,  # IS(...) 
    employer_contact_person_name=None,  # XPN(...) 
    employer_contact_person_phone_number=None,  # XTN(...) 
    employer_contact_reason=None,  # IS(...) 
    insureds_contact_persons_name=None,  # XPN(...) 
    insureds_contact_person_phone_number=None,  # XTN(...) 
    insureds_contact_person_reason=None,  # IS(...) 
    relationship_to_the_patient_start_date=None,  # DT(...) 
    relationship_to_the_patient_stop_date=None,  # DT(...) 
    insurance_co_contact_reason=None,  # IS(...) 
    insurance_co_contact_phone_number=None,  # XTN(...) 
    policy_scope=None,  # IS(...) 
    policy_source=None,  # IS(...) 
    patient_member_number=None,  # CX(...) 
    guarantors_relationship_to_insured=None,  # CE(...) 
    insureds_phone_number_home=None,  # XTN(...) 
    insureds_employer_phone_number=None,  # XTN(...) 
    military_handicapped_program=None,  # CE(...) 
    suspend_flag=None,  # ID(...) 
    copay_limit_flag=None,  # ID(...) 
    stoploss_limit_flag=None,  # ID(...) 
    insured_organization_name_and_id=None,  # XON(...) 
    insured_employer_organization_name_and_id=None,  # XON(...) 
    race=None,  # CE(...) 
    cms_patients_relationship_to_insured=None,  # CE(...) 
)

-----END SEGMENT::IN2 TEMPLATE-----
"""


class IN2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """IN2"""
    _hl7_name = """Insurance Additional Information"""
    _hl7_description = """The IN2 segment contains additional insurance policy coverage and benefit information necessary for proper billing and reimbursement"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2"
    _c_length = (250, 11, 250, 1, 1, 15, 250, 15, 250, 20, 250, 25, 25, 14, 2, 3, 8, 1, 1, 1, 1, 250, 30, 8, 250, 250, 1, 82, 56, 25, 2, 2, 250, 250, 2, 250, 1, 2, 250, 250, 250, 250, 250, 8, 8, 20, 20, 2, 250, 250, 2, 250, 250, 2, 8, 8, 2, 250, 2, 2, 250, 250, 250, 250, 250, 1, 1, 1, 250, 250, 250, 250,)
    _c_rpt = (65535, 1, 65535, 1, 65535, 1, 65535, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 1, 65535, 65535, 1, 1, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 1, 65535, 65535, 1, 1, 1, 1, 1, 65535, 65535, 1, 65535, 65535, 65535, 1, 65535, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 65535, 65535, 65535, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CX, ST, XCN, IS, IS, ST, XPN, ST, XPN, ST, CE, ST, ST, IS, IS, IS, DT, ID, ID, ID, ST, XPN, ST, IS, CX, CX, IS, RMC, PTA, DDI, IS, IS, CE, CE, IS, CE, ID, IS, CE, XPN, CE, CE, CE, DT, DT, ST, JCC, IS, XPN, XTN, IS, XPN, XTN, IS, DT, DT, IS, XTN, IS, IS, CX, CE, XTN, XTN, CE, ID, ID, ID, XON, XON, CE, CE,)
    _c_aliases = ("IN2.1", "IN2.2", "IN2.3", "IN2.4", "IN2.5", "IN2.6", "IN2.7", "IN2.8", "IN2.9", "IN2.10", "IN2.11", "IN2.12", "IN2.13", "IN2.14", "IN2.15", "IN2.16", "IN2.17", "IN2.18", "IN2.19", "IN2.20", "IN2.21", "IN2.22", "IN2.23", "IN2.24", "IN2.25", "IN2.26", "IN2.27", "IN2.28", "IN2.29", "IN2.30", "IN2.31", "IN2.32", "IN2.33", "IN2.34", "IN2.35", "IN2.36", "IN2.37", "IN2.38", "IN2.39", "IN2.40", "IN2.41", "IN2.42", "IN2.43", "IN2.44", "IN2.45", "IN2.46", "IN2.47", "IN2.48", "IN2.49", "IN2.50", "IN2.51", "IN2.52", "IN2.53", "IN2.54", "IN2.55", "IN2.56", "IN2.57", "IN2.58", "IN2.59", "IN2.60", "IN2.61", "IN2.62", "IN2.63", "IN2.64", "IN2.65", "IN2.66", "IN2.67", "IN2.68", "IN2.69", "IN2.70", "IN2.71", "IN2.72",)
    _c_names = ("Insured's Employee ID", "Insured's Social Security Number", "Insured's Employer's Name and ID", "Employer Information Data", "Mail Claim Party", "Medicare Health Ins Card Number", "Medicaid Case Name", "Medicaid Case Number", "Military Sponsor Name", "Military ID Number", "Dependent Of Military Recipient", "Military Organization", "Military Station", "Military Service", "Military Rank/Grade", "Military Status", "Military Retire Date", "Military Non-Avail Cert On File", "Baby Coverage", "Combine Baby Bill", "Blood Deductible", "Special Coverage Approval Name", "Special Coverage Approval Title", "Non-Covered Insurance Code", "Payor ID", "Payor Subscriber ID", "Eligibility Source", "Room Coverage Type/Amount", "Policy Type/Amount", "Daily Deductible", "Living Dependency", "Ambulatory Status", "Citizenship", "Primary Language", "Living Arrangement", "Publicity Code", "Protection Indicator", "Student Indicator", "Religion", "Mother's Maiden Name", "Nationality", "Ethnic Group", "Marital Status", "Insured's Employment Start Date", "Employment Stop Date", "Job Title", "Job Code/Class", "Job Status", "Employer Contact Person Name", "Employer Contact Person Phone Number", "Employer Contact Reason", "Insured's Contact Person's Name", "Insured's Contact Person Phone Number", "Insured's Contact Person Reason", "Relationship to the Patient Start Date", "Relationship to the Patient Stop Date", "Insurance Co. Contact Reason", "Insurance Co Contact Phone Number", "Policy Scope", "Policy Source", "Patient Member Number", "Guarantor's Relationship To Insured", "Insured's Phone Number - Home", "Insured's Employer Phone Number", "Military Handicapped Program", "Suspend Flag", "Copay Limit Flag", "Stoploss Limit Flag", "Insured Organization Name and ID", "Insured Employer Organization Name and ID", "Race", "CMS Patient's Relationship to Insured",)
    _c_attrs = ("insureds_employee_id", "insureds_social_security_number", "insureds_employers_name_and_id", "employer_information_data", "mail_claim_party", "medicare_health_ins_card_number", "medicaid_case_name", "medicaid_case_number", "military_sponsor_name", "military_id_number", "dependent_of_military_recipient", "military_organization", "military_station", "military_service", "military_rank_or_grade", "military_status", "military_retire_date", "military_non_avail_cert_on_file", "baby_coverage", "combine_baby_bill", "blood_deductible", "special_coverage_approval_name", "special_coverage_approval_title", "non_covered_insurance_code", "payor_id", "payor_subscriber_id", "eligibility_source", "room_coverage_type_or_amount", "policy_type_or_amount", "daily_deductible", "living_dependency", "ambulatory_status", "citizenship", "primary_language", "living_arrangement", "publicity_code", "protection_indicator", "student_indicator", "religion", "mothers_maiden_name", "nationality", "ethnic_group", "marital_status", "insureds_employment_start_date", "employment_stop_date", "job_title", "job_code_or_class", "job_status", "employer_contact_person_name", "employer_contact_person_phone_number", "employer_contact_reason", "insureds_contact_persons_name", "insureds_contact_person_phone_number", "insureds_contact_person_reason", "relationship_to_the_patient_start_date", "relationship_to_the_patient_stop_date", "insurance_co_contact_reason", "insurance_co_contact_phone_number", "policy_scope", "policy_source", "patient_member_number", "guarantors_relationship_to_insured", "insureds_phone_number_home", "insureds_employer_phone_number", "military_handicapped_program", "suspend_flag", "copay_limit_flag", "stoploss_limit_flag", "insured_organization_name_and_id", "insured_employer_organization_name_and_id", "race", "cms_patients_relationship_to_insured",)
    # fmt: on

    def __init__(
        self,
        insureds_employee_id: CX | None = None,  # IN2.1
        insureds_social_security_number: ST | None = None,  # IN2.2
        insureds_employers_name_and_id: XCN | None = None,  # IN2.3
        employer_information_data: EmployerInformationData | IS | None = None,  # IN2.4
        mail_claim_party: MailClaimParty | IS | None = None,  # IN2.5
        medicare_health_ins_card_number: ST | None = None,  # IN2.6
        medicaid_case_name: XPN | None = None,  # IN2.7
        medicaid_case_number: ST | None = None,  # IN2.8
        military_sponsor_name: XPN | None = None,  # IN2.9
        military_id_number: ST | None = None,  # IN2.10
        dependent_of_military_recipient: MilitaryRecipient | CE | None = None,  # IN2.11
        military_organization: ST | None = None,  # IN2.12
        military_station: ST | None = None,  # IN2.13
        military_service: MilitaryService | IS | None = None,  # IN2.14
        military_rank_or_grade: MilitaryRankOrGrade | IS | None = None,  # IN2.15
        military_status: MilitaryStatus | IS | None = None,  # IN2.16
        military_retire_date: DT | None = None,  # IN2.17
        military_non_avail_cert_on_file: YesOrNoIndicator | ID | None = None,  # IN2.18
        baby_coverage: YesOrNoIndicator | ID | None = None,  # IN2.19
        combine_baby_bill: YesOrNoIndicator | ID | None = None,  # IN2.20
        blood_deductible: ST | None = None,  # IN2.21
        special_coverage_approval_name: XPN | None = None,  # IN2.22
        special_coverage_approval_title: ST | None = None,  # IN2.23
        non_covered_insurance_code: NonCoveredInsuranceCode
        | IS
        | None = None,  # IN2.24
        payor_id: CX | None = None,  # IN2.25
        payor_subscriber_id: CX | None = None,  # IN2.26
        eligibility_source: EligibilitySource | IS | None = None,  # IN2.27
        room_coverage_type_or_amount: RMC | None = None,  # IN2.28
        policy_type_or_amount: PTA | None = None,  # IN2.29
        daily_deductible: DDI | None = None,  # IN2.30
        living_dependency: LivingDependency | IS | None = None,  # IN2.31
        ambulatory_status: AmbulatoryStatus | IS | None = None,  # IN2.32
        citizenship: Citizenship | CE | None = None,  # IN2.33
        primary_language: PrimaryLanguage | CE | None = None,  # IN2.34
        living_arrangement: LivingArrangement | IS | None = None,  # IN2.35
        publicity_code: PublicityCode | CE | None = None,  # IN2.36
        protection_indicator: YesOrNoIndicator | ID | None = None,  # IN2.37
        student_indicator: StudentStatus | IS | None = None,  # IN2.38
        religion: Religion | CE | None = None,  # IN2.39
        mothers_maiden_name: XPN | None = None,  # IN2.40
        nationality: Nationality | CE | None = None,  # IN2.41
        ethnic_group: EthnicGroup | CE | None = None,  # IN2.42
        marital_status: MaritalStatus | CE | None = None,  # IN2.43
        insureds_employment_start_date: DT | None = None,  # IN2.44
        employment_stop_date: DT | None = None,  # IN2.45
        job_title: ST | None = None,  # IN2.46
        job_code_or_class: JCC | None = None,  # IN2.47
        job_status: JobStatus | IS | None = None,  # IN2.48
        employer_contact_person_name: XPN | None = None,  # IN2.49
        employer_contact_person_phone_number: XTN | None = None,  # IN2.50
        employer_contact_reason: ContactReason | IS | None = None,  # IN2.51
        insureds_contact_persons_name: XPN | None = None,  # IN2.52
        insureds_contact_person_phone_number: XTN | None = None,  # IN2.53
        insureds_contact_person_reason: ContactReason | IS | None = None,  # IN2.54
        relationship_to_the_patient_start_date: DT | None = None,  # IN2.55
        relationship_to_the_patient_stop_date: DT | None = None,  # IN2.56
        insurance_co_contact_reason: InsuranceCompanyContactReason
        | IS
        | None = None,  # IN2.57
        insurance_co_contact_phone_number: XTN | None = None,  # IN2.58
        policy_scope: PolicyScope | IS | None = None,  # IN2.59
        policy_source: PolicySource | IS | None = None,  # IN2.60
        patient_member_number: CX | None = None,  # IN2.61
        guarantors_relationship_to_insured: Relationship | CE | None = None,  # IN2.62
        insureds_phone_number_home: XTN | None = None,  # IN2.63
        insureds_employer_phone_number: XTN | None = None,  # IN2.64
        military_handicapped_program: MilitaryHandicappedProgramCode
        | CE
        | None = None,  # IN2.65
        suspend_flag: YesOrNoIndicator | ID | None = None,  # IN2.66
        copay_limit_flag: YesOrNoIndicator | ID | None = None,  # IN2.67
        stoploss_limit_flag: YesOrNoIndicator | ID | None = None,  # IN2.68
        insured_organization_name_and_id: XON | None = None,  # IN2.69
        insured_employer_organization_name_and_id: XON | None = None,  # IN2.70
        race: Race | CE | None = None,  # IN2.71
        cms_patients_relationship_to_insured: PatientSRelationshipToInsured
        | CE
        | None = None,  # IN2.72
    ):
        """
        Insurance Additional Information - `IN2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN2>`_
        The IN2 segment contains additional insurance policy coverage and benefit information necessary for proper billing and reimbursement. Fields used by this segment are defined by CMS or other regulatory agencies.

        :param insureds_employee_id: Extended Composite ID with Check Digit (id: IN2.1 | len: 250 | use: O | rpt: *)
        :param insureds_social_security_number: String Data (id: IN2.2 | len: 11 | use: O | rpt: 1)
        :param insureds_employers_name_and_id: Extended Composite ID Number and Name for Persons (id: IN2.3 | len: 250 | use: O | rpt: *)
        :param employer_information_data: Coded value for user-defined tables (id: IN2.4 | len: 1 | use: O | rpt: 1)
        :param mail_claim_party: Coded value for user-defined tables (id: IN2.5 | len: 1 | use: O | rpt: *)
        :param medicare_health_ins_card_number: String Data (id: IN2.6 | len: 15 | use: O | rpt: 1)
        :param medicaid_case_name: Extended Person Name (id: IN2.7 | len: 250 | use: O | rpt: *)
        :param medicaid_case_number: String Data (id: IN2.8 | len: 15 | use: O | rpt: 1)
        :param military_sponsor_name: Extended Person Name (id: IN2.9 | len: 250 | use: O | rpt: *)
        :param military_id_number: String Data (id: IN2.10 | len: 20 | use: O | rpt: 1)
        :param dependent_of_military_recipient: Coded Element (id: IN2.11 | len: 250 | use: O | rpt: 1)
        :param military_organization: String Data (id: IN2.12 | len: 25 | use: O | rpt: 1)
        :param military_station: String Data (id: IN2.13 | len: 25 | use: O | rpt: 1)
        :param military_service: Coded value for user-defined tables (id: IN2.14 | len: 14 | use: O | rpt: 1)
        :param military_rank_or_grade: Coded value for user-defined tables (id: IN2.15 | len: 2 | use: O | rpt: 1)
        :param military_status: Coded value for user-defined tables (id: IN2.16 | len: 3 | use: O | rpt: 1)
        :param military_retire_date: Date (id: IN2.17 | len: 8 | use: O | rpt: 1)
        :param military_non_avail_cert_on_file: Coded values for HL7 tables (id: IN2.18 | len: 1 | use: O | rpt: 1)
        :param baby_coverage: Coded values for HL7 tables (id: IN2.19 | len: 1 | use: O | rpt: 1)
        :param combine_baby_bill: Coded values for HL7 tables (id: IN2.20 | len: 1 | use: O | rpt: 1)
        :param blood_deductible: String Data (id: IN2.21 | len: 1 | use: O | rpt: 1)
        :param special_coverage_approval_name: Extended Person Name (id: IN2.22 | len: 250 | use: O | rpt: *)
        :param special_coverage_approval_title: String Data (id: IN2.23 | len: 30 | use: O | rpt: 1)
        :param non_covered_insurance_code: Coded value for user-defined tables (id: IN2.24 | len: 8 | use: O | rpt: *)
        :param payor_id: Extended Composite ID with Check Digit (id: IN2.25 | len: 250 | use: O | rpt: *)
        :param payor_subscriber_id: Extended Composite ID with Check Digit (id: IN2.26 | len: 250 | use: O | rpt: *)
        :param eligibility_source: Coded value for user-defined tables (id: IN2.27 | len: 1 | use: O | rpt: 1)
        :param room_coverage_type_or_amount: Room Coverage (id: IN2.28 | len: 82 | use: O | rpt: *)
        :param policy_type_or_amount: Policy Type and Amount (id: IN2.29 | len: 56 | use: O | rpt: *)
        :param daily_deductible: Daily Deductible Information (id: IN2.30 | len: 25 | use: O | rpt: 1)
        :param living_dependency: Coded value for user-defined tables (id: IN2.31 | len: 2 | use: O | rpt: 1)
        :param ambulatory_status: Coded value for user-defined tables (id: IN2.32 | len: 2 | use: O | rpt: *)
        :param citizenship: Coded Element (id: IN2.33 | len: 250 | use: O | rpt: *)
        :param primary_language: Coded Element (id: IN2.34 | len: 250 | use: O | rpt: 1)
        :param living_arrangement: Coded value for user-defined tables (id: IN2.35 | len: 2 | use: O | rpt: 1)
        :param publicity_code: Coded Element (id: IN2.36 | len: 250 | use: O | rpt: 1)
        :param protection_indicator: Coded values for HL7 tables (id: IN2.37 | len: 1 | use: O | rpt: 1)
        :param student_indicator: Coded value for user-defined tables (id: IN2.38 | len: 2 | use: O | rpt: 1)
        :param religion: Coded Element (id: IN2.39 | len: 250 | use: O | rpt: 1)
        :param mothers_maiden_name: Extended Person Name (id: IN2.40 | len: 250 | use: O | rpt: *)
        :param nationality: Coded Element (id: IN2.41 | len: 250 | use: O | rpt: 1)
        :param ethnic_group: Coded Element (id: IN2.42 | len: 250 | use: O | rpt: *)
        :param marital_status: Coded Element (id: IN2.43 | len: 250 | use: O | rpt: *)
        :param insureds_employment_start_date: Date (id: IN2.44 | len: 8 | use: O | rpt: 1)
        :param employment_stop_date: Date (id: IN2.45 | len: 8 | use: O | rpt: 1)
        :param job_title: String Data (id: IN2.46 | len: 20 | use: O | rpt: 1)
        :param job_code_or_class: Job Code/Class (id: IN2.47 | len: 20 | use: O | rpt: 1)
        :param job_status: Coded value for user-defined tables (id: IN2.48 | len: 2 | use: O | rpt: 1)
        :param employer_contact_person_name: Extended Person Name (id: IN2.49 | len: 250 | use: O | rpt: *)
        :param employer_contact_person_phone_number: Extended Telecommunication Number (id: IN2.50 | len: 250 | use: O | rpt: *)
        :param employer_contact_reason: Coded value for user-defined tables (id: IN2.51 | len: 2 | use: O | rpt: 1)
        :param insureds_contact_persons_name: Extended Person Name (id: IN2.52 | len: 250 | use: O | rpt: *)
        :param insureds_contact_person_phone_number: Extended Telecommunication Number (id: IN2.53 | len: 250 | use: O | rpt: *)
        :param insureds_contact_person_reason: Coded value for user-defined tables (id: IN2.54 | len: 2 | use: O | rpt: *)
        :param relationship_to_the_patient_start_date: Date (id: IN2.55 | len: 8 | use: O | rpt: 1)
        :param relationship_to_the_patient_stop_date: Date (id: IN2.56 | len: 8 | use: O | rpt: *)
        :param insurance_co_contact_reason: Coded value for user-defined tables (id: IN2.57 | len: 2 | use: O | rpt: 1)
        :param insurance_co_contact_phone_number: Extended Telecommunication Number (id: IN2.58 | len: 250 | use: O | rpt: 1)
        :param policy_scope: Coded value for user-defined tables (id: IN2.59 | len: 2 | use: O | rpt: 1)
        :param policy_source: Coded value for user-defined tables (id: IN2.60 | len: 2 | use: O | rpt: 1)
        :param patient_member_number: Extended Composite ID with Check Digit (id: IN2.61 | len: 250 | use: O | rpt: 1)
        :param guarantors_relationship_to_insured: Coded Element (id: IN2.62 | len: 250 | use: O | rpt: 1)
        :param insureds_phone_number_home: Extended Telecommunication Number (id: IN2.63 | len: 250 | use: O | rpt: *)
        :param insureds_employer_phone_number: Extended Telecommunication Number (id: IN2.64 | len: 250 | use: O | rpt: *)
        :param military_handicapped_program: Coded Element (id: IN2.65 | len: 250 | use: O | rpt: 1)
        :param suspend_flag: Coded values for HL7 tables (id: IN2.66 | len: 1 | use: O | rpt: 1)
        :param copay_limit_flag: Coded values for HL7 tables (id: IN2.67 | len: 1 | use: O | rpt: 1)
        :param stoploss_limit_flag: Coded values for HL7 tables (id: IN2.68 | len: 1 | use: O | rpt: 1)
        :param insured_organization_name_and_id: Extended Composite Name and Identification Number for Organizations (id: IN2.69 | len: 250 | use: O | rpt: *)
        :param insured_employer_organization_name_and_id: Extended Composite Name and Identification Number for Organizations (id: IN2.70 | len: 250 | use: O | rpt: *)
        :param race: Coded Element (id: IN2.71 | len: 250 | use: O | rpt: *)
        :param cms_patients_relationship_to_insured: Coded Element (id: IN2.72 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 72
        self.insureds_employee_id = insureds_employee_id
        self.insureds_social_security_number = insureds_social_security_number
        self.insureds_employers_name_and_id = insureds_employers_name_and_id
        self.employer_information_data = employer_information_data
        self.mail_claim_party = mail_claim_party
        self.medicare_health_ins_card_number = medicare_health_ins_card_number
        self.medicaid_case_name = medicaid_case_name
        self.medicaid_case_number = medicaid_case_number
        self.military_sponsor_name = military_sponsor_name
        self.military_id_number = military_id_number
        self.dependent_of_military_recipient = dependent_of_military_recipient
        self.military_organization = military_organization
        self.military_station = military_station
        self.military_service = military_service
        self.military_rank_or_grade = military_rank_or_grade
        self.military_status = military_status
        self.military_retire_date = military_retire_date
        self.military_non_avail_cert_on_file = military_non_avail_cert_on_file
        self.baby_coverage = baby_coverage
        self.combine_baby_bill = combine_baby_bill
        self.blood_deductible = blood_deductible
        self.special_coverage_approval_name = special_coverage_approval_name
        self.special_coverage_approval_title = special_coverage_approval_title
        self.non_covered_insurance_code = non_covered_insurance_code
        self.payor_id = payor_id
        self.payor_subscriber_id = payor_subscriber_id
        self.eligibility_source = eligibility_source
        self.room_coverage_type_or_amount = room_coverage_type_or_amount
        self.policy_type_or_amount = policy_type_or_amount
        self.daily_deductible = daily_deductible
        self.living_dependency = living_dependency
        self.ambulatory_status = ambulatory_status
        self.citizenship = citizenship
        self.primary_language = primary_language
        self.living_arrangement = living_arrangement
        self.publicity_code = publicity_code
        self.protection_indicator = protection_indicator
        self.student_indicator = student_indicator
        self.religion = religion
        self.mothers_maiden_name = mothers_maiden_name
        self.nationality = nationality
        self.ethnic_group = ethnic_group
        self.marital_status = marital_status
        self.insureds_employment_start_date = insureds_employment_start_date
        self.employment_stop_date = employment_stop_date
        self.job_title = job_title
        self.job_code_or_class = job_code_or_class
        self.job_status = job_status
        self.employer_contact_person_name = employer_contact_person_name
        self.employer_contact_person_phone_number = employer_contact_person_phone_number
        self.employer_contact_reason = employer_contact_reason
        self.insureds_contact_persons_name = insureds_contact_persons_name
        self.insureds_contact_person_phone_number = insureds_contact_person_phone_number
        self.insureds_contact_person_reason = insureds_contact_person_reason
        self.relationship_to_the_patient_start_date = (
            relationship_to_the_patient_start_date
        )
        self.relationship_to_the_patient_stop_date = (
            relationship_to_the_patient_stop_date
        )
        self.insurance_co_contact_reason = insurance_co_contact_reason
        self.insurance_co_contact_phone_number = insurance_co_contact_phone_number
        self.policy_scope = policy_scope
        self.policy_source = policy_source
        self.patient_member_number = patient_member_number
        self.guarantors_relationship_to_insured = guarantors_relationship_to_insured
        self.insureds_phone_number_home = insureds_phone_number_home
        self.insureds_employer_phone_number = insureds_employer_phone_number
        self.military_handicapped_program = military_handicapped_program
        self.suspend_flag = suspend_flag
        self.copay_limit_flag = copay_limit_flag
        self.stoploss_limit_flag = stoploss_limit_flag
        self.insured_organization_name_and_id = insured_organization_name_and_id
        self.insured_employer_organization_name_and_id = (
            insured_employer_organization_name_and_id
        )
        self.race = race
        self.cms_patients_relationship_to_insured = cms_patients_relationship_to_insured

    @property
    def insureds_employee_id(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: IN2.1 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.1
        """
        return self._c_data[0]

    @insureds_employee_id.setter  # set IN2.1
    def insureds_employee_id(self, cx: CX | tuple[CX] | None):
        """
        id: IN2.1 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.1
        """
        if isinstance(cx, tuple):
            self._c_data[0] = cx
        else:
            self._c_data[0] = (cx,)

    @property  # get IN2.2
    def insureds_social_security_number(self) -> ST | None:
        """
        id: IN2.2 | len: 11 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.2
        """
        return self._c_data[1][0]

    @insureds_social_security_number.setter  # set IN2.2
    def insureds_social_security_number(self, st: ST | None):
        """
        id: IN2.2 | len: 11 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.2
        """
        self._c_data[1] = (st,)

    @property
    def insureds_employers_name_and_id(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: IN2.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.3
        """
        return self._c_data[2]

    @insureds_employers_name_and_id.setter  # set IN2.3
    def insureds_employers_name_and_id(self, xcn: XCN | tuple[XCN] | None):
        """
        id: IN2.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.3
        """
        if isinstance(xcn, tuple):
            self._c_data[2] = xcn
        else:
            self._c_data[2] = (xcn,)

    @property  # get IN2.4
    def employer_information_data(self) -> EmployerInformationData | None:
        """
        id: IN2.4 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.4
        """
        return self._c_data[3][0]

    @employer_information_data.setter  # set IN2.4
    def employer_information_data(
        self, employer_information_data: EmployerInformationData | None
    ):
        """
        id: IN2.4 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.4
        """
        self._c_data[3] = (employer_information_data,)

    @property
    def mail_claim_party(self) -> tuple[MailClaimParty, ...] | tuple[None]:
        """
        id: IN2.5 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.5
        """
        return self._c_data[4]

    @mail_claim_party.setter  # set IN2.5
    def mail_claim_party(
        self, mail_claim_party: MailClaimParty | tuple[MailClaimParty] | None
    ):
        """
        id: IN2.5 | len: 1 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.5
        """
        if isinstance(mail_claim_party, tuple):
            self._c_data[4] = mail_claim_party
        else:
            self._c_data[4] = (mail_claim_party,)

    @property  # get IN2.6
    def medicare_health_ins_card_number(self) -> ST | None:
        """
        id: IN2.6 | len: 15 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.6
        """
        return self._c_data[5][0]

    @medicare_health_ins_card_number.setter  # set IN2.6
    def medicare_health_ins_card_number(self, st: ST | None):
        """
        id: IN2.6 | len: 15 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.6
        """
        self._c_data[5] = (st,)

    @property
    def medicaid_case_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN2.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.7
        """
        return self._c_data[6]

    @medicaid_case_name.setter  # set IN2.7
    def medicaid_case_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN2.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.7
        """
        if isinstance(xpn, tuple):
            self._c_data[6] = xpn
        else:
            self._c_data[6] = (xpn,)

    @property  # get IN2.8
    def medicaid_case_number(self) -> ST | None:
        """
        id: IN2.8 | len: 15 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.8
        """
        return self._c_data[7][0]

    @medicaid_case_number.setter  # set IN2.8
    def medicaid_case_number(self, st: ST | None):
        """
        id: IN2.8 | len: 15 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.8
        """
        self._c_data[7] = (st,)

    @property
    def military_sponsor_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN2.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.9
        """
        return self._c_data[8]

    @military_sponsor_name.setter  # set IN2.9
    def military_sponsor_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN2.9 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.9
        """
        if isinstance(xpn, tuple):
            self._c_data[8] = xpn
        else:
            self._c_data[8] = (xpn,)

    @property  # get IN2.10
    def military_id_number(self) -> ST | None:
        """
        id: IN2.10 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.10
        """
        return self._c_data[9][0]

    @military_id_number.setter  # set IN2.10
    def military_id_number(self, st: ST | None):
        """
        id: IN2.10 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.10
        """
        self._c_data[9] = (st,)

    @property  # get IN2.11
    def dependent_of_military_recipient(self) -> MilitaryRecipient | None:
        """
        id: IN2.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.11
        """
        return self._c_data[10][0]

    @dependent_of_military_recipient.setter  # set IN2.11
    def dependent_of_military_recipient(
        self, military_recipient: MilitaryRecipient | None
    ):
        """
        id: IN2.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.11
        """
        self._c_data[10] = (military_recipient,)

    @property  # get IN2.12
    def military_organization(self) -> ST | None:
        """
        id: IN2.12 | len: 25 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.12
        """
        return self._c_data[11][0]

    @military_organization.setter  # set IN2.12
    def military_organization(self, st: ST | None):
        """
        id: IN2.12 | len: 25 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.12
        """
        self._c_data[11] = (st,)

    @property  # get IN2.13
    def military_station(self) -> ST | None:
        """
        id: IN2.13 | len: 25 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.13
        """
        return self._c_data[12][0]

    @military_station.setter  # set IN2.13
    def military_station(self, st: ST | None):
        """
        id: IN2.13 | len: 25 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.13
        """
        self._c_data[12] = (st,)

    @property  # get IN2.14
    def military_service(self) -> MilitaryService | None:
        """
        id: IN2.14 | len: 14 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.14
        """
        return self._c_data[13][0]

    @military_service.setter  # set IN2.14
    def military_service(self, military_service: MilitaryService | None):
        """
        id: IN2.14 | len: 14 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.14
        """
        self._c_data[13] = (military_service,)

    @property  # get IN2.15
    def military_rank_or_grade(self) -> MilitaryRankOrGrade | None:
        """
        id: IN2.15 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.15
        """
        return self._c_data[14][0]

    @military_rank_or_grade.setter  # set IN2.15
    def military_rank_or_grade(
        self, military_rank_or_grade: MilitaryRankOrGrade | None
    ):
        """
        id: IN2.15 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.15
        """
        self._c_data[14] = (military_rank_or_grade,)

    @property  # get IN2.16
    def military_status(self) -> MilitaryStatus | None:
        """
        id: IN2.16 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.16
        """
        return self._c_data[15][0]

    @military_status.setter  # set IN2.16
    def military_status(self, military_status: MilitaryStatus | None):
        """
        id: IN2.16 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.16
        """
        self._c_data[15] = (military_status,)

    @property  # get IN2.17
    def military_retire_date(self) -> DT | None:
        """
        id: IN2.17 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.17
        """
        return self._c_data[16][0]

    @military_retire_date.setter  # set IN2.17
    def military_retire_date(self, dt: DT | None):
        """
        id: IN2.17 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.17
        """
        self._c_data[16] = (dt,)

    @property  # get IN2.18
    def military_non_avail_cert_on_file(self) -> YesOrNoIndicator | None:
        """
        id: IN2.18 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.18
        """
        return self._c_data[17][0]

    @military_non_avail_cert_on_file.setter  # set IN2.18
    def military_non_avail_cert_on_file(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: IN2.18 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.18
        """
        self._c_data[17] = (yes_or_no_indicator,)

    @property  # get IN2.19
    def baby_coverage(self) -> YesOrNoIndicator | None:
        """
        id: IN2.19 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.19
        """
        return self._c_data[18][0]

    @baby_coverage.setter  # set IN2.19
    def baby_coverage(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN2.19 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.19
        """
        self._c_data[18] = (yes_or_no_indicator,)

    @property  # get IN2.20
    def combine_baby_bill(self) -> YesOrNoIndicator | None:
        """
        id: IN2.20 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.20
        """
        return self._c_data[19][0]

    @combine_baby_bill.setter  # set IN2.20
    def combine_baby_bill(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN2.20 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.20
        """
        self._c_data[19] = (yes_or_no_indicator,)

    @property  # get IN2.21
    def blood_deductible(self) -> ST | None:
        """
        id: IN2.21 | len: 1 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.21
        """
        return self._c_data[20][0]

    @blood_deductible.setter  # set IN2.21
    def blood_deductible(self, st: ST | None):
        """
        id: IN2.21 | len: 1 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.21
        """
        self._c_data[20] = (st,)

    @property
    def special_coverage_approval_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN2.22 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.22
        """
        return self._c_data[21]

    @special_coverage_approval_name.setter  # set IN2.22
    def special_coverage_approval_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN2.22 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.22
        """
        if isinstance(xpn, tuple):
            self._c_data[21] = xpn
        else:
            self._c_data[21] = (xpn,)

    @property  # get IN2.23
    def special_coverage_approval_title(self) -> ST | None:
        """
        id: IN2.23 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.23
        """
        return self._c_data[22][0]

    @special_coverage_approval_title.setter  # set IN2.23
    def special_coverage_approval_title(self, st: ST | None):
        """
        id: IN2.23 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.23
        """
        self._c_data[22] = (st,)

    @property
    def non_covered_insurance_code(
        self,
    ) -> tuple[NonCoveredInsuranceCode, ...] | tuple[None]:
        """
        id: IN2.24 | len: 8 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.24
        """
        return self._c_data[23]

    @non_covered_insurance_code.setter  # set IN2.24
    def non_covered_insurance_code(
        self,
        noncovered_insurance_code: NonCoveredInsuranceCode
        | tuple[NonCoveredInsuranceCode]
        | None,
    ):
        """
        id: IN2.24 | len: 8 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.24
        """
        if isinstance(noncovered_insurance_code, tuple):
            self._c_data[23] = noncovered_insurance_code
        else:
            self._c_data[23] = (noncovered_insurance_code,)

    @property
    def payor_id(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: IN2.25 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.25
        """
        return self._c_data[24]

    @payor_id.setter  # set IN2.25
    def payor_id(self, cx: CX | tuple[CX] | None):
        """
        id: IN2.25 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.25
        """
        if isinstance(cx, tuple):
            self._c_data[24] = cx
        else:
            self._c_data[24] = (cx,)

    @property
    def payor_subscriber_id(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: IN2.26 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.26
        """
        return self._c_data[25]

    @payor_subscriber_id.setter  # set IN2.26
    def payor_subscriber_id(self, cx: CX | tuple[CX] | None):
        """
        id: IN2.26 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.26
        """
        if isinstance(cx, tuple):
            self._c_data[25] = cx
        else:
            self._c_data[25] = (cx,)

    @property  # get IN2.27
    def eligibility_source(self) -> EligibilitySource | None:
        """
        id: IN2.27 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.27
        """
        return self._c_data[26][0]

    @eligibility_source.setter  # set IN2.27
    def eligibility_source(self, eligibility_source: EligibilitySource | None):
        """
        id: IN2.27 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.27
        """
        self._c_data[26] = (eligibility_source,)

    @property
    def room_coverage_type_or_amount(self) -> tuple[RMC, ...] | tuple[None]:
        """
        id: IN2.28 | len: 82 | use: O | rpt: *
        ---
        return_type: tuple[RMC, ...]: (Room Coverage, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.28
        """
        return self._c_data[27]

    @room_coverage_type_or_amount.setter  # set IN2.28
    def room_coverage_type_or_amount(self, rmc: RMC | tuple[RMC] | None):
        """
        id: IN2.28 | len: 82 | use: O | rpt: *
        ---
        param_type: RMC | tuple[RMC, ...]: (Room Coverage, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.28
        """
        if isinstance(rmc, tuple):
            self._c_data[27] = rmc
        else:
            self._c_data[27] = (rmc,)

    @property
    def policy_type_or_amount(self) -> tuple[PTA, ...] | tuple[None]:
        """
        id: IN2.29 | len: 56 | use: O | rpt: *
        ---
        return_type: tuple[PTA, ...]: (Policy Type and Amount, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.29
        """
        return self._c_data[28]

    @policy_type_or_amount.setter  # set IN2.29
    def policy_type_or_amount(self, pta: PTA | tuple[PTA] | None):
        """
        id: IN2.29 | len: 56 | use: O | rpt: *
        ---
        param_type: PTA | tuple[PTA, ...]: (Policy Type and Amount, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.29
        """
        if isinstance(pta, tuple):
            self._c_data[28] = pta
        else:
            self._c_data[28] = (pta,)

    @property  # get IN2.30
    def daily_deductible(self) -> DDI | None:
        """
        id: IN2.30 | len: 25 | use: O | rpt: 1
        ---
        return_type: DDI: Daily Deductible Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.30
        """
        return self._c_data[29][0]

    @daily_deductible.setter  # set IN2.30
    def daily_deductible(self, ddi: DDI | None):
        """
        id: IN2.30 | len: 25 | use: O | rpt: 1
        ---
        param_type: DDI: Daily Deductible Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.30
        """
        self._c_data[29] = (ddi,)

    @property  # get IN2.31
    def living_dependency(self) -> LivingDependency | None:
        """
        id: IN2.31 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.31
        """
        return self._c_data[30][0]

    @living_dependency.setter  # set IN2.31
    def living_dependency(self, living_dependency: LivingDependency | None):
        """
        id: IN2.31 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.31
        """
        self._c_data[30] = (living_dependency,)

    @property
    def ambulatory_status(self) -> tuple[AmbulatoryStatus, ...] | tuple[None]:
        """
        id: IN2.32 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.32
        """
        return self._c_data[31]

    @ambulatory_status.setter  # set IN2.32
    def ambulatory_status(
        self, ambulatory_status: AmbulatoryStatus | tuple[AmbulatoryStatus] | None
    ):
        """
        id: IN2.32 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.32
        """
        if isinstance(ambulatory_status, tuple):
            self._c_data[31] = ambulatory_status
        else:
            self._c_data[31] = (ambulatory_status,)

    @property
    def citizenship(self) -> tuple[Citizenship, ...] | tuple[None]:
        """
        id: IN2.33 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.33
        """
        return self._c_data[32]

    @citizenship.setter  # set IN2.33
    def citizenship(self, citizenship: Citizenship | tuple[Citizenship] | None):
        """
        id: IN2.33 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.33
        """
        if isinstance(citizenship, tuple):
            self._c_data[32] = citizenship
        else:
            self._c_data[32] = (citizenship,)

    @property  # get IN2.34
    def primary_language(self) -> PrimaryLanguage | None:
        """
        id: IN2.34 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.34
        """
        return self._c_data[33][0]

    @primary_language.setter  # set IN2.34
    def primary_language(self, primary_language: PrimaryLanguage | None):
        """
        id: IN2.34 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.34
        """
        self._c_data[33] = (primary_language,)

    @property  # get IN2.35
    def living_arrangement(self) -> LivingArrangement | None:
        """
        id: IN2.35 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.35
        """
        return self._c_data[34][0]

    @living_arrangement.setter  # set IN2.35
    def living_arrangement(self, living_arrangement: LivingArrangement | None):
        """
        id: IN2.35 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.35
        """
        self._c_data[34] = (living_arrangement,)

    @property  # get IN2.36
    def publicity_code(self) -> PublicityCode | None:
        """
        id: IN2.36 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.36
        """
        return self._c_data[35][0]

    @publicity_code.setter  # set IN2.36
    def publicity_code(self, publicity_code: PublicityCode | None):
        """
        id: IN2.36 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.36
        """
        self._c_data[35] = (publicity_code,)

    @property  # get IN2.37
    def protection_indicator(self) -> YesOrNoIndicator | None:
        """
        id: IN2.37 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.37
        """
        return self._c_data[36][0]

    @protection_indicator.setter  # set IN2.37
    def protection_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN2.37 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.37
        """
        self._c_data[36] = (yes_or_no_indicator,)

    @property  # get IN2.38
    def student_indicator(self) -> StudentStatus | None:
        """
        id: IN2.38 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.38
        """
        return self._c_data[37][0]

    @student_indicator.setter  # set IN2.38
    def student_indicator(self, student_status: StudentStatus | None):
        """
        id: IN2.38 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.38
        """
        self._c_data[37] = (student_status,)

    @property  # get IN2.39
    def religion(self) -> Religion | None:
        """
        id: IN2.39 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.39
        """
        return self._c_data[38][0]

    @religion.setter  # set IN2.39
    def religion(self, religion: Religion | None):
        """
        id: IN2.39 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.39
        """
        self._c_data[38] = (religion,)

    @property
    def mothers_maiden_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN2.40 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.40
        """
        return self._c_data[39]

    @mothers_maiden_name.setter  # set IN2.40
    def mothers_maiden_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN2.40 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.40
        """
        if isinstance(xpn, tuple):
            self._c_data[39] = xpn
        else:
            self._c_data[39] = (xpn,)

    @property  # get IN2.41
    def nationality(self) -> Nationality | None:
        """
        id: IN2.41 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.41
        """
        return self._c_data[40][0]

    @nationality.setter  # set IN2.41
    def nationality(self, nationality: Nationality | None):
        """
        id: IN2.41 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.41
        """
        self._c_data[40] = (nationality,)

    @property
    def ethnic_group(self) -> tuple[EthnicGroup, ...] | tuple[None]:
        """
        id: IN2.42 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.42
        """
        return self._c_data[41]

    @ethnic_group.setter  # set IN2.42
    def ethnic_group(self, ethnic_group: EthnicGroup | tuple[EthnicGroup] | None):
        """
        id: IN2.42 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.42
        """
        if isinstance(ethnic_group, tuple):
            self._c_data[41] = ethnic_group
        else:
            self._c_data[41] = (ethnic_group,)

    @property
    def marital_status(self) -> tuple[MaritalStatus, ...] | tuple[None]:
        """
        id: IN2.43 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.43
        """
        return self._c_data[42]

    @marital_status.setter  # set IN2.43
    def marital_status(
        self, marital_status: MaritalStatus | tuple[MaritalStatus] | None
    ):
        """
        id: IN2.43 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.43
        """
        if isinstance(marital_status, tuple):
            self._c_data[42] = marital_status
        else:
            self._c_data[42] = (marital_status,)

    @property  # get IN2.44
    def insureds_employment_start_date(self) -> DT | None:
        """
        id: IN2.44 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.44
        """
        return self._c_data[43][0]

    @insureds_employment_start_date.setter  # set IN2.44
    def insureds_employment_start_date(self, dt: DT | None):
        """
        id: IN2.44 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.44
        """
        self._c_data[43] = (dt,)

    @property  # get IN2.45
    def employment_stop_date(self) -> DT | None:
        """
        id: IN2.45 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.45
        """
        return self._c_data[44][0]

    @employment_stop_date.setter  # set IN2.45
    def employment_stop_date(self, dt: DT | None):
        """
        id: IN2.45 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.45
        """
        self._c_data[44] = (dt,)

    @property  # get IN2.46
    def job_title(self) -> ST | None:
        """
        id: IN2.46 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.46
        """
        return self._c_data[45][0]

    @job_title.setter  # set IN2.46
    def job_title(self, st: ST | None):
        """
        id: IN2.46 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.46
        """
        self._c_data[45] = (st,)

    @property  # get IN2.47
    def job_code_or_class(self) -> JCC | None:
        """
        id: IN2.47 | len: 20 | use: O | rpt: 1
        ---
        return_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.47
        """
        return self._c_data[46][0]

    @job_code_or_class.setter  # set IN2.47
    def job_code_or_class(self, jcc: JCC | None):
        """
        id: IN2.47 | len: 20 | use: O | rpt: 1
        ---
        param_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.47
        """
        self._c_data[46] = (jcc,)

    @property  # get IN2.48
    def job_status(self) -> JobStatus | None:
        """
        id: IN2.48 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.48
        """
        return self._c_data[47][0]

    @job_status.setter  # set IN2.48
    def job_status(self, job_status: JobStatus | None):
        """
        id: IN2.48 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.48
        """
        self._c_data[47] = (job_status,)

    @property
    def employer_contact_person_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN2.49 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.49
        """
        return self._c_data[48]

    @employer_contact_person_name.setter  # set IN2.49
    def employer_contact_person_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN2.49 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.49
        """
        if isinstance(xpn, tuple):
            self._c_data[48] = xpn
        else:
            self._c_data[48] = (xpn,)

    @property
    def employer_contact_person_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN2.50 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.50
        """
        return self._c_data[49]

    @employer_contact_person_phone_number.setter  # set IN2.50
    def employer_contact_person_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN2.50 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.50
        """
        if isinstance(xtn, tuple):
            self._c_data[49] = xtn
        else:
            self._c_data[49] = (xtn,)

    @property  # get IN2.51
    def employer_contact_reason(self) -> ContactReason | None:
        """
        id: IN2.51 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.51
        """
        return self._c_data[50][0]

    @employer_contact_reason.setter  # set IN2.51
    def employer_contact_reason(self, contact_reason: ContactReason | None):
        """
        id: IN2.51 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.51
        """
        self._c_data[50] = (contact_reason,)

    @property
    def insureds_contact_persons_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN2.52 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.52
        """
        return self._c_data[51]

    @insureds_contact_persons_name.setter  # set IN2.52
    def insureds_contact_persons_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN2.52 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.52
        """
        if isinstance(xpn, tuple):
            self._c_data[51] = xpn
        else:
            self._c_data[51] = (xpn,)

    @property
    def insureds_contact_person_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN2.53 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.53
        """
        return self._c_data[52]

    @insureds_contact_person_phone_number.setter  # set IN2.53
    def insureds_contact_person_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN2.53 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.53
        """
        if isinstance(xtn, tuple):
            self._c_data[52] = xtn
        else:
            self._c_data[52] = (xtn,)

    @property
    def insureds_contact_person_reason(self) -> tuple[ContactReason, ...] | tuple[None]:
        """
        id: IN2.54 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.54
        """
        return self._c_data[53]

    @insureds_contact_person_reason.setter  # set IN2.54
    def insureds_contact_person_reason(
        self, contact_reason: ContactReason | tuple[ContactReason] | None
    ):
        """
        id: IN2.54 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.54
        """
        if isinstance(contact_reason, tuple):
            self._c_data[53] = contact_reason
        else:
            self._c_data[53] = (contact_reason,)

    @property  # get IN2.55
    def relationship_to_the_patient_start_date(self) -> DT | None:
        """
        id: IN2.55 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.55
        """
        return self._c_data[54][0]

    @relationship_to_the_patient_start_date.setter  # set IN2.55
    def relationship_to_the_patient_start_date(self, dt: DT | None):
        """
        id: IN2.55 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.55
        """
        self._c_data[54] = (dt,)

    @property
    def relationship_to_the_patient_stop_date(self) -> tuple[DT, ...] | tuple[None]:
        """
        id: IN2.56 | len: 8 | use: O | rpt: *
        ---
        return_type: tuple[DT, ...]: (Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.56
        """
        return self._c_data[55]

    @relationship_to_the_patient_stop_date.setter  # set IN2.56
    def relationship_to_the_patient_stop_date(self, dt: DT | tuple[DT] | None):
        """
        id: IN2.56 | len: 8 | use: O | rpt: *
        ---
        param_type: DT | tuple[DT, ...]: (Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.56
        """
        if isinstance(dt, tuple):
            self._c_data[55] = dt
        else:
            self._c_data[55] = (dt,)

    @property  # get IN2.57
    def insurance_co_contact_reason(self) -> InsuranceCompanyContactReason | None:
        """
        id: IN2.57 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.57
        """
        return self._c_data[56][0]

    @insurance_co_contact_reason.setter  # set IN2.57
    def insurance_co_contact_reason(
        self, insurance_company_contact_reason: InsuranceCompanyContactReason | None
    ):
        """
        id: IN2.57 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.57
        """
        self._c_data[56] = (insurance_company_contact_reason,)

    @property  # get IN2.58
    def insurance_co_contact_phone_number(self) -> XTN | None:
        """
        id: IN2.58 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.58
        """
        return self._c_data[57][0]

    @insurance_co_contact_phone_number.setter  # set IN2.58
    def insurance_co_contact_phone_number(self, xtn: XTN | None):
        """
        id: IN2.58 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.58
        """
        self._c_data[57] = (xtn,)

    @property  # get IN2.59
    def policy_scope(self) -> PolicyScope | None:
        """
        id: IN2.59 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.59
        """
        return self._c_data[58][0]

    @policy_scope.setter  # set IN2.59
    def policy_scope(self, policy_scope: PolicyScope | None):
        """
        id: IN2.59 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.59
        """
        self._c_data[58] = (policy_scope,)

    @property  # get IN2.60
    def policy_source(self) -> PolicySource | None:
        """
        id: IN2.60 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.60
        """
        return self._c_data[59][0]

    @policy_source.setter  # set IN2.60
    def policy_source(self, policy_source: PolicySource | None):
        """
        id: IN2.60 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.60
        """
        self._c_data[59] = (policy_source,)

    @property  # get IN2.61
    def patient_member_number(self) -> CX | None:
        """
        id: IN2.61 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.61
        """
        return self._c_data[60][0]

    @patient_member_number.setter  # set IN2.61
    def patient_member_number(self, cx: CX | None):
        """
        id: IN2.61 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.61
        """
        self._c_data[60] = (cx,)

    @property  # get IN2.62
    def guarantors_relationship_to_insured(self) -> Relationship | None:
        """
        id: IN2.62 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.62
        """
        return self._c_data[61][0]

    @guarantors_relationship_to_insured.setter  # set IN2.62
    def guarantors_relationship_to_insured(self, relationship: Relationship | None):
        """
        id: IN2.62 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.62
        """
        self._c_data[61] = (relationship,)

    @property
    def insureds_phone_number_home(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN2.63 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.63
        """
        return self._c_data[62]

    @insureds_phone_number_home.setter  # set IN2.63
    def insureds_phone_number_home(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN2.63 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.63
        """
        if isinstance(xtn, tuple):
            self._c_data[62] = xtn
        else:
            self._c_data[62] = (xtn,)

    @property
    def insureds_employer_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN2.64 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.64
        """
        return self._c_data[63]

    @insureds_employer_phone_number.setter  # set IN2.64
    def insureds_employer_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN2.64 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.64
        """
        if isinstance(xtn, tuple):
            self._c_data[63] = xtn
        else:
            self._c_data[63] = (xtn,)

    @property  # get IN2.65
    def military_handicapped_program(self) -> MilitaryHandicappedProgramCode | None:
        """
        id: IN2.65 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.65
        """
        return self._c_data[64][0]

    @military_handicapped_program.setter  # set IN2.65
    def military_handicapped_program(
        self, military_handicapped_program_code: MilitaryHandicappedProgramCode | None
    ):
        """
        id: IN2.65 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.65
        """
        self._c_data[64] = (military_handicapped_program_code,)

    @property  # get IN2.66
    def suspend_flag(self) -> YesOrNoIndicator | None:
        """
        id: IN2.66 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.66
        """
        return self._c_data[65][0]

    @suspend_flag.setter  # set IN2.66
    def suspend_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN2.66 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.66
        """
        self._c_data[65] = (yes_or_no_indicator,)

    @property  # get IN2.67
    def copay_limit_flag(self) -> YesOrNoIndicator | None:
        """
        id: IN2.67 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.67
        """
        return self._c_data[66][0]

    @copay_limit_flag.setter  # set IN2.67
    def copay_limit_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN2.67 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.67
        """
        self._c_data[66] = (yes_or_no_indicator,)

    @property  # get IN2.68
    def stoploss_limit_flag(self) -> YesOrNoIndicator | None:
        """
        id: IN2.68 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.68
        """
        return self._c_data[67][0]

    @stoploss_limit_flag.setter  # set IN2.68
    def stoploss_limit_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN2.68 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.68
        """
        self._c_data[67] = (yes_or_no_indicator,)

    @property
    def insured_organization_name_and_id(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: IN2.69 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.69
        """
        return self._c_data[68]

    @insured_organization_name_and_id.setter  # set IN2.69
    def insured_organization_name_and_id(self, xon: XON | tuple[XON] | None):
        """
        id: IN2.69 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.69
        """
        if isinstance(xon, tuple):
            self._c_data[68] = xon
        else:
            self._c_data[68] = (xon,)

    @property
    def insured_employer_organization_name_and_id(
        self,
    ) -> tuple[XON, ...] | tuple[None]:
        """
        id: IN2.70 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.70
        """
        return self._c_data[69]

    @insured_employer_organization_name_and_id.setter  # set IN2.70
    def insured_employer_organization_name_and_id(self, xon: XON | tuple[XON] | None):
        """
        id: IN2.70 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.70
        """
        if isinstance(xon, tuple):
            self._c_data[69] = xon
        else:
            self._c_data[69] = (xon,)

    @property
    def race(self) -> tuple[Race, ...] | tuple[None]:
        """
        id: IN2.71 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.71
        """
        return self._c_data[70]

    @race.setter  # set IN2.71
    def race(self, race: Race | tuple[Race] | None):
        """
        id: IN2.71 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.71
        """
        if isinstance(race, tuple):
            self._c_data[70] = race
        else:
            self._c_data[70] = (race,)

    @property  # get IN2.72
    def cms_patients_relationship_to_insured(
        self,
    ) -> PatientSRelationshipToInsured | None:
        """
        id: IN2.72 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.72
        """
        return self._c_data[71][0]

    @cms_patients_relationship_to_insured.setter  # set IN2.72
    def cms_patients_relationship_to_insured(
        self, patients_relationship_to_insured: PatientSRelationshipToInsured | None
    ):
        """
        id: IN2.72 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN2.72
        """
        self._c_data[71] = (patients_relationship_to_insured,)
