from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.CQ import CQ
from ..data_types.LA2 import LA2
from ..data_types.TS import TS
from ..data_types.XCN import XCN
from ..data_types.NM import NM
from ..data_types.XAD import XAD
from ..data_types.CWE import CWE
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..tables.SubstitutionStatus import SubstitutionStatus
from ..tables.VaccinesAdministered import VaccinesAdministered
from ..tables.DispenseMethod import DispenseMethod
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.ManufacturersOfVaccines import ManufacturersOfVaccines
from ..tables.PharmacyOrderTypes import PharmacyOrderTypes
from ..tables.DispenseType import DispenseType


"""
Pharmacy/Treatment Dispense - RXD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXD,
    CE, CQ, LA2, TS, XCN, NM, XAD, CWE, ST, ID
)

rxd = RXD(  #  - 
    dispense_sub_id_counter=nm,  # NM(...)  # Required.
    dispense_or_give_code=ce,  # CE(...)  # Required.
    date_or_time_dispensed=ts,  # TS(...)  # Required.
    actual_dispense_amount=nm,  # NM(...)  # Required.
    actual_dispense_units=None,  # CE(...) 
    actual_dosage_form=None,  # CE(...) 
    prescription_number=st,  # ST(...)  # Required.
    number_of_refills_remaining=None,  # NM(...) 
    dispense_notes=None,  # ST(...) 
    dispensing_provider=None,  # XCN(...) 
    substitution_status=None,  # ID(...) 
    total_daily_dose=None,  # CQ(...) 
    dispense_to_location=None,  # LA2(...) 
    needs_human_review=None,  # ID(...) 
    pharmacy_or_treatment_suppliers_special_dispensing_instructions=None,  # CE(...) 
    actual_strength=None,  # NM(...) 
    actual_strength_unit=None,  # CE(...) 
    substance_lot_number=None,  # ST(...) 
    substance_expiration_date=None,  # TS(...) 
    substance_manufacturer_name=None,  # CE(...) 
    indication=None,  # CE(...) 
    dispense_package_size=None,  # NM(...) 
    dispense_package_size_unit=None,  # CE(...) 
    dispense_package_method=None,  # ID(...) 
    supplementary_code=None,  # CE(...) 
    initiating_location=None,  # CE(...) 
    packaging_or_assembly_location=None,  # CE(...) 
    actual_drug_strength_volume=None,  # NM(...) 
    actual_drug_strength_volume_units=None,  # CWE(...) 
    dispense_to_pharmacy=None,  # CWE(...) 
    dispense_to_pharmacy_address=None,  # XAD(...) 
    pharmacy_order_type=None,  # ID(...) 
    dispense_type=None,  # CWE(...) 
)

-----END SEGMENT::RXD TEMPLATE-----
"""


class RXD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXD"""
    _hl7_name = """Pharmacy/Treatment Dispense"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD"
    _c_length = (4, 250, 26, 20, 250, 250, 20, 20, 200, 200, 1, 10, 200, 1, 250, 20, 250, 20, 26, 250, 250, 20, 250, 2, 250, 250, 250, 5, 250, 180, 106, 1, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 65535, 1, 1, 65535, 65535, 65535, 65535, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "C", "O", "R", "C", "O", "O", "O", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, CE, TS, NM, CE, CE, ST, NM, ST, XCN, ID, CQ, LA2, ID, CE, NM, CE, ST, TS, CE, CE, NM, CE, ID, CE, CE, CE, NM, CWE, CWE, XAD, ID, CWE,)
    _c_aliases = ("RXD.1", "RXD.2", "RXD.3", "RXD.4", "RXD.5", "RXD.6", "RXD.7", "RXD.8", "RXD.9", "RXD.10", "RXD.11", "RXD.12", "RXD.13", "RXD.14", "RXD.15", "RXD.16", "RXD.17", "RXD.18", "RXD.19", "RXD.20", "RXD.21", "RXD.22", "RXD.23", "RXD.24", "RXD.25", "RXD.26", "RXD.27", "RXD.28", "RXD.29", "RXD.30", "RXD.31", "RXD.32", "RXD.33",)
    _c_names = ("Dispense Sub-ID Counter", "Dispense/Give Code", "Date/Time Dispensed", "Actual Dispense Amount", "Actual Dispense Units", "Actual Dosage Form", "Prescription Number", "Number of Refills Remaining", "Dispense Notes", "Dispensing Provider", "Substitution Status", "Total Daily Dose", "Dispense-to Location", "Needs Human Review", "Pharmacy/Treatment Supplier's Special Dispensing Instructions", "Actual Strength", "Actual Strength Unit", "Substance Lot Number", "Substance Expiration Date", "Substance Manufacturer Name", "Indication", "Dispense Package Size", "Dispense Package Size Unit", "Dispense Package Method", "Supplementary Code", "Initiating Location", "Packaging/Assembly Location", "Actual Drug Strength Volume", "Actual Drug Strength Volume Units", "Dispense to Pharmacy", "Dispense to Pharmacy Address", "Pharmacy Order Type", "Dispense Type",)
    _c_attrs = ("dispense_sub_id_counter", "dispense_or_give_code", "date_or_time_dispensed", "actual_dispense_amount", "actual_dispense_units", "actual_dosage_form", "prescription_number", "number_of_refills_remaining", "dispense_notes", "dispensing_provider", "substitution_status", "total_daily_dose", "dispense_to_location", "needs_human_review", "pharmacy_or_treatment_suppliers_special_dispensing_instructions", "actual_strength", "actual_strength_unit", "substance_lot_number", "substance_expiration_date", "substance_manufacturer_name", "indication", "dispense_package_size", "dispense_package_size_unit", "dispense_package_method", "supplementary_code", "initiating_location", "packaging_or_assembly_location", "actual_drug_strength_volume", "actual_drug_strength_volume_units", "dispense_to_pharmacy", "dispense_to_pharmacy_address", "pharmacy_order_type", "dispense_type",)
    # fmt: on

    def __init__(
        self,
        dispense_sub_id_counter: NM | tuple[NM, ...],  # RXD.1
        dispense_or_give_code: VaccinesAdministered
        | CE
        | tuple[VaccinesAdministered | CE, ...],  # RXD.2
        date_or_time_dispensed: TS | tuple[TS, ...],  # RXD.3
        actual_dispense_amount: NM | tuple[NM, ...],  # RXD.4
        prescription_number: ST | tuple[ST, ...],  # RXD.7
        actual_dispense_units: CE | tuple[CE, ...] | None = None,  # RXD.5
        actual_dosage_form: CE | tuple[CE, ...] | None = None,  # RXD.6
        number_of_refills_remaining: NM | tuple[NM, ...] | None = None,  # RXD.8
        dispense_notes: ST | tuple[ST, ...] | None = None,  # RXD.9
        dispensing_provider: XCN | tuple[XCN, ...] | None = None,  # RXD.10
        substitution_status: SubstitutionStatus
        | ID
        | tuple[SubstitutionStatus | ID, ...]
        | None = None,  # RXD.11
        total_daily_dose: CQ | tuple[CQ, ...] | None = None,  # RXD.12
        dispense_to_location: LA2 | tuple[LA2, ...] | None = None,  # RXD.13
        needs_human_review: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # RXD.14
        pharmacy_or_treatment_suppliers_special_dispensing_instructions: CE
        | tuple[CE, ...]
        | None = None,  # RXD.15
        actual_strength: NM | tuple[NM, ...] | None = None,  # RXD.16
        actual_strength_unit: CE | tuple[CE, ...] | None = None,  # RXD.17
        substance_lot_number: ST | tuple[ST, ...] | None = None,  # RXD.18
        substance_expiration_date: TS | tuple[TS, ...] | None = None,  # RXD.19
        substance_manufacturer_name: ManufacturersOfVaccines
        | CE
        | tuple[ManufacturersOfVaccines | CE, ...]
        | None = None,  # RXD.20
        indication: CE | tuple[CE, ...] | None = None,  # RXD.21
        dispense_package_size: NM | tuple[NM, ...] | None = None,  # RXD.22
        dispense_package_size_unit: CE | tuple[CE, ...] | None = None,  # RXD.23
        dispense_package_method: DispenseMethod
        | ID
        | tuple[DispenseMethod | ID, ...]
        | None = None,  # RXD.24
        supplementary_code: CE | tuple[CE, ...] | None = None,  # RXD.25
        initiating_location: CE | tuple[CE, ...] | None = None,  # RXD.26
        packaging_or_assembly_location: CE | tuple[CE, ...] | None = None,  # RXD.27
        actual_drug_strength_volume: NM | tuple[NM, ...] | None = None,  # RXD.28
        actual_drug_strength_volume_units: CWE
        | tuple[CWE, ...]
        | None = None,  # RXD.29
        dispense_to_pharmacy: CWE | tuple[CWE, ...] | None = None,  # RXD.30
        dispense_to_pharmacy_address: XAD | tuple[XAD, ...] | None = None,  # RXD.31
        pharmacy_order_type: PharmacyOrderTypes
        | ID
        | tuple[PharmacyOrderTypes | ID, ...]
        | None = None,  # RXD.32
        dispense_type: DispenseType
        | CWE
        | tuple[DispenseType | CWE, ...]
        | None = None,  # RXD.33
    ):
        """
        Pharmacy/Treatment Dispense - `RXD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD>`_


        :param dispense_sub_id_counter: Numeric (id: RXD.1 | len: 4 | use: R | rpt: 1)
        :param dispense_or_give_code: Coded Element (id: RXD.2 | len: 250 | use: R | rpt: 1)
        :param date_or_time_dispensed: Time Stamp (id: RXD.3 | len: 26 | use: R | rpt: 1)
        :param actual_dispense_amount: Numeric (id: RXD.4 | len: 20 | use: R | rpt: 1)
        :param actual_dispense_units: Coded Element (id: RXD.5 | len: 250 | use: C | rpt: 1)
        :param actual_dosage_form: Coded Element (id: RXD.6 | len: 250 | use: O | rpt: 1)
        :param prescription_number: String Data (id: RXD.7 | len: 20 | use: R | rpt: 1)
        :param number_of_refills_remaining: Numeric (id: RXD.8 | len: 20 | use: C | rpt: 1)
        :param dispense_notes: String Data (id: RXD.9 | len: 200 | use: O | rpt: *)
        :param dispensing_provider: Extended Composite ID Number and Name for Persons (id: RXD.10 | len: 200 | use: O | rpt: *)
        :param substitution_status: Coded values for HL7 tables (id: RXD.11 | len: 1 | use: O | rpt: 1)
        :param total_daily_dose: Composite Quantity with Units (id: RXD.12 | len: 10 | use: O | rpt: 1)
        :param dispense_to_location: Location with Address Variation 2 (id: RXD.13 | len: 200 | use: C | rpt: 1)
        :param needs_human_review: Coded values for HL7 tables (id: RXD.14 | len: 1 | use: O | rpt: 1)
        :param pharmacy_or_treatment_suppliers_special_dispensing_instructions: Coded Element (id: RXD.15 | len: 250 | use: O | rpt: *)
        :param actual_strength: Numeric (id: RXD.16 | len: 20 | use: O | rpt: 1)
        :param actual_strength_unit: Coded Element (id: RXD.17 | len: 250 | use: O | rpt: 1)
        :param substance_lot_number: String Data (id: RXD.18 | len: 20 | use: O | rpt: *)
        :param substance_expiration_date: Time Stamp (id: RXD.19 | len: 26 | use: O | rpt: *)
        :param substance_manufacturer_name: Coded Element (id: RXD.20 | len: 250 | use: O | rpt: *)
        :param indication: Coded Element (id: RXD.21 | len: 250 | use: O | rpt: *)
        :param dispense_package_size: Numeric (id: RXD.22 | len: 20 | use: O | rpt: 1)
        :param dispense_package_size_unit: Coded Element (id: RXD.23 | len: 250 | use: O | rpt: 1)
        :param dispense_package_method: Coded values for HL7 tables (id: RXD.24 | len: 2 | use: O | rpt: 1)
        :param supplementary_code: Coded Element (id: RXD.25 | len: 250 | use: O | rpt: *)
        :param initiating_location: Coded Element (id: RXD.26 | len: 250 | use: O | rpt: 1)
        :param packaging_or_assembly_location: Coded Element (id: RXD.27 | len: 250 | use: O | rpt: 1)
        :param actual_drug_strength_volume: Numeric (id: RXD.28 | len: 5 | use: O | rpt: 1)
        :param actual_drug_strength_volume_units: Coded with Exceptions (id: RXD.29 | len: 250 | use: O | rpt: 1)
        :param dispense_to_pharmacy: Coded with Exceptions (id: RXD.30 | len: 180 | use: O | rpt: 1)
        :param dispense_to_pharmacy_address: Extended Address (id: RXD.31 | len: 106 | use: O | rpt: 1)
        :param pharmacy_order_type: Coded values for HL7 tables (id: RXD.32 | len: 1 | use: O | rpt: 1)
        :param dispense_type: Coded with Exceptions (id: RXD.33 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 33
        self.dispense_sub_id_counter = dispense_sub_id_counter
        self.dispense_or_give_code = dispense_or_give_code
        self.date_or_time_dispensed = date_or_time_dispensed
        self.actual_dispense_amount = actual_dispense_amount
        self.actual_dispense_units = actual_dispense_units
        self.actual_dosage_form = actual_dosage_form
        self.prescription_number = prescription_number
        self.number_of_refills_remaining = number_of_refills_remaining
        self.dispense_notes = dispense_notes
        self.dispensing_provider = dispensing_provider
        self.substitution_status = substitution_status
        self.total_daily_dose = total_daily_dose
        self.dispense_to_location = dispense_to_location
        self.needs_human_review = needs_human_review
        self.pharmacy_or_treatment_suppliers_special_dispensing_instructions = (
            pharmacy_or_treatment_suppliers_special_dispensing_instructions
        )
        self.actual_strength = actual_strength
        self.actual_strength_unit = actual_strength_unit
        self.substance_lot_number = substance_lot_number
        self.substance_expiration_date = substance_expiration_date
        self.substance_manufacturer_name = substance_manufacturer_name
        self.indication = indication
        self.dispense_package_size = dispense_package_size
        self.dispense_package_size_unit = dispense_package_size_unit
        self.dispense_package_method = dispense_package_method
        self.supplementary_code = supplementary_code
        self.initiating_location = initiating_location
        self.packaging_or_assembly_location = packaging_or_assembly_location
        self.actual_drug_strength_volume = actual_drug_strength_volume
        self.actual_drug_strength_volume_units = actual_drug_strength_volume_units
        self.dispense_to_pharmacy = dispense_to_pharmacy
        self.dispense_to_pharmacy_address = dispense_to_pharmacy_address
        self.pharmacy_order_type = pharmacy_order_type
        self.dispense_type = dispense_type

    @property  # get RXD.1
    def dispense_sub_id_counter(self) -> NM:
        """
        id: RXD.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.1
        """
        return self._c_data[0][0]

    @dispense_sub_id_counter.setter  # set RXD.1
    def dispense_sub_id_counter(self, nm: NM):
        """
        id: RXD.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.1
        """
        self._c_data[0] = (nm,)

    @property  # get RXD.2
    def dispense_or_give_code(self) -> VaccinesAdministered:
        """
        id: RXD.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.2
        """
        return self._c_data[1][0]

    @dispense_or_give_code.setter  # set RXD.2
    def dispense_or_give_code(self, vaccines_administered: VaccinesAdministered):
        """
        id: RXD.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.2
        """
        self._c_data[1] = (vaccines_administered,)

    @property  # get RXD.3
    def date_or_time_dispensed(self) -> TS:
        """
        id: RXD.3 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.3
        """
        return self._c_data[2][0]

    @date_or_time_dispensed.setter  # set RXD.3
    def date_or_time_dispensed(self, ts: TS):
        """
        id: RXD.3 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.3
        """
        self._c_data[2] = (ts,)

    @property  # get RXD.4
    def actual_dispense_amount(self) -> NM:
        """
        id: RXD.4 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.4
        """
        return self._c_data[3][0]

    @actual_dispense_amount.setter  # set RXD.4
    def actual_dispense_amount(self, nm: NM):
        """
        id: RXD.4 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.4
        """
        self._c_data[3] = (nm,)

    @property  # get RXD.5
    def actual_dispense_units(self) -> CE | None:
        """
        id: RXD.5 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.5
        """
        return self._c_data[4][0]

    @actual_dispense_units.setter  # set RXD.5
    def actual_dispense_units(self, ce: CE | None):
        """
        id: RXD.5 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.5
        """
        self._c_data[4] = (ce,)

    @property  # get RXD.6
    def actual_dosage_form(self) -> CE | None:
        """
        id: RXD.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.6
        """
        return self._c_data[5][0]

    @actual_dosage_form.setter  # set RXD.6
    def actual_dosage_form(self, ce: CE | None):
        """
        id: RXD.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.6
        """
        self._c_data[5] = (ce,)

    @property  # get RXD.7
    def prescription_number(self) -> ST:
        """
        id: RXD.7 | len: 20 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.7
        """
        return self._c_data[6][0]

    @prescription_number.setter  # set RXD.7
    def prescription_number(self, st: ST):
        """
        id: RXD.7 | len: 20 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.7
        """
        self._c_data[6] = (st,)

    @property  # get RXD.8
    def number_of_refills_remaining(self) -> NM | None:
        """
        id: RXD.8 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.8
        """
        return self._c_data[7][0]

    @number_of_refills_remaining.setter  # set RXD.8
    def number_of_refills_remaining(self, nm: NM | None):
        """
        id: RXD.8 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.8
        """
        self._c_data[7] = (nm,)

    @property
    def dispense_notes(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: RXD.9 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.9
        """
        return self._c_data[8]

    @dispense_notes.setter  # set RXD.9
    def dispense_notes(self, st: ST | tuple[ST] | None):
        """
        id: RXD.9 | len: 200 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.9
        """
        if isinstance(st, tuple):
            self._c_data[8] = st
        else:
            self._c_data[8] = (st,)

    @property
    def dispensing_provider(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: RXD.10 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.10
        """
        return self._c_data[9]

    @dispensing_provider.setter  # set RXD.10
    def dispensing_provider(self, xcn: XCN | tuple[XCN] | None):
        """
        id: RXD.10 | len: 200 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.10
        """
        if isinstance(xcn, tuple):
            self._c_data[9] = xcn
        else:
            self._c_data[9] = (xcn,)

    @property  # get RXD.11
    def substitution_status(self) -> SubstitutionStatus | None:
        """
        id: RXD.11 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.11
        """
        return self._c_data[10][0]

    @substitution_status.setter  # set RXD.11
    def substitution_status(self, substitution_status: SubstitutionStatus | None):
        """
        id: RXD.11 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.11
        """
        self._c_data[10] = (substitution_status,)

    @property  # get RXD.12
    def total_daily_dose(self) -> CQ | None:
        """
        id: RXD.12 | len: 10 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.12
        """
        return self._c_data[11][0]

    @total_daily_dose.setter  # set RXD.12
    def total_daily_dose(self, cq: CQ | None):
        """
        id: RXD.12 | len: 10 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.12
        """
        self._c_data[11] = (cq,)

    @property  # get RXD.13
    def dispense_to_location(self) -> LA2 | None:
        """
        id: RXD.13 | len: 200 | use: C | rpt: 1
        ---
        return_type: LA2: Location with Address Variation 2
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.13
        """
        return self._c_data[12][0]

    @dispense_to_location.setter  # set RXD.13
    def dispense_to_location(self, la2: LA2 | None):
        """
        id: RXD.13 | len: 200 | use: C | rpt: 1
        ---
        param_type: LA2: Location with Address Variation 2
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.13
        """
        self._c_data[12] = (la2,)

    @property  # get RXD.14
    def needs_human_review(self) -> YesOrNoIndicator | None:
        """
        id: RXD.14 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.14
        """
        return self._c_data[13][0]

    @needs_human_review.setter  # set RXD.14
    def needs_human_review(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RXD.14 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.14
        """
        self._c_data[13] = (yes_or_no_indicator,)

    @property
    def pharmacy_or_treatment_suppliers_special_dispensing_instructions(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXD.15 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.15
        """
        return self._c_data[14]

    @pharmacy_or_treatment_suppliers_special_dispensing_instructions.setter  # set RXD.15
    def pharmacy_or_treatment_suppliers_special_dispensing_instructions(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: RXD.15 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.15
        """
        if isinstance(ce, tuple):
            self._c_data[14] = ce
        else:
            self._c_data[14] = (ce,)

    @property  # get RXD.16
    def actual_strength(self) -> NM | None:
        """
        id: RXD.16 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.16
        """
        return self._c_data[15][0]

    @actual_strength.setter  # set RXD.16
    def actual_strength(self, nm: NM | None):
        """
        id: RXD.16 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.16
        """
        self._c_data[15] = (nm,)

    @property  # get RXD.17
    def actual_strength_unit(self) -> CE | None:
        """
        id: RXD.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.17
        """
        return self._c_data[16][0]

    @actual_strength_unit.setter  # set RXD.17
    def actual_strength_unit(self, ce: CE | None):
        """
        id: RXD.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.17
        """
        self._c_data[16] = (ce,)

    @property
    def substance_lot_number(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: RXD.18 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.18
        """
        return self._c_data[17]

    @substance_lot_number.setter  # set RXD.18
    def substance_lot_number(self, st: ST | tuple[ST] | None):
        """
        id: RXD.18 | len: 20 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.18
        """
        if isinstance(st, tuple):
            self._c_data[17] = st
        else:
            self._c_data[17] = (st,)

    @property
    def substance_expiration_date(self) -> tuple[TS, ...] | tuple[None]:
        """
        id: RXD.19 | len: 26 | use: O | rpt: *
        ---
        return_type: tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.19
        """
        return self._c_data[18]

    @substance_expiration_date.setter  # set RXD.19
    def substance_expiration_date(self, ts: TS | tuple[TS] | None):
        """
        id: RXD.19 | len: 26 | use: O | rpt: *
        ---
        param_type: TS | tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.19
        """
        if isinstance(ts, tuple):
            self._c_data[18] = ts
        else:
            self._c_data[18] = (ts,)

    @property
    def substance_manufacturer_name(
        self,
    ) -> tuple[ManufacturersOfVaccines, ...] | tuple[None]:
        """
        id: RXD.20 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.20
        """
        return self._c_data[19]

    @substance_manufacturer_name.setter  # set RXD.20
    def substance_manufacturer_name(
        self,
        manufacturers_of_vaccines: ManufacturersOfVaccines
        | tuple[ManufacturersOfVaccines]
        | None,
    ):
        """
        id: RXD.20 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.20
        """
        if isinstance(manufacturers_of_vaccines, tuple):
            self._c_data[19] = manufacturers_of_vaccines
        else:
            self._c_data[19] = (manufacturers_of_vaccines,)

    @property
    def indication(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXD.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.21
        """
        return self._c_data[20]

    @indication.setter  # set RXD.21
    def indication(self, ce: CE | tuple[CE] | None):
        """
        id: RXD.21 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.21
        """
        if isinstance(ce, tuple):
            self._c_data[20] = ce
        else:
            self._c_data[20] = (ce,)

    @property  # get RXD.22
    def dispense_package_size(self) -> NM | None:
        """
        id: RXD.22 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.22
        """
        return self._c_data[21][0]

    @dispense_package_size.setter  # set RXD.22
    def dispense_package_size(self, nm: NM | None):
        """
        id: RXD.22 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.22
        """
        self._c_data[21] = (nm,)

    @property  # get RXD.23
    def dispense_package_size_unit(self) -> CE | None:
        """
        id: RXD.23 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.23
        """
        return self._c_data[22][0]

    @dispense_package_size_unit.setter  # set RXD.23
    def dispense_package_size_unit(self, ce: CE | None):
        """
        id: RXD.23 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.23
        """
        self._c_data[22] = (ce,)

    @property  # get RXD.24
    def dispense_package_method(self) -> DispenseMethod | None:
        """
        id: RXD.24 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.24
        """
        return self._c_data[23][0]

    @dispense_package_method.setter  # set RXD.24
    def dispense_package_method(self, dispense_method: DispenseMethod | None):
        """
        id: RXD.24 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.24
        """
        self._c_data[23] = (dispense_method,)

    @property
    def supplementary_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXD.25 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.25
        """
        return self._c_data[24]

    @supplementary_code.setter  # set RXD.25
    def supplementary_code(self, ce: CE | tuple[CE] | None):
        """
        id: RXD.25 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.25
        """
        if isinstance(ce, tuple):
            self._c_data[24] = ce
        else:
            self._c_data[24] = (ce,)

    @property  # get RXD.26
    def initiating_location(self) -> CE | None:
        """
        id: RXD.26 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.26
        """
        return self._c_data[25][0]

    @initiating_location.setter  # set RXD.26
    def initiating_location(self, ce: CE | None):
        """
        id: RXD.26 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.26
        """
        self._c_data[25] = (ce,)

    @property  # get RXD.27
    def packaging_or_assembly_location(self) -> CE | None:
        """
        id: RXD.27 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.27
        """
        return self._c_data[26][0]

    @packaging_or_assembly_location.setter  # set RXD.27
    def packaging_or_assembly_location(self, ce: CE | None):
        """
        id: RXD.27 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.27
        """
        self._c_data[26] = (ce,)

    @property  # get RXD.28
    def actual_drug_strength_volume(self) -> NM | None:
        """
        id: RXD.28 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.28
        """
        return self._c_data[27][0]

    @actual_drug_strength_volume.setter  # set RXD.28
    def actual_drug_strength_volume(self, nm: NM | None):
        """
        id: RXD.28 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.28
        """
        self._c_data[27] = (nm,)

    @property  # get RXD.29
    def actual_drug_strength_volume_units(self) -> CWE | None:
        """
        id: RXD.29 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.29
        """
        return self._c_data[28][0]

    @actual_drug_strength_volume_units.setter  # set RXD.29
    def actual_drug_strength_volume_units(self, cwe: CWE | None):
        """
        id: RXD.29 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.29
        """
        self._c_data[28] = (cwe,)

    @property  # get RXD.30
    def dispense_to_pharmacy(self) -> CWE | None:
        """
        id: RXD.30 | len: 180 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.30
        """
        return self._c_data[29][0]

    @dispense_to_pharmacy.setter  # set RXD.30
    def dispense_to_pharmacy(self, cwe: CWE | None):
        """
        id: RXD.30 | len: 180 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.30
        """
        self._c_data[29] = (cwe,)

    @property  # get RXD.31
    def dispense_to_pharmacy_address(self) -> XAD | None:
        """
        id: RXD.31 | len: 106 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.31
        """
        return self._c_data[30][0]

    @dispense_to_pharmacy_address.setter  # set RXD.31
    def dispense_to_pharmacy_address(self, xad: XAD | None):
        """
        id: RXD.31 | len: 106 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.31
        """
        self._c_data[30] = (xad,)

    @property  # get RXD.32
    def pharmacy_order_type(self) -> PharmacyOrderTypes | None:
        """
        id: RXD.32 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.32
        """
        return self._c_data[31][0]

    @pharmacy_order_type.setter  # set RXD.32
    def pharmacy_order_type(self, pharmacy_order_types: PharmacyOrderTypes | None):
        """
        id: RXD.32 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.32
        """
        self._c_data[31] = (pharmacy_order_types,)

    @property  # get RXD.33
    def dispense_type(self) -> DispenseType | None:
        """
        id: RXD.33 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.33
        """
        return self._c_data[32][0]

    @dispense_type.setter  # set RXD.33
    def dispense_type(self, dispense_type: DispenseType | None):
        """
        id: RXD.33 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXD.33
        """
        self._c_data[32] = (dispense_type,)
