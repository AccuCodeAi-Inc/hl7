from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.IS import IS
from ..data_types.CX import CX
from ..data_types.DT import DT
from ..data_types.NM import NM
from ..data_types.XCN import XCN
from ..data_types.FC import FC
from ..data_types.DLD import DLD
from ..data_types.SI import SI
from ..data_types.PL import PL
from ..data_types.TS import TS
from ..tables.AdmitSource import AdmitSource
from ..tables.AdmissionType import AdmissionType
from ..tables.AmbulatoryStatus import AmbulatoryStatus
from ..tables.ChargeOrPriceIndicator import ChargeOrPriceIndicator
from ..tables.BadDebtAgencyCode import BadDebtAgencyCode
from ..tables.PatientClass import PatientClass
from ..tables.AccountStatus import AccountStatus
from ..tables.ContractCode import ContractCode
from ..tables.BedStatus import BedStatus
from ..tables.TransferToBadDebtCode import TransferToBadDebtCode
from ..tables.VipIndicator import VipIndicator
from ..tables.VisitIndicator import VisitIndicator
from ..tables.DischargeDisposition import DischargeDisposition
from ..tables.InterestRateCode import InterestRateCode
from ..tables.PhysicianId import PhysicianId
from ..tables.CourtesyCode import CourtesyCode
from ..tables.DietType import DietType
from ..tables.PreAdmitTestIndicator import PreAdmitTestIndicator
from ..tables.ReAdmissionIndicator import ReAdmissionIndicator
from ..tables.HospitalService import HospitalService
from ..tables.DeleteAccountCode import DeleteAccountCode
from ..tables.CreditRating import CreditRating
from ..tables.PatientType import PatientType
from ..tables.ServicingFacility import ServicingFacility


"""
Patient Visit - PV1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PV1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PV1,
    CE, IS, CX, DT, NM, XCN, FC, DLD, SI, PL, TS
)

pv1 = PV1(  #  - The PV1 segment is used by Registration/Patient Administration applications to communicate information on an account or visit-specific basis
    set_id_pv1=None,  # SI(...) 
    patient_class=_is,  # IS(...)  # Required.
    assigned_patient_location=None,  # PL(...) 
    admission_type=None,  # IS(...) 
    preadmit_number=None,  # CX(...) 
    prior_patient_location=None,  # PL(...) 
    attending_doctor=None,  # XCN(...) 
    referring_doctor=None,  # XCN(...) 
    consulting_doctor=None,  # XCN(...) 
    hospital_service=None,  # IS(...) 
    temporary_location=None,  # PL(...) 
    preadmit_test_indicator=None,  # IS(...) 
    re_admission_indicator=None,  # IS(...) 
    admit_source=None,  # IS(...) 
    ambulatory_status=None,  # IS(...) 
    vip_indicator=None,  # IS(...) 
    admitting_doctor=None,  # XCN(...) 
    patient_type=None,  # IS(...) 
    visit_number=None,  # CX(...) 
    financial_class=None,  # FC(...) 
    charge_price_indicator=None,  # IS(...) 
    courtesy_code=None,  # IS(...) 
    credit_rating=None,  # IS(...) 
    contract_code=None,  # IS(...) 
    contract_effective_date=None,  # DT(...) 
    contract_amount=None,  # NM(...) 
    contract_period=None,  # NM(...) 
    interest_code=None,  # IS(...) 
    transfer_to_bad_debt_code=None,  # IS(...) 
    transfer_to_bad_debt_date=None,  # DT(...) 
    bad_debt_agency_code=None,  # IS(...) 
    bad_debt_transfer_amount=None,  # NM(...) 
    bad_debt_recovery_amount=None,  # NM(...) 
    delete_account_indicator=None,  # IS(...) 
    delete_account_date=None,  # DT(...) 
    discharge_disposition=None,  # IS(...) 
    discharged_to_location=None,  # DLD(...) 
    diet_type=None,  # CE(...) 
    servicing_facility=None,  # IS(...) 
    bed_status=None,  # IS(...) 
    account_status=None,  # IS(...) 
    pending_location=None,  # PL(...) 
    prior_temporary_location=None,  # PL(...) 
    admit_date_or_time=None,  # TS(...) 
    discharge_date_or_time=None,  # TS(...) 
    current_patient_balance=None,  # NM(...) 
    total_charges=None,  # NM(...) 
    total_adjustments=None,  # NM(...) 
    total_payments=None,  # NM(...) 
    alternate_visit_id=None,  # CX(...) 
    visit_indicator=None,  # IS(...) 
    other_healthcare_provider=None,  # XCN(...) 
)

-----END SEGMENT::PV1 TEMPLATE-----
"""


