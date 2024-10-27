from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CM0 import CM0
from ..segments.MFE import MFE
from ..segment_groups.MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP import (
    MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP,
)


"""
MF CLIN STUDY - MFN_M06_MF_CLIN_STUDY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M06_MF_CLIN_STUDY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M06_MF_CLIN_STUDY_GROUP
from utils.hl7.v2_5_1.segments import (
    MFE, CM0
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
)

mfn_m06_mf_clin_study_group = MFN_M06_MF_CLIN_STUDY_GROUP(  # MF CLIN STUDY - Segment group for MFN_M06 - Master files notification - Clinical study with phases and schedules master file consisting of MFE, CM0, MF PHASE SCHED DETAIL|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    clinical_study_master=cm0,  # CM0(...)  # Required.
    mf_phase_sched_detail=None,  # MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M06_MF_CLIN_STUDY_GROUP TEMPLATE-----
"""


class MFN_M06_MF_CLIN_STUDY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M06_MF_CLIN_STUDY_GROUP"""
    _hl7_name = """MF CLIN STUDY"""
    _hl7_description = """Segment group for MFN_M06 - Master files notification - Clinical study with phases and schedules master file consisting of MFE, CM0, MF PHASE SCHED DETAIL|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M06_MF_CLIN_STUDY_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("4", "5", "None")
    _c_components = (MFE, CM0, MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP)
    _c_name = ("MFE", "CM0", "MF PHASE SCHED DETAIL")
    _c_is_group = (False, False, True)
    _c_attrs = ("master_file_entry", "clinical_study_master", "mf_phase_sched_detail",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        clinical_study_master: CM0,  #  Required. CM0.5
        mf_phase_sched_detail: MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
        | tuple[MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP, ...]
        | None = None,  #  (CM1.6, CM2.7, ...)
    ):
        """
        None - `MFN_M06_MF_CLIN_STUDY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M06_MF_CLIN_STUDY_GROUP>`_
        Segment group for MFN_M06 - Master files notification - Clinical study with phases and schedules master file consisting of MFE, CM0, MF PHASE SCHED DETAIL|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param clinical_study_master: Clinical Study Master (id: CM0 | seq: 5 | use: R | rpt: 1)
        :param mf_phase_sched_detail: Mf Phase Sched Detail segment group: [CM1, CM2|None] (id: MF PHASE SCHED DETAIL | seq: 6, 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.master_file_entry = master_file_entry
        self.clinical_study_master = clinical_study_master
        self.mf_phase_sched_detail = mf_phase_sched_detail

    @property  # get MFE.4
    def master_file_entry(self) -> MFE:
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        return_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[0][0]

    @master_file_entry.setter  # set MFE.4
    def master_file_entry(self, mfe: MFE):
        """
        id: MFE | use: R | rpt: 1 | seq: 4
        ---
        param_type: MFE.4: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        self._c_data[0] = (mfe,)

    @property  # get CM0.5
    def clinical_study_master(self) -> CM0:
        """
        id: CM0 | use: R | rpt: 1 | seq: 5
        ---
        return_type: CM0.5: Clinical Study Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM0
        """
        return self._c_data[1][0]

    @clinical_study_master.setter  # set CM0.5
    def clinical_study_master(self, cm0: CM0):
        """
        id: CM0 | use: R | rpt: 1 | seq: 5
        ---
        param_type: CM0.5: Clinical Study Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM0
        """
        self._c_data[1] = (cm0,)

    @property  # get MF PHASE SCHED DETAIL
    def mf_phase_sched_detail(
        self,
    ) -> (
        tuple[MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP, ...]
        | tuple[None]
    ):
        """
        id: MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
        """
        return self._c_data[2]

    @mf_phase_sched_detail.setter  # set MF PHASE SCHED DETAIL
    def mf_phase_sched_detail(
        self,
        mf_phase_sched_detail: MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
        | tuple[MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP, ...]
        | None,
    ):
        """
        id: MF PHASE SCHED DETAIL SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP.None | tuple[MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M06_MF_CLIN_STUDY_GROUP_MF_PHASE_SCHED_DETAIL_GROUP
        """
        if isinstance(mf_phase_sched_detail, tuple):
            self._c_data[2] = mf_phase_sched_detail
        else:
            self._c_data[2] = (mf_phase_sched_detail,)
