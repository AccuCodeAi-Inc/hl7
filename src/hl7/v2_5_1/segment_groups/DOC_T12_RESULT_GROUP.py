from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.EVN import EVN
from ..segments.PV1 import PV1
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.TXA import TXA


"""
RESULT - DOC_T12_RESULT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DOC_T12_RESULT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DOC_T12_RESULT_GROUP
from utils.hl7.v2_5_1.segments import (
    PV1, TXA, PID, EVN, OBX
)

doc_t12_result_group = DOC_T12_RESULT_GROUP(  # RESULT - Segment group for DOC_T12 - Document response consisting of EVN|None, PID, PV1, TXA, OBX|None
    event_type=None,  # EVN(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=pv1,  # PV1(...)  # Required.
    transcription_document_header=txa,  # TXA(...)  # Required.
    observation_or_result=None,  # OBX(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DOC_T12_RESULT_GROUP TEMPLATE-----
"""


class DOC_T12_RESULT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DOC_T12_RESULT_GROUP"""
    _hl7_name = """RESULT"""
    _hl7_description = """Segment group for DOC_T12 - Document response consisting of EVN|None, PID, PV1, TXA, OBX|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DOC_T12_RESULT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1, 65535)
    _c_usage = ("O", "R", "R", "R", "O")
    _c_aliases = ("6", "7", "8", "9", "10")
    _c_components = (EVN, PID, PV1, TXA, OBX)
    _c_name = ("EVN", "PID", "PV1", "TXA", "OBX")
    _c_is_group = (False, False, False, False, False)
    _c_attrs = ("event_type", "patient_identification", "patient_visit", "transcription_document_header", "observation_or_result",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        patient_visit: PV1,  #  Required. PV1.8
        transcription_document_header: TXA,  #  Required. TXA.9
        event_type: EVN | None = None,  #  EVN.6
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.10
    ):
        """
        None - `DOC_T12_RESULT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DOC_T12_RESULT_GROUP>`_
        Segment group for DOC_T12 - Document response consisting of EVN|None, PID, PV1, TXA, OBX|None

        :param event_type: Event Type (id: EVN | seq: 6 | use: O | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 8 | use: R | rpt: 1)
        :param transcription_document_header: Transcription Document Header (id: TXA | seq: 9 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 10 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.transcription_document_header = transcription_document_header
        self.observation_or_result = observation_or_result

    @property  # get EVN.6
    def event_type(self) -> EVN | None:
        """
        id: EVN | use: O | rpt: 1 | seq: 6
        ---
        return_type: EVN.6: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[0][0]

    @event_type.setter  # set EVN.6
    def event_type(self, evn: EVN | None):
        """
        id: EVN | use: O | rpt: 1 | seq: 6
        ---
        param_type: EVN.6: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[0] = (evn,)

    @property  # get PID.7
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        return_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[1][0]

    @patient_identification.setter  # set PID.7
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        param_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[1] = (pid,)

    @property  # get PV1.8
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 8
        ---
        return_type: PV1.8: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[2][0]

    @patient_visit.setter  # set PV1.8
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 8
        ---
        param_type: PV1.8: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[2] = (pv1,)

    @property  # get TXA.9
    def transcription_document_header(self) -> TXA:
        """
        id: TXA | use: R | rpt: 1 | seq: 9
        ---
        return_type: TXA.9: Transcription Document Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TXA
        """
        return self._c_data[3][0]

    @transcription_document_header.setter  # set TXA.9
    def transcription_document_header(self, txa: TXA):
        """
        id: TXA | use: R | rpt: 1 | seq: 9
        ---
        param_type: TXA.9: Transcription Document Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TXA
        """
        self._c_data[3] = (txa,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[4]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: OBX.10 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[4] = obx
        else:
            self._c_data[4] = (obx,)
