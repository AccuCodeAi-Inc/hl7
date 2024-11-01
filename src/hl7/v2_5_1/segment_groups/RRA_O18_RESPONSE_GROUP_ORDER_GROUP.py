from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ORC import ORC
from ..segment_groups.RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP import (
    RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP,
)


"""
ORDER - RRA_O18_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRA_O18_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRA_O18_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP
)

rra_o18_response_group_order_group = RRA_O18_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for RRA_O18_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ADMINISTRATION|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    administration=None,  # RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRA_O18_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RRA_O18_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRA_O18_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RRA_O18_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ADMINISTRATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRA_O18_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("8", "None", "None")
    _c_components = (ORC, RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP)
    _c_name = ("ORC", "TIMING", "ADMINISTRATION")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "timing", "administration",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        timing: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        administration: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP
        | None = None,  #  RXA.11, RXR.12
    ):
        """
        None - `RRA_O18_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRA_O18_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for RRA_O18_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ADMINISTRATION|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param administration: Administration segment group: [RXA, RXR] (id: ADMINISTRATION | seq: 11, 12 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.timing = timing
        self.administration = administration

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
    ) -> tuple[RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRA_O18_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP.None
    def administration(
        self,
    ) -> RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP | None:
        """
        id: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP
        """
        return self._c_data[2][0]

    @administration.setter  # set RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP.None
    def administration(
        self,
        admin_istration: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP | None,
    ):
        """
        id: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP
        """
        self._c_data[2] = (admin_istration,)
