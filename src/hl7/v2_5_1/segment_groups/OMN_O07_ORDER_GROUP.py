from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OMN_O07_ORDER_GROUP_TIMING_GROUP import (
    OMN_O07_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.RQD import RQD
from ..segment_groups.OMN_O07_ORDER_GROUP_OBSERVATION_GROUP import (
    OMN_O07_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.BLG import BLG
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RQ1 import RQ1


"""
ORDER - OMN_O07_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMN_O07_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMN_O07_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RQD, NTE, BLG, ORC, RQ1
)
from utils.hl7.v2_5_1.segment_groups import (
    OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, OMN_O07_ORDER_GROUP_TIMING_GROUP
)

omn_o07_order_group = OMN_O07_ORDER_GROUP(  # ORDER - Segment group for OMN_O07 - Non-Stock Requisition Order consisting of ORC, TIMING|None, RQD, RQ1|None, NTE|None, OBSERVATION|None, BLG|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # OMN_O07_ORDER_GROUP_TIMING_GROUP(...) 
    requisition_detail=rqd,  # RQD(...)  # Required.
    requisition_detail_1=None,  # RQ1(...) 
    notes_and_comments=None,  # NTE(...) 
    observation=None,  # OMN_O07_ORDER_GROUP_OBSERVATION_GROUP(...) 
    billing=None,  # BLG(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMN_O07_ORDER_GROUP TEMPLATE-----
"""


class OMN_O07_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMN_O07_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OMN_O07 - Non-Stock Requisition Order consisting of ORC, TIMING|None, RQD, RQ1|None, NTE|None, OBSERVATION|None, BLG|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMN_O07_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O")
    _c_aliases = ("14", "None", "17", "18", "19", "None", "22")
    _c_components = (ORC, OMN_O07_ORDER_GROUP_TIMING_GROUP, RQD, RQ1, NTE, OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, BLG)
    _c_name = ("ORC", "TIMING", "RQD", "RQ1", "NTE", "OBSERVATION", "BLG")
    _c_is_group = (False, True, False, False, False, True, False)
    _c_attrs = ("common_order", "timing", "requisition_detail", "requisition_detail_1", "notes_and_comments", "observation", "billing",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        requisition_detail: RQD,  #  Required. RQD.17
        timing: OMN_O07_ORDER_GROUP_TIMING_GROUP
        | tuple[OMN_O07_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        requisition_detail_1: RQ1 | None = None,  #  RQ1.18
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
        observation: OMN_O07_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.20, NTE.21, ...)
        billing: BLG | None = None,  #  BLG.22
    ):
        """
        None - `OMN_O07_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMN_O07_ORDER_GROUP>`_
        Segment group for OMN_O07 - Non-Stock Requisition Order consisting of ORC, TIMING|None, RQD, RQ1|None, NTE|None, OBSERVATION|None, BLG|None

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param requisition_detail: Requisition Detail (id: RQD | seq: 17 | use: R | rpt: 1)
        :param requisition_detail_1: Requisition Detail-1 (id: RQ1 | seq: 18 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 20, 21 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 22 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.common_order = common_order
        self.timing = timing
        self.requisition_detail = requisition_detail
        self.requisition_detail_1 = requisition_detail_1
        self.notes_and_comments = notes_and_comments
        self.observation = observation
        self.billing = billing

    @property  # get ORC.14
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        return_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.14
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        param_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[OMN_O07_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: OMN_O07_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMN_O07_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMN_O07_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: OMN_O07_ORDER_GROUP_TIMING_GROUP
        | tuple[OMN_O07_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMN_O07_ORDER_GROUP_TIMING_GROUP.None | tuple[OMN_O07_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMN_O07_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RQD.17
    def requisition_detail(self) -> RQD:
        """
        id: RQD | use: R | rpt: 1 | seq: 17
        ---
        return_type: RQD.17: Requisition Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD
        """
        return self._c_data[2][0]

    @requisition_detail.setter  # set RQD.17
    def requisition_detail(self, rqd: RQD):
        """
        id: RQD | use: R | rpt: 1 | seq: 17
        ---
        param_type: RQD.17: Requisition Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD
        """
        self._c_data[2] = (rqd,)

    @property  # get RQ1.18
    def requisition_detail_1(self) -> RQ1 | None:
        """
        id: RQ1 | use: O | rpt: 1 | seq: 18
        ---
        return_type: RQ1.18: Requisition Detail-1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1
        """
        return self._c_data[3][0]

    @requisition_detail_1.setter  # set RQ1.18
    def requisition_detail_1(self, rq1: RQ1 | None):
        """
        id: RQ1 | use: O | rpt: 1 | seq: 18
        ---
        param_type: RQ1.18: Requisition Detail-1
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1
        """
        self._c_data[3] = (rq1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[4]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: NTE.19 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[4] = nte
        else:
            self._c_data[4] = (nte,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: OMN_O07_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMN_O07_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OMN_O07_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMN_O07_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[OMN_O07_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMN_O07_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[5] = observation
        else:
            self._c_data[5] = (observation,)

    @property  # get BLG.22
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 22
        ---
        return_type: BLG.22: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[6][0]

    @billing.setter  # set BLG.22
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 22
        ---
        param_type: BLG.22: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[6] = (blg,)
