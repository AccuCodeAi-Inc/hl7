from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.QRF import QRF
from ..segments.QRD import QRD


"""
Document Query - QRY_T12
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::QRY_T12 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import QRY_T12
from utils.hl7.v2_5_1.segments import (
    QRF, QRD, MSH
)

qry_t12 = QRY_T12(  #  - A query may be used to retrieve a list of documents or a specific document
    message_header=msh,  # MSH(...)  # Required.
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
)

-----END TRIGGER_EVENT::QRY_T12 TEMPLATE-----
"""


class QRY_T12(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """QRY_T12"""
    _hl7_name = """Document Query"""
    _hl7_description = """A query may be used to retrieve a list of documents or a specific document"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QRY_T12"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("1", "2", "3")
    _c_components = (MSH, QRD, QRF)
    _c_name = ("MSH", "QRD", "QRF")
    _c_is_group = (False, False, False)
    _c_attrs = ("message_header", "original_style_query_definition", "original_style_query_filter",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        original_style_query_definition: QRD,  #  Required. QRD.2
        original_style_query_filter: QRF | None = None,  #  QRF.3
    ):
        """
         - `QRY_T12 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QRY_T12>`_
        A query may be used to retrieve a list of documents or a specific document.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 2 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 3 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.message_header = message_header
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter

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
