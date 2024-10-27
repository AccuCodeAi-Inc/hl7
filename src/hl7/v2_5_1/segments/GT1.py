from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.JCC import JCC
from ..data_types.XAD import XAD
from ..data_types.CX import CX
from ..data_types.ST import ST
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.NM import NM
from ..data_types.XPN import XPN
from ..data_types.DT import DT
from ..data_types.IS import IS
from ..data_types.XTN import XTN
from ..data_types.CP import CP
from ..data_types.FC import FC
from ..data_types.XON import XON
from ..tables.EthnicGroup import EthnicGroup
from ..tables.GuarantorCreditRatingCode import GuarantorCreditRatingCode
from ..tables.MaritalStatus import MaritalStatus
from ..tables.JobStatus import JobStatus
from ..tables.LivingArrangement import LivingArrangement
from ..tables.Religion import Religion
from ..tables.LivingDependency import LivingDependency
from ..tables.Handicap import Handicap
from ..tables.ContactReason import ContactReason
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.GuarantorType import GuarantorType
from ..tables.EmploymentStatus import EmploymentStatus
from ..tables.StudentStatus import StudentStatus
from ..tables.Citizenship import Citizenship
from ..tables.PublicityCode import PublicityCode
from ..tables.PatientChargeAdjustment import PatientChargeAdjustment
from ..tables.PrimaryLanguage import PrimaryLanguage
from ..tables.AdministrativeSex import AdministrativeSex
from ..tables.Race import Race
from ..tables.Nationality import Nationality
from ..tables.Relationship import Relationship
from ..tables.VipIndicator import VipIndicator
from ..tables.AmbulatoryStatus import AmbulatoryStatus


"""
Guarantor - GT1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::GT1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    GT1,
    ID, TS, JCC, XAD, CX, ST, SI, CE, NM, XPN, DT, IS, XTN, CP, FC, XON
)

gt1 = GT1(  #  - The GT1 segment contains guarantor (e
    set_id_gt1=si,  # SI(...)  # Required.
    guarantor_number=None,  # CX(...) 
    guarantor_name=xpn,  # XPN(...)  # Required.
    guarantor_spouse_name=None,  # XPN(...) 
    guarantor_address=None,  # XAD(...) 
    guarantor_ph_num_home=None,  # XTN(...) 
    guarantor_ph_num_business=None,  # XTN(...) 
    guarantor_date_or_time_of_birth=None,  # TS(...) 
    guarantor_administrative_sex=None,  # IS(...) 
    guarantor_type=None,  # IS(...) 
    guarantor_relationship=None,  # CE(...) 
    guarantor_ssn=None,  # ST(...) 
    guarantor_date_begin=None,  # DT(...) 
    guarantor_date_end=None,  # DT(...) 
    guarantor_priority=None,  # NM(...) 
    guarantor_employer_name=None,  # XPN(...) 
    guarantor_employer_address=None,  # XAD(...) 
    guarantor_employer_phone_number=None,  # XTN(...) 
    guarantor_employee_id_number=None,  # CX(...) 
    guarantor_employment_status=None,  # IS(...) 
    guarantor_organization_name=None,  # XON(...) 
    guarantor_billing_hold_flag=None,  # ID(...) 
    guarantor_credit_rating_code=None,  # CE(...) 
    guarantor_death_date_and_time=None,  # TS(...) 
    guarantor_death_flag=None,  # ID(...) 
    guarantor_charge_adjustment_code=None,  # CE(...) 
    guarantor_household_annual_income=None,  # CP(...) 
    guarantor_household_size=None,  # NM(...) 
    guarantor_employer_id_number=None,  # CX(...) 
    guarantor_marital_status_code=None,  # CE(...) 
    guarantor_hire_effective_date=None,  # DT(...) 
    employment_stop_date=None,  # DT(...) 
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
    contact_persons_name=None,  # XPN(...) 
    contact_persons_telephone_number=None,  # XTN(...) 
    contact_reason=None,  # CE(...) 
    contact_relationship=None,  # IS(...) 
    job_title=None,  # ST(...) 
    job_code_or_class=None,  # JCC(...) 
    guarantor_employers_organization_name=None,  # XON(...) 
    handicap=None,  # IS(...) 
    job_status=None,  # IS(...) 
    guarantor_financial_class=None,  # FC(...) 
    guarantor_race=None,  # CE(...) 
    guarantor_birth_place=None,  # ST(...) 
    vip_indicator=None,  # IS(...) 
)

-----END SEGMENT::GT1 TEMPLATE-----
"""


