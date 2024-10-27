from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..tables.QueryName import QueryName


"""
Query Identification - QID
HL7 Version: 2.5.1

-----BEGIN SEGMENT::QID TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QID,
    CE, ST
)

qid = QID(  #  - The QID segment contains the information necessary to uniquely identify a query
    query_tag=st,  # ST(...)  # Required.
    message_query_name=ce,  # CE(...)  # Required.
)

-----END SEGMENT::QID TEMPLATE-----
"""


class QID(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """QID"""
    _hl7_name = """Query Identification"""
    _hl7_description = """The QID segment contains the information necessary to uniquely identify a query"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QID"
    _c_length = (32, 250,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "R",)
    _c_components = (ST, CE,)
    _c_aliases = ("QID.1", "QID.2",)
    _c_names = ("Query Tag", "Message Query Name",)
    _c_attrs = ("query_tag", "message_query_name",)
    # fmt: on

    def __init__(
        self,
        query_tag: ST,  # QID.1
        message_query_name: QueryName | CE,  # QID.2
    ):
        """
        Query Identification - `QID <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QID>`_
        The QID segment contains the information necessary to uniquely identify a query. Its primary use is in query cancellation or subscription cancellation.

        :param query_tag: String Data (id: QID.1 | len: 32 | use: R | rpt: 1)
        :param message_query_name: Coded Element (id: QID.2 | len: 250 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.query_tag = query_tag
        self.message_query_name = message_query_name

    @property  # get QID.1
    def query_tag(self) -> ST:
        """
        id: QID.1 | len: 32 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QID.1
        """
        return self._c_data[0][0]

    @query_tag.setter  # set QID.1
    def query_tag(self, st: ST):
        """
        id: QID.1 | len: 32 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QID.1
        """
        self._c_data[0] = (st,)

    @property  # get QID.2
    def message_query_name(self) -> QueryName:
        """
        id: QID.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QID.2
        """
        return self._c_data[1][0]

    @message_query_name.setter  # set QID.2
    def message_query_name(self, query_name: QueryName):
        """
        id: QID.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QID.2
        """
        self._c_data[1] = (query_name,)
