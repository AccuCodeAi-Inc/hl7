from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CSP import CSP
from ..segment_groups.CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP import (
    CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP,
)


"""
STUDY PHASE - CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP
from utils.hl7.v2_5_1.segments import (
    CSP
)
from utils.hl7.v2_5_1.segment_groups import (
    CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
)

csu_c11_patient_group_study_phase_group = CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP(  # STUDY PHASE - Segment group for CSU_C11_PATIENT_GROUP - PATIENT consisting of CSP|None, STUDY SCHEDULE
    clinical_study_phase=None,  # CSP(...) 
    study_schedule=csu_c11_patient_group_study_phase_group_study_schedule_group,  # CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP TEMPLATE-----
"""


class CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP"""
    _hl7_name = """STUDY PHASE"""
    _hl7_description = """Segment group for CSU_C11_PATIENT_GROUP - PATIENT consisting of CSP|None, STUDY SCHEDULE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("9", "None")
    _c_components = (CSP, CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP)
    _c_name = ("CSP", "STUDY SCHEDULE")
    _c_is_group = (False, True)
    _c_attrs = ("clinical_study_phase", "study_schedule",)
    # fmt: on

    def __init__(
        self,
        study_schedule: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
        | tuple[
            CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP, ...
        ],  #  Required. (CSS.10, ...)
        clinical_study_phase: CSP | None = None,  #  CSP.9
    ):
        """
        None - `CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP>`_
        Segment group for CSU_C11_PATIENT_GROUP - PATIENT consisting of CSP|None, STUDY SCHEDULE

        :param clinical_study_phase: Clinical Study Phase (id: CSP | seq: 9 | use: O | rpt: 1)
        :param study_schedule: Study Schedule segment group: [CSS|None, STUDY OBSERVATION, STUDY PHARM] (id: STUDY SCHEDULE | seq: 10, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.clinical_study_phase = clinical_study_phase
        self.study_schedule = study_schedule

    @property  # get CSP.9
    def clinical_study_phase(self) -> CSP | None:
        """
        id: CSP | use: O | rpt: 1 | seq: 9
        ---
        return_type: CSP.9: Clinical Study Phase
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP
        """
        return self._c_data[0][0]

    @clinical_study_phase.setter  # set CSP.9
    def clinical_study_phase(self, csp: CSP | None):
        """
        id: CSP | use: O | rpt: 1 | seq: 9
        ---
        param_type: CSP.9: Clinical Study Phase
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP
        """
        self._c_data[0] = (csp,)

    @property  # get STUDY SCHEDULE
    def study_schedule(
        self,
    ) -> tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP, ...]:
        """
        id: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
        """
        return self._c_data[1]

    @study_schedule.setter  # set STUDY SCHEDULE
    def study_schedule(
        self,
        study_schedule: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
        | tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP, ...],
    ):
        """
        id: STUDY SCHEDULE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP.None | tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
        """
        if isinstance(study_schedule, tuple):
            self._c_data[1] = study_schedule
        else:
            self._c_data[1] = (study_schedule,)
