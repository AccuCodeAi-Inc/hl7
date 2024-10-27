from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.CWE import CWE
from ..data_types.TQ import TQ
from ..data_types.XAD import XAD
from ..data_types.XTN import XTN
from ..data_types.CE import CE
from ..data_types.CNE import CNE
from ..data_types.EI import EI
from ..data_types.EIP import EIP
from ..data_types.XCN import XCN
from ..data_types.PL import PL
from ..data_types.XON import XON
from ..tables.OrderType import OrderType
from ..tables.AdvancedBeneficiaryNoticeOverrideReason import (
    AdvancedBeneficiaryNoticeOverrideReason,
)
from ..tables.AdvancedBeneficiaryNoticeCode import AdvancedBeneficiaryNoticeCode
from ..tables.ResponseFlag import ResponseFlag
from ..tables.ConfidentialityCode import ConfidentialityCode
from ..tables.OrderControlCodes import OrderControlCodes
from ..tables.OrderStatus import OrderStatus
from ..tables.AuthorizationMode import AuthorizationMode


"""
Common Order - ORC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ORC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ORC,
    ID, TS, CWE, TQ, XAD, XTN, CE, CNE, EI, EIP, XCN, PL, XON
)

orc = ORC(  #  - The Common Order segment (ORC) is used to transmit fields that are common to all orders (all types of services that are requested)
    order_control=id,  # ID(...)  # Required.
    placer_order_number=None,  # EI(...) 
    filler_order_number=None,  # EI(...) 
    placer_group_number=None,  # EI(...) 
    order_status=None,  # ID(...) 
    response_flag=None,  # ID(...) 
    quantity_or_timing=None,  # TQ(...) 
    parent_order=None,  # EIP(...) 
    date_or_time_of_transaction=None,  # TS(...) 
    entered_by=None,  # XCN(...) 
    verified_by=None,  # XCN(...) 
    ordering_provider=None,  # XCN(...) 
    enterers_location=None,  # PL(...) 
    call_back_phone_number=None,  # XTN(...) 
    order_effective_date_or_time=None,  # TS(...) 
    order_control_code_reason=None,  # CE(...) 
    entering_organization=None,  # CE(...) 
    entering_device=None,  # CE(...) 
    action_by=None,  # XCN(...) 
    advanced_beneficiary_notice_code=None,  # CE(...) 
    ordering_facility_name=None,  # XON(...) 
    ordering_facility_address=None,  # XAD(...) 
    ordering_facility_phone_number=None,  # XTN(...) 
    ordering_provider_address=None,  # XAD(...) 
    order_status_modifier=None,  # CWE(...) 
    advanced_beneficiary_notice_override_reason=None,  # CWE(...) 
    fillers_expected_availability_date_or_time=None,  # TS(...) 
    confidentiality_code=None,  # CWE(...) 
    order_type=None,  # CWE(...) 
    enterer_authorization_mode=None,  # CNE(...) 
    parent_universal_service_identifier=None,  # CWE(...) 
)

-----END SEGMENT::ORC TEMPLATE-----
"""


