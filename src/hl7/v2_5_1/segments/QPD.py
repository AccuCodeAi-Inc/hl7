from __future__ import annotations
from ...base import HL7Segment
from ..data_types.VARIES import VARIES
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..tables.QueryName import QueryName


"""
Query Parameter Definition - QPD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::QPD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QPD,
    VARIES, ST, CE
)

qpd = QPD(  #  - The QPD segment defines the parameters of the query
    message_query_name=ce,  # CE(...)  # Required.
    query_tag=None,  # ST(...) 
    user_parameters=None,  # VARIES(...) 
)

-----END SEGMENT::QPD TEMPLATE-----
"""


class QPD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """QPD"""
    _hl7_name = """Query Parameter Definition"""
    _hl7_description = """The QPD segment defines the parameters of the query"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QPD"
    _c_length = (250, 32, 256,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "C", "O",)
    _c_components = (CE, ST, VARIES,)
    _c_aliases = ("QPD.1", "QPD.2", "QPD.3",)
    _c_names = ("Message Query Name", "Query Tag", "User Parameters (in successive fields)",)
    _c_attrs = ("message_query_name", "query_tag", "user_parameters",)
    # fmt: on

    def __init__(
        self,
        message_query_name: QueryName | CE | tuple[QueryName | CE],  # QPD.1
        query_tag: ST | tuple[ST] | None = None,  # QPD.2
        user_parameters: VARIES | tuple[VARIES] | None = None,  # QPD.3
    ):
        """
        Query Parameter Definition - `QPD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QPD>`_
        The QPD segment defines the parameters of the query.

        :param message_query_name: Coded Element (id: QPD.1 | len: 250 | use: R | rpt: 1)
        :param query_tag: String Data (id: QPD.2 | len: 32 | use: C | rpt: 1)
        :param user_parameters: Variable Datatype (id: QPD.3 | len: 256 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.message_query_name = message_query_name
        self.query_tag = query_tag
        self.user_parameters = user_parameters

    @property  # get QPD.1
    def message_query_name(self) -> QueryName:
        """
        id: QPD.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QPD.1
        """
        return self._c_data[0][0]

    @message_query_name.setter  # set QPD.1
    def message_query_name(self, query_name: QueryName):
        """
        id: QPD.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QPD.1
        """
        self._c_data[0] = (query_name,)

    @property  # get QPD.2
    def query_tag(self) -> ST | None:
        """
        id: QPD.2 | len: 32 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QPD.2
        """
        return self._c_data[1][0]

    @query_tag.setter  # set QPD.2
    def query_tag(self, st: ST | None):
        """
        id: QPD.2 | len: 32 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QPD.2
        """
        self._c_data[1] = (st,)

    @property  # get QPD.3
    def user_parameters(self) -> VARIES | None:
        """
        id: QPD.3 | len: 256 | use: O | rpt: 1
        ---
        return_type: VARIES: Variable Datatype
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QPD.3
        """
        return self._c_data[2][0]

    @user_parameters.setter  # set QPD.3
    def user_parameters(self, varies: VARIES | None):
        """
        id: QPD.3 | len: 256 | use: O | rpt: 1
        ---
        param_type: VARIES: Variable Datatype
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QPD.3
        """
        self._c_data[2] = (varies,)
