from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.VAR import VAR
from ..segment_groups.PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP import (
    PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
)
from ..segments.NTE import NTE
from ..segment_groups.PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP import (
    PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
)


"""
ORDER DETAIL - PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    VAR, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
)

ppg_pcg_pathway_group_goal_group_order_group_order_detail_group = PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None
    order_detail_segment=ppg_pcg_pathway_group_goal_group_order_group_order_detail_group_order_detail_segment_group,  # PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    order_observation=None,  # PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("None", "32", "33", "None")
    _c_components = (PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, NTE, VAR, PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP)
    _c_name = ("ORDER DETAIL SEGMENT", "NTE", "VAR", "ORDER OBSERVATION")
    _c_is_group = (True, False, False, True)
    _c_attrs = ("order_detail_segment", "notes_and_comments", "variance", "order_observation",)
    # fmt: on

    def __init__(
        self,
        order_detail_segment: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,  #  Required. OBR.26, RQD.27, RQ1.28, RXO.29, ODS.30, ODT.31
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.32
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.33
        order_observation: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.34, NTE.35, VAR.36, ...)
    ):
        """
        None - `PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None

        :param order_detail_segment: Order Detail Segment segment group: [OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None] (id: ORDER DETAIL SEGMENT | seq: 26, 27, 28, 29, 30, 31 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 32 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 33 | use: O | rpt: *)
        :param order_observation: Order Observation segment group: [OBX, NTE|None, VAR|None] (id: ORDER OBSERVATION | seq: 34, 35, 36 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.order_detail_segment = order_detail_segment
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.order_observation = order_observation

    @property  # get PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
    ) -> PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP:
        """
        id: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        return_type: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        return self._c_data[0][0]

    @order_detail_segment.setter  # set PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
        order_detail_segment: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
    ):
        """
        id: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        param_type: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        self._c_data[0] = (order_detail_segment,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 32
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 32
        ---
        param_type: NTE.32 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get VAR
    def variance(self) -> tuple[VAR, ...] | tuple[None]:
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 33
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 33
        ---
        param_type: VAR.33 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[2] = var
        else:
            self._c_data[2] = (var,)

    @property  # get ORDER OBSERVATION
    def order_observation(
        self,
    ) -> (
        tuple[
            PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        """
        return self._c_data[3]

    @order_observation.setter  # set ORDER OBSERVATION
    def order_observation(
        self,
        order_observation: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: ORDER OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP.None | tuple[PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        """
        if isinstance(order_observation, tuple):
            self._c_data[3] = order_observation
        else:
            self._c_data[3] = (order_observation,)
