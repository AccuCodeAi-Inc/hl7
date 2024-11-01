from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP import (
    RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - RRE_O12_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRE_O12_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRE_O12_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP, RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

rre_o12_response_group_order_group = RRE_O12_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for RRE_O12_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ENCODING|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    encoding=None,  # RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRE_O12_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RRE_O12_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRE_O12_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RRE_O12_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ENCODING|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRE_O12_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("8", "None", "None")
    _c_components = (ORC, RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP)
    _c_name = ("ORC", "TIMING", "ENCODING")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "timing", "encoding",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        timing: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        encoding: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.11, NTE.12, RXR.15, RXC.16
    ):
        """
        None - `RRE_O12_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRE_O12_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for RRE_O12_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ENCODING|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param encoding: Encoding segment group: [RXE, NTE|None, TIMING ENCODED, RXR, RXC|None] (id: ENCODING | seq: 11, 12, None, 15, 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.timing = timing
        self.encoding = encoding

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
    ) -> tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[2][0]

    @encoding.setter  # set RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(
        self, encoding: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | None
    ):
        """
        id: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[2] = (encoding,)
