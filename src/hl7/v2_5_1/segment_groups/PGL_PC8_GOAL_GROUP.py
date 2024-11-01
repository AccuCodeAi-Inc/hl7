from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP import (
    PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP,
)
from ..segments.VAR import VAR
from ..segments.NTE import NTE
from ..segments.GOL import GOL
from ..segment_groups.PGL_PC8_GOAL_GROUP_PATHWAY_GROUP import (
    PGL_PC8_GOAL_GROUP_PATHWAY_GROUP,
)
from ..segment_groups.PGL_PC8_GOAL_GROUP_ORDER_GROUP import (
    PGL_PC8_GOAL_GROUP_ORDER_GROUP,
)
from ..segment_groups.PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP import (
    PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP,
)
from ..segment_groups.PGL_PC8_GOAL_GROUP_PROBLEM_GROUP import (
    PGL_PC8_GOAL_GROUP_PROBLEM_GROUP,
)


"""
GOAL - PGL_PC8_GOAL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC8_GOAL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PGL_PC8_GOAL_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, GOL, VAR
)
from utils.hl7.v2_5_1.segment_groups import (
    PGL_PC8_GOAL_GROUP_ORDER_GROUP, PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, PGL_PC8_GOAL_GROUP_PROBLEM_GROUP
)

pgl_pc8_goal_group = PGL_PC8_GOAL_GROUP(  # GOAL - Segment group for PGL_PC8 - Goal delete consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, PATHWAY|None, OBSERVATION|None, PROBLEM|None, ORDER|None
    goal_detail=gol,  # GOL(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    goal_role=None,  # PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP(...) 
    pathway=None,  # PGL_PC8_GOAL_GROUP_PATHWAY_GROUP(...) 
    observation=None,  # PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP(...) 
    problem=None,  # PGL_PC8_GOAL_GROUP_PROBLEM_GROUP(...) 
    order=None,  # PGL_PC8_GOAL_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PGL_PC8_GOAL_GROUP TEMPLATE-----
"""


