from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.CNE import CNE
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.XCN import XCN
from ..data_types.EI import EI
from ..data_types.XON import XON
from ..tables.BloodProductTransfusionOrDispositionStatus import (
    BloodProductTransfusionOrDispositionStatus,
)
from ..tables.CommercialProduct import CommercialProduct
from ..tables.TransfusionAdverseReaction import TransfusionAdverseReaction
from ..tables.BpObservationStatusCodesInterpretation import (
    BpObservationStatusCodesInterpretation,
)
from ..tables.TransfusionInterruptedReason import TransfusionInterruptedReason


"""
Blood Product Transfusion/Disposition - BTX
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BTX TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BTX,
    TS, CNE, ID, NM, CWE, SI, CE, XCN, EI, XON
)

btx = BTX(  #  - 
    set_id_btx=si,  # SI(...)  # Required.
    bc_donation_id=None,  # EI(...) 
    bc_component=None,  # CNE(...) 
    bc_blood_group=None,  # CNE(...) 
    cp_commercial_product=None,  # CWE(...) 
    cp_manufacturer=None,  # XON(...) 
    cp_lot_number=None,  # EI(...) 
    bp_quantity=nm,  # NM(...)  # Required.
    bp_amount=None,  # NM(...) 
    bp_units=None,  # CE(...) 
    bp_transfusion_or_disposition_status=cwe,  # CWE(...)  # Required.
    bp_message_status=id,  # ID(...)  # Required.
    bp_date_or_time_of_status=ts,  # TS(...)  # Required.
    bp_administrator=None,  # XCN(...) 
    bp_verifier=None,  # XCN(...) 
    bp_transfusion_start_date_or_time_of_status=None,  # TS(...) 
    bp_transfusion_end_date_or_time_of_status=None,  # TS(...) 
    bp_adverse_reaction_type=None,  # CWE(...) 
    bp_transfusion_interrupted_reason=None,  # CWE(...) 
)

-----END SEGMENT::BTX TEMPLATE-----
"""


