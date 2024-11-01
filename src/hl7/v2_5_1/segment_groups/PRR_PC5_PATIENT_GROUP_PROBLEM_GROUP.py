from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP,
)
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP,
)
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP,
)
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP,
)
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
)
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from ..segments.NTE import NTE


"""
PROBLEM - PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, PRB, VAR
)
from utils.hl7.v2_5_1.segment_groups import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP
)

prr_pc5_patient_group_problem_group = PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP(  # PROBLEM - Segment group for PRR_PC5_PATIENT_GROUP - PATIENT consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM PATHWAY|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None
    problem_details=prb,  # PRB(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    problem_role=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(...) 
    problem_pathway=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP(...) 
    problem_observation=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP(...) 
    goal=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP(...) 
    order=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP TEMPLATE-----
"""


class PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP"""
    _hl7_name = """PROBLEM"""
    _hl7_description = """Segment group for PRR_PC5_PATIENT_GROUP - PATIENT consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM PATHWAY|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("10", "11", "12", "None", "None", "None", "None", "None")
    _c_components = (PRB, NTE, VAR, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP)
    _c_name = ("PRB", "NTE", "VAR", "PROBLEM ROLE", "PROBLEM PATHWAY", "PROBLEM OBSERVATION", "GOAL", "ORDER")
    _c_is_group = (False, False, False, True, True, True, True, True)
    _c_attrs = ("problem_details", "notes_and_comments", "variance", "problem_role", "problem_pathway", "problem_observation", "goal", "order",)
    # fmt: on

    def __init__(
        self,
        problem_details: PRB,  #  Required. PRB.10
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.12
        problem_role: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]
        | None = None,  #  (ROL.13, VAR.14, ...)
        problem_pathway: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, ...]
        | None = None,  #  (PTH.15, VAR.16, ...)
        problem_observation: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.17, NTE.18, ...)
        goal: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]
        | None = None,  #  (GOL.19, NTE.20, VAR.21, ...)
        order: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.26, ...)
    ):
        """
        None - `PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP>`_
        Segment group for PRR_PC5_PATIENT_GROUP - PATIENT consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM PATHWAY|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None

        :param problem_details: Problem Details (id: PRB | seq: 10 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 12 | use: O | rpt: *)
        :param problem_role: Problem Role segment group: [ROL, VAR|None] (id: PROBLEM ROLE | seq: 13, 14 | use: O | rpt: *)
        :param problem_pathway: Problem Pathway segment group: [PTH, VAR|None] (id: PROBLEM PATHWAY | seq: 15, 16 | use: O | rpt: *)
        :param problem_observation: Problem Observation segment group: [OBX, NTE|None] (id: PROBLEM OBSERVATION | seq: 17, 18 | use: O | rpt: *)
        :param goal: Goal segment group: [GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL OBSERVATION|None] (id: GOAL | seq: 19, 20, 21, None, None | use: O | rpt: *)
        :param order: Order segment group: [ORC, ORDER DETAIL|None] (id: ORDER | seq: 26, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.problem_details = problem_details
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.problem_role = problem_role
        self.problem_pathway = problem_pathway
        self.problem_observation = problem_observation
        self.goal = goal
        self.order = order

    @property  # get PRB.10
    def problem_details(self) -> PRB:
        """
        id: PRB | use: R | rpt: 1 | seq: 10
        ---
        return_type: PRB.10: Problem Details
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        return self._c_data[0][0]

    @problem_details.setter  # set PRB.10
    def problem_details(self, prb: PRB):
        """
        id: PRB | use: R | rpt: 1 | seq: 10
        ---
        param_type: PRB.10: Problem Details
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        self._c_data[0] = (prb,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: NTE.11 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: VAR.12 | tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        if isinstance(var, tuple):
            self._c_data[2] = var
        else:
            self._c_data[2] = (var,)

    @property  # get PROBLEM ROLE
    def problem_role(
        self,
    ) -> (
        tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...] | tuple[None]
    ):
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        """
        return self._c_data[3]

    @problem_role.setter  # set PROBLEM ROLE
    def problem_role(
        self,
        problem_role: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]
        | None,
    ):
        """
        id: PROBLEM ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        """
        if isinstance(problem_role, tuple):
            self._c_data[3] = problem_role
        else:
            self._c_data[3] = (problem_role,)

    @property  # get PROBLEM PATHWAY
    def problem_pathway(
        self,
    ) -> (
        tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP
        """
        return self._c_data[4]

    @problem_pathway.setter  # set PROBLEM PATHWAY
    def problem_pathway(
        self,
        problem_pathway: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, ...]
        | None,
    ):
        """
        id: PROBLEM PATHWAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_PATHWAY_GROUP
        """
        if isinstance(problem_pathway, tuple):
            self._c_data[4] = problem_pathway
        else:
            self._c_data[4] = (problem_pathway,)

    @property  # get PROBLEM OBSERVATION
    def problem_observation(
        self,
    ) -> (
        tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @problem_observation.setter  # set PROBLEM OBSERVATION
    def problem_observation(
        self,
        problem_observation: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: PROBLEM OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        """
        if isinstance(problem_observation, tuple):
            self._c_data[5] = problem_observation
        else:
            self._c_data[5] = (problem_observation,)

    @property  # get GOAL
    def goal(
        self,
    ) -> tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...] | tuple[None]:
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP
        """
        return self._c_data[6]

    @goal.setter  # set GOAL
    def goal(
        self,
        goal: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]
        | None,
    ):
        """
        id: GOAL SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP
        """
        if isinstance(goal, tuple):
            self._c_data[6] = goal
        else:
            self._c_data[6] = (goal,)

    @property  # get ORDER
    def order(
        self,
    ) -> tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...] | tuple[None]:
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP
        """
        return self._c_data[7]

    @order.setter  # set ORDER
    def order(
        self,
        order: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[7] = order
        else:
            self._c_data[7] = (order,)
