from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.DSC import DSC
from ..segments.RDF import RDF
from ..segments.VTQ import VTQ
from ..segments.SFT import SFT
from ..segments.MSH import MSH


"""
Virtual Table Query - VQQ_Q07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::VQQ_Q07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VQQ_Q07
from utils.hl7.v2_5_1.segments import (
    MSH, VTQ, RDF, SFT, DSC
)

vqq_q07 = VQQ_Q07(  #  - The VTQ provides a way to query for data to be expressed as tables without having to specify SQL or a stored procedure
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    virtual_table_query_request=vtq,  # VTQ(...)  # Required.
    table_row_definition=None,  # RDF(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::VQQ_Q07 TEMPLATE-----
"""


class VQQ_Q07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """VQQ_Q07"""
    _hl7_name = """Virtual Table Query"""
    _hl7_description = """The VTQ provides a way to query for data to be expressed as tables without having to specify SQL or a stored procedure"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VQQ_Q07"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1)
    _c_usage = ("R", "O", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5")
    _c_components = (MSH, SFT, VTQ, RDF, DSC)
    _c_name = ("MSH", "SFT", "VTQ", "RDF", "DSC")
    _c_is_group = (False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "virtual_table_query_request", "table_row_definition", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        virtual_table_query_request: VTQ,  #  Required. VTQ.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        table_row_definition: RDF | None = None,  #  RDF.4
        continuation_pointer: DSC | None = None,  #  DSC.5
    ):
        """
                 - `VQQ_Q07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VQQ_Q07>`_
                The VTQ provides a way to query for data to be expressed as tables without having to specify SQL or a stored procedure.

        The VQQ supports queries against server database table (virtual or actual) based on specific selection criteria delineated in the VTQ segment.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param virtual_table_query_request: Virtual Table Query Request (id: VTQ | seq: 3 | use: R | rpt: 1)
                :param table_row_definition: Table Row Definition (id: RDF | seq: 4 | use: O | rpt: 1)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 5 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.virtual_table_query_request = virtual_table_query_request
        self.table_row_definition = table_row_definition
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

    @property  # get VTQ.3
    def virtual_table_query_request(self) -> VTQ:
        """
        id: VTQ | use: R | rpt: 1 | seq: 3
        ---
        return_type: VTQ.3: Virtual Table Query Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VTQ
        """
        return self._c_data[2][0]

    @virtual_table_query_request.setter  # set VTQ.3
    def virtual_table_query_request(self, vtq: VTQ):
        """
        id: VTQ | use: R | rpt: 1 | seq: 3
        ---
        param_type: VTQ.3: Virtual Table Query Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VTQ
        """
        self._c_data[2] = (vtq,)

    @property  # get RDF.4
    def table_row_definition(self) -> RDF | None:
        """
        id: RDF | use: O | rpt: 1 | seq: 4
        ---
        return_type: RDF.4: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        return self._c_data[3][0]

    @table_row_definition.setter  # set RDF.4
    def table_row_definition(self, rdf: RDF | None):
        """
        id: RDF | use: O | rpt: 1 | seq: 4
        ---
        param_type: RDF.4: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        self._c_data[3] = (rdf,)

    @property  # get DSC.5
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 5
        ---
        return_type: DSC.5: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[4][0]

    @continuation_pointer.setter  # set DSC.5
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 5
        ---
        param_type: DSC.5: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[4] = (dsc,)
