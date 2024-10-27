from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.RDF import RDF
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.DSC import DSC
from ..segments.SPR import SPR


"""
Stored Procedure Request - SPQ_Q08
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SPQ_Q08 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SPQ_Q08
from utils.hl7.v2_5_1.segments import (
    DSC, RDF, SPR, MSH, SFT
)

spq_q08 = SPQ_Q08(  #  - The Stored Procedure Query provides a mechanism for the querying system to invoke a stored procedure on the responding system
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    stored_procedure_request_definition=spr,  # SPR(...)  # Required.
    table_row_definition=None,  # RDF(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::SPQ_Q08 TEMPLATE-----
"""


class SPQ_Q08(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SPQ_Q08"""
    _hl7_name = """Stored Procedure Request"""
    _hl7_description = """The Stored Procedure Query provides a mechanism for the querying system to invoke a stored procedure on the responding system"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SPQ_Q08"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1)
    _c_usage = ("R", "O", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5")
    _c_components = (MSH, SFT, SPR, RDF, DSC)
    _c_name = ("MSH", "SFT", "SPR", "RDF", "DSC")
    _c_is_group = (False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "stored_procedure_request_definition", "table_row_definition", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        stored_procedure_request_definition: SPR,  #  Required. SPR.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        table_row_definition: RDF | None = None,  #  RDF.4
        continuation_pointer: DSC | None = None,  #  DSC.5
    ):
        """
                 - `SPQ_Q08 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SPQ_Q08>`_
                The Stored Procedure Query provides a mechanism for the querying system to invoke a stored procedure on the responding system. The request includes a stored procedure name and a list of parameters passed to it.

        The SPQ enables an application on one system to execute a stored procedure on another system, which is coded to extract specific data.

        Since the SPR segment includes a response format code, the response could be tabular, display or segment pattern .

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param stored_procedure_request_definition: Stored Procedure Request Definition (id: SPR | seq: 3 | use: R | rpt: 1)
                :param table_row_definition: Table Row Definition (id: RDF | seq: 4 | use: O | rpt: 1)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 5 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.stored_procedure_request_definition = stored_procedure_request_definition
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

    @property  # get SPR.3
    def stored_procedure_request_definition(self) -> SPR:
        """
        id: SPR | use: R | rpt: 1 | seq: 3
        ---
        return_type: SPR.3: Stored Procedure Request Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPR
        """
        return self._c_data[2][0]

    @stored_procedure_request_definition.setter  # set SPR.3
    def stored_procedure_request_definition(self, spr: SPR):
        """
        id: SPR | use: R | rpt: 1 | seq: 3
        ---
        param_type: SPR.3: Stored Procedure Request Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPR
        """
        self._c_data[2] = (spr,)

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
