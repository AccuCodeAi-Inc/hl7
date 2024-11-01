from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..tables.QueryName import QueryName
from ..tables.QueryResponseStatus import QueryResponseStatus


"""
Query Acknowledgment - QAK
HL7 Version: 2.5.1

-----BEGIN SEGMENT::QAK TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QAK,
    ST, CE, ID, NM
)

qak = QAK(  #  - The QAK segment contains information sent with responses to a query
    query_tag=None,  # ST(...) 
    query_response_status=None,  # ID(...) 
    message_query_name=None,  # CE(...) 
    hit_count=None,  # NM(...) 
    this_payload=None,  # NM(...) 
    hits_remaining=None,  # NM(...) 
)

-----END SEGMENT::QAK TEMPLATE-----
"""


class QAK(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """QAK"""
    _hl7_name = """Query Acknowledgment"""
    _hl7_description = """The QAK segment contains information sent with responses to a query"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK"
    _c_length = (32, 2, 250, 10, 10, 10,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("C", "O", "O", "O", "O", "O",)
    _c_components = (ST, ID, CE, NM, NM, NM,)
    _c_aliases = ("QAK.1", "QAK.2", "QAK.3", "QAK.4", "QAK.5", "QAK.6",)
    _c_names = ("Query Tag", "Query Response Status", "Message Query Name", "Hit Count", "This payload", "Hits remaining",)
    _c_attrs = ("query_tag", "query_response_status", "message_query_name", "hit_count", "this_payload", "hits_remaining",)
    # fmt: on

    def __init__(
        self,
        query_tag: ST | tuple[ST, ...] | None = None,  # QAK.1
        query_response_status: QueryResponseStatus
        | ID
        | tuple[QueryResponseStatus | ID, ...]
        | None = None,  # QAK.2
        message_query_name: QueryName
        | CE
        | tuple[QueryName | CE, ...]
        | None = None,  # QAK.3
        hit_count: NM | tuple[NM, ...] | None = None,  # QAK.4
        this_payload: NM | tuple[NM, ...] | None = None,  # QAK.5
        hits_remaining: NM | tuple[NM, ...] | None = None,  # QAK.6
    ):
        """
        Query Acknowledgment - `QAK <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK>`_
        The QAK segment contains information sent with responses to a query. Although the QAK segment is required in the responses to the enhanced queries, it may appear as an optional segment placed after the (optional) ERR segment in any query response (message) to any original mode query.

        :param query_tag: String Data (id: QAK.1 | len: 32 | use: C | rpt: 1)
        :param query_response_status: Coded values for HL7 tables (id: QAK.2 | len: 2 | use: O | rpt: 1)
        :param message_query_name: Coded Element (id: QAK.3 | len: 250 | use: O | rpt: 1)
        :param hit_count: Numeric (id: QAK.4 | len: 10 | use: O | rpt: 1)
        :param this_payload: Numeric (id: QAK.5 | len: 10 | use: O | rpt: 1)
        :param hits_remaining: Numeric (id: QAK.6 | len: 10 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.query_tag = query_tag
        self.query_response_status = query_response_status
        self.message_query_name = message_query_name
        self.hit_count = hit_count
        self.this_payload = this_payload
        self.hits_remaining = hits_remaining

    @property  # get QAK.1
    def query_tag(self) -> ST | None:
        """
        id: QAK.1 | len: 32 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.1
        """
        return self._c_data[0][0]

    @query_tag.setter  # set QAK.1
    def query_tag(self, st: ST | None):
        """
        id: QAK.1 | len: 32 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.1
        """
        self._c_data[0] = (st,)

    @property  # get QAK.2
    def query_response_status(self) -> QueryResponseStatus | None:
        """
        id: QAK.2 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.2
        """
        return self._c_data[1][0]

    @query_response_status.setter  # set QAK.2
    def query_response_status(self, query_response_status: QueryResponseStatus | None):
        """
        id: QAK.2 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.2
        """
        self._c_data[1] = (query_response_status,)

    @property  # get QAK.3
    def message_query_name(self) -> QueryName | None:
        """
        id: QAK.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.3
        """
        return self._c_data[2][0]

    @message_query_name.setter  # set QAK.3
    def message_query_name(self, query_name: QueryName | None):
        """
        id: QAK.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.3
        """
        self._c_data[2] = (query_name,)

    @property  # get QAK.4
    def hit_count(self) -> NM | None:
        """
        id: QAK.4 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.4
        """
        return self._c_data[3][0]

    @hit_count.setter  # set QAK.4
    def hit_count(self, nm: NM | None):
        """
        id: QAK.4 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.4
        """
        self._c_data[3] = (nm,)

    @property  # get QAK.5
    def this_payload(self) -> NM | None:
        """
        id: QAK.5 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.5
        """
        return self._c_data[4][0]

    @this_payload.setter  # set QAK.5
    def this_payload(self, nm: NM | None):
        """
        id: QAK.5 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.5
        """
        self._c_data[4] = (nm,)

    @property  # get QAK.6
    def hits_remaining(self) -> NM | None:
        """
        id: QAK.6 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.6
        """
        return self._c_data[5][0]

    @hits_remaining.setter  # set QAK.6
    def hits_remaining(self, nm: NM | None):
        """
        id: QAK.6 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QAK.6
        """
        self._c_data[5] = (nm,)
