from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.QIP import QIP
from ..data_types.ID import ID
from ..tables.QueryOrResponseFormatCode import QueryOrResponseFormatCode


"""
Stored Procedure Request Definition - SPR
HL7 Version: 2.5.1

-----BEGIN SEGMENT::SPR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SPR,
    ST, CE, QIP, ID
)

spr = SPR(  #  - This segment is not carried forward to the recommended queries for v 2
    query_tag=None,  # ST(...) 
    query_or_response_format_code=id,  # ID(...)  # Required.
    stored_procedure_name=ce,  # CE(...)  # Required.
    input_parameter_list=None,  # QIP(...) 
)

-----END SEGMENT::SPR TEMPLATE-----
"""


class SPR(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """SPR"""
    _hl7_name = """Stored Procedure Request Definition"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPR"
    _c_length = (32, 1, 250, 256,)
    _c_rpt = (1, 1, 1, 65535,)
    _c_usage = ("O", "R", "R", "O",)
    _c_components = (ST, ID, CE, QIP,)
    _c_aliases = ("SPR.1", "SPR.2", "SPR.3", "SPR.4",)
    _c_names = ("Query Tag", "Query/Response Format Code", "Stored Procedure Name", "Input Parameter List",)
    _c_attrs = ("query_tag", "query_or_response_format_code", "stored_procedure_name", "input_parameter_list",)
    # fmt: on

    def __init__(
        self,
        query_or_response_format_code: QueryOrResponseFormatCode
        | ID
        | tuple[QueryOrResponseFormatCode | ID, ...],  # SPR.2
        stored_procedure_name: CE | tuple[CE, ...],  # SPR.3
        query_tag: ST | tuple[ST, ...] | None = None,  # SPR.1
        input_parameter_list: QIP | tuple[QIP, ...] | None = None,  # SPR.4
    ):
        """
                Stored Procedure Request Definition - `SPR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPR>`_
                This segment is not carried forward to the recommended queries for v 2.4.

        The SPR segment is used to issue queries using stored procedure calls.  Refer to the functional chapters for the lists of HL7-defined stored procedure names, input parameters and output tables.

                :param query_tag: String Data (id: SPR.1 | len: 32 | use: O | rpt: 1)
                :param query_or_response_format_code: Coded values for HL7 tables (id: SPR.2 | len: 1 | use: R | rpt: 1)
                :param stored_procedure_name: Coded Element (id: SPR.3 | len: 250 | use: R | rpt: 1)
                :param input_parameter_list: Query Input Parameter List (id: SPR.4 | len: 256 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.query_tag = query_tag
        self.query_or_response_format_code = query_or_response_format_code
        self.stored_procedure_name = stored_procedure_name
        self.input_parameter_list = input_parameter_list

    @property  # get SPR.1
    def query_tag(self) -> ST | None:
        """
        id: SPR.1 | len: 32 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.1
        """
        return self._c_data[0][0]

    @query_tag.setter  # set SPR.1
    def query_tag(self, st: ST | None):
        """
        id: SPR.1 | len: 32 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.1
        """
        self._c_data[0] = (st,)

    @property  # get SPR.2
    def query_or_response_format_code(self) -> QueryOrResponseFormatCode:
        """
        id: SPR.2 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.2
        """
        return self._c_data[1][0]

    @query_or_response_format_code.setter  # set SPR.2
    def query_or_response_format_code(
        self, query_or_response_format_code: QueryOrResponseFormatCode
    ):
        """
        id: SPR.2 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.2
        """
        self._c_data[1] = (query_or_response_format_code,)

    @property  # get SPR.3
    def stored_procedure_name(self) -> CE:
        """
        id: SPR.3 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.3
        """
        return self._c_data[2][0]

    @stored_procedure_name.setter  # set SPR.3
    def stored_procedure_name(self, ce: CE):
        """
        id: SPR.3 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.3
        """
        self._c_data[2] = (ce,)

    @property
    def input_parameter_list(self) -> tuple[QIP, ...] | tuple[None]:
        """
        id: SPR.4 | len: 256 | use: O | rpt: *
        ---
        return_type: tuple[QIP, ...]: (Query Input Parameter List, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.4
        """
        return self._c_data[3]

    @input_parameter_list.setter  # set SPR.4
    def input_parameter_list(self, qip: QIP | tuple[QIP] | None):
        """
        id: SPR.4 | len: 256 | use: O | rpt: *
        ---
        param_type: QIP | tuple[QIP, ...]: (Query Input Parameter List, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SPR.4
        """
        if isinstance(qip, tuple):
            self._c_data[3] = qip
        else:
            self._c_data[3] = (qip,)
