from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXC import RXC
from ..segments.RXO import RXO


"""
ORDER DETAIL - RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    RXO, RXC, RXR
)

rsp_z86_query_response_group_common_order_group_order_detail_group = RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXO, RXR, RXC|None
    pharmacy_or_treatment_order=rxo,  # RXO(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXO, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("14", "15", "16")
    _c_components = (RXO, RXR, RXC)
    _c_name = ("RXO", "RXR", "RXC")
    _c_is_group = (False, False, False)
    _c_attrs = ("pharmacy_or_treatment_order", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_order: RXO,  #  Required. RXO.14
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.15
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.16
    ):
        """
        None - `RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXO, RXR, RXC|None

        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 14 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 15 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 16 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXO.14
    def pharmacy_or_treatment_order(self) -> RXO:
        """
        id: RXO | use: R | rpt: 1 | seq: 14
        ---
        return_type: RXO.14: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_order.setter  # set RXO.14
    def pharmacy_or_treatment_order(self, rxo: RXO):
        """
        id: RXO | use: R | rpt: 1 | seq: 14
        ---
        param_type: RXO.14: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[0] = (rxo,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 15
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 15
        ---
        param_type: RXR.15 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
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
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[2]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: RXC.16 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[2] = rxc
        else:
            self._c_data[2] = (rxc,)
