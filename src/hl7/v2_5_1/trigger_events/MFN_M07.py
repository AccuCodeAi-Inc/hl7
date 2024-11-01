from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.MFN_M07_MF_CLIN_STUDY_SCHED_GROUP import (
    MFN_M07_MF_CLIN_STUDY_SCHED_GROUP,
)
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.MFI import MFI


"""
Master files notification - Clinical study without phases but with schedules master file - MFN_M07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MFN_M07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MFN_M07
from utils.hl7.v2_5_1.segments import (
    MFI, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
)

mfn_m07 = MFN_M07(  #  - The CM0 (Clinical Study Master), CM1 (Clinical Study Phase), and CM2 (Clinical Study Schedule) segments can be used to transmit master files information between systems
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    master_file_identification=mfi,  # MFI(...)  # Required.
    mf_clin_study_sched=mfn_m07_mf_clin_study_sched_group,  # MFN_M07_MF_CLIN_STUDY_SCHED_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::MFN_M07 TEMPLATE-----
"""


class MFN_M07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MFN_M07"""
    _hl7_name = """Master files notification - Clinical study without phases but with schedules master file"""
    _hl7_description = """The CM0 (Clinical Study Master), CM1 (Clinical Study Phase), and CM2 (Clinical Study Schedule) segments can be used to transmit master files information between systems"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M07"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "None")
    _c_components = (MSH, SFT, MFI, MFN_M07_MF_CLIN_STUDY_SCHED_GROUP)
    _c_name = ("MSH", "SFT", "MFI", "MF CLIN STUDY SCHED")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "master_file_identification", "mf_clin_study_sched",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        master_file_identification: MFI,  #  Required. MFI.3
        mf_clin_study_sched: MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
        | tuple[
            MFN_M07_MF_CLIN_STUDY_SCHED_GROUP, ...
        ],  #  Required. (MFE.4, CM0.5, CM2.6, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
                 - `MFN_M07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MFN_M07>`_
                The CM0 (Clinical Study Master), CM1 (Clinical Study Phase), and CM2 (Clinical Study Schedule) segments can be used to transmit master files information between systems. The CM0 segment contains the information about the study itself; the CM1 contains the information about one phase of the study identified in the preceding CM0; and the CM2 contains the information about the scheduled time points for the preceding study or phase-related treatment or evaluation events.  When these segments are used in an MFN message, the abstract definition is described below.

        MFN message for Clinical Study without phases but with schedules.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param master_file_identification: Master File Identification (id: MFI | seq: 3 | use: R | rpt: 1)
                :param mf_clin_study_sched: Mf Clin Study Sched segment group: [MFE, CM0, CM2|None] (id: MF CLIN STUDY SCHED | seq: 4, 5, 6 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.master_file_identification = master_file_identification
        self.mf_clin_study_sched = mf_clin_study_sched

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get MFI.3
    def master_file_identification(self) -> MFI:
        """
        id: MFI | use: R | rpt: 1 | seq: 3
        ---
        return_type: MFI.3: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        return self._c_data[2][0]

    @master_file_identification.setter  # set MFI.3
    def master_file_identification(self, mfi: MFI):
        """
        id: MFI | use: R | rpt: 1 | seq: 3
        ---
        param_type: MFI.3: Master File Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFI
        """
        self._c_data[2] = (mfi,)

    @property  # get MF CLIN STUDY SCHED
    def mf_clin_study_sched(self) -> tuple[MFN_M07_MF_CLIN_STUDY_SCHED_GROUP, ...]:
        """
        id: MFN_M07_MF_CLIN_STUDY_SCHED_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[MFN_M07_MF_CLIN_STUDY_SCHED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
        """
        return self._c_data[3]

    @mf_clin_study_sched.setter  # set MF CLIN STUDY SCHED
    def mf_clin_study_sched(
        self,
        mf_clin_study_sched: MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
        | tuple[MFN_M07_MF_CLIN_STUDY_SCHED_GROUP, ...],
    ):
        """
        id: MF CLIN STUDY SCHED SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: MFN_M07_MF_CLIN_STUDY_SCHED_GROUP.None | tuple[MFN_M07_MF_CLIN_STUDY_SCHED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MFN_M07_MF_CLIN_STUDY_SCHED_GROUP
        """
        if isinstance(mf_clin_study_sched, tuple):
            self._c_data[3] = mf_clin_study_sched
        else:
            self._c_data[3] = (mf_clin_study_sched,)
