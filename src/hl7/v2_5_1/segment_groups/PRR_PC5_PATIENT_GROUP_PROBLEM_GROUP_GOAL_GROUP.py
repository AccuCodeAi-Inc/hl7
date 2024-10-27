from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP,
)
from ..segments.NTE import NTE
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP,
)
from ..segments.GOL import GOL
from ..segments.VAR import VAR


"""
GOAL - PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP
from utils.hl7.v2_5_1.segments import (
    VAR, NTE, GOL
)
from utils.hl7.v2_5_1.segment_groups import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
)

prr_pc5_patient_group_problem_group_goal_group = PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP(  # GOAL - Segment group for PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP - PROBLEM consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL OBSERVATION|None
    goal_detail=gol,  # GOL(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    goal_role=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP(...) 
    goal_observation=None,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP TEMPLATE-----
"""


class PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP"""
    _hl7_name = """GOAL"""
    _hl7_description = """Segment group for PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP - PROBLEM consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("19", "20", "21", "None", "None")
    _c_components = (GOL, NTE, VAR, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP)
    _c_name = ("GOL", "NTE", "VAR", "GOAL ROLE", "GOAL OBSERVATION")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("goal_detail", "notes_and_comments", "variance", "goal_role", "goal_observation",)
    # fmt: on

    def __init__(
        self,
        goal_detail: GOL,  #  Required. GOL.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.20
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.21
        goal_role: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | None = None,  #  (ROL.22, VAR.23, ...)
        goal_observation: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        | tuple[
            PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...
        ]
        | None = None,  #  (OBX.24, NTE.25, ...)
    ):
        """
        None - `PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP>`_
        Segment group for PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP - PROBLEM consisting of GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL OBSERVATION|None

        :param goal_detail: Goal Detail (id: GOL | seq: 19 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 20 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 21 | use: O | rpt: *)
        :param goal_role: Goal Role segment group: [ROL, VAR|None] (id: GOAL ROLE | seq: 22, 23 | use: O | rpt: *)
        :param goal_observation: Goal Observation segment group: [OBX, NTE|None] (id: GOAL OBSERVATION | seq: 24, 25 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.goal_detail = goal_detail
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.goal_role = goal_role
        self.goal_observation = goal_observation

    @property  # get GOL.19
    def goal_detail(self) -> GOL:
        """
        id: GOL | use: R | rpt: 1 | seq: 19
        ---
        return_type: GOL.19: Goal Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL
        """
        return self._c_data[0][0]

    @goal_detail.setter  # set GOL.19
    def goal_detail(self, gol: GOL):
        """
        id: GOL | use: R | rpt: 1 | seq: 19
        ---
        param_type: GOL.19: Goal Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GOL
        """
        self._c_data[0] = (gol,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: NTE.20 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: VAR.21 | tuple[VAR, ...]: (Variance, ...)
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
    ) -> (
        tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | tuple[None]
    ):
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        """
        return self._c_data[3]

    @goal_role.setter  # set GOAL ROLE
    def goal_role(
        self,
        goal_role: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]
        | None,
    ):
        """
        id: GOAL ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_ROLE_GROUP
        """
        if isinstance(goal_role, tuple):
            self._c_data[3] = goal_role
        else:
            self._c_data[3] = (goal_role,)

    @property  # get GOAL OBSERVATION
    def goal_observation(
        self,
    ) -> (
        tuple[
            PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...
        ]
        | tuple[None]
    ):
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @goal_observation.setter  # set GOAL OBSERVATION
    def goal_observation(
        self,
        goal_observation: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        | tuple[
            PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...
        ]
        | None,
    ):
        """
        id: GOAL OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP_GOAL_GROUP_GOAL_OBSERVATION_GROUP
        """
        if isinstance(goal_observation, tuple):
            self._c_data[4] = goal_observation
        else:
            self._c_data[4] = (goal_observation,)