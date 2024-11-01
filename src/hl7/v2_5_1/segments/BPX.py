from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.CNE import CNE
from ..data_types.NM import NM
from ..data_types.PL import PL
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.XAD import XAD
from ..data_types.EI import EI
from ..data_types.XCN import XCN
from ..data_types.XON import XON
from ..tables.BloodProductDispenseStatus import BloodProductDispenseStatus
from ..tables.CommercialProduct import CommercialProduct
from ..tables.BpObservationStatusCodesInterpretation import (
    BpObservationStatusCodesInterpretation,
)


"""
Blood product dispense status - BPX
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BPX TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BPX,
    TS, ID, CNE, NM, PL, CWE, SI, CE, XAD, EI, XCN, XON
)

bpx = BPX(  #  - In the processing of blood products, it is necessary for the transfusion service and the placer system to communicate information
    set_id_bpx=si,  # SI(...)  # Required.
    bp_dispense_status=cwe,  # CWE(...)  # Required.
    bp_status=id,  # ID(...)  # Required.
    bp_date_or_time_of_status=ts,  # TS(...)  # Required.
    bc_donation_id=None,  # EI(...) 
    bc_component=None,  # CNE(...) 
    bc_donation_type_or_intended_use=None,  # CNE(...) 
    cp_commercial_product=None,  # CWE(...) 
    cp_manufacturer=None,  # XON(...) 
    cp_lot_number=None,  # EI(...) 
    bp_blood_group=None,  # CNE(...) 
    bc_special_testing=None,  # CNE(...) 
    bp_expiration_date_or_time=None,  # TS(...) 
    bp_quantity=nm,  # NM(...)  # Required.
    bp_amount=None,  # NM(...) 
    bp_units=None,  # CE(...) 
    bp_unique_id=None,  # EI(...) 
    bp_actual_dispensed_to_location=None,  # PL(...) 
    bp_actual_dispensed_to_address=None,  # XAD(...) 
    bp_dispensed_to_receiver=None,  # XCN(...) 
    bp_dispensing_individual=None,  # XCN(...) 
)

-----END SEGMENT::BPX TEMPLATE-----
"""


