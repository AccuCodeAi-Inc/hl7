from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.VAR import VAR
from ..segments.NTE import NTE
from ..segment_groups.PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP,
)
from ..segments.PRB import PRB
from ..segment_groups.PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
)


"""
PROBLEM - PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, VAR, PRB
)
from utils.hl7.v2_5_1.segment_groups import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
)

ppt_pcl_patient_group_pathway_group_goal_group_problem_group = PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP(  # PROBLEM - Segment group for PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP - GOAL consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None
    problem_details=prb,  # PRB(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    variance=None,  # VAR(...) 
    problem_role=None,  # PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP(...) 
    problem_observation=None,  # PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP TEMPLATE-----
"""


class PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP"""
    _hl7_name = """PROBLEM"""
    _hl7_description = """Segment group for PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP - GOAL consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("22", "23", "24", "None", "None")
    _c_components = (PRB, NTE, VAR, PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP)
    _c_name = ("PRB", "NTE", "VAR", "PROBLEM ROLE", "PROBLEM OBSERVATION")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("problem_details", "notes_and_comments", "variance", "problem_role", "problem_observation",)
    # fmt: on

    def __init__(
        self,
        problem_details: PRB,  #  Required. PRB.22
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.23
        variance: VAR | tuple[VAR, ...] | None = None,  #  VAR.24
        problem_role: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP,
            ...,
        ]
        | None = None,  #  (ROL.25, VAR.26, ...)
        problem_observation: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.27, NTE.28, ...)
    ):
        """
        None - `PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP>`_
        Segment group for PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP - GOAL consisting of PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM OBSERVATION|None

        :param problem_details: Problem Details (id: PRB | seq: 22 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 23 | use: O | rpt: *)
        :param variance: Variance (id: VAR | seq: 24 | use: O | rpt: *)
        :param problem_role: Problem Role segment group: [ROL, VAR|None] (id: PROBLEM ROLE | seq: 25, 26 | use: O | rpt: *)
        :param problem_observation: Problem Observation segment group: [OBX, NTE|None] (id: PROBLEM OBSERVATION | seq: 27, 28 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.problem_details = problem_details
        self.notes_and_comments = notes_and_comments
        self.variance = variance
        self.problem_role = problem_role
        self.problem_observation = problem_observation

    @property  # get PRB.22
    def problem_details(self) -> PRB:
        """
        id: PRB | use: R | rpt: 1 | seq: 22
        ---
        return_type: PRB.22: Problem Details
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        return self._c_data[0][0]

    @problem_details.setter  # set PRB.22
    def problem_details(self, prb: PRB):
        """
        id: PRB | use: R | rpt: 1 | seq: 22
        ---
        param_type: PRB.22: Problem Details
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRB
        """
        self._c_data[0] = (prb,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: NTE.23 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        return_type: tuple[VAR, ...]: (Variance, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VAR
        """
        return self._c_data[2]

    @variance.setter  # set VAR
    def variance(self, var: VAR | tuple[VAR, ...] | None):
        """
        id: VAR SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        param_type: VAR.24 | tuple[VAR, ...]: (Variance, ...)
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
        tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        """
        return self._c_data[3]

    @problem_role.setter  # set PROBLEM ROLE
    def problem_role(
        self,
        problem_role: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: PROBLEM ROLE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP.None | tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_ROLE_GROUP
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
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @problem_observation.setter  # set PROBLEM OBSERVATION
    def problem_observation(
        self,
        problem_observation: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: PROBLEM OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP.None | tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP_GOAL_GROUP_PROBLEM_GROUP_PROBLEM_OBSERVATION_GROUP
        """
        if isinstance(problem_observation, tuple):
            self._c_data[4] = problem_observation
        else:
            self._c_data[4] = (problem_observation,)
