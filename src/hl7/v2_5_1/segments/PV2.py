from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..data_types.IS import IS
from ..data_types.DT import DT
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.PL import PL
from ..data_types.TS import TS
from ..tables.RecurringServiceCode import RecurringServiceCode
from ..tables.AccommodationCode import AccommodationCode
from ..tables.VisitUserCode import VisitUserCode
from ..tables.PatientConditionCode import PatientConditionCode
from ..tables.VisitPriorityCode import VisitPriorityCode
from ..tables.PublicityCode import PublicityCode
from ..tables.AdmissionLevelOfCareCode import AdmissionLevelOfCareCode
from ..tables.SpecialProgramCode import SpecialProgramCode
from ..tables.NotifyClergyCode import NotifyClergyCode
from ..tables.PrecautionCode import PrecautionCode
from ..tables.OrganDonorCode import OrganDonorCode
from ..tables.RecreationalDrugUseCode import RecreationalDrugUseCode
from ..tables.DischargeDisposition import DischargeDisposition
from ..tables.AdvanceDirectiveCode import AdvanceDirectiveCode
from ..tables.PurgeStatusCode import PurgeStatusCode
from ..tables.LivingWillCode import LivingWillCode
from ..tables.PatientChargeAdjustment import PatientChargeAdjustment
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.ModeOfArrivalCode import ModeOfArrivalCode
from ..tables.PatientStatusCode import PatientStatusCode


"""
Patient Visit - Additional Information - PV2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PV2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PV2,
    CE, XON, IS, DT, ID, NM, ST, XCN, PL, TS
)

pv2 = PV2(  #  - The PV2 segment is a continuation of information contained on the PV1 segment
    prior_pending_location=None,  # PL(...) 
    accommodation_code=None,  # CE(...) 
    admit_reason=None,  # CE(...) 
    transfer_reason=None,  # CE(...) 
    patient_valuables=None,  # ST(...) 
    patient_valuables_location=None,  # ST(...) 
    visit_user_code=None,  # IS(...) 
    expected_admit_date_or_time=None,  # TS(...) 
    expected_discharge_date_or_time=None,  # TS(...) 
    estimated_length_of_inpatient_stay=None,  # NM(...) 
    actual_length_of_inpatient_stay=None,  # NM(...) 
    visit_description=None,  # ST(...) 
    referral_source_code=None,  # XCN(...) 
    previous_service_date=None,  # DT(...) 
    employment_illness_related_indicator=None,  # ID(...) 
    purge_status_code=None,  # IS(...) 
    purge_status_date=None,  # DT(...) 
    special_program_code=None,  # IS(...) 
    retention_indicator=None,  # ID(...) 
    expected_number_of_insurance_plans=None,  # NM(...) 
    visit_publicity_code=None,  # IS(...) 
    visit_protection_indicator=None,  # ID(...) 
    clinic_organization_name=None,  # XON(...) 
    patient_status_code=None,  # IS(...) 
    visit_priority_code=None,  # IS(...) 
    previous_treatment_date=None,  # DT(...) 
    expected_discharge_disposition=None,  # IS(...) 
    signature_on_file_date=None,  # DT(...) 
    first_similar_illness_date=None,  # DT(...) 
    patient_charge_adjustment_code=None,  # CE(...) 
    recurring_service_code=None,  # IS(...) 
    billing_media_code=None,  # ID(...) 
    expected_surgery_date_and_time=None,  # TS(...) 
    military_partnership_code=None,  # ID(...) 
    military_non_availability_code=None,  # ID(...) 
    newborn_baby_indicator=None,  # ID(...) 
    baby_detained_indicator=None,  # ID(...) 
    mode_of_arrival_code=None,  # CE(...) 
    recreational_drug_use_code=None,  # CE(...) 
    admission_level_of_care_code=None,  # CE(...) 
    precaution_code=None,  # CE(...) 
    patient_condition_code=None,  # CE(...) 
    living_will_code=None,  # IS(...) 
    organ_donor_code=None,  # IS(...) 
    advance_directive_code=None,  # CE(...) 
    patient_status_effective_date=None,  # DT(...) 
    expected_loa_return_date_or_time=None,  # TS(...) 
    expected_pre_admission_testing_date_or_time=None,  # TS(...) 
    notify_clergy_code=None,  # IS(...) 
)

-----END SEGMENT::PV2 TEMPLATE-----
"""