class BTX(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BTX"""
    _hl7_name = """Blood Product Transfusion/Disposition"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTX"
    _c_length = (4, 22, 250, 250, 250, 250, 22, 5, 5, 250, 250, 1, 26, 250, 250, 26, 26, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1,)
    _c_usage = ("R", "C", "C", "C", "C", "C", "C", "R", "O", "O", "R", "R", "R", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, EI, CNE, CNE, CWE, XON, EI, NM, NM, CE, CWE, ID, TS, XCN, XCN, TS, TS, CWE, CWE,)
    _c_aliases = ("BTX.1", "BTX.2", "BTX.3", "BTX.4", "BTX.5", "BTX.6", "BTX.7", "BTX.8", "BTX.9", "BTX.10", "BTX.11", "BTX.12", "BTX.13", "BTX.14", "BTX.15", "BTX.16", "BTX.17", "BTX.18", "BTX.19",)
    _c_names = ("Set ID - BTX", "BC Donation ID", "BC Component", "BC Blood Group", "CP Commercial Product", "CP Manufacturer", "CP Lot Number", "BP Quantity", "BP Amount", "BP Units", "BP Transfusion/Disposition Status", "BP Message Status", "BP Date/Time of Status", "BP Administrator", "BP Verifier", "BP Transfusion Start Date/Time of Status", "BP Transfusion End Date/Time of Status", "BP Adverse Reaction Type", "BP Transfusion Interrupted Reason",)
    _c_attrs = ("set_id_btx", "bc_donation_id", "bc_component", "bc_blood_group", "cp_commercial_product", "cp_manufacturer", "cp_lot_number", "bp_quantity", "bp_amount", "bp_units", "bp_transfusion_or_disposition_status", "bp_message_status", "bp_date_or_time_of_status", "bp_administrator", "bp_verifier", "bp_transfusion_start_date_or_time_of_status", "bp_transfusion_end_date_or_time_of_status", "bp_adverse_reaction_type", "bp_transfusion_interrupted_reason",)
    # fmt: on

    def __init__(
        self,
        set_id_btx: SI | tuple[SI],  # BTX.1
        bp_quantity: NM | tuple[NM],  # BTX.8
        bp_transfusion_or_disposition_status: BloodProductTransfusionOrDispositionStatus
        | CWE
        | tuple[BloodProductTransfusionOrDispositionStatus | CWE],  # BTX.11
        bp_message_status: BpObservationStatusCodesInterpretation
        | ID
        | tuple[BpObservationStatusCodesInterpretation | ID],  # BTX.12
        bp_date_or_time_of_status: TS | tuple[TS],  # BTX.13
        bc_donation_id: EI | tuple[EI] | None = None,  # BTX.2
        bc_component: CNE | tuple[CNE] | None = None,  # BTX.3
        bc_blood_group: CNE | tuple[CNE] | None = None,  # BTX.4
        cp_commercial_product: CommercialProduct
        | CWE
        | tuple[CommercialProduct | CWE]
        | None = None,  # BTX.5
        cp_manufacturer: XON | tuple[XON] | None = None,  # BTX.6
        cp_lot_number: EI | tuple[EI] | None = None,  # BTX.7
        bp_amount: NM | tuple[NM] | None = None,  # BTX.9
        bp_units: CE | tuple[CE] | None = None,  # BTX.10
        bp_administrator: XCN | tuple[XCN] | None = None,  # BTX.14
        bp_verifier: XCN | tuple[XCN] | None = None,  # BTX.15
        bp_transfusion_start_date_or_time_of_status: TS
        | tuple[TS]
        | None = None,  # BTX.16
        bp_transfusion_end_date_or_time_of_status: TS
        | tuple[TS]
        | None = None,  # BTX.17
        bp_adverse_reaction_type: TransfusionAdverseReaction
        | CWE
        | tuple[TransfusionAdverseReaction | CWE]
        | None = None,  # BTX.18
        bp_transfusion_interrupted_reason: TransfusionInterruptedReason
        | CWE
        | tuple[TransfusionInterruptedReason | CWE]
        | None = None,  # BTX.19
    ):
        """
        Blood Product Transfusion/Disposition - `BTX <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTX>`_


        :param set_id_btx: Sequence ID (id: BTX.1 | len: 4 | use: R | rpt: 1)
        :param bc_donation_id: Entity Identifier (id: BTX.2 | len: 22 | use: C | rpt: 1)
        :param bc_component: Coded with No Exceptions (id: BTX.3 | len: 250 | use: C | rpt: 1)
        :param bc_blood_group: Coded with No Exceptions (id: BTX.4 | len: 250 | use: C | rpt: 1)
        :param cp_commercial_product: Coded with Exceptions (id: BTX.5 | len: 250 | use: C | rpt: 1)
        :param cp_manufacturer: Extended Composite Name and Identification Number for Organizations (id: BTX.6 | len: 250 | use: C | rpt: 1)
        :param cp_lot_number: Entity Identifier (id: BTX.7 | len: 22 | use: C | rpt: 1)
        :param bp_quantity: Numeric (id: BTX.8 | len: 5 | use: R | rpt: 1)
        :param bp_amount: Numeric (id: BTX.9 | len: 5 | use: O | rpt: 1)
        :param bp_units: Coded Element (id: BTX.10 | len: 250 | use: O | rpt: 1)
        :param bp_transfusion_or_disposition_status: Coded with Exceptions (id: BTX.11 | len: 250 | use: R | rpt: 1)
        :param bp_message_status: Coded values for HL7 tables (id: BTX.12 | len: 1 | use: R | rpt: 1)
        :param bp_date_or_time_of_status: Time Stamp (id: BTX.13 | len: 26 | use: R | rpt: 1)
        :param bp_administrator: Extended Composite ID Number and Name for Persons (id: BTX.14 | len: 250 | use: O | rpt: 1)
        :param bp_verifier: Extended Composite ID Number and Name for Persons (id: BTX.15 | len: 250 | use: O | rpt: 1)
        :param bp_transfusion_start_date_or_time_of_status: Time Stamp (id: BTX.16 | len: 26 | use: O | rpt: 1)
        :param bp_transfusion_end_date_or_time_of_status: Time Stamp (id: BTX.17 | len: 26 | use: O | rpt: 1)
        :param bp_adverse_reaction_type: Coded with Exceptions (id: BTX.18 | len: 250 | use: O | rpt: *)
        :param bp_transfusion_interrupted_reason: Coded with Exceptions (id: BTX.19 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 19
        self.set_id_btx = set_id_btx
        self.bc_donation_id = bc_donation_id
        self.bc_component = bc_component
        self.bc_blood_group = bc_blood_group
        self.cp_commercial_product = cp_commercial_product
        self.cp_manufacturer = cp_manufacturer
        self.cp_lot_number = cp_lot_number
        self.bp_quantity = bp_quantity
        self.bp_amount = bp_amount
        self.bp_units = bp_units
        self.bp_transfusion_or_disposition_status = bp_transfusion_or_disposition_status
        self.bp_message_status = bp_message_status
        self.bp_date_or_time_of_status = bp_date_or_time_of_status
        self.bp_administrator = bp_administrator
        self.bp_verifier = bp_verifier
        self.bp_transfusion_start_date_or_time_of_status = (
            bp_transfusion_start_date_or_time_of_status
        )
        self.bp_transfusion_end_date_or_time_of_status = (
            bp_transfusion_end_date_or_time_of_status
        )
        self.bp_adverse_reaction_type = bp_adverse_reaction_type
        self.bp_transfusion_interrupted_reason = bp_transfusion_interrupted_reason

    @property  # get BTX.1
    def set_id_btx(self) -> SI:
        """
        id: BTX.1 | len: 4 | use: R | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.1
        """
        return self._c_data[0][0]

    @set_id_btx.setter  # set BTX.1
    def set_id_btx(self, si: SI):
        """
        id: BTX.1 | len: 4 | use: R | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.1
        """
        self._c_data[0] = (si,)

    @property  # get BTX.2
    def bc_donation_id(self) -> EI | None:
        """
        id: BTX.2 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.2
        """
        return self._c_data[1][0]

    @bc_donation_id.setter  # set BTX.2
    def bc_donation_id(self, ei: EI | None):
        """
        id: BTX.2 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.2
        """
        self._c_data[1] = (ei,)

    @property  # get BTX.3
    def bc_component(self) -> CNE | None:
        """
        id: BTX.3 | len: 250 | use: C | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.3
        """
        return self._c_data[2][0]

    @bc_component.setter  # set BTX.3
    def bc_component(self, cne: CNE | None):
        """
        id: BTX.3 | len: 250 | use: C | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.3
        """
        self._c_data[2] = (cne,)

    @property  # get BTX.4
    def bc_blood_group(self) -> CNE | None:
        """
        id: BTX.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.4
        """
        return self._c_data[3][0]

    @bc_blood_group.setter  # set BTX.4
    def bc_blood_group(self, cne: CNE | None):
        """
        id: BTX.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.4
        """
        self._c_data[3] = (cne,)

    @property  # get BTX.5
    def cp_commercial_product(self) -> CommercialProduct | None:
        """
        id: BTX.5 | len: 250 | use: C | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.5
        """
        return self._c_data[4][0]

    @cp_commercial_product.setter  # set BTX.5
    def cp_commercial_product(self, commercial_product: CommercialProduct | None):
        """
        id: BTX.5 | len: 250 | use: C | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.5
        """
        self._c_data[4] = (commercial_product,)

    @property  # get BTX.6
    def cp_manufacturer(self) -> XON | None:
        """
        id: BTX.6 | len: 250 | use: C | rpt: 1
        ---
        return_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.6
        """
        return self._c_data[5][0]

    @cp_manufacturer.setter  # set BTX.6
    def cp_manufacturer(self, xon: XON | None):
        """
        id: BTX.6 | len: 250 | use: C | rpt: 1
        ---
        param_type: XON: Extended Composite Name and Identification Number for Organizations
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.6
        """
        self._c_data[5] = (xon,)

    @property  # get BTX.7
    def cp_lot_number(self) -> EI | None:
        """
        id: BTX.7 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.7
        """
        return self._c_data[6][0]

    @cp_lot_number.setter  # set BTX.7
    def cp_lot_number(self, ei: EI | None):
        """
        id: BTX.7 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.7
        """
        self._c_data[6] = (ei,)

    @property  # get BTX.8
    def bp_quantity(self) -> NM:
        """
        id: BTX.8 | len: 5 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.8
        """
        return self._c_data[7][0]

    @bp_quantity.setter  # set BTX.8
    def bp_quantity(self, nm: NM):
        """
        id: BTX.8 | len: 5 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.8
        """
        self._c_data[7] = (nm,)

    @property  # get BTX.9
    def bp_amount(self) -> NM | None:
        """
        id: BTX.9 | len: 5 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.9
        """
        return self._c_data[8][0]

    @bp_amount.setter  # set BTX.9
    def bp_amount(self, nm: NM | None):
        """
        id: BTX.9 | len: 5 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.9
        """
        self._c_data[8] = (nm,)

    @property  # get BTX.10
    def bp_units(self) -> CE | None:
        """
        id: BTX.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.10
        """
        return self._c_data[9][0]

    @bp_units.setter  # set BTX.10
    def bp_units(self, ce: CE | None):
        """
        id: BTX.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.10
        """
        self._c_data[9] = (ce,)

    @property  # get BTX.11
    def bp_transfusion_or_disposition_status(
        self,
    ) -> BloodProductTransfusionOrDispositionStatus:
        """
        id: BTX.11 | len: 250 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.11
        """
        return self._c_data[10][0]

    @bp_transfusion_or_disposition_status.setter  # set BTX.11
    def bp_transfusion_or_disposition_status(
        self,
        blood_product_transfusion_or_disposition_status: BloodProductTransfusionOrDispositionStatus,
    ):
        """
        id: BTX.11 | len: 250 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.11
        """
        self._c_data[10] = (blood_product_transfusion_or_disposition_status,)

    @property  # get BTX.12
    def bp_message_status(self) -> BpObservationStatusCodesInterpretation:
        """
        id: BTX.12 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.12
        """
        return self._c_data[11][0]

    @bp_message_status.setter  # set BTX.12
    def bp_message_status(
        self,
        bp_observation_status_codes_interpretation: BpObservationStatusCodesInterpretation,
    ):
        """
        id: BTX.12 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.12
        """
        self._c_data[11] = (bp_observation_status_codes_interpretation,)

    @property  # get BTX.13
    def bp_date_or_time_of_status(self) -> TS:
        """
        id: BTX.13 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.13
        """
        return self._c_data[12][0]

    @bp_date_or_time_of_status.setter  # set BTX.13
    def bp_date_or_time_of_status(self, ts: TS):
        """
        id: BTX.13 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.13
        """
        self._c_data[12] = (ts,)

    @property  # get BTX.14
    def bp_administrator(self) -> XCN | None:
        """
        id: BTX.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.14
        """
        return self._c_data[13][0]

    @bp_administrator.setter  # set BTX.14
    def bp_administrator(self, xcn: XCN | None):
        """
        id: BTX.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.14
        """
        self._c_data[13] = (xcn,)

    @property  # get BTX.15
    def bp_verifier(self) -> XCN | None:
        """
        id: BTX.15 | len: 250 | use: O | rpt: 1
        ---
        return_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.15
        """
        return self._c_data[14][0]

    @bp_verifier.setter  # set BTX.15
    def bp_verifier(self, xcn: XCN | None):
        """
        id: BTX.15 | len: 250 | use: O | rpt: 1
        ---
        param_type: XCN: Extended Composite ID Number and Name for Persons
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.15
        """
        self._c_data[14] = (xcn,)

    @property  # get BTX.16
    def bp_transfusion_start_date_or_time_of_status(self) -> TS | None:
        """
        id: BTX.16 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.16
        """
        return self._c_data[15][0]

    @bp_transfusion_start_date_or_time_of_status.setter  # set BTX.16
    def bp_transfusion_start_date_or_time_of_status(self, ts: TS | None):
        """
        id: BTX.16 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.16
        """
        self._c_data[15] = (ts,)

    @property  # get BTX.17
    def bp_transfusion_end_date_or_time_of_status(self) -> TS | None:
        """
        id: BTX.17 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.17
        """
        return self._c_data[16][0]

    @bp_transfusion_end_date_or_time_of_status.setter  # set BTX.17
    def bp_transfusion_end_date_or_time_of_status(self, ts: TS | None):
        """
        id: BTX.17 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.17
        """
        self._c_data[16] = (ts,)

    @property
    def bp_adverse_reaction_type(
        self,
    ) -> tuple[TransfusionAdverseReaction, ...] | tuple[None]:
        """
        id: BTX.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.18
        """
        return self._c_data[17]

    @bp_adverse_reaction_type.setter  # set BTX.18
    def bp_adverse_reaction_type(
        self,
        transfusion_adverse_reaction: TransfusionAdverseReaction
        | tuple[TransfusionAdverseReaction]
        | None,
    ):
        """
        id: BTX.18 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.18
        """
        if isinstance(transfusion_adverse_reaction, tuple):
            self._c_data[17] = transfusion_adverse_reaction
        else:
            self._c_data[17] = (transfusion_adverse_reaction,)

    @property  # get BTX.19
    def bp_transfusion_interrupted_reason(self) -> TransfusionInterruptedReason | None:
        """
        id: BTX.19 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.19
        """
        return self._c_data[18][0]

    @bp_transfusion_interrupted_reason.setter  # set BTX.19
    def bp_transfusion_interrupted_reason(
        self, transfusion_interrupted_reason: TransfusionInterruptedReason | None
    ):
        """
        id: BTX.19 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BTX.19
        """
        self._c_data[18] = (transfusion_interrupted_reason,)
