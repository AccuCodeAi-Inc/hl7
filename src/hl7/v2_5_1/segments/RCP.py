from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.CQ import CQ
from ..data_types.CE import CE
from ..data_types.SRT import SRT
from ..tables.ResponseModality import ResponseModality
from ..tables.QueryPriority import QueryPriority
from ..tables.SegmentGroup import SegmentGroup
from ..tables.ModifyIndicator import ModifyIndicator


"""
Response Control Parameter - RCP
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RCP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RCP,
    ID, TS, CQ, CE, SRT
)

rcp = RCP(  #  - The RCP segment is used to restrict the amount of data that should be returned in response to query
    query_priority=None,  # ID(...) 
    quantity_limited_request=None,  # CQ(...) 
    response_modality=None,  # CE(...) 
    execution_and_delivery_time=None,  # TS(...) 
    modify_indicator=None,  # ID(...) 
    sort_by_field=None,  # SRT(...) 
    segment_group_inclusion=None,  # ID(...) 
)

-----END SEGMENT::RCP TEMPLATE-----
"""


class RCP(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RCP"""
    _hl7_name = """Response Control Parameter"""
    _hl7_description = """The RCP segment is used to restrict the amount of data that should be returned in response to query"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP"
    _c_length = (1, 10, 250, 26, 1, 512, 256,)
    _c_rpt = (1, 1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("O", "O", "O", "C", "O", "O", "O",)
    _c_components = (ID, CQ, CE, TS, ID, SRT, ID,)
    _c_aliases = ("RCP.1", "RCP.2", "RCP.3", "RCP.4", "RCP.5", "RCP.6", "RCP.7",)
    _c_names = ("Query Priority", "Quantity Limited Request", "Response Modality", "Execution and Delivery Time", "Modify Indicator", "Sort-by Field", "Segment group inclusion",)
    _c_attrs = ("query_priority", "quantity_limited_request", "response_modality", "execution_and_delivery_time", "modify_indicator", "sort_by_field", "segment_group_inclusion",)
    # fmt: on

    def __init__(
        self,
        query_priority: QueryPriority | ID | None = None,  # RCP.1
        quantity_limited_request: CQ | None = None,  # RCP.2
        response_modality: ResponseModality | CE | None = None,  # RCP.3
        execution_and_delivery_time: TS | None = None,  # RCP.4
        modify_indicator: ModifyIndicator | ID | None = None,  # RCP.5
        sort_by_field: SRT | None = None,  # RCP.6
        segment_group_inclusion: SegmentGroup | ID | None = None,  # RCP.7
    ):
        """
        Response Control Parameter - `RCP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCP>`_
        The RCP segment is used to restrict the amount of data that should be returned in response to query.

        :param query_priority: Coded values for HL7 tables (id: RCP.1 | len: 1 | use: O | rpt: 1)
        :param quantity_limited_request: Composite Quantity with Units (id: RCP.2 | len: 10 | use: O | rpt: 1)
        :param response_modality: Coded Element (id: RCP.3 | len: 250 | use: O | rpt: 1)
        :param execution_and_delivery_time: Time Stamp (id: RCP.4 | len: 26 | use: C | rpt: 1)
        :param modify_indicator: Coded values for HL7 tables (id: RCP.5 | len: 1 | use: O | rpt: 1)
        :param sort_by_field: Sort Order (id: RCP.6 | len: 512 | use: O | rpt: *)
        :param segment_group_inclusion: Coded values for HL7 tables (id: RCP.7 | len: 256 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.query_priority = query_priority
        self.quantity_limited_request = quantity_limited_request
        self.response_modality = response_modality
        self.execution_and_delivery_time = execution_and_delivery_time
        self.modify_indicator = modify_indicator
        self.sort_by_field = sort_by_field
        self.segment_group_inclusion = segment_group_inclusion

    @property  # get RCP.1
    def query_priority(self) -> QueryPriority | None:
        """
        id: RCP.1 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.1
        """
        return self._c_data[0][0]

    @query_priority.setter  # set RCP.1
    def query_priority(self, query_priority: QueryPriority | None):
        """
        id: RCP.1 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.1
        """
        self._c_data[0] = (query_priority,)

    @property  # get RCP.2
    def quantity_limited_request(self) -> CQ | None:
        """
        id: RCP.2 | len: 10 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.2
        """
        return self._c_data[1][0]

    @quantity_limited_request.setter  # set RCP.2
    def quantity_limited_request(self, cq: CQ | None):
        """
        id: RCP.2 | len: 10 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.2
        """
        self._c_data[1] = (cq,)

    @property  # get RCP.3
    def response_modality(self) -> ResponseModality | None:
        """
        id: RCP.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.3
        """
        return self._c_data[2][0]

    @response_modality.setter  # set RCP.3
    def response_modality(self, response_modality: ResponseModality | None):
        """
        id: RCP.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.3
        """
        self._c_data[2] = (response_modality,)

    @property  # get RCP.4
    def execution_and_delivery_time(self) -> TS | None:
        """
        id: RCP.4 | len: 26 | use: C | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.4
        """
        return self._c_data[3][0]

    @execution_and_delivery_time.setter  # set RCP.4
    def execution_and_delivery_time(self, ts: TS | None):
        """
        id: RCP.4 | len: 26 | use: C | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.4
        """
        self._c_data[3] = (ts,)

    @property  # get RCP.5
    def modify_indicator(self) -> ModifyIndicator | None:
        """
        id: RCP.5 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.5
        """
        return self._c_data[4][0]

    @modify_indicator.setter  # set RCP.5
    def modify_indicator(self, modify_indicator: ModifyIndicator | None):
        """
        id: RCP.5 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.5
        """
        self._c_data[4] = (modify_indicator,)

    @property
    def sort_by_field(self) -> tuple[SRT, ...] | tuple[None]:
        """
        id: RCP.6 | len: 512 | use: O | rpt: *
        ---
        return_type: tuple[SRT, ...]: (Sort Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.6
        """
        return self._c_data[5]

    @sort_by_field.setter  # set RCP.6
    def sort_by_field(self, srt: SRT | tuple[SRT] | None):
        """
        id: RCP.6 | len: 512 | use: O | rpt: *
        ---
        param_type: SRT | tuple[SRT, ...]: (Sort Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.6
        """
        if isinstance(srt, tuple):
            self._c_data[5] = srt
        else:
            self._c_data[5] = (srt,)

    @property
    def segment_group_inclusion(self) -> tuple[SegmentGroup, ...] | tuple[None]:
        """
        id: RCP.7 | len: 256 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.7
        """
        return self._c_data[6]

    @segment_group_inclusion.setter  # set RCP.7
    def segment_group_inclusion(
        self, segment_group: SegmentGroup | tuple[SegmentGroup] | None
    ):
        """
        id: RCP.7 | len: 256 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCP.7
        """
        if isinstance(segment_group, tuple):
            self._c_data[6] = segment_group
        else:
            self._c_data[6] = (segment_group,)
