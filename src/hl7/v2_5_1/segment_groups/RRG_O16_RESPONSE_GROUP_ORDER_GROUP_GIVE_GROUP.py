from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP import (
    RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP,
)
from ..segments.RXG import RXG
from ..segments.RXR import RXR
from ..segments.RXC import RXC


"""
GIVE - RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXG, RXC
)
from utils.hl7.v2_5_1.segment_groups import (
    RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
)

rrg_o16_response_group_order_group_give_group = RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP(  # GIVE - Segment group for RRG_O16_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXG, TIMING GIVE, RXR, RXC|None
    pharmacy_or_treatment_give=rxg,  # RXG(...)  # Required.
    timing_give=rrg_o16_response_group_order_group_give_group_timing_give_group,  # RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP TEMPLATE-----
"""


class RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP"""
    _hl7_name = """GIVE"""
    _hl7_description = """Segment group for RRG_O16_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXG, TIMING GIVE, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "R", "R", "O")
    _c_aliases = ("11", "None", "14", "15")
    _c_components = (RXG, RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, RXR, RXC)
    _c_name = ("RXG", "TIMING GIVE", "RXR", "RXC")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("pharmacy_or_treatment_give", "timing_give", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_give: RXG,  #  Required. RXG.11
        timing_give: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        | tuple[
            RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...
        ],  #  Required. (TQ1.12, TQ2.13, ...)
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.14
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.15
    ):
        """
        None - `RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP>`_
        Segment group for RRG_O16_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXG, TIMING GIVE, RXR, RXC|None

        :param pharmacy_or_treatment_give: Pharmacy/Treatment Give (id: RXG | seq: 11 | use: R | rpt: 1)
        :param timing_give: Timing Give segment group: [TQ1, TQ2|None] (id: TIMING GIVE | seq: 12, 13 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 14 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pharmacy_or_treatment_give = pharmacy_or_treatment_give
        self.timing_give = timing_give
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXG.11
    def pharmacy_or_treatment_give(self) -> RXG:
        """
        id: RXG | use: R | rpt: 1 | seq: 11
        ---
        return_type: RXG.11: Pharmacy/Treatment Give
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_give.setter  # set RXG.11
    def pharmacy_or_treatment_give(self, rxg: RXG):
        """
        id: RXG | use: R | rpt: 1 | seq: 11
        ---
        param_type: RXG.11: Pharmacy/Treatment Give
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        self._c_data[0] = (rxg,)

    @property  # get TIMING GIVE
    def timing_give(
        self,
    ) -> tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...]:
        """
        id: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        """
        return self._c_data[1]

    @timing_give.setter  # set TIMING GIVE
    def timing_give(
        self,
        timing_give: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        | tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...],
    ):
        """
        id: TIMING GIVE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP.None | tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        """
        if isinstance(timing_give, tuple):
            self._c_data[1] = timing_give
        else:
            self._c_data[1] = (timing_give,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        param_type: RXR.14 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[3]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: RXC.15 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[3] = rxc
        else:
            self._c_data[3] = (rxc,)
