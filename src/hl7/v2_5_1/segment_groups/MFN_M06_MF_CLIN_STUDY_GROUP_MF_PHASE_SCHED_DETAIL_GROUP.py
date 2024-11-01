from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CM1 import CM1
from ..segments.CM2 import CM2


"""
MF PHASE SCHED DETAIL - MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    CM2, CM1
)

mfn_m06_mf_clin_study_group_mf_phase_sched_detail_group = MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP(  # MF PHASE SCHED DETAIL - Segment group for MFN_M06_MF_CLIN_STUDY_GROUP - MF CLIN STUDY consisting of CM1, CM2|None
    clinical_study_phase_master=cm1,  # CM1(...)  # Required.
    clinical_study_schedule_master=None,  # CM2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP TEMPLATE-----
"""


class MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP"""
    _hl7_name = """MF PHASE SCHED DETAIL"""
    _hl7_description = """Segment group for MFN_M06_MF_CLIN_STUDY_GROUP - MF CLIN STUDY consisting of CM1, CM2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "7")
    _c_components = (CM1, CM2)
    _c_name = ("CM1", "CM2")
    _c_is_group = (False, False)
    _c_attrs = ("clinical_study_phase_master", "clinical_study_schedule_master",)
    # fmt: on

    def __init__(
        self,
        clinical_study_phase_master: CM1,  #  Required. CM1.6
        clinical_study_schedule_master: CM2 | tuple[CM2, ...] | None = None,  #  CM2.7
    ):
        """
        None - `MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP>`_
        Segment group for MFN_M06_MF_CLIN_STUDY_GROUP - MF CLIN STUDY consisting of CM1, CM2|None

        :param clinical_study_phase_master: Clinical Study Phase Master (id: CM1 | seq: 6 | use: R | rpt: 1)
        :param clinical_study_schedule_master: Clinical Study Schedule Master (id: CM2 | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.clinical_study_phase_master = clinical_study_phase_master
        self.clinical_study_schedule_master = clinical_study_schedule_master

    @property  # get CM1.6
    def clinical_study_phase_master(self) -> CM1:
        """
        id: CM1 | use: R | rpt: 1 | seq: 6
        ---
        return_type: CM1.6: Clinical Study Phase Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM1
        """
        return self._c_data[0][0]

    @clinical_study_phase_master.setter  # set CM1.6
    def clinical_study_phase_master(self, cm1: CM1):
        """
        id: CM1 | use: R | rpt: 1 | seq: 6
        ---
        param_type: CM1.6: Clinical Study Phase Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM1
        """
        self._c_data[0] = (cm1,)

    @property  # get CM2
    def clinical_study_schedule_master(self) -> tuple[CM2, ...] | tuple[None]:
        """
        id: CM2 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[CM2, ...]: (Clinical Study Schedule Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2
        """
        return self._c_data[1]

    @clinical_study_schedule_master.setter  # set CM2
    def clinical_study_schedule_master(self, cm2: CM2 | tuple[CM2, ...] | None):
        """
        id: CM2 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: CM2.7 | tuple[CM2, ...]: (Clinical Study Schedule Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2
        """
        if isinstance(cm2, tuple):
            self._c_data[1] = cm2
        else:
            self._c_data[1] = (cm2,)
