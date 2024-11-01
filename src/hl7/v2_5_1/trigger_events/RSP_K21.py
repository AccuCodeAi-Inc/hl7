from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.RSP_K21_QUERY_RESPONSE_GROUP import RSP_K21_QUERY_RESPONSE_GROUP
from ..segments.SFT import SFT
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.QPD import QPD
from ..segments.QAK import QAK


"""
Get Person Demographics Response - RSP_K21
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RSP_K21 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K21
from utils.hl7.v2_5_1.segments import (
    ERR, DSC, QPD, MSA, SFT, MSH, QAK
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_K21_QUERY_RESPONSE_GROUP
)

rsp_k21 = RSP_K21(  #  - This query/response is designed for interaction between a client system and an MPI (Master Person Index)
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=qak,  # QAK(...)  # Required.
    query_parameter_definition=qpd,  # QPD(...)  # Required.
    query_response=None,  # RSP_K21_QUERY_RESPONSE_GROUP(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::RSP_K21 TEMPLATE-----
"""


class RSP_K21(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RSP_K21"""
    _hl7_name = """Get Person Demographics Response"""
    _hl7_description = """This query/response is designed for interaction between a client system and an MPI (Master Person Index)"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K21"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 1)
    _c_usage = ("R", "O", "R", "O", "R", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "None", "11")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QPD, RSP_K21_QUERY_RESPONSE_GROUP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QPD", "QUERY RESPONSE", "DSC")
    _c_is_group = (False, False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "query_parameter_definition", "query_response", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        query_acknowledgment: QAK,  #  Required. QAK.5
        query_parameter_definition: QPD,  #  Required. QPD.6
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | None = None,  #  ERR.4
        query_response: RSP_K21_QUERY_RESPONSE_GROUP
        | None = None,  #  PID.7, PD1.8, NK1.9, QRI.10
        continuation_pointer: DSC | None = None,  #  DSC.11
    ):
        """
         - `RSP_K21 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K21>`_
        This query/response is designed for interaction between a client system and an MPI (Master Person Index). The query consists of an identifier for a person, and the response the demographics for that person

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: 1)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: R | rpt: 1)
        :param query_parameter_definition: Query Parameter Definition (id: QPD | seq: 6 | use: R | rpt: 1)
        :param query_response: Query Response segment group: [PID, PD1|None, NK1|None, QRI] (id: QUERY RESPONSE | seq: 7, 8, 9, 10 | use: O | rpt: 1)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 11 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.query_parameter_definition = query_parameter_definition
        self.query_response = query_response
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

    @property  # get QPD.6
    def query_parameter_definition(self) -> QPD:
        """
        id: QPD | use: R | rpt: 1 | seq: 6
        ---
        return_type: QPD.6: Query Parameter Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QPD
        """
        return self._c_data[5][0]

    @query_parameter_definition.setter  # set QPD.6
    def query_parameter_definition(self, qpd: QPD):
        """
        id: QPD | use: R | rpt: 1 | seq: 6
        ---
        param_type: QPD.6: Query Parameter Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QPD
        """
        self._c_data[5] = (qpd,)

    @property  # get RSP_K21_QUERY_RESPONSE_GROUP.None
    def query_response(self) -> RSP_K21_QUERY_RESPONSE_GROUP | None:
        """
        id: RSP_K21_QUERY_RESPONSE_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_K21_QUERY_RESPONSE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K21_QUERY_RESPONSE_GROUP
        """
        return self._c_data[6][0]

    @query_response.setter  # set RSP_K21_QUERY_RESPONSE_GROUP.None
    def query_response(self, query_response: RSP_K21_QUERY_RESPONSE_GROUP | None):
        """
        id: RSP_K21_QUERY_RESPONSE_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_K21_QUERY_RESPONSE_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K21_QUERY_RESPONSE_GROUP
        """
        self._c_data[6] = (query_response,)

    @property  # get DSC.11
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 11
        ---
        return_type: DSC.11: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[7][0]

    @continuation_pointer.setter  # set DSC.11
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 11
        ---
        param_type: DSC.11: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[7] = (dsc,)
