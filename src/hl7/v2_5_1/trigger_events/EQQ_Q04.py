from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.DSC import DSC
from ..segments.EQL import EQL
from ..segments.MSH import MSH
from ..segments.SFT import SFT


"""
Embedded Query Language Query - EQQ_Q04
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::EQQ_Q04 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EQQ_Q04
from utils.hl7.v2_5_1.segments import (
    SFT, DSC, EQL, MSH
)

eqq_q04 = EQQ_Q04(  #  - This query provides an envelope with which a query expressed in a language (e
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    embedded_query_language=eql,  # EQL(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::EQQ_Q04 TEMPLATE-----
"""


class EQQ_Q04(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """EQQ_Q04"""
    _hl7_name = """Embedded Query Language Query"""
    _hl7_description = """This query provides an envelope with which a query expressed in a language (e"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EQQ_Q04"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4")
    _c_components = (MSH, SFT, EQL, DSC)
    _c_name = ("MSH", "SFT", "EQL", "DSC")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "embedded_query_language", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        embedded_query_language: EQL,  #  Required. EQL.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        continuation_pointer: DSC | None = None,  #  DSC.4
    ):
        """
                 - `EQQ_Q04 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EQQ_Q04>`_
                This query provides an envelope with which a query expressed in a language (e.g., SQL) is packaged and sent to the responding system. It is meant to provide the maximum query function without reinventing the wheel.

        The EQQ with its EQL query defining segment supports free-form select statements, based on the query language of choice (e.g., SQL).

        The response to the EQQ could be tabular or display. The segment pattern response (the ERP) is invalid given that there is no way to specify the desired segment pattern in the query defining segment, EQL.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param embedded_query_language: Embedded Query Language (id: EQL | seq: 3 | use: R | rpt: 1)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.embedded_query_language = embedded_query_language
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

    @property  # get EQL.3
    def embedded_query_language(self) -> EQL:
        """
        id: EQL | use: R | rpt: 1 | seq: 3
        ---
        return_type: EQL.3: Embedded Query Language
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQL
        """
        return self._c_data[2][0]

    @embedded_query_language.setter  # set EQL.3
    def embedded_query_language(self, eql: EQL):
        """
        id: EQL | use: R | rpt: 1 | seq: 3
        ---
        param_type: EQL.3: Embedded Query Language
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQL
        """
        self._c_data[2] = (eql,)

    @property  # get DSC.4
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 4
        ---
        return_type: DSC.4: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[3][0]

    @continuation_pointer.setter  # set DSC.4
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 4
        ---
        param_type: DSC.4: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[3] = (dsc,)
