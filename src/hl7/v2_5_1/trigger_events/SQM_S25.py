from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.QRD import QRD
from ..segment_groups.SQM_S25_REQUEST_GROUP import SQM_S25_REQUEST_GROUP
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRF import QRF


"""
Schedule query message and response - SQM_S25
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SQM_S25 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQM_S25
from utils.hl7.v2_5_1.segments import (
    QRF, QRD, DSC, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SQM_S25_REQUEST_GROUP
)

sqm_s25 = SQM_S25(  #  - Original Mode record-oriented query transactions are initiated from the querying application using the Schedule Query (SQM) to request information about a filler application's schedule(s)
    message_header=msh,  # MSH(...)  # Required.
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    request=None,  # SQM_S25_REQUEST_GROUP(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::SQM_S25 TEMPLATE-----
"""


class SQM_S25(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SQM_S25"""
    _hl7_name = """Schedule query message and response"""
    _hl7_description = """Original Mode record-oriented query transactions are initiated from the querying application using the Schedule Query (SQM) to request information about a filler application's schedule(s)"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1, 1)
    _c_usage = ("R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "None", "16")
    _c_components = (MSH, QRD, QRF, SQM_S25_REQUEST_GROUP, DSC)
    _c_name = ("MSH", "QRD", "QRF", "REQUEST", "DSC")
    _c_is_group = (False, False, False, True, False)
    _c_attrs = ("message_header", "original_style_query_definition", "original_style_query_filter", "request", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        original_style_query_definition: QRD,  #  Required. QRD.2
        original_style_query_filter: QRF | None = None,  #  QRF.3
        request: SQM_S25_REQUEST_GROUP | None = None,  #  ARQ.4, APR.5, PID.6
        continuation_pointer: DSC | None = None,  #  DSC.16
    ):
        """
         - `SQM_S25 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25>`_
        Original Mode record-oriented query transactions are initiated from the querying application using the Schedule Query (SQM) to request information about a filler application's schedule(s).  The filler application responds to these requests, using the Schedule Query Response (SQR) message to either return the requested information, or to signal that an interfacing error of some kind has occurred.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 2 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 3 | use: O | rpt: 1)
        :param request: Request segment group: [ARQ, APR|None, PID|None, RESOURCES] (id: REQUEST | seq: 4, 5, 6, None | use: O | rpt: 1)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.request = request
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

    @property  # get QRD.2
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 2
        ---
        return_type: QRD.2: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[1][0]

    @original_style_query_definition.setter  # set QRD.2
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 2
        ---
        param_type: QRD.2: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[1] = (qrd,)

    @property  # get QRF.3
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 3
        ---
        return_type: QRF.3: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[2][0]

    @original_style_query_filter.setter  # set QRF.3
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 3
        ---
        param_type: QRF.3: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[2] = (qrf,)

    @property  # get SQM_S25_REQUEST_GROUP.None
    def request(self) -> SQM_S25_REQUEST_GROUP | None:
        """
        id: SQM_S25_REQUEST_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: SQM_S25_REQUEST_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQM_S25_REQUEST_GROUP
        """
        return self._c_data[3][0]

    @request.setter  # set SQM_S25_REQUEST_GROUP.None
    def request(self, request: SQM_S25_REQUEST_GROUP | None):
        """
        id: SQM_S25_REQUEST_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: SQM_S25_REQUEST_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQM_S25_REQUEST_GROUP
        """
        self._c_data[3] = (request,)

    @property  # get DSC.16
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 16
        ---
        return_type: DSC.16: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[4][0]

    @continuation_pointer.setter  # set DSC.16
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 16
        ---
        param_type: DSC.16: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[4] = (dsc,)
