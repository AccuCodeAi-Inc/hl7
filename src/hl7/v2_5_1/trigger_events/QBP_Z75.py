from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.RDF import RDF
from ..segments.SFT import SFT
from ..segments.RCP import RCP
from ..segments.QPD import QPD
from ..segments.MSH import MSH
from ..segments.DSC import DSC


"""
Tabular Patient List Query - QBP_Z75
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::QBP_Z75 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import QBP_Z75
from utils.hl7.v2_5_1.segments import (
    QPD, DSC, RDF, RCP, MSH, SFT
)

qbp_z75 = QBP_Z75(  #  - The purpose of this query/response pair is to find patient records that closely (as specified by the Client) match a set of input criteria using a specified algorithm
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    query_parameter_definition=qpd,  # QPD(...)  # Required.
    response_control_parameter=rcp,  # RCP(...)  # Required.
    table_row_definition=None,  # RDF(...) 
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::QBP_Z75 TEMPLATE-----
"""


class QBP_Z75(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """QBP_Z75"""
    _hl7_name = """Tabular Patient List Query"""
    _hl7_description = """The purpose of this query/response pair is to find patient records that closely (as specified by the Client) match a set of input criteria using a specified algorithm"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QBP_Z75"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1)
    _c_usage = ("R", "O", "R", "R", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6")
    _c_components = (MSH, SFT, QPD, RCP, RDF, DSC)
    _c_name = ("MSH", "SFT", "QPD", "RCP", "RDF", "DSC")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "query_parameter_definition", "response_control_parameter", "table_row_definition", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        query_parameter_definition: QPD,  #  Required. QPD.3
        response_control_parameter: RCP,  #  Required. RCP.4
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        table_row_definition: RDF | None = None,  #  RDF.5
        continuation_pointer: DSC | None = None,  #  DSC.6
    ):
        """
         - `QBP_Z75 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/QBP_Z75>`_
        The purpose of this query/response pair is to find patient records that closely (as specified by the Client) match a set of input criteria using a specified algorithm.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param query_parameter_definition: Query Parameter Definition (id: QPD | seq: 3 | use: R | rpt: 1)
        :param response_control_parameter: Response Control Parameter (id: RCP | seq: 4 | use: R | rpt: 1)
        :param table_row_definition: Table Row Definition (id: RDF | seq: 5 | use: O | rpt: 1)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.query_parameter_definition = query_parameter_definition
        self.response_control_parameter = response_control_parameter
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

    @property  # get RCP.4
    def response_control_parameter(self) -> RCP:
        """
        id: RCP | use: R | rpt: 1 | seq: 4
        ---
        return_type: RCP.4: Response Control Parameter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP
        """
        return self._c_data[3][0]

    @response_control_parameter.setter  # set RCP.4
    def response_control_parameter(self, rcp: RCP):
        """
        id: RCP | use: R | rpt: 1 | seq: 4
        ---
        param_type: RCP.4: Response Control Parameter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP
        """
        self._c_data[3] = (rcp,)

    @property  # get RDF.5
    def table_row_definition(self) -> RDF | None:
        """
        id: RDF | use: O | rpt: 1 | seq: 5
        ---
        return_type: RDF.5: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        return self._c_data[4][0]

    @table_row_definition.setter  # set RDF.5
    def table_row_definition(self, rdf: RDF | None):
        """
        id: RDF | use: O | rpt: 1 | seq: 5
        ---
        param_type: RDF.5: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        self._c_data[4] = (rdf,)

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