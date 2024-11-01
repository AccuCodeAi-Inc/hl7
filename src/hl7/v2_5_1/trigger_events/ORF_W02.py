from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.MSA import MSA
from ..segment_groups.ORF_W02_RESPONSE_GROUP import ORF_W02_RESPONSE_GROUP
from ..segments.QAK import QAK
from ..segments.QRF import QRF
from ..segments.DSC import DSC
from ..segments.SFT import SFT


"""
Waveform result, response to query - ORF_W02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ORF_W02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORF_W02
from utils.hl7.v2_5_1.segments import (
    QAK, QRD, SFT, QRF, MSA, ERR, DSC, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    ORF_W02_RESPONSE_GROUP
)

orf_w02 = ORF_W02(  #  - The W02 trigger event identifies QRF messages which are a response to a QRY message specifying an immediate mode query for waveform results/observations with record-oriented format
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    response=orf_w02_response_group,  # ORF_W02_RESPONSE_GROUP(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=None,  # QAK(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::ORF_W02 TEMPLATE-----
"""


class ORF_W02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ORF_W02"""
    _hl7_name = """Waveform result, response to query"""
    _hl7_description = """The W02 trigger event identifies QRF messages which are a response to a QRY message specifying an immediate mode query for waveform results/observations with record-oriented format"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 65535, 1, 1)
    _c_usage = ("R", "O", "R", "R", "O", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "None", "15", "16", "17")
    _c_components = (MSH, SFT, MSA, QRD, QRF, ORF_W02_RESPONSE_GROUP, ERR, QAK, DSC)
    _c_name = ("MSH", "SFT", "MSA", "QRD", "QRF", "RESPONSE", "ERR", "QAK", "DSC")
    _c_is_group = (False, False, False, False, False, True, False, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "original_style_query_definition", "original_style_query_filter", "response", "error", "query_acknowledgment", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        original_style_query_definition: QRD,  #  Required. QRD.4
        response: ORF_W02_RESPONSE_GROUP
        | tuple[ORF_W02_RESPONSE_GROUP, ...],  #  Required. (, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        original_style_query_filter: QRF | None = None,  #  QRF.5
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.15
        query_acknowledgment: QAK | None = None,  #  QAK.16
        continuation_pointer: DSC | None = None,  #  DSC.17
    ):
        """
         - `ORF_W02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02>`_
        The W02 trigger event identifies QRF messages which are a response to a QRY message specifying an immediate mode query for waveform results/observations with record-oriented format.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 4 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 5 | use: O | rpt: 1)
        :param response: Response segment group: [PATIENT|None, ORDER] (id: RESPONSE | seq: None, None | use: R | rpt: *)
        :param error: Error (id: ERR | seq: 15 | use: O | rpt: *)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 16 | use: O | rpt: 1)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 17 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.response = response
        self.error = error
        self.query_acknowledgment = query_acknowledgment
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

    @property  # get MSA.3
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        param_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[2] = (msa,)

    @property  # get QRD.4
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 4
        ---
        return_type: QRD.4: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[3][0]

    @original_style_query_definition.setter  # set QRD.4
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 4
        ---
        param_type: QRD.4: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[3] = (qrd,)

    @property  # get QRF.5
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 5
        ---
        return_type: QRF.5: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[4][0]

    @original_style_query_filter.setter  # set QRF.5
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 5
        ---
        param_type: QRF.5: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[4] = (qrf,)

    @property  # get RESPONSE
    def response(self) -> tuple[ORF_W02_RESPONSE_GROUP, ...]:
        """
        id: ORF_W02_RESPONSE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORF_W02_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP
        """
        return self._c_data[5]

    @response.setter  # set RESPONSE
    def response(
        self, response: ORF_W02_RESPONSE_GROUP | tuple[ORF_W02_RESPONSE_GROUP, ...]
    ):
        """
        id: RESPONSE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORF_W02_RESPONSE_GROUP.None | tuple[ORF_W02_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP
        """
        if isinstance(response, tuple):
            self._c_data[5] = response
        else:
            self._c_data[5] = (response,)

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[6]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: ERR.15 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[6] = err
        else:
            self._c_data[6] = (err,)

    @property  # get QAK.16
    def query_acknowledgment(self) -> QAK | None:
        """
        id: QAK | use: O | rpt: 1 | seq: 16
        ---
        return_type: QAK.16: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[7][0]

    @query_acknowledgment.setter  # set QAK.16
    def query_acknowledgment(self, qak: QAK | None):
        """
        id: QAK | use: O | rpt: 1 | seq: 16
        ---
        param_type: QAK.16: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[7] = (qak,)

    @property  # get DSC.17
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 17
        ---
        return_type: DSC.17: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[8][0]

    @continuation_pointer.setter  # set DSC.17
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 17
        ---
        param_type: DSC.17: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[8] = (dsc,)
