from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.QSC import QSC
from ..tables.QueryOrResponseFormatCode import QueryOrResponseFormatCode


"""
Virtual Table Query Request - VTQ
HL7 Version: 2.5.1

-----BEGIN SEGMENT::VTQ TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    VTQ,
    ST, CE, ID, QSC
)

vtq = VTQ(  #  - This segment is not carried forward to the recommended queries for v 2
    query_tag=None,  # ST(...) 
    query_or_response_format_code=id,  # ID(...)  # Required.
    vt_query_name=ce,  # CE(...)  # Required.
    virtual_table_name=ce,  # CE(...)  # Required.
    selection_criteria=None,  # QSC(...) 
)

-----END SEGMENT::VTQ TEMPLATE-----
"""


class VTQ(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """VTQ"""
    _hl7_name = """Virtual Table Query Request"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VTQ"
    _c_length = (32, 1, 250, 250, 256,)
    _c_rpt = (1, 1, 1, 1, 65535,)
    _c_usage = ("O", "R", "R", "R", "O",)
    _c_components = (ST, ID, CE, CE, QSC,)
    _c_aliases = ("VTQ.1", "VTQ.2", "VTQ.3", "VTQ.4", "VTQ.5",)
    _c_names = ("Query Tag", "Query/Response Format Code", "VT Query Name", "Virtual Table Name", "Selection Criteria",)
    _c_attrs = ("query_tag", "query_or_response_format_code", "vt_query_name", "virtual_table_name", "selection_criteria",)
    # fmt: on

    def __init__(
        self,
        query_or_response_format_code: QueryOrResponseFormatCode
        | ID
        | tuple[QueryOrResponseFormatCode | ID, ...],  # VTQ.2
        vt_query_name: CE | tuple[CE, ...],  # VTQ.3
        virtual_table_name: CE | tuple[CE, ...],  # VTQ.4
        query_tag: ST | tuple[ST, ...] | None = None,  # VTQ.1
        selection_criteria: QSC | tuple[QSC, ...] | None = None,  # VTQ.5
    ):
        """
                Virtual Table Query Request - `VTQ <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VTQ>`_
                This segment is not carried forward to the recommended queries for v 2.4.

        The VTQ segment is used to define queries that are responded to with the Tabular Data Message (TBR).  The VTQ query message is an alternate method to the EQQ query message that some systems may find easier to implement, due to its use of HL7 delimiters that separate components of the selection definition, and its limited selection criteria.  Queries involving complex selection criteria (nested operators, etc.) may need to be formatted as an EQL segment.

                :param query_tag: String Data (id: VTQ.1 | len: 32 | use: O | rpt: 1)
                :param query_or_response_format_code: Coded values for HL7 tables (id: VTQ.2 | len: 1 | use: R | rpt: 1)
                :param vt_query_name: Coded Element (id: VTQ.3 | len: 250 | use: R | rpt: 1)
                :param virtual_table_name: Coded Element (id: VTQ.4 | len: 250 | use: R | rpt: 1)
                :param selection_criteria: Query Selection Criteria (id: VTQ.5 | len: 256 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.query_tag = query_tag
        self.query_or_response_format_code = query_or_response_format_code
        self.vt_query_name = vt_query_name
        self.virtual_table_name = virtual_table_name
        self.selection_criteria = selection_criteria

    @property  # get VTQ.1
    def query_tag(self) -> ST | None:
        """
        id: VTQ.1 | len: 32 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.1
        """
        return self._c_data[0][0]

    @query_tag.setter  # set VTQ.1
    def query_tag(self, st: ST | None):
        """
        id: VTQ.1 | len: 32 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.1
        """
        self._c_data[0] = (st,)

    @property  # get VTQ.2
    def query_or_response_format_code(self) -> QueryOrResponseFormatCode:
        """
        id: VTQ.2 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.2
        """
        return self._c_data[1][0]

    @query_or_response_format_code.setter  # set VTQ.2
    def query_or_response_format_code(
        self, query_or_response_format_code: QueryOrResponseFormatCode
    ):
        """
        id: VTQ.2 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.2
        """
        self._c_data[1] = (query_or_response_format_code,)

    @property  # get VTQ.3
    def vt_query_name(self) -> CE:
        """
        id: VTQ.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.3
        """
        return self._c_data[2][0]

    @vt_query_name.setter  # set VTQ.3
    def vt_query_name(self, ce: CE):
        """
        id: VTQ.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.3
        """
        self._c_data[2] = (ce,)

    @property  # get VTQ.4
    def virtual_table_name(self) -> CE:
        """
        id: VTQ.4 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.4
        """
        return self._c_data[3][0]

    @virtual_table_name.setter  # set VTQ.4
    def virtual_table_name(self, ce: CE):
        """
        id: VTQ.4 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.4
        """
        self._c_data[3] = (ce,)

    @property
    def selection_criteria(self) -> tuple[QSC, ...] | tuple[None]:
        """
        id: VTQ.5 | len: 256 | use: O | rpt: *
        ---
        return_type: tuple[QSC, ...]: (Query Selection Criteria, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.5
        """
        return self._c_data[4]

    @selection_criteria.setter  # set VTQ.5
    def selection_criteria(self, qsc: QSC | tuple[QSC] | None):
        """
        id: VTQ.5 | len: 256 | use: O | rpt: *
        ---
        param_type: QSC | tuple[QSC, ...]: (Query Selection Criteria, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VTQ.5
        """
        if isinstance(qsc, tuple):
            self._c_data[4] = qsc
        else:
            self._c_data[4] = (qsc,)
