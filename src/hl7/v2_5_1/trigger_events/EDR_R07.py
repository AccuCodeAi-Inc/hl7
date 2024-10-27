from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.ERR import ERR
from ..segments.DSP import DSP
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.DSC import DSC
from ..segments.QAK import QAK


"""
Enhanced Display Response - EDR_R07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::EDR_R07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EDR_R07
from utils.hl7.v2_5_1.segments import (
    QAK, ERR, MSA, DSC, DSP, MSH, SFT
)

edr_r07 = EDR_R07(  #  - The response to the EQQ could be tabular or display
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=qak,  # QAK(...)  # Required.
    display_data=dsp,  # DSP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::EDR_R07 TEMPLATE-----
"""


class EDR_R07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """EDR_R07"""
    _hl7_name = """Enhanced Display Response"""
    _hl7_description = """The response to the EQQ could be tabular or display"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EDR_R07"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7")
    _c_components = (MSH, SFT, MSA, ERR, QAK, DSP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "DSP", "DSC")
    _c_is_group = (False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "display_data", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        query_acknowledgment: QAK,  #  Required. QAK.5
        display_data: DSP | tuple[DSP, ...],  #  Required. DSP.6
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | None = None,  #  ERR.4
        continuation_pointer: DSC | None = None,  #  DSC.7
    ):
        """
         - `EDR_R07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EDR_R07>`_
        The response to the EQQ could be tabular or display. The segment pattern response (the ERP) is invalid given that there is no way to specify the desired segment pattern in the query defining segment, EQL.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: 1)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: R | rpt: 1)
        :param display_data: Display Data (id: DSP | seq: 6 | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 7 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
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
    def query_acknowledgment(self) -> QAK:
        """
        id: QAK | use: R | rpt: 1 | seq: 5
        ---
        return_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[4][0]

    @query_acknowledgment.setter  # set QAK.5
    def query_acknowledgment(self, qak: QAK):
        """
        id: QAK | use: R | rpt: 1 | seq: 5
        ---
        param_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[4] = (qak,)

    @property  # get DSP
    def display_data(self) -> tuple[DSP, ...]:
        """
        id: DSP SEGMENT GROUP | use: R | rpt: * | seq: 6
        ---
        return_type: tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        return self._c_data[5]

    @display_data.setter  # set DSP
    def display_data(self, dsp: DSP | tuple[DSP, ...]):
        """
        id: DSP SEGMENT GROUP | use: R | rpt: * | seq: 6
        ---
        param_type: DSP.6 | tuple[DSP, ...]: (Display Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSP
        """
        if isinstance(dsp, tuple):
            self._c_data[5] = dsp
        else:
            self._c_data[5] = (dsp,)

    @property  # get DSC.7
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 7
        ---
        return_type: DSC.7: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[6][0]

    @continuation_pointer.setter  # set DSC.7
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 7
        ---
        param_type: DSC.7: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[6] = (dsc,)