class ORC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ORC"""
    _hl7_name = """Common Order"""
    _hl7_description = """The Common Order segment (ORC) is used to transmit fields that are common to all orders (all types of services that are requested)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC"
    _c_length = (2, 22, 22, 22, 2, 1, 200, 200, 26, 250, 250, 250, 80, 250, 26, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 60, 26, 250, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 65535, 1, 1, 65535, 65535, 65535, 1, 2, 1, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "C", "C", "O", "O", "O", "B", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C", "O", "O", "O", "O", "O",)
    _c_components = (ID, EI, EI, EI, ID, ID, TQ, EIP, TS, XCN, XCN, XCN, PL, XTN, TS, CE, CE, CE, XCN, CE, XON, XAD, XTN, XAD, CWE, CWE, TS, CWE, CWE, CNE, CWE,)
    _c_aliases = ("ORC.1", "ORC.2", "ORC.3", "ORC.4", "ORC.5", "ORC.6", "ORC.7", "ORC.8", "ORC.9", "ORC.10", "ORC.11", "ORC.12", "ORC.13", "ORC.14", "ORC.15", "ORC.16", "ORC.17", "ORC.18", "ORC.19", "ORC.20", "ORC.21", "ORC.22", "ORC.23", "ORC.24", "ORC.25", "ORC.26", "ORC.27", "ORC.28", "ORC.29", "ORC.30", "ORC.31",)
    _c_names = ("Order Control", "Placer Order Number", "Filler Order Number", "Placer Group Number", "Order Status", "Response Flag", "Quantity/Timing", "Parent Order", "Date/Time of Transaction", "Entered By", "Verified By", "Ordering Provider", "Enterer's Location", "Call Back Phone Number", "Order Effective Date/Time", "Order Control Code Reason", "Entering Organization", "Entering Device", "Action By", "Advanced Beneficiary Notice Code", "Ordering Facility Name", "Ordering Facility Address", "Ordering Facility Phone Number", "Ordering Provider Address", "Order Status Modifier", "Advanced Beneficiary Notice Override Reason", "Filler's Expected Availability Date/Time", "Confidentiality Code", "Order Type", "Enterer Authorization Mode", "Parent Universal Service Identifier",)
    _c_attrs = ("order_control", "placer_order_number", "filler_order_number", "placer_group_number", "order_status", "response_flag", "quantity_or_timing", "parent_order", "date_or_time_of_transaction", "entered_by", "verified_by", "ordering_provider", "enterers_location", "call_back_phone_number", "order_effective_date_or_time", "order_control_code_reason", "entering_organization", "entering_device", "action_by", "advanced_beneficiary_notice_code", "ordering_facility_name", "ordering_facility_address", "ordering_facility_phone_number", "ordering_provider_address", "order_status_modifier", "advanced_beneficiary_notice_override_reason", "fillers_expected_availability_date_or_time", "confidentiality_code", "order_type", "enterer_authorization_mode", "parent_universal_service_identifier",)
    # fmt: on

    def __init__(
        self,
        order_control: OrderControlCodes | ID,  # ORC.1
        placer_order_number: EI | None = None,  # ORC.2
        filler_order_number: EI | None = None,  # ORC.3
        placer_group_number: EI | None = None,  # ORC.4
        order_status: OrderStatus | ID | None = None,  # ORC.5
        response_flag: ResponseFlag | ID | None = None,  # ORC.6
        quantity_or_timing: TQ | None = None,  # ORC.7
        parent_order: EIP | None = None,  # ORC.8
        date_or_time_of_transaction: TS | None = None,  # ORC.9
        entered_by: XCN | None = None,  # ORC.10
        verified_by: XCN | None = None,  # ORC.11
        ordering_provider: XCN | None = None,  # ORC.12
        enterers_location: PL | None = None,  # ORC.13
        call_back_phone_number: XTN | None = None,  # ORC.14
        order_effective_date_or_time: TS | None = None,  # ORC.15
        order_control_code_reason: CE | None = None,  # ORC.16
        entering_organization: CE | None = None,  # ORC.17
        entering_device: CE | None = None,  # ORC.18
        action_by: XCN | None = None,  # ORC.19
        advanced_beneficiary_notice_code: AdvancedBeneficiaryNoticeCode
        | CE
        | None = None,  # ORC.20
        ordering_facility_name: XON | None = None,  # ORC.21
        ordering_facility_address: XAD | None = None,  # ORC.22
        ordering_facility_phone_number: XTN | None = None,  # ORC.23
        ordering_provider_address: XAD | None = None,  # ORC.24
        order_status_modifier: CWE | None = None,  # ORC.25
        advanced_beneficiary_notice_override_reason: AdvancedBeneficiaryNoticeOverrideReason
        | CWE
        | None = None,  # ORC.26
        fillers_expected_availability_date_or_time: TS | None = None,  # ORC.27
        confidentiality_code: ConfidentialityCode | CWE | None = None,  # ORC.28
        order_type: OrderType | CWE | None = None,  # ORC.29
        enterer_authorization_mode: AuthorizationMode | CNE | None = None,  # ORC.30
        parent_universal_service_identifier: CWE | None = None,  # ORC.31
    ):
        """
                Common Order - `ORC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC>`_
                The Common Order segment (ORC) is used to transmit fields that are common to all orders (all types of services that are requested). The ORC segment is required in the Order (ORM) message. ORC is mandatory in Order Acknowledgment (ORR) messages if an order detail segment is present, but is not required otherwise.

        If details are needed for a particular type of order segment (e.g., Pharmacy, Dietary), the ORC must precede any order detail segment (e.g., RXO, ODS).  In some cases, the ORC may be as simple as the string ORC|OK|<placer order number>|<filler order number>|<cr>.

        If details are not needed for the order, the order detail segment may be omitted.  For example, to place an order on hold, one would transmit an ORC with the following fields completed: ORC-1-order control with a value of HD, ORC-2-placer order number, and ORC-3-filler order number.

                :param order_control: Coded values for HL7 tables (id: ORC.1 | len: 2 | use: R | rpt: 1)
                :param placer_order_number: Entity Identifier (id: ORC.2 | len: 22 | use: C | rpt: 1)
                :param filler_order_number: Entity Identifier (id: ORC.3 | len: 22 | use: C | rpt: 1)
                :param placer_group_number: Entity Identifier (id: ORC.4 | len: 22 | use: O | rpt: 1)
                :param order_status: Coded values for HL7 tables (id: ORC.5 | len: 2 | use: O | rpt: 1)
                :param response_flag: Coded values for HL7 tables (id: ORC.6 | len: 1 | use: O | rpt: 1)
                :param quantity_or_timing: Timing Quantity (id: ORC.7 | len: 200 | use: B | rpt: *)
                :param parent_order: Entity Identifier Pair (id: ORC.8 | len: 200 | use: O | rpt: 1)
                :param date_or_time_of_transaction: Time Stamp (id: ORC.9 | len: 26 | use: O | rpt: 1)
                :param entered_by: Extended Composite ID Number and Name for Persons (id: ORC.10 | len: 250 | use: O | rpt: *)
                :param verified_by: Extended Composite ID Number and Name for Persons (id: ORC.11 | len: 250 | use: O | rpt: *)
                :param ordering_provider: Extended Composite ID Number and Name for Persons (id: ORC.12 | len: 250 | use: O | rpt: *)
                :param enterers_location: Person Location (id: ORC.13 | len: 80 | use: O | rpt: 1)
                :param call_back_phone_number: Extended Telecommunication Number (id: ORC.14 | len: 250 | use: O | rpt: 2)
                :param order_effective_date_or_time: Time Stamp (id: ORC.15 | len: 26 | use: O | rpt: 1)
                :param order_control_code_reason: Coded Element (id: ORC.16 | len: 250 | use: O | rpt: 1)
                :param entering_organization: Coded Element (id: ORC.17 | len: 250 | use: O | rpt: 1)
                :param entering_device: Coded Element (id: ORC.18 | len: 250 | use: O | rpt: 1)
                :param action_by: Extended Composite ID Number and Name for Persons (id: ORC.19 | len: 250 | use: O | rpt: *)
                :param advanced_beneficiary_notice_code: Coded Element (id: ORC.20 | len: 250 | use: O | rpt: 1)
                :param ordering_facility_name: Extended Composite Name and Identification Number for Organizations (id: ORC.21 | len: 250 | use: O | rpt: *)
                :param ordering_facility_address: Extended Address (id: ORC.22 | len: 250 | use: O | rpt: *)
                :param ordering_facility_phone_number: Extended Telecommunication Number (id: ORC.23 | len: 250 | use: O | rpt: *)
                :param ordering_provider_address: Extended Address (id: ORC.24 | len: 250 | use: O | rpt: *)
                :param order_status_modifier: Coded with Exceptions (id: ORC.25 | len: 250 | use: O | rpt: 1)
                :param advanced_beneficiary_notice_override_reason: Coded with Exceptions (id: ORC.26 | len: 60 | use: C | rpt: 1)
                :param fillers_expected_availability_date_or_time: Time Stamp (id: ORC.27 | len: 26 | use: O | rpt: 1)
                :param confidentiality_code: Coded with Exceptions (id: ORC.28 | len: 250 | use: O | rpt: 1)
                :param order_type: Coded with Exceptions (id: ORC.29 | len: 250 | use: O | rpt: 1)
                :param enterer_authorization_mode: Coded with No Exceptions (id: ORC.30 | len: 250 | use: O | rpt: 1)
                :param parent_universal_service_identifier: Coded with Exceptions (id: ORC.31 | len: 250 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 31
        self.order_control = order_control
        self.placer_order_number = placer_order_number
        self.filler_order_number = filler_order_number
        self.placer_group_number = placer_group_number
        self.order_status = order_status
        self.response_flag = response_flag
        self.quantity_or_timing = quantity_or_timing
        self.parent_order = parent_order
        self.date_or_time_of_transaction = date_or_time_of_transaction
        self.entered_by = entered_by
        self.verified_by = verified_by
        self.ordering_provider = ordering_provider
        self.enterers_location = enterers_location
        self.call_back_phone_number = call_back_phone_number
        self.order_effective_date_or_time = order_effective_date_or_time
        self.order_control_code_reason = order_control_code_reason
        self.entering_organization = entering_organization
        self.entering_device = entering_device
        self.action_by = action_by
        self.advanced_beneficiary_notice_code = advanced_beneficiary_notice_code
        self.ordering_facility_name = ordering_facility_name
        self.ordering_facility_address = ordering_facility_address
        self.ordering_facility_phone_number = ordering_facility_phone_number
        self.ordering_provider_address = ordering_provider_address
        self.order_status_modifier = order_status_modifier
        self.advanced_beneficiary_notice_override_reason = (
            advanced_beneficiary_notice_override_reason
        )
        self.fillers_expected_availability_date_or_time = (
            fillers_expected_availability_date_or_time
        )
        self.confidentiality_code = confidentiality_code
        self.order_type = order_type
        self.enterer_authorization_mode = enterer_authorization_mode
        self.parent_universal_service_identifier = parent_universal_service_identifier

    @property  # get ORC.1
    def order_control(self) -> OrderControlCodes:
        """
        id: ORC.1 | len: 2 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.1
        """
        return self._c_data[0][0]

    @order_control.setter  # set ORC.1
    def order_control(self, order_control_codes: OrderControlCodes):
        """
        id: ORC.1 | len: 2 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.1
        """
        self._c_data[0] = (order_control_codes,)

    @property  # get ORC.2
    def placer_order_number(self) -> EI | None:
        """
        id: ORC.2 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.2
        """
        return self._c_data[1][0]

    @placer_order_number.setter  # set ORC.2
    def placer_order_number(self, ei: EI | None):
        """
        id: ORC.2 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.2
        """
        self._c_data[1] = (ei,)

    @property  # get ORC.3
    def filler_order_number(self) -> EI | None:
        """
        id: ORC.3 | len: 22 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.3
        """
        return self._c_data[2][0]

    @filler_order_number.setter  # set ORC.3
    def filler_order_number(self, ei: EI | None):
        """
        id: ORC.3 | len: 22 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.3
        """
        self._c_data[2] = (ei,)

    @property  # get ORC.4
    def placer_group_number(self) -> EI | None:
        """
        id: ORC.4 | len: 22 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.4
        """
        return self._c_data[3][0]

    @placer_group_number.setter  # set ORC.4
    def placer_group_number(self, ei: EI | None):
        """
        id: ORC.4 | len: 22 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.4
        """
        self._c_data[3] = (ei,)

    @property  # get ORC.5
    def order_status(self) -> OrderStatus | None:
        """
        id: ORC.5 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.5
        """
        return self._c_data[4][0]

    @order_status.setter  # set ORC.5
    def order_status(self, order_status: OrderStatus | None):
        """
        id: ORC.5 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.5
        """
        self._c_data[4] = (order_status,)

    @property  # get ORC.6
    def response_flag(self) -> ResponseFlag | None:
        """
        id: ORC.6 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.6
        """
        return self._c_data[5][0]

    @response_flag.setter  # set ORC.6
    def response_flag(self, response_flag: ResponseFlag | None):
        """
        id: ORC.6 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.6
        """
        self._c_data[5] = (response_flag,)

    @property
    def quantity_or_timing(self) -> tuple[TQ, ...] | tuple[None]:
        """
        id: ORC.7 | len: 200 | use: B | rpt: *
        ---
        return_type: tuple[TQ, ...]: (Timing Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.7
        """
        return self._c_data[6]

    @quantity_or_timing.setter  # set ORC.7
    def quantity_or_timing(self, tq: TQ | tuple[TQ] | None):
        """
        id: ORC.7 | len: 200 | use: B | rpt: *
        ---
        param_type: TQ | tuple[TQ, ...]: (Timing Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.7
        """
        if isinstance(tq, tuple):
            self._c_data[6] = tq
        else:
            self._c_data[6] = (tq,)

    @property  # get ORC.8
    def parent_order(self) -> EIP | None:
        """
        id: ORC.8 | len: 200 | use: O | rpt: 1
        ---
        return_type: EIP: Entity Identifier Pair
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.8
        """
        return self._c_data[7][0]

    @parent_order.setter  # set ORC.8
    def parent_order(self, eip: EIP | None):
        """
        id: ORC.8 | len: 200 | use: O | rpt: 1
        ---
        param_type: EIP: Entity Identifier Pair
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.8
        """
        self._c_data[7] = (eip,)

    @property  # get ORC.9
    def date_or_time_of_transaction(self) -> TS | None:
        """
        id: ORC.9 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.9
        """
        return self._c_data[8][0]

    @date_or_time_of_transaction.setter  # set ORC.9
    def date_or_time_of_transaction(self, ts: TS | None):
        """
        id: ORC.9 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.9
        """
        self._c_data[8] = (ts,)

    @property
    def entered_by(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: ORC.10 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.10
        """
        return self._c_data[9]

    @entered_by.setter  # set ORC.10
    def entered_by(self, xcn: XCN | tuple[XCN] | None):
        """
        id: ORC.10 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.10
        """
        if isinstance(xcn, tuple):
            self._c_data[9] = xcn
        else:
            self._c_data[9] = (xcn,)

    @property
    def verified_by(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: ORC.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.11
        """
        return self._c_data[10]

    @verified_by.setter  # set ORC.11
    def verified_by(self, xcn: XCN | tuple[XCN] | None):
        """
        id: ORC.11 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.11
        """
        if isinstance(xcn, tuple):
            self._c_data[10] = xcn
        else:
            self._c_data[10] = (xcn,)

    @property
    def ordering_provider(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: ORC.12 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.12
        """
        return self._c_data[11]

    @ordering_provider.setter  # set ORC.12
    def ordering_provider(self, xcn: XCN | tuple[XCN] | None):
        """
        id: ORC.12 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.12
        """
        if isinstance(xcn, tuple):
            self._c_data[11] = xcn
        else:
            self._c_data[11] = (xcn,)

    @property  # get ORC.13
    def enterers_location(self) -> PL | None:
        """
        id: ORC.13 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.13
        """
        return self._c_data[12][0]

    @enterers_location.setter  # set ORC.13
    def enterers_location(self, pl: PL | None):
        """
        id: ORC.13 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.13
        """
        self._c_data[12] = (pl,)

    @property
    def call_back_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: ORC.14 | len: 250 | use: O | rpt: 2
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.14
        """
        return self._c_data[13]

    @call_back_phone_number.setter  # set ORC.14
    def call_back_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: ORC.14 | len: 250 | use: O | rpt: 2
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.14
        """
        if isinstance(xtn, tuple):
            self._c_data[13] = xtn
        else:
            self._c_data[13] = (xtn,)

    @property  # get ORC.15
    def order_effective_date_or_time(self) -> TS | None:
        """
        id: ORC.15 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.15
        """
        return self._c_data[14][0]

    @order_effective_date_or_time.setter  # set ORC.15
    def order_effective_date_or_time(self, ts: TS | None):
        """
        id: ORC.15 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.15
        """
        self._c_data[14] = (ts,)

    @property  # get ORC.16
    def order_control_code_reason(self) -> CE | None:
        """
        id: ORC.16 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.16
        """
        return self._c_data[15][0]

    @order_control_code_reason.setter  # set ORC.16
    def order_control_code_reason(self, ce: CE | None):
        """
        id: ORC.16 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.16
        """
        self._c_data[15] = (ce,)

    @property  # get ORC.17
    def entering_organization(self) -> CE | None:
        """
        id: ORC.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.17
        """
        return self._c_data[16][0]

    @entering_organization.setter  # set ORC.17
    def entering_organization(self, ce: CE | None):
        """
        id: ORC.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.17
        """
        self._c_data[16] = (ce,)

    @property  # get ORC.18
    def entering_device(self) -> CE | None:
        """
        id: ORC.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.18
        """
        return self._c_data[17][0]

    @entering_device.setter  # set ORC.18
    def entering_device(self, ce: CE | None):
        """
        id: ORC.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.18
        """
        self._c_data[17] = (ce,)

    @property
    def action_by(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: ORC.19 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.19
        """
        return self._c_data[18]

    @action_by.setter  # set ORC.19
    def action_by(self, xcn: XCN | tuple[XCN] | None):
        """
        id: ORC.19 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.19
        """
        if isinstance(xcn, tuple):
            self._c_data[18] = xcn
        else:
            self._c_data[18] = (xcn,)

    @property  # get ORC.20
    def advanced_beneficiary_notice_code(self) -> AdvancedBeneficiaryNoticeCode | None:
        """
        id: ORC.20 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.20
        """
        return self._c_data[19][0]

    @advanced_beneficiary_notice_code.setter  # set ORC.20
    def advanced_beneficiary_notice_code(
        self, advanced_beneficiary_notice_code: AdvancedBeneficiaryNoticeCode | None
    ):
        """
        id: ORC.20 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.20
        """
        self._c_data[19] = (advanced_beneficiary_notice_code,)

    @property
    def ordering_facility_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: ORC.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.21
        """
        return self._c_data[20]

    @ordering_facility_name.setter  # set ORC.21
    def ordering_facility_name(self, xon: XON | tuple[XON] | None):
        """
        id: ORC.21 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.21
        """
        if isinstance(xon, tuple):
            self._c_data[20] = xon
        else:
            self._c_data[20] = (xon,)

    @property
    def ordering_facility_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: ORC.22 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.22
        """
        return self._c_data[21]

    @ordering_facility_address.setter  # set ORC.22
    def ordering_facility_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: ORC.22 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.22
        """
        if isinstance(xad, tuple):
            self._c_data[21] = xad
        else:
            self._c_data[21] = (xad,)

    @property
    def ordering_facility_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: ORC.23 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.23
        """
        return self._c_data[22]

    @ordering_facility_phone_number.setter  # set ORC.23
    def ordering_facility_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: ORC.23 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.23
        """
        if isinstance(xtn, tuple):
            self._c_data[22] = xtn
        else:
            self._c_data[22] = (xtn,)

    @property
    def ordering_provider_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: ORC.24 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.24
        """
        return self._c_data[23]

    @ordering_provider_address.setter  # set ORC.24
    def ordering_provider_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: ORC.24 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.24
        """
        if isinstance(xad, tuple):
            self._c_data[23] = xad
        else:
            self._c_data[23] = (xad,)

    @property  # get ORC.25
    def order_status_modifier(self) -> CWE | None:
        """
        id: ORC.25 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.25
        """
        return self._c_data[24][0]

    @order_status_modifier.setter  # set ORC.25
    def order_status_modifier(self, cwe: CWE | None):
        """
        id: ORC.25 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.25
        """
        self._c_data[24] = (cwe,)

    @property  # get ORC.26
    def advanced_beneficiary_notice_override_reason(
        self,
    ) -> AdvancedBeneficiaryNoticeOverrideReason | None:
        """
        id: ORC.26 | len: 60 | use: C | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.26
        """
        return self._c_data[25][0]

    @advanced_beneficiary_notice_override_reason.setter  # set ORC.26
    def advanced_beneficiary_notice_override_reason(
        self,
        advanced_beneficiary_notice_override_reason: AdvancedBeneficiaryNoticeOverrideReason
        | None,
    ):
        """
        id: ORC.26 | len: 60 | use: C | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.26
        """
        self._c_data[25] = (advanced_beneficiary_notice_override_reason,)

    @property  # get ORC.27
    def fillers_expected_availability_date_or_time(self) -> TS | None:
        """
        id: ORC.27 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.27
        """
        return self._c_data[26][0]

    @fillers_expected_availability_date_or_time.setter  # set ORC.27
    def fillers_expected_availability_date_or_time(self, ts: TS | None):
        """
        id: ORC.27 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.27
        """
        self._c_data[26] = (ts,)

    @property  # get ORC.28
    def confidentiality_code(self) -> ConfidentialityCode | None:
        """
        id: ORC.28 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.28
        """
        return self._c_data[27][0]

    @confidentiality_code.setter  # set ORC.28
    def confidentiality_code(self, confidentiality_code: ConfidentialityCode | None):
        """
        id: ORC.28 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.28
        """
        self._c_data[27] = (confidentiality_code,)

    @property  # get ORC.29
    def order_type(self) -> OrderType | None:
        """
        id: ORC.29 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.29
        """
        return self._c_data[28][0]

    @order_type.setter  # set ORC.29
    def order_type(self, order_type: OrderType | None):
        """
        id: ORC.29 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.29
        """
        self._c_data[28] = (order_type,)

    @property  # get ORC.30
    def enterer_authorization_mode(self) -> AuthorizationMode | None:
        """
        id: ORC.30 | len: 250 | use: O | rpt: 1
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.30
        """
        return self._c_data[29][0]

    @enterer_authorization_mode.setter  # set ORC.30
    def enterer_authorization_mode(self, authorization_mode: AuthorizationMode | None):
        """
        id: ORC.30 | len: 250 | use: O | rpt: 1
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.30
        """
        self._c_data[29] = (authorization_mode,)

    @property  # get ORC.31
    def parent_universal_service_identifier(self) -> CWE | None:
        """
        id: ORC.31 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.31
        """
        return self._c_data[30][0]

    @parent_universal_service_identifier.setter  # set ORC.31
    def parent_universal_service_identifier(self, cwe: CWE | None):
        """
        id: ORC.31 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ORC.31
        """
        self._c_data[30] = (cwe,)