class PV2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PV2"""
    _hl7_name = """Patient Visit - Additional Information"""
    _hl7_description = """The PV2 segment is a continuation of information contained on the PV1 segment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2"
    _c_length = (80, 250, 250, 250, 25, 25, 2, 26, 26, 3, 3, 50, 250, 8, 1, 1, 8, 2, 1, 1, 1, 1, 250, 2, 1, 8, 2, 8, 8, 250, 2, 1, 26, 1, 1, 1, 1, 250, 250, 250, 250, 250, 2, 2, 250, 8, 26, 26, 20,)
    _c_rpt = (1, 1, 1, 1, 65535, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 65535, 1, 1, 1, 65535, 1, 1, 1, 65535,)
    _c_usage = ("C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C", "O", "O",)
    _c_components = (PL, CE, CE, CE, ST, ST, IS, TS, TS, NM, NM, ST, XCN, DT, ID, IS, DT, IS, ID, NM, IS, ID, XON, IS, IS, DT, IS, DT, DT, CE, IS, ID, TS, ID, ID, ID, ID, CE, CE, CE, CE, CE, IS, IS, CE, DT, TS, TS, IS,)
    _c_aliases = ("PV2.1", "PV2.2", "PV2.3", "PV2.4", "PV2.5", "PV2.6", "PV2.7", "PV2.8", "PV2.9", "PV2.10", "PV2.11", "PV2.12", "PV2.13", "PV2.14", "PV2.15", "PV2.16", "PV2.17", "PV2.18", "PV2.19", "PV2.20", "PV2.21", "PV2.22", "PV2.23", "PV2.24", "PV2.25", "PV2.26", "PV2.27", "PV2.28", "PV2.29", "PV2.30", "PV2.31", "PV2.32", "PV2.33", "PV2.34", "PV2.35", "PV2.36", "PV2.37", "PV2.38", "PV2.39", "PV2.40", "PV2.41", "PV2.42", "PV2.43", "PV2.44", "PV2.45", "PV2.46", "PV2.47", "PV2.48", "PV2.49",)
    _c_names = ("Prior Pending Location", "Accommodation Code", "Admit Reason", "Transfer Reason", "Patient Valuables", "Patient Valuables Location", "Visit User Code", "Expected Admit Date/Time", "Expected Discharge Date/Time", "Estimated Length of Inpatient Stay", "Actual Length of Inpatient Stay", "Visit Description", "Referral Source Code", "Previous Service Date", "Employment Illness Related Indicator", "Purge Status Code", "Purge Status Date", "Special Program Code", "Retention Indicator", "Expected Number of Insurance Plans", "Visit Publicity Code", "Visit Protection Indicator", "Clinic Organization Name", "Patient Status Code", "Visit Priority Code", "Previous Treatment Date", "Expected Discharge Disposition", "Signature on File Date", "First Similar Illness Date", "Patient Charge Adjustment Code", "Recurring Service Code", "Billing Media Code", "Expected Surgery Date and Time", "Military Partnership Code", "Military Non-Availability Code", "Newborn Baby Indicator", "Baby Detained Indicator", "Mode of Arrival Code", "Recreational Drug Use Code", "Admission Level of Care Code", "Precaution Code", "Patient Condition Code", "Living Will Code", "Organ Donor Code", "Advance Directive Code", "Patient Status Effective Date", "Expected LOA Return Date/Time", "Expected Pre-admission Testing Date/Time", "Notify Clergy Code",)
    _c_attrs = ("prior_pending_location", "accommodation_code", "admit_reason", "transfer_reason", "patient_valuables", "patient_valuables_location", "visit_user_code", "expected_admit_date_or_time", "expected_discharge_date_or_time", "estimated_length_of_inpatient_stay", "actual_length_of_inpatient_stay", "visit_description", "referral_source_code", "previous_service_date", "employment_illness_related_indicator", "purge_status_code", "purge_status_date", "special_program_code", "retention_indicator", "expected_number_of_insurance_plans", "visit_publicity_code", "visit_protection_indicator", "clinic_organization_name", "patient_status_code", "visit_priority_code", "previous_treatment_date", "expected_discharge_disposition", "signature_on_file_date", "first_similar_illness_date", "patient_charge_adjustment_code", "recurring_service_code", "billing_media_code", "expected_surgery_date_and_time", "military_partnership_code", "military_non_availability_code", "newborn_baby_indicator", "baby_detained_indicator", "mode_of_arrival_code", "recreational_drug_use_code", "admission_level_of_care_code", "precaution_code", "patient_condition_code", "living_will_code", "organ_donor_code", "advance_directive_code", "patient_status_effective_date", "expected_loa_return_date_or_time", "expected_pre_admission_testing_date_or_time", "notify_clergy_code",)
    # fmt: on

    def __init__(
        self,
        prior_pending_location: PL | None = None,  # PV2.1
        accommodation_code: AccommodationCode | CE | None = None,  # PV2.2
        admit_reason: CE | None = None,  # PV2.3
        transfer_reason: CE | None = None,  # PV2.4
        patient_valuables: ST | None = None,  # PV2.5
        patient_valuables_location: ST | None = None,  # PV2.6
        visit_user_code: VisitUserCode | IS | None = None,  # PV2.7
        expected_admit_date_or_time: TS | None = None,  # PV2.8
        expected_discharge_date_or_time: TS | None = None,  # PV2.9
        estimated_length_of_inpatient_stay: NM | None = None,  # PV2.10
        actual_length_of_inpatient_stay: NM | None = None,  # PV2.11
        visit_description: ST | None = None,  # PV2.12
        referral_source_code: XCN | None = None,  # PV2.13
        previous_service_date: DT | None = None,  # PV2.14
        employment_illness_related_indicator: YesOrNoIndicator
        | ID
        | None = None,  # PV2.15
        purge_status_code: PurgeStatusCode | IS | None = None,  # PV2.16
        purge_status_date: DT | None = None,  # PV2.17
        special_program_code: SpecialProgramCode | IS | None = None,  # PV2.18
        retention_indicator: YesOrNoIndicator | ID | None = None,  # PV2.19
        expected_number_of_insurance_plans: NM | None = None,  # PV2.20
        visit_publicity_code: PublicityCode | IS | None = None,  # PV2.21
        visit_protection_indicator: YesOrNoIndicator | ID | None = None,  # PV2.22
        clinic_organization_name: XON | None = None,  # PV2.23
        patient_status_code: PatientStatusCode | IS | None = None,  # PV2.24
        visit_priority_code: VisitPriorityCode | IS | None = None,  # PV2.25
        previous_treatment_date: DT | None = None,  # PV2.26
        expected_discharge_disposition: DischargeDisposition
        | IS
        | None = None,  # PV2.27
        signature_on_file_date: DT | None = None,  # PV2.28
        first_similar_illness_date: DT | None = None,  # PV2.29
        patient_charge_adjustment_code: PatientChargeAdjustment
        | CE
        | None = None,  # PV2.30
        recurring_service_code: RecurringServiceCode | IS | None = None,  # PV2.31
        billing_media_code: YesOrNoIndicator | ID | None = None,  # PV2.32
        expected_surgery_date_and_time: TS | None = None,  # PV2.33
        military_partnership_code: YesOrNoIndicator | ID | None = None,  # PV2.34
        military_non_availability_code: YesOrNoIndicator | ID | None = None,  # PV2.35
        newborn_baby_indicator: YesOrNoIndicator | ID | None = None,  # PV2.36
        baby_detained_indicator: YesOrNoIndicator | ID | None = None,  # PV2.37
        mode_of_arrival_code: ModeOfArrivalCode | CE | None = None,  # PV2.38
        recreational_drug_use_code: RecreationalDrugUseCode
        | CE
        | None = None,  # PV2.39
        admission_level_of_care_code: AdmissionLevelOfCareCode
        | CE
        | None = None,  # PV2.40
        precaution_code: PrecautionCode | CE | None = None,  # PV2.41
        patient_condition_code: PatientConditionCode | CE | None = None,  # PV2.42
        living_will_code: LivingWillCode | IS | None = None,  # PV2.43
        organ_donor_code: OrganDonorCode | IS | None = None,  # PV2.44
        advance_directive_code: AdvanceDirectiveCode | CE | None = None,  # PV2.45
        patient_status_effective_date: DT | None = None,  # PV2.46
        expected_loa_return_date_or_time: TS | None = None,  # PV2.47
        expected_pre_admission_testing_date_or_time: TS | None = None,  # PV2.48
        notify_clergy_code: NotifyClergyCode | IS | None = None,  # PV2.49
    ):
        """
        Patient Visit - Additional Information - `PV2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2>`_
        The PV2 segment is a continuation of information contained on the PV1 segment.

        :param prior_pending_location: Person Location (id: PV2.1 | len: 80 | use: C | rpt: 1)
        :param accommodation_code: Coded Element (id: PV2.2 | len: 250 | use: O | rpt: 1)
        :param admit_reason: Coded Element (id: PV2.3 | len: 250 | use: O | rpt: 1)
        :param transfer_reason: Coded Element (id: PV2.4 | len: 250 | use: O | rpt: 1)
        :param patient_valuables: String Data (id: PV2.5 | len: 25 | use: O | rpt: *)
        :param patient_valuables_location: String Data (id: PV2.6 | len: 25 | use: O | rpt: 1)
        :param visit_user_code: Coded value for user-defined tables (id: PV2.7 | len: 2 | use: O | rpt: *)
        :param expected_admit_date_or_time: Time Stamp (id: PV2.8 | len: 26 | use: O | rpt: 1)
        :param expected_discharge_date_or_time: Time Stamp (id: PV2.9 | len: 26 | use: O | rpt: 1)
        :param estimated_length_of_inpatient_stay: Numeric (id: PV2.10 | len: 3 | use: O | rpt: 1)
        :param actual_length_of_inpatient_stay: Numeric (id: PV2.11 | len: 3 | use: O | rpt: 1)
        :param visit_description: String Data (id: PV2.12 | len: 50 | use: O | rpt: 1)
        :param referral_source_code: Extended Composite ID Number and Name for Persons (id: PV2.13 | len: 250 | use: O | rpt: *)
        :param previous_service_date: Date (id: PV2.14 | len: 8 | use: O | rpt: 1)
        :param employment_illness_related_indicator: Coded values for HL7 tables (id: PV2.15 | len: 1 | use: O | rpt: 1)
        :param purge_status_code: Coded value for user-defined tables (id: PV2.16 | len: 1 | use: O | rpt: 1)
        :param purge_status_date: Date (id: PV2.17 | len: 8 | use: O | rpt: 1)
        :param special_program_code: Coded value for user-defined tables (id: PV2.18 | len: 2 | use: O | rpt: 1)
        :param retention_indicator: Coded values for HL7 tables (id: PV2.19 | len: 1 | use: O | rpt: 1)
        :param expected_number_of_insurance_plans: Numeric (id: PV2.20 | len: 1 | use: O | rpt: 1)
        :param visit_publicity_code: Coded value for user-defined tables (id: PV2.21 | len: 1 | use: O | rpt: 1)
        :param visit_protection_indicator: Coded values for HL7 tables (id: PV2.22 | len: 1 | use: O | rpt: 1)
        :param clinic_organization_name: Extended Composite Name and Identification Number for Organizations (id: PV2.23 | len: 250 | use: O | rpt: *)
        :param patient_status_code: Coded value for user-defined tables (id: PV2.24 | len: 2 | use: O | rpt: 1)
        :param visit_priority_code: Coded value for user-defined tables (id: PV2.25 | len: 1 | use: O | rpt: 1)
        :param previous_treatment_date: Date (id: PV2.26 | len: 8 | use: O | rpt: 1)
        :param expected_discharge_disposition: Coded value for user-defined tables (id: PV2.27 | len: 2 | use: O | rpt: 1)
        :param signature_on_file_date: Date (id: PV2.28 | len: 8 | use: O | rpt: 1)
        :param first_similar_illness_date: Date (id: PV2.29 | len: 8 | use: O | rpt: 1)
        :param patient_charge_adjustment_code: Coded Element (id: PV2.30 | len: 250 | use: O | rpt: 1)
        :param recurring_service_code: Coded value for user-defined tables (id: PV2.31 | len: 2 | use: O | rpt: 1)
        :param billing_media_code: Coded values for HL7 tables (id: PV2.32 | len: 1 | use: O | rpt: 1)
        :param expected_surgery_date_and_time: Time Stamp (id: PV2.33 | len: 26 | use: O | rpt: 1)
        :param military_partnership_code: Coded values for HL7 tables (id: PV2.34 | len: 1 | use: O | rpt: 1)
        :param military_non_availability_code: Coded values for HL7 tables (id: PV2.35 | len: 1 | use: O | rpt: 1)
        :param newborn_baby_indicator: Coded values for HL7 tables (id: PV2.36 | len: 1 | use: O | rpt: 1)
        :param baby_detained_indicator: Coded values for HL7 tables (id: PV2.37 | len: 1 | use: O | rpt: 1)
        :param mode_of_arrival_code: Coded Element (id: PV2.38 | len: 250 | use: O | rpt: 1)
        :param recreational_drug_use_code: Coded Element (id: PV2.39 | len: 250 | use: O | rpt: *)
        :param admission_level_of_care_code: Coded Element (id: PV2.40 | len: 250 | use: O | rpt: 1)
        :param precaution_code: Coded Element (id: PV2.41 | len: 250 | use: O | rpt: *)
        :param patient_condition_code: Coded Element (id: PV2.42 | len: 250 | use: O | rpt: 1)
        :param living_will_code: Coded value for user-defined tables (id: PV2.43 | len: 2 | use: O | rpt: 1)
        :param organ_donor_code: Coded value for user-defined tables (id: PV2.44 | len: 2 | use: O | rpt: 1)
        :param advance_directive_code: Coded Element (id: PV2.45 | len: 250 | use: O | rpt: *)
        :param patient_status_effective_date: Date (id: PV2.46 | len: 8 | use: O | rpt: 1)
        :param expected_loa_return_date_or_time: Time Stamp (id: PV2.47 | len: 26 | use: C | rpt: 1)
        :param expected_pre_admission_testing_date_or_time: Time Stamp (id: PV2.48 | len: 26 | use: O | rpt: 1)
        :param notify_clergy_code: Coded value for user-defined tables (id: PV2.49 | len: 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 49
        self.prior_pending_location = prior_pending_location
        self.accommodation_code = accommodation_code
        self.admit_reason = admit_reason
        self.transfer_reason = transfer_reason
        self.patient_valuables = patient_valuables
        self.patient_valuables_location = patient_valuables_location
        self.visit_user_code = visit_user_code
        self.expected_admit_date_or_time = expected_admit_date_or_time
        self.expected_discharge_date_or_time = expected_discharge_date_or_time
        self.estimated_length_of_inpatient_stay = estimated_length_of_inpatient_stay
        self.actual_length_of_inpatient_stay = actual_length_of_inpatient_stay
        self.visit_description = visit_description
        self.referral_source_code = referral_source_code
        self.previous_service_date = previous_service_date
        self.employment_illness_related_indicator = employment_illness_related_indicator
        self.purge_status_code = purge_status_code
        self.purge_status_date = purge_status_date
        self.special_program_code = special_program_code
        self.retention_indicator = retention_indicator
        self.expected_number_of_insurance_plans = expected_number_of_insurance_plans
        self.visit_publicity_code = visit_publicity_code
        self.visit_protection_indicator = visit_protection_indicator
        self.clinic_organization_name = clinic_organization_name
        self.patient_status_code = patient_status_code
        self.visit_priority_code = visit_priority_code
        self.previous_treatment_date = previous_treatment_date
        self.expected_discharge_disposition = expected_discharge_disposition
        self.signature_on_file_date = signature_on_file_date
        self.first_similar_illness_date = first_similar_illness_date
        self.patient_charge_adjustment_code = patient_charge_adjustment_code
        self.recurring_service_code = recurring_service_code
        self.billing_media_code = billing_media_code
        self.expected_surgery_date_and_time = expected_surgery_date_and_time
        self.military_partnership_code = military_partnership_code
        self.military_non_availability_code = military_non_availability_code
        self.newborn_baby_indicator = newborn_baby_indicator
        self.baby_detained_indicator = baby_detained_indicator
        self.mode_of_arrival_code = mode_of_arrival_code
        self.recreational_drug_use_code = recreational_drug_use_code
        self.admission_level_of_care_code = admission_level_of_care_code
        self.precaution_code = precaution_code
        self.patient_condition_code = patient_condition_code
        self.living_will_code = living_will_code
        self.organ_donor_code = organ_donor_code
        self.advance_directive_code = advance_directive_code
        self.patient_status_effective_date = patient_status_effective_date
        self.expected_loa_return_date_or_time = expected_loa_return_date_or_time
        self.expected_pre_admission_testing_date_or_time = (
            expected_pre_admission_testing_date_or_time
        )
        self.notify_clergy_code = notify_clergy_code

    @property  # get PV2.1
    def prior_pending_location(self) -> PL | None:
        """
        id: PV2.1 | len: 80 | use: C | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.1
        """
        return self._c_data[0][0]

    @prior_pending_location.setter  # set PV2.1
    def prior_pending_location(self, pl: PL | None):
        """
        id: PV2.1 | len: 80 | use: C | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.1
        """
        self._c_data[0] = (pl,)

    @property  # get PV2.2
    def accommodation_code(self) -> AccommodationCode | None:
        """
        id: PV2.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.2
        """
        return self._c_data[1][0]

    @accommodation_code.setter  # set PV2.2
    def accommodation_code(self, accommodation_code: AccommodationCode | None):
        """
        id: PV2.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.2
        """
        self._c_data[1] = (accommodation_code,)

    @property  # get PV2.3
    def admit_reason(self) -> CE | None:
        """
        id: PV2.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.3
        """
        return self._c_data[2][0]

    @admit_reason.setter  # set PV2.3
    def admit_reason(self, ce: CE | None):
        """
        id: PV2.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.3
        """
        self._c_data[2] = (ce,)

    @property  # get PV2.4
    def transfer_reason(self) -> CE | None:
        """
        id: PV2.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.4
        """
        return self._c_data[3][0]

    @transfer_reason.setter  # set PV2.4
    def transfer_reason(self, ce: CE | None):
        """
        id: PV2.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.4
        """
        self._c_data[3] = (ce,)

    @property
    def patient_valuables(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: PV2.5 | len: 25 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.5
        """
        return self._c_data[4]

    @patient_valuables.setter  # set PV2.5
    def patient_valuables(self, st: ST | tuple[ST] | None):
        """
        id: PV2.5 | len: 25 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.5
        """
        if isinstance(st, tuple):
            self._c_data[4] = st
        else:
            self._c_data[4] = (st,)

    @property  # get PV2.6
    def patient_valuables_location(self) -> ST | None:
        """
        id: PV2.6 | len: 25 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.6
        """
        return self._c_data[5][0]

    @patient_valuables_location.setter  # set PV2.6
    def patient_valuables_location(self, st: ST | None):
        """
        id: PV2.6 | len: 25 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.6
        """
        self._c_data[5] = (st,)

    @property
    def visit_user_code(self) -> tuple[VisitUserCode, ...] | tuple[None]:
        """
        id: PV2.7 | len: 2 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.7
        """
        return self._c_data[6]

    @visit_user_code.setter  # set PV2.7
    def visit_user_code(
        self, visit_user_code: VisitUserCode | tuple[VisitUserCode] | None
    ):
        """
        id: PV2.7 | len: 2 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.7
        """
        if isinstance(visit_user_code, tuple):
            self._c_data[6] = visit_user_code
        else:
            self._c_data[6] = (visit_user_code,)

    @property  # get PV2.8
    def expected_admit_date_or_time(self) -> TS | None:
        """
        id: PV2.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.8
        """
        return self._c_data[7][0]

    @expected_admit_date_or_time.setter  # set PV2.8
    def expected_admit_date_or_time(self, ts: TS | None):
        """
        id: PV2.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.8
        """
        self._c_data[7] = (ts,)

    @property  # get PV2.9
    def expected_discharge_date_or_time(self) -> TS | None:
        """
        id: PV2.9 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.9
        """
        return self._c_data[8][0]

    @expected_discharge_date_or_time.setter  # set PV2.9
    def expected_discharge_date_or_time(self, ts: TS | None):
        """
        id: PV2.9 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.9
        """
        self._c_data[8] = (ts,)

    @property  # get PV2.10
    def estimated_length_of_inpatient_stay(self) -> NM | None:
        """
        id: PV2.10 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.10
        """
        return self._c_data[9][0]

    @estimated_length_of_inpatient_stay.setter  # set PV2.10
    def estimated_length_of_inpatient_stay(self, nm: NM | None):
        """
        id: PV2.10 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.10
        """
        self._c_data[9] = (nm,)

    @property  # get PV2.11
    def actual_length_of_inpatient_stay(self) -> NM | None:
        """
        id: PV2.11 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.11
        """
        return self._c_data[10][0]

    @actual_length_of_inpatient_stay.setter  # set PV2.11
    def actual_length_of_inpatient_stay(self, nm: NM | None):
        """
        id: PV2.11 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.11
        """
        self._c_data[10] = (nm,)

    @property  # get PV2.12
    def visit_description(self) -> ST | None:
        """
        id: PV2.12 | len: 50 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.12
        """
        return self._c_data[11][0]

    @visit_description.setter  # set PV2.12
    def visit_description(self, st: ST | None):
        """
        id: PV2.12 | len: 50 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.12
        """
        self._c_data[11] = (st,)

    @property
    def referral_source_code(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: PV2.13 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.13
        """
        return self._c_data[12]

    @referral_source_code.setter  # set PV2.13
    def referral_source_code(self, xcn: XCN | tuple[XCN] | None):
        """
        id: PV2.13 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.13
        """
        if isinstance(xcn, tuple):
            self._c_data[12] = xcn
        else:
            self._c_data[12] = (xcn,)

    @property  # get PV2.14
    def previous_service_date(self) -> DT | None:
        """
        id: PV2.14 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.14
        """
        return self._c_data[13][0]

    @previous_service_date.setter  # set PV2.14
    def previous_service_date(self, dt: DT | None):
        """
        id: PV2.14 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.14
        """
        self._c_data[13] = (dt,)

    @property  # get PV2.15
    def employment_illness_related_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PV2.15 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.15
        """
        return self._c_data[14][0]

    @employment_illness_related_indicator.setter  # set PV2.15
    def employment_illness_related_indicator(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: PV2.15 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.15
        """
        self._c_data[14] = (yes_or_no_indicator,)

    @property  # get PV2.16
    def purge_status_code(self) -> PurgeStatusCode | None:
        """
        id: PV2.16 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.16
        """
        return self._c_data[15][0]

    @purge_status_code.setter  # set PV2.16
    def purge_status_code(self, purge_status_code: PurgeStatusCode | None):
        """
        id: PV2.16 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.16
        """
        self._c_data[15] = (purge_status_code,)

    @property  # get PV2.17
    def purge_status_date(self) -> DT | None:
        """
        id: PV2.17 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.17
        """
        return self._c_data[16][0]

    @purge_status_date.setter  # set PV2.17
    def purge_status_date(self, dt: DT | None):
        """
        id: PV2.17 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.17
        """
        self._c_data[16] = (dt,)

    @property  # get PV2.18
    def special_program_code(self) -> SpecialProgramCode | None:
        """
        id: PV2.18 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.18
        """
        return self._c_data[17][0]

    @special_program_code.setter  # set PV2.18
    def special_program_code(self, special_program_code: SpecialProgramCode | None):
        """
        id: PV2.18 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.18
        """
        self._c_data[17] = (special_program_code,)

    @property  # get PV2.19
    def retention_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PV2.19 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.19
        """
        return self._c_data[18][0]

    @retention_indicator.setter  # set PV2.19
    def retention_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PV2.19 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.19
        """
        self._c_data[18] = (yes_or_no_indicator,)

    @property  # get PV2.20
    def expected_number_of_insurance_plans(self) -> NM | None:
        """
        id: PV2.20 | len: 1 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.20
        """
        return self._c_data[19][0]

    @expected_number_of_insurance_plans.setter  # set PV2.20
    def expected_number_of_insurance_plans(self, nm: NM | None):
        """
        id: PV2.20 | len: 1 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.20
        """
        self._c_data[19] = (nm,)

    @property  # get PV2.21
    def visit_publicity_code(self) -> PublicityCode | None:
        """
        id: PV2.21 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.21
        """
        return self._c_data[20][0]

    @visit_publicity_code.setter  # set PV2.21
    def visit_publicity_code(self, publicity_code: PublicityCode | None):
        """
        id: PV2.21 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.21
        """
        self._c_data[20] = (publicity_code,)

    @property  # get PV2.22
    def visit_protection_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PV2.22 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.22
        """
        return self._c_data[21][0]

    @visit_protection_indicator.setter  # set PV2.22
    def visit_protection_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PV2.22 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.22
        """
        self._c_data[21] = (yes_or_no_indicator,)

    @property
    def clinic_organization_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: PV2.23 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.23
        """
        return self._c_data[22]

    @clinic_organization_name.setter  # set PV2.23
    def clinic_organization_name(self, xon: XON | tuple[XON] | None):
        """
        id: PV2.23 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.23
        """
        if isinstance(xon, tuple):
            self._c_data[22] = xon
        else:
            self._c_data[22] = (xon,)

    @property  # get PV2.24
    def patient_status_code(self) -> PatientStatusCode | None:
        """
        id: PV2.24 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.24
        """
        return self._c_data[23][0]

    @patient_status_code.setter  # set PV2.24
    def patient_status_code(self, patient_status_code: PatientStatusCode | None):
        """
        id: PV2.24 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.24
        """
        self._c_data[23] = (patient_status_code,)

    @property  # get PV2.25
    def visit_priority_code(self) -> VisitPriorityCode | None:
        """
        id: PV2.25 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.25
        """
        return self._c_data[24][0]

    @visit_priority_code.setter  # set PV2.25
    def visit_priority_code(self, visit_priority_code: VisitPriorityCode | None):
        """
        id: PV2.25 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.25
        """
        self._c_data[24] = (visit_priority_code,)

    @property  # get PV2.26
    def previous_treatment_date(self) -> DT | None:
        """
        id: PV2.26 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.26
        """
        return self._c_data[25][0]

    @previous_treatment_date.setter  # set PV2.26
    def previous_treatment_date(self, dt: DT | None):
        """
        id: PV2.26 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.26
        """
        self._c_data[25] = (dt,)

    @property  # get PV2.27
    def expected_discharge_disposition(self) -> DischargeDisposition | None:
        """
        id: PV2.27 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.27
        """
        return self._c_data[26][0]

    @expected_discharge_disposition.setter  # set PV2.27
    def expected_discharge_disposition(
        self, discharge_disposition: DischargeDisposition | None
    ):
        """
        id: PV2.27 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.27
        """
        self._c_data[26] = (discharge_disposition,)

    @property  # get PV2.28
    def signature_on_file_date(self) -> DT | None:
        """
        id: PV2.28 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.28
        """
        return self._c_data[27][0]

    @signature_on_file_date.setter  # set PV2.28
    def signature_on_file_date(self, dt: DT | None):
        """
        id: PV2.28 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.28
        """
        self._c_data[27] = (dt,)

    @property  # get PV2.29
    def first_similar_illness_date(self) -> DT | None:
        """
        id: PV2.29 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.29
        """
        return self._c_data[28][0]

    @first_similar_illness_date.setter  # set PV2.29
    def first_similar_illness_date(self, dt: DT | None):
        """
        id: PV2.29 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.29
        """
        self._c_data[28] = (dt,)

    @property  # get PV2.30
    def patient_charge_adjustment_code(self) -> PatientChargeAdjustment | None:
        """
        id: PV2.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.30
        """
        return self._c_data[29][0]

    @patient_charge_adjustment_code.setter  # set PV2.30
    def patient_charge_adjustment_code(
        self, patient_charge_adjustment: PatientChargeAdjustment | None
    ):
        """
        id: PV2.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.30
        """
        self._c_data[29] = (patient_charge_adjustment,)

    @property  # get PV2.31
    def recurring_service_code(self) -> RecurringServiceCode | None:
        """
        id: PV2.31 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.31
        """
        return self._c_data[30][0]

    @recurring_service_code.setter  # set PV2.31
    def recurring_service_code(
        self, recurring_service_code: RecurringServiceCode | None
    ):
        """
        id: PV2.31 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.31
        """
        self._c_data[30] = (recurring_service_code,)

    @property  # get PV2.32
    def billing_media_code(self) -> YesOrNoIndicator | None:
        """
        id: PV2.32 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.32
        """
        return self._c_data[31][0]

    @billing_media_code.setter  # set PV2.32
    def billing_media_code(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PV2.32 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.32
        """
        self._c_data[31] = (yes_or_no_indicator,)

    @property  # get PV2.33
    def expected_surgery_date_and_time(self) -> TS | None:
        """
        id: PV2.33 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.33
        """
        return self._c_data[32][0]

    @expected_surgery_date_and_time.setter  # set PV2.33
    def expected_surgery_date_and_time(self, ts: TS | None):
        """
        id: PV2.33 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.33
        """
        self._c_data[32] = (ts,)

    @property  # get PV2.34
    def military_partnership_code(self) -> YesOrNoIndicator | None:
        """
        id: PV2.34 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.34
        """
        return self._c_data[33][0]

    @military_partnership_code.setter  # set PV2.34
    def military_partnership_code(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PV2.34 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.34
        """
        self._c_data[33] = (yes_or_no_indicator,)

    @property  # get PV2.35
    def military_non_availability_code(self) -> YesOrNoIndicator | None:
        """
        id: PV2.35 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.35
        """
        return self._c_data[34][0]

    @military_non_availability_code.setter  # set PV2.35
    def military_non_availability_code(
        self, yes_or_no_indicator: YesOrNoIndicator | None
    ):
        """
        id: PV2.35 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.35
        """
        self._c_data[34] = (yes_or_no_indicator,)

    @property  # get PV2.36
    def newborn_baby_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PV2.36 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.36
        """
        return self._c_data[35][0]

    @newborn_baby_indicator.setter  # set PV2.36
    def newborn_baby_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PV2.36 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.36
        """
        self._c_data[35] = (yes_or_no_indicator,)

    @property  # get PV2.37
    def baby_detained_indicator(self) -> YesOrNoIndicator | None:
        """
        id: PV2.37 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.37
        """
        return self._c_data[36][0]

    @baby_detained_indicator.setter  # set PV2.37
    def baby_detained_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PV2.37 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.37
        """
        self._c_data[36] = (yes_or_no_indicator,)

    @property  # get PV2.38
    def mode_of_arrival_code(self) -> ModeOfArrivalCode | None:
        """
        id: PV2.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.38
        """
        return self._c_data[37][0]

    @mode_of_arrival_code.setter  # set PV2.38
    def mode_of_arrival_code(self, mode_of_arrival_code: ModeOfArrivalCode | None):
        """
        id: PV2.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.38
        """
        self._c_data[37] = (mode_of_arrival_code,)

    @property
    def recreational_drug_use_code(
        self,
    ) -> tuple[RecreationalDrugUseCode, ...] | tuple[None]:
        """
        id: PV2.39 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.39
        """
        return self._c_data[38]

    @recreational_drug_use_code.setter  # set PV2.39
    def recreational_drug_use_code(
        self,
        recreational_drug_use_code: RecreationalDrugUseCode
        | tuple[RecreationalDrugUseCode]
        | None,
    ):
        """
        id: PV2.39 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.39
        """
        if isinstance(recreational_drug_use_code, tuple):
            self._c_data[38] = recreational_drug_use_code
        else:
            self._c_data[38] = (recreational_drug_use_code,)

    @property  # get PV2.40
    def admission_level_of_care_code(self) -> AdmissionLevelOfCareCode | None:
        """
        id: PV2.40 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.40
        """
        return self._c_data[39][0]

    @admission_level_of_care_code.setter  # set PV2.40
    def admission_level_of_care_code(
        self, admission_level_of_care_code: AdmissionLevelOfCareCode | None
    ):
        """
        id: PV2.40 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.40
        """
        self._c_data[39] = (admission_level_of_care_code,)

    @property
    def precaution_code(self) -> tuple[PrecautionCode, ...] | tuple[None]:
        """
        id: PV2.41 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.41
        """
        return self._c_data[40]

    @precaution_code.setter  # set PV2.41
    def precaution_code(
        self, precaution_code: PrecautionCode | tuple[PrecautionCode] | None
    ):
        """
        id: PV2.41 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.41
        """
        if isinstance(precaution_code, tuple):
            self._c_data[40] = precaution_code
        else:
            self._c_data[40] = (precaution_code,)

    @property  # get PV2.42
    def patient_condition_code(self) -> PatientConditionCode | None:
        """
        id: PV2.42 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.42
        """
        return self._c_data[41][0]

    @patient_condition_code.setter  # set PV2.42
    def patient_condition_code(
        self, patient_condition_code: PatientConditionCode | None
    ):
        """
        id: PV2.42 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.42
        """
        self._c_data[41] = (patient_condition_code,)

    @property  # get PV2.43
    def living_will_code(self) -> LivingWillCode | None:
        """
        id: PV2.43 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.43
        """
        return self._c_data[42][0]

    @living_will_code.setter  # set PV2.43
    def living_will_code(self, living_will_code: LivingWillCode | None):
        """
        id: PV2.43 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.43
        """
        self._c_data[42] = (living_will_code,)

    @property  # get PV2.44
    def organ_donor_code(self) -> OrganDonorCode | None:
        """
        id: PV2.44 | len: 2 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.44
        """
        return self._c_data[43][0]

    @organ_donor_code.setter  # set PV2.44
    def organ_donor_code(self, organ_donor_code: OrganDonorCode | None):
        """
        id: PV2.44 | len: 2 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.44
        """
        self._c_data[43] = (organ_donor_code,)

    @property
    def advance_directive_code(self) -> tuple[AdvanceDirectiveCode, ...] | tuple[None]:
        """
        id: PV2.45 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.45
        """
        return self._c_data[44]

    @advance_directive_code.setter  # set PV2.45
    def advance_directive_code(
        self,
        advance_directive_code: AdvanceDirectiveCode
        | tuple[AdvanceDirectiveCode]
        | None,
    ):
        """
        id: PV2.45 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.45
        """
        if isinstance(advance_directive_code, tuple):
            self._c_data[44] = advance_directive_code
        else:
            self._c_data[44] = (advance_directive_code,)

    @property  # get PV2.46
    def patient_status_effective_date(self) -> DT | None:
        """
        id: PV2.46 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.46
        """
        return self._c_data[45][0]

    @patient_status_effective_date.setter  # set PV2.46
    def patient_status_effective_date(self, dt: DT | None):
        """
        id: PV2.46 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.46
        """
        self._c_data[45] = (dt,)

    @property  # get PV2.47
    def expected_loa_return_date_or_time(self) -> TS | None:
        """
        id: PV2.47 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.47
        """
        return self._c_data[46][0]

    @expected_loa_return_date_or_time.setter  # set PV2.47
    def expected_loa_return_date_or_time(self, ts: TS | None):
        """
        id: PV2.47 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.47
        """
        self._c_data[46] = (ts,)

    @property  # get PV2.48
    def expected_pre_admission_testing_date_or_time(self) -> TS | None:
        """
        id: PV2.48 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.48
        """
        return self._c_data[47][0]

    @expected_pre_admission_testing_date_or_time.setter  # set PV2.48
    def expected_pre_admission_testing_date_or_time(self, ts: TS | None):
        """
        id: PV2.48 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.48
        """
        self._c_data[47] = (ts,)

    @property
    def notify_clergy_code(self) -> tuple[NotifyClergyCode, ...] | tuple[None]:
        """
        id: PV2.49 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.49
        """
        return self._c_data[48]

    @notify_clergy_code.setter  # set PV2.49
    def notify_clergy_code(
        self, notify_clergy_code: NotifyClergyCode | tuple[NotifyClergyCode] | None
    ):
        """
        id: PV2.49 | len: 20 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PV2.49
        """
        if isinstance(notify_clergy_code, tuple):
            self._c_data[48] = notify_clergy_code
        else:
            self._c_data[48] = (notify_clergy_code,)
