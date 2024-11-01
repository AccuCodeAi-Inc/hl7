from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segment_groups.PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
)
from ..segments.VAR import VAR
from ..segment_groups.PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
)


"""
ORDER DETAIL - PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, VAR
)
from utils.hl7.v2_5_1.segment_groups import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
)

ppt_pcl_patient_group_pathway_group_goal_group_order_group_order_detail_group = PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None
    order_detail_segment=ppt_pcl_patient_group_pathway_group_goal_group_order_group_order_detail_group_order_detail_segment_group,  # PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    order_observation=None,  # PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("None", "36", "37", "None")
    _c_components = (PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, NTE, VAR, PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP)
    _c_name = ("ORDER DETAIL SEGMENT", "NTE", "VAR", "ORDER OBSERVATION")
    _c_is_group = (True, False, False, True)
    _c_attrs = ("order_detail_segment", "notes_and_comments", "variance", "order_observation",)
    # fmt: on

    def __init__(
        self,
        order_detail_segment: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,  #  Required. OBR.30, RQD.31, RQ1.32, RXO.33, ODS.34, ODT.35
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.36
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.37
        order_observation: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.38, NTE.39, VAR.40, ...)
    ):
        """
        None - `PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None

        :param order_detail_segment: Order Detail Segment segment group: [OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None] (id: ORDER DETAIL SEGMENT | seq: 30, 31, 32, 33, 34, 35 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 36 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 37 | use: O | rpt: *)
        :param order_observation: Order Observation segment group: [OBX, NTE|None, VAR|None] (id: ORDER OBSERVATION | seq: 38, 39, 40 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.order_detail_segment = order_detail_segment
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.order_observation = order_observation

    @property  # get PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
    ) -> PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP:
        """
        id: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        return_type: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        return self._c_data[0][0]

    @order_detail_segment.setter  # set PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
        order_detail_segment: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
    ):
        """
        id: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        param_type: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        self._c_data[0] = (order_detail_segment,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 36
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 36
        ---
        param_type: NTE.36 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 37
        ---
        param_type: VAR.37 | tuple[VAR, ...]: (Variance, ...)
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
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        """
        return self._c_data[3]

    @order_observation.setter  # set ORDER OBSERVATION
    def order_observation(
        self,
        order_observation: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: ORDER OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP.None | tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        """
        if isinstance(order_observation, tuple):
            self._c_data[3] = order_observation
        else:
            self._c_data[3] = (order_observation,)
