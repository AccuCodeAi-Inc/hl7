from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segment_groups.PPV_PCA_PATIENT_GROUP_GOAL_GROUP import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP,
)
from ..segments.PID import PID


"""
PATIENT - PPV_PCA_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPV_PCA_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    PPV_PCA_PATIENT_GROUP_GOAL_GROUP, PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP
)

ppv_pca_patient_group = PPV_PCA_PATIENT_GROUP(  # PATIENT - Segment group for PPV_PCA - Patient goal response consisting of PID, PATIENT VISIT|None, GOAL
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
    goal=ppv_pca_patient_group_goal_group,  # PPV_PCA_PATIENT_GROUP_GOAL_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPV_PCA_PATIENT_GROUP TEMPLATE-----
"""


class PPV_PCA_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPV_PCA_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for PPV_PCA - Patient goal response consisting of PID, PATIENT VISIT|None, GOAL"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("7", "None", "None")
    _c_components = (PID, PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP, PPV_PCA_PATIENT_GROUP_GOAL_GROUP)
    _c_name = ("PID", "PATIENT VISIT", "GOAL")
    _c_is_group = (False, True, True)
    _c_attrs = ("patient_identification", "patient_visit", "goal",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        goal: PPV_PCA_PATIENT_GROUP_GOAL_GROUP
        | tuple[
            PPV_PCA_PATIENT_GROUP_GOAL_GROUP, ...
        ],  #  Required. (GOL.10, NTE.11, VAR.12, ...)
        patient_visit: PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.8, PV2.9
    ):
        """
        None - `PPV_PCA_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPV_PCA_PATIENT_GROUP>`_
        Segment group for PPV_PCA - Patient goal response consisting of PID, PATIENT VISIT|None, GOAL

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 8, 9 | use: O | rpt: 1)
        :param goal: Goal segment group: [GOL, NTE|None, VAR|None, GOAL ROLE|None, GOAL PATHWAY|None, GOAL OBSERVATION|None, PROBLEM|None, ORDER|None] (id: GOAL | seq: 10, 11, 12, None, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.goal = goal

    @property  # get PID.7
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        return_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.7
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        param_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[1] = (patient_v_isit,)

    @property  # get GOAL
    def goal(self) -> tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP, ...]:
        """
        id: PPV_PCA_PATIENT_GROUP_GOAL_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP
        """
        return self._c_data[2]

    @goal.setter  # set GOAL
    def goal(
        self,
        goal: PPV_PCA_PATIENT_GROUP_GOAL_GROUP
        | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP, ...],
    ):
        """
        id: GOAL SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PPV_PCA_PATIENT_GROUP_GOAL_GROUP.None | tuple[PPV_PCA_PATIENT_GROUP_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPV_PCA_PATIENT_GROUP_GOAL_GROUP
        """
        if isinstance(goal, tuple):
            self._c_data[2] = goal
        else:
            self._c_data[2] = (goal,)
