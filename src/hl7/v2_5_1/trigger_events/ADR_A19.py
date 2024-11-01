from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ERR import ERR
from ..segments.DSC import DSC
from ..segments.QRF import QRF
from ..segment_groups.ADR_A19_QUERY_RESPONSE_GROUP import ADR_A19_QUERY_RESPONSE_GROUP
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.MSA import MSA
from ..segments.QRD import QRD


"""
Patient Query - Response - ADR_A19
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADR_A19 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADR_A19
from utils.hl7.v2_5_1.segments import (
    MSH, QRD, SFT, ERR, QRF, DSC, QAK, MSA
)
from utils.hl7.v2_5_1.segment_groups import (
    ADR_A19_QUERY_RESPONSE_GROUP
)

adr_a19 = ADR_A19(  #  - The following trigger event is served by QRY (a query from another system) and ADR (a response from an Patient Administration system
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=None,  # QAK(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    query_response=adr_a19_query_response_group,  # ADR_A19_QUERY_RESPONSE_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::ADR_A19 TEMPLATE-----
"""


class ADR_A19(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADR_A19"""
    _hl7_name = """Patient Query - Response"""
    _hl7_description = """The following trigger event is served by QRY (a query from another system) and ADR (a response from an Patient Administration system"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADR_A19"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "O", "R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "None", "31")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QRD, QRF, ADR_A19_QUERY_RESPONSE_GROUP, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QRD", "QRF", "QUERY RESPONSE", "DSC")
    _c_is_group = (False, False, False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "original_style_query_definition", "original_style_query_filter", "query_response", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        original_style_query_definition: QRD,  #  Required. QRD.6
        query_response: ADR_A19_QUERY_RESPONSE_GROUP
        | tuple[
            ADR_A19_QUERY_RESPONSE_GROUP, ...
        ],  #  Required. (EVN.8, PID.9, PD1.10, ROL.11, NK1.12, PV1.13, PV2.14, ROL.15, DB1.16, OBX.17, AL1.18, DG1.19, DRG.20, GT1.23, ACC.28, UB1.29, UB2.30, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | None = None,  #  ERR.4
        query_acknowledgment: QAK | None = None,  #  QAK.5
        original_style_query_filter: QRF | None = None,  #  QRF.7
        continuation_pointer: DSC | None = None,  #  DSC.31
    ):
        """
                 - `ADR_A19 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADR_A19>`_
                The following trigger event is served by QRY (a query from another system) and ADR (a response from an Patient Administration system.)

        Another application determines a need for Patient Administration data about a patient and sends a query to the Patient Administration system.  The Who Filter in the QRD can identify the patient or account number upon which the query is defined and can contain a format code of “R” (record-oriented).  If the query is based on the Patient ID and there are data associated with multiple accounts, the problem of which account data should be returned becomes an implementation issue.  The ADT event-type segment, if included in the response, describes the last event for which the Patient Administration system initiated an unsolicited update.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
                :param error: Error (id: ERR | seq: 4 | use: O | rpt: 1)
                :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: O | rpt: 1)
                :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 6 | use: R | rpt: 1)
                :param original_style_query_filter: Original style query filter (id: QRF | seq: 7 | use: O | rpt: 1)
                :param query_response: Query Response segment group: [EVN|None, PID, PD1|None, ROL|None, NK1|None, PV1, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None] (id: QUERY RESPONSE | seq: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, 23, None, 28, 29, 30 | use: R | rpt: *)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 31 | use: O | rpt: 1)
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

    @property  # get QUERY RESPONSE
    def query_response(self) -> tuple[ADR_A19_QUERY_RESPONSE_GROUP, ...]:
        """
        id: ADR_A19_QUERY_RESPONSE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ADR_A19_QUERY_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADR_A19_QUERY_RESPONSE_GROUP
        """
        return self._c_data[7]

    @query_response.setter  # set QUERY RESPONSE
    def query_response(
        self,
        query_response: ADR_A19_QUERY_RESPONSE_GROUP
        | tuple[ADR_A19_QUERY_RESPONSE_GROUP, ...],
    ):
        """
        id: QUERY RESPONSE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ADR_A19_QUERY_RESPONSE_GROUP.None | tuple[ADR_A19_QUERY_RESPONSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADR_A19_QUERY_RESPONSE_GROUP
        """
        if isinstance(query_response, tuple):
            self._c_data[7] = query_response
        else:
            self._c_data[7] = (query_response,)

    @property  # get DSC.31
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 31
        ---
        return_type: DSC.31: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[8][0]

    @continuation_pointer.setter  # set DSC.31
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 31
        ---
        param_type: DSC.31: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[8] = (dsc,)
