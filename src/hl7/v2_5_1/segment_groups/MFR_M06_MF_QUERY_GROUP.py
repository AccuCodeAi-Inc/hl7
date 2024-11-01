from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CM0 import CM0
from ..segments.CM1 import CM1
from ..segments.MFE import MFE
from ..segments.CM2 import CM2


"""
MF QUERY - MFR_M06_MF_QUERY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MFR_M06_MF_QUERY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFR_M06_MF_QUERY_GROUP
from utils.hl7.v2_5_1.segments import (
    CM1, CM0, CM2, MFE
)

mfr_m06_mf_query_group = MFR_M06_MF_QUERY_GROUP(  # MF QUERY - Segment group for MFR_M06 - Master Files Response - Clinical study with phases and schedules master file consisting of MFE, CM0, CM1|None, CM2|None
    master_file_entry=mfe,  # MFE(...)  # Required.
    clinical_study_master=cm0,  # CM0(...)  # Required.
    clinical_study_phase_master=None,  # CM1(...) 
    clinical_study_schedule_master=None,  # CM2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MFR_M06_MF_QUERY_GROUP TEMPLATE-----
"""


class MFR_M06_MF_QUERY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MFR_M06_MF_QUERY_GROUP"""
    _hl7_name = """MF QUERY"""
    _hl7_description = """Segment group for MFR_M06 - Master Files Response - Clinical study with phases and schedules master file consisting of MFE, CM0, CM1|None, CM2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M06_MF_QUERY_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("R", "R", "O", "O")
    _c_aliases = ("9", "10", "11", "12")
    _c_components = (MFE, CM0, CM1, CM2)
    _c_name = ("MFE", "CM0", "CM1", "CM2")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("master_file_entry", "clinical_study_master", "clinical_study_phase_master", "clinical_study_schedule_master",)
    # fmt: on

    def __init__(
        self,
        master_file_entry: MFE,  #  Required. MFE.9
        clinical_study_master: CM0,  #  Required. CM0.10
        clinical_study_phase_master: CM1 | tuple[CM1, ...] | None = None,  #  CM1.11
        clinical_study_schedule_master: CM2 | tuple[CM2, ...] | None = None,  #  CM2.12
    ):
        """
        None - `MFR_M06_MF_QUERY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFR_M06_MF_QUERY_GROUP>`_
        Segment group for MFR_M06 - Master Files Response - Clinical study with phases and schedules master file consisting of MFE, CM0, CM1|None, CM2|None

        :param master_file_entry: Master File Entry (id: MFE | seq: 9 | use: R | rpt: 1)
        :param clinical_study_master: Clinical Study Master (id: CM0 | seq: 10 | use: R | rpt: 1)
        :param clinical_study_phase_master: Clinical Study Phase Master (id: CM1 | seq: 11 | use: O | rpt: *)
        :param clinical_study_schedule_master: Clinical Study Schedule Master (id: CM2 | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.master_file_entry = master_file_entry
        self.clinical_study_master = clinical_study_master
        self.clinical_study_phase_master = clinical_study_phase_master
        self.clinical_study_schedule_master = clinical_study_schedule_master

    @property  # get MFE.9
    def master_file_entry(self) -> MFE:
        """
        id: MFE | use: R | rpt: 1 | seq: 9
        ---
        return_type: MFE.9: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        return self._c_data[0][0]

    @master_file_entry.setter  # set MFE.9
    def master_file_entry(self, mfe: MFE):
        """
        id: MFE | use: R | rpt: 1 | seq: 9
        ---
        param_type: MFE.9: Master File Entry
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFE
        """
        self._c_data[0] = (mfe,)

    @property  # get CM0.10
    def clinical_study_master(self) -> CM0:
        """
        id: CM0 | use: R | rpt: 1 | seq: 10
        ---
        return_type: CM0.10: Clinical Study Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM0
        """
        return self._c_data[1][0]

    @clinical_study_master.setter  # set CM0.10
    def clinical_study_master(self, cm0: CM0):
        """
        id: CM0 | use: R | rpt: 1 | seq: 10
        ---
        param_type: CM0.10: Clinical Study Master
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM0
        """
        self._c_data[1] = (cm0,)

    @property  # get CM1
    def clinical_study_phase_master(self) -> tuple[CM1, ...] | tuple[None]:
        """
        id: CM1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[CM1, ...]: (Clinical Study Phase Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM1
        """
        return self._c_data[2]

    @clinical_study_phase_master.setter  # set CM1
    def clinical_study_phase_master(self, cm1: CM1 | tuple[CM1, ...] | None):
        """
        id: CM1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: CM1.11 | tuple[CM1, ...]: (Clinical Study Phase Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM1
        """
        if isinstance(cm1, tuple):
            self._c_data[2] = cm1
        else:
            self._c_data[2] = (cm1,)

    @property  # get CM2
    def clinical_study_schedule_master(self) -> tuple[CM2, ...] | tuple[None]:
        """
        id: CM2 SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[CM2, ...]: (Clinical Study Schedule Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2
        """
        return self._c_data[3]

    @clinical_study_schedule_master.setter  # set CM2
    def clinical_study_schedule_master(self, cm2: CM2 | tuple[CM2, ...] | None):
        """
        id: CM2 SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: CM2.12 | tuple[CM2, ...]: (Clinical Study Schedule Master, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CM2
        """
        if isinstance(cm2, tuple):
            self._c_data[3] = cm2
        else:
            self._c_data[3] = (cm2,)
