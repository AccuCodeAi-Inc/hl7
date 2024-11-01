from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.NTE import NTE


"""
GOAL OBSERVATION - PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, OBX
)

ppp_pcd_pathway_group_problem_group_goal_group_goal_observation_group = PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP(  # GOAL OBSERVATION - Segment group for PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP - GOAL consisting of OBX, NTE|None
    observation_or_result=obx,  # OBX(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP TEMPLATE-----
"""


class PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP"""
    _hl7_name = """GOAL OBSERVATION"""
    _hl7_description = """Segment group for PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP - GOAL consisting of OBX, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("23", "24")
    _c_components = (OBX, NTE)
    _c_name = ("OBX", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("observation_or_result", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX,  #  Required. OBX.23
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.24
    ):
        """
        None - `PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP>`_
        Segment group for PPP_PCD_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP - GOAL consisting of OBX, NTE|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 23 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 24 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_or_result = observation_or_result
        self.notes_and_comments = notes_and_comments

    @property  # get OBX.23
    def observation_or_result(self) -> OBX:
        """
        id: OBX | use: R | rpt: 1 | seq: 23
        ---
        return_type: OBX.23: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.23
    def observation_or_result(self, obx: OBX):
        """
        id: OBX | use: R | rpt: 1 | seq: 23
        ---
        param_type: OBX.23: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        param_type: NTE.24 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
