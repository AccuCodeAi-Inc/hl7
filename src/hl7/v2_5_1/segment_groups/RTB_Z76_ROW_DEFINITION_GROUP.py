from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RDF import RDF
from ..segments.RDT import RDT


"""
ROW DEFINITION - RTB_Z76_ROW_DEFINITION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RTB_Z76_ROW_DEFINITION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RTB_Z76_ROW_DEFINITION_GROUP
from utils.hl7.v2_5_1.segments import (
    RDF, RDT
)

rtb_z76_row_definition_group = RTB_Z76_ROW_DEFINITION_GROUP(  # ROW DEFINITION - Segment group for RTB_Z76 - Tabular Patient List consisting of RDF, RDT|None
    table_row_definition=rdf,  # RDF(...)  # Required.
    table_row_data=None,  # RDT(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RTB_Z76_ROW_DEFINITION_GROUP TEMPLATE-----
"""


class RTB_Z76_ROW_DEFINITION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RTB_Z76_ROW_DEFINITION_GROUP"""
    _hl7_name = """ROW DEFINITION"""
    _hl7_description = """Segment group for RTB_Z76 - Tabular Patient List consisting of RDF, RDT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RTB_Z76_ROW_DEFINITION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("7", "8")
    _c_components = (RDF, RDT)
    _c_name = ("RDF", "RDT")
    _c_is_group = (False, False)
    _c_attrs = ("table_row_definition", "table_row_data",)
    # fmt: on

    def __init__(
        self,
        table_row_definition: RDF,  #  Required. RDF.7
        table_row_data: RDT | tuple[RDT, ...] | None = None,  #  RDT.8
    ):
        """
        None - `RTB_Z76_ROW_DEFINITION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RTB_Z76_ROW_DEFINITION_GROUP>`_
        Segment group for RTB_Z76 - Tabular Patient List consisting of RDF, RDT|None

        :param table_row_definition: Table Row Definition (id: RDF | seq: 7 | use: R | rpt: 1)
        :param table_row_data: Table Row Data (id: RDT | seq: 8 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.table_row_definition = table_row_definition
        self.table_row_data = table_row_data

    @property  # get RDF.7
    def table_row_definition(self) -> RDF:
        """
        id: RDF | use: R | rpt: 1 | seq: 7
        ---
        return_type: RDF.7: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        return self._c_data[0][0]

    @table_row_definition.setter  # set RDF.7
    def table_row_definition(self, rdf: RDF):
        """
        id: RDF | use: R | rpt: 1 | seq: 7
        ---
        param_type: RDF.7: Table Row Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF
        """
        self._c_data[0] = (rdf,)

    @property  # get RDT
    def table_row_data(self) -> tuple[RDT, ...] | tuple[None]:
        """
        id: RDT SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[RDT, ...]: (Table Row Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDT
        """
        return self._c_data[1]

    @table_row_data.setter  # set RDT
    def table_row_data(self, rdt: RDT | tuple[RDT, ...] | None):
        """
        id: RDT SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: RDT.8 | tuple[RDT, ...]: (Table Row Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDT
        """
        if isinstance(rdt, tuple):
            self._c_data[1] = rdt
        else:
            self._c_data[1] = (rdt,)
