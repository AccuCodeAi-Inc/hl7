from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..tables.QueryOrResponseFormatCode import QueryOrResponseFormatCode


"""
Embedded Query Language - EQL
HL7 Version: 2.5.1

-----BEGIN SEGMENT::EQL TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EQL,
    ST, CE, ID
)

eql = EQL(  #  - The EQL segment is used to define queries using select statements based on the query language of choice (e
    query_tag=None,  # ST(...) 
    query_or_response_format_code=id,  # ID(...)  # Required.
    eql_query_name=ce,  # CE(...)  # Required.
    eql_query_statement=st,  # ST(...)  # Required.
)

-----END SEGMENT::EQL TEMPLATE-----
"""


class EQL(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """EQL"""
    _hl7_name = """Embedded Query Language"""
    _hl7_description = """The EQL segment is used to define queries using select statements based on the query language of choice (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQL"
    _c_length = (32, 1, 250, 4096,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "R", "R", "R",)
    _c_components = (ST, ID, CE, ST,)
    _c_aliases = ("EQL.1", "EQL.2", "EQL.3", "EQL.4",)
    _c_names = ("Query Tag", "Query/Response Format Code", "EQL Query Name", "EQL Query Statement",)
    _c_attrs = ("query_tag", "query_or_response_format_code", "eql_query_name", "eql_query_statement",)
    # fmt: on

    def __init__(
        self,
        query_or_response_format_code: QueryOrResponseFormatCode
        | ID
        | tuple[QueryOrResponseFormatCode | ID, ...],  # EQL.2
        eql_query_name: CE | tuple[CE, ...],  # EQL.3
        eql_query_statement: ST | tuple[ST, ...],  # EQL.4
        query_tag: ST | tuple[ST, ...] | None = None,  # EQL.1
    ):
        """
                Embedded Query Language - `EQL <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQL>`_
                The EQL segment is used to define queries using select statements based on the query language of choice (e.g., SQL).  Refer to the functional chapters for the lists of HL7-defined EQL select statements.

        This segment is not carried forward to the recommended queries for v 2.4.

                :param query_tag: String Data (id: EQL.1 | len: 32 | use: O | rpt: 1)
                :param query_or_response_format_code: Coded values for HL7 tables (id: EQL.2 | len: 1 | use: R | rpt: 1)
                :param eql_query_name: Coded Element (id: EQL.3 | len: 250 | use: R | rpt: 1)
                :param eql_query_statement: String Data (id: EQL.4 | len: 4096 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.query_tag = query_tag
        self.query_or_response_format_code = query_or_response_format_code
        self.eql_query_name = eql_query_name
        self.eql_query_statement = eql_query_statement

    @property  # get EQL.1
    def query_tag(self) -> ST | None:
        """
        id: EQL.1 | len: 32 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.1
        """
        return self._c_data[0][0]

    @query_tag.setter  # set EQL.1
    def query_tag(self, st: ST | None):
        """
        id: EQL.1 | len: 32 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.1
        """
        self._c_data[0] = (st,)

    @property  # get EQL.2
    def query_or_response_format_code(self) -> QueryOrResponseFormatCode:
        """
        id: EQL.2 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.2
        """
        return self._c_data[1][0]

    @query_or_response_format_code.setter  # set EQL.2
    def query_or_response_format_code(
        self, query_or_response_format_code: QueryOrResponseFormatCode
    ):
        """
        id: EQL.2 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.2
        """
        self._c_data[1] = (query_or_response_format_code,)

    @property  # get EQL.3
    def eql_query_name(self) -> CE:
        """
        id: EQL.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.3
        """
        return self._c_data[2][0]

    @eql_query_name.setter  # set EQL.3
    def eql_query_name(self, ce: CE):
        """
        id: EQL.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.3
        """
        self._c_data[2] = (ce,)

    @property  # get EQL.4
    def eql_query_statement(self) -> ST:
        """
        id: EQL.4 | len: 4096 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.4
        """
        return self._c_data[3][0]

    @eql_query_statement.setter  # set EQL.4
    def eql_query_statement(self, st: ST):
        """
        id: EQL.4 | len: 4096 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQL.4
        """
        self._c_data[3] = (st,)
