from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXE import RXE
from ..segments.RXC import RXC


"""
ENCODING - RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXE, RXC
)

rdr_rdr_definition_group_order_group_encoding_group = RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP(  # ENCODING - Segment group for RDR_RDR_DEFINITION_GROUP_ORDER_GROUP - ORDER consisting of RXE, RXR, RXC|None
    pharmacy_or_treatment_encoded_order=rxe,  # RXE(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP TEMPLATE-----
"""


class RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP"""
    _hl7_name = """ENCODING"""
    _hl7_description = """Segment group for RDR_RDR_DEFINITION_GROUP_ORDER_GROUP - ORDER consisting of RXE, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("10", "11", "12")
    _c_components = (RXE, RXR, RXC)
    _c_name = ("RXE", "RXR", "RXC")
    _c_is_group = (False, False, False)
    _c_attrs = ("pharmacy_or_treatment_encoded_order", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_encoded_order: RXE,  #  Required. RXE.10
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.11
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.12
    ):
        """
        None - `RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP>`_
        Segment group for RDR_RDR_DEFINITION_GROUP_ORDER_GROUP - ORDER consisting of RXE, RXR, RXC|None

        :param pharmacy_or_treatment_encoded_order: Pharmacy/Treatment Encoded Order (id: RXE | seq: 10 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 11 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.pharmacy_or_treatment_encoded_order = pharmacy_or_treatment_encoded_order
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXE.10
    def pharmacy_or_treatment_encoded_order(self) -> RXE:
        """
        id: RXE | use: R | rpt: 1 | seq: 10
        ---
        return_type: RXE.10: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_encoded_order.setter  # set RXE.10
    def pharmacy_or_treatment_encoded_order(self, rxe: RXE):
        """
        id: RXE | use: R | rpt: 1 | seq: 10
        ---
        param_type: RXE.10: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        self._c_data[0] = (rxe,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 11
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 11
        ---
        param_type: RXR.11 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[1] = rxr
        else:
            self._c_data[1] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[2]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: RXC.12 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[2] = rxc
        else:
            self._c_data[2] = (rxc,)
