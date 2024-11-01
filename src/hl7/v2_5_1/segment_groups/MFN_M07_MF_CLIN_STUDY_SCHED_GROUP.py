from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CM2 import CM2
from ..segments.CM0 import CM0
from ..segments.MFE import MFE


"""
MF CLIN STUDY SCHED - MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFN_M07_MF_CLIN_STUDY_SCHED_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
from utils.hl7.v2_5_1.segments import (
    CM2, MFE, CM0
)

mfn_m07_mf_clin_study_sched_group = MFN_M07_MF_CLIN_STUDY_SCHED_GROUP(  # MF CLIN STUDY SCHED - Segment group for MFN_M07 - Master files notification - Clinical study without phases but with schedules master file consisting of MFE, CM0, CM2|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    clinical_study_master=cm0,  # CM0(...)  # Required.
    clinical_study_schedule_master=None,  # CM2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFN_M07_MF_CLIN_STUDY_SCHED_GROUP TEMPLATE-----
"""


class MFN_M07_MF_CLIN_STUDY_SCHED_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFN_M07_MF_CLIN_STUDY_SCHED_GROUP"""
    _hl7_name = """MF CLIN STUDY SCHED"""
    _hl7_description = """Segment group for MFN_M07 - Master files notification - Clinical study without phases but with schedules master file consisting of MFE, CM0, CM2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M07_MF_CLIN_STUDY_SCHED_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("4", "5", "6")
    _c_components = (MFE, CM0, CM2)
    _c_name = ("MFE", "CM0", "CM2")
    _c_is_group = (False, False, False)
    _c_attrs = ("master_file_entry", "clinical_study_master", "clinical_study_schedule_master",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.4
        clinical_study_master: CM0,  #  Required. CM0.5
        clinical_study_schedule_master: CM2 | tuple[CM2, ...] | None = None,  #  CM2.6
    ):
        """
        None - `MFN_M07_MF_CLIN_STUDY_SCHED_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M07_MF_CLIN_STUDY_SCHED_GROUP>`_
        Segment group for MFN_M07 - Master files notification - Clinical study without phases but with schedules master file consisting of MFE, CM0, CM2|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 4 | use: R | rpt: 1)
        :param clinical_study_master: Clinical Study Master (id: CM0 | seq: 5 | use: R | rpt: 1)
        :param clinical_study_schedule_master: Clinical Study Schedule Master (id: CM2 | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.master_file_entry = master_file_entry
        self.clinical_study_master = clinical_study_master
        self.clinical_study_schedule_master = clinical_study_schedule_master

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

    @property  # get CM2
    def clinical_study_schedule_master(self) -> tuple[CM2, ...] | tuple[None]:
        """
        id: CM2 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[CM2, ...]: (Clinical Study Schedule Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2
        """
        return self._c_data[2]

    @clinical_study_schedule_master.setter  # set CM2
    def clinical_study_schedule_master(self, cm2: CM2 | tuple[CM2, ...] | None):
        """
        id: CM2 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: CM2.6 | tuple[CM2, ...]: (Clinical Study Schedule Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2
        """
        if isinstance(cm2, tuple):
            self._c_data[2] = cm2
        else:
            self._c_data[2] = (cm2,)
