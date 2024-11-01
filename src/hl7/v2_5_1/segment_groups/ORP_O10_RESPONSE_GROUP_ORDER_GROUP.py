from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP,
)
from ..segment_groups.ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - ORP_O10_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORP_O10_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORP_O10_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
)

orp_o10_response_group_order_group = ORP_O10_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORP_O10_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORP_O10_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORP_O10_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORP_O10_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORP_O10_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORP_O10_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("8", "None", "None")
    _c_components = (ORC, ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "timing", "order_detail",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        timing: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        order_detail: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None = None,  #  RXO.11, NTE.12, RXR.13
    ):
        """
        None - `ORP_O10_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORP_O10_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for ORP_O10_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, NTE|None, RXR, COMPONENT|None] (id: ORDER DETAIL | seq: 11, 12, 13, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail

    @property  # get ORC.8
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        return_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.8
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        param_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self,
    ) -> ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self, order_detail: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | None
    ):
        """
        id: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)
