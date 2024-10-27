from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ORC import ORC
from ..segment_groups.PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP,
)


"""
ORDER - PGL_PC6_GOAL_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC6_GOAL_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PGL_PC6_GOAL_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
)

pgl_pc6_goal_group_order_group = PGL_PC6_GOAL_GROUP_ORDER_GROUP(  # ORDER - Segment group for PGL_PC6_GOAL_GROUP - GOAL consisting of ORC, ORDER DETAIL|None
    common_order=orc,  # ORC(...)  # Required.
    order_detail=None,  # PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC6_GOAL_GROUP_ORDER_GROUP TEMPLATE-----
"""


class PGL_PC6_GOAL_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PGL_PC6_GOAL_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for PGL_PC6_GOAL_GROUP - GOAL consisting of ORC, ORDER DETAIL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC6_GOAL_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("22", "None")
    _c_components = (ORC, PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP)
    _c_name = ("ORC", "ORDER DETAIL")
    _c_is_group = (False, True)
    _c_attrs = ("common_order", "order_detail",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.22
        order_detail: PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None = None,  #  NTE.29, VAR.30
    ):
        """
        None - `PGL_PC6_GOAL_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC6_GOAL_GROUP_ORDER_GROUP>`_
        Segment group for PGL_PC6_GOAL_GROUP - GOAL consisting of ORC, ORDER DETAIL|None

        :param common_order: Common Order (id: ORC | seq: 22 | use: R | rpt: 1)
        :param order_detail: Order Detail segment group: [ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None] (id: ORDER DETAIL | seq: None, 29, 30, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.common_order = common_order
        self.order_detail = order_detail

    @property  # get ORC.22
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 22
        ---
        return_type: ORC.22: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.22
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 22
        ---
        param_type: ORC.22: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self) -> PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[1][0]

    @order_detail.setter  # set PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self, order_detail: PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | None
    ):
        """
        id: PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC6_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[1] = (order_detail,)
