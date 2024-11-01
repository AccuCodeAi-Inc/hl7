from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CQ import CQ
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.VR import VR
from ..data_types.XCN import XCN
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..tables.QueryPriority import QueryPriority
from ..tables.WhatSubjectFilter import WhatSubjectFilter
from ..tables.QueryResultsLevel import QueryResultsLevel
from ..tables.DeferredResponseType import DeferredResponseType
from ..tables.QueryOrResponseFormatCode import QueryOrResponseFormatCode


"""
Original-Style Query Definition - QRD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::QRD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QRD,
    CQ, TS, ID, VR, XCN, ST, CE
)

qrd = QRD(  #  - This segment is not carried forward to the recommended queries for v 2
    query_date_or_time=ts,  # TS(...)  # Required.
    query_format_code=id,  # ID(...)  # Required.
    query_priority=id,  # ID(...)  # Required.
    query_id=st,  # ST(...)  # Required.
    deferred_response_type=None,  # ID(...) 
    deferred_response_date_or_time=None,  # TS(...) 
    quantity_limited_request=cq,  # CQ(...)  # Required.
    who_subject_filter=xcn,  # XCN(...)  # Required.
    what_subject_filter=ce,  # CE(...)  # Required.
    what_department_data_code=ce,  # CE(...)  # Required.
    what_data_code_value_qual=None,  # VR(...) 
    query_results_level=None,  # ID(...) 
)

-----END SEGMENT::QRD TEMPLATE-----
"""


