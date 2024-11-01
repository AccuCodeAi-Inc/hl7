from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXG import RXG
from ..segments.RXC import RXC


"""
GIVE - RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP
from utils.hl7.v2_5_1.segments import (
    RXG, RXC, RXR
)

rsp_z86_query_response_group_common_order_group_give_group = RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP(  # GIVE - Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXG, RXR, RXC|None
    pharmacy_or_treatment_give=rxg,  # RXG(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP TEMPLATE-----
"""


class RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP"""
    _hl7_name = """GIVE"""
    _hl7_description = """Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXG, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("25", "26", "27")
    _c_components = (RXG, RXR, RXC)
    _c_name = ("RXG", "RXR", "RXC")
    _c_is_group = (False, False, False)
    _c_attrs = ("pharmacy_or_treatment_give", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_give: RXG,  #  Required. RXG.25
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.26
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.27
    ):
        """
        None - `RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_GIVE_GROUP>`_
        Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXG, RXR, RXC|None

        :param pharmacy_or_treatment_give: Pharmacy/Treatment Give (id: RXG | seq: 25 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 26 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 27 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.pharmacy_or_treatment_give = pharmacy_or_treatment_give
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXG.25
    def pharmacy_or_treatment_give(self) -> RXG:
        """
        id: RXG | use: R | rpt: 1 | seq: 25
        ---
        return_type: RXG.25: Pharmacy/Treatment Give
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_give.setter  # set RXG.25
    def pharmacy_or_treatment_give(self, rxg: RXG):
        """
        id: RXG | use: R | rpt: 1 | seq: 25
        ---
        param_type: RXG.25: Pharmacy/Treatment Give
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        self._c_data[0] = (rxg,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 26
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 26
        ---
        param_type: RXR.26 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
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
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[2]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        param_type: RXC.27 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[2] = rxc
        else:
            self._c_data[2] = (rxc,)
