from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.CWE import CWE
from ..data_types.XCN import XCN
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.LA2 import LA2
from ..tables.PharmacyOrderTypes import PharmacyOrderTypes
from ..tables.VaccinesAdministered import VaccinesAdministered
from ..tables.CompletionStatus import CompletionStatus
from ..tables.ManufacturersOfVaccines import ManufacturersOfVaccines
from ..tables.ActionCode import ActionCode


"""
Pharmacy/Treatment Administration - RXA
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RXA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RXA,
    TS, ID, NM, CWE, XCN, CE, ST, LA2
)

rxa = RXA(  #  - The ORC must have the filler order number and the order control code RE
    give_sub_id_counter=nm,  # NM(...)  # Required.
    administration_sub_id_counter=nm,  # NM(...)  # Required.
    date_or_time_start_of_administration=ts,  # TS(...)  # Required.
    date_or_time_end_of_administration=ts,  # TS(...)  # Required.
    administered_code=ce,  # CE(...)  # Required.
    administered_amount=nm,  # NM(...)  # Required.
    administered_units=None,  # CE(...) 
    administered_dosage_form=None,  # CE(...) 
    administration_notes=None,  # CE(...) 
    administering_provider=None,  # XCN(...) 
    administered_at_location=None,  # LA2(...) 
    administered_per=None,  # ST(...) 
    administered_strength=None,  # NM(...) 
    administered_strength_units=None,  # CE(...) 
    substance_lot_number=None,  # ST(...) 
    substance_expiration_date=None,  # TS(...) 
    substance_manufacturer_name=None,  # CE(...) 
    substance_or_treatment_refusal_reason=None,  # CE(...) 
    indication=None,  # CE(...) 
    completion_status=None,  # ID(...) 
    action_code_rxa=None,  # ID(...) 
    system_entry_date_or_time=None,  # TS(...) 
    administered_drug_strength_volume=None,  # NM(...) 
    administered_drug_strength_volume_units=None,  # CWE(...) 
    administered_barcode_identifier=None,  # CWE(...) 
    pharmacy_order_type=None,  # ID(...) 
)

-----END SEGMENT::RXA TEMPLATE-----
"""


