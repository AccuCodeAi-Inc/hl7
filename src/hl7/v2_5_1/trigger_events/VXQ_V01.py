from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.QRF import QRF
from ..segments.QRD import QRD


"""
Vaccination Record Query - VXQ_V01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::VXQ_V01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXQ_V01
from utils.hl7.v2_5_1.segments import (
    SFT, QRF, QRD, MSH
)

vxq_v01 = VXQ_V01(  #  - When an immunization registry does not already have the complete patient vaccination record, it will send a query (with a V01 event) for the definitive (last updated) record
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
)

-----END TRIGGER_EVENT::VXQ_V01 TEMPLATE-----
"""


class VXQ_V01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """VXQ_V01"""
    _hl7_name = """Vaccination Record Query"""
    _hl7_description = """When an immunization registry does not already have the complete patient vaccination record, it will send a query (with a V01 event) for the definitive (last updated) record"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXQ_V01"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4")
    _c_components = (MSH, SFT, QRD, QRF)
    _c_name = ("MSH", "SFT", "QRD", "QRF")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "original_style_query_definition", "original_style_query_filter",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        original_style_query_definition: QRD,  #  Required. QRD.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        original_style_query_filter: QRF | None = None,  #  QRF.4
    ):
        """
         - `VXQ_V01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXQ_V01>`_
        When an immunization registry does not already have the complete patient vaccination record, it will send a query (with a V01 event) for the definitive (last updated) record.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 3 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
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

    @property  # get QRD.3
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 3
        ---
        return_type: QRD.3: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[2][0]

    @original_style_query_definition.setter  # set QRD.3
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 3
        ---
        param_type: QRD.3: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[2] = (qrd,)

    @property  # get QRF.4
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 4
        ---
        return_type: QRF.4: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[3][0]

    @original_style_query_filter.setter  # set QRF.4
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 4
        ---
        param_type: QRF.4: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[3] = (qrf,)
