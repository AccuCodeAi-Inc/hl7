from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..data_types.IS import IS
from ..data_types.CX import CX
from ..data_types.DT import DT
from ..data_types.AUI import AUI
from ..data_types.TS import TS
from ..data_types.XTN import XTN
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.XPN import XPN
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.CP import CP
from ..data_types.SI import SI
from ..data_types.XAD import XAD
from ..tables.Relationship import Relationship
from ..tables.EmploymentStatus import EmploymentStatus
from ..tables.VipIndicator import VipIndicator
from ..tables.CoordinationOfBenefits import CoordinationOfBenefits
from ..tables.AdministrativeSex import AdministrativeSex
from ..tables.ReleaseInformation import ReleaseInformation
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.CoverageType import CoverageType
from ..tables.TypeOfAgreement import TypeOfAgreement
from ..tables.InsurancePlanId import InsurancePlanId
from ..tables.PlanId import PlanId
from ..tables.BillingStatus import BillingStatus
from ..tables.CompanyPlanCode import CompanyPlanCode
from ..tables.AssignmentOfBenefits import AssignmentOfBenefits
from ..tables.Handicap import Handicap
from ..tables.SignatureCode import SignatureCode


"""
Insurance - IN1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::IN1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    IN1,
    CE, XON, IS, CX, DT, AUI, TS, XTN, ID, NM, XPN, ST, XCN, CP, SI, XAD
)

in1 = IN1(  #  - The IN1 segment contains insurance policy coverage information necessary to produce properly pro-rated and patient and insurance bills
    set_id_in1=si,  # SI(...)  # Required.
    insurance_plan_id=ce,  # CE(...)  # Required.
    insurance_company_id=cx,  # CX(...)  # Required.
    insurance_company_name=None,  # XON(...) 
    insurance_company_address=None,  # XAD(...) 
    insurance_co_contact_person=None,  # XPN(...) 
    insurance_co_phone_number=None,  # XTN(...) 
    group_number=None,  # ST(...) 
    group_name=None,  # XON(...) 
    insureds_group_emp_id=None,  # CX(...) 
    insureds_group_emp_name=None,  # XON(...) 
    plan_effective_date=None,  # DT(...) 
    plan_expiration_date=None,  # DT(...) 
    authorization_information=None,  # AUI(...) 
    plan_type=None,  # IS(...) 
    name_of_insured=None,  # XPN(...) 
    insureds_relationship_to_patient=None,  # CE(...) 
    insureds_date_of_birth=None,  # TS(...) 
    insureds_address=None,  # XAD(...) 
    assignment_of_benefits=None,  # IS(...) 
    coordination_of_benefits=None,  # IS(...) 
    coord_of_ben_priority=None,  # ST(...) 
    notice_of_admission_flag=None,  # ID(...) 
    notice_of_admission_date=None,  # DT(...) 
    report_of_eligibility_flag=None,  # ID(...) 
    report_of_eligibility_date=None,  # DT(...) 
    release_information_code=None,  # IS(...) 
    pre_admit_cert=None,  # ST(...) 
    verification_date_or_time=None,  # TS(...) 
    verification_by=None,  # XCN(...) 
    type_of_agreement_code=None,  # IS(...) 
    billing_status=None,  # IS(...) 
    lifetime_reserve_days=None,  # NM(...) 
    delay_before_l_r_day=None,  # NM(...) 
    company_plan_code=None,  # IS(...) 
    policy_number=None,  # ST(...) 
    policy_deductible=None,  # CP(...) 
    policy_limit_amount=None,  # CP(...) 
    policy_limit_days=None,  # NM(...) 
    room_rate_semi_private=None,  # CP(...) 
    room_rate_private=None,  # CP(...) 
    insureds_employment_status=None,  # CE(...) 
    insureds_administrative_sex=None,  # IS(...) 
    insureds_employers_address=None,  # XAD(...) 
    verification_status=None,  # ST(...) 
    prior_insurance_plan_id=None,  # IS(...) 
    coverage_type=None,  # IS(...) 
    handicap=None,  # IS(...) 
    insureds_id_number=None,  # CX(...) 
    signature_code=None,  # IS(...) 
    signature_code_date=None,  # DT(...) 
    insureds_birth_place=None,  # ST(...) 
    vip_indicator=None,  # IS(...) 
)

-----END SEGMENT::IN1 TEMPLATE-----
"""