class RXA(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RXA"""
    _hl7_name = """Pharmacy/Treatment Administration"""
    _hl7_description = """The ORC must have the filler order number and the order control code RE"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA"
    _c_length = (4, 4, 26, 26, 250, 20, 250, 250, 250, 250, 200, 20, 20, 250, 20, 26, 250, 250, 250, 2, 2, 26, 5, 250, 60, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 1, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "R", "R", "C", "O", "O", "O", "C", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, NM, TS, TS, CE, NM, CE, CE, CE, XCN, LA2, ST, NM, CE, ST, TS, CE, CE, CE, ID, ID, TS, NM, CWE, CWE, ID,)
    _c_aliases = ("RXA.1", "RXA.2", "RXA.3", "RXA.4", "RXA.5", "RXA.6", "RXA.7", "RXA.8", "RXA.9", "RXA.10", "RXA.11", "RXA.12", "RXA.13", "RXA.14", "RXA.15", "RXA.16", "RXA.17", "RXA.18", "RXA.19", "RXA.20", "RXA.21", "RXA.22", "RXA.23", "RXA.24", "RXA.25", "RXA.26",)
    _c_names = ("Give Sub-ID Counter", "Administration Sub-ID Counter", "Date/Time Start of Administration", "Date/Time End of Administration", "Administered Code", "Administered Amount", "Administered Units", "Administered Dosage Form", "Administration Notes", "Administering Provider", "Administered-at Location", "Administered Per (Time Unit)", "Administered Strength", "Administered Strength Units", "Substance Lot Number", "Substance Expiration Date", "Substance Manufacturer Name", "Substance/Treatment Refusal Reason", "Indication", "Completion Status", "Action Code - RXA", "System Entry Date/Time", "Administered Drug Strength Volume", "Administered Drug Strength Volume Units", "Administered Barcode Identifier", "Pharmacy Order Type",)
    _c_attrs = ("give_sub_id_counter", "administration_sub_id_counter", "date_or_time_start_of_administration", "date_or_time_end_of_administration", "administered_code", "administered_amount", "administered_units", "administered_dosage_form", "administration_notes", "administering_provider", "administered_at_location", "administered_per", "administered_strength", "administered_strength_units", "substance_lot_number", "substance_expiration_date", "substance_manufacturer_name", "substance_or_treatment_refusal_reason", "indication", "completion_status", "action_code_rxa", "system_entry_date_or_time", "administered_drug_strength_volume", "administered_drug_strength_volume_units", "administered_barcode_identifier", "pharmacy_order_type",)
    # fmt: on

    def __init__(
        self,
        give_sub_id_counter: NM | tuple[NM],  # RXA.1
        administration_sub_id_counter: NM | tuple[NM],  # RXA.2
        date_or_time_start_of_administration: TS | tuple[TS],  # RXA.3
        date_or_time_end_of_administration: TS | tuple[TS],  # RXA.4
        administered_code: VaccinesAdministered
        | CE
        | tuple[VaccinesAdministered | CE],  # RXA.5
        administered_amount: NM | tuple[NM],  # RXA.6
        administered_units: CE | tuple[CE] | None = None,  # RXA.7
        administered_dosage_form: CE | tuple[CE] | None = None,  # RXA.8
        administration_notes: CE | tuple[CE] | None = None,  # RXA.9
        administering_provider: XCN | tuple[XCN] | None = None,  # RXA.10
        administered_at_location: LA2 | tuple[LA2] | None = None,  # RXA.11
        administered_per: ST | tuple[ST] | None = None,  # RXA.12
        administered_strength: NM | tuple[NM] | None = None,  # RXA.13
        administered_strength_units: CE | tuple[CE] | None = None,  # RXA.14
        substance_lot_number: ST | tuple[ST] | None = None,  # RXA.15
        substance_expiration_date: TS | tuple[TS] | None = None,  # RXA.16
        substance_manufacturer_name: ManufacturersOfVaccines
        | CE
        | tuple[ManufacturersOfVaccines | CE]
        | None = None,  # RXA.17
        substance_or_treatment_refusal_reason: CE | tuple[CE] | None = None,  # RXA.18
        indication: CE | tuple[CE] | None = None,  # RXA.19
        completion_status: CompletionStatus
        | ID
        | tuple[CompletionStatus | ID]
        | None = None,  # RXA.20
        action_code_rxa: ActionCode
        | ID
        | tuple[ActionCode | ID]
        | None = None,  # RXA.21
        system_entry_date_or_time: TS | tuple[TS] | None = None,  # RXA.22
        administered_drug_strength_volume: NM | tuple[NM] | None = None,  # RXA.23
        administered_drug_strength_volume_units: CWE
        | tuple[CWE]
        | None = None,  # RXA.24
        administered_barcode_identifier: CWE | tuple[CWE] | None = None,  # RXA.25
        pharmacy_order_type: PharmacyOrderTypes
        | ID
        | tuple[PharmacyOrderTypes | ID]
        | None = None,  # RXA.26
    ):
        """
        Pharmacy/Treatment Administration - `RXA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA>`_
        The ORC must have the filler order number and the order control code RE. As a site-specific variant, the RXO and associated RXCs and/or the RXE (and associated RXCs) may be present if the receiving application needs any of their data. The RXA carries the administration data.

        :param give_sub_id_counter: Numeric (id: RXA.1 | len: 4 | use: R | rpt: 1)
        :param administration_sub_id_counter: Numeric (id: RXA.2 | len: 4 | use: R | rpt: 1)
        :param date_or_time_start_of_administration: Time Stamp (id: RXA.3 | len: 26 | use: R | rpt: 1)
        :param date_or_time_end_of_administration: Time Stamp (id: RXA.4 | len: 26 | use: R | rpt: 1)
        :param administered_code: Coded Element (id: RXA.5 | len: 250 | use: R | rpt: 1)
        :param administered_amount: Numeric (id: RXA.6 | len: 20 | use: R | rpt: 1)
        :param administered_units: Coded Element (id: RXA.7 | len: 250 | use: C | rpt: 1)
        :param administered_dosage_form: Coded Element (id: RXA.8 | len: 250 | use: O | rpt: 1)
        :param administration_notes: Coded Element (id: RXA.9 | len: 250 | use: O | rpt: *)
        :param administering_provider: Extended Composite ID Number and Name for Persons (id: RXA.10 | len: 250 | use: O | rpt: *)
        :param administered_at_location: Location with Address Variation 2 (id: RXA.11 | len: 200 | use: C | rpt: 1)
        :param administered_per: String Data (id: RXA.12 | len: 20 | use: C | rpt: 1)
        :param administered_strength: Numeric (id: RXA.13 | len: 20 | use: O | rpt: 1)
        :param administered_strength_units: Coded Element (id: RXA.14 | len: 250 | use: O | rpt: 1)
        :param substance_lot_number: String Data (id: RXA.15 | len: 20 | use: O | rpt: *)
        :param substance_expiration_date: Time Stamp (id: RXA.16 | len: 26 | use: O | rpt: *)
        :param substance_manufacturer_name: Coded Element (id: RXA.17 | len: 250 | use: O | rpt: *)
        :param substance_or_treatment_refusal_reason: Coded Element (id: RXA.18 | len: 250 | use: O | rpt: *)
        :param indication: Coded Element (id: RXA.19 | len: 250 | use: O | rpt: *)
        :param completion_status: Coded values for HL7 tables (id: RXA.20 | len: 2 | use: O | rpt: 1)
        :param action_code_rxa: Coded values for HL7 tables (id: RXA.21 | len: 2 | use: O | rpt: 1)
        :param system_entry_date_or_time: Time Stamp (id: RXA.22 | len: 26 | use: O | rpt: 1)
        :param administered_drug_strength_volume: Numeric (id: RXA.23 | len: 5 | use: O | rpt: 1)
        :param administered_drug_strength_volume_units: Coded with Exceptions (id: RXA.24 | len: 250 | use: O | rpt: 1)
        :param administered_barcode_identifier: Coded with Exceptions (id: RXA.25 | len: 60 | use: O | rpt: 1)
        :param pharmacy_order_type: Coded values for HL7 tables (id: RXA.26 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 26
        self.give_sub_id_counter = give_sub_id_counter
        self.administration_sub_id_counter = administration_sub_id_counter
        self.date_or_time_start_of_administration = date_or_time_start_of_administration
        self.date_or_time_end_of_administration = date_or_time_end_of_administration
        self.administered_code = administered_code
        self.administered_amount = administered_amount
        self.administered_units = administered_units
        self.administered_dosage_form = administered_dosage_form
        self.administration_notes = administration_notes
        self.administering_provider = administering_provider
        self.administered_at_location = administered_at_location
        self.administered_per = administered_per
        self.administered_strength = administered_strength
        self.administered_strength_units = administered_strength_units
        self.substance_lot_number = substance_lot_number
        self.substance_expiration_date = substance_expiration_date
        self.substance_manufacturer_name = substance_manufacturer_name
        self.substance_or_treatment_refusal_reason = (
            substance_or_treatment_refusal_reason
        )
        self.indication = indication
        self.completion_status = completion_status
        self.action_code_rxa = action_code_rxa
        self.system_entry_date_or_time = system_entry_date_or_time
        self.administered_drug_strength_volume = administered_drug_strength_volume
        self.administered_drug_strength_volume_units = (
            administered_drug_strength_volume_units
        )
        self.administered_barcode_identifier = administered_barcode_identifier
        self.pharmacy_order_type = pharmacy_order_type

    @property  # get RXA.1
    def give_sub_id_counter(self) -> NM:
        """
        id: RXA.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.1
        """
        return self._c_data[0][0]

    @give_sub_id_counter.setter  # set RXA.1
    def give_sub_id_counter(self, nm: NM):
        """
        id: RXA.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.1
        """
        self._c_data[0] = (nm,)

    @property  # get RXA.2
    def administration_sub_id_counter(self) -> NM:
        """
        id: RXA.2 | len: 4 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.2
        """
        return self._c_data[1][0]

    @administration_sub_id_counter.setter  # set RXA.2
    def administration_sub_id_counter(self, nm: NM):
        """
        id: RXA.2 | len: 4 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.2
        """
        self._c_data[1] = (nm,)

    @property  # get RXA.3
    def date_or_time_start_of_administration(self) -> TS:
        """
        id: RXA.3 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.3
        """
        return self._c_data[2][0]

    @date_or_time_start_of_administration.setter  # set RXA.3
    def date_or_time_start_of_administration(self, ts: TS):
        """
        id: RXA.3 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.3
        """
        self._c_data[2] = (ts,)

    @property  # get RXA.4
    def date_or_time_end_of_administration(self) -> TS:
        """
        id: RXA.4 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.4
        """
        return self._c_data[3][0]

    @date_or_time_end_of_administration.setter  # set RXA.4
    def date_or_time_end_of_administration(self, ts: TS):
        """
        id: RXA.4 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.4
        """
        self._c_data[3] = (ts,)

    @property  # get RXA.5
    def administered_code(self) -> VaccinesAdministered:
        """
        id: RXA.5 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.5
        """
        return self._c_data[4][0]

    @administered_code.setter  # set RXA.5
    def administered_code(self, vaccines_administered: VaccinesAdministered):
        """
        id: RXA.5 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.5
        """
        self._c_data[4] = (vaccines_administered,)

    @property  # get RXA.6
    def administered_amount(self) -> NM:
        """
        id: RXA.6 | len: 20 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.6
        """
        return self._c_data[5][0]

    @administered_amount.setter  # set RXA.6
    def administered_amount(self, nm: NM):
        """
        id: RXA.6 | len: 20 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.6
        """
        self._c_data[5] = (nm,)

    @property  # get RXA.7
    def administered_units(self) -> CE | None:
        """
        id: RXA.7 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.7
        """
        return self._c_data[6][0]

    @administered_units.setter  # set RXA.7
    def administered_units(self, ce: CE | None):
        """
        id: RXA.7 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.7
        """
        self._c_data[6] = (ce,)

    @property  # get RXA.8
    def administered_dosage_form(self) -> CE | None:
        """
        id: RXA.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.8
        """
        return self._c_data[7][0]

    @administered_dosage_form.setter  # set RXA.8
    def administered_dosage_form(self, ce: CE | None):
        """
        id: RXA.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.8
        """
        self._c_data[7] = (ce,)

    @property
    def administration_notes(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXA.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.9
        """
        return self._c_data[8]

    @administration_notes.setter  # set RXA.9
    def administration_notes(self, ce: CE | tuple[CE] | None):
        """
        id: RXA.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.9
        """
        if isinstance(ce, tuple):
            self._c_data[8] = ce
        else:
            self._c_data[8] = (ce,)

    @property
    def administering_provider(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: RXA.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.10
        """
        return self._c_data[9]

    @administering_provider.setter  # set RXA.10
    def administering_provider(self, xcn: XCN | tuple[XCN] | None):
        """
        id: RXA.10 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.10
        """
        if isinstance(xcn, tuple):
            self._c_data[9] = xcn
        else:
            self._c_data[9] = (xcn,)

    @property  # get RXA.11
    def administered_at_location(self) -> LA2 | None:
        """
        id: RXA.11 | len: 200 | use: C | rpt: 1
        ---
        return_type: LA2: Location with Address Variation 2
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.11
        """
        return self._c_data[10][0]

    @administered_at_location.setter  # set RXA.11
    def administered_at_location(self, la2: LA2 | None):
        """
        id: RXA.11 | len: 200 | use: C | rpt: 1
        ---
        param_type: LA2: Location with Address Variation 2
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.11
        """
        self._c_data[10] = (la2,)

    @property  # get RXA.12
    def administered_per(self) -> ST | None:
        """
        id: RXA.12 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.12
        """
        return self._c_data[11][0]

    @administered_per.setter  # set RXA.12
    def administered_per(self, st: ST | None):
        """
        id: RXA.12 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.12
        """
        self._c_data[11] = (st,)

    @property  # get RXA.13
    def administered_strength(self) -> NM | None:
        """
        id: RXA.13 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.13
        """
        return self._c_data[12][0]

    @administered_strength.setter  # set RXA.13
    def administered_strength(self, nm: NM | None):
        """
        id: RXA.13 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.13
        """
        self._c_data[12] = (nm,)

    @property  # get RXA.14
    def administered_strength_units(self) -> CE | None:
        """
        id: RXA.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.14
        """
        return self._c_data[13][0]

    @administered_strength_units.setter  # set RXA.14
    def administered_strength_units(self, ce: CE | None):
        """
        id: RXA.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.14
        """
        self._c_data[13] = (ce,)

    @property
    def substance_lot_number(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: RXA.15 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.15
        """
        return self._c_data[14]

    @substance_lot_number.setter  # set RXA.15
    def substance_lot_number(self, st: ST | tuple[ST] | None):
        """
        id: RXA.15 | len: 20 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.15
        """
        if isinstance(st, tuple):
            self._c_data[14] = st
        else:
            self._c_data[14] = (st,)

    @property
    def substance_expiration_date(self) -> tuple[TS, ...] | tuple[None]:
        """
        id: RXA.16 | len: 26 | use: O | rpt: *
        ---
        return_type: tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.16
        """
        return self._c_data[15]

    @substance_expiration_date.setter  # set RXA.16
    def substance_expiration_date(self, ts: TS | tuple[TS] | None):
        """
        id: RXA.16 | len: 26 | use: O | rpt: *
        ---
        param_type: TS | tuple[TS, ...]: (Time Stamp, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.16
        """
        if isinstance(ts, tuple):
            self._c_data[15] = ts
        else:
            self._c_data[15] = (ts,)

    @property
    def substance_manufacturer_name(
        self,
    ) -> tuple[ManufacturersOfVaccines, ...] | tuple[None]:
        """
        id: RXA.17 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.17
        """
        return self._c_data[16]

    @substance_manufacturer_name.setter  # set RXA.17
    def substance_manufacturer_name(
        self,
        manufacturers_of_vaccines: ManufacturersOfVaccines
        | tuple[ManufacturersOfVaccines]
        | None,
    ):
        """
        id: RXA.17 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.17
        """
        if isinstance(manufacturers_of_vaccines, tuple):
            self._c_data[16] = manufacturers_of_vaccines
        else:
            self._c_data[16] = (manufacturers_of_vaccines,)

    @property
    def substance_or_treatment_refusal_reason(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXA.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.18
        """
        return self._c_data[17]

    @substance_or_treatment_refusal_reason.setter  # set RXA.18
    def substance_or_treatment_refusal_reason(self, ce: CE | tuple[CE] | None):
        """
        id: RXA.18 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.18
        """
        if isinstance(ce, tuple):
            self._c_data[17] = ce
        else:
            self._c_data[17] = (ce,)

    @property
    def indication(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: RXA.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.19
        """
        return self._c_data[18]

    @indication.setter  # set RXA.19
    def indication(self, ce: CE | tuple[CE] | None):
        """
        id: RXA.19 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.19
        """
        if isinstance(ce, tuple):
            self._c_data[18] = ce
        else:
            self._c_data[18] = (ce,)

    @property  # get RXA.20
    def completion_status(self) -> CompletionStatus | None:
        """
        id: RXA.20 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.20
        """
        return self._c_data[19][0]

    @completion_status.setter  # set RXA.20
    def completion_status(self, completion_status: CompletionStatus | None):
        """
        id: RXA.20 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.20
        """
        self._c_data[19] = (completion_status,)

    @property  # get RXA.21
    def action_code_rxa(self) -> ActionCode | None:
        """
        id: RXA.21 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.21
        """
        return self._c_data[20][0]

    @action_code_rxa.setter  # set RXA.21
    def action_code_rxa(self, action_code: ActionCode | None):
        """
        id: RXA.21 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.21
        """
        self._c_data[20] = (action_code,)

    @property  # get RXA.22
    def system_entry_date_or_time(self) -> TS | None:
        """
        id: RXA.22 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.22
        """
        return self._c_data[21][0]

    @system_entry_date_or_time.setter  # set RXA.22
    def system_entry_date_or_time(self, ts: TS | None):
        """
        id: RXA.22 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.22
        """
        self._c_data[21] = (ts,)

    @property  # get RXA.23
    def administered_drug_strength_volume(self) -> NM | None:
        """
        id: RXA.23 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.23
        """
        return self._c_data[22][0]

    @administered_drug_strength_volume.setter  # set RXA.23
    def administered_drug_strength_volume(self, nm: NM | None):
        """
        id: RXA.23 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.23
        """
        self._c_data[22] = (nm,)

    @property  # get RXA.24
    def administered_drug_strength_volume_units(self) -> CWE | None:
        """
        id: RXA.24 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.24
        """
        return self._c_data[23][0]

    @administered_drug_strength_volume_units.setter  # set RXA.24
    def administered_drug_strength_volume_units(self, cwe: CWE | None):
        """
        id: RXA.24 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.24
        """
        self._c_data[23] = (cwe,)

    @property  # get RXA.25
    def administered_barcode_identifier(self) -> CWE | None:
        """
        id: RXA.25 | len: 60 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.25
        """
        return self._c_data[24][0]

    @administered_barcode_identifier.setter  # set RXA.25
    def administered_barcode_identifier(self, cwe: CWE | None):
        """
        id: RXA.25 | len: 60 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.25
        """
        self._c_data[24] = (cwe,)

    @property  # get RXA.26
    def pharmacy_order_type(self) -> PharmacyOrderTypes | None:
        """
        id: RXA.26 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.26
        """
        return self._c_data[25][0]

    @pharmacy_order_type.setter  # set RXA.26
    def pharmacy_order_type(self, pharmacy_order_types: PharmacyOrderTypes | None):
        """
        id: RXA.26 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RXA.26
        """
        self._c_data[25] = (pharmacy_order_types,)
