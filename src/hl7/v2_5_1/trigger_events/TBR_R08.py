from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segments.RDF import RDF
from ..segments.RDT import RDT
from ..segments.QAK import QAK


"""
Tabular data response - TBR_R08
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::TBR_R08 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import TBR_R08
from utils.hl7.v2_5_1.segments import (
    ERR, DSC, RDF, MSA, SFT, RDT, MSH, QAK
)

tbr_r08 = TBR_R08(  #  - The response to the EQQ could be tabular or display
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=qak,  # QAK(...)  # Required.
    table_row_definition=rdf,  # RDF(...)  # Required.
    table_row_data=rdt,  # RDT(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::TBR_R08 TEMPLATE-----
"""


class TBR_R08(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """TBR_R08"""
    _hl7_name = """Tabular data response"""
    _hl7_description = """The response to the EQQ could be tabular or display"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/TBR_R08"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "R", "R", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8")
    _c_components = (MSH, SFT, MSA, ERR, QAK, RDF, RDT, DSC)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "RDF", "RDT", "DSC")
    _c_is_group = (False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "table_row_definition", "table_row_data", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        query_acknowledgment: QAK,  #  Required. QAK.5
        table_row_definition: RDF,  #  Required. RDF.6
        table_row_data: RDT | tuple[RDT, ...],  #  Required. RDT.7
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | None = None,  #  ERR.4
        continuation_pointer: DSC | None = None,  #  DSC.8
    ):
        """
         - `TBR_R08 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/TBR_R08>`_
        The response to the EQQ could be tabular or display. The segment pattern response (the ERP) is invalid given that there is no way to specify the desired segment pattern in the query defining segment, EQL.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: 1)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: R | rpt: 1)
        :param table_row_definition: Table Row Definition (id: RDF | seq: 6 | use: R | rpt: 1)
        :param table_row_data: Table Row Data (id: RDT | seq: 7 | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.table_row_definition = table_row_definition
        self.table_row_data = table_row_data
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

    @property  # get RDF.6
    def table_row_definition(self) -> RDF:
        """
        id: RDF | use: R | rpt: 1 | seq: 6
        ---
        return_type: RDF.6: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        return self._c_data[5][0]

    @table_row_definition.setter  # set RDF.6
    def table_row_definition(self, rdf: RDF):
        """
        id: RDF | use: R | rpt: 1 | seq: 6
        ---
        param_type: RDF.6: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        self._c_data[5] = (rdf,)

    @property  # get RDT
    def table_row_data(self) -> tuple[RDT, ...]:
        """
        id: RDT SEGMENT GROUP | use: R | rpt: * | seq: 7
        ---
        return_type: tuple[RDT, ...]: (Table Row Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDT
        """
        return self._c_data[6]

    @table_row_data.setter  # set RDT
    def table_row_data(self, rdt: RDT | tuple[RDT, ...]):
        """
        id: RDT SEGMENT GROUP | use: R | rpt: * | seq: 7
        ---
        param_type: RDT.7 | tuple[RDT, ...]: (Table Row Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDT
        """
        if isinstance(rdt, tuple):
            self._c_data[6] = rdt
        else:
            self._c_data[6] = (rdt,)

    @property  # get DSC.8
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 8
        ---
        return_type: DSC.8: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[7][0]

    @continuation_pointer.setter  # set DSC.8
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 8
        ---
        param_type: DSC.8: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[7] = (dsc,)
