from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.QRD import QRD
from ..segments.QRF import QRF


"""
QRY WITH DETAIL - NMQ_N01_QRY_WITH_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMQ_N01_QRY_WITH_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMQ_N01_QRY_WITH_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    QRF, QRD
)

nmq_n01_qry_with_detail_group = NMQ_N01_QRY_WITH_DETAIL_GROUP(  # QRY WITH DETAIL - Segment group for NMQ_N01 - Application management query message consisting of QRD, QRF|None
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMQ_N01_QRY_WITH_DETAIL_GROUP TEMPLATE-----
"""


class NMQ_N01_QRY_WITH_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMQ_N01_QRY_WITH_DETAIL_GROUP"""
    _hl7_name = """QRY WITH DETAIL"""
    _hl7_description = """Segment group for NMQ_N01 - Application management query message consisting of QRD, QRF|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMQ_N01_QRY_WITH_DETAIL_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("3", "4")
    _c_components = (QRD, QRF)
    _c_name = ("QRD", "QRF")
    _c_is_group = (False, False)
    _c_attrs = ("original_style_query_definition", "original_style_query_filter",)
    # fmt: on

    def __init__(
        self,
        original_style_query_definition: QRD,  #  Required. QRD.3
        original_style_query_filter: QRF | None = None,  #  QRF.4
    ):
        """
        None - `NMQ_N01_QRY_WITH_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMQ_N01_QRY_WITH_DETAIL_GROUP>`_
        Segment group for NMQ_N01 - Application management query message consisting of QRD, QRF|None

        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 3 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter

    @property  # get QRD.3
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 3
        ---
        return_type: QRD.3: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[0][0]

    @original_style_query_definition.setter  # set QRD.3
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 3
        ---
        param_type: QRD.3: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[0] = (qrd,)

    @property  # get QRF.4
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 4
        ---
        return_type: QRF.4: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[1][0]

    @original_style_query_filter.setter  # set QRF.4
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 4
        ---
        param_type: QRF.4: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[1] = (qrf,)
