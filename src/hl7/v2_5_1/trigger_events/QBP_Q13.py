from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.QPD import QPD
from ..segments.RCP import RCP


"""
Query by Parameter Requesting an RTB Tabular Response - QBP_Q13
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::QBP_Q13 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import QBP_Q13
from utils.hl7.v2_5_1.segments import (
    DSC, RDF, RCP, QPD, SFT, MSH
)

qbp_q13 = QBP_Q13(  #  - The QBP_Q13 structure supports a Tabular Response and contains the MSH, RDF, RCP, and DSC segments
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    query_parameter_definition=qpd,  # QPD(...)  # Required.
    table_row_definition=None,  # RDF(...) 
    response_control_parameter=rcp,  # RCP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::QBP_Q13 TEMPLATE-----
"""


class QBP_Q13(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """QBP_Q13"""
    _hl7_name = """Query by Parameter Requesting an RTB Tabular Response"""
    _hl7_description = """The QBP_Q13 structure supports a Tabular Response and contains the MSH, RDF, RCP, and DSC segments"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QBP_Q13"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1)
    _c_usage = ("R", "O", "R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6")
    _c_components = (MSH, SFT, QPD, RDF, RCP, DSC)
    _c_name = ("MSH", "SFT", "QPD", "RDF", "RCP", "DSC")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "query_parameter_definition", "table_row_definition", "response_control_parameter", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        query_parameter_definition: QPD,  #  Required. QPD.3
        response_control_parameter: RCP,  #  Required. RCP.5
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        table_row_definition: RDF | None = None,  #  RDF.4
        continuation_pointer: DSC | None = None,  #  DSC.6
    ):
        """
                 - `QBP_Q13 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QBP_Q13>`_
                The QBP_Q13 structure supports a Tabular Response and contains the MSH, RDF, RCP, and DSC segments.  Its default trigger event is Q13.  A standard or site-defined query may use this trigger event or may specify a unique trigger event value in its Conformance Statement.  If a unique trigger event value is chosen for a site-defined query, that value must begin with Z.

        Note on QBP: Query By Example variant:  The query by example is an extension of Query By Parameter (QBP) in which search parameters are passed by sending them in the segment which naturally carries them. A Conformance Statement which uses this variant must replace the ellipses in the input QBP_Q11 grammar above, with the specific segments that it accepts.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param query_parameter_definition: Query Parameter Definition (id: QPD | seq: 3 | use: R | rpt: 1)
                :param table_row_definition: Table Row Definition (id: RDF | seq: 4 | use: O | rpt: 1)
                :param response_control_parameter: Response Control Parameter (id: RCP | seq: 5 | use: R | rpt: 1)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.query_parameter_definition = query_parameter_definition
        self.table_row_definition = table_row_definition
        self.response_control_parameter = response_control_parameter
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

    @property  # get QPD.3
    def query_parameter_definition(self) -> QPD:
        """
        id: QPD | use: R | rpt: 1 | seq: 3
        ---
        return_type: QPD.3: Query Parameter Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QPD
        """
        return self._c_data[2][0]

    @query_parameter_definition.setter  # set QPD.3
    def query_parameter_definition(self, qpd: QPD):
        """
        id: QPD | use: R | rpt: 1 | seq: 3
        ---
        param_type: QPD.3: Query Parameter Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QPD
        """
        self._c_data[2] = (qpd,)

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

    @property  # get RCP.5
    def response_control_parameter(self) -> RCP:
        """
        id: RCP | use: R | rpt: 1 | seq: 5
        ---
        return_type: RCP.5: Response Control Parameter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP
        """
        return self._c_data[4][0]

    @response_control_parameter.setter  # set RCP.5
    def response_control_parameter(self, rcp: RCP):
        """
        id: RCP | use: R | rpt: 1 | seq: 5
        ---
        param_type: RCP.5: Response Control Parameter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP
        """
        self._c_data[4] = (rcp,)

    @property  # get DSC.6
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 6
        ---
        return_type: DSC.6: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[5][0]

    @continuation_pointer.setter  # set DSC.6
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 6
        ---
        param_type: DSC.6: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[5] = (dsc,)