class QRD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """QRD"""
    _hl7_name = """Original-Style Query Definition"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD"
    _c_length = (26, 1, 1, 10, 1, 26, 10, 250, 250, 250, 20, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 65535, 65535, 65535, 65535, 1,)
    _c_usage = ("R", "R", "R", "R", "O", "O", "R", "R", "R", "R", "O", "O",)
    _c_components = (TS, ID, ID, ST, ID, TS, CQ, XCN, CE, CE, VR, ID,)
    _c_aliases = ("QRD.1", "QRD.2", "QRD.3", "QRD.4", "QRD.5", "QRD.6", "QRD.7", "QRD.8", "QRD.9", "QRD.10", "QRD.11", "QRD.12",)
    _c_names = ("Query Date/Time", "Query Format Code", "Query Priority", "Query ID", "Deferred Response Type", "Deferred Response Date/Time", "Quantity Limited Request", "Who Subject Filter", "What Subject Filter", "What Department Data Code", "What Data Code Value Qual.", "Query Results Level",)
    _c_attrs = ("query_date_or_time", "query_format_code", "query_priority", "query_id", "deferred_response_type", "deferred_response_date_or_time", "quantity_limited_request", "who_subject_filter", "what_subject_filter", "what_department_data_code", "what_data_code_value_qual", "query_results_level",)
    # fmt: on

    def __init__(
        self,
        query_date_or_time: TS | tuple[TS],  # QRD.1
        query_format_code: QueryOrResponseFormatCode
        | ID
        | tuple[QueryOrResponseFormatCode | ID],  # QRD.2
        query_priority: QueryPriority | ID | tuple[QueryPriority | ID],  # QRD.3
        query_id: ST | tuple[ST],  # QRD.4
        quantity_limited_request: CQ | tuple[CQ],  # QRD.7
        who_subject_filter: XCN | tuple[XCN],  # QRD.8
        what_subject_filter: WhatSubjectFilter
        | CE
        | tuple[WhatSubjectFilter | CE],  # QRD.9
        what_department_data_code: CE | tuple[CE],  # QRD.10
        deferred_response_type: DeferredResponseType
        | ID
        | tuple[DeferredResponseType | ID]
        | None = None,  # QRD.5
        deferred_response_date_or_time: TS | tuple[TS] | None = None,  # QRD.6
        what_data_code_value_qual: VR | tuple[VR] | None = None,  # QRD.11
        query_results_level: QueryResultsLevel
        | ID
        | tuple[QueryResultsLevel | ID]
        | None = None,  # QRD.12
    ):
        """
                Original-Style Query Definition - `QRD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD>`_
                This segment is not carried forward to the recommended queries for v 2.4.

        The QRD segment is used to define a query.

                :param query_date_or_time: Time Stamp (id: QRD.1 | len: 26 | use: R | rpt: 1)
                :param query_format_code: Coded values for HL7 tables (id: QRD.2 | len: 1 | use: R | rpt: 1)
                :param query_priority: Coded values for HL7 tables (id: QRD.3 | len: 1 | use: R | rpt: 1)
                :param query_id: String Data (id: QRD.4 | len: 10 | use: R | rpt: 1)
                :param deferred_response_type: Coded values for HL7 tables (id: QRD.5 | len: 1 | use: O | rpt: 1)
                :param deferred_response_date_or_time: Time Stamp (id: QRD.6 | len: 26 | use: O | rpt: 1)
                :param quantity_limited_request: Composite Quantity with Units (id: QRD.7 | len: 10 | use: R | rpt: 1)
                :param who_subject_filter: Extended Composite ID Number and Name for Persons (id: QRD.8 | len: 250 | use: R | rpt: *)
                :param what_subject_filter: Coded Element (id: QRD.9 | len: 250 | use: R | rpt: *)
                :param what_department_data_code: Coded Element (id: QRD.10 | len: 250 | use: R | rpt: *)
                :param what_data_code_value_qual: Value Range (id: QRD.11 | len: 20 | use: O | rpt: *)
                :param query_results_level: Coded values for HL7 tables (id: QRD.12 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.query_date_or_time = query_date_or_time
        self.query_format_code = query_format_code
        self.query_priority = query_priority
        self.query_id = query_id
        self.deferred_response_type = deferred_response_type
        self.deferred_response_date_or_time = deferred_response_date_or_time
        self.quantity_limited_request = quantity_limited_request
        self.who_subject_filter = who_subject_filter
        self.what_subject_filter = what_subject_filter
        self.what_department_data_code = what_department_data_code
        self.what_data_code_value_qual = what_data_code_value_qual
        self.query_results_level = query_results_level

    @property  # get QRD.1
    def query_date_or_time(self) -> TS:
        """
        id: QRD.1 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.1
        """
        return self._c_data[0][0]

    @query_date_or_time.setter  # set QRD.1
    def query_date_or_time(self, ts: TS):
        """
        id: QRD.1 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.1
        """
        self._c_data[0] = (ts,)

    @property  # get QRD.2
    def query_format_code(self) -> QueryOrResponseFormatCode:
        """
        id: QRD.2 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.2
        """
        return self._c_data[1][0]

    @query_format_code.setter  # set QRD.2
    def query_format_code(
        self, query_or_response_format_code: QueryOrResponseFormatCode
    ):
        """
        id: QRD.2 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.2
        """
        self._c_data[1] = (query_or_response_format_code,)

    @property  # get QRD.3
    def query_priority(self) -> QueryPriority:
        """
        id: QRD.3 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.3
        """
        return self._c_data[2][0]

    @query_priority.setter  # set QRD.3
    def query_priority(self, query_priority: QueryPriority):
        """
        id: QRD.3 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.3
        """
        self._c_data[2] = (query_priority,)

    @property  # get QRD.4
    def query_id(self) -> ST:
        """
        id: QRD.4 | len: 10 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.4
        """
        return self._c_data[3][0]

    @query_id.setter  # set QRD.4
    def query_id(self, st: ST):
        """
        id: QRD.4 | len: 10 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.4
        """
        self._c_data[3] = (st,)

    @property  # get QRD.5
    def deferred_response_type(self) -> DeferredResponseType | None:
        """
        id: QRD.5 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.5
        """
        return self._c_data[4][0]

    @deferred_response_type.setter  # set QRD.5
    def deferred_response_type(
        self, deferred_response_type: DeferredResponseType | None
    ):
        """
        id: QRD.5 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.5
        """
        self._c_data[4] = (deferred_response_type,)

    @property  # get QRD.6
    def deferred_response_date_or_time(self) -> TS | None:
        """
        id: QRD.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.6
        """
        return self._c_data[5][0]

    @deferred_response_date_or_time.setter  # set QRD.6
    def deferred_response_date_or_time(self, ts: TS | None):
        """
        id: QRD.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.6
        """
        self._c_data[5] = (ts,)

    @property  # get QRD.7
    def quantity_limited_request(self) -> CQ:
        """
        id: QRD.7 | len: 10 | use: R | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.7
        """
        return self._c_data[6][0]

    @quantity_limited_request.setter  # set QRD.7
    def quantity_limited_request(self, cq: CQ):
        """
        id: QRD.7 | len: 10 | use: R | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.7
        """
        self._c_data[6] = (cq,)

    @property
    def who_subject_filter(self) -> tuple[XCN, ...]:
        """
        id: QRD.8 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.8
        """
        return self._c_data[7]

    @who_subject_filter.setter  # set QRD.8
    def who_subject_filter(self, xcn: XCN | tuple[XCN]):
        """
        id: QRD.8 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.8
        """
        if isinstance(xcn, tuple):
            self._c_data[7] = xcn
        else:
            self._c_data[7] = (xcn,)

    @property
    def what_subject_filter(self) -> tuple[WhatSubjectFilter, ...]:
        """
        id: QRD.9 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.9
        """
        return self._c_data[8]

    @what_subject_filter.setter  # set QRD.9
    def what_subject_filter(
        self, what_subject_filter: WhatSubjectFilter | tuple[WhatSubjectFilter]
    ):
        """
        id: QRD.9 | len: 250 | use: R | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.9
        """
        if isinstance(what_subject_filter, tuple):
            self._c_data[8] = what_subject_filter
        else:
            self._c_data[8] = (what_subject_filter,)

    @property
    def what_department_data_code(self) -> tuple[CE, ...]:
        """
        id: QRD.10 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.10
        """
        return self._c_data[9]

    @what_department_data_code.setter  # set QRD.10
    def what_department_data_code(self, ce: CE | tuple[CE]):
        """
        id: QRD.10 | len: 250 | use: R | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.10
        """
        if isinstance(ce, tuple):
            self._c_data[9] = ce
        else:
            self._c_data[9] = (ce,)

    @property
    def what_data_code_value_qual(self) -> tuple[VR, ...] | tuple[None]:
        """
        id: QRD.11 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[VR, ...]: (Value Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.11
        """
        return self._c_data[10]

    @what_data_code_value_qual.setter  # set QRD.11
    def what_data_code_value_qual(self, vr: VR | tuple[VR] | None):
        """
        id: QRD.11 | len: 20 | use: O | rpt: *
        ---
        param_type: VR | tuple[VR, ...]: (Value Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.11
        """
        if isinstance(vr, tuple):
            self._c_data[10] = vr
        else:
            self._c_data[10] = (vr,)

    @property  # get QRD.12
    def query_results_level(self) -> QueryResultsLevel | None:
        """
        id: QRD.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.12
        """
        return self._c_data[11][0]

    @query_results_level.setter  # set QRD.12
    def query_results_level(self, query_results_level: QueryResultsLevel | None):
        """
        id: QRD.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRD.12
        """
        self._c_data[11] = (query_results_level,)
