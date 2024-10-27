from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PRB import PRB
from ..segment_groups.PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP import (
    PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP,
)
from ..segment_groups.PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP import (
    PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP,
)
from ..segments.NTE import NTE
from ..segment_groups.PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP import (
    PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
)
from ..segments.VAR import VAR
from ..segment_groups.PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP import (
    PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP,
)


"""
PROBLEM - PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP
from utils.hl7.v2_5_1.segments import (
    VAR, PRB, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
)

ptr_pcf_patient_group_pathway_group_problem_group = PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP(  # PROBLEM - Segment group for PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP - PATHWAY consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None
    problem_details=prb,  # PRB(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    problem_role=None,  # PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(...) 
    problem_observation=None,  # PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP(...) 
    goal=None,  # PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP(...) 
    order=None,  # PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP TEMPLATE-----
"""


class PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP"""
    _hl7_name = """PROBLEM"""
    _hl7_description = """Segment group for PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP - PATHWAY consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("15", "16", "17", "None", "None", "None", "None")
    _c_components = (PRB, NTE, VAR, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP)
    _c_name = ("PRB", "NTE", "VAR", "PROBLEM ROLE", "PROBLEM OBSERVATION", "GOAL", "ORDER")
    _c_is_group = (False, False, False, True, True, True, True)
    _c_attrs = ("problem_details", "notes_and_comments", "variance", "problem_role", "problem_observation", "goal", "order",)
    # fmt: on

    def __init__(
        self,
        problem_details: PRB,  #  Required. PRB.15
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.16
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.17
        problem_role: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        | tuple[
            PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...
        ]
        | None = None,  #  (ROL.18, VAR.19, ...)
        problem_observation: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        | tuple[
            PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.20, NTE.21, ...)
        goal: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP
        | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]
        | None = None,  #  (GOL.22, NTE.23, VAR.24, ...)
        order: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP
        | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.29, ...)
    ):
        """
        None - `PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP>`_
        Segment group for PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP - PATHWAY consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None

        :param problem_details: Problem Details (id: PRB | seq: 15 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 16 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 17 | use: O | rpt: *)
        :param problem_role: Problem Role segment group: [ROL, VAR|None] (id: PROBLEM ROLE | seq: 18, 19 | use: O | rpt: *)
        :param problem_observation: Problem Observation segment group: [OBX, NTE|None] (id: PROBLEM OBSERVATION | seq: 20, 21 | use: O | rpt: *)
        :param goal: Goal segment group: [GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL OBSERVATION|None] (id: GOAL | seq: 22, 23, 24, None, None | use: O | rpt: *)
        :param order: Order segment group: [ORC, ORDER DETAIL|None] (id: ORDER | seq: 29, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.problem_details = problem_details
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.problem_role = problem_role
        self.problem_observation = problem_observation
        self.goal = goal
        self.order = order

    @property  # get PRB.15
    def problem_details(self) -> PRB:
        """
        id: PRB | use: R | rpt: 1 | seq: 15
        ---
        return_type: PRB.15: Problem Details
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        return self._c_data[0][0]

    @problem_details.setter  # set PRB.15
    def problem_details(self, prb: PRB):
        """
        id: PRB | use: R | rpt: 1 | seq: 15
        ---
        param_type: PRB.15: Problem Details
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        self._c_data[0] = (prb,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: NTE.16 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: VAR.17 | tuple[VAR, ...]: (Variance, ...)
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
        tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        """
        return self._c_data[3]

    @problem_role.setter  # set PROBLEM ROLE
    def problem_role(
        self,
        problem_role: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        | tuple[
            PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...
        ]
        | None,
    ):
        """
        id: PROBLEM ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP.None | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        """
        if isinstance(problem_role, tuple):
            self._c_data[3] = problem_role
        else:
            self._c_data[3] = (problem_role,)

    @property  # get PROBLEM OBSERVATION
    def problem_observation(
        self,
    ) -> (
        tuple[
            PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @problem_observation.setter  # set PROBLEM OBSERVATION
    def problem_observation(
        self,
        problem_observation: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        | tuple[
            PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: PROBLEM OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP.None | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        """
        if isinstance(problem_observation, tuple):
            self._c_data[4] = problem_observation
        else:
            self._c_data[4] = (problem_observation,)

    @property  # get GOAL
    def goal(
        self,
    ) -> (
        tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP
        """
        return self._c_data[5]

    @goal.setter  # set GOAL
    def goal(
        self,
        goal: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP
        | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]
        | None,
    ):
        """
        id: GOAL SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP.None | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_GOAL_GROUP
        """
        if isinstance(goal, tuple):
            self._c_data[5] = goal
        else:
            self._c_data[5] = (goal,)

    @property  # get ORDER
    def order(
        self,
    ) -> (
        tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP
        """
        return self._c_data[6]

    @order.setter  # set ORDER
    def order(
        self,
        order: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP
        | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP.None | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP_PROBLEM_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[6] = order
        else:
            self._c_data[6] = (order,)