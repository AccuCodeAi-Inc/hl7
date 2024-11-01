from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segments.PID import PID
from ..segment_groups.PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP import (
    PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP,
)


"""
PATIENT - PRR_PC5_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PRR_PC5_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
)

prr_pc5_patient_group = PRR_PC5_PATIENT_GROUP(  # PATIENT - Segment group for PRR_PC5 - Patient problem response consisting of PID, PATIENT VISIT|None, PROBLEM
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
    problem=prr_pc5_patient_group_problem_group,  # PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PRR_PC5_PATIENT_GROUP TEMPLATE-----
"""


class PRR_PC5_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PRR_PC5_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for PRR_PC5 - Patient problem response consisting of PID, PATIENT VISIT|None, PROBLEM"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("7", "None", "None")
    _c_components = (PID, PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP, PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP)
    _c_name = ("PID", "PATIENT VISIT", "PROBLEM")
    _c_is_group = (False, True, True)
    _c_attrs = ("patient_identification", "patient_visit", "problem",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        problem: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
        | tuple[
            PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP, ...
        ],  #  Required. (PRB.10, NTE.11, VAR.12, ...)
        patient_visit: PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.8, PV2.9
    ):
        """
        None - `PRR_PC5_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PRR_PC5_PATIENT_GROUP>`_
        Segment group for PRR_PC5 - Patient problem response consisting of PID, PATIENT VISIT|None, PROBLEM

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 8, 9 | use: O | rpt: 1)
        :param problem: Problem segment group: [PRB, NTE|None, VAR|None, PROBLEM ROLE|None, PROBLEM PATHWAY|None, PROBLEM OBSERVATION|None, GOAL|None, ORDER|None] (id: PROBLEM | seq: 10, 11, 12, None, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.problem = problem

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

    @property  # get PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[1] = (patient_v_isit,)

    @property  # get PROBLEM
    def problem(self) -> tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP, ...]:
        """
        id: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
        """
        return self._c_data[2]

    @problem.setter  # set PROBLEM
    def problem(
        self,
        problem: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
        | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP, ...],
    ):
        """
        id: PROBLEM SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP.None | tuple[PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRR_PC5_PATIENT_GROUP_PROBLEM_GROUP
        """
        if isinstance(problem, tuple):
            self._c_data[2] = problem
        else:
            self._c_data[2] = (problem,)
