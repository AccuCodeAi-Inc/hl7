from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.RCP import RCP
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.MSA import MSA
from ..segments.QAK import QAK
from ..segment_groups.RSP_Z88_QUERY_RESPONSE_GROUP import RSP_Z88_QUERY_RESPONSE_GROUP
from ..segments.DSC import DSC
from ..segments.SFT import SFT


"""
Dispense Information Response - RSP_Z88
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RSP_Z88 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z88
from utils.hl7.v2_5_1.segments import (
    QAK, SFT, RCP, ERR, MSA, QPD, MSH, DSC
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z88_QUERY_RESPONSE_GROUP
)

rsp_z88 = RSP_Z88(  #  - The purpose of this query/response pair is to retrieve patient pharmacy dispense history information from the Server
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=qak,  # QAK(...)  # Required.
    query_parameter_definition=qpd,  # QPD(...)  # Required.
    response_control_parameter=rcp,  # RCP(...)  # Required.
    query_response=rsp_z88_query_response_group,  # RSP_Z88_QUERY_RESPONSE_GROUP(...)  # Required.
    continuation_pointer=dsc,  # DSC(...)  # Required.
)

-----END TRIGGER_EVENT::RSP_Z88 TEMPLATE-----
"""


class RSP_Z88(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RSP_Z88"""
    _hl7_name = """Dispense Information Response"""
    _hl7_description = """The purpose of this query/response pair is to retrieve patient pharmacy dispense history information from the Server"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z88"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "R", "R", "R", "R", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "None", "32")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QPD, RCP, RSP_Z88_QUERY_RESPONSE_GROUP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QPD", "RCP", "QUERY RESPONSE", "DSC")
    _c_is_group = (False, False, False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "query_parameter_definition", "response_control_parameter", "query_response", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        query_acknowledgment: QAK,  #  Required. QAK.5
        query_parameter_definition: QPD,  #  Required. QPD.6
        response_control_parameter: RCP,  #  Required. RCP.7
        query_response: RSP_Z88_QUERY_RESPONSE_GROUP
        | tuple[RSP_Z88_QUERY_RESPONSE_GROUP, ...],  #  Required. (, ...)
        continuation_pointer: DSC,  #  Required. DSC.32
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | None = None,  #  ERR.4
    ):
        """
         - `RSP_Z88 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z88>`_
        The purpose of this query/response pair is to retrieve patient pharmacy dispense history information from the Server.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: 1)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: R | rpt: 1)
        :param query_parameter_definition: Query Parameter Definition (id: QPD | seq: 6 | use: R | rpt: 1)
        :param response_control_parameter: Response Control Parameter (id: RCP | seq: 7 | use: R | rpt: 1)
        :param query_response: Query Response segment group: [PATIENT|None, COMMON ORDER] (id: QUERY RESPONSE | seq: None, None | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 32 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.query_parameter_definition = query_parameter_definition
        self.response_control_parameter = response_control_parameter
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

    @property  # get RCP.7
    def response_control_parameter(self) -> RCP:
        """
        id: RCP | use: R | rpt: 1 | seq: 7
        ---
        return_type: RCP.7: Response Control Parameter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP
        """
        return self._c_data[6][0]

    @response_control_parameter.setter  # set RCP.7
    def response_control_parameter(self, rcp: RCP):
        """
        id: RCP | use: R | rpt: 1 | seq: 7
        ---
        param_type: RCP.7: Response Control Parameter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP
        """
        self._c_data[6] = (rcp,)

    @property  # get QUERY RESPONSE
    def query_response(self) -> tuple[RSP_Z88_QUERY_RESPONSE_GROUP, ...]:
        """
        id: RSP_Z88_QUERY_RESPONSE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z88_QUERY_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z88_QUERY_RESPONSE_GROUP
        """
        return self._c_data[7]

    @query_response.setter  # set QUERY RESPONSE
    def query_response(
        self,
        query_response: RSP_Z88_QUERY_RESPONSE_GROUP
        | tuple[RSP_Z88_QUERY_RESPONSE_GROUP, ...],
    ):
        """
        id: QUERY RESPONSE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_Z88_QUERY_RESPONSE_GROUP.None | tuple[RSP_Z88_QUERY_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z88_QUERY_RESPONSE_GROUP
        """
        if isinstance(query_response, tuple):
            self._c_data[7] = query_response
        else:
            self._c_data[7] = (query_response,)

    @property  # get DSC.32
    def continuation_pointer(self) -> DSC:
        """
        id: DSC | use: R | rpt: 1 | seq: 32
        ---
        return_type: DSC.32: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[8][0]

    @continuation_pointer.setter  # set DSC.32
    def continuation_pointer(self, dsc: DSC):
        """
        id: DSC | use: R | rpt: 1 | seq: 32
        ---
        param_type: DSC.32: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[8] = (dsc,)