class PV1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PV1"""
    _hl7_name = """Patient Visit"""
    _hl7_description = """The PV1 segment is used by Registration/Patient Administration applications to communicate information on an account or visit-specific basis"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1"
    _c_length = (4, 1, 80, 2, 250, 80, 250, 250, 250, 3, 80, 2, 2, 6, 2, 2, 250, 2, 250, 50, 2, 2, 2, 2, 8, 12, 3, 2, 4, 8, 10, 12, 12, 1, 8, 3, 47, 250, 2, 1, 2, 80, 80, 26, 26, 12, 12, 12, 12, 250, 1, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 65535, 65535, 65535, 1, 1, 1, 1, 1, 65535, 1, 65535, 1, 1, 65535, 1, 1, 1, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 65535,)
    _c_usage = ("O", "R", "O", "O", "O", "O", "O", "O", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B",)
    _c_components = (SI, IS, PL, IS, CX, PL, XCN, XCN, XCN, IS, PL, IS, IS, IS, IS, IS, XCN, IS, CX, FC, IS, IS, IS, IS, DT, NM, NM, IS, IS, DT, IS, NM, NM, IS, DT, IS, DLD, CE, IS, IS, IS, PL, PL, TS, TS, NM, NM, NM, NM, CX, IS, XCN,)
    _c_aliases = ("PV1.1", "PV1.2", "PV1.3", "PV1.4", "PV1.5", "PV1.6", "PV1.7", "PV1.8", "PV1.9", "PV1.10", "PV1.11", "PV1.12", "PV1.13", "PV1.14", "PV1.15", "PV1.16", "PV1.17", "PV1.18", "PV1.19", "PV1.20", "PV1.21", "PV1.22", "PV1.23", "PV1.24", "PV1.25", "PV1.26", "PV1.27", "PV1.28", "PV1.29", "PV1.30", "PV1.31", "PV1.32", "PV1.33", "PV1.34", "PV1.35", "PV1.36", "PV1.37", "PV1.38", "PV1.39", "PV1.40", "PV1.41", "PV1.42", "PV1.43", "PV1.44", "PV1.45", "PV1.46", "PV1.47", "PV1.48", "PV1.49", "PV1.50", "PV1.51", "PV1.52",)
    _c_names = ("Set ID - PV1", "Patient Class", "Assigned Patient Location", "Admission Type", "Preadmit Number", "Prior Patient Location", "Attending Doctor", "Referring Doctor", "Consulting Doctor", "Hospital Service", "Temporary Location", "Preadmit Test Indicator", "Re-admission Indicator", "Admit Source", "Ambulatory Status", "VIP Indicator", "Admitting Doctor", "Patient Type", "Visit Number", "Financial Class", "Charge Price Indicator", "Courtesy Code", "Credit Rating", "Contract Code", "Contract Effective Date", "Contract Amount", "Contract Period", "Interest Code", "Transfer to Bad Debt Code", "Transfer to Bad Debt Date", "Bad Debt Agency Code", "Bad Debt Transfer Amount", "Bad Debt Recovery Amount", "Delete Account Indicator", "Delete Account Date", "Discharge Disposition", "Discharged to Location", "Diet Type", "Servicing Facility", "Bed Status", "Account Status", "Pending Location", "Prior Temporary Location", "Admit Date/Time", "Discharge Date/Time", "Current Patient Balance", "Total Charges", "Total Adjustments", "Total Payments", "Alternate Visit ID", "Visit Indicator", "Other Healthcare Provider",)
    _c_attrs = ("set_id_pv1", "patient_class", "assigned_patient_location", "admission_type", "preadmit_number", "prior_patient_location", "attending_doctor", "referring_doctor", "consulting_doctor", "hospital_service", "temporary_location", "preadmit_test_indicator", "re_admission_indicator", "admit_source", "ambulatory_status", "vip_indicator", "admitting_doctor", "patient_type", "visit_number", "financial_class", "charge_price_indicator", "courtesy_code", "credit_rating", "contract_code", "contract_effective_date", "contract_amount", "contract_period", "interest_code", "transfer_to_bad_debt_code", "transfer_to_bad_debt_date", "bad_debt_agency_code", "bad_debt_transfer_amount", "bad_debt_recovery_amount", "delete_account_indicator", "delete_account_date", "discharge_disposition", "discharged_to_location", "diet_type", "servicing_facility", "bed_status", "account_status", "pending_location", "prior_temporary_location", "admit_date_or_time", "discharge_date_or_time", "current_patient_balance", "total_charges", "total_adjustments", "total_payments", "alternate_visit_id", "visit_indicator", "other_healthcare_provider",)
    # fmt: on

    def __init__(
        self,
        patient_class: PatientClass | IS,  # PV1.2
        set_id_pv1: SI | None = None,  # PV1.1
        assigned_patient_location: PL | None = None,  # PV1.3
        admission_type: AdmissionType | IS | None = None,  # PV1.4
        preadmit_number: CX | None = None,  # PV1.5
        prior_patient_location: PL | None = None,  # PV1.6
        attending_doctor: PhysicianId | XCN | None = None,  # PV1.7
        referring_doctor: PhysicianId | XCN | None = None,  # PV1.8
        consulting_doctor: PhysicianId | XCN | None = None,  # PV1.9
        hospital_service: HospitalService | IS | None = None,  # PV1.10
        temporary_location: PL | None = None,  # PV1.11
        preadmit_test_indicator: PreAdmitTestIndicator | IS | None = None,  # PV1.12
        re_admission_indicator: ReAdmissionIndicator | IS | None = None,  # PV1.13
        admit_source: AdmitSource | IS | None = None,  # PV1.14
        ambulatory_status: AmbulatoryStatus | IS | None = None,  # PV1.15
        vip_indicator: VipIndicator | IS | None = None,  # PV1.16
        admitting_doctor: PhysicianId | XCN | None = None,  # PV1.17
        patient_type: PatientType | IS | None = None,  # PV1.18
        visit_number: CX | None = None,  # PV1.19
        financial_class: FC | None = None,  # PV1.20
        charge_price_indicator: ChargeOrPriceIndicator | IS | None = None,  # PV1.21
        courtesy_code: CourtesyCode | IS | None = None,  # PV1.22
        credit_rating: CreditRating | IS | None = None,  # PV1.23
        contract_code: ContractCode | IS | None = None,  # PV1.24
        contract_effective_date: DT | None = None,  # PV1.25
        contract_amount: NM | None = None,  # PV1.26
        contract_period: NM | None = None,  # PV1.27
        interest_code: InterestRateCode | IS | None = None,  # PV1.28
        transfer_to_bad_debt_code: TransferToBadDebtCode | IS | None = None,  # PV1.29
        transfer_to_bad_debt_date: DT | None = None,  # PV1.30
        bad_debt_agency_code: BadDebtAgencyCode | IS | None = None,  # PV1.31
        bad_debt_transfer_amount: NM | None = None,  # PV1.32
        bad_debt_recovery_amount: NM | None = None,  # PV1.33
        delete_account_indicator: DeleteAccountCode | IS | None = None,  # PV1.34
        delete_account_date: DT | None = None,  # PV1.35
        discharge_disposition: DischargeDisposition | IS | None = None,  # PV1.36
        discharged_to_location: DLD | None = None,  # PV1.37
        diet_type: DietType | CE | None = None,  # PV1.38
        servicing_facility: ServicingFacility | IS | None = None,  # PV1.39
        bed_status: BedStatus | IS | None = None,  # PV1.40
        account_status: AccountStatus | IS | None = None,  # PV1.41
        pending_location: PL | None = None,  # PV1.42
        prior_temporary_location: PL | None = None,  # PV1.43
        admit_date_or_time: TS | None = None,  # PV1.44
        discharge_date_or_time: TS | None = None,  # PV1.45
        current_patient_balance: NM | None = None,  # PV1.46
        total_charges: NM | None = None,  # PV1.47
        total_adjustments: NM | None = None,  # PV1.48
        total_payments: NM | None = None,  # PV1.49
        alternate_visit_id: CX | None = None,  # PV1.50
        visit_indicator: VisitIndicator | IS | None = None,  # PV1.51
        other_healthcare_provider: PhysicianId | XCN | None = None,  # PV1.52
    ):
        """
        Patient Visit - `PV1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1>`_
        The PV1 segment is used by Registration/Patient Administration applications to communicate information on an account or visit-specific basis. The default is to send account level data. To use this segment for visit level data PV1-51 - Visit Indicator must be valued to V. The value of PV-51 affects the level of data being sent on the PV1, PV2, and any other segments that are part of the associated PV1 hierarchy (e.g. ROL, DG1, or OBX).

        :param set_id_pv1: Sequence ID (id: PV1.1 | len: 4 | use: O | rpt: 1)
        :param patient_class: Coded value for user-defined tables (id: PV1.2 | len: 1 | use: R | rpt: 1)
        :param assigned_patient_location: Person Location (id: PV1.3 | len: 80 | use: O | rpt: 1)
        :param admission_type: Coded value for user-defined tables (id: PV1.4 | len: 2 | use: O | rpt: 1)
        :param preadmit_number: Extended Composite ID with Check Digit (id: PV1.5 | len: 250 | use: O | rpt: 1)
        :param prior_patient_location: Person Location (id: PV1.6 | len: 80 | use: O | rpt: 1)
        :param attending_doctor: Extended Composite ID Number and Name for Persons (id: PV1.7 | len: 250 | use: O | rpt: *)
        :param referring_doctor: Extended Composite ID Number and Name for Persons (id: PV1.8 | len: 250 | use: O | rpt: *)
        :param consulting_doctor: Extended Composite ID Number and Name for Persons (id: PV1.9 | len: 250 | use: B | rpt: *)
        :param hospital_service: Coded value for user-defined tables (id: PV1.10 | len: 3 | use: O | rpt: 1)
        :param temporary_location: Person Location (id: PV1.11 | len: 80 | use: O | rpt: 1)
        :param preadmit_test_indicator: Coded value for user-defined tables (id: PV1.12 | len: 2 | use: O | rpt: 1)
        :param re_admission_indicator: Coded value for user-defined tables (id: PV1.13 | len: 2 | use: O | rpt: 1)
        :param admit_source: Coded value for user-defined tables (id: PV1.14 | len: 6 | use: O | rpt: 1)
        :param ambulatory_status: Coded value for user-defined tables (id: PV1.15 | len: 2 | use: O | rpt: *)
        :param vip_indicator: Coded value for user-defined tables (id: PV1.16 | len: 2 | use: O | rpt: 1)
        :param admitting_doctor: Extended Composite ID Number and Name for Persons (id: PV1.17 | len: 250 | use: O | rpt: *)
        :param patient_type: Coded value for user-defined tables (id: PV1.18 | len: 2 | use: O | rpt: 1)
        :param visit_number: Extended Composite ID with Check Digit (id: PV1.19 | len: 250 | use: O | rpt: 1)
        :param financial_class: Financial Class (id: PV1.20 | len: 50 | use: O | rpt: *)
        :param charge_price_indicator: Coded value for user-defined tables (id: PV1.21 | len: 2 | use: O | rpt: 1)
        :param courtesy_code: Coded value for user-defined tables (id: PV1.22 | len: 2 | use: O | rpt: 1)
        :param credit_rating: Coded value for user-defined tables (id: PV1.23 | len: 2 | use: O | rpt: 1)
        :param contract_code: Coded value for user-defined tables (id: PV1.24 | len: 2 | use: O | rpt: *)
        :param contract_effective_date: Date (id: PV1.25 | len: 8 | use: O | rpt: *)
        :param contract_amount: Numeric (id: PV1.26 | len: 12 | use: O | rpt: *)
        :param contract_period: Numeric (id: PV1.27 | len: 3 | use: O | rpt: *)
        :param interest_code: Coded value for user-defined tables (id: PV1.28 | len: 2 | use: O | rpt: 1)
        :param transfer_to_bad_debt_code: Coded value for user-defined tables (id: PV1.29 | len: 4 | use: O | rpt: 1)
        :param transfer_to_bad_debt_date: Date (id: PV1.30 | len: 8 | use: O | rpt: 1)
        :param bad_debt_agency_code: Coded value for user-defined tables (id: PV1.31 | len: 10 | use: O | rpt: 1)
        :param bad_debt_transfer_amount: Numeric (id: PV1.32 | len: 12 | use: O | rpt: 1)
        :param bad_debt_recovery_amount: Numeric (id: PV1.33 | len: 12 | use: O | rpt: 1)
        :param delete_account_indicator: Coded value for user-defined tables (id: PV1.34 | len: 1 | use: O | rpt: 1)
        :param delete_account_date: Date (id: PV1.35 | len: 8 | use: O | rpt: 1)
        :param discharge_disposition: Coded value for user-defined tables (id: PV1.36 | len: 3 | use: O | rpt: 1)
        :param discharged_to_location: Discharge Location and Date (id: PV1.37 | len: 47 | use: O | rpt: 1)
        :param diet_type: Coded Element (id: PV1.38 | len: 250 | use: O | rpt: 1)
        :param servicing_facility: Coded value for user-defined tables (id: PV1.39 | len: 2 | use: O | rpt: 1)
        :param bed_status: Coded value for user-defined tables (id: PV1.40 | len: 1 | use: B | rpt: 1)
        :param account_status: Coded value for user-defined tables (id: PV1.41 | len: 2 | use: O | rpt: 1)
        :param pending_location: Person Location (id: PV1.42 | len: 80 | use: O | rpt: 1)
        :param prior_temporary_location: Person Location (id: PV1.43 | len: 80 | use: O | rpt: 1)
        :param admit_date_or_time: Time Stamp (id: PV1.44 | len: 26 | use: O | rpt: 1)
        :param discharge_date_or_time: Time Stamp (id: PV1.45 | len: 26 | use: O | rpt: *)
        :param current_patient_balance: Numeric (id: PV1.46 | len: 12 | use: O | rpt: 1)
        :param total_charges: Numeric (id: PV1.47 | len: 12 | use: O | rpt: 1)
        :param total_adjustments: Numeric (id: PV1.48 | len: 12 | use: O | rpt: 1)
        :param total_payments: Numeric (id: PV1.49 | len: 12 | use: O | rpt: 1)
        :param alternate_visit_id: Extended Composite ID with Check Digit (id: PV1.50 | len: 250 | use: O | rpt: 1)
        :param visit_indicator: Coded value for user-defined tables (id: PV1.51 | len: 1 | use: O | rpt: 1)
        :param other_healthcare_provider: Extended Composite ID Number and Name for Persons (id: PV1.52 | len: 250 | use: B | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 52
        self.set_id_pv1 = set_id_pv1
        self.patient_class = patient_class
        self.assigned_patient_location = assigned_patient_location
        self.admission_type = admission_type
        self.preadmit_number = preadmit_number
        self.prior_patient_location = prior_patient_location
        self.attending_doctor = attending_doctor
        self.referring_doctor = referring_doctor
        self.consulting_doctor = consulting_doctor
        self.hospital_service = hospital_service
        self.temporary_location = temporary_location
        self.preadmit_test_indicator = preadmit_test_indicator
        self.re_admission_indicator = re_admission_indicator
        self.admit_source = admit_source
        self.ambulatory_status = ambulatory_status
        self.vip_indicator = vip_indicator
        self.admitting_doctor = admitting_doctor
        self.patient_type = patient_type
        self.visit_number = visit_number
        self.financial_class = financial_class
        self.charge_price_indicator = charge_price_indicator
        self.courtesy_code = courtesy_code
        self.credit_rating = credit_rating
        self.contract_code = contract_code
        self.contract_effective_date = contract_effective_date
        self.contract_amount = contract_amount
        self.contract_period = contract_period
        self.interest_code = interest_code
        self.transfer_to_bad_debt_code = transfer_to_bad_debt_code
        self.transfer_to_bad_debt_date = transfer_to_bad_debt_date
        self.bad_debt_agency_code = bad_debt_agency_code
        self.bad_debt_transfer_amount = bad_debt_transfer_amount
        self.bad_debt_recovery_amount = bad_debt_recovery_amount
        self.delete_account_indicator = delete_account_indicator
        self.delete_account_date = delete_account_date
        self.discharge_disposition = discharge_disposition
        self.discharged_to_location = discharged_to_location
        self.diet_type = diet_type
        self.servicing_facility = servicing_facility
        self.bed_status = bed_status
        self.account_status = account_status
        self.pending_location = pending_location
        self.prior_temporary_location = prior_temporary_location
        self.admit_date_or_time = admit_date_or_time
        self.discharge_date_or_time = discharge_date_or_time
        self.current_patient_balance = current_patient_balance
        self.total_charges = total_charges
        self.total_adjustments = total_adjustments
        self.total_payments = total_payments
        self.alternate_visit_id = alternate_visit_id
        self.visit_indicator = visit_indicator
        self.other_healthcare_provider = other_healthcare_provider

    @property  # get PV1.1
    def set_id_pv1(self) -> SI | None:
        """
        id: PV1.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.1
        """
        return self._c_data[0][0]

    @set_id_pv1.setter  # set PV1.1
    def set_id_pv1(self, si: SI | None):
        """
        id: PV1.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.1
        """
        self._c_data[0] = (si,)

    @property  # get PV1.2
    def patient_class(self) -> PatientClass:
        """
        id: PV1.2 | len: 1 | use: R | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.2
        """
        return self._c_data[1][0]

    @patient_class.setter  # set PV1.2
    def patient_class(self, patient_class: PatientClass):
        """
        id: PV1.2 | len: 1 | use: R | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.2
        """
        self._c_data[1] = (patient_class,)

    @property  # get PV1.3
    def assigned_patient_location(self) -> PL | None:
        """
        id: PV1.3 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.3
        """
        return self._c_data[2][0]

    @assigned_patient_location.setter  # set PV1.3
    def assigned_patient_location(self, pl: PL | None):
        """
        id: PV1.3 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.3
        """
        self._c_data[2] = (pl,)

    @property  # get PV1.4
    def admission_type(self) -> AdmissionType | None:
        """
        id: PV1.4 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.4
        """
        return self._c_data[3][0]

    @admission_type.setter  # set PV1.4
    def admission_type(self, admission_type: AdmissionType | None):
        """
        id: PV1.4 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.4
        """
        self._c_data[3] = (admission_type,)

    @property  # get PV1.5
    def preadmit_number(self) -> CX | None:
        """
        id: PV1.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.5
        """
        return self._c_data[4][0]

    @preadmit_number.setter  # set PV1.5
    def preadmit_number(self, cx: CX | None):
        """
        id: PV1.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.5
        """
        self._c_data[4] = (cx,)

    @property  # get PV1.6
    def prior_patient_location(self) -> PL | None:
        """
        id: PV1.6 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.6
        """
        return self._c_data[5][0]

    @prior_patient_location.setter  # set PV1.6
    def prior_patient_location(self, pl: PL | None):
        """
        id: PV1.6 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.6
        """
        self._c_data[5] = (pl,)

    @property
    def attending_doctor(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PV1.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.7
        """
        return self._c_data[6]

    @attending_doctor.setter  # set PV1.7
    def attending_doctor(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: PV1.7 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.7
        """
        if isinstance(physician_id, tuple):
            self._c_data[6] = physician_id
        else:
            self._c_data[6] = (physician_id,)

    @property
    def referring_doctor(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PV1.8 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.8
        """
        return self._c_data[7]

    @referring_doctor.setter  # set PV1.8
    def referring_doctor(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: PV1.8 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.8
        """
        if isinstance(physician_id, tuple):
            self._c_data[7] = physician_id
        else:
            self._c_data[7] = (physician_id,)

    @property
    def consulting_doctor(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PV1.9 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.9
        """
        return self._c_data[8]

    @consulting_doctor.setter  # set PV1.9
    def consulting_doctor(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: PV1.9 | len: 250 | use: B | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.9
        """
        if isinstance(physician_id, tuple):
            self._c_data[8] = physician_id
        else:
            self._c_data[8] = (physician_id,)

    @property  # get PV1.10
    def hospital_service(self) -> HospitalService | None:
        """
        id: PV1.10 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.10
        """
        return self._c_data[9][0]

    @hospital_service.setter  # set PV1.10
    def hospital_service(self, hospital_service: HospitalService | None):
        """
        id: PV1.10 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.10
        """
        self._c_data[9] = (hospital_service,)

    @property  # get PV1.11
    def temporary_location(self) -> PL | None:
        """
        id: PV1.11 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.11
        """
        return self._c_data[10][0]

    @temporary_location.setter  # set PV1.11
    def temporary_location(self, pl: PL | None):
        """
        id: PV1.11 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.11
        """
        self._c_data[10] = (pl,)

    @property  # get PV1.12
    def preadmit_test_indicator(self) -> PreAdmitTestIndicator | None:
        """
        id: PV1.12 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.12
        """
        return self._c_data[11][0]

    @preadmit_test_indicator.setter  # set PV1.12
    def preadmit_test_indicator(
        self, preadmit_test_indicator: PreAdmitTestIndicator | None
    ):
        """
        id: PV1.12 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.12
        """
        self._c_data[11] = (preadmit_test_indicator,)

    @property  # get PV1.13
    def re_admission_indicator(self) -> ReAdmissionIndicator | None:
        """
        id: PV1.13 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.13
        """
        return self._c_data[12][0]

    @re_admission_indicator.setter  # set PV1.13
    def re_admission_indicator(
        self, readmission_indicator: ReAdmissionIndicator | None
    ):
        """
        id: PV1.13 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.13
        """
        self._c_data[12] = (readmission_indicator,)

    @property  # get PV1.14
    def admit_source(self) -> AdmitSource | None:
        """
        id: PV1.14 | len: 6 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.14
        """
        return self._c_data[13][0]

    @admit_source.setter  # set PV1.14
    def admit_source(self, admit_source: AdmitSource | None):
        """
        id: PV1.14 | len: 6 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.14
        """
        self._c_data[13] = (admit_source,)

    @property
    def ambulatory_status(self) -> tuple[AmbulatoryStatus, ...] | tuple[None]:
        """
        id: PV1.15 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.15
        """
        return self._c_data[14]

    @ambulatory_status.setter  # set PV1.15
    def ambulatory_status(
        self, ambulatory_status: AmbulatoryStatus | tuple[AmbulatoryStatus] | None
    ):
        """
        id: PV1.15 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.15
        """
        if isinstance(ambulatory_status, tuple):
            self._c_data[14] = ambulatory_status
        else:
            self._c_data[14] = (ambulatory_status,)

    @property  # get PV1.16
    def vip_indicator(self) -> VipIndicator | None:
        """
        id: PV1.16 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.16
        """
        return self._c_data[15][0]

    @vip_indicator.setter  # set PV1.16
    def vip_indicator(self, vip_indicator: VipIndicator | None):
        """
        id: PV1.16 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.16
        """
        self._c_data[15] = (vip_indicator,)

    @property
    def admitting_doctor(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PV1.17 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.17
        """
        return self._c_data[16]

    @admitting_doctor.setter  # set PV1.17
    def admitting_doctor(self, physician_id: PhysicianId | tuple[PhysicianId] | None):
        """
        id: PV1.17 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.17
        """
        if isinstance(physician_id, tuple):
            self._c_data[16] = physician_id
        else:
            self._c_data[16] = (physician_id,)

    @property  # get PV1.18
    def patient_type(self) -> PatientType | None:
        """
        id: PV1.18 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.18
        """
        return self._c_data[17][0]

    @patient_type.setter  # set PV1.18
    def patient_type(self, patient_type: PatientType | None):
        """
        id: PV1.18 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.18
        """
        self._c_data[17] = (patient_type,)

    @property  # get PV1.19
    def visit_number(self) -> CX | None:
        """
        id: PV1.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.19
        """
        return self._c_data[18][0]

    @visit_number.setter  # set PV1.19
    def visit_number(self, cx: CX | None):
        """
        id: PV1.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.19
        """
        self._c_data[18] = (cx,)

    @property
    def financial_class(self) -> tuple[FC, ...] | tuple[None]:
        """
        id: PV1.20 | len: 50 | use: O | rpt: *
        ---
        return_type: tuple[FC, ...]: (Financial Class, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.20
        """
        return self._c_data[19]

    @financial_class.setter  # set PV1.20
    def financial_class(self, fc: FC | tuple[FC] | None):
        """
        id: PV1.20 | len: 50 | use: O | rpt: *
        ---
        param_type: FC | tuple[FC, ...]: (Financial Class, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.20
        """
        if isinstance(fc, tuple):
            self._c_data[19] = fc
        else:
            self._c_data[19] = (fc,)

    @property  # get PV1.21
    def charge_price_indicator(self) -> ChargeOrPriceIndicator | None:
        """
        id: PV1.21 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.21
        """
        return self._c_data[20][0]

    @charge_price_indicator.setter  # set PV1.21
    def charge_price_indicator(
        self, charge_or_price_indicator: ChargeOrPriceIndicator | None
    ):
        """
        id: PV1.21 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.21
        """
        self._c_data[20] = (charge_or_price_indicator,)

    @property  # get PV1.22
    def courtesy_code(self) -> CourtesyCode | None:
        """
        id: PV1.22 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.22
        """
        return self._c_data[21][0]

    @courtesy_code.setter  # set PV1.22
    def courtesy_code(self, courtesy_code: CourtesyCode | None):
        """
        id: PV1.22 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.22
        """
        self._c_data[21] = (courtesy_code,)

    @property  # get PV1.23
    def credit_rating(self) -> CreditRating | None:
        """
        id: PV1.23 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.23
        """
        return self._c_data[22][0]

    @credit_rating.setter  # set PV1.23
    def credit_rating(self, credit_rating: CreditRating | None):
        """
        id: PV1.23 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.23
        """
        self._c_data[22] = (credit_rating,)

    @property
    def contract_code(self) -> tuple[ContractCode, ...] | tuple[None]:
        """
        id: PV1.24 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.24
        """
        return self._c_data[23]

    @contract_code.setter  # set PV1.24
    def contract_code(self, contract_code: ContractCode | tuple[ContractCode] | None):
        """
        id: PV1.24 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.24
        """
        if isinstance(contract_code, tuple):
            self._c_data[23] = contract_code
        else:
            self._c_data[23] = (contract_code,)

    @property
    def contract_effective_date(self) -> tuple[DT, ...] | tuple[None]:
        """
        id: PV1.25 | len: 8 | use: O | rpt: *
        ---
        return_type: tuple[DT, ...]: (Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.25
        """
        return self._c_data[24]

    @contract_effective_date.setter  # set PV1.25
    def contract_effective_date(self, dt: DT | tuple[DT] | None):
        """
        id: PV1.25 | len: 8 | use: O | rpt: *
        ---
        param_type: DT | tuple[DT, ...]: (Date, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.25
        """
        if isinstance(dt, tuple):
            self._c_data[24] = dt
        else:
            self._c_data[24] = (dt,)

    @property
    def contract_amount(self) -> tuple[NM, ...] | tuple[None]:
        """
        id: PV1.26 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.26
        """
        return self._c_data[25]

    @contract_amount.setter  # set PV1.26
    def contract_amount(self, nm: NM | tuple[NM] | None):
        """
        id: PV1.26 | len: 12 | use: O | rpt: *
        ---
        param_type: NM | tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.26
        """
        if isinstance(nm, tuple):
            self._c_data[25] = nm
        else:
            self._c_data[25] = (nm,)

    @property
    def contract_period(self) -> tuple[NM, ...] | tuple[None]:
        """
        id: PV1.27 | len: 3 | use: O | rpt: *
        ---
        return_type: tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.27
        """
        return self._c_data[26]

    @contract_period.setter  # set PV1.27
    def contract_period(self, nm: NM | tuple[NM] | None):
        """
        id: PV1.27 | len: 3 | use: O | rpt: *
        ---
        param_type: NM | tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.27
        """
        if isinstance(nm, tuple):
            self._c_data[26] = nm
        else:
            self._c_data[26] = (nm,)

    @property  # get PV1.28
    def interest_code(self) -> InterestRateCode | None:
        """
        id: PV1.28 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.28
        """
        return self._c_data[27][0]

    @interest_code.setter  # set PV1.28
    def interest_code(self, interest_rate_code: InterestRateCode | None):
        """
        id: PV1.28 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.28
        """
        self._c_data[27] = (interest_rate_code,)

    @property  # get PV1.29
    def transfer_to_bad_debt_code(self) -> TransferToBadDebtCode | None:
        """
        id: PV1.29 | len: 4 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.29
        """
        return self._c_data[28][0]

    @transfer_to_bad_debt_code.setter  # set PV1.29
    def transfer_to_bad_debt_code(
        self, transfer_to_bad_debt_code: TransferToBadDebtCode | None
    ):
        """
        id: PV1.29 | len: 4 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.29
        """
        self._c_data[28] = (transfer_to_bad_debt_code,)

    @property  # get PV1.30
    def transfer_to_bad_debt_date(self) -> DT | None:
        """
        id: PV1.30 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.30
        """
        return self._c_data[29][0]

    @transfer_to_bad_debt_date.setter  # set PV1.30
    def transfer_to_bad_debt_date(self, dt: DT | None):
        """
        id: PV1.30 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.30
        """
        self._c_data[29] = (dt,)

    @property  # get PV1.31
    def bad_debt_agency_code(self) -> BadDebtAgencyCode | None:
        """
        id: PV1.31 | len: 10 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.31
        """
        return self._c_data[30][0]

    @bad_debt_agency_code.setter  # set PV1.31
    def bad_debt_agency_code(self, bad_debt_agency_code: BadDebtAgencyCode | None):
        """
        id: PV1.31 | len: 10 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.31
        """
        self._c_data[30] = (bad_debt_agency_code,)

    @property  # get PV1.32
    def bad_debt_transfer_amount(self) -> NM | None:
        """
        id: PV1.32 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.32
        """
        return self._c_data[31][0]

    @bad_debt_transfer_amount.setter  # set PV1.32
    def bad_debt_transfer_amount(self, nm: NM | None):
        """
        id: PV1.32 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.32
        """
        self._c_data[31] = (nm,)

    @property  # get PV1.33
    def bad_debt_recovery_amount(self) -> NM | None:
        """
        id: PV1.33 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.33
        """
        return self._c_data[32][0]

    @bad_debt_recovery_amount.setter  # set PV1.33
    def bad_debt_recovery_amount(self, nm: NM | None):
        """
        id: PV1.33 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.33
        """
        self._c_data[32] = (nm,)

    @property  # get PV1.34
    def delete_account_indicator(self) -> DeleteAccountCode | None:
        """
        id: PV1.34 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.34
        """
        return self._c_data[33][0]

    @delete_account_indicator.setter  # set PV1.34
    def delete_account_indicator(self, delete_account_code: DeleteAccountCode | None):
        """
        id: PV1.34 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.34
        """
        self._c_data[33] = (delete_account_code,)

    @property  # get PV1.35
    def delete_account_date(self) -> DT | None:
        """
        id: PV1.35 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.35
        """
        return self._c_data[34][0]

    @delete_account_date.setter  # set PV1.35
    def delete_account_date(self, dt: DT | None):
        """
        id: PV1.35 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.35
        """
        self._c_data[34] = (dt,)

    @property  # get PV1.36
    def discharge_disposition(self) -> DischargeDisposition | None:
        """
        id: PV1.36 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.36
        """
        return self._c_data[35][0]

    @discharge_disposition.setter  # set PV1.36
    def discharge_disposition(self, discharge_disposition: DischargeDisposition | None):
        """
        id: PV1.36 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.36
        """
        self._c_data[35] = (discharge_disposition,)

    @property  # get PV1.37
    def discharged_to_location(self) -> DLD | None:
        """
        id: PV1.37 | len: 47 | use: O | rpt: 1
        ---
        return_type: DLD: Discharge Location and Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.37
        """
        return self._c_data[36][0]

    @discharged_to_location.setter  # set PV1.37
    def discharged_to_location(self, dld: DLD | None):
        """
        id: PV1.37 | len: 47 | use: O | rpt: 1
        ---
        param_type: DLD: Discharge Location and Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.37
        """
        self._c_data[36] = (dld,)

    @property  # get PV1.38
    def diet_type(self) -> DietType | None:
        """
        id: PV1.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.38
        """
        return self._c_data[37][0]

    @diet_type.setter  # set PV1.38
    def diet_type(self, diet_type: DietType | None):
        """
        id: PV1.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.38
        """
        self._c_data[37] = (diet_type,)

    @property  # get PV1.39
    def servicing_facility(self) -> ServicingFacility | None:
        """
        id: PV1.39 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.39
        """
        return self._c_data[38][0]

    @servicing_facility.setter  # set PV1.39
    def servicing_facility(self, servicing_facility: ServicingFacility | None):
        """
        id: PV1.39 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.39
        """
        self._c_data[38] = (servicing_facility,)

    @property  # get PV1.40
    def bed_status(self) -> BedStatus | None:
        """
        id: PV1.40 | len: 1 | use: B | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.40
        """
        return self._c_data[39][0]

    @bed_status.setter  # set PV1.40
    def bed_status(self, bed_status: BedStatus | None):
        """
        id: PV1.40 | len: 1 | use: B | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.40
        """
        self._c_data[39] = (bed_status,)

    @property  # get PV1.41
    def account_status(self) -> AccountStatus | None:
        """
        id: PV1.41 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.41
        """
        return self._c_data[40][0]

    @account_status.setter  # set PV1.41
    def account_status(self, account_status: AccountStatus | None):
        """
        id: PV1.41 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.41
        """
        self._c_data[40] = (account_status,)

    @property  # get PV1.42
    def pending_location(self) -> PL | None:
        """
        id: PV1.42 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.42
        """
        return self._c_data[41][0]

    @pending_location.setter  # set PV1.42
    def pending_location(self, pl: PL | None):
        """
        id: PV1.42 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.42
        """
        self._c_data[41] = (pl,)

    @property  # get PV1.43
    def prior_temporary_location(self) -> PL | None:
        """
        id: PV1.43 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.43
        """
        return self._c_data[42][0]

    @prior_temporary_location.setter  # set PV1.43
    def prior_temporary_location(self, pl: PL | None):
        """
        id: PV1.43 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.43
        """
        self._c_data[42] = (pl,)

    @property  # get PV1.44
    def admit_date_or_time(self) -> TS | None:
        """
        id: PV1.44 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.44
        """
        return self._c_data[43][0]

    @admit_date_or_time.setter  # set PV1.44
    def admit_date_or_time(self, ts: TS | None):
        """
        id: PV1.44 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.44
        """
        self._c_data[43] = (ts,)

    @property
    def discharge_date_or_time(self) -> tuple[TS, ...] | tuple[None]:
        """
        id: PV1.45 | len: 26 | use: O | rpt: *
        ---
        return_type: tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.45
        """
        return self._c_data[44]

    @discharge_date_or_time.setter  # set PV1.45
    def discharge_date_or_time(self, ts: TS | tuple[TS] | None):
        """
        id: PV1.45 | len: 26 | use: O | rpt: *
        ---
        param_type: TS | tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.45
        """
        if isinstance(ts, tuple):
            self._c_data[44] = ts
        else:
            self._c_data[44] = (ts,)

    @property  # get PV1.46
    def current_patient_balance(self) -> NM | None:
        """
        id: PV1.46 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.46
        """
        return self._c_data[45][0]

    @current_patient_balance.setter  # set PV1.46
    def current_patient_balance(self, nm: NM | None):
        """
        id: PV1.46 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.46
        """
        self._c_data[45] = (nm,)

    @property  # get PV1.47
    def total_charges(self) -> NM | None:
        """
        id: PV1.47 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.47
        """
        return self._c_data[46][0]

    @total_charges.setter  # set PV1.47
    def total_charges(self, nm: NM | None):
        """
        id: PV1.47 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.47
        """
        self._c_data[46] = (nm,)

    @property  # get PV1.48
    def total_adjustments(self) -> NM | None:
        """
        id: PV1.48 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.48
        """
        return self._c_data[47][0]

    @total_adjustments.setter  # set PV1.48
    def total_adjustments(self, nm: NM | None):
        """
        id: PV1.48 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.48
        """
        self._c_data[47] = (nm,)

    @property  # get PV1.49
    def total_payments(self) -> NM | None:
        """
        id: PV1.49 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.49
        """
        return self._c_data[48][0]

    @total_payments.setter  # set PV1.49
    def total_payments(self, nm: NM | None):
        """
        id: PV1.49 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.49
        """
        self._c_data[48] = (nm,)

    @property  # get PV1.50
    def alternate_visit_id(self) -> CX | None:
        """
        id: PV1.50 | len: 250 | use: O | rpt: 1
        ---
        return_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.50
        """
        return self._c_data[49][0]

    @alternate_visit_id.setter  # set PV1.50
    def alternate_visit_id(self, cx: CX | None):
        """
        id: PV1.50 | len: 250 | use: O | rpt: 1
        ---
        param_type: CX: Extended Composite ID with Check Digit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.50
        """
        self._c_data[49] = (cx,)

    @property  # get PV1.51
    def visit_indicator(self) -> VisitIndicator | None:
        """
        id: PV1.51 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.51
        """
        return self._c_data[50][0]

    @visit_indicator.setter  # set PV1.51
    def visit_indicator(self, visit_indicator: VisitIndicator | None):
        """
        id: PV1.51 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.51
        """
        self._c_data[50] = (visit_indicator,)

    @property
    def other_healthcare_provider(self) -> tuple[PhysicianId, ...] | tuple[None]:
        """
        id: PV1.52 | len: 250 | use: B | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.52
        """
        return self._c_data[51]

    @other_healthcare_provider.setter  # set PV1.52
    def other_healthcare_provider(
        self, physician_id: PhysicianId | tuple[PhysicianId] | None
    ):
        """
        id: PV1.52 | len: 250 | use: B | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV1.52
        """
        if isinstance(physician_id, tuple):
            self._c_data[51] = physician_id
        else:
            self._c_data[51] = (physician_id,)
