from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP import (
    PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
)
from ..segments.VAR import VAR
from ..segments.NTE import NTE
from ..segment_groups.PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP import (
    PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
)


"""
ORDER DETAIL - PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, VAR
)
from utils.hl7.v2_5_1.segment_groups import (
    PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
)

ppr_pc1_problem_group_order_group_order_detail_group = PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for PPR_PC1_PROBLEM_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None
    order_detail_segment=ppr_pc1_problem_group_order_group_order_detail_group_order_detail_segment_group,  # PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    order_observation=None,  # PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for PPR_PC1_PROBLEM_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("None", "29", "30", "None")
    _c_components = (PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP, NTE, VAR, PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP)
    _c_name = ("ORDER DETAIL SEGMENT", "NTE", "VAR", "ORDER OBSERVATION")
    _c_is_group = (True, False, False, True)
    _c_attrs = ("order_detail_segment", "notes_and_comments", "variance", "order_observation",)
    # fmt: on

    def __init__(
        self,
        order_detail_segment: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,  #  Required. OBR.23, RQD.24, RQ1.25, RXO.26, ODS.27, ODT.28
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.29
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.30
        order_observation: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.31, NTE.32, VAR.33, ...)
    ):
        """
        None - `PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for PPR_PC1_PROBLEM_GROUP_ORDER_GROUP - ORDER consisting of ORDER DETAIL SEGMENT, NTE|None, VAR|None, ORDER OBSERVATION|None

        :param order_detail_segment: Order Detail Segment segment group: [OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None] (id: ORDER DETAIL SEGMENT | seq: 23, 24, 25, 26, 27, 28 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 29 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 30 | use: O | rpt: *)
        :param order_observation: Order Observation segment group: [OBX, NTE|None, VAR|None] (id: ORDER OBSERVATION | seq: 31, 32, 33 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.order_detail_segment = order_detail_segment
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.order_observation = order_observation

    @property  # get PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
    ) -> (
        PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
    ):
        """
        id: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        return_type: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        return self._c_data[0][0]

    @order_detail_segment.setter  # set PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
        order_detail_segment: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
    ):
        """
        id: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: R | rpt: 1 | seq: None
        ---
        param_type: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        self._c_data[0] = (order_detail_segment,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        param_type: NTE.29 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 30
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 30
        ---
        param_type: VAR.30 | tuple[VAR, ...]: (Variance, ...)
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
            PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        """
        return self._c_data[3]

    @order_observation.setter  # set ORDER OBSERVATION
    def order_observation(
        self,
        order_observation: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: ORDER OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP.None | tuple[PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPR_PC1_PROBLEM_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_OBSERVATION_GROUP
        """
        if isinstance(order_observation, tuple):
            self._c_data[3] = order_observation
        else:
            self._c_data[3] = (order_observation,)