class IN1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """IN1"""
    _hl7_name = """Insurance"""
    _hl7_description = """The IN1 segment contains insurance policy coverage information necessary to produce properly pro-rated and patient and insurance bills"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1"
    _c_length = (4, 250, 250, 250, 250, 250, 250, 12, 250, 250, 250, 8, 8, 239, 3, 250, 250, 26, 250, 2, 2, 2, 1, 8, 1, 8, 2, 15, 26, 250, 2, 2, 4, 4, 8, 15, 12, 12, 4, 12, 12, 250, 1, 250, 2, 8, 3, 2, 250, 1, 8, 250, 2,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535, 65535, 65535, 1, 1, 1, 1, 65535, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 65535, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B", "O", "B", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CE, CX, XON, XAD, XPN, XTN, ST, XON, CX, XON, DT, DT, AUI, IS, XPN, CE, TS, XAD, IS, IS, ST, ID, DT, ID, DT, IS, ST, TS, XCN, IS, IS, NM, NM, IS, ST, CP, CP, NM, CP, CP, CE, IS, XAD, ST, IS, IS, IS, CX, IS, DT, ST, IS,)
    _c_aliases = ("IN1.1", "IN1.2", "IN1.3", "IN1.4", "IN1.5", "IN1.6", "IN1.7", "IN1.8", "IN1.9", "IN1.10", "IN1.11", "IN1.12", "IN1.13", "IN1.14", "IN1.15", "IN1.16", "IN1.17", "IN1.18", "IN1.19", "IN1.20", "IN1.21", "IN1.22", "IN1.23", "IN1.24", "IN1.25", "IN1.26", "IN1.27", "IN1.28", "IN1.29", "IN1.30", "IN1.31", "IN1.32", "IN1.33", "IN1.34", "IN1.35", "IN1.36", "IN1.37", "IN1.38", "IN1.39", "IN1.40", "IN1.41", "IN1.42", "IN1.43", "IN1.44", "IN1.45", "IN1.46", "IN1.47", "IN1.48", "IN1.49", "IN1.50", "IN1.51", "IN1.52", "IN1.53",)
    _c_names = ("Set ID - IN1", "Insurance Plan ID", "Insurance Company ID", "Insurance Company Name", "Insurance Company Address", "Insurance Co Contact Person", "Insurance Co Phone Number", "Group Number", "Group Name", "Insured's Group Emp ID", "Insured's Group Emp Name", "Plan Effective Date", "Plan Expiration Date", "Authorization Information", "Plan Type", "Name Of Insured", "Insured's Relationship To Patient", "Insured's Date Of Birth", "Insured's Address", "Assignment Of Benefits", "Coordination Of Benefits", "Coord Of Ben. Priority", "Notice Of Admission Flag", "Notice Of Admission Date", "Report Of Eligibility Flag", "Report Of Eligibility Date", "Release Information Code", "Pre-Admit Cert (PAC)", "Verification Date/Time", "Verification By", "Type Of Agreement Code", "Billing Status", "Lifetime Reserve Days", "Delay Before L.R. Day", "Company Plan Code", "Policy Number", "Policy Deductible", "Policy Limit - Amount", "Policy Limit - Days", "Room Rate - Semi-Private", "Room Rate - Private", "Insured's Employment Status", "Insured's Administrative Sex", "Insured's Employer's Address", "Verification Status", "Prior Insurance Plan ID", "Coverage Type", "Handicap", "Insured's ID Number", "Signature Code", "Signature Code Date", "Insured's Birth Place", "VIP Indicator",)
    _c_attrs = ("set_id_in1", "insurance_plan_id", "insurance_company_id", "insurance_company_name", "insurance_company_address", "insurance_co_contact_person", "insurance_co_phone_number", "group_number", "group_name", "insureds_group_emp_id", "insureds_group_emp_name", "plan_effective_date", "plan_expiration_date", "authorization_information", "plan_type", "name_of_insured", "insureds_relationship_to_patient", "insureds_date_of_birth", "insureds_address", "assignment_of_benefits", "coordination_of_benefits", "coord_of_ben_priority", "notice_of_admission_flag", "notice_of_admission_date", "report_of_eligibility_flag", "report_of_eligibility_date", "release_information_code", "pre_admit_cert", "verification_date_or_time", "verification_by", "type_of_agreement_code", "billing_status", "lifetime_reserve_days", "delay_before_l_r_day", "company_plan_code", "policy_number", "policy_deductible", "policy_limit_amount", "policy_limit_days", "room_rate_semi_private", "room_rate_private", "insureds_employment_status", "insureds_administrative_sex", "insureds_employers_address", "verification_status", "prior_insurance_plan_id", "coverage_type", "handicap", "insureds_id_number", "signature_code", "signature_code_date", "insureds_birth_place", "vip_indicator",)
    # fmt: on

    def __init__(
        self,
        set_id_in1: SI,  # IN1.1
        insurance_plan_id: InsurancePlanId | CE,  # IN1.2
        insurance_company_id: CX,  # IN1.3
        insurance_company_name: XON | None = None,  # IN1.4
        insurance_company_address: XAD | None = None,  # IN1.5
        insurance_co_contact_person: XPN | None = None,  # IN1.6
        insurance_co_phone_number: XTN | None = None,  # IN1.7
        group_number: ST | None = None,  # IN1.8
        group_name: XON | None = None,  # IN1.9
        insureds_group_emp_id: CX | None = None,  # IN1.10
        insureds_group_emp_name: XON | None = None,  # IN1.11
        plan_effective_date: DT | None = None,  # IN1.12
        plan_expiration_date: DT | None = None,  # IN1.13
        authorization_information: AUI | None = None,  # IN1.14
        plan_type: PlanId | IS | None = None,  # IN1.15
        name_of_insured: XPN | None = None,  # IN1.16
        insureds_relationship_to_patient: Relationship | CE | None = None,  # IN1.17
        insureds_date_of_birth: TS | None = None,  # IN1.18
        insureds_address: XAD | None = None,  # IN1.19
        assignment_of_benefits: AssignmentOfBenefits | IS | None = None,  # IN1.20
        coordination_of_benefits: CoordinationOfBenefits | IS | None = None,  # IN1.21
        coord_of_ben_priority: ST | None = None,  # IN1.22
        notice_of_admission_flag: YesOrNoIndicator | ID | None = None,  # IN1.23
        notice_of_admission_date: DT | None = None,  # IN1.24
        report_of_eligibility_flag: YesOrNoIndicator | ID | None = None,  # IN1.25
        report_of_eligibility_date: DT | None = None,  # IN1.26
        release_information_code: ReleaseInformation | IS | None = None,  # IN1.27
        pre_admit_cert: ST | None = None,  # IN1.28
        verification_date_or_time: TS | None = None,  # IN1.29
        verification_by: XCN | None = None,  # IN1.30
        type_of_agreement_code: TypeOfAgreement | IS | None = None,  # IN1.31
        billing_status: BillingStatus | IS | None = None,  # IN1.32
        lifetime_reserve_days: NM | None = None,  # IN1.33
        delay_before_l_r_day: NM | None = None,  # IN1.34
        company_plan_code: CompanyPlanCode | IS | None = None,  # IN1.35
        policy_number: ST | None = None,  # IN1.36
        policy_deductible: CP | None = None,  # IN1.37
        policy_limit_amount: CP | None = None,  # IN1.38
        policy_limit_days: NM | None = None,  # IN1.39
        room_rate_semi_private: CP | None = None,  # IN1.40
        room_rate_private: CP | None = None,  # IN1.41
        insureds_employment_status: EmploymentStatus | CE | None = None,  # IN1.42
        insureds_administrative_sex: AdministrativeSex | IS | None = None,  # IN1.43
        insureds_employers_address: XAD | None = None,  # IN1.44
        verification_status: ST | None = None,  # IN1.45
        prior_insurance_plan_id: InsurancePlanId | IS | None = None,  # IN1.46
        coverage_type: CoverageType | IS | None = None,  # IN1.47
        handicap: Handicap | IS | None = None,  # IN1.48
        insureds_id_number: CX | None = None,  # IN1.49
        signature_code: SignatureCode | IS | None = None,  # IN1.50
        signature_code_date: DT | None = None,  # IN1.51
        insureds_birth_place: ST | None = None,  # IN1.52
        vip_indicator: VipIndicator | IS | None = None,  # IN1.53
    ):
        """
        Insurance - `IN1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IN1>`_
        The IN1 segment contains insurance policy coverage information necessary to produce properly pro-rated and patient and insurance bills.

        :param set_id_in1: Sequence ID (id: IN1.1 | len: 4 | use: R | rpt: 1)
        :param insurance_plan_id: Coded Element (id: IN1.2 | len: 250 | use: R | rpt: 1)
        :param insurance_company_id: Extended Composite ID with Check Digit (id: IN1.3 | len: 250 | use: R | rpt: *)
        :param insurance_company_name: Extended Composite Name and Identification Number for Organizations (id: IN1.4 | len: 250 | use: O | rpt: *)
        :param insurance_company_address: Extended Address (id: IN1.5 | len: 250 | use: O | rpt: *)
        :param insurance_co_contact_person: Extended Person Name (id: IN1.6 | len: 250 | use: O | rpt: *)
        :param insurance_co_phone_number: Extended Telecommunication Number (id: IN1.7 | len: 250 | use: O | rpt: *)
        :param group_number: String Data (id: IN1.8 | len: 12 | use: O | rpt: 1)
        :param group_name: Extended Composite Name and Identification Number for Organizations (id: IN1.9 | len: 250 | use: O | rpt: *)
        :param insureds_group_emp_id: Extended Composite ID with Check Digit (id: IN1.10 | len: 250 | use: O | rpt: *)
        :param insureds_group_emp_name: Extended Composite Name and Identification Number for Organizations (id: IN1.11 | len: 250 | use: O | rpt: *)
        :param plan_effective_date: Date (id: IN1.12 | len: 8 | use: O | rpt: 1)
        :param plan_expiration_date: Date (id: IN1.13 | len: 8 | use: O | rpt: 1)
        :param authorization_information: Authorization Information (id: IN1.14 | len: 239 | use: O | rpt: 1)
        :param plan_type: Coded value for user-defined tables (id: IN1.15 | len: 3 | use: O | rpt: 1)
        :param name_of_insured: Extended Person Name (id: IN1.16 | len: 250 | use: O | rpt: *)
        :param insureds_relationship_to_patient: Coded Element (id: IN1.17 | len: 250 | use: O | rpt: 1)
        :param insureds_date_of_birth: Time Stamp (id: IN1.18 | len: 26 | use: O | rpt: 1)
        :param insureds_address: Extended Address (id: IN1.19 | len: 250 | use: O | rpt: *)
        :param assignment_of_benefits: Coded value for user-defined tables (id: IN1.20 | len: 2 | use: O | rpt: 1)
        :param coordination_of_benefits: Coded value for user-defined tables (id: IN1.21 | len: 2 | use: O | rpt: 1)
        :param coord_of_ben_priority: String Data (id: IN1.22 | len: 2 | use: O | rpt: 1)
        :param notice_of_admission_flag: Coded values for HL7 tables (id: IN1.23 | len: 1 | use: O | rpt: 1)
        :param notice_of_admission_date: Date (id: IN1.24 | len: 8 | use: O | rpt: 1)
        :param report_of_eligibility_flag: Coded values for HL7 tables (id: IN1.25 | len: 1 | use: O | rpt: 1)
        :param report_of_eligibility_date: Date (id: IN1.26 | len: 8 | use: O | rpt: 1)
        :param release_information_code: Coded value for user-defined tables (id: IN1.27 | len: 2 | use: O | rpt: 1)
        :param pre_admit_cert: String Data (id: IN1.28 | len: 15 | use: O | rpt: 1)
        :param verification_date_or_time: Time Stamp (id: IN1.29 | len: 26 | use: O | rpt: 1)
        :param verification_by: Extended Composite ID Number and Name for Persons (id: IN1.30 | len: 250 | use: O | rpt: *)
        :param type_of_agreement_code: Coded value for user-defined tables (id: IN1.31 | len: 2 | use: O | rpt: 1)
        :param billing_status: Coded value for user-defined tables (id: IN1.32 | len: 2 | use: O | rpt: 1)
        :param lifetime_reserve_days: Numeric (id: IN1.33 | len: 4 | use: O | rpt: 1)
        :param delay_before_l_r_day: Numeric (id: IN1.34 | len: 4 | use: O | rpt: 1)
        :param company_plan_code: Coded value for user-defined tables (id: IN1.35 | len: 8 | use: O | rpt: 1)
        :param policy_number: String Data (id: IN1.36 | len: 15 | use: O | rpt: 1)
        :param policy_deductible: Composite Price (id: IN1.37 | len: 12 | use: O | rpt: 1)
        :param policy_limit_amount: Composite Price (id: IN1.38 | len: 12 | use: B | rpt: 1)
        :param policy_limit_days: Numeric (id: IN1.39 | len: 4 | use: O | rpt: 1)
        :param room_rate_semi_private: Composite Price (id: IN1.40 | len: 12 | use: B | rpt: 1)
        :param room_rate_private: Composite Price (id: IN1.41 | len: 12 | use: B | rpt: 1)
        :param insureds_employment_status: Coded Element (id: IN1.42 | len: 250 | use: O | rpt: 1)
        :param insureds_administrative_sex: Coded value for user-defined tables (id: IN1.43 | len: 1 | use: O | rpt: 1)
        :param insureds_employers_address: Extended Address (id: IN1.44 | len: 250 | use: O | rpt: *)
        :param verification_status: String Data (id: IN1.45 | len: 2 | use: O | rpt: 1)
        :param prior_insurance_plan_id: Coded value for user-defined tables (id: IN1.46 | len: 8 | use: O | rpt: 1)
        :param coverage_type: Coded value for user-defined tables (id: IN1.47 | len: 3 | use: O | rpt: 1)
        :param handicap: Coded value for user-defined tables (id: IN1.48 | len: 2 | use: O | rpt: 1)
        :param insureds_id_number: Extended Composite ID with Check Digit (id: IN1.49 | len: 250 | use: O | rpt: *)
        :param signature_code: Coded value for user-defined tables (id: IN1.50 | len: 1 | use: O | rpt: 1)
        :param signature_code_date: Date (id: IN1.51 | len: 8 | use: O | rpt: 1)
        :param insureds_birth_place: String Data (id: IN1.52 | len: 250 | use: O | rpt: 1)
        :param vip_indicator: Coded value for user-defined tables (id: IN1.53 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 53
        self.set_id_in1 = set_id_in1
        self.insurance_plan_id = insurance_plan_id
        self.insurance_company_id = insurance_company_id
        self.insurance_company_name = insurance_company_name
        self.insurance_company_address = insurance_company_address
        self.insurance_co_contact_person = insurance_co_contact_person
        self.insurance_co_phone_number = insurance_co_phone_number
        self.group_number = group_number
        self.group_name = group_name
        self.insureds_group_emp_id = insureds_group_emp_id
        self.insureds_group_emp_name = insureds_group_emp_name
        self.plan_effective_date = plan_effective_date
        self.plan_expiration_date = plan_expiration_date
        self.authorization_information = authorization_information
        self.plan_type = plan_type
        self.name_of_insured = name_of_insured
        self.insureds_relationship_to_patient = insureds_relationship_to_patient
        self.insureds_date_of_birth = insureds_date_of_birth
        self.insureds_address = insureds_address
        self.assignment_of_benefits = assignment_of_benefits
        self.coordination_of_benefits = coordination_of_benefits
        self.coord_of_ben_priority = coord_of_ben_priority
        self.notice_of_admission_flag = notice_of_admission_flag
        self.notice_of_admission_date = notice_of_admission_date
        self.report_of_eligibility_flag = report_of_eligibility_flag
        self.report_of_eligibility_date = report_of_eligibility_date
        self.release_information_code = release_information_code
        self.pre_admit_cert = pre_admit_cert
        self.verification_date_or_time = verification_date_or_time
        self.verification_by = verification_by
        self.type_of_agreement_code = type_of_agreement_code
        self.billing_status = billing_status
        self.lifetime_reserve_days = lifetime_reserve_days
        self.delay_before_l_r_day = delay_before_l_r_day
        self.company_plan_code = company_plan_code
        self.policy_number = policy_number
        self.policy_deductible = policy_deductible
        self.policy_limit_amount = policy_limit_amount
        self.policy_limit_days = policy_limit_days
        self.room_rate_semi_private = room_rate_semi_private
        self.room_rate_private = room_rate_private
        self.insureds_employment_status = insureds_employment_status
        self.insureds_administrative_sex = insureds_administrative_sex
        self.insureds_employers_address = insureds_employers_address
        self.verification_status = verification_status
        self.prior_insurance_plan_id = prior_insurance_plan_id
        self.coverage_type = coverage_type
        self.handicap = handicap
        self.insureds_id_number = insureds_id_number
        self.signature_code = signature_code
        self.signature_code_date = signature_code_date
        self.insureds_birth_place = insureds_birth_place
        self.vip_indicator = vip_indicator

    @property  # get IN1.1
    def set_id_in1(self) -> SI:
        """
        id: IN1.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.1
        """
        return self._c_data[0][0]

    @set_id_in1.setter  # set IN1.1
    def set_id_in1(self, si: SI):
        """
        id: IN1.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.1
        """
        self._c_data[0] = (si,)

    @property  # get IN1.2
    def insurance_plan_id(self) -> InsurancePlanId:
        """
        id: IN1.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.2
        """
        return self._c_data[1][0]

    @insurance_plan_id.setter  # set IN1.2
    def insurance_plan_id(self, insurance_plan_id: InsurancePlanId):
        """
        id: IN1.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.2
        """
        self._c_data[1] = (insurance_plan_id,)

    @property
    def insurance_company_id(self) -> tuple[CX, ...]:
        """
        id: IN1.3 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.3
        """
        return self._c_data[2]

    @insurance_company_id.setter  # set IN1.3
    def insurance_company_id(self, cx: CX | tuple[CX]):
        """
        id: IN1.3 | len: 250 | use: R | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.3
        """
        if isinstance(cx, tuple):
            self._c_data[2] = cx
        else:
            self._c_data[2] = (cx,)

    @property
    def insurance_company_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: IN1.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.4
        """
        return self._c_data[3]

    @insurance_company_name.setter  # set IN1.4
    def insurance_company_name(self, xon: XON | tuple[XON] | None):
        """
        id: IN1.4 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.4
        """
        if isinstance(xon, tuple):
            self._c_data[3] = xon
        else:
            self._c_data[3] = (xon,)

    @property
    def insurance_company_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: IN1.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.5
        """
        return self._c_data[4]

    @insurance_company_address.setter  # set IN1.5
    def insurance_company_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: IN1.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.5
        """
        if isinstance(xad, tuple):
            self._c_data[4] = xad
        else:
            self._c_data[4] = (xad,)

    @property
    def insurance_co_contact_person(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN1.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.6
        """
        return self._c_data[5]

    @insurance_co_contact_person.setter  # set IN1.6
    def insurance_co_contact_person(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN1.6 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.6
        """
        if isinstance(xpn, tuple):
            self._c_data[5] = xpn
        else:
            self._c_data[5] = (xpn,)

    @property
    def insurance_co_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: IN1.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.7
        """
        return self._c_data[6]

    @insurance_co_phone_number.setter  # set IN1.7
    def insurance_co_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: IN1.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.7
        """
        if isinstance(xtn, tuple):
            self._c_data[6] = xtn
        else:
            self._c_data[6] = (xtn,)

    @property  # get IN1.8
    def group_number(self) -> ST | None:
        """
        id: IN1.8 | len: 12 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.8
        """
        return self._c_data[7][0]

    @group_number.setter  # set IN1.8
    def group_number(self, st: ST | None):
        """
        id: IN1.8 | len: 12 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.8
        """
        self._c_data[7] = (st,)

    @property
    def group_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: IN1.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.9
        """
        return self._c_data[8]

    @group_name.setter  # set IN1.9
    def group_name(self, xon: XON | tuple[XON] | None):
        """
        id: IN1.9 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.9
        """
        if isinstance(xon, tuple):
            self._c_data[8] = xon
        else:
            self._c_data[8] = (xon,)

    @property
    def insureds_group_emp_id(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: IN1.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.10
        """
        return self._c_data[9]

    @insureds_group_emp_id.setter  # set IN1.10
    def insureds_group_emp_id(self, cx: CX | tuple[CX] | None):
        """
        id: IN1.10 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.10
        """
        if isinstance(cx, tuple):
            self._c_data[9] = cx
        else:
            self._c_data[9] = (cx,)

    @property
    def insureds_group_emp_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: IN1.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.11
        """
        return self._c_data[10]

    @insureds_group_emp_name.setter  # set IN1.11
    def insureds_group_emp_name(self, xon: XON | tuple[XON] | None):
        """
        id: IN1.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.11
        """
        if isinstance(xon, tuple):
            self._c_data[10] = xon
        else:
            self._c_data[10] = (xon,)

    @property  # get IN1.12
    def plan_effective_date(self) -> DT | None:
        """
        id: IN1.12 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.12
        """
        return self._c_data[11][0]

    @plan_effective_date.setter  # set IN1.12
    def plan_effective_date(self, dt: DT | None):
        """
        id: IN1.12 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.12
        """
        self._c_data[11] = (dt,)

    @property  # get IN1.13
    def plan_expiration_date(self) -> DT | None:
        """
        id: IN1.13 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.13
        """
        return self._c_data[12][0]

    @plan_expiration_date.setter  # set IN1.13
    def plan_expiration_date(self, dt: DT | None):
        """
        id: IN1.13 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.13
        """
        self._c_data[12] = (dt,)

    @property  # get IN1.14
    def authorization_information(self) -> AUI | None:
        """
        id: IN1.14 | len: 239 | use: O | rpt: 1
        ---
        return_type: AUI: Authorization Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.14
        """
        return self._c_data[13][0]

    @authorization_information.setter  # set IN1.14
    def authorization_information(self, aui: AUI | None):
        """
        id: IN1.14 | len: 239 | use: O | rpt: 1
        ---
        param_type: AUI: Authorization Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.14
        """
        self._c_data[13] = (aui,)

    @property  # get IN1.15
    def plan_type(self) -> PlanId | None:
        """
        id: IN1.15 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.15
        """
        return self._c_data[14][0]

    @plan_type.setter  # set IN1.15
    def plan_type(self, plan_id: PlanId | None):
        """
        id: IN1.15 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.15
        """
        self._c_data[14] = (plan_id,)

    @property
    def name_of_insured(self) -> tuple[XPN, ...] | tuple[None]:
        """
        id: IN1.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.16
        """
        return self._c_data[15]

    @name_of_insured.setter  # set IN1.16
    def name_of_insured(self, xpn: XPN | tuple[XPN] | None):
        """
        id: IN1.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XPN | tuple[XPN, ...]: (Extended Person Name, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.16
        """
        if isinstance(xpn, tuple):
            self._c_data[15] = xpn
        else:
            self._c_data[15] = (xpn,)

    @property  # get IN1.17
    def insureds_relationship_to_patient(self) -> Relationship | None:
        """
        id: IN1.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.17
        """
        return self._c_data[16][0]

    @insureds_relationship_to_patient.setter  # set IN1.17
    def insureds_relationship_to_patient(self, relationship: Relationship | None):
        """
        id: IN1.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.17
        """
        self._c_data[16] = (relationship,)

    @property  # get IN1.18
    def insureds_date_of_birth(self) -> TS | None:
        """
        id: IN1.18 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.18
        """
        return self._c_data[17][0]

    @insureds_date_of_birth.setter  # set IN1.18
    def insureds_date_of_birth(self, ts: TS | None):
        """
        id: IN1.18 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.18
        """
        self._c_data[17] = (ts,)

    @property
    def insureds_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: IN1.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.19
        """
        return self._c_data[18]

    @insureds_address.setter  # set IN1.19
    def insureds_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: IN1.19 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.19
        """
        if isinstance(xad, tuple):
            self._c_data[18] = xad
        else:
            self._c_data[18] = (xad,)

    @property  # get IN1.20
    def assignment_of_benefits(self) -> AssignmentOfBenefits | None:
        """
        id: IN1.20 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.20
        """
        return self._c_data[19][0]

    @assignment_of_benefits.setter  # set IN1.20
    def assignment_of_benefits(
        self, assignment_of_benefits: AssignmentOfBenefits | None
    ):
        """
        id: IN1.20 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.20
        """
        self._c_data[19] = (assignment_of_benefits,)

    @property  # get IN1.21
    def coordination_of_benefits(self) -> CoordinationOfBenefits | None:
        """
        id: IN1.21 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.21
        """
        return self._c_data[20][0]

    @coordination_of_benefits.setter  # set IN1.21
    def coordination_of_benefits(
        self, coordination_of_benefits: CoordinationOfBenefits | None
    ):
        """
        id: IN1.21 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.21
        """
        self._c_data[20] = (coordination_of_benefits,)

    @property  # get IN1.22
    def coord_of_ben_priority(self) -> ST | None:
        """
        id: IN1.22 | len: 2 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.22
        """
        return self._c_data[21][0]

    @coord_of_ben_priority.setter  # set IN1.22
    def coord_of_ben_priority(self, st: ST | None):
        """
        id: IN1.22 | len: 2 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.22
        """
        self._c_data[21] = (st,)

    @property  # get IN1.23
    def notice_of_admission_flag(self) -> YesOrNoIndicator | None:
        """
        id: IN1.23 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.23
        """
        return self._c_data[22][0]

    @notice_of_admission_flag.setter  # set IN1.23
    def notice_of_admission_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN1.23 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.23
        """
        self._c_data[22] = (yes_or_no_indicator,)

    @property  # get IN1.24
    def notice_of_admission_date(self) -> DT | None:
        """
        id: IN1.24 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.24
        """
        return self._c_data[23][0]

    @notice_of_admission_date.setter  # set IN1.24
    def notice_of_admission_date(self, dt: DT | None):
        """
        id: IN1.24 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.24
        """
        self._c_data[23] = (dt,)

    @property  # get IN1.25
    def report_of_eligibility_flag(self) -> YesOrNoIndicator | None:
        """
        id: IN1.25 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.25
        """
        return self._c_data[24][0]

    @report_of_eligibility_flag.setter  # set IN1.25
    def report_of_eligibility_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: IN1.25 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.25
        """
        self._c_data[24] = (yes_or_no_indicator,)

    @property  # get IN1.26
    def report_of_eligibility_date(self) -> DT | None:
        """
        id: IN1.26 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.26
        """
        return self._c_data[25][0]

    @report_of_eligibility_date.setter  # set IN1.26
    def report_of_eligibility_date(self, dt: DT | None):
        """
        id: IN1.26 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.26
        """
        self._c_data[25] = (dt,)

    @property  # get IN1.27
    def release_information_code(self) -> ReleaseInformation | None:
        """
        id: IN1.27 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.27
        """
        return self._c_data[26][0]

    @release_information_code.setter  # set IN1.27
    def release_information_code(self, release_information: ReleaseInformation | None):
        """
        id: IN1.27 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.27
        """
        self._c_data[26] = (release_information,)

    @property  # get IN1.28
    def pre_admit_cert(self) -> ST | None:
        """
        id: IN1.28 | len: 15 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.28
        """
        return self._c_data[27][0]

    @pre_admit_cert.setter  # set IN1.28
    def pre_admit_cert(self, st: ST | None):
        """
        id: IN1.28 | len: 15 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.28
        """
        self._c_data[27] = (st,)

    @property  # get IN1.29
    def verification_date_or_time(self) -> TS | None:
        """
        id: IN1.29 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.29
        """
        return self._c_data[28][0]

    @verification_date_or_time.setter  # set IN1.29
    def verification_date_or_time(self, ts: TS | None):
        """
        id: IN1.29 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.29
        """
        self._c_data[28] = (ts,)

    @property
    def verification_by(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: IN1.30 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.30
        """
        return self._c_data[29]

    @verification_by.setter  # set IN1.30
    def verification_by(self, xcn: XCN | tuple[XCN] | None):
        """
        id: IN1.30 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.30
        """
        if isinstance(xcn, tuple):
            self._c_data[29] = xcn
        else:
            self._c_data[29] = (xcn,)

    @property  # get IN1.31
    def type_of_agreement_code(self) -> TypeOfAgreement | None:
        """
        id: IN1.31 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.31
        """
        return self._c_data[30][0]

    @type_of_agreement_code.setter  # set IN1.31
    def type_of_agreement_code(self, type_of_agreement: TypeOfAgreement | None):
        """
        id: IN1.31 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.31
        """
        self._c_data[30] = (type_of_agreement,)

    @property  # get IN1.32
    def billing_status(self) -> BillingStatus | None:
        """
        id: IN1.32 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.32
        """
        return self._c_data[31][0]

    @billing_status.setter  # set IN1.32
    def billing_status(self, billing_status: BillingStatus | None):
        """
        id: IN1.32 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.32
        """
        self._c_data[31] = (billing_status,)

    @property  # get IN1.33
    def lifetime_reserve_days(self) -> NM | None:
        """
        id: IN1.33 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.33
        """
        return self._c_data[32][0]

    @lifetime_reserve_days.setter  # set IN1.33
    def lifetime_reserve_days(self, nm: NM | None):
        """
        id: IN1.33 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.33
        """
        self._c_data[32] = (nm,)

    @property  # get IN1.34
    def delay_before_l_r_day(self) -> NM | None:
        """
        id: IN1.34 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.34
        """
        return self._c_data[33][0]

    @delay_before_l_r_day.setter  # set IN1.34
    def delay_before_l_r_day(self, nm: NM | None):
        """
        id: IN1.34 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.34
        """
        self._c_data[33] = (nm,)

    @property  # get IN1.35
    def company_plan_code(self) -> CompanyPlanCode | None:
        """
        id: IN1.35 | len: 8 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.35
        """
        return self._c_data[34][0]

    @company_plan_code.setter  # set IN1.35
    def company_plan_code(self, company_plan_code: CompanyPlanCode | None):
        """
        id: IN1.35 | len: 8 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.35
        """
        self._c_data[34] = (company_plan_code,)

    @property  # get IN1.36
    def policy_number(self) -> ST | None:
        """
        id: IN1.36 | len: 15 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.36
        """
        return self._c_data[35][0]

    @policy_number.setter  # set IN1.36
    def policy_number(self, st: ST | None):
        """
        id: IN1.36 | len: 15 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.36
        """
        self._c_data[35] = (st,)

    @property  # get IN1.37
    def policy_deductible(self) -> CP | None:
        """
        id: IN1.37 | len: 12 | use: O | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.37
        """
        return self._c_data[36][0]

    @policy_deductible.setter  # set IN1.37
    def policy_deductible(self, cp: CP | None):
        """
        id: IN1.37 | len: 12 | use: O | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.37
        """
        self._c_data[36] = (cp,)

    @property  # get IN1.38
    def policy_limit_amount(self) -> CP | None:
        """
        id: IN1.38 | len: 12 | use: B | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.38
        """
        return self._c_data[37][0]

    @policy_limit_amount.setter  # set IN1.38
    def policy_limit_amount(self, cp: CP | None):
        """
        id: IN1.38 | len: 12 | use: B | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.38
        """
        self._c_data[37] = (cp,)

    @property  # get IN1.39
    def policy_limit_days(self) -> NM | None:
        """
        id: IN1.39 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.39
        """
        return self._c_data[38][0]

    @policy_limit_days.setter  # set IN1.39
    def policy_limit_days(self, nm: NM | None):
        """
        id: IN1.39 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.39
        """
        self._c_data[38] = (nm,)

    @property  # get IN1.40
    def room_rate_semi_private(self) -> CP | None:
        """
        id: IN1.40 | len: 12 | use: B | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.40
        """
        return self._c_data[39][0]

    @room_rate_semi_private.setter  # set IN1.40
    def room_rate_semi_private(self, cp: CP | None):
        """
        id: IN1.40 | len: 12 | use: B | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.40
        """
        self._c_data[39] = (cp,)

    @property  # get IN1.41
    def room_rate_private(self) -> CP | None:
        """
        id: IN1.41 | len: 12 | use: B | rpt: 1
        ---
        return_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.41
        """
        return self._c_data[40][0]

    @room_rate_private.setter  # set IN1.41
    def room_rate_private(self, cp: CP | None):
        """
        id: IN1.41 | len: 12 | use: B | rpt: 1
        ---
        param_type: CP: Composite Price
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.41
        """
        self._c_data[40] = (cp,)

    @property  # get IN1.42
    def insureds_employment_status(self) -> EmploymentStatus | None:
        """
        id: IN1.42 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.42
        """
        return self._c_data[41][0]

    @insureds_employment_status.setter  # set IN1.42
    def insureds_employment_status(self, employment_status: EmploymentStatus | None):
        """
        id: IN1.42 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.42
        """
        self._c_data[41] = (employment_status,)

    @property  # get IN1.43
    def insureds_administrative_sex(self) -> AdministrativeSex | None:
        """
        id: IN1.43 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.43
        """
        return self._c_data[42][0]

    @insureds_administrative_sex.setter  # set IN1.43
    def insureds_administrative_sex(self, administrative_sex: AdministrativeSex | None):
        """
        id: IN1.43 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.43
        """
        self._c_data[42] = (administrative_sex,)

    @property
    def insureds_employers_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: IN1.44 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.44
        """
        return self._c_data[43]

    @insureds_employers_address.setter  # set IN1.44
    def insureds_employers_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: IN1.44 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.44
        """
        if isinstance(xad, tuple):
            self._c_data[43] = xad
        else:
            self._c_data[43] = (xad,)

    @property  # get IN1.45
    def verification_status(self) -> ST | None:
        """
        id: IN1.45 | len: 2 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.45
        """
        return self._c_data[44][0]

    @verification_status.setter  # set IN1.45
    def verification_status(self, st: ST | None):
        """
        id: IN1.45 | len: 2 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.45
        """
        self._c_data[44] = (st,)

    @property  # get IN1.46
    def prior_insurance_plan_id(self) -> InsurancePlanId | None:
        """
        id: IN1.46 | len: 8 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.46
        """
        return self._c_data[45][0]

    @prior_insurance_plan_id.setter  # set IN1.46
    def prior_insurance_plan_id(self, insurance_plan_id: InsurancePlanId | None):
        """
        id: IN1.46 | len: 8 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.46
        """
        self._c_data[45] = (insurance_plan_id,)

    @property  # get IN1.47
    def coverage_type(self) -> CoverageType | None:
        """
        id: IN1.47 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.47
        """
        return self._c_data[46][0]

    @coverage_type.setter  # set IN1.47
    def coverage_type(self, coverage_type: CoverageType | None):
        """
        id: IN1.47 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.47
        """
        self._c_data[46] = (coverage_type,)

    @property  # get IN1.48
    def handicap(self) -> Handicap | None:
        """
        id: IN1.48 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.48
        """
        return self._c_data[47][0]

    @handicap.setter  # set IN1.48
    def handicap(self, handicap: Handicap | None):
        """
        id: IN1.48 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.48
        """
        self._c_data[47] = (handicap,)

    @property
    def insureds_id_number(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: IN1.49 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.49
        """
        return self._c_data[48]

    @insureds_id_number.setter  # set IN1.49
    def insureds_id_number(self, cx: CX | tuple[CX] | None):
        """
        id: IN1.49 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.49
        """
        if isinstance(cx, tuple):
            self._c_data[48] = cx
        else:
            self._c_data[48] = (cx,)

    @property  # get IN1.50
    def signature_code(self) -> SignatureCode | None:
        """
        id: IN1.50 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.50
        """
        return self._c_data[49][0]

    @signature_code.setter  # set IN1.50
    def signature_code(self, signature_code: SignatureCode | None):
        """
        id: IN1.50 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.50
        """
        self._c_data[49] = (signature_code,)

    @property  # get IN1.51
    def signature_code_date(self) -> DT | None:
        """
        id: IN1.51 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.51
        """
        return self._c_data[50][0]

    @signature_code_date.setter  # set IN1.51
    def signature_code_date(self, dt: DT | None):
        """
        id: IN1.51 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.51
        """
        self._c_data[50] = (dt,)

    @property  # get IN1.52
    def insureds_birth_place(self) -> ST | None:
        """
        id: IN1.52 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.52
        """
        return self._c_data[51][0]

    @insureds_birth_place.setter  # set IN1.52
    def insureds_birth_place(self, st: ST | None):
        """
        id: IN1.52 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.52
        """
        self._c_data[51] = (st,)

    @property  # get IN1.53
    def vip_indicator(self) -> VipIndicator | None:
        """
        id: IN1.53 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.53
        """
        return self._c_data[52][0]

    @vip_indicator.setter  # set IN1.53
    def vip_indicator(self, vip_indicator: VipIndicator | None):
        """
        id: IN1.53 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IN1.53
        """
        self._c_data[52] = (vip_indicator,)
