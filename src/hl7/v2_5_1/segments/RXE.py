from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TQ import TQ
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.CWE import CWE
from ..data_types.LA1 import LA1
from ..data_types.XAD import XAD
from ..data_types.PL import PL
from ..data_types.TS import TS
from ..tables.SubstitutionStatus import SubstitutionStatus
from ..tables.DispenseMethod import DispenseMethod
from ..tables.PharmacyOrderTypes import PharmacyOrderTypes
from ..tables.ControlledSubstanceSchedule_ import ControlledSubstanceSchedule_
from ..tables.FormularyStatus import FormularyStatus
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Pharmacy/Treatment Encoded Order - RXE
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXE TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXE,
    CE, TQ, CQ, ID, NM, ST, XCN, CWE, LA1, XAD, PL, TS
)

rxe = RXE(  #  - The RXE segment details the pharmacy or treatment application's encoding of the order
    quantity_or_timing=None,  # TQ(...) 
    give_code=ce,  # CE(...)  # Required.
    give_amount_minimum=nm,  # NM(...)  # Required.
    give_amount_maximum=None,  # NM(...) 
    give_units=ce,  # CE(...)  # Required.
    give_dosage_form=None,  # CE(...) 
    providers_administration_instructions=None,  # CE(...) 
    deliver_to_location=None,  # LA1(...) 
    substitution_status=None,  # ID(...) 
    dispense_amount=None,  # NM(...) 
    dispense_units=None,  # CE(...) 
    number_of_refills=None,  # NM(...) 
    ordering_providers_dea_number=None,  # XCN(...) 
    pharmacist_or_treatment_suppliers_verifier_id=None,  # XCN(...) 
    prescription_number=None,  # ST(...) 
    number_of_refills_remaining=None,  # NM(...) 
    number_of_refills_or_doses_dispensed=None,  # NM(...) 
    d_or_t_of_most_recent_refill_or_dose_dispensed=None,  # TS(...) 
    total_daily_dose=None,  # CQ(...) 
    needs_human_review=None,  # ID(...) 
    pharmacy_or_treatment_suppliers_special_dispensing_instructions=None,  # CE(...) 
    give_per=None,  # ST(...) 
    give_rate_amount=None,  # ST(...) 
    give_rate_units=None,  # CE(...) 
    give_strength=None,  # NM(...) 
    give_strength_units=None,  # CE(...) 
    give_indication=None,  # CE(...) 
    dispense_package_size=None,  # NM(...) 
    dispense_package_size_unit=None,  # CE(...) 
    dispense_package_method=None,  # ID(...) 
    supplementary_code=None,  # CE(...) 
    original_order_date_or_time=None,  # TS(...) 
    give_drug_strength_volume=None,  # NM(...) 
    give_drug_strength_volume_units=None,  # CWE(...) 
    controlled_substance_schedule=None,  # CWE(...) 
    formulary_status=None,  # ID(...) 
    pharmaceutical_substance_alternative=None,  # CWE(...) 
    pharmacy_of_most_recent_fill=None,  # CWE(...) 
    initial_dispense_amount=None,  # NM(...) 
    dispensing_pharmacy=None,  # CWE(...) 
    dispensing_pharmacy_address=None,  # XAD(...) 
    deliver_to_patient_location=None,  # PL(...) 
    deliver_to_address=None,  # XAD(...) 
    pharmacy_order_type=None,  # ID(...) 
)

