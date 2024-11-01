from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP import (
    CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP,
)
from ..segments.CSS import CSS
from ..segment_groups.CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP import (
    CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP,
)


"""
STUDY SCHEDULE - CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP
from utils.hl7.v2_5_1.segments import (
    CSS
)
from utils.hl7.v2_5_1.segment_groups import (
    CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP, CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
)

csu_c11_patient_group_study_phase_group_study_schedule_group = CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP(  # STUDY SCHEDULE - Segment group for CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP - STUDY PHASE consisting of CSS|None, STUDY OBSERVATION, STUDY PHARM
    clinical_study_data_schedule_segment=None,  # CSS(...) 
    study_observation=csu_c11_patient_group_study_phase_group_study_schedule_group_study_observation_group,  # CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP(...)  # Required.
    study_pharm=csu_c11_patient_group_study_phase_group_study_schedule_group_study_pharm_group,  # CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP TEMPLATE-----
"""


class CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP"""
    _hl7_name = """STUDY SCHEDULE"""
    _hl7_description = """Segment group for CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP - STUDY PHASE consisting of CSS|None, STUDY OBSERVATION, STUDY PHARM"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("O", "R", "R")
    _c_aliases = ("10", "None", "None")
    _c_components = (CSS, CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP, CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP)
    _c_name = ("CSS", "STUDY OBSERVATION", "STUDY PHARM")
    _c_is_group = (False, True, True)
    _c_attrs = ("clinical_study_data_schedule_segment", "study_observation", "study_pharm",)
    # fmt: on

    def __init__(
        self,
        study_observation: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
        | tuple[
            CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP,
            ...,
        ],  #  Required. (ORC.11, OBR.12, OBX.15, ...)
        study_pharm: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP
        | tuple[
            CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP,
            ...,
        ],  #  Required. (ORC.16, ...)
        clinical_study_data_schedule_segment: CSS | None = None,  #  CSS.10
    ):
        """
        None - `CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP>`_
        Segment group for CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP - STUDY PHASE consisting of CSS|None, STUDY OBSERVATION, STUDY PHARM

        :param clinical_study_data_schedule_segment: Clinical Study Data Schedule Segment (id: CSS | seq: 10 | use: O | rpt: 1)
        :param study_observation: Study Observation segment group: [ORC|None, OBR, TIMING QTY|None, OBX] (id: STUDY OBSERVATION | seq: 11, 12, None, 15 | use: R | rpt: *)
        :param study_pharm: Study Pharm segment group: [ORC|None, RX ADMIN] (id: STUDY PHARM | seq: 16, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.clinical_study_data_schedule_segment = clinical_study_data_schedule_segment
        self.study_observation = study_observation
        self.study_pharm = study_pharm

    @property  # get CSS.10
    def clinical_study_data_schedule_segment(self) -> CSS | None:
        """
        id: CSS | use: O | rpt: 1 | seq: 10
        ---
        return_type: CSS.10: Clinical Study Data Schedule Segment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSS
        """
        return self._c_data[0][0]

    @clinical_study_data_schedule_segment.setter  # set CSS.10
    def clinical_study_data_schedule_segment(self, css: CSS | None):
        """
        id: CSS | use: O | rpt: 1 | seq: 10
        ---
        param_type: CSS.10: Clinical Study Data Schedule Segment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSS
        """
        self._c_data[0] = (css,)

    @property  # get STUDY OBSERVATION
    def study_observation(
        self,
    ) -> tuple[
        CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP,
        ...,
    ]:
        """
        id: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
        """
        return self._c_data[1]

    @study_observation.setter  # set STUDY OBSERVATION
    def study_observation(
        self,
        study_observation: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
        | tuple[
            CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP,
            ...,
        ],
    ):
        """
        id: STUDY OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP.None | tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
        """
        if isinstance(study_observation, tuple):
            self._c_data[1] = study_observation
        else:
            self._c_data[1] = (study_observation,)

    @property  # get STUDY PHARM
    def study_pharm(
        self,
    ) -> tuple[
        CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP,
        ...,
    ]:
        """
        id: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP
        """
        return self._c_data[2]

    @study_pharm.setter  # set STUDY PHARM
    def study_pharm(
        self,
        study_pharm: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP
        | tuple[
            CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP,
            ...,
        ],
    ):
        """
        id: STUDY PHARM SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP.None | tuple[CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C11_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP
        """
        if isinstance(study_pharm, tuple):
            self._c_data[2] = study_pharm
        else:
            self._c_data[2] = (study_pharm,)
