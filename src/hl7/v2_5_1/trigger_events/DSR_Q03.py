from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.ERR import ERR
from ..segments.QRF import QRF
from ..segments.DSP import DSP
from ..segments.QRD import QRD
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.DSC import DSC
from ..segments.QAK import QAK


"""
Deferred Response to a Query - DSR_Q03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::DSR_Q03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DSR_Q03
from utils.hl7.v2_5_1.segments import (
    QAK, ERR, MSA, DSC, DSP, QRD, MSH, SFT, QRF
)

dsr_q03 = DSR_Q03(  #  - This section is retained for backward compatibility and the framework for the existing functional queries
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=None,  # MSA(...) 
    error=None,  # ERR(...) 
    query_acknowledgment=None,  # QAK(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    display_data=dsp,  # DSP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::DSR_Q03 TEMPLATE-----
"""


class DSR_Q03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """DSR_Q03"""
    _hl7_name = """Deferred Response to a Query"""
    _hl7_description = """This section is retained for backward compatibility and the framework for the existing functional queries"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DSR_Q03"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O", "R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QRD, QRF, DSP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QRD", "QRF", "DSP", "DSC")
    _c_is_group = (False, False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "original_style_query_definition", "original_style_query_filter", "display_data", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        original_style_query_definition: QRD,  #  Required. QRD.6
        display_data: DSP | tuple[DSP, ...],  #  Required. DSP.8
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        message_acknowledgment: MSA | None = None,  #  MSA.3
        error: ERR | None = None,  #  ERR.4
        query_acknowledgment: QAK | None = None,  #  QAK.5
        original_style_query_filter: QRF | None = None,  #  QRF.7
        continuation_pointer: DSC | None = None,  #  DSC.9
    ):
        """
         - `DSR_Q03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DSR_Q03>`_
        This section is retained for backward compatibility and the framework for the existing functional queries.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: O | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: 1)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: O | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 6 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 7 | use: O | rpt: 1)
        :param display_data: Display Data (id: DSP | seq: 8 | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 9 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.display_data = display_data
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
    def message_acknowledgment(self) -> MSA | None:
        """
        id: MSA | use: O | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA | None):
        """
        id: MSA | use: O | rpt: 1 | seq: 3
        ---
        param_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[2] = (msa,)

    @property  # get ERR.4
    def error(self) -> ERR | None:
        """
        id: ERR | use: O | rpt: 1 | seq: 4
        ---
        return_type: ERR.4: Error
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[3][0]

    @error.setter  # set ERR.4
    def error(self, err: ERR | None):
        """
        id: ERR | use: O | rpt: 1 | seq: 4
        ---
        param_type: ERR.4: Error
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        self._c_data[3] = (err,)

    @property  # get QAK.5
    def query_acknowledgment(self) -> QAK | None:
        """
        id: QAK | use: O | rpt: 1 | seq: 5
        ---
        return_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[4][0]

    @query_acknowledgment.setter  # set QAK.5
    def query_acknowledgment(self, qak: QAK | None):
        """
        id: QAK | use: O | rpt: 1 | seq: 5
        ---
        param_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[4] = (qak,)

    @property  # get QRD.6
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 6
        ---
        return_type: QRD.6: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[5][0]

    @original_style_query_definition.setter  # set QRD.6
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 6
        ---
        param_type: QRD.6: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[5] = (qrd,)

    @property  # get QRF.7
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 7
        ---
        return_type: QRF.7: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[6][0]

    @original_style_query_filter.setter  # set QRF.7
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 7
        ---
        param_type: QRF.7: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[6] = (qrf,)

    @property  # get DSP
    def display_data(self) -> tuple[DSP, ...]:
        """
        id: DSP SEGMENT GROUP | use: R | rpt: * | seq: 8
        ---
        return_type: tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        return self._c_data[7]

    @display_data.setter  # set DSP
    def display_data(self, dsp: DSP | tuple[DSP, ...]):
        """
        id: DSP SEGMENT GROUP | use: R | rpt: * | seq: 8
        ---
        param_type: DSP.8 | tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        if isinstance(dsp, tuple):
            self._c_data[7] = dsp
        else:
            self._c_data[7] = (dsp,)

    @property  # get DSC.9
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 9
        ---
        return_type: DSC.9: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[8][0]

    @continuation_pointer.setter  # set DSC.9
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 9
        ---
        param_type: DSC.9: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[8] = (dsc,)