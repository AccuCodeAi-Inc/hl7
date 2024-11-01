from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP,
)
from ..segment_groups.PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP,
)
from ..segment_groups.PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP,
)
from ..segment_groups.PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP,
)
from ..segment_groups.PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP,
)
from ..segments.VAR import VAR
from ..segments.GOL import GOL
from ..segments.NTE import NTE


"""
GOAL - PPV_PCA_PATIENT_GROUP_GOAL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP_GOAL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPV_PCA_PATIENT_GROUP_GOAL_GROUP
from utils.hl7.v2_5_1.segments import (
    GOL, NTE, VAR
)
from utils.hl7.v2_5_1.segment_groups import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
)

ppv_pca_patient_group_goal_group = PPV_PCA_PATIENT_GROUP_GOAL_GROUP(  # GOAL - Segment group for PPV_PCA_PATIENT_GROUP - PATIENT consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL PATHWAY|None, GOAL OBSERVATION|None, PROBLEM|None, ORDER|None
    goal_detail=gol,  # GOL(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    goal_role=None,  # PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP(...) 
    goal_pathway=None,  # PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP(...) 
    goal_observation=None,  # PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP(...) 
    problem=None,  # PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP(...) 
    order=None,  # PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP_GOAL_GROUP TEMPLATE-----
"""


class PPV_PCA_PATIENT_GROUP_GOAL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPV_PCA_PATIENT_GROUP_GOAL_GROUP"""
    _hl7_name = """GOAL"""
    _hl7_description = """Segment group for PPV_PCA_PATIENT_GROUP - PATIENT consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL PATHWAY|None, GOAL OBSERVATION|None, PROBLEM|None, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP_GOAL_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("10", "11", "12", "None", "None", "None", "None", "None")
    _c_components = (GOL, NTE, VAR, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP)
    _c_name = ("GOL", "NTE", "VAR", "GOAL ROLE", "GOAL PATHWAY", "GOAL OBSERVATION", "PROBLEM", "ORDER")
    _c_is_group = (False, False, False, True, True, True, True, True)
    _c_attrs = ("goal_detail", "notes_and_comments", "variance", "goal_role", "goal_pathway", "goal_observation", "problem", "order",)
    # fmt: on

    def __init__(
        self,
        goal_detail: GOL,  #  Required. GOL.10
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.12
        goal_role: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | None = None,  #  (ROL.13, VAR.14, ...)
        goal_pathway: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, ...]
        | None = None,  #  (PTH.15, VAR.16, ...)
        goal_observation: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.17, NTE.18, ...)
        problem: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, ...]
        | None = None,  #  (PRB.19, NTE.20, VAR.21, ...)
        order: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.26, ...)
    ):
        """
        None - `PPV_PCA_PATIENT_GROUP_GOAL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP_GOAL_GROUP>`_
        Segment group for PPV_PCA_PATIENT_GROUP - PATIENT consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL PATHWAY|None, GOAL OBSERVATION|None, PROBLEM|None, ORDER|None

        :param goal_detail: Goal Detail (id: GOL | seq: 10 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 12 | use: O | rpt: *)
        :param goal_role: Goal Role segment group: [ROL, VAR|None] (id: GOAL ROLE | seq: 13, 14 | use: O | rpt: *)
        :param goal_pathway: Goal Pathway segment group: [PTH, VAR|None] (id: GOAL PATHWAY | seq: 15, 16 | use: O | rpt: *)
        :param goal_observation: Goal Observation segment group: [OBX, NTE|None] (id: GOAL OBSERVATION | seq: 17, 18 | use: O | rpt: *)
        :param problem: Problem segment group: [PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None] (id: PROBLEM | seq: 19, 20, 21, None, None | use: O | rpt: *)
        :param order: Order segment group: [ORC, ORDER DETAIL|None] (id: ORDER | seq: 26, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.goal_detail = goal_detail
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.goal_role = goal_role
        self.goal_pathway = goal_pathway
        self.goal_observation = goal_observation
        self.problem = problem
        self.order = order

    @property  # get GOL.10
    def goal_detail(self) -> GOL:
        """
        id: GOL | use: R | rpt: 1 | seq: 10
        ---
        return_type: GOL.10: Goal Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL
        """
        return self._c_data[0][0]

    @goal_detail.setter  # set GOL.10
    def goal_detail(self, gol: GOL):
        """
        id: GOL | use: R | rpt: 1 | seq: 10
        ---
        param_type: GOL.10: Goal Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL
        """
        self._c_data[0] = (gol,)

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

    @property  # get GOAL ROLE
    def goal_role(
        self,
    ) -> tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...] | tuple[None]:
        """
        id: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        """
        return self._c_data[3]

    @goal_role.setter  # set GOAL ROLE
    def goal_role(
        self,
        goal_role: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | None,
    ):
        """
        id: GOAL ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP.None | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        """
        if isinstance(goal_role, tuple):
            self._c_data[3] = goal_role
        else:
            self._c_data[3] = (goal_role,)

    @property  # get GOAL PATHWAY
    def goal_pathway(
        self,
    ) -> tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, ...] | tuple[None]:
        """
        id: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP
        """
        return self._c_data[4]

    @goal_pathway.setter  # set GOAL PATHWAY
    def goal_pathway(
        self,
        goal_pathway: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, ...]
        | None,
    ):
        """
        id: GOAL PATHWAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP.None | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_PATHWAY_GROUP
        """
        if isinstance(goal_pathway, tuple):
            self._c_data[4] = goal_pathway
        else:
            self._c_data[4] = (goal_pathway,)

    @property  # get GOAL OBSERVATION
    def goal_observation(
        self,
    ) -> (
        tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @goal_observation.setter  # set GOAL OBSERVATION
    def goal_observation(
        self,
        goal_observation: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: GOAL OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP.None | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        """
        if isinstance(goal_observation, tuple):
            self._c_data[5] = goal_observation
        else:
            self._c_data[5] = (goal_observation,)

    @property  # get PROBLEM
    def problem(
        self,
    ) -> tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, ...] | tuple[None]:
        """
        id: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP
        """
        return self._c_data[6]

    @problem.setter  # set PROBLEM
    def problem(
        self,
        problem: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, ...]
        | None,
    ):
        """
        id: PROBLEM SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP.None | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_PROBLEM_GROUP
        """
        if isinstance(problem, tuple):
            self._c_data[6] = problem
        else:
            self._c_data[6] = (problem,)

    @property  # get ORDER
    def order(
        self,
    ) -> tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP, ...] | tuple[None]:
        """
        id: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP
        """
        return self._c_data[7]

    @order.setter  # set ORDER
    def order(
        self,
        order: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP.None | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[7] = order
        else:
            self._c_data[7] = (order,)
