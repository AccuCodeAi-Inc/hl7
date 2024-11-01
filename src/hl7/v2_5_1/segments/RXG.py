from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.TQ import TQ
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.LA2 import LA2
from ..data_types.ST import ST
from ..data_types.CWE import CWE
from ..data_types.TS import TS
from ..tables.SubstitutionStatus import SubstitutionStatus
from ..tables.ManufacturersOfVaccines import ManufacturersOfVaccines
from ..tables.PharmacyOrderTypes import PharmacyOrderTypes
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.VaccinesAdministered import VaccinesAdministered


"""
Pharmacy/Treatment Give - RXG
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXG TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXG,
    CE, TQ, ID, NM, LA2, ST, CWE, TS
)

rxg = RXG(  #  - 
    give_sub_id_counter=nm,  # NM(...)  # Required.
    dispense_sub_id_counter=None,  # NM(...) 
    quantity_or_timing=None,  # TQ(...) 
    give_code=ce,  # CE(...)  # Required.
    give_amount_minimum=nm,  # NM(...)  # Required.
    give_amount_maximum=None,  # NM(...) 
    give_units=ce,  # CE(...)  # Required.
    give_dosage_form=None,  # CE(...) 
    administration_notes=None,  # CE(...) 
    substitution_status=None,  # ID(...) 
    dispense_to_location=None,  # LA2(...) 
    needs_human_review=None,  # ID(...) 
    pharmacy_or_treatment_suppliers_special_administration_instructions=None,  # CE(...) 
    give_per=None,  # ST(...) 
    give_rate_amount=None,  # ST(...) 
    give_rate_units=None,  # CE(...) 
    give_strength=None,  # NM(...) 
    give_strength_units=None,  # CE(...) 
    substance_lot_number=None,  # ST(...) 
    substance_expiration_date=None,  # TS(...) 
    substance_manufacturer_name=None,  # CE(...) 
    indication=None,  # CE(...) 
    give_drug_strength_volume=None,  # NM(...) 
    give_drug_strength_volume_units=None,  # CWE(...) 
    give_barcode_identifier=None,  # CWE(...) 
    pharmacy_order_type=None,  # ID(...) 
)

-----END SEGMENT::RXG TEMPLATE-----
"""