class PGL_PC8_GOAL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PGL_PC8_GOAL_GROUP"""
    _hl7_name = """GOAL"""
    _hl7_description = """Segment group for PGL_PC8 - Goal delete consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, PATHWAY|None, OBSERVATION|None, PROBLEM|None, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC8_GOAL_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("6", "7", "8", "None", "None", "None", "None", "None")
    _c_components = (GOL, NTE, VAR, PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, PGL_PC8_GOAL_GROUP_PROBLEM_GROUP, PGL_PC8_GOAL_GROUP_ORDER_GROUP)
    _c_name = ("GOL", "NTE", "VAR", "GOAL ROLE", "PATHWAY", "OBSERVATION", "PROBLEM", "ORDER")
    _c_is_group = (False, False, False, True, True, True, True, True)
    _c_attrs = ("goal_detail", "notes_and_comments", "variance", "goal_role", "pathway", "observation", "problem", "order",)
    # fmt: on

    def __init__(
        self,
        goal_detail: GOL,  #  Required. GOL.6
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.7
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.8
        goal_role: PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | None = None,  #  (ROL.9, VAR.10, ...)
        pathway: PGL_PC8_GOAL_GROUP_PATHWAY_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, ...]
        | None = None,  #  (PTH.11, VAR.12, ...)
        observation: PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.13, NTE.14, ...)
        problem: PGL_PC8_GOAL_GROUP_PROBLEM_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_PROBLEM_GROUP, ...]
        | None = None,  #  (PRB.15, NTE.16, VAR.17, ...)
        order: PGL_PC8_GOAL_GROUP_ORDER_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.22, ...)
    ):
        """
        None - `PGL_PC8_GOAL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC8_GOAL_GROUP>`_
        Segment group for PGL_PC8 - Goal delete consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, PATHWAY|None, OBSERVATION|None, PROBLEM|None, ORDER|None

        :param goal_detail: Goal Detail (id: GOL | seq: 6 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 7 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 8 | use: O | rpt: *)
        :param goal_role: Goal Role segment group: [ROL, VAR|None] (id: GOAL ROLE | seq: 9, 10 | use: O | rpt: *)
        :param pathway: Pathway segment group: [PTH, VAR|None] (id: PATHWAY | seq: 11, 12 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 13, 14 | use: O | rpt: *)
        :param problem: Problem segment group: [PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None] (id: PROBLEM | seq: 15, 16, 17, None, None | use: O | rpt: *)
        :param order: Order segment group: [ORC, ORDER DETAIL|None] (id: ORDER | seq: 22, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.goal_detail = goal_detail
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.goal_role = goal_role
        self.pathway = pathway
        self.observation = observation
        self.problem = problem
        self.order = order

    @property  # get GOL.6
    def goal_detail(self) -> GOL:
        """
        id: GOL | use: R | rpt: 1 | seq: 6
        ---
        return_type: GOL.6: Goal Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL
        """
        return self._c_data[0][0]

    @goal_detail.setter  # set GOL.6
    def goal_detail(self, gol: GOL):
        """
        id: GOL | use: R | rpt: 1 | seq: 6
        ---
        param_type: GOL.6: Goal Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL
        """
        self._c_data[0] = (gol,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NTE.7 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: VAR.8 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[2] = var
        else:
            self._c_data[2] = (var,)

    @property  # get GOAL ROLE
    def goal_role(self) -> tuple[PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, ...] | tuple[None]:
        """
        id: PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP
        """
        return self._c_data[3]

    @goal_role.setter  # set GOAL ROLE
    def goal_role(
        self,
        goal_role: PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | None,
    ):
        """
        id: GOAL ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP.None | tuple[PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_GOAL_ROLE_GROUP
        """
        if isinstance(goal_role, tuple):
            self._c_data[3] = goal_role
        else:
            self._c_data[3] = (goal_role,)

    @property  # get PATHWAY
    def pathway(self) -> tuple[PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, ...] | tuple[None]:
        """
        id: PGL_PC8_GOAL_GROUP_PATHWAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_PATHWAY_GROUP
        """
        return self._c_data[4]

    @pathway.setter  # set PATHWAY
    def pathway(
        self,
        pathway: PGL_PC8_GOAL_GROUP_PATHWAY_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, ...]
        | None,
    ):
        """
        id: PATHWAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PGL_PC8_GOAL_GROUP_PATHWAY_GROUP.None | tuple[PGL_PC8_GOAL_GROUP_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_PATHWAY_GROUP
        """
        if isinstance(pathway, tuple):
            self._c_data[4] = pathway
        else:
            self._c_data[4] = (pathway,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP.None | tuple[PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[5] = observation
        else:
            self._c_data[5] = (observation,)

    @property  # get PROBLEM
    def problem(self) -> tuple[PGL_PC8_GOAL_GROUP_PROBLEM_GROUP, ...] | tuple[None]:
        """
        id: PGL_PC8_GOAL_GROUP_PROBLEM_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PGL_PC8_GOAL_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_PROBLEM_GROUP
        """
        return self._c_data[6]

    @problem.setter  # set PROBLEM
    def problem(
        self,
        problem: PGL_PC8_GOAL_GROUP_PROBLEM_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_PROBLEM_GROUP, ...]
        | None,
    ):
        """
        id: PROBLEM SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PGL_PC8_GOAL_GROUP_PROBLEM_GROUP.None | tuple[PGL_PC8_GOAL_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_PROBLEM_GROUP
        """
        if isinstance(problem, tuple):
            self._c_data[6] = problem
        else:
            self._c_data[6] = (problem,)

    @property  # get ORDER
    def order(self) -> tuple[PGL_PC8_GOAL_GROUP_ORDER_GROUP, ...] | tuple[None]:
        """
        id: PGL_PC8_GOAL_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PGL_PC8_GOAL_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_ORDER_GROUP
        """
        return self._c_data[7]

    @order.setter  # set ORDER
    def order(
        self,
        order: PGL_PC8_GOAL_GROUP_ORDER_GROUP
        | tuple[PGL_PC8_GOAL_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PGL_PC8_GOAL_GROUP_ORDER_GROUP.None | tuple[PGL_PC8_GOAL_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC8_GOAL_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[7] = order
        else:
            self._c_data[7] = (order,)