-----END SEGMENT::RXE TEMPLATE-----
"""


class RXE(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXE"""
    _hl7_name = """Pharmacy/Treatment Encoded Order"""
    _hl7_description = """The RXE segment details the pharmacy or treatment application's encoding of the order"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE"
    _c_length = (200, 250, 20, 20, 250, 250, 250, 200, 1, 20, 250, 3, 250, 250, 20, 20, 20, 26, 10, 1, 250, 20, 6, 250, 20, 250, 250, 20, 250, 2, 250, 26, 5, 250, 60, 1, 60, 250, 250, 250, 250, 80, 250, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("B", "R", "R", "O", "R", "O", "O", "B", "O", "C", "C", "O", "C", "O", "C", "C", "C", "C", "C", "O", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (TQ, CE, NM, NM, CE, CE, CE, LA1, ID, NM, CE, NM, XCN, XCN, ST, NM, NM, TS, CQ, ID, CE, ST, ST, CE, NM, CE, CE, NM, CE, ID, CE, TS, NM, CWE, CWE, ID, CWE, CWE, NM, CWE, XAD, PL, XAD, ID,)
    _c_aliases = ("RXE.1", "RXE.2", "RXE.3", "RXE.4", "RXE.5", "RXE.6", "RXE.7", "RXE.8", "RXE.9", "RXE.10", "RXE.11", "RXE.12", "RXE.13", "RXE.14", "RXE.15", "RXE.16", "RXE.17", "RXE.18", "RXE.19", "RXE.20", "RXE.21", "RXE.22", "RXE.23", "RXE.24", "RXE.25", "RXE.26", "RXE.27", "RXE.28", "RXE.29", "RXE.30", "RXE.31", "RXE.32", "RXE.33", "RXE.34", "RXE.35", "RXE.36", "RXE.37", "RXE.38", "RXE.39", "RXE.40", "RXE.41", "RXE.42", "RXE.43", "RXE.44",)
    _c_names = ("Quantity/Timing", "Give Code", "Give Amount - Minimum", "Give Amount - Maximum", "Give Units", "Give Dosage Form", "Provider's Administration Instructions", "Deliver-To Location", "Substitution Status", "Dispense Amount", "Dispense Units", "Number Of Refills", "Ordering Provider's DEA Number", "Pharmacist/Treatment Supplier's Verifier ID", "Prescription Number", "Number of Refills Remaining", "Number of Refills/Doses Dispensed", "D/T of Most Recent Refill or Dose Dispensed", "Total Daily Dose", "Needs Human Review", "Pharmacy/Treatment Supplier's Special Dispensing Instructions", "Give Per (Time Units)", "Give Rate Amount", "Give Rate Units", "Give Strength", "Give Strength Units", "Give Indication", "Dispense Package Size", "Dispense Package Size Unit", "Dispense Package Method", "Supplementary Code", "Original Order Date/Time", "Give Drug Strength Volume", "Give Drug Strength Volume Units", "Controlled Substance Schedule", "Formulary Status", "Pharmaceutical Substance Alternative", "Pharmacy of Most Recent Fill", "Initial Dispense Amount", "Dispensing Pharmacy", "Dispensing Pharmacy Address", "Deliver-to Patient Location", "Deliver-to Address", "Pharmacy Order Type",)
    _c_attrs = ("quantity_or_timing", "give_code", "give_amount_minimum", "give_amount_maximum", "give_units", "give_dosage_form", "providers_administration_instructions", "deliver_to_location", "substitution_status", "dispense_amount", "dispense_units", "number_of_refills", "ordering_providers_dea_number", "pharmacist_or_treatment_suppliers_verifier_id", "prescription_number", "number_of_refills_remaining", "number_of_refills_or_doses_dispensed", "d_or_t_of_most_recent_refill_or_dose_dispensed", "total_daily_dose", "needs_human_review", "pharmacy_or_treatment_suppliers_special_dispensing_instructions", "give_per", "give_rate_amount", "give_rate_units", "give_strength", "give_strength_units", "give_indication", "dispense_package_size", "dispense_package_size_unit", "dispense_package_method", "supplementary_code", "original_order_date_or_time", "give_drug_strength_volume", "give_drug_strength_volume_units", "controlled_substance_schedule", "formulary_status", "pharmaceutical_substance_alternative", "pharmacy_of_most_recent_fill", "initial_dispense_amount", "dispensing_pharmacy", "dispensing_pharmacy_address", "deliver_to_patient_location", "deliver_to_address", "pharmacy_order_type",)
    # fmt: on

    def __init__(
        self,
        give_code: CE,  # RXE.2
        give_amount_minimum: NM,  # RXE.3
        give_units: CE,  # RXE.5
        quantity_or_timing: TQ | None = None,  # RXE.1
        give_amount_maximum: NM | None = None,  # RXE.4
        give_dosage_form: CE | None = None,  # RXE.6
        providers_administration_instructions: CE | None = None,  # RXE.7
        deliver_to_location: LA1 | None = None,  # RXE.8
        substitution_status: SubstitutionStatus | ID | None = None,  # RXE.9
        dispense_amount: NM | None = None,  # RXE.10
        dispense_units: CE | None = None,  # RXE.11
        number_of_refills: NM | None = None,  # RXE.12
        ordering_providers_dea_number: XCN | None = None,  # RXE.13
        pharmacist_or_treatment_suppliers_verifier_id: XCN | None = None,  # RXE.14
        prescription_number: ST | None = None,  # RXE.15
        number_of_refills_remaining: NM | None = None,  # RXE.16
        number_of_refills_or_doses_dispensed: NM | None = None,  # RXE.17
        d_or_t_of_most_recent_refill_or_dose_dispensed: TS | None = None,  # RXE.18
        total_daily_dose: CQ | None = None,  # RXE.19
        needs_human_review: YesOrNoIndicator | ID | None = None,  # RXE.20
        pharmacy_or_treatment_suppliers_special_dispensing_instructions: CE
        | None = None,  # RXE.21
        give_per: ST | None = None,  # RXE.22
        give_rate_amount: ST | None = None,  # RXE.23
        give_rate_units: CE | None = None,  # RXE.24
        give_strength: NM | None = None,  # RXE.25
        give_strength_units: CE | None = None,  # RXE.26
        give_indication: CE | None = None,  # RXE.27
        dispense_package_size: NM | None = None,  # RXE.28
        dispense_package_size_unit: CE | None = None,  # RXE.29
        dispense_package_method: DispenseMethod | ID | None = None,  # RXE.30
        supplementary_code: CE | None = None,  # RXE.31
        original_order_date_or_time: TS | None = None,  # RXE.32
        give_drug_strength_volume: NM | None = None,  # RXE.33
        give_drug_strength_volume_units: CWE | None = None,  # RXE.34
        controlled_substance_schedule: ControlledSubstanceSchedule_
        | CWE
        | None = None,  # RXE.35
        formulary_status: FormularyStatus | ID | None = None,  # RXE.36
        pharmaceutical_substance_alternative: CWE | None = None,  # RXE.37
        pharmacy_of_most_recent_fill: CWE | None = None,  # RXE.38
        initial_dispense_amount: NM | None = None,  # RXE.39
        dispensing_pharmacy: CWE | None = None,  # RXE.40
        dispensing_pharmacy_address: XAD | None = None,  # RXE.41
        deliver_to_patient_location: PL | None = None,  # RXE.42
        deliver_to_address: XAD | None = None,  # RXE.43
        pharmacy_order_type: PharmacyOrderTypes | ID | None = None,  # RXE.44
    ):
        """
        Pharmacy/Treatment Encoded Order - `RXE <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE>`_
        The RXE segment details the pharmacy or treatment application's encoding of the order. It also contains several pharmacy-specific order status fields, such as RXE-16-number of refills remaining, RXE-17-number of refills/doses dispensed, RXE-18-D/T of most recent refill or dose dispensed, and RXE-19-total daily dose.

        :param quantity_or_timing: Timing Quantity (id: RXE.1 | len: 200 | use: B | rpt: 1)
        :param give_code: Coded Element (id: RXE.2 | len: 250 | use: R | rpt: 1)
        :param give_amount_minimum: Numeric (id: RXE.3 | len: 20 | use: R | rpt: 1)
        :param give_amount_maximum: Numeric (id: RXE.4 | len: 20 | use: O | rpt: 1)
        :param give_units: Coded Element (id: RXE.5 | len: 250 | use: R | rpt: 1)
        :param give_dosage_form: Coded Element (id: RXE.6 | len: 250 | use: O | rpt: 1)
        :param providers_administration_instructions: Coded Element (id: RXE.7 | len: 250 | use: O | rpt: *)
        :param deliver_to_location: Location with Address Variation 1 (id: RXE.8 | len: 200 | use: B | rpt: 1)
        :param substitution_status: Coded values for HL7 tables (id: RXE.9 | len: 1 | use: O | rpt: 1)
        :param dispense_amount: Numeric (id: RXE.10 | len: 20 | use: C | rpt: 1)
        :param dispense_units: Coded Element (id: RXE.11 | len: 250 | use: C | rpt: 1)
        :param number_of_refills: Numeric (id: RXE.12 | len: 3 | use: O | rpt: 1)
        :param ordering_providers_dea_number: Extended Composite ID Number and Name for Persons (id: RXE.13 | len: 250 | use: C | rpt: *)
        :param pharmacist_or_treatment_suppliers_verifier_id: Extended Composite ID Number and Name for Persons (id: RXE.14 | len: 250 | use: O | rpt: *)
        :param prescription_number: String Data (id: RXE.15 | len: 20 | use: C | rpt: 1)
        :param number_of_refills_remaining: Numeric (id: RXE.16 | len: 20 | use: C | rpt: 1)
        :param number_of_refills_or_doses_dispensed: Numeric (id: RXE.17 | len: 20 | use: C | rpt: 1)
        :param d_or_t_of_most_recent_refill_or_dose_dispensed: Time Stamp (id: RXE.18 | len: 26 | use: C | rpt: 1)
        :param total_daily_dose: Composite Quantity with Units (id: RXE.19 | len: 10 | use: C | rpt: 1)
        :param needs_human_review: Coded values for HL7 tables (id: RXE.20 | len: 1 | use: O | rpt: 1)
        :param pharmacy_or_treatment_suppliers_special_dispensing_instructions: Coded Element (id: RXE.21 | len: 250 | use: O | rpt: *)
        :param give_per: String Data (id: RXE.22 | len: 20 | use: C | rpt: 1)
        :param give_rate_amount: String Data (id: RXE.23 | len: 6 | use: O | rpt: 1)
        :param give_rate_units: Coded Element (id: RXE.24 | len: 250 | use: O | rpt: 1)
        :param give_strength: Numeric (id: RXE.25 | len: 20 | use: O | rpt: 1)
        :param give_strength_units: Coded Element (id: RXE.26 | len: 250 | use: O | rpt: 1)
        :param give_indication: Coded Element (id: RXE.27 | len: 250 | use: O | rpt: *)
        :param dispense_package_size: Numeric (id: RXE.28 | len: 20 | use: O | rpt: 1)
        :param dispense_package_size_unit: Coded Element (id: RXE.29 | len: 250 | use: O | rpt: 1)
        :param dispense_package_method: Coded values for HL7 tables (id: RXE.30 | len: 2 | use: O | rpt: 1)
        :param supplementary_code: Coded Element (id: RXE.31 | len: 250 | use: O | rpt: *)
        :param original_order_date_or_time: Time Stamp (id: RXE.32 | len: 26 | use: O | rpt: 1)
        :param give_drug_strength_volume: Numeric (id: RXE.33 | len: 5 | use: O | rpt: 1)
        :param give_drug_strength_volume_units: Coded with Exceptions (id: RXE.34 | len: 250 | use: O | rpt: 1)
        :param controlled_substance_schedule: Coded with Exceptions (id: RXE.35 | len: 60 | use: O | rpt: 1)
        :param formulary_status: Coded values for HL7 tables (id: RXE.36 | len: 1 | use: O | rpt: 1)
        :param pharmaceutical_substance_alternative: Coded with Exceptions (id: RXE.37 | len: 60 | use: O | rpt: *)
        :param pharmacy_of_most_recent_fill: Coded with Exceptions (id: RXE.38 | len: 250 | use: O | rpt: 1)
        :param initial_dispense_amount: Numeric (id: RXE.39 | len: 250 | use: O | rpt: 1)
        :param dispensing_pharmacy: Coded with Exceptions (id: RXE.40 | len: 250 | use: O | rpt: 1)
        :param dispensing_pharmacy_address: Extended Address (id: RXE.41 | len: 250 | use: O | rpt: 1)
        :param deliver_to_patient_location: Person Location (id: RXE.42 | len: 80 | use: O | rpt: 1)
        :param deliver_to_address: Extended Address (id: RXE.43 | len: 250 | use: O | rpt: 1)
        :param pharmacy_order_type: Coded values for HL7 tables (id: RXE.44 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 44
        self.quantity_or_timing = quantity_or_timing
        self.give_code = give_code
        self.give_amount_minimum = give_amount_minimum
        self.give_amount_maximum = give_amount_maximum
        self.give_units = give_units
        self.give_dosage_form = give_dosage_form
        self.providers_administration_instructions = (
            providers_administration_instructions
        )
        self.deliver_to_location = deliver_to_location
        self.substitution_status = substitution_status
        self.dispense_amount = dispense_amount
        self.dispense_units = dispense_units
        self.number_of_refills = number_of_refills
        self.ordering_providers_dea_number = ordering_providers_dea_number
        self.pharmacist_or_treatment_suppliers_verifier_id = (
            pharmacist_or_treatment_suppliers_verifier_id
        )
        self.prescription_number = prescription_number
        self.number_of_refills_remaining = number_of_refills_remaining
        self.number_of_refills_or_doses_dispensed = number_of_refills_or_doses_dispensed
        self.d_or_t_of_most_recent_refill_or_dose_dispensed = (
            d_or_t_of_most_recent_refill_or_dose_dispensed
        )
        self.total_daily_dose = total_daily_dose
        self.needs_human_review = needs_human_review
        self.pharmacy_or_treatment_suppliers_special_dispensing_instructions = (
            pharmacy_or_treatment_suppliers_special_dispensing_instructions
        )
        self.give_per = give_per
        self.give_rate_amount = give_rate_amount
        self.give_rate_units = give_rate_units
        self.give_strength = give_strength
        self.give_strength_units = give_strength_units
        self.give_indication = give_indication
        self.dispense_package_size = dispense_package_size
        self.dispense_package_size_unit = dispense_package_size_unit
        self.dispense_package_method = dispense_package_method
        self.supplementary_code = supplementary_code
        self.original_order_date_or_time = original_order_date_or_time
        self.give_drug_strength_volume = give_drug_strength_volume
        self.give_drug_strength_volume_units = give_drug_strength_volume_units
        self.controlled_substance_schedule = controlled_substance_schedule
        self.formulary_status = formulary_status
        self.pharmaceutical_substance_alternative = pharmaceutical_substance_alternative
        self.pharmacy_of_most_recent_fill = pharmacy_of_most_recent_fill
        self.initial_dispense_amount = initial_dispense_amount
        self.dispensing_pharmacy = dispensing_pharmacy
        self.dispensing_pharmacy_address = dispensing_pharmacy_address
        self.deliver_to_patient_location = deliver_to_patient_location
        self.deliver_to_address = deliver_to_address
        self.pharmacy_order_type = pharmacy_order_type

    @property  # get RXE.1
    def quantity_or_timing(self) -> TQ | None:
        """
        id: RXE.1 | len: 200 | use: B | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.1
        """
        return self._c_data[0][0]

    @quantity_or_timing.setter  # set RXE.1
    def quantity_or_timing(self, tq: TQ | None):
        """
        id: RXE.1 | len: 200 | use: B | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.1
        """
        self._c_data[0] = (tq,)

    @property  # get RXE.2
    def give_code(self) -> CE:
        """
        id: RXE.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.2
        """
        return self._c_data[1][0]

    @give_code.setter  # set RXE.2
    def give_code(self, ce: CE):
        """
        id: RXE.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.2
        """
        self._c_data[1] = (ce,)

    @property  # get RXE.3
    def give_amount_minimum(self) -> NM:
        """
        id: RXE.3 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.3
        """
        return self._c_data[2][0]

    @give_amount_minimum.setter  # set RXE.3
    def give_amount_minimum(self, nm: NM):
        """
        id: RXE.3 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.3
        """
        self._c_data[2] = (nm,)

    @property  # get RXE.4
    def give_amount_maximum(self) -> NM | None:
        """
        id: RXE.4 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.4
        """
        return self._c_data[3][0]

    @give_amount_maximum.setter  # set RXE.4
    def give_amount_maximum(self, nm: NM | None):
        """
        id: RXE.4 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.4
        """
        self._c_data[3] = (nm,)

    @property  # get RXE.5
    def give_units(self) -> CE:
        """
        id: RXE.5 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.5
        """
        return self._c_data[4][0]

    @give_units.setter  # set RXE.5
    def give_units(self, ce: CE):
        """
        id: RXE.5 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.5
        """
        self._c_data[4] = (ce,)

    @property  # get RXE.6
    def give_dosage_form(self) -> CE | None:
        """
        id: RXE.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.6
        """
        return self._c_data[5][0]

    @give_dosage_form.setter  # set RXE.6
    def give_dosage_form(self, ce: CE | None):
        """
        id: RXE.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.6
        """
        self._c_data[5] = (ce,)

    @property
    def providers_administration_instructions(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXE.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.7
        """
        return self._c_data[6]

    @providers_administration_instructions.setter  # set RXE.7
    def providers_administration_instructions(self, ce: CE | tuple[CE] | None):
        """
        id: RXE.7 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.7
        """
        if isinstance(ce, tuple):
            self._c_data[6] = ce
        else:
            self._c_data[6] = (ce,)

    @property  # get RXE.8
    def deliver_to_location(self) -> LA1 | None:
        """
        id: RXE.8 | len: 200 | use: B | rpt: 1
        ---
        return_type: LA1: Location with Address Variation 1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.8
        """
        return self._c_data[7][0]

    @deliver_to_location.setter  # set RXE.8
    def deliver_to_location(self, la1: LA1 | None):
        """
        id: RXE.8 | len: 200 | use: B | rpt: 1
        ---
        param_type: LA1: Location with Address Variation 1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.8
        """
        self._c_data[7] = (la1,)

    @property  # get RXE.9
    def substitution_status(self) -> SubstitutionStatus | None:
        """
        id: RXE.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.9
        """
        return self._c_data[8][0]

    @substitution_status.setter  # set RXE.9
    def substitution_status(self, substitution_status: SubstitutionStatus | None):
        """
        id: RXE.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.9
        """
        self._c_data[8] = (substitution_status,)

    @property  # get RXE.10
    def dispense_amount(self) -> NM | None:
        """
        id: RXE.10 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.10
        """
        return self._c_data[9][0]

    @dispense_amount.setter  # set RXE.10
    def dispense_amount(self, nm: NM | None):
        """
        id: RXE.10 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.10
        """
        self._c_data[9] = (nm,)

    @property  # get RXE.11
    def dispense_units(self) -> CE | None:
        """
        id: RXE.11 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.11
        """
        return self._c_data[10][0]

    @dispense_units.setter  # set RXE.11
    def dispense_units(self, ce: CE | None):
        """
        id: RXE.11 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.11
        """
        self._c_data[10] = (ce,)

    @property  # get RXE.12
    def number_of_refills(self) -> NM | None:
        """
        id: RXE.12 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.12
        """
        return self._c_data[11][0]

    @number_of_refills.setter  # set RXE.12
    def number_of_refills(self, nm: NM | None):
        """
        id: RXE.12 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.12
        """
        self._c_data[11] = (nm,)

    @property
    def ordering_providers_dea_number(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: RXE.13 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.13
        """
        return self._c_data[12]

    @ordering_providers_dea_number.setter  # set RXE.13
    def ordering_providers_dea_number(self, xcn: XCN | tuple[XCN] | None):
        """
        id: RXE.13 | len: 250 | use: C | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.13
        """
        if isinstance(xcn, tuple):
            self._c_data[12] = xcn
        else:
            self._c_data[12] = (xcn,)

    @property
    def pharmacist_or_treatment_suppliers_verifier_id(
        self,
    ) -> tuple[XCN, ...] | tuple[None]:
        """
        id: RXE.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.14
        """
        return self._c_data[13]

    @pharmacist_or_treatment_suppliers_verifier_id.setter  # set RXE.14
    def pharmacist_or_treatment_suppliers_verifier_id(
        self, xcn: XCN | tuple[XCN] | None
    ):
        """
        id: RXE.14 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.14
        """
        if isinstance(xcn, tuple):
            self._c_data[13] = xcn
        else:
            self._c_data[13] = (xcn,)

    @property  # get RXE.15
    def prescription_number(self) -> ST | None:
        """
        id: RXE.15 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.15
        """
        return self._c_data[14][0]

    @prescription_number.setter  # set RXE.15
    def prescription_number(self, st: ST | None):
        """
        id: RXE.15 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.15
        """
        self._c_data[14] = (st,)

    @property  # get RXE.16
    def number_of_refills_remaining(self) -> NM | None:
        """
        id: RXE.16 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.16
        """
        return self._c_data[15][0]

    @number_of_refills_remaining.setter  # set RXE.16
    def number_of_refills_remaining(self, nm: NM | None):
        """
        id: RXE.16 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.16
        """
        self._c_data[15] = (nm,)

    @property  # get RXE.17
    def number_of_refills_or_doses_dispensed(self) -> NM | None:
        """
        id: RXE.17 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.17
        """
        return self._c_data[16][0]

    @number_of_refills_or_doses_dispensed.setter  # set RXE.17
    def number_of_refills_or_doses_dispensed(self, nm: NM | None):
        """
        id: RXE.17 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.17
        """
        self._c_data[16] = (nm,)

    @property  # get RXE.18
    def d_or_t_of_most_recent_refill_or_dose_dispensed(self) -> TS | None:
        """
        id: RXE.18 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.18
        """
        return self._c_data[17][0]

    @d_or_t_of_most_recent_refill_or_dose_dispensed.setter  # set RXE.18
    def d_or_t_of_most_recent_refill_or_dose_dispensed(self, ts: TS | None):
        """
        id: RXE.18 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.18
        """
        self._c_data[17] = (ts,)

    @property  # get RXE.19
    def total_daily_dose(self) -> CQ | None:
        """
        id: RXE.19 | len: 10 | use: C | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.19
        """
        return self._c_data[18][0]

    @total_daily_dose.setter  # set RXE.19
    def total_daily_dose(self, cq: CQ | None):
        """
        id: RXE.19 | len: 10 | use: C | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.19
        """
        self._c_data[18] = (cq,)

    @property  # get RXE.20
    def needs_human_review(self) -> YesOrNoIndicator | None:
        """
        id: RXE.20 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.20
        """
        return self._c_data[19][0]

    @needs_human_review.setter  # set RXE.20
    def needs_human_review(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RXE.20 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.20
        """
        self._c_data[19] = (yes_or_no_indicator,)

    @property
    def pharmacy_or_treatment_suppliers_special_dispensing_instructions(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXE.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.21
        """
        return self._c_data[20]

    @pharmacy_or_treatment_suppliers_special_dispensing_instructions.setter  # set RXE.21
    def pharmacy_or_treatment_suppliers_special_dispensing_instructions(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: RXE.21 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.21
        """
        if isinstance(ce, tuple):
            self._c_data[20] = ce
        else:
            self._c_data[20] = (ce,)

    @property  # get RXE.22
    def give_per(self) -> ST | None:
        """
        id: RXE.22 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.22
        """
        return self._c_data[21][0]

    @give_per.setter  # set RXE.22
    def give_per(self, st: ST | None):
        """
        id: RXE.22 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.22
        """
        self._c_data[21] = (st,)

    @property  # get RXE.23
    def give_rate_amount(self) -> ST | None:
        """
        id: RXE.23 | len: 6 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.23
        """
        return self._c_data[22][0]

    @give_rate_amount.setter  # set RXE.23
    def give_rate_amount(self, st: ST | None):
        """
        id: RXE.23 | len: 6 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.23
        """
        self._c_data[22] = (st,)

    @property  # get RXE.24
    def give_rate_units(self) -> CE | None:
        """
        id: RXE.24 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.24
        """
        return self._c_data[23][0]

    @give_rate_units.setter  # set RXE.24
    def give_rate_units(self, ce: CE | None):
        """
        id: RXE.24 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.24
        """
        self._c_data[23] = (ce,)

    @property  # get RXE.25
    def give_strength(self) -> NM | None:
        """
        id: RXE.25 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.25
        """
        return self._c_data[24][0]

    @give_strength.setter  # set RXE.25
    def give_strength(self, nm: NM | None):
        """
        id: RXE.25 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.25
        """
        self._c_data[24] = (nm,)

    @property  # get RXE.26
    def give_strength_units(self) -> CE | None:
        """
        id: RXE.26 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.26
        """
        return self._c_data[25][0]

    @give_strength_units.setter  # set RXE.26
    def give_strength_units(self, ce: CE | None):
        """
        id: RXE.26 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.26
        """
        self._c_data[25] = (ce,)

    @property
    def give_indication(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXE.27 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.27
        """
        return self._c_data[26]

    @give_indication.setter  # set RXE.27
    def give_indication(self, ce: CE | tuple[CE] | None):
        """
        id: RXE.27 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.27
        """
        if isinstance(ce, tuple):
            self._c_data[26] = ce
        else:
            self._c_data[26] = (ce,)

    @property  # get RXE.28
    def dispense_package_size(self) -> NM | None:
        """
        id: RXE.28 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.28
        """
        return self._c_data[27][0]

    @dispense_package_size.setter  # set RXE.28
    def dispense_package_size(self, nm: NM | None):
        """
        id: RXE.28 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.28
        """
        self._c_data[27] = (nm,)

    @property  # get RXE.29
    def dispense_package_size_unit(self) -> CE | None:
        """
        id: RXE.29 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.29
        """
        return self._c_data[28][0]

    @dispense_package_size_unit.setter  # set RXE.29
    def dispense_package_size_unit(self, ce: CE | None):
        """
        id: RXE.29 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.29
        """
        self._c_data[28] = (ce,)

    @property  # get RXE.30
    def dispense_package_method(self) -> DispenseMethod | None:
        """
        id: RXE.30 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.30
        """
        return self._c_data[29][0]

    @dispense_package_method.setter  # set RXE.30
    def dispense_package_method(self, dispense_method: DispenseMethod | None):
        """
        id: RXE.30 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.30
        """
        self._c_data[29] = (dispense_method,)

    @property
    def supplementary_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXE.31 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.31
        """
        return self._c_data[30]

    @supplementary_code.setter  # set RXE.31
    def supplementary_code(self, ce: CE | tuple[CE] | None):
        """
        id: RXE.31 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.31
        """
        if isinstance(ce, tuple):
            self._c_data[30] = ce
        else:
            self._c_data[30] = (ce,)

    @property  # get RXE.32
    def original_order_date_or_time(self) -> TS | None:
        """
        id: RXE.32 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.32
        """
        return self._c_data[31][0]

    @original_order_date_or_time.setter  # set RXE.32
    def original_order_date_or_time(self, ts: TS | None):
        """
        id: RXE.32 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.32
        """
        self._c_data[31] = (ts,)

    @property  # get RXE.33
    def give_drug_strength_volume(self) -> NM | None:
        """
        id: RXE.33 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.33
        """
        return self._c_data[32][0]

    @give_drug_strength_volume.setter  # set RXE.33
    def give_drug_strength_volume(self, nm: NM | None):
        """
        id: RXE.33 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.33
        """
        self._c_data[32] = (nm,)

    @property  # get RXE.34
    def give_drug_strength_volume_units(self) -> CWE | None:
        """
        id: RXE.34 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.34
        """
        return self._c_data[33][0]

    @give_drug_strength_volume_units.setter  # set RXE.34
    def give_drug_strength_volume_units(self, cwe: CWE | None):
        """
        id: RXE.34 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.34
        """
        self._c_data[33] = (cwe,)

    @property  # get RXE.35
    def controlled_substance_schedule(self) -> ControlledSubstanceSchedule_ | None:
        """
        id: RXE.35 | len: 60 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.35
        """
        return self._c_data[34][0]

    @controlled_substance_schedule.setter  # set RXE.35
    def controlled_substance_schedule(
        self, controlled_substance_schedule_: ControlledSubstanceSchedule_ | None
    ):
        """
        id: RXE.35 | len: 60 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.35
        """
        self._c_data[34] = (controlled_substance_schedule_,)

    @property  # get RXE.36
    def formulary_status(self) -> FormularyStatus | None:
        """
        id: RXE.36 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.36
        """
        return self._c_data[35][0]

    @formulary_status.setter  # set RXE.36
    def formulary_status(self, formulary_status: FormularyStatus | None):
        """
        id: RXE.36 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.36
        """
        self._c_data[35] = (formulary_status,)

    @property
    def pharmaceutical_substance_alternative(self) -> tuple[CWE, ...] | tuple[None]:
        """
        id: RXE.37 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.37
        """
        return self._c_data[36]

    @pharmaceutical_substance_alternative.setter  # set RXE.37
    def pharmaceutical_substance_alternative(self, cwe: CWE | tuple[CWE] | None):
        """
        id: RXE.37 | len: 60 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.37
        """
        if isinstance(cwe, tuple):
            self._c_data[36] = cwe
        else:
            self._c_data[36] = (cwe,)

    @property  # get RXE.38
    def pharmacy_of_most_recent_fill(self) -> CWE | None:
        """
        id: RXE.38 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.38
        """
        return self._c_data[37][0]

    @pharmacy_of_most_recent_fill.setter  # set RXE.38
    def pharmacy_of_most_recent_fill(self, cwe: CWE | None):
        """
        id: RXE.38 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.38
        """
        self._c_data[37] = (cwe,)

    @property  # get RXE.39
    def initial_dispense_amount(self) -> NM | None:
        """
        id: RXE.39 | len: 250 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.39
        """
        return self._c_data[38][0]

    @initial_dispense_amount.setter  # set RXE.39
    def initial_dispense_amount(self, nm: NM | None):
        """
        id: RXE.39 | len: 250 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.39
        """
        self._c_data[38] = (nm,)

    @property  # get RXE.40
    def dispensing_pharmacy(self) -> CWE | None:
        """
        id: RXE.40 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.40
        """
        return self._c_data[39][0]

    @dispensing_pharmacy.setter  # set RXE.40
    def dispensing_pharmacy(self, cwe: CWE | None):
        """
        id: RXE.40 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.40
        """
        self._c_data[39] = (cwe,)

    @property  # get RXE.41
    def dispensing_pharmacy_address(self) -> XAD | None:
        """
        id: RXE.41 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.41
        """
        return self._c_data[40][0]

    @dispensing_pharmacy_address.setter  # set RXE.41
    def dispensing_pharmacy_address(self, xad: XAD | None):
        """
        id: RXE.41 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.41
        """
        self._c_data[40] = (xad,)

    @property  # get RXE.42
    def deliver_to_patient_location(self) -> PL | None:
        """
        id: RXE.42 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.42
        """
        return self._c_data[41][0]

    @deliver_to_patient_location.setter  # set RXE.42
    def deliver_to_patient_location(self, pl: PL | None):
        """
        id: RXE.42 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.42
        """
        self._c_data[41] = (pl,)

    @property  # get RXE.43
    def deliver_to_address(self) -> XAD | None:
        """
        id: RXE.43 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.43
        """
        return self._c_data[42][0]

    @deliver_to_address.setter  # set RXE.43
    def deliver_to_address(self, xad: XAD | None):
        """
        id: RXE.43 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.43
        """
        self._c_data[42] = (xad,)

    @property  # get RXE.44
    def pharmacy_order_type(self) -> PharmacyOrderTypes | None:
        """
        id: RXE.44 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.44
        """
        return self._c_data[43][0]

    @pharmacy_order_type.setter  # set RXE.44
    def pharmacy_order_type(self, pharmacy_order_types: PharmacyOrderTypes | None):
        """
        id: RXE.44 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXE.44
        """
        self._c_data[43] = (pharmacy_order_types,)
