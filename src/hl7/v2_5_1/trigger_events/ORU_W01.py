from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.DSC import DSC
from ..segments.SFT import SFT
from ..segment_groups.ORU_W01_PATIENT_RESULT_GROUP import ORU_W01_PATIENT_RESULT_GROUP


"""
Waveform result, unsolicited transmission of requested information - ORU_W01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ORU_W01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORU_W01
from utils.hl7.v2_5_1.segments import (
    SFT, DSC, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    ORU_W01_PATIENT_RESULT_GROUP
)

oru_w01 = ORU_W01(  #  - The waveform response unsolicited trigger event identifies ORU messages used to transmit waveform data which are results of an ordered test or series of observations
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient_result=oru_w01_patient_result_group,  # ORU_W01_PATIENT_RESULT_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::ORU_W01 TEMPLATE-----
"""


class ORU_W01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ORU_W01"""
    _hl7_name = """Waveform result, unsolicited transmission of requested information"""
    _hl7_description = """The waveform response unsolicited trigger event identifies ORU messages used to transmit waveform data which are results of an ordered test or series of observations"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("1", "2", "None", "19")
    _c_components = (MSH, SFT, ORU_W01_PATIENT_RESULT_GROUP, DSC)
    _c_name = ("MSH", "SFT", "PATIENT RESULT", "DSC")
    _c_is_group = (False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "patient_result", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient_result: ORU_W01_PATIENT_RESULT_GROUP
        | tuple[ORU_W01_PATIENT_RESULT_GROUP, ...],  #  Required. (, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        continuation_pointer: DSC | None = None,  #  DSC.19
    ):
        """
         - `ORU_W01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01>`_
        The waveform response unsolicited trigger event identifies ORU messages used to transmit waveform data which are results of an ordered test or series of observations. The W01 trigger event may also be used to identify ORU messages sent as the eventual response to a QRY message specifying a deferred mode query for waveform results/observations with record-oriented format (similar to the deferred response display mode DSR message type described in Chapter 2).  One or more ORU messages with the W01 trigger event  may result from this type of QRY message.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient_result: Patient Result segment group: [PATIENT|None, ORDER OBSERVATION] (id: PATIENT RESULT | seq: None, None | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 19 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.patient_result = patient_result
        self.continuation_pointer = continuation_pointer

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

    @property  # get PATIENT RESULT
    def patient_result(self) -> tuple[ORU_W01_PATIENT_RESULT_GROUP, ...]:
        """
        id: ORU_W01_PATIENT_RESULT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORU_W01_PATIENT_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP
        """
        return self._c_data[2]

    @patient_result.setter  # set PATIENT RESULT
    def patient_result(
        self,
        patient_result: ORU_W01_PATIENT_RESULT_GROUP
        | tuple[ORU_W01_PATIENT_RESULT_GROUP, ...],
    ):
        """
        id: PATIENT RESULT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORU_W01_PATIENT_RESULT_GROUP.None | tuple[ORU_W01_PATIENT_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP
        """
        if isinstance(patient_result, tuple):
            self._c_data[2] = patient_result
        else:
            self._c_data[2] = (patient_result,)

    @property  # get DSC.19
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 19
        ---
        return_type: DSC.19: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[3][0]

    @continuation_pointer.setter  # set DSC.19
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 19
        ---
        param_type: DSC.19: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[3] = (dsc,)