class BPX(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BPX"""
    _hl7_name = """Blood product dispense status"""
    _hl7_description = """In the processing of blood products, it is necessary for the transfusion service and the placer system to communicate information"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPX"
    _c_length = (4, 250, 1, 26, 22, 250, 250, 250, 250, 22, 250, 250, 26, 5, 5, 250, 22, 80, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "R", "C", "C", "O", "C", "C", "C", "O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CWE, ID, TS, EI, CNE, CNE, CWE, XON, EI, CNE, CNE, TS, NM, NM, CE, EI, PL, XAD, XCN, XCN,)
    _c_aliases = ("BPX.1", "BPX.2", "BPX.3", "BPX.4", "BPX.5", "BPX.6", "BPX.7", "BPX.8", "BPX.9", "BPX.10", "BPX.11", "BPX.12", "BPX.13", "BPX.14", "BPX.15", "BPX.16", "BPX.17", "BPX.18", "BPX.19", "BPX.20", "BPX.21",)
    _c_names = ("Set ID - BPX", "BP Dispense Status", "BP Status", "BP Date/Time of Status", "BC Donation ID", "BC Component", "BC Donation Type / Intended Use", "CP Commercial Product", "CP Manufacturer", "CP Lot Number", "BP Blood Group", "BC Special Testing", "BP Expiration Date/Time", "BP Quantity", "BP Amount", "BP Units", "BP Unique ID", "BP Actual Dispensed To Location", "BP Actual Dispensed To Address", "BP Dispensed to Receiver", "BP Dispensing Individual",)
    _c_attrs = ("set_id_bpx", "bp_dispense_status", "bp_status", "bp_date_or_time_of_status", "bc_donation_id", "bc_component", "bc_donation_type_or_intended_use", "cp_commercial_product", "cp_manufacturer", "cp_lot_number", "bp_blood_group", "bc_special_testing", "bp_expiration_date_or_time", "bp_quantity", "bp_amount", "bp_units", "bp_unique_id", "bp_actual_dispensed_to_location", "bp_actual_dispensed_to_address", "bp_dispensed_to_receiver", "bp_dispensing_individual",)
    # fmt: on

    def __init__(
        self,
        set_id_bpx: SI | tuple[SI],  # BPX.1
        bp_dispense_status: BloodProductDispenseStatus
        | CWE
        | tuple[BloodProductDispenseStatus | CWE],  # BPX.2
        bp_status: BpObservationStatusCodesInterpretation
        | ID
        | tuple[BpObservationStatusCodesInterpretation | ID],  # BPX.3
        bp_date_or_time_of_status: TS | tuple[TS],  # BPX.4
        bp_quantity: NM | tuple[NM],  # BPX.14
        bc_donation_id: EI | tuple[EI] | None = None,  # BPX.5
        bc_component: CNE | tuple[CNE] | None = None,  # BPX.6
        bc_donation_type_or_intended_use: CNE | tuple[CNE] | None = None,  # BPX.7
        cp_commercial_product: CommercialProduct
        | CWE
        | tuple[CommercialProduct | CWE]
        | None = None,  # BPX.8
        cp_manufacturer: XON | tuple[XON] | None = None,  # BPX.9
        cp_lot_number: EI | tuple[EI] | None = None,  # BPX.10
        bp_blood_group: CNE | tuple[CNE] | None = None,  # BPX.11
        bc_special_testing: CNE | tuple[CNE] | None = None,  # BPX.12
        bp_expiration_date_or_time: TS | tuple[TS] | None = None,  # BPX.13
        bp_amount: NM | tuple[NM] | None = None,  # BPX.15
        bp_units: CE | tuple[CE] | None = None,  # BPX.16
        bp_unique_id: EI | tuple[EI] | None = None,  # BPX.17
        bp_actual_dispensed_to_location: PL | tuple[PL] | None = None,  # BPX.18
        bp_actual_dispensed_to_address: XAD | tuple[XAD] | None = None,  # BPX.19
        bp_dispensed_to_receiver: XCN | tuple[XCN] | None = None,  # BPX.20
        bp_dispensing_individual: XCN | tuple[XCN] | None = None,  # BPX.21
    ):
        """
        Blood product dispense status - `BPX <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPX>`_
        In the processing of blood products, it is necessary for the transfusion service and the placer system to communicate information. The status messages need to contain additional information regarding the blood products requested, such as the unique donation ID, product code, blood type, expiration date/time of the blood product, and current status of the product. This segment is similar to an OBX segment, but contains additional attributes.

        :param set_id_bpx: Sequence ID (id: BPX.1 | len: 4 | use: R | rpt: 1)
        :param bp_dispense_status: Coded with Exceptions (id: BPX.2 | len: 250 | use: R | rpt: 1)
        :param bp_status: Coded values for HL7 tables (id: BPX.3 | len: 1 | use: R | rpt: 1)
        :param bp_date_or_time_of_status: Time Stamp (id: BPX.4 | len: 26 | use: R | rpt: 1)
        :param bc_donation_id: Entity Identifier (id: BPX.5 | len: 22 | use: C | rpt: 1)
        :param bc_component: Coded with No Exceptions (id: BPX.6 | len: 250 | use: C | rpt: 1)
        :param bc_donation_type_or_intended_use: Coded with No Exceptions (id: BPX.7 | len: 250 | use: O | rpt: 1)
        :param cp_commercial_product: Coded with Exceptions (id: BPX.8 | len: 250 | use: C | rpt: 1)
        :param cp_manufacturer: Extended Composite Name and Identification Number for Organizations (id: BPX.9 | len: 250 | use: C | rpt: 1)
        :param cp_lot_number: Entity Identifier (id: BPX.10 | len: 22 | use: C | rpt: 1)
        :param bp_blood_group: Coded with No Exceptions (id: BPX.11 | len: 250 | use: O | rpt: 1)
        :param bc_special_testing: Coded with No Exceptions (id: BPX.12 | len: 250 | use: O | rpt: *)
        :param bp_expiration_date_or_time: Time Stamp (id: BPX.13 | len: 26 | use: O | rpt: 1)
        :param bp_quantity: Numeric (id: BPX.14 | len: 5 | use: R | rpt: 1)
        :param bp_amount: Numeric (id: BPX.15 | len: 5 | use: O | rpt: 1)
        :param bp_units: Coded Element (id: BPX.16 | len: 250 | use: O | rpt: 1)
        :param bp_unique_id: Entity Identifier (id: BPX.17 | len: 22 | use: O | rpt: 1)
        :param bp_actual_dispensed_to_location: Person Location (id: BPX.18 | len: 80 | use: O | rpt: 1)
        :param bp_actual_dispensed_to_address: Extended Address (id: BPX.19 | len: 250 | use: O | rpt: 1)
        :param bp_dispensed_to_receiver: Extended Composite ID Number and Name for Persons (id: BPX.20 | len: 250 | use: O | rpt: 1)
        :param bp_dispensing_individual: Extended Composite ID Number and Name for Persons (id: BPX.21 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 21
        self.set_id_bpx = set_id_bpx
        self.bp_dispense_status = bp_dispense_status
        self.bp_status = bp_status
        self.bp_date_or_time_of_status = bp_date_or_time_of_status
        self.bc_donation_id = bc_donation_id
        self.bc_component = bc_component
        self.bc_donation_type_or_intended_use = bc_donation_type_or_intended_use
        self.cp_commercial_product = cp_commercial_product
        self.cp_manufacturer = cp_manufacturer
        self.cp_lot_number = cp_lot_number
        self.bp_blood_group = bp_blood_group
        self.bc_special_testing = bc_special_testing
        self.bp_expiration_date_or_time = bp_expiration_date_or_time
        self.bp_quantity = bp_quantity
        self.bp_amount = bp_amount
        self.bp_units = bp_units
        self.bp_unique_id = bp_unique_id
        self.bp_actual_dispensed_to_location = bp_actual_dispensed_to_location
        self.bp_actual_dispensed_to_address = bp_actual_dispensed_to_address
        self.bp_dispensed_to_receiver = bp_dispensed_to_receiver
        self.bp_dispensing_individual = bp_dispensing_individual

    @property  # get BPX.1
    def set_id_bpx(self) -> SI:
        """
        id: BPX.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.1
        """
        return self._c_data[0][0]

    @set_id_bpx.setter  # set BPX.1
    def set_id_bpx(self, si: SI):
        """
        id: BPX.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.1
        """
        self._c_data[0] = (si,)

    @property  # get BPX.2
    def bp_dispense_status(self) -> BloodProductDispenseStatus:
        """
        id: BPX.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.2
        """
        return self._c_data[1][0]

    @bp_dispense_status.setter  # set BPX.2
    def bp_dispense_status(
        self, blood_product_dispense_status: BloodProductDispenseStatus
    ):
        """
        id: BPX.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.2
        """
        self._c_data[1] = (blood_product_dispense_status,)

    @property  # get BPX.3
    def bp_status(self) -> BpObservationStatusCodesInterpretation:
        """
        id: BPX.3 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.3
        """
        return self._c_data[2][0]

    @bp_status.setter  # set BPX.3
    def bp_status(
        self,
        bp_observation_status_codes_interpretation: BpObservationStatusCodesInterpretation,
    ):
        """
        id: BPX.3 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.3
        """
        self._c_data[2] = (bp_observation_status_codes_interpretation,)

    @property  # get BPX.4
    def bp_date_or_time_of_status(self) -> TS:
        """
        id: BPX.4 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.4
        """
        return self._c_data[3][0]

    @bp_date_or_time_of_status.setter  # set BPX.4
    def bp_date_or_time_of_status(self, ts: TS):
        """
        id: BPX.4 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.4
        """
        self._c_data[3] = (ts,)

    @property  # get BPX.5
    def bc_donation_id(self) -> EI | None:
        """
        id: BPX.5 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.5
        """
        return self._c_data[4][0]

    @bc_donation_id.setter  # set BPX.5
    def bc_donation_id(self, ei: EI | None):
        """
        id: BPX.5 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.5
        """
        self._c_data[4] = (ei,)

    @property  # get BPX.6
    def bc_component(self) -> CNE | None:
        """
        id: BPX.6 | len: 250 | use: C | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.6
        """
        return self._c_data[5][0]

    @bc_component.setter  # set BPX.6
    def bc_component(self, cne: CNE | None):
        """
        id: BPX.6 | len: 250 | use: C | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.6
        """
        self._c_data[5] = (cne,)

    @property  # get BPX.7
    def bc_donation_type_or_intended_use(self) -> CNE | None:
        """
        id: BPX.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.7
        """
        return self._c_data[6][0]

    @bc_donation_type_or_intended_use.setter  # set BPX.7
    def bc_donation_type_or_intended_use(self, cne: CNE | None):
        """
        id: BPX.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.7
        """
        self._c_data[6] = (cne,)

    @property  # get BPX.8
    def cp_commercial_product(self) -> CommercialProduct | None:
        """
        id: BPX.8 | len: 250 | use: C | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.8
        """
        return self._c_data[7][0]

    @cp_commercial_product.setter  # set BPX.8
    def cp_commercial_product(self, commercial_product: CommercialProduct | None):
        """
        id: BPX.8 | len: 250 | use: C | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.8
        """
        self._c_data[7] = (commercial_product,)

    @property  # get BPX.9
    def cp_manufacturer(self) -> XON | None:
        """
        id: BPX.9 | len: 250 | use: C | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.9
        """
        return self._c_data[8][0]

    @cp_manufacturer.setter  # set BPX.9
    def cp_manufacturer(self, xon: XON | None):
        """
        id: BPX.9 | len: 250 | use: C | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.9
        """
        self._c_data[8] = (xon,)

    @property  # get BPX.10
    def cp_lot_number(self) -> EI | None:
        """
        id: BPX.10 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.10
        """
        return self._c_data[9][0]

    @cp_lot_number.setter  # set BPX.10
    def cp_lot_number(self, ei: EI | None):
        """
        id: BPX.10 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.10
        """
        self._c_data[9] = (ei,)

    @property  # get BPX.11
    def bp_blood_group(self) -> CNE | None:
        """
        id: BPX.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.11
        """
        return self._c_data[10][0]

    @bp_blood_group.setter  # set BPX.11
    def bp_blood_group(self, cne: CNE | None):
        """
        id: BPX.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.11
        """
        self._c_data[10] = (cne,)

    @property
    def bc_special_testing(self) -> tuple[CNE, ...] | tuple[None]:
        """
        id: BPX.12 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CNE, ...]: (Coded with No Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.12
        """
        return self._c_data[11]

    @bc_special_testing.setter  # set BPX.12
    def bc_special_testing(self, cne: CNE | tuple[CNE] | None):
        """
        id: BPX.12 | len: 250 | use: O | rpt: *
        ---
        param_type: CNE | tuple[CNE, ...]: (Coded with No Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.12
        """
        if isinstance(cne, tuple):
            self._c_data[11] = cne
        else:
            self._c_data[11] = (cne,)

    @property  # get BPX.13
    def bp_expiration_date_or_time(self) -> TS | None:
        """
        id: BPX.13 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.13
        """
        return self._c_data[12][0]

    @bp_expiration_date_or_time.setter  # set BPX.13
    def bp_expiration_date_or_time(self, ts: TS | None):
        """
        id: BPX.13 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.13
        """
        self._c_data[12] = (ts,)

    @property  # get BPX.14
    def bp_quantity(self) -> NM:
        """
        id: BPX.14 | len: 5 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.14
        """
        return self._c_data[13][0]

    @bp_quantity.setter  # set BPX.14
    def bp_quantity(self, nm: NM):
        """
        id: BPX.14 | len: 5 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.14
        """
        self._c_data[13] = (nm,)

    @property  # get BPX.15
    def bp_amount(self) -> NM | None:
        """
        id: BPX.15 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.15
        """
        return self._c_data[14][0]

    @bp_amount.setter  # set BPX.15
    def bp_amount(self, nm: NM | None):
        """
        id: BPX.15 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.15
        """
        self._c_data[14] = (nm,)

    @property  # get BPX.16
    def bp_units(self) -> CE | None:
        """
        id: BPX.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.16
        """
        return self._c_data[15][0]

    @bp_units.setter  # set BPX.16
    def bp_units(self, ce: CE | None):
        """
        id: BPX.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.16
        """
        self._c_data[15] = (ce,)

    @property  # get BPX.17
    def bp_unique_id(self) -> EI | None:
        """
        id: BPX.17 | len: 22 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.17
        """
        return self._c_data[16][0]

    @bp_unique_id.setter  # set BPX.17
    def bp_unique_id(self, ei: EI | None):
        """
        id: BPX.17 | len: 22 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.17
        """
        self._c_data[16] = (ei,)

    @property  # get BPX.18
    def bp_actual_dispensed_to_location(self) -> PL | None:
        """
        id: BPX.18 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.18
        """
        return self._c_data[17][0]

    @bp_actual_dispensed_to_location.setter  # set BPX.18
    def bp_actual_dispensed_to_location(self, pl: PL | None):
        """
        id: BPX.18 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.18
        """
        self._c_data[17] = (pl,)

    @property  # get BPX.19
    def bp_actual_dispensed_to_address(self) -> XAD | None:
        """
        id: BPX.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.19
        """
        return self._c_data[18][0]

    @bp_actual_dispensed_to_address.setter  # set BPX.19
    def bp_actual_dispensed_to_address(self, xad: XAD | None):
        """
        id: BPX.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: XAD: Extended Address
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.19
        """
        self._c_data[18] = (xad,)

    @property  # get BPX.20
    def bp_dispensed_to_receiver(self) -> XCN | None:
        """
        id: BPX.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.20
        """
        return self._c_data[19][0]

    @bp_dispensed_to_receiver.setter  # set BPX.20
    def bp_dispensed_to_receiver(self, xcn: XCN | None):
        """
        id: BPX.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.20
        """
        self._c_data[19] = (xcn,)

    @property  # get BPX.21
    def bp_dispensing_individual(self) -> XCN | None:
        """
        id: BPX.21 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.21
        """
        return self._c_data[20][0]

    @bp_dispensing_individual.setter  # set BPX.21
    def bp_dispensing_individual(self, xcn: XCN | None):
        """
        id: BPX.21 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BPX.21
        """
        self._c_data[20] = (xcn,)