class GT1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """GT1"""
    _hl7_name = """Guarantor"""
    _hl7_description = """The GT1 segment contains guarantor (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1"
    _c_length = (4, 250, 250, 250, 250, 250, 250, 26, 1, 2, 250, 11, 8, 8, 2, 250, 250, 250, 250, 2, 250, 1, 250, 26, 1, 250, 10, 3, 250, 250, 8, 8, 2, 2, 250, 250, 2, 250, 1, 2, 250, 250, 250, 250, 250, 250, 250, 3, 20, 20, 250, 2, 2, 50, 250, 250, 2,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 65535, 65535, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 1, 1,)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CX, XPN, XPN, XAD, XTN, XTN, TS, IS, IS, CE, ST, DT, DT, NM, XPN, XAD, XTN, CX, IS, XON, ID, CE, TS, ID, CE, CP, NM, CX, CE, DT, DT, IS, IS, CE, CE, IS, CE, ID, IS, CE, XPN, CE, CE, XPN, XTN, CE, IS, ST, JCC, XON, IS, IS, FC, CE, ST, IS,)
    _c_aliases = ("GT1.1", "GT1.2", "GT1.3", "GT1.4", "GT1.5", "GT1.6", "GT1.7", "GT1.8", "GT1.9", "GT1.10", "GT1.11", "GT1.12", "GT1.13", "GT1.14", "GT1.15", "GT1.16", "GT1.17", "GT1.18", "GT1.19", "GT1.20", "GT1.21", "GT1.22", "GT1.23", "GT1.24", "GT1.25", "GT1.26", "GT1.27", "GT1.28", "GT1.29", "GT1.30", "GT1.31", "GT1.32", "GT1.33", "GT1.34", "GT1.35", "GT1.36", "GT1.37", "GT1.38", "GT1.39", "GT1.40", "GT1.41", "GT1.42", "GT1.43", "GT1.44", "GT1.45", "GT1.46", "GT1.47", "GT1.48", "GT1.49", "GT1.50", "GT1.51", "GT1.52", "GT1.53", "GT1.54", "GT1.55", "GT1.56", "GT1.57",)
    _c_names = ("Set ID - GT1", "Guarantor Number", "Guarantor Name", "Guarantor Spouse Name", "Guarantor Address", "Guarantor Ph Num - Home", "Guarantor Ph Num - Business", "Guarantor Date/Time Of Birth", "Guarantor Administrative Sex", "Guarantor Type", "Guarantor Relationship", "Guarantor SSN", "Guarantor Date - Begin", "Guarantor Date - End", "Guarantor Priority", "Guarantor Employer Name", "Guarantor Employer Address", "Guarantor Employer Phone Number", "Guarantor Employee ID Number", "Guarantor Employment Status", "Guarantor Organization Name", "Guarantor Billing Hold Flag", "Guarantor Credit Rating Code", "Guarantor Death Date And Time", "Guarantor Death Flag", "Guarantor Charge Adjustment Code", "Guarantor Household Annual Income", "Guarantor Household Size", "Guarantor Employer ID Number", "Guarantor Marital Status Code", "Guarantor Hire Effective Date", "Employment Stop Date", "Living Dependency", "Ambulatory Status", "Citizenship", "Primary Language", "Living Arrangement", "Publicity Code", "Protection Indicator", "Student Indicator", "Religion", "Mother's Maiden Name", "Nationality", "Ethnic Group", "Contact Person's Name", "Contact Person's Telephone Number", "Contact Reason", "Contact Relationship", "Job Title", "Job Code/Class", "Guarantor Employer's Organization Name", "Handicap", "Job Status", "Guarantor Financial Class", "Guarantor Race", "Guarantor Birth Place", "VIP Indicator",)
    _c_attrs = ("set_id_gt1", "guarantor_number", "guarantor_name", "guarantor_spouse_name", "guarantor_address", "guarantor_ph_num_home", "guarantor_ph_num_business", "guarantor_date_or_time_of_birth", "guarantor_administrative_sex", "guarantor_type", "guarantor_relationship", "guarantor_ssn", "guarantor_date_begin", "guarantor_date_end", "guarantor_priority", "guarantor_employer_name", "guarantor_employer_address", "guarantor_employer_phone_number", "guarantor_employee_id_number", "guarantor_employment_status", "guarantor_organization_name", "guarantor_billing_hold_flag", "guarantor_credit_rating_code", "guarantor_death_date_and_time", "guarantor_death_flag", "guarantor_charge_adjustment_code", "guarantor_household_annual_income", "guarantor_household_size", "guarantor_employer_id_number", "guarantor_marital_status_code", "guarantor_hire_effective_date", "employment_stop_date", "living_dependency", "ambulatory_status", "citizenship", "primary_language", "living_arrangement", "publicity_code", "protection_indicator", "student_indicator", "religion", "mothers_maiden_name", "nationality", "ethnic_group", "contact_persons_name", "contact_persons_telephone_number", "contact_reason", "contact_relationship", "job_title", "job_code_or_class", "guarantor_employers_organization_name", "handicap", "job_status", "guarantor_financial_class", "guarantor_race", "guarantor_birth_place", "vip_indicator",)
    # fmt: on

    def __init__(
        self,
        set_id_gt1: SI,  # GT1.1
        guarantor_name: XPN,  # GT1.3
        guarantor_number: CX | None = None,  # GT1.2
        guarantor_spouse_name: XPN | None = None,  # GT1.4
        guarantor_address: XAD | None = None,  # GT1.5
        guarantor_ph_num_home: XTN | None = None,  # GT1.6
        guarantor_ph_num_business: XTN | None = None,  # GT1.7
        guarantor_date_or_time_of_birth: TS | None = None,  # GT1.8
        guarantor_administrative_sex: AdministrativeSex | IS | None = None,  # GT1.9
        guarantor_type: GuarantorType | IS | None = None,  # GT1.10
        guarantor_relationship: Relationship | CE | None = None,  # GT1.11
        guarantor_ssn: ST | None = None,  # GT1.12
        guarantor_date_begin: DT | None = None,  # GT1.13
        guarantor_date_end: DT | None = None,  # GT1.14
        guarantor_priority: NM | None = None,  # GT1.15
        guarantor_employer_name: XPN | None = None,  # GT1.16
        guarantor_employer_address: XAD | None = None,  # GT1.17
        guarantor_employer_phone_number: XTN | None = None,  # GT1.18
        guarantor_employee_id_number: CX | None = None,  # GT1.19
        guarantor_employment_status: EmploymentStatus | IS | None = None,  # GT1.20
        guarantor_organization_name: XON | None = None,  # GT1.21
        guarantor_billing_hold_flag: YesOrNoIndicator | ID | None = None,  # GT1.22
        guarantor_credit_rating_code: GuarantorCreditRatingCode
        | CE
        | None = None,  # GT1.23
        guarantor_death_date_and_time: TS | None = None,  # GT1.24
        guarantor_death_flag: YesOrNoIndicator | ID | None = None,  # GT1.25
        guarantor_charge_adjustment_code: PatientChargeAdjustment
        | CE
        | None = None,  # GT1.26
        guarantor_household_annual_income: CP | None = None,  # GT1.27
        guarantor_household_size: NM | None = None,  # GT1.28
        guarantor_employer_id_number: CX | None = None,  # GT1.29
        guarantor_marital_status_code: MaritalStatus | CE | None = None,  # GT1.30
        guarantor_hire_effective_date: DT | None = None,  # GT1.31
        employment_stop_date: DT | None = None,  # GT1.32
        living_dependency: LivingDependency | IS | None = None,  # GT1.33
        ambulatory_status: AmbulatoryStatus | IS | None = None,  # GT1.34
        citizenship: Citizenship | CE | None = None,  # GT1.35
        primary_language: PrimaryLanguage | CE | None = None,  # GT1.36
        living_arrangement: LivingArrangement | IS | None = None,  # GT1.37
        publicity_code: PublicityCode | CE | None = None,  # GT1.38
        protection_indicator: YesOrNoIndicator | ID | None = None,  # GT1.39
        student_indicator: StudentStatus | IS | None = None,  # GT1.40
        religion: Religion | CE | None = None,  # GT1.41
        mothers_maiden_name: XPN | None = None,  # GT1.42
        nationality: Nationality | CE | None = None,  # GT1.43
        ethnic_group: EthnicGroup | CE | None = None,  # GT1.44
        contact_persons_name: XPN | None = None,  # GT1.45
        contact_persons_telephone_number: XTN | None = None,  # GT1.46
        contact_reason: ContactReason | CE | None = None,  # GT1.47
        contact_relationship: Relationship | IS | None = None,  # GT1.48
        job_title: ST | None = None,  # GT1.49
        job_code_or_class: JCC | None = None,  # GT1.50
        guarantor_employers_organization_name: XON | None = None,  # GT1.51
        handicap: Handicap | IS | None = None,  # GT1.52
        job_status: JobStatus | IS | None = None,  # GT1.53
        guarantor_financial_class: FC | None = None,  # GT1.54
        guarantor_race: Race | CE | None = None,  # GT1.55
        guarantor_birth_place: ST | None = None,  # GT1.56
        vip_indicator: VipIndicator | IS | None = None,  # GT1.57
    ):
        """
        Guarantor - `GT1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1>`_
        The GT1 segment contains guarantor (e.g., the person or the organization with financial responsibility for payment of a patient account) data for patient and insurance billing applications.

        :param set_id_gt1: Sequence ID (id: GT1.1 | len: 4 | use: R | rpt: 1)
        :param guarantor_number: Extended Composite ID with Check Digit (id: GT1.2 | len: 250 | use: O | rpt: *)
        :param guarantor_name: Extended Person Name (id: GT1.3 | len: 250 | use: R | rpt: *)
        :param guarantor_spouse_name: Extended Person Name (id: GT1.4 | len: 250 | use: O | rpt: *)
        :param guarantor_address: Extended Address (id: GT1.5 | len: 250 | use: O | rpt: *)
        :param guarantor_ph_num_home: Extended Telecommunication Number (id: GT1.6 | len: 250 | use: O | rpt: *)
        :param guarantor_ph_num_business: Extended Telecommunication Number (id: GT1.7 | len: 250 | use: O | rpt: *)
        :param guarantor_date_or_time_of_birth: Time Stamp (id: GT1.8 | len: 26 | use: O | rpt: 1)
        :param guarantor_administrative_sex: Coded value for user-defined tables (id: GT1.9 | len: 1 | use: O | rpt: 1)
        :param guarantor_type: Coded value for user-defined tables (id: GT1.10 | len: 2 | use: O | rpt: 1)
        :param guarantor_relationship: Coded Element (id: GT1.11 | len: 250 | use: O | rpt: 1)
        :param guarantor_ssn: String Data (id: GT1.12 | len: 11 | use: O | rpt: 1)
        :param guarantor_date_begin: Date (id: GT1.13 | len: 8 | use: O | rpt: 1)
        :param guarantor_date_end: Date (id: GT1.14 | len: 8 | use: O | rpt: 1)
        :param guarantor_priority: Numeric (id: GT1.15 | len: 2 | use: O | rpt: 1)
        :param guarantor_employer_name: Extended Person Name (id: GT1.16 | len: 250 | use: O | rpt: *)
        :param guarantor_employer_address: Extended Address (id: GT1.17 | len: 250 | use: O | rpt: *)
        :param guarantor_employer_phone_number: Extended Telecommunication Number (id: GT1.18 | len: 250 | use: O | rpt: *)
        :param guarantor_employee_id_number: Extended Composite ID with Check Digit (id: GT1.19 | len: 250 | use: O | rpt: *)
        :param guarantor_employment_status: Coded value for user-defined tables (id: GT1.20 | len: 2 | use: O | rpt: 1)
        :param guarantor_organization_name: Extended Composite Name and Identification Number for Organizations (id: GT1.21 | len: 250 | use: O | rpt: *)
        :param guarantor_billing_hold_flag: Coded values for HL7 tables (id: GT1.22 | len: 1 | use: O | rpt: 1)
        :param guarantor_credit_rating_code: Coded Element (id: GT1.23 | len: 250 | use: O | rpt: 1)
        :param guarantor_death_date_and_time: Time Stamp (id: GT1.24 | len: 26 | use: O | rpt: 1)
        :param guarantor_death_flag: Coded values for HL7 tables (id: GT1.25 | len: 1 | use: O | rpt: 1)
        :param guarantor_charge_adjustment_code: Coded Element (id: GT1.26 | len: 250 | use: O | rpt: 1)
        :param guarantor_household_annual_income: Composite Price (id: GT1.27 | len: 10 | use: O | rpt: 1)
        :param guarantor_household_size: Numeric (id: GT1.28 | len: 3 | use: O | rpt: 1)
        :param guarantor_employer_id_number: Extended Composite ID with Check Digit (id: GT1.29 | len: 250 | use: O | rpt: *)
        :param guarantor_marital_status_code: Coded Element (id: GT1.30 | len: 250 | use: O | rpt: 1)
        :param guarantor_hire_effective_date: Date (id: GT1.31 | len: 8 | use: O | rpt: 1)
        :param employment_stop_date: Date (id: GT1.32 | len: 8 | use: O | rpt: 1)
        :param living_dependency: Coded value for user-defined tables (id: GT1.33 | len: 2 | use: O | rpt: 1)
        :param ambulatory_status: Coded value for user-defined tables (id: GT1.34 | len: 2 | use: O | rpt: *)
        :param citizenship: Coded Element (id: GT1.35 | len: 250 | use: O | rpt: *)
        :param primary_language: Coded Element (id: GT1.36 | len: 250 | use: O | rpt: 1)
        :param living_arrangement: Coded value for user-defined tables (id: GT1.37 | len: 2 | use: O | rpt: 1)
        :param publicity_code: Coded Element (id: GT1.38 | len: 250 | use: O | rpt: 1)
        :param protection_indicator: Coded values for HL7 tables (id: GT1.39 | len: 1 | use: O | rpt: 1)
        :param student_indicator: Coded value for user-defined tables (id: GT1.40 | len: 2 | use: O | rpt: 1)
        :param religion: Coded Element (id: GT1.41 | len: 250 | use: O | rpt: 1)
        :param mothers_maiden_name: Extended Person Name (id: GT1.42 | len: 250 | use: O | rpt: *)
        :param nationality: Coded Element (id: GT1.43 | len: 250 | use: O | rpt: 1)
        :param ethnic_group: Coded Element (id: GT1.44 | len: 250 | use: O | rpt: *)
        :param contact_persons_name: Extended Person Name (id: GT1.45 | len: 250 | use: O | rpt: *)
        :param contact_persons_telephone_number: Extended Telecommunication Number (id: GT1.46 | len: 250 | use: O | rpt: *)
        :param contact_reason: Coded Element (id: GT1.47 | len: 250 | use: O | rpt: 1)
        :param contact_relationship: Coded value for user-defined tables (id: GT1.48 | len: 3 | use: O | rpt: 1)
        :param job_title: String Data (id: GT1.49 | len: 20 | use: O | rpt: 1)
        :param job_code_or_class: Job Code/Class (id: GT1.50 | len: 20 | use: O | rpt: 1)
        :param guarantor_employers_organization_name: Extended Composite Name and Identification Number for Organizations (id: GT1.51 | len: 250 | use: O | rpt: *)
        :param handicap: Coded value for user-defined tables (id: GT1.52 | len: 2 | use: O | rpt: 1)
        :param job_status: Coded value for user-defined tables (id: GT1.53 | len: 2 | use: O | rpt: 1)
        :param guarantor_financial_class: Financial Class (id: GT1.54 | len: 50 | use: O | rpt: 1)
        :param guarantor_race: Coded Element (id: GT1.55 | len: 250 | use: O | rpt: *)
        :param guarantor_birth_place: String Data (id: GT1.56 | len: 250 | use: O | rpt: 1)
        :param vip_indicator: Coded value for user-defined tables (id: GT1.57 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 57
        self.set_id_gt1 = set_id_gt1
        self.guarantor_number = guarantor_number
        self.guarantor_name = guarantor_name
        self.guarantor_spouse_name = guarantor_spouse_name
        self.guarantor_address = guarantor_address
        self.guarantor_ph_num_home = guarantor_ph_num_home
        self.guarantor_ph_num_business = guarantor_ph_num_business
        self.guarantor_date_or_time_of_birth = guarantor_date_or_time_of_birth
        self.guarantor_administrative_sex = guarantor_administrative_sex
        self.guarantor_type = guarantor_type
        self.guarantor_relationship = guarantor_relationship
        self.guarantor_ssn = guarantor_ssn
        self.guarantor_date_begin = guarantor_date_begin
        self.guarantor_date_end = guarantor_date_end
        self.guarantor_priority = guarantor_priority
        self.guarantor_employer_name = guarantor_employer_name
        self.guarantor_employer_address = guarantor_employer_address
        self.guarantor_employer_phone_number = guarantor_employer_phone_number
        self.guarantor_employee_id_number = guarantor_employee_id_number
        self.guarantor_employment_status = guarantor_employment_status
        self.guarantor_organization_name = guarantor_organization_name
        self.guarantor_billing_hold_flag = guarantor_billing_hold_flag
        self.guarantor_credit_rating_code = guarantor_credit_rating_code
        self.guarantor_death_date_and_time = guarantor_death_date_and_time
        self.guarantor_death_flag = guarantor_death_flag
        self.guarantor_charge_adjustment_code = guarantor_charge_adjustment_code
        self.guarantor_household_annual_income = guarantor_household_annual_income
        self.guarantor_household_size = guarantor_household_size
        self.guarantor_employer_id_number = guarantor_employer_id_number
        self.guarantor_marital_status_code = guarantor_marital_status_code
        self.guarantor_hire_effective_date = guarantor_hire_effective_date
        self.employment_stop_date = employment_stop_date
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
        self.contact_persons_name = contact_persons_name
        self.contact_persons_telephone_number = contact_persons_telephone_number
        self.contact_reason = contact_reason
        self.contact_relationship = contact_relationship
        self.job_title = job_title
        self.job_code_or_class = job_code_or_class
        self.guarantor_employers_organization_name = (
            guarantor_employers_organization_name
        )
        self.handicap = handicap
        self.job_status = job_status
        self.guarantor_financial_class = guarantor_financial_class
        self.guarantor_race = guarantor_race
        self.guarantor_birth_place = guarantor_birth_place
        self.vip_indicator = vip_indicator

    @property  # get GT1.1
    def set_id_gt1(self) -> SI:
        """
        id: GT1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.1
        """
        return self._c_data[0][0]

    @set_id_gt1.setter  # set GT1.1
    def set_id_gt1(self, si: SI):
        """
        id: GT1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.1
        """
        self._c_data[0] = (si,)

    @property
    def guarantor_number(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: GT1.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.2
        """
        return self._c_data[1]

    @guarantor_number.setter  # set GT1.2
    def guarantor_number(self, cx: CX | tuple[CX] | None):
        """
        id: GT1.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.2
        """
        if isinstance(cx, tuple):
            self._c_data[1] = cx
        else:
            self._c_data[1] = (cx,)

    @property
    def guarantor_name(self) -> tuple[XPN, ...]:
        """
        id: GT1.3 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.3
        """
        return self._c_data[2]

    @guarantor_name.setter  # set GT1.3
    def guarantor_name(self, xpn: XPN | tuple[XPN]):
        """
        id: GT1.3 | len: 250 | use: R | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.3
        """
        if isinstance(xpn, tuple):
            self._c_data[2] = xpn
        else:
            self._c_data[2] = (xpn,)

    @property
    def guarantor_spouse_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: GT1.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.4
        """
        return self._c_data[3]

    @guarantor_spouse_name.setter  # set GT1.4
    def guarantor_spouse_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: GT1.4 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.4
        """
        if isinstance(xpn, tuple):
            self._c_data[3] = xpn
        else:
            self._c_data[3] = (xpn,)

    @property
    def guarantor_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: GT1.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.5
        """
        return self._c_data[4]

    @guarantor_address.setter  # set GT1.5
    def guarantor_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: GT1.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.5
        """
        if isinstance(xad, tuple):
            self._c_data[4] = xad
        else:
            self._c_data[4] = (xad,)

    @property
    def guarantor_ph_num_home(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: GT1.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.6
        """
        return self._c_data[5]

    @guarantor_ph_num_home.setter  # set GT1.6
    def guarantor_ph_num_home(self, xtn: XTN | tuple[XTN] | None):
        """
        id: GT1.6 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.6
        """
        if isinstance(xtn, tuple):
            self._c_data[5] = xtn
        else:
            self._c_data[5] = (xtn,)

    @property
    def guarantor_ph_num_business(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: GT1.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.7
        """
        return self._c_data[6]

    @guarantor_ph_num_business.setter  # set GT1.7
    def guarantor_ph_num_business(self, xtn: XTN | tuple[XTN] | None):
        """
        id: GT1.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.7
        """
        if isinstance(xtn, tuple):
            self._c_data[6] = xtn
        else:
            self._c_data[6] = (xtn,)

    @property  # get GT1.8
    def guarantor_date_or_time_of_birth(self) -> TS | None:
        """
        id: GT1.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.8
        """
        return self._c_data[7][0]

    @guarantor_date_or_time_of_birth.setter  # set GT1.8
    def guarantor_date_or_time_of_birth(self, ts: TS | None):
        """
        id: GT1.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.8
        """
        self._c_data[7] = (ts,)

    @property  # get GT1.9
    def guarantor_administrative_sex(self) -> AdministrativeSex | None:
        """
        id: GT1.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.9
        """
        return self._c_data[8][0]

    @guarantor_administrative_sex.setter  # set GT1.9
    def guarantor_administrative_sex(
        self, administrative_sex: AdministrativeSex | None
    ):
        """
        id: GT1.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.9
        """
        self._c_data[8] = (administrative_sex,)

    @property  # get GT1.10
    def guarantor_type(self) -> GuarantorType | None:
        """
        id: GT1.10 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.10
        """
        return self._c_data[9][0]

    @guarantor_type.setter  # set GT1.10
    def guarantor_type(self, guarantor_type: GuarantorType | None):
        """
        id: GT1.10 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.10
        """
        self._c_data[9] = (guarantor_type,)

    @property  # get GT1.11
    def guarantor_relationship(self) -> Relationship | None:
        """
        id: GT1.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.11
        """
        return self._c_data[10][0]

    @guarantor_relationship.setter  # set GT1.11
    def guarantor_relationship(self, relationship: Relationship | None):
        """
        id: GT1.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.11
        """
        self._c_data[10] = (relationship,)

    @property  # get GT1.12
    def guarantor_ssn(self) -> ST | None:
        """
        id: GT1.12 | len: 11 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.12
        """
        return self._c_data[11][0]

    @guarantor_ssn.setter  # set GT1.12
    def guarantor_ssn(self, st: ST | None):
        """
        id: GT1.12 | len: 11 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.12
        """
        self._c_data[11] = (st,)

    @property  # get GT1.13
    def guarantor_date_begin(self) -> DT | None:
        """
        id: GT1.13 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.13
        """
        return self._c_data[12][0]

    @guarantor_date_begin.setter  # set GT1.13
    def guarantor_date_begin(self, dt: DT | None):
        """
        id: GT1.13 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.13
        """
        self._c_data[12] = (dt,)

    @property  # get GT1.14
    def guarantor_date_end(self) -> DT | None:
        """
        id: GT1.14 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.14
        """
        return self._c_data[13][0]

    @guarantor_date_end.setter  # set GT1.14
    def guarantor_date_end(self, dt: DT | None):
        """
        id: GT1.14 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.14
        """
        self._c_data[13] = (dt,)

    @property  # get GT1.15
    def guarantor_priority(self) -> NM | None:
        """
        id: GT1.15 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.15
        """
        return self._c_data[14][0]

    @guarantor_priority.setter  # set GT1.15
    def guarantor_priority(self, nm: NM | None):
        """
        id: GT1.15 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.15
        """
        self._c_data[14] = (nm,)

    @property
    def guarantor_employer_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: GT1.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.16
        """
        return self._c_data[15]

    @guarantor_employer_name.setter  # set GT1.16
    def guarantor_employer_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: GT1.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.16
        """
        if isinstance(xpn, tuple):
            self._c_data[15] = xpn
        else:
            self._c_data[15] = (xpn,)

    @property
    def guarantor_employer_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: GT1.17 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.17
        """
        return self._c_data[16]

    @guarantor_employer_address.setter  # set GT1.17
    def guarantor_employer_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: GT1.17 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.17
        """
        if isinstance(xad, tuple):
            self._c_data[16] = xad
        else:
            self._c_data[16] = (xad,)

    @property
    def guarantor_employer_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: GT1.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.18
        """
        return self._c_data[17]

    @guarantor_employer_phone_number.setter  # set GT1.18
    def guarantor_employer_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: GT1.18 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.18
        """
        if isinstance(xtn, tuple):
            self._c_data[17] = xtn
        else:
            self._c_data[17] = (xtn,)

    @property
    def guarantor_employee_id_number(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: GT1.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.19
        """
        return self._c_data[18]

    @guarantor_employee_id_number.setter  # set GT1.19
    def guarantor_employee_id_number(self, cx: CX | tuple[CX] | None):
        """
        id: GT1.19 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.19
        """
        if isinstance(cx, tuple):
            self._c_data[18] = cx
        else:
            self._c_data[18] = (cx,)

    @property  # get GT1.20
    def guarantor_employment_status(self) -> EmploymentStatus | None:
        """
        id: GT1.20 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.20
        """
        return self._c_data[19][0]

    @guarantor_employment_status.setter  # set GT1.20
    def guarantor_employment_status(self, employment_status: EmploymentStatus | None):
        """
        id: GT1.20 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.20
        """
        self._c_data[19] = (employment_status,)

    @property
    def guarantor_organization_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: GT1.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.21
        """
        return self._c_data[20]

    @guarantor_organization_name.setter  # set GT1.21
    def guarantor_organization_name(self, xon: XON | tuple[XON] | None):
        """
        id: GT1.21 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.21
        """
        if isinstance(xon, tuple):
            self._c_data[20] = xon
        else:
            self._c_data[20] = (xon,)

    @property  # get GT1.22
    def guarantor_billing_hold_flag(self) -> YesOrNoIndicator | None:
        """
        id: GT1.22 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.22
        """
        return self._c_data[21][0]

    @guarantor_billing_hold_flag.setter  # set GT1.22
    def guarantor_billing_hold_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: GT1.22 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.22
        """
        self._c_data[21] = (yes_or_no_indicator,)

    @property  # get GT1.23
    def guarantor_credit_rating_code(self) -> GuarantorCreditRatingCode | None:
        """
        id: GT1.23 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.23
        """
        return self._c_data[22][0]

    @guarantor_credit_rating_code.setter  # set GT1.23
    def guarantor_credit_rating_code(
        self, guarantor_credit_rating_code: GuarantorCreditRatingCode | None
    ):
        """
        id: GT1.23 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.23
        """
        self._c_data[22] = (guarantor_credit_rating_code,)

    @property  # get GT1.24
    def guarantor_death_date_and_time(self) -> TS | None:
        """
        id: GT1.24 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.24
        """
        return self._c_data[23][0]

    @guarantor_death_date_and_time.setter  # set GT1.24
    def guarantor_death_date_and_time(self, ts: TS | None):
        """
        id: GT1.24 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.24
        """
        self._c_data[23] = (ts,)

    @property  # get GT1.25
    def guarantor_death_flag(self) -> YesOrNoIndicator | None:
        """
        id: GT1.25 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.25
        """
        return self._c_data[24][0]

    @guarantor_death_flag.setter  # set GT1.25
    def guarantor_death_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: GT1.25 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.25
        """
        self._c_data[24] = (yes_or_no_indicator,)

    @property  # get GT1.26
    def guarantor_charge_adjustment_code(self) -> PatientChargeAdjustment | None:
        """
        id: GT1.26 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.26
        """
        return self._c_data[25][0]

    @guarantor_charge_adjustment_code.setter  # set GT1.26
    def guarantor_charge_adjustment_code(
        self, patient_charge_adjustment: PatientChargeAdjustment | None
    ):
        """
        id: GT1.26 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.26
        """
        self._c_data[25] = (patient_charge_adjustment,)

    @property  # get GT1.27
    def guarantor_household_annual_income(self) -> CP | None:
        """
        id: GT1.27 | len: 10 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.27
        """
        return self._c_data[26][0]

    @guarantor_household_annual_income.setter  # set GT1.27
    def guarantor_household_annual_income(self, cp: CP | None):
        """
        id: GT1.27 | len: 10 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.27
        """
        self._c_data[26] = (cp,)

    @property  # get GT1.28
    def guarantor_household_size(self) -> NM | None:
        """
        id: GT1.28 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.28
        """
        return self._c_data[27][0]

    @guarantor_household_size.setter  # set GT1.28
    def guarantor_household_size(self, nm: NM | None):
        """
        id: GT1.28 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.28
        """
        self._c_data[27] = (nm,)

    @property
    def guarantor_employer_id_number(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: GT1.29 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.29
        """
        return self._c_data[28]

    @guarantor_employer_id_number.setter  # set GT1.29
    def guarantor_employer_id_number(self, cx: CX | tuple[CX] | None):
        """
        id: GT1.29 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.29
        """
        if isinstance(cx, tuple):
            self._c_data[28] = cx
        else:
            self._c_data[28] = (cx,)

    @property  # get GT1.30
    def guarantor_marital_status_code(self) -> MaritalStatus | None:
        """
        id: GT1.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.30
        """
        return self._c_data[29][0]

    @guarantor_marital_status_code.setter  # set GT1.30
    def guarantor_marital_status_code(self, marital_status: MaritalStatus | None):
        """
        id: GT1.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.30
        """
        self._c_data[29] = (marital_status,)

    @property  # get GT1.31
    def guarantor_hire_effective_date(self) -> DT | None:
        """
        id: GT1.31 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.31
        """
        return self._c_data[30][0]

    @guarantor_hire_effective_date.setter  # set GT1.31
    def guarantor_hire_effective_date(self, dt: DT | None):
        """
        id: GT1.31 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.31
        """
        self._c_data[30] = (dt,)

    @property  # get GT1.32
    def employment_stop_date(self) -> DT | None:
        """
        id: GT1.32 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.32
        """
        return self._c_data[31][0]

    @employment_stop_date.setter  # set GT1.32
    def employment_stop_date(self, dt: DT | None):
        """
        id: GT1.32 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.32
        """
        self._c_data[31] = (dt,)

    @property  # get GT1.33
    def living_dependency(self) -> LivingDependency | None:
        """
        id: GT1.33 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.33
        """
        return self._c_data[32][0]

    @living_dependency.setter  # set GT1.33
    def living_dependency(self, living_dependency: LivingDependency | None):
        """
        id: GT1.33 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.33
        """
        self._c_data[32] = (living_dependency,)

    @property
    def ambulatory_status(self) -> tuple[AmbulatoryStatus, ...] | tuple[None]:
        """
        id: GT1.34 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.34
        """
        return self._c_data[33]

    @ambulatory_status.setter  # set GT1.34
    def ambulatory_status(
        self, ambulatory_status: AmbulatoryStatus | tuple[AmbulatoryStatus] | None
    ):
        """
        id: GT1.34 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.34
        """
        if isinstance(ambulatory_status, tuple):
            self._c_data[33] = ambulatory_status
        else:
            self._c_data[33] = (ambulatory_status,)

    @property
    def citizenship(self) -> tuple[Citizenship, ...] | tuple[None]:
        """
        id: GT1.35 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.35
        """
        return self._c_data[34]

    @citizenship.setter  # set GT1.35
    def citizenship(self, citizenship: Citizenship | tuple[Citizenship] | None):
        """
        id: GT1.35 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.35
        """
        if isinstance(citizenship, tuple):
            self._c_data[34] = citizenship
        else:
            self._c_data[34] = (citizenship,)

    @property  # get GT1.36
    def primary_language(self) -> PrimaryLanguage | None:
        """
        id: GT1.36 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.36
        """
        return self._c_data[35][0]

    @primary_language.setter  # set GT1.36
    def primary_language(self, primary_language: PrimaryLanguage | None):
        """
        id: GT1.36 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.36
        """
        self._c_data[35] = (primary_language,)

    @property  # get GT1.37
    def living_arrangement(self) -> LivingArrangement | None:
        """
        id: GT1.37 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.37
        """
        return self._c_data[36][0]

    @living_arrangement.setter  # set GT1.37
    def living_arrangement(self, living_arrangement: LivingArrangement | None):
        """
        id: GT1.37 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.37
        """
        self._c_data[36] = (living_arrangement,)

    @property  # get GT1.38
    def publicity_code(self) -> PublicityCode | None:
        """
        id: GT1.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.38
        """
        return self._c_data[37][0]

    @publicity_code.setter  # set GT1.38
    def publicity_code(self, publicity_code: PublicityCode | None):
        """
        id: GT1.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.38
        """
        self._c_data[37] = (publicity_code,)

    @property  # get GT1.39
    def protection_indicator(self) -> YesOrNoIndicator | None:
        """
        id: GT1.39 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.39
        """
        return self._c_data[38][0]

    @protection_indicator.setter  # set GT1.39
    def protection_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: GT1.39 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.39
        """
        self._c_data[38] = (yes_or_no_indicator,)

    @property  # get GT1.40
    def student_indicator(self) -> StudentStatus | None:
        """
        id: GT1.40 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.40
        """
        return self._c_data[39][0]

    @student_indicator.setter  # set GT1.40
    def student_indicator(self, student_status: StudentStatus | None):
        """
        id: GT1.40 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.40
        """
        self._c_data[39] = (student_status,)

    @property  # get GT1.41
    def religion(self) -> Religion | None:
        """
        id: GT1.41 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.41
        """
        return self._c_data[40][0]

    @religion.setter  # set GT1.41
    def religion(self, religion: Religion | None):
        """
        id: GT1.41 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.41
        """
        self._c_data[40] = (religion,)

    @property
    def mothers_maiden_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: GT1.42 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.42
        """
        return self._c_data[41]

    @mothers_maiden_name.setter  # set GT1.42
    def mothers_maiden_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: GT1.42 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.42
        """
        if isinstance(xpn, tuple):
            self._c_data[41] = xpn
        else:
            self._c_data[41] = (xpn,)

    @property  # get GT1.43
    def nationality(self) -> Nationality | None:
        """
        id: GT1.43 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.43
        """
        return self._c_data[42][0]

    @nationality.setter  # set GT1.43
    def nationality(self, nationality: Nationality | None):
        """
        id: GT1.43 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.43
        """
        self._c_data[42] = (nationality,)

    @property
    def ethnic_group(self) -> tuple[EthnicGroup, ...] | tuple[None]:
        """
        id: GT1.44 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.44
        """
        return self._c_data[43]

    @ethnic_group.setter  # set GT1.44
    def ethnic_group(self, ethnic_group: EthnicGroup | tuple[EthnicGroup] | None):
        """
        id: GT1.44 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.44
        """
        if isinstance(ethnic_group, tuple):
            self._c_data[43] = ethnic_group
        else:
            self._c_data[43] = (ethnic_group,)

    @property
    def contact_persons_name(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: GT1.45 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.45
        """
        return self._c_data[44]

    @contact_persons_name.setter  # set GT1.45
    def contact_persons_name(self, xpn: XPN | tuple[XPN] | None):
        """
        id: GT1.45 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.45
        """
        if isinstance(xpn, tuple):
            self._c_data[44] = xpn
        else:
            self._c_data[44] = (xpn,)

    @property
    def contact_persons_telephone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: GT1.46 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.46
        """
        return self._c_data[45]

    @contact_persons_telephone_number.setter  # set GT1.46
    def contact_persons_telephone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: GT1.46 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.46
        """
        if isinstance(xtn, tuple):
            self._c_data[45] = xtn
        else:
            self._c_data[45] = (xtn,)

    @property  # get GT1.47
    def contact_reason(self) -> ContactReason | None:
        """
        id: GT1.47 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.47
        """
        return self._c_data[46][0]

    @contact_reason.setter  # set GT1.47
    def contact_reason(self, contact_reason: ContactReason | None):
        """
        id: GT1.47 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.47
        """
        self._c_data[46] = (contact_reason,)

    @property  # get GT1.48
    def contact_relationship(self) -> Relationship | None:
        """
        id: GT1.48 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.48
        """
        return self._c_data[47][0]

    @contact_relationship.setter  # set GT1.48
    def contact_relationship(self, relationship: Relationship | None):
        """
        id: GT1.48 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.48
        """
        self._c_data[47] = (relationship,)

    @property  # get GT1.49
    def job_title(self) -> ST | None:
        """
        id: GT1.49 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.49
        """
        return self._c_data[48][0]

    @job_title.setter  # set GT1.49
    def job_title(self, st: ST | None):
        """
        id: GT1.49 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.49
        """
        self._c_data[48] = (st,)

    @property  # get GT1.50
    def job_code_or_class(self) -> JCC | None:
        """
        id: GT1.50 | len: 20 | use: O | rpt: 1
        ---
        return_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.50
        """
        return self._c_data[49][0]

    @job_code_or_class.setter  # set GT1.50
    def job_code_or_class(self, jcc: JCC | None):
        """
        id: GT1.50 | len: 20 | use: O | rpt: 1
        ---
        param_type: JCC: Job Code/Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.50
        """
        self._c_data[49] = (jcc,)

    @property
    def guarantor_employers_organization_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: GT1.51 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.51
        """
        return self._c_data[50]

    @guarantor_employers_organization_name.setter  # set GT1.51
    def guarantor_employers_organization_name(self, xon: XON | tuple[XON] | None):
        """
        id: GT1.51 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.51
        """
        if isinstance(xon, tuple):
            self._c_data[50] = xon
        else:
            self._c_data[50] = (xon,)

    @property  # get GT1.52
    def handicap(self) -> Handicap | None:
        """
        id: GT1.52 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.52
        """
        return self._c_data[51][0]

    @handicap.setter  # set GT1.52
    def handicap(self, handicap: Handicap | None):
        """
        id: GT1.52 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.52
        """
        self._c_data[51] = (handicap,)

    @property  # get GT1.53
    def job_status(self) -> JobStatus | None:
        """
        id: GT1.53 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.53
        """
        return self._c_data[52][0]

    @job_status.setter  # set GT1.53
    def job_status(self, job_status: JobStatus | None):
        """
        id: GT1.53 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.53
        """
        self._c_data[52] = (job_status,)

    @property  # get GT1.54
    def guarantor_financial_class(self) -> FC | None:
        """
        id: GT1.54 | len: 50 | use: O | rpt: 1
        ---
        return_type: FC: Financial Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.54
        """
        return self._c_data[53][0]

    @guarantor_financial_class.setter  # set GT1.54
    def guarantor_financial_class(self, fc: FC | None):
        """
        id: GT1.54 | len: 50 | use: O | rpt: 1
        ---
        param_type: FC: Financial Class
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.54
        """
        self._c_data[53] = (fc,)

    @property
    def guarantor_race(self) -> tuple[Race, ...] | tuple[None]:
        """
        id: GT1.55 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.55
        """
        return self._c_data[54]

    @guarantor_race.setter  # set GT1.55
    def guarantor_race(self, race: Race | tuple[Race] | None):
        """
        id: GT1.55 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.55
        """
        if isinstance(race, tuple):
            self._c_data[54] = race
        else:
            self._c_data[54] = (race,)

    @property  # get GT1.56
    def guarantor_birth_place(self) -> ST | None:
        """
        id: GT1.56 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.56
        """
        return self._c_data[55][0]

    @guarantor_birth_place.setter  # set GT1.56
    def guarantor_birth_place(self, st: ST | None):
        """
        id: GT1.56 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.56
        """
        self._c_data[55] = (st,)

    @property  # get GT1.57
    def vip_indicator(self) -> VipIndicator | None:
        """
        id: GT1.57 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.57
        """
        return self._c_data[56][0]

    @vip_indicator.setter  # set GT1.57
    def vip_indicator(self, vip_indicator: VipIndicator | None):
        """
        id: GT1.57 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/GT1.57
        """
        self._c_data[56] = (vip_indicator,)