class RXG(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXG"""
    _hl7_name = """Pharmacy/Treatment Give"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG"
    _c_length = (4, 4, 200, 250, 20, 20, 250, 250, 250, 1, 200, 1, 250, 20, 6, 250, 20, 250, 20, 26, 250, 250, 5, 250, 60, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 65535, 65535, 65535, 65535, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "B", "R", "R", "O", "R", "O", "O", "O", "O", "O", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, NM, TQ, CE, NM, NM, CE, CE, CE, ID, LA2, ID, CE, ST, ST, CE, NM, CE, ST, TS, CE, CE, NM, CWE, CWE, ID,)
    _c_aliases = ("RXG.1", "RXG.2", "RXG.3", "RXG.4", "RXG.5", "RXG.6", "RXG.7", "RXG.8", "RXG.9", "RXG.10", "RXG.11", "RXG.12", "RXG.13", "RXG.14", "RXG.15", "RXG.16", "RXG.17", "RXG.18", "RXG.19", "RXG.20", "RXG.21", "RXG.22", "RXG.23", "RXG.24", "RXG.25", "RXG.26",)
    _c_names = ("Give Sub-ID Counter", "Dispense Sub-ID Counter", "Quantity/Timing", "Give Code", "Give Amount - Minimum", "Give Amount - Maximum", "Give Units", "Give Dosage Form", "Administration Notes", "Substitution Status", "Dispense-to Location", "Needs Human Review", "Pharmacy/Treatment Supplier's Special Administration Instructions", "Give Per (Time Unit)", "Give Rate Amount", "Give Rate Units", "Give Strength", "Give Strength Units", "Substance Lot Number", "Substance Expiration Date", "Substance Manufacturer Name", "Indication", "Give Drug Strength Volume", "Give Drug Strength Volume Units", "Give Barcode Identifier", "Pharmacy Order Type",)
    _c_attrs = ("give_sub_id_counter", "dispense_sub_id_counter", "quantity_or_timing", "give_code", "give_amount_minimum", "give_amount_maximum", "give_units", "give_dosage_form", "administration_notes", "substitution_status", "dispense_to_location", "needs_human_review", "pharmacy_or_treatment_suppliers_special_administration_instructions", "give_per", "give_rate_amount", "give_rate_units", "give_strength", "give_strength_units", "substance_lot_number", "substance_expiration_date", "substance_manufacturer_name", "indication", "give_drug_strength_volume", "give_drug_strength_volume_units", "give_barcode_identifier", "pharmacy_order_type",)
    # fmt: on

    def __init__(
        self,
        give_sub_id_counter: NM,  # RXG.1
        give_code: VaccinesAdministered | CE,  # RXG.4
        give_amount_minimum: NM,  # RXG.5
        give_units: CE,  # RXG.7
        dispense_sub_id_counter: NM | None = None,  # RXG.2
        quantity_or_timing: TQ | None = None,  # RXG.3
        give_amount_maximum: NM | None = None,  # RXG.6
        give_dosage_form: CE | None = None,  # RXG.8
        administration_notes: CE | None = None,  # RXG.9
        substitution_status: SubstitutionStatus | ID | None = None,  # RXG.10
        dispense_to_location: LA2 | None = None,  # RXG.11
        needs_human_review: YesOrNoIndicator | ID | None = None,  # RXG.12
        pharmacy_or_treatment_suppliers_special_administration_instructions: CE
        | None = None,  # RXG.13
        give_per: ST | None = None,  # RXG.14
        give_rate_amount: ST | None = None,  # RXG.15
        give_rate_units: CE | None = None,  # RXG.16
        give_strength: NM | None = None,  # RXG.17
        give_strength_units: CE | None = None,  # RXG.18
        substance_lot_number: ST | None = None,  # RXG.19
        substance_expiration_date: TS | None = None,  # RXG.20
        substance_manufacturer_name: ManufacturersOfVaccines
        | CE
        | None = None,  # RXG.21
        indication: CE | None = None,  # RXG.22
        give_drug_strength_volume: NM | None = None,  # RXG.23
        give_drug_strength_volume_units: CWE | None = None,  # RXG.24
        give_barcode_identifier: CWE | None = None,  # RXG.25
        pharmacy_order_type: PharmacyOrderTypes | ID | None = None,  # RXG.26
    ):
        """
        Pharmacy/Treatment Give - `RXG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG>`_


        :param give_sub_id_counter: Numeric (id: RXG.1 | len: 4 | use: R | rpt: 1)
        :param dispense_sub_id_counter: Numeric (id: RXG.2 | len: 4 | use: O | rpt: 1)
        :param quantity_or_timing: Timing Quantity (id: RXG.3 | len: 200 | use: B | rpt: 1)
        :param give_code: Coded Element (id: RXG.4 | len: 250 | use: R | rpt: 1)
        :param give_amount_minimum: Numeric (id: RXG.5 | len: 20 | use: R | rpt: 1)
        :param give_amount_maximum: Numeric (id: RXG.6 | len: 20 | use: O | rpt: 1)
        :param give_units: Coded Element (id: RXG.7 | len: 250 | use: R | rpt: 1)
        :param give_dosage_form: Coded Element (id: RXG.8 | len: 250 | use: O | rpt: 1)
        :param administration_notes: Coded Element (id: RXG.9 | len: 250 | use: O | rpt: *)
        :param substitution_status: Coded values for HL7 tables (id: RXG.10 | len: 1 | use: O | rpt: 1)
        :param dispense_to_location: Location with Address Variation 2 (id: RXG.11 | len: 200 | use: O | rpt: 1)
        :param needs_human_review: Coded values for HL7 tables (id: RXG.12 | len: 1 | use: O | rpt: 1)
        :param pharmacy_or_treatment_suppliers_special_administration_instructions: Coded Element (id: RXG.13 | len: 250 | use: O | rpt: *)
        :param give_per: String Data (id: RXG.14 | len: 20 | use: C | rpt: 1)
        :param give_rate_amount: String Data (id: RXG.15 | len: 6 | use: O | rpt: 1)
        :param give_rate_units: Coded Element (id: RXG.16 | len: 250 | use: O | rpt: 1)
        :param give_strength: Numeric (id: RXG.17 | len: 20 | use: O | rpt: 1)
        :param give_strength_units: Coded Element (id: RXG.18 | len: 250 | use: O | rpt: 1)
        :param substance_lot_number: String Data (id: RXG.19 | len: 20 | use: O | rpt: *)
        :param substance_expiration_date: Time Stamp (id: RXG.20 | len: 26 | use: O | rpt: *)
        :param substance_manufacturer_name: Coded Element (id: RXG.21 | len: 250 | use: O | rpt: *)
        :param indication: Coded Element (id: RXG.22 | len: 250 | use: O | rpt: *)
        :param give_drug_strength_volume: Numeric (id: RXG.23 | len: 5 | use: O | rpt: 1)
        :param give_drug_strength_volume_units: Coded with Exceptions (id: RXG.24 | len: 250 | use: O | rpt: 1)
        :param give_barcode_identifier: Coded with Exceptions (id: RXG.25 | len: 60 | use: O | rpt: 1)
        :param pharmacy_order_type: Coded values for HL7 tables (id: RXG.26 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 26
        self.give_sub_id_counter = give_sub_id_counter
        self.dispense_sub_id_counter = dispense_sub_id_counter
        self.quantity_or_timing = quantity_or_timing
        self.give_code = give_code
        self.give_amount_minimum = give_amount_minimum
        self.give_amount_maximum = give_amount_maximum
        self.give_units = give_units
        self.give_dosage_form = give_dosage_form
        self.administration_notes = administration_notes
        self.substitution_status = substitution_status
        self.dispense_to_location = dispense_to_location
        self.needs_human_review = needs_human_review
        self.pharmacy_or_treatment_suppliers_special_administration_instructions = (
            pharmacy_or_treatment_suppliers_special_administration_instructions
        )
        self.give_per = give_per
        self.give_rate_amount = give_rate_amount
        self.give_rate_units = give_rate_units
        self.give_strength = give_strength
        self.give_strength_units = give_strength_units
        self.substance_lot_number = substance_lot_number
        self.substance_expiration_date = substance_expiration_date
        self.substance_manufacturer_name = substance_manufacturer_name
        self.indication = indication
        self.give_drug_strength_volume = give_drug_strength_volume
        self.give_drug_strength_volume_units = give_drug_strength_volume_units
        self.give_barcode_identifier = give_barcode_identifier
        self.pharmacy_order_type = pharmacy_order_type

    @property  # get RXG.1
    def give_sub_id_counter(self) -> NM:
        """
        id: RXG.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.1
        """
        return self._c_data[0][0]

    @give_sub_id_counter.setter  # set RXG.1
    def give_sub_id_counter(self, nm: NM):
        """
        id: RXG.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.1
        """
        self._c_data[0] = (nm,)

    @property  # get RXG.2
    def dispense_sub_id_counter(self) -> NM | None:
        """
        id: RXG.2 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.2
        """
        return self._c_data[1][0]

    @dispense_sub_id_counter.setter  # set RXG.2
    def dispense_sub_id_counter(self, nm: NM | None):
        """
        id: RXG.2 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.2
        """
        self._c_data[1] = (nm,)

    @property  # get RXG.3
    def quantity_or_timing(self) -> TQ | None:
        """
        id: RXG.3 | len: 200 | use: B | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.3
        """
        return self._c_data[2][0]

    @quantity_or_timing.setter  # set RXG.3
    def quantity_or_timing(self, tq: TQ | None):
        """
        id: RXG.3 | len: 200 | use: B | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.3
        """
        self._c_data[2] = (tq,)

    @property  # get RXG.4
    def give_code(self) -> VaccinesAdministered:
        """
        id: RXG.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.4
        """
        return self._c_data[3][0]

    @give_code.setter  # set RXG.4
    def give_code(self, vaccines_administered: VaccinesAdministered):
        """
        id: RXG.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.4
        """
        self._c_data[3] = (vaccines_administered,)

    @property  # get RXG.5
    def give_amount_minimum(self) -> NM:
        """
        id: RXG.5 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.5
        """
        return self._c_data[4][0]

    @give_amount_minimum.setter  # set RXG.5
    def give_amount_minimum(self, nm: NM):
        """
        id: RXG.5 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.5
        """
        self._c_data[4] = (nm,)

    @property  # get RXG.6
    def give_amount_maximum(self) -> NM | None:
        """
        id: RXG.6 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.6
        """
        return self._c_data[5][0]

    @give_amount_maximum.setter  # set RXG.6
    def give_amount_maximum(self, nm: NM | None):
        """
        id: RXG.6 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.6
        """
        self._c_data[5] = (nm,)

    @property  # get RXG.7
    def give_units(self) -> CE:
        """
        id: RXG.7 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.7
        """
        return self._c_data[6][0]

    @give_units.setter  # set RXG.7
    def give_units(self, ce: CE):
        """
        id: RXG.7 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.7
        """
        self._c_data[6] = (ce,)

    @property  # get RXG.8
    def give_dosage_form(self) -> CE | None:
        """
        id: RXG.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.8
        """
        return self._c_data[7][0]

    @give_dosage_form.setter  # set RXG.8
    def give_dosage_form(self, ce: CE | None):
        """
        id: RXG.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.8
        """
        self._c_data[7] = (ce,)

    @property
    def administration_notes(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXG.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.9
        """
        return self._c_data[8]

    @administration_notes.setter  # set RXG.9
    def administration_notes(self, ce: CE | tuple[CE] | None):
        """
        id: RXG.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.9
        """
        if isinstance(ce, tuple):
            self._c_data[8] = ce
        else:
            self._c_data[8] = (ce,)

    @property  # get RXG.10
    def substitution_status(self) -> SubstitutionStatus | None:
        """
        id: RXG.10 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.10
        """
        return self._c_data[9][0]

    @substitution_status.setter  # set RXG.10
    def substitution_status(self, substitution_status: SubstitutionStatus | None):
        """
        id: RXG.10 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.10
        """
        self._c_data[9] = (substitution_status,)

    @property  # get RXG.11
    def dispense_to_location(self) -> LA2 | None:
        """
        id: RXG.11 | len: 200 | use: O | rpt: 1
        ---
        return_type: LA2: Location with Address Variation 2
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.11
        """
        return self._c_data[10][0]

    @dispense_to_location.setter  # set RXG.11
    def dispense_to_location(self, la2: LA2 | None):
        """
        id: RXG.11 | len: 200 | use: O | rpt: 1
        ---
        param_type: LA2: Location with Address Variation 2
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.11
        """
        self._c_data[10] = (la2,)

    @property  # get RXG.12
    def needs_human_review(self) -> YesOrNoIndicator | None:
        """
        id: RXG.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.12
        """
        return self._c_data[11][0]

    @needs_human_review.setter  # set RXG.12
    def needs_human_review(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RXG.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.12
        """
        self._c_data[11] = (yes_or_no_indicator,)

    @property
    def pharmacy_or_treatment_suppliers_special_administration_instructions(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXG.13 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.13
        """
        return self._c_data[12]

    @pharmacy_or_treatment_suppliers_special_administration_instructions.setter  # set RXG.13
    def pharmacy_or_treatment_suppliers_special_administration_instructions(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: RXG.13 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.13
        """
        if isinstance(ce, tuple):
            self._c_data[12] = ce
        else:
            self._c_data[12] = (ce,)

    @property  # get RXG.14
    def give_per(self) -> ST | None:
        """
        id: RXG.14 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.14
        """
        return self._c_data[13][0]

    @give_per.setter  # set RXG.14
    def give_per(self, st: ST | None):
        """
        id: RXG.14 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.14
        """
        self._c_data[13] = (st,)

    @property  # get RXG.15
    def give_rate_amount(self) -> ST | None:
        """
        id: RXG.15 | len: 6 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.15
        """
        return self._c_data[14][0]

    @give_rate_amount.setter  # set RXG.15
    def give_rate_amount(self, st: ST | None):
        """
        id: RXG.15 | len: 6 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.15
        """
        self._c_data[14] = (st,)

    @property  # get RXG.16
    def give_rate_units(self) -> CE | None:
        """
        id: RXG.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.16
        """
        return self._c_data[15][0]

    @give_rate_units.setter  # set RXG.16
    def give_rate_units(self, ce: CE | None):
        """
        id: RXG.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.16
        """
        self._c_data[15] = (ce,)

    @property  # get RXG.17
    def give_strength(self) -> NM | None:
        """
        id: RXG.17 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.17
        """
        return self._c_data[16][0]

    @give_strength.setter  # set RXG.17
    def give_strength(self, nm: NM | None):
        """
        id: RXG.17 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.17
        """
        self._c_data[16] = (nm,)

    @property  # get RXG.18
    def give_strength_units(self) -> CE | None:
        """
        id: RXG.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.18
        """
        return self._c_data[17][0]

    @give_strength_units.setter  # set RXG.18
    def give_strength_units(self, ce: CE | None):
        """
        id: RXG.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.18
        """
        self._c_data[17] = (ce,)

    @property
    def substance_lot_number(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: RXG.19 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.19
        """
        return self._c_data[18]

    @substance_lot_number.setter  # set RXG.19
    def substance_lot_number(self, st: ST | tuple[ST] | None):
        """
        id: RXG.19 | len: 20 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.19
        """
        if isinstance(st, tuple):
            self._c_data[18] = st
        else:
            self._c_data[18] = (st,)

    @property
    def substance_expiration_date(self) -> tuple[TS, ...] | tuple[None]:
        """
        id: RXG.20 | len: 26 | use: O | rpt: *
        ---
        return_type: tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.20
        """
        return self._c_data[19]

    @substance_expiration_date.setter  # set RXG.20
    def substance_expiration_date(self, ts: TS | tuple[TS] | None):
        """
        id: RXG.20 | len: 26 | use: O | rpt: *
        ---
        param_type: TS | tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.20
        """
        if isinstance(ts, tuple):
            self._c_data[19] = ts
        else:
            self._c_data[19] = (ts,)

    @property
    def substance_manufacturer_name(
        self,
    ) -> tuple[ManufacturersOfVaccines, ...] | tuple[None]:
        """
        id: RXG.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.21
        """
        return self._c_data[20]

    @substance_manufacturer_name.setter  # set RXG.21
    def substance_manufacturer_name(
        self,
        manufacturers_of_vaccines: ManufacturersOfVaccines
        | tuple[ManufacturersOfVaccines]
        | None,
    ):
        """
        id: RXG.21 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.21
        """
        if isinstance(manufacturers_of_vaccines, tuple):
            self._c_data[20] = manufacturers_of_vaccines
        else:
            self._c_data[20] = (manufacturers_of_vaccines,)

    @property
    def indication(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXG.22 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.22
        """
        return self._c_data[21]

    @indication.setter  # set RXG.22
    def indication(self, ce: CE | tuple[CE] | None):
        """
        id: RXG.22 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.22
        """
        if isinstance(ce, tuple):
            self._c_data[21] = ce
        else:
            self._c_data[21] = (ce,)

    @property  # get RXG.23
    def give_drug_strength_volume(self) -> NM | None:
        """
        id: RXG.23 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.23
        """
        return self._c_data[22][0]

    @give_drug_strength_volume.setter  # set RXG.23
    def give_drug_strength_volume(self, nm: NM | None):
        """
        id: RXG.23 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.23
        """
        self._c_data[22] = (nm,)

    @property  # get RXG.24
    def give_drug_strength_volume_units(self) -> CWE | None:
        """
        id: RXG.24 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.24
        """
        return self._c_data[23][0]

    @give_drug_strength_volume_units.setter  # set RXG.24
    def give_drug_strength_volume_units(self, cwe: CWE | None):
        """
        id: RXG.24 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.24
        """
        self._c_data[23] = (cwe,)

    @property  # get RXG.25
    def give_barcode_identifier(self) -> CWE | None:
        """
        id: RXG.25 | len: 60 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.25
        """
        return self._c_data[24][0]

    @give_barcode_identifier.setter  # set RXG.25
    def give_barcode_identifier(self, cwe: CWE | None):
        """
        id: RXG.25 | len: 60 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.25
        """
        self._c_data[24] = (cwe,)

    @property  # get RXG.26
    def pharmacy_order_type(self) -> PharmacyOrderTypes | None:
        """
        id: RXG.26 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.26
        """
        return self._c_data[25][0]

    @pharmacy_order_type.setter  # set RXG.26
    def pharmacy_order_type(self, pharmacy_order_types: PharmacyOrderTypes | None):
        """
        id: RXG.26 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXG.26
        """
        self._c_data[25] = (pharmacy_order_types,)
