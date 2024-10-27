from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ORC import ORC
from ..segment_groups.RGV_O15_ORDER_GROUP_ENCODING_GROUP import (
    RGV_O15_ORDER_GROUP_ENCODING_GROUP,
)
from ..segment_groups.RGV_O15_ORDER_GROUP_GIVE_GROUP import (
    RGV_O15_ORDER_GROUP_GIVE_GROUP,
)
from ..segment_groups.RGV_O15_ORDER_GROUP_TIMING_GROUP import (
    RGV_O15_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP,
)


"""
ORDER - RGV_O15_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RGV_O15_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP, RGV_O15_ORDER_GROUP_TIMING_GROUP, RGV_O15_ORDER_GROUP_ENCODING_GROUP, RGV_O15_ORDER_GROUP_GIVE_GROUP
)

rgv_o15_order_group = RGV_O15_ORDER_GROUP(  # ORDER - Segment group for RGV_O15 - Pharmacy/Treatment Give consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, GIVE
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RGV_O15_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    encoding=None,  # RGV_O15_ORDER_GROUP_ENCODING_GROUP(...) 
    give=rgv_o15_order_group_give_group,  # RGV_O15_ORDER_GROUP_GIVE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_ORDER_GROUP TEMPLATE-----
"""


class RGV_O15_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RGV_O15_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RGV_O15 - Pharmacy/Treatment Give consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, GIVE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("9", "None", "None", "None", "None")
    _c_components = (ORC, RGV_O15_ORDER_GROUP_TIMING_GROUP, RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP, RGV_O15_ORDER_GROUP_ENCODING_GROUP, RGV_O15_ORDER_GROUP_GIVE_GROUP)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL", "ENCODING", "GIVE")
    _c_is_group = (False, True, True, True, True)
    _c_attrs = ("common_order", "timing", "order_detail", "encoding", "give",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.9
        give: RGV_O15_ORDER_GROUP_GIVE_GROUP
        | tuple[
            RGV_O15_ORDER_GROUP_GIVE_GROUP, ...
        ],  #  Required. (RXG.22, RXR.25, RXC.26, ...)
        timing: RGV_O15_ORDER_GROUP_TIMING_GROUP
        | tuple[RGV_O15_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.10, TQ2.11, ...)
        order_detail: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP | None = None,  #  RXO.12
        encoding: RGV_O15_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.17, RXR.20, RXC.21
    ):
        """
        None - `RGV_O15_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_ORDER_GROUP>`_
        Segment group for RGV_O15 - Pharmacy/Treatment Give consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, GIVE

        :param common_order: Common Order (id: ORC | seq: 9 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 10, 11 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, ORDER DETAIL SUPPLEMENT|None] (id: ORDER DETAIL | seq: 12, None | use: O | rpt: 1)
        :param encoding: Encoding segment group: [RXE, TIMING ENCODED, RXR, RXC|None] (id: ENCODING | seq: 17, None, 20, 21 | use: O | rpt: 1)
        :param give: Give segment group: [RXG, TIMING GIVE, RXR, RXC|None, OBSERVATION] (id: GIVE | seq: 22, None, 25, 26, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail
        self.encoding = encoding
        self.give = give

    @property  # get ORC.9
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 9
        ---
        return_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.9
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 9
        ---
        param_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[RGV_O15_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RGV_O15_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RGV_O15_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RGV_O15_ORDER_GROUP_TIMING_GROUP
        | tuple[RGV_O15_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_TIMING_GROUP.None | tuple[RGV_O15_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self) -> RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self, order_detail: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP | None):
        """
        id: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)

    @property  # get RGV_O15_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RGV_O15_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RGV_O15_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RGV_O15_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[3][0]

    @encoding.setter  # set RGV_O15_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self, encoding: RGV_O15_ORDER_GROUP_ENCODING_GROUP | None):
        """
        id: RGV_O15_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[3] = (encoding,)

    @property  # get GIVE
    def give(self) -> tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP, ...]:
        """
        id: RGV_O15_ORDER_GROUP_GIVE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_GIVE_GROUP
        """
        return self._c_data[4]

    @give.setter  # set GIVE
    def give(
        self,
        give: RGV_O15_ORDER_GROUP_GIVE_GROUP
        | tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP, ...],
    ):
        """
        id: GIVE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_GIVE_GROUP.None | tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_GIVE_GROUP
        """
        if isinstance(give, tuple):
            self._c_data[4] = give
        else:
            self._c_data[4] = (give,)
