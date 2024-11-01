from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RQD import RQD
from ..segments.NTE import NTE
from ..segment_groups.ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1


"""
ORDER - ORN_O08_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORN_O08_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORN_O08_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, ORC, RQ1, RQD
)
from utils.hl7.v2_5_1.segment_groups import (
    ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

orn_o08_response_group_order_group = ORN_O08_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORN_O08_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, RQD, RQ1|None, NTE|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    requisition_detail=rqd,  # RQD(...)  # Required.
    requisition_detail_1=None,  # RQ1(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORN_O08_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORN_O08_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORN_O08_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORN_O08_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, RQD, RQ1|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORN_O08_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O")
    _c_aliases = ("8", "None", "11", "12", "13")
    _c_components = (ORC, ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RQD, RQ1, NTE)
    _c_name = ("ORC", "TIMING", "RQD", "RQ1", "NTE")
    _c_is_group = (False, True, False, False, False)
    _c_attrs = ("common_order", "timing", "requisition_detail", "requisition_detail_1", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        requisition_detail: RQD,  #  Required. RQD.11
        timing: ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        requisition_detail_1: RQ1 | None = None,  #  RQ1.12
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
    ):
        """
        None - `ORN_O08_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORN_O08_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for ORN_O08_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, RQD, RQ1|None, NTE|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param requisition_detail: Requisition Detail (id: RQD | seq: 11 | use: R | rpt: 1)
        :param requisition_detail_1: Requisition Detail-1 (id: RQ1 | seq: 12 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.requisition_detail = requisition_detail
        self.requisition_detail_1 = requisition_detail_1
        self.notes_and_comments = notes_and_comments

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
    ) -> tuple[ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORN_O08_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RQD.11
    def requisition_detail(self) -> RQD:
        """
        id: RQD | use: R | rpt: 1 | seq: 11
        ---
        return_type: RQD.11: Requisition Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD
        """
        return self._c_data[2][0]

    @requisition_detail.setter  # set RQD.11
    def requisition_detail(self, rqd: RQD):
        """
        id: RQD | use: R | rpt: 1 | seq: 11
        ---
        param_type: RQD.11: Requisition Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD
        """
        self._c_data[2] = (rqd,)

    @property  # get RQ1.12
    def requisition_detail_1(self) -> RQ1 | None:
        """
        id: RQ1 | use: O | rpt: 1 | seq: 12
        ---
        return_type: RQ1.12: Requisition Detail-1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1
        """
        return self._c_data[3][0]

    @requisition_detail_1.setter  # set RQ1.12
    def requisition_detail_1(self, rq1: RQ1 | None):
        """
        id: RQ1 | use: O | rpt: 1 | seq: 12
        ---
        param_type: RQ1.12: Requisition Detail-1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1
        """
        self._c_data[3] = (rq1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[4]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: NTE.13 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[4] = nte
        else:
            self._c_data[4] = (nte,)
