from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.CQ import CQ
from ..data_types.XCN import XCN
from ..data_types.NM import NM
from ..data_types.CWE import CWE
from ..data_types.ST import ST
from ..data_types.LA1 import LA1
from ..data_types.ID import ID
from ..tables.PharmacyOrderTypes import PharmacyOrderTypes
from ..tables.AllowSubstitution import AllowSubstitution
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Pharmacy/Treatment Order - RXO
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXO TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXO,
    CE, CQ, XCN, NM, CWE, ST, LA1, ID
)

rxo = RXO(  #  - This is the master pharmacy/treatment order segment
    requested_give_code=None,  # CE(...) 
    requested_give_amount_minimum=None,  # NM(...) 
    requested_give_amount_maximum=None,  # NM(...) 
    requested_give_units=None,  # CE(...) 
    requested_dosage_form=None,  # CE(...) 
    providers_pharmacy_or_treatment_instructions=None,  # CE(...) 
    providers_administration_instructions=None,  # CE(...) 
    deliver_to_location=None,  # LA1(...) 
    allow_substitutions=None,  # ID(...) 
    requested_dispense_code=None,  # CE(...) 
    requested_dispense_amount=None,  # NM(...) 
    requested_dispense_units=None,  # CE(...) 
    number_of_refills=None,  # NM(...) 
    ordering_providers_dea_number=None,  # XCN(...) 
    pharmacist_or_treatment_suppliers_verifier_id=None,  # XCN(...) 
    needs_human_review=None,  # ID(...) 
    requested_give_per=None,  # ST(...) 
    requested_give_strength=None,  # NM(...) 
    requested_give_strength_units=None,  # CE(...) 
    indication=None,  # CE(...) 
    requested_give_rate_amount=None,  # ST(...) 
    requested_give_rate_units=None,  # CE(...) 
    total_daily_dose=None,  # CQ(...) 
    supplementary_code=None,  # CE(...) 
    requested_drug_strength_volume=None,  # NM(...) 
    requested_drug_strength_volume_units=None,  # CWE(...) 
    pharmacy_order_type=None,  # ID(...) 
    dispensing_interval=None,  # NM(...) 
)

