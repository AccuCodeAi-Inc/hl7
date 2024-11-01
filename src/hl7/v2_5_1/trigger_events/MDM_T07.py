from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.MDM_T07_COMMON_ORDER_GROUP import MDM_T07_COMMON_ORDER_GROUP
from ..segments.EVN import EVN
from ..segments.PV1 import PV1
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.TXA import TXA


"""
Document edit  notification - MDM_T07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::MDM_T07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MDM_T07
from utils.hl7.v2_5_1.segments import (
    PID, SFT, EVN, MSH, PV1, TXA
)
from utils.hl7.v2_5_1.segment_groups import (
    MDM_T07_COMMON_ORDER_GROUP
)

mdm_t07 = MDM_T07(  #  - This is a notification of an edit to a document without the accompanying content

Note: The only valid use of this trigger event is for documents whose availability status is “Unavailable,” i
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=pv1,  # PV1(...)  # Required.
    common_order=None,  # MDM_T07_COMMON_ORDER_GROUP(...) 
    transcription_document_header=txa,  # TXA(...)  # Required.
)

-----END TRIGGER_EVENT::MDM_T07 TEMPLATE-----
"""


class MDM_T07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """MDM_T07"""
    _hl7_name = """Document edit  notification"""
    _hl7_description = """This is a notification of an edit to a document without the accompanying content

Note: The only valid use of this trigger event is for documents whose availability status is “Unavailable,” i"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MDM_T07"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "R", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "None", "11")
    _c_components = (MSH, SFT, EVN, PID, PV1, MDM_T07_COMMON_ORDER_GROUP, TXA)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PV1", "COMMON ORDER", "TXA")
    _c_is_group = (False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_visit", "common_order", "transcription_document_header",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.5
        transcription_document_header: TXA,  #  Required. TXA.11
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        common_order: MDM_T07_COMMON_ORDER_GROUP
        | tuple[MDM_T07_COMMON_ORDER_GROUP, ...]
        | None = None,  #  (ORC.6, OBR.9, NTE.10, ...)
    ):
        """
                 - `MDM_T07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MDM_T07>`_
                This is a notification of an edit to a document without the accompanying content

        Note: The only valid use of this trigger event is for documents whose availability status is “Unavailable,” i.e., the document has not been made available for patient care.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_visit: Patient Visit (id: PV1 | seq: 5 | use: R | rpt: 1)
                :param common_order: Common Order segment group: [ORC, TIMING|None, OBR, NTE|None] (id: COMMON ORDER | seq: 6, None, 9, 10 | use: O | rpt: *)
                :param transcription_document_header: Transcription Document Header (id: TXA | seq: 11 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.common_order = common_order
        self.transcription_document_header = transcription_document_header

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

    @property  # get EVN.3
    def event_type(self) -> EVN:
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        return_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[2][0]

    @event_type.setter  # set EVN.3
    def event_type(self, evn: EVN):
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        param_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[2] = (evn,)

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[3][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[3] = (pid,)

    @property  # get PV1.5
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 5
        ---
        return_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[4][0]

    @patient_visit.setter  # set PV1.5
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 5
        ---
        param_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[4] = (pv1,)

    @property  # get COMMON ORDER
    def common_order(self) -> tuple[MDM_T07_COMMON_ORDER_GROUP, ...] | tuple[None]:
        """
        id: MDM_T07_COMMON_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[MDM_T07_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MDM_T07_COMMON_ORDER_GROUP
        """
        return self._c_data[5]

    @common_order.setter  # set COMMON ORDER
    def common_order(
        self,
        common_order: MDM_T07_COMMON_ORDER_GROUP
        | tuple[MDM_T07_COMMON_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: COMMON ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: MDM_T07_COMMON_ORDER_GROUP.None | tuple[MDM_T07_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MDM_T07_COMMON_ORDER_GROUP
        """
        if isinstance(common_order, tuple):
            self._c_data[5] = common_order
        else:
            self._c_data[5] = (common_order,)

    @property  # get TXA.11
    def transcription_document_header(self) -> TXA:
        """
        id: TXA | use: R | rpt: 1 | seq: 11
        ---
        return_type: TXA.11: Transcription Document Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TXA
        """
        return self._c_data[6][0]

    @transcription_document_header.setter  # set TXA.11
    def transcription_document_header(self, txa: TXA):
        """
        id: TXA | use: R | rpt: 1 | seq: 11
        ---
        param_type: TXA.11: Transcription Document Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TXA
        """
        self._c_data[6] = (txa,)
