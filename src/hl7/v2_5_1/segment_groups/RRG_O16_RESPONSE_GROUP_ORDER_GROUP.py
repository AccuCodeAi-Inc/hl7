from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP import (
    RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - RRG_O16_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRG_O16_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRG_O16_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP
)

rrg_o16_response_group_order_group = RRG_O16_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for RRG_O16_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, GIVE|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    give=None,  # RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRG_O16_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RRG_O16_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRG_O16_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RRG_O16_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, GIVE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRG_O16_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("8", "None", "None")
    _c_components = (ORC, RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP)
    _c_name = ("ORC", "TIMING", "GIVE")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "timing", "give",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        timing: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        give: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP
        | None = None,  #  RXG.11, RXR.14, RXC.15
    ):
        """
        None - `RRG_O16_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRG_O16_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for RRG_O16_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, GIVE|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param give: Give segment group: [RXG, TIMING GIVE, RXR, RXC|None] (id: GIVE | seq: 11, None, 14, 15 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.timing = timing
        self.give = give

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
    ) -> tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP.None
    def give(self) -> RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP | None:
        """
        id: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP
        """
        return self._c_data[2][0]

    @give.setter  # set RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP.None
    def give(self, give: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP | None):
        """
        id: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRG_O16_RESPONSE_GROUP_ORDER_GROUP_GIVE_GROUP
        """
        self._c_data[2] = (give,)