-----END SEGMENT::RXO TEMPLATE-----
"""


class RXO(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXO"""
    _hl7_name = """Pharmacy/Treatment Order"""
    _hl7_description = """This is the master pharmacy/treatment order segment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO"
    _c_length = (250, 20, 20, 250, 250, 250, 250, 200, 1, 250, 20, 250, 3, 250, 250, 1, 20, 20, 250, 250, 6, 250, 10, 250, 5, 250, 1, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 1, 1, 1, 1,)
    _c_usage = ("C", "C", "O", "C", "C", "O", "O", "O", "O", "O", "O", "O", "O", "C", "C", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, NM, NM, CE, CE, CE, CE, LA1, ID, CE, NM, CE, NM, XCN, XCN, ID, ST, NM, CE, CE, ST, CE, CQ, CE, NM, CWE, ID, NM,)
    _c_aliases = ("RXO.1", "RXO.2", "RXO.3", "RXO.4", "RXO.5", "RXO.6", "RXO.7", "RXO.8", "RXO.9", "RXO.10", "RXO.11", "RXO.12", "RXO.13", "RXO.14", "RXO.15", "RXO.16", "RXO.17", "RXO.18", "RXO.19", "RXO.20", "RXO.21", "RXO.22", "RXO.23", "RXO.24", "RXO.25", "RXO.26", "RXO.27", "RXO.28",)
    _c_names = ("Requested Give Code", "Requested Give Amount - Minimum", "Requested Give Amount - Maximum", "Requested Give Units", "Requested Dosage Form", "Provider's Pharmacy/Treatment Instructions", "Provider's Administration Instructions", "Deliver-To Location", "Allow Substitutions", "Requested Dispense Code", "Requested Dispense Amount", "Requested Dispense Units", "Number Of Refills", "Ordering Provider's DEA Number", "Pharmacist/Treatment Supplier's Verifier ID", "Needs Human Review", "Requested Give Per (Time Unit)", "Requested Give Strength", "Requested Give Strength Units", "Indication", "Requested Give Rate Amount", "Requested Give Rate Units", "Total Daily Dose", "Supplementary Code", "Requested Drug Strength Volume", "Requested Drug Strength Volume Units", "Pharmacy Order Type", "Dispensing Interval",)
    _c_attrs = ("requested_give_code", "requested_give_amount_minimum", "requested_give_amount_maximum", "requested_give_units", "requested_dosage_form", "providers_pharmacy_or_treatment_instructions", "providers_administration_instructions", "deliver_to_location", "allow_substitutions", "requested_dispense_code", "requested_dispense_amount", "requested_dispense_units", "number_of_refills", "ordering_providers_dea_number", "pharmacist_or_treatment_suppliers_verifier_id", "needs_human_review", "requested_give_per", "requested_give_strength", "requested_give_strength_units", "indication", "requested_give_rate_amount", "requested_give_rate_units", "total_daily_dose", "supplementary_code", "requested_drug_strength_volume", "requested_drug_strength_volume_units", "pharmacy_order_type", "dispensing_interval",)
    # fmt: on

    def __init__(
        self,
        requested_give_code: CE | tuple[CE, ...] | None = None,  # RXO.1
        requested_give_amount_minimum: NM | tuple[NM, ...] | None = None,  # RXO.2
        requested_give_amount_maximum: NM | tuple[NM, ...] | None = None,  # RXO.3
        requested_give_units: CE | tuple[CE, ...] | None = None,  # RXO.4
        requested_dosage_form: CE | tuple[CE, ...] | None = None,  # RXO.5
        providers_pharmacy_or_treatment_instructions: CE
        | tuple[CE, ...]
        | None = None,  # RXO.6
        providers_administration_instructions: CE
        | tuple[CE, ...]
        | None = None,  # RXO.7
        deliver_to_location: LA1 | tuple[LA1, ...] | None = None,  # RXO.8
        allow_substitutions: AllowSubstitution
        | ID
        | tuple[AllowSubstitution | ID, ...]
        | None = None,  # RXO.9
        requested_dispense_code: CE | tuple[CE, ...] | None = None,  # RXO.10
        requested_dispense_amount: NM | tuple[NM, ...] | None = None,  # RXO.11
        requested_dispense_units: CE | tuple[CE, ...] | None = None,  # RXO.12
        number_of_refills: NM | tuple[NM, ...] | None = None,  # RXO.13
        ordering_providers_dea_number: XCN | tuple[XCN, ...] | None = None,  # RXO.14
        pharmacist_or_treatment_suppliers_verifier_id: XCN
        | tuple[XCN, ...]
        | None = None,  # RXO.15
        needs_human_review: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # RXO.16
        requested_give_per: ST | tuple[ST, ...] | None = None,  # RXO.17
        requested_give_strength: NM | tuple[NM, ...] | None = None,  # RXO.18
        requested_give_strength_units: CE | tuple[CE, ...] | None = None,  # RXO.19
        indication: CE | tuple[CE, ...] | None = None,  # RXO.20
        requested_give_rate_amount: ST | tuple[ST, ...] | None = None,  # RXO.21
        requested_give_rate_units: CE | tuple[CE, ...] | None = None,  # RXO.22
        total_daily_dose: CQ | tuple[CQ, ...] | None = None,  # RXO.23
        supplementary_code: CE | tuple[CE, ...] | None = None,  # RXO.24
        requested_drug_strength_volume: NM | tuple[NM, ...] | None = None,  # RXO.25
        requested_drug_strength_volume_units: CWE
        | tuple[CWE, ...]
        | None = None,  # RXO.26
        pharmacy_order_type: PharmacyOrderTypes
        | ID
        | tuple[PharmacyOrderTypes | ID, ...]
        | None = None,  # RXO.27
        dispensing_interval: NM | tuple[NM, ...] | None = None,  # RXO.28
    ):
        """
        Pharmacy/Treatment Order - `RXO <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO>`_
        This is the "master" pharmacy/treatment order segment. It contains order data not specific to components or additives. Unlike the OBR, it does not contain status fields or other data that are results-only.

        :param requested_give_code: Coded Element (id: RXO.1 | len: 250 | use: C | rpt: 1)
        :param requested_give_amount_minimum: Numeric (id: RXO.2 | len: 20 | use: C | rpt: 1)
        :param requested_give_amount_maximum: Numeric (id: RXO.3 | len: 20 | use: O | rpt: 1)
        :param requested_give_units: Coded Element (id: RXO.4 | len: 250 | use: C | rpt: 1)
        :param requested_dosage_form: Coded Element (id: RXO.5 | len: 250 | use: C | rpt: 1)
        :param providers_pharmacy_or_treatment_instructions: Coded Element (id: RXO.6 | len: 250 | use: O | rpt: *)
        :param providers_administration_instructions: Coded Element (id: RXO.7 | len: 250 | use: O | rpt: *)
        :param deliver_to_location: Location with Address Variation 1 (id: RXO.8 | len: 200 | use: O | rpt: 1)
        :param allow_substitutions: Coded values for HL7 tables (id: RXO.9 | len: 1 | use: O | rpt: 1)
        :param requested_dispense_code: Coded Element (id: RXO.10 | len: 250 | use: O | rpt: 1)
        :param requested_dispense_amount: Numeric (id: RXO.11 | len: 20 | use: O | rpt: 1)
        :param requested_dispense_units: Coded Element (id: RXO.12 | len: 250 | use: O | rpt: 1)
        :param number_of_refills: Numeric (id: RXO.13 | len: 3 | use: O | rpt: 1)
        :param ordering_providers_dea_number: Extended Composite ID Number and Name for Persons (id: RXO.14 | len: 250 | use: C | rpt: *)
        :param pharmacist_or_treatment_suppliers_verifier_id: Extended Composite ID Number and Name for Persons (id: RXO.15 | len: 250 | use: C | rpt: *)
        :param needs_human_review: Coded values for HL7 tables (id: RXO.16 | len: 1 | use: O | rpt: 1)
        :param requested_give_per: String Data (id: RXO.17 | len: 20 | use: C | rpt: 1)
        :param requested_give_strength: Numeric (id: RXO.18 | len: 20 | use: O | rpt: 1)
        :param requested_give_strength_units: Coded Element (id: RXO.19 | len: 250 | use: O | rpt: 1)
        :param indication: Coded Element (id: RXO.20 | len: 250 | use: O | rpt: *)
        :param requested_give_rate_amount: String Data (id: RXO.21 | len: 6 | use: O | rpt: 1)
        :param requested_give_rate_units: Coded Element (id: RXO.22 | len: 250 | use: O | rpt: 1)
        :param total_daily_dose: Composite Quantity with Units (id: RXO.23 | len: 10 | use: O | rpt: 1)
        :param supplementary_code: Coded Element (id: RXO.24 | len: 250 | use: O | rpt: *)
        :param requested_drug_strength_volume: Numeric (id: RXO.25 | len: 5 | use: O | rpt: 1)
        :param requested_drug_strength_volume_units: Coded with Exceptions (id: RXO.26 | len: 250 | use: O | rpt: 1)
        :param pharmacy_order_type: Coded values for HL7 tables (id: RXO.27 | len: 1 | use: O | rpt: 1)
        :param dispensing_interval: Numeric (id: RXO.28 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 28
        self.requested_give_code = requested_give_code
        self.requested_give_amount_minimum = requested_give_amount_minimum
        self.requested_give_amount_maximum = requested_give_amount_maximum
        self.requested_give_units = requested_give_units
        self.requested_dosage_form = requested_dosage_form
        self.providers_pharmacy_or_treatment_instructions = (
            providers_pharmacy_or_treatment_instructions
        )
        self.providers_administration_instructions = (
            providers_administration_instructions
        )
        self.deliver_to_location = deliver_to_location
        self.allow_substitutions = allow_substitutions
        self.requested_dispense_code = requested_dispense_code
        self.requested_dispense_amount = requested_dispense_amount
        self.requested_dispense_units = requested_dispense_units
        self.number_of_refills = number_of_refills
        self.ordering_providers_dea_number = ordering_providers_dea_number
        self.pharmacist_or_treatment_suppliers_verifier_id = (
            pharmacist_or_treatment_suppliers_verifier_id
        )
        self.needs_human_review = needs_human_review
        self.requested_give_per = requested_give_per
        self.requested_give_strength = requested_give_strength
        self.requested_give_strength_units = requested_give_strength_units
        self.indication = indication
        self.requested_give_rate_amount = requested_give_rate_amount
        self.requested_give_rate_units = requested_give_rate_units
        self.total_daily_dose = total_daily_dose
        self.supplementary_code = supplementary_code
        self.requested_drug_strength_volume = requested_drug_strength_volume
        self.requested_drug_strength_volume_units = requested_drug_strength_volume_units
        self.pharmacy_order_type = pharmacy_order_type
        self.dispensing_interval = dispensing_interval

    @property  # get RXO.1
    def requested_give_code(self) -> CE | None:
        """
        id: RXO.1 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.1
        """
        return self._c_data[0][0]

    @requested_give_code.setter  # set RXO.1
    def requested_give_code(self, ce: CE | None):
        """
        id: RXO.1 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.1
        """
        self._c_data[0] = (ce,)

    @property  # get RXO.2
    def requested_give_amount_minimum(self) -> NM | None:
        """
        id: RXO.2 | len: 20 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.2
        """
        return self._c_data[1][0]

    @requested_give_amount_minimum.setter  # set RXO.2
    def requested_give_amount_minimum(self, nm: NM | None):
        """
        id: RXO.2 | len: 20 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.2
        """
        self._c_data[1] = (nm,)

    @property  # get RXO.3
    def requested_give_amount_maximum(self) -> NM | None:
        """
        id: RXO.3 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.3
        """
        return self._c_data[2][0]

    @requested_give_amount_maximum.setter  # set RXO.3
    def requested_give_amount_maximum(self, nm: NM | None):
        """
        id: RXO.3 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.3
        """
        self._c_data[2] = (nm,)

    @property  # get RXO.4
    def requested_give_units(self) -> CE | None:
        """
        id: RXO.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.4
        """
        return self._c_data[3][0]

    @requested_give_units.setter  # set RXO.4
    def requested_give_units(self, ce: CE | None):
        """
        id: RXO.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.4
        """
        self._c_data[3] = (ce,)

    @property  # get RXO.5
    def requested_dosage_form(self) -> CE | None:
        """
        id: RXO.5 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.5
        """
        return self._c_data[4][0]

    @requested_dosage_form.setter  # set RXO.5
    def requested_dosage_form(self, ce: CE | None):
        """
        id: RXO.5 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.5
        """
        self._c_data[4] = (ce,)

    @property
    def providers_pharmacy_or_treatment_instructions(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXO.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.6
        """
        return self._c_data[5]

    @providers_pharmacy_or_treatment_instructions.setter  # set RXO.6
    def providers_pharmacy_or_treatment_instructions(self, ce: CE | tuple[CE] | None):
        """
        id: RXO.6 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.6
        """
        if isinstance(ce, tuple):
            self._c_data[5] = ce
        else:
            self._c_data[5] = (ce,)

    @property
    def providers_administration_instructions(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXO.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.7
        """
        return self._c_data[6]

    @providers_administration_instructions.setter  # set RXO.7
    def providers_administration_instructions(self, ce: CE | tuple[CE] | None):
        """
        id: RXO.7 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.7
        """
        if isinstance(ce, tuple):
            self._c_data[6] = ce
        else:
            self._c_data[6] = (ce,)

    @property  # get RXO.8
    def deliver_to_location(self) -> LA1 | None:
        """
        id: RXO.8 | len: 200 | use: O | rpt: 1
        ---
        return_type: LA1: Location with Address Variation 1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.8
        """
        return self._c_data[7][0]

    @deliver_to_location.setter  # set RXO.8
    def deliver_to_location(self, la1: LA1 | None):
        """
        id: RXO.8 | len: 200 | use: O | rpt: 1
        ---
        param_type: LA1: Location with Address Variation 1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.8
        """
        self._c_data[7] = (la1,)

    @property  # get RXO.9
    def allow_substitutions(self) -> AllowSubstitution | None:
        """
        id: RXO.9 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.9
        """
        return self._c_data[8][0]

    @allow_substitutions.setter  # set RXO.9
    def allow_substitutions(self, allow_substitution: AllowSubstitution | None):
        """
        id: RXO.9 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.9
        """
        self._c_data[8] = (allow_substitution,)

    @property  # get RXO.10
    def requested_dispense_code(self) -> CE | None:
        """
        id: RXO.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.10
        """
        return self._c_data[9][0]

    @requested_dispense_code.setter  # set RXO.10
    def requested_dispense_code(self, ce: CE | None):
        """
        id: RXO.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.10
        """
        self._c_data[9] = (ce,)

    @property  # get RXO.11
    def requested_dispense_amount(self) -> NM | None:
        """
        id: RXO.11 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.11
        """
        return self._c_data[10][0]

    @requested_dispense_amount.setter  # set RXO.11
    def requested_dispense_amount(self, nm: NM | None):
        """
        id: RXO.11 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.11
        """
        self._c_data[10] = (nm,)

    @property  # get RXO.12
    def requested_dispense_units(self) -> CE | None:
        """
        id: RXO.12 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.12
        """
        return self._c_data[11][0]

    @requested_dispense_units.setter  # set RXO.12
    def requested_dispense_units(self, ce: CE | None):
        """
        id: RXO.12 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.12
        """
        self._c_data[11] = (ce,)

    @property  # get RXO.13
    def number_of_refills(self) -> NM | None:
        """
        id: RXO.13 | len: 3 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.13
        """
        return self._c_data[12][0]

    @number_of_refills.setter  # set RXO.13
    def number_of_refills(self, nm: NM | None):
        """
        id: RXO.13 | len: 3 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.13
        """
        self._c_data[12] = (nm,)

    @property
    def ordering_providers_dea_number(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: RXO.14 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.14
        """
        return self._c_data[13]

    @ordering_providers_dea_number.setter  # set RXO.14
    def ordering_providers_dea_number(self, xcn: XCN | tuple[XCN] | None):
        """
        id: RXO.14 | len: 250 | use: C | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.14
        """
        if isinstance(xcn, tuple):
            self._c_data[13] = xcn
        else:
            self._c_data[13] = (xcn,)

    @property
    def pharmacist_or_treatment_suppliers_verifier_id(
        self,
    ) -> tuple[XCN, ...] | tuple[None]:
        """
        id: RXO.15 | len: 250 | use: C | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.15
        """
        return self._c_data[14]

    @pharmacist_or_treatment_suppliers_verifier_id.setter  # set RXO.15
    def pharmacist_or_treatment_suppliers_verifier_id(
        self, xcn: XCN | tuple[XCN] | None
    ):
        """
        id: RXO.15 | len: 250 | use: C | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.15
        """
        if isinstance(xcn, tuple):
            self._c_data[14] = xcn
        else:
            self._c_data[14] = (xcn,)

    @property  # get RXO.16
    def needs_human_review(self) -> YesOrNoIndicator | None:
        """
        id: RXO.16 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.16
        """
        return self._c_data[15][0]

    @needs_human_review.setter  # set RXO.16
    def needs_human_review(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RXO.16 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.16
        """
        self._c_data[15] = (yes_or_no_indicator,)

    @property  # get RXO.17
    def requested_give_per(self) -> ST | None:
        """
        id: RXO.17 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.17
        """
        return self._c_data[16][0]

    @requested_give_per.setter  # set RXO.17
    def requested_give_per(self, st: ST | None):
        """
        id: RXO.17 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.17
        """
        self._c_data[16] = (st,)

    @property  # get RXO.18
    def requested_give_strength(self) -> NM | None:
        """
        id: RXO.18 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.18
        """
        return self._c_data[17][0]

    @requested_give_strength.setter  # set RXO.18
    def requested_give_strength(self, nm: NM | None):
        """
        id: RXO.18 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.18
        """
        self._c_data[17] = (nm,)

    @property  # get RXO.19
    def requested_give_strength_units(self) -> CE | None:
        """
        id: RXO.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.19
        """
        return self._c_data[18][0]

    @requested_give_strength_units.setter  # set RXO.19
    def requested_give_strength_units(self, ce: CE | None):
        """
        id: RXO.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.19
        """
        self._c_data[18] = (ce,)

    @property
    def indication(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXO.20 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.20
        """
        return self._c_data[19]

    @indication.setter  # set RXO.20
    def indication(self, ce: CE | tuple[CE] | None):
        """
        id: RXO.20 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.20
        """
        if isinstance(ce, tuple):
            self._c_data[19] = ce
        else:
            self._c_data[19] = (ce,)

    @property  # get RXO.21
    def requested_give_rate_amount(self) -> ST | None:
        """
        id: RXO.21 | len: 6 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.21
        """
        return self._c_data[20][0]

    @requested_give_rate_amount.setter  # set RXO.21
    def requested_give_rate_amount(self, st: ST | None):
        """
        id: RXO.21 | len: 6 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.21
        """
        self._c_data[20] = (st,)

    @property  # get RXO.22
    def requested_give_rate_units(self) -> CE | None:
        """
        id: RXO.22 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.22
        """
        return self._c_data[21][0]

    @requested_give_rate_units.setter  # set RXO.22
    def requested_give_rate_units(self, ce: CE | None):
        """
        id: RXO.22 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.22
        """
        self._c_data[21] = (ce,)

    @property  # get RXO.23
    def total_daily_dose(self) -> CQ | None:
        """
        id: RXO.23 | len: 10 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.23
        """
        return self._c_data[22][0]

    @total_daily_dose.setter  # set RXO.23
    def total_daily_dose(self, cq: CQ | None):
        """
        id: RXO.23 | len: 10 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.23
        """
        self._c_data[22] = (cq,)

    @property
    def supplementary_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXO.24 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.24
        """
        return self._c_data[23]

    @supplementary_code.setter  # set RXO.24
    def supplementary_code(self, ce: CE | tuple[CE] | None):
        """
        id: RXO.24 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.24
        """
        if isinstance(ce, tuple):
            self._c_data[23] = ce
        else:
            self._c_data[23] = (ce,)

    @property  # get RXO.25
    def requested_drug_strength_volume(self) -> NM | None:
        """
        id: RXO.25 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.25
        """
        return self._c_data[24][0]

    @requested_drug_strength_volume.setter  # set RXO.25
    def requested_drug_strength_volume(self, nm: NM | None):
        """
        id: RXO.25 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.25
        """
        self._c_data[24] = (nm,)

    @property  # get RXO.26
    def requested_drug_strength_volume_units(self) -> CWE | None:
        """
        id: RXO.26 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.26
        """
        return self._c_data[25][0]

    @requested_drug_strength_volume_units.setter  # set RXO.26
    def requested_drug_strength_volume_units(self, cwe: CWE | None):
        """
        id: RXO.26 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.26
        """
        self._c_data[25] = (cwe,)

    @property  # get RXO.27
    def pharmacy_order_type(self) -> PharmacyOrderTypes | None:
        """
        id: RXO.27 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.27
        """
        return self._c_data[26][0]

    @pharmacy_order_type.setter  # set RXO.27
    def pharmacy_order_type(self, pharmacy_order_types: PharmacyOrderTypes | None):
        """
        id: RXO.27 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.27
        """
        self._c_data[26] = (pharmacy_order_types,)

    @property  # get RXO.28
    def dispensing_interval(self) -> NM | None:
        """
        id: RXO.28 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.28
        """
        return self._c_data[27][0]

    @dispensing_interval.setter  # set RXO.28
    def dispensing_interval(self, nm: NM | None):
        """
        id: RXO.28 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXO.28
        """
        self._c_data[27] = (nm,)
