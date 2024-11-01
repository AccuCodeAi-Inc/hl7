from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.DOC_T12_RESULT_GROUP import DOC_T12_RESULT_GROUP
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.MSA import MSA
from ..segments.QAK import QAK
from ..segments.DSC import DSC


"""
Document response - DOC_T12
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::DOC_T12 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DOC_T12
from utils.hl7.v2_5_1.segments import (
    QAK, QRD, ERR, MSA, DSC, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    DOC_T12_RESULT_GROUP
)

doc_t12 = DOC_T12(  #  - A query may be used to retrieve a list of documents or a specific document
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=None,  # QAK(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    result=doc_t12_result_group,  # DOC_T12_RESULT_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::DOC_T12 TEMPLATE-----
"""


class DOC_T12(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """DOC_T12"""
    _hl7_name = """Document response"""
    _hl7_description = """A query may be used to retrieve a list of documents or a specific document"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DOC_T12"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "R", "O", "O", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "None", "11")
    _c_components = (MSH, MSA, ERR, QAK, QRD, DOC_T12_RESULT_GROUP, DSC)
    _c_name = ("MSH", "MSA", "ERR", "QAK", "QRD", "RESULT", "DSC")
    _c_is_group = (False, False, False, False, False, True, False)
    _c_attrs = ("message_header", "message_acknowledgment", "error", "query_acknowledgment", "original_style_query_definition", "result", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        original_style_query_definition: QRD,  #  Required. QRD.5
        result: DOC_T12_RESULT_GROUP
        | tuple[
            DOC_T12_RESULT_GROUP, ...
        ],  #  Required. (EVN.6, PID.7, PV1.8, TXA.9, OBX.10, ...)
        error: ERR | None = None,  #  ERR.3
        query_acknowledgment: QAK | None = None,  #  QAK.4
        continuation_pointer: DSC | None = None,  #  DSC.11
    ):
        """
         - `DOC_T12 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DOC_T12>`_
        A query may be used to retrieve a list of documents or a specific document

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 3 | use: O | rpt: 1)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 4 | use: O | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 5 | use: R | rpt: 1)
        :param result: Result segment group: [EVN|None, PID, PV1, TXA, OBX|None] (id: RESULT | seq: 6, 7, 8, 9, 10 | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 11 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.original_style_query_definition = original_style_query_definition
        self.result = result
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

    @property  # get MSA.2
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 2
        ---
        return_type: MSA.2: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[1][0]

    @message_acknowledgment.setter  # set MSA.2
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 2
        ---
        param_type: MSA.2: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[1] = (msa,)

    @property  # get ERR.3
    def error(self) -> ERR | None:
        """
        id: ERR | use: O | rpt: 1 | seq: 3
        ---
        return_type: ERR.3: Error
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[2][0]

    @error.setter  # set ERR.3
    def error(self, err: ERR | None):
        """
        id: ERR | use: O | rpt: 1 | seq: 3
        ---
        param_type: ERR.3: Error
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        self._c_data[2] = (err,)

    @property  # get QAK.4
    def query_acknowledgment(self) -> QAK | None:
        """
        id: QAK | use: O | rpt: 1 | seq: 4
        ---
        return_type: QAK.4: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[3][0]

    @query_acknowledgment.setter  # set QAK.4
    def query_acknowledgment(self, qak: QAK | None):
        """
        id: QAK | use: O | rpt: 1 | seq: 4
        ---
        param_type: QAK.4: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[3] = (qak,)

    @property  # get QRD.5
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 5
        ---
        return_type: QRD.5: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[4][0]

    @original_style_query_definition.setter  # set QRD.5
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 5
        ---
        param_type: QRD.5: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[4] = (qrd,)

    @property  # get RESULT
    def result(self) -> tuple[DOC_T12_RESULT_GROUP, ...]:
        """
        id: DOC_T12_RESULT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[DOC_T12_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DOC_T12_RESULT_GROUP
        """
        return self._c_data[5]

    @result.setter  # set RESULT
    def result(self, result: DOC_T12_RESULT_GROUP | tuple[DOC_T12_RESULT_GROUP, ...]):
        """
        id: RESULT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: DOC_T12_RESULT_GROUP.None | tuple[DOC_T12_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DOC_T12_RESULT_GROUP
        """
        if isinstance(result, tuple):
            self._c_data[5] = result
        else:
            self._c_data[5] = (result,)

    @property  # get DSC.11
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 11
        ---
        return_type: DSC.11: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[6][0]

    @continuation_pointer.setter  # set DSC.11
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 11
        ---
        param_type: DSC.11: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[6] = (dsc,)
