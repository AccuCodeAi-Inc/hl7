from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.RCP import RCP
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.MSA import MSA
from ..segments.QAK import QAK
from ..segment_groups.RSP_K25_STAFF_GROUP import RSP_K25_STAFF_GROUP
from ..segments.DSC import DSC
from ..segments.SFT import SFT


"""
Response - Personnel information - RSP_K25
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RSP_K25 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K25
from utils.hl7.v2_5_1.segments import (
    QAK, SFT, RCP, ERR, MSA, QPD, MSH, DSC
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_K25_STAFF_GROUP
)

rsp_k25 = RSP_K25(  #  - The following trigger event is served by the following Conformance Statement: Another application determines a need for Personnel data about a person and sends a query to a system providing this information
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=qak,  # QAK(...)  # Required.
    query_parameter_definition=qpd,  # QPD(...)  # Required.
    response_control_parameter=rcp,  # RCP(...)  # Required.
    staff=rsp_k25_staff_group,  # RSP_K25_STAFF_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::RSP_K25 TEMPLATE-----
"""


class RSP_K25(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RSP_K25"""
    _hl7_name = """Response - Personnel information"""
    _hl7_description = """The following trigger event is served by the following Conformance Statement: Another application determines a need for Personnel data about a person and sends a query to a system providing this information"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K25"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "R", "R", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "None", "15")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QPD, RCP, RSP_K25_STAFF_GROUP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QPD", "RCP", "STAFF", "DSC")
    _c_is_group = (False, False, False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "query_parameter_definition", "response_control_parameter", "staff", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        query_acknowledgment: QAK,  #  Required. QAK.5
        query_parameter_definition: QPD,  #  Required. QPD.6
        response_control_parameter: RCP,  #  Required. RCP.7
        staff: RSP_K25_STAFF_GROUP
        | tuple[
            RSP_K25_STAFF_GROUP, ...
        ],  #  Required. (STF.8, PRA.9, ORG.10, AFF.11, LAN.12, EDU.13, CER.14, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.4
        continuation_pointer: DSC | None = None,  #  DSC.15
    ):
        """
         - `RSP_K25 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K25>`_
        The following trigger event is served by the following Conformance Statement: Another application determines a need for Personnel data about a person and sends a query to a system providing this information.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: *)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: R | rpt: 1)
        :param query_parameter_definition: Query Parameter Definition (id: QPD | seq: 6 | use: R | rpt: 1)
        :param response_control_parameter: Response Control Parameter (id: RCP | seq: 7 | use: R | rpt: 1)
        :param staff: Staff segment group: [STF, PRA|None, ORG|None, AFF|None, LAN|None, EDU|None, CER|None] (id: STAFF | seq: 8, 9, 10, 11, 12, 13, 14 | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 15 | use: O | rpt: 1)
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
        self.staff = staff
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

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[3]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: ERR.4 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[3] = err
        else:
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

    @property  # get STAFF
    def staff(self) -> tuple[RSP_K25_STAFF_GROUP, ...]:
        """
        id: RSP_K25_STAFF_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_K25_STAFF_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K25_STAFF_GROUP
        """
        return self._c_data[7]

    @staff.setter  # set STAFF
    def staff(self, staff: RSP_K25_STAFF_GROUP | tuple[RSP_K25_STAFF_GROUP, ...]):
        """
        id: STAFF SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_K25_STAFF_GROUP.None | tuple[RSP_K25_STAFF_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K25_STAFF_GROUP
        """
        if isinstance(staff, tuple):
            self._c_data[7] = staff
        else:
            self._c_data[7] = (staff,)

    @property  # get DSC.15
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 15
        ---
        return_type: DSC.15: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[8][0]

    @continuation_pointer.setter  # set DSC.15
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 15
        ---
        param_type: DSC.15: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[8] = (dsc,)
