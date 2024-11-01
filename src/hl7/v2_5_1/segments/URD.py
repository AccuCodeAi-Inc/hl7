from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.ST import ST
from ..data_types.XCN import XCN
from ..data_types.TS import TS
from ..tables.QueryResultsLevel import QueryResultsLevel
from ..tables.ReportPriority import ReportPriority
from ..tables.WhatSubjectFilter import WhatSubjectFilter


"""
Results/update Definition - URD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::URD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    URD,
    CE, ID, ST, XCN, TS
)

urd = URD(  #  - This segment is not carried forward to the recommended queries for v 2
    r_or_u_date_or_time=None,  # TS(...) 
    report_priority=None,  # ID(...) 
    r_or_u_who_subject_definition=xcn,  # XCN(...)  # Required.
    r_or_u_what_subject_definition=None,  # CE(...) 
    r_or_u_what_department_code=None,  # CE(...) 
    r_or_u_display_or_print_locations=None,  # ST(...) 
    r_or_u_results_level=None,  # ID(...) 
)

-----END SEGMENT::URD TEMPLATE-----
"""


class URD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """URD"""
    _hl7_name = """Results/update Definition"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URD"
    _c_length = (26, 1, 250, 250, 250, 20, 1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 1,)
    _c_usage = ("O", "O", "R", "O", "O", "O", "O",)
    _c_components = (TS, ID, XCN, CE, CE, ST, ID,)
    _c_aliases = ("URD.1", "URD.2", "URD.3", "URD.4", "URD.5", "URD.6", "URD.7",)
    _c_names = ("R/U Date/Time", "Report Priority", "R/U Who Subject Definition", "R/U What Subject Definition", "R/U What Department Code", "R/U Display/Print Locations", "R/U Results Level",)
    _c_attrs = ("r_or_u_date_or_time", "report_priority", "r_or_u_who_subject_definition", "r_or_u_what_subject_definition", "r_or_u_what_department_code", "r_or_u_display_or_print_locations", "r_or_u_results_level",)
    # fmt: on

    def __init__(
        self,
        r_or_u_who_subject_definition: XCN,  # URD.3
        r_or_u_date_or_time: TS | None = None,  # URD.1
        report_priority: ReportPriority | ID | None = None,  # URD.2
        r_or_u_what_subject_definition: WhatSubjectFilter | CE | None = None,  # URD.4
        r_or_u_what_department_code: CE | None = None,  # URD.5
        r_or_u_display_or_print_locations: ST | None = None,  # URD.6
        r_or_u_results_level: QueryResultsLevel | ID | None = None,  # URD.7
    ):
        """
                Results/update Definition - `URD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URD>`_
                This segment is not carried forward to the recommended queries for v 2.4.

        The URD segment is used in sending unsolicited updates about orders and results.  Its purpose is similar to that of the QRD segment, but from the results/unsolicited update point of view.  Some of the fields have parallels in the QRD segment.

                :param r_or_u_date_or_time: Time Stamp (id: URD.1 | len: 26 | use: O | rpt: 1)
                :param report_priority: Coded values for HL7 tables (id: URD.2 | len: 1 | use: O | rpt: 1)
                :param r_or_u_who_subject_definition: Extended Composite ID Number and Name for Persons (id: URD.3 | len: 250 | use: R | rpt: *)
                :param r_or_u_what_subject_definition: Coded Element (id: URD.4 | len: 250 | use: O | rpt: *)
                :param r_or_u_what_department_code: Coded Element (id: URD.5 | len: 250 | use: O | rpt: *)
                :param r_or_u_display_or_print_locations: String Data (id: URD.6 | len: 20 | use: O | rpt: *)
                :param r_or_u_results_level: Coded values for HL7 tables (id: URD.7 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.r_or_u_date_or_time = r_or_u_date_or_time
        self.report_priority = report_priority
        self.r_or_u_who_subject_definition = r_or_u_who_subject_definition
        self.r_or_u_what_subject_definition = r_or_u_what_subject_definition
        self.r_or_u_what_department_code = r_or_u_what_department_code
        self.r_or_u_display_or_print_locations = r_or_u_display_or_print_locations
        self.r_or_u_results_level = r_or_u_results_level

    @property  # get URD.1
    def r_or_u_date_or_time(self) -> TS | None:
        """
        id: URD.1 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.1
        """
        return self._c_data[0][0]

    @r_or_u_date_or_time.setter  # set URD.1
    def r_or_u_date_or_time(self, ts: TS | None):
        """
        id: URD.1 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.1
        """
        self._c_data[0] = (ts,)

    @property  # get URD.2
    def report_priority(self) -> ReportPriority | None:
        """
        id: URD.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.2
        """
        return self._c_data[1][0]

    @report_priority.setter  # set URD.2
    def report_priority(self, report_priority: ReportPriority | None):
        """
        id: URD.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.2
        """
        self._c_data[1] = (report_priority,)

    @property
    def r_or_u_who_subject_definition(self) -> tuple[XCN, ...]:
        """
        id: URD.3 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.3
        """
        return self._c_data[2]

    @r_or_u_who_subject_definition.setter  # set URD.3
    def r_or_u_who_subject_definition(self, xcn: XCN | tuple[XCN]):
        """
        id: URD.3 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.3
        """
        if isinstance(xcn, tuple):
            self._c_data[2] = xcn
        else:
            self._c_data[2] = (xcn,)

    @property
    def r_or_u_what_subject_definition(
        self,
    ) -> tuple[WhatSubjectFilter, ...] | tuple[None]:
        """
        id: URD.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.4
        """
        return self._c_data[3]

    @r_or_u_what_subject_definition.setter  # set URD.4
    def r_or_u_what_subject_definition(
        self, what_subject_filter: WhatSubjectFilter | tuple[WhatSubjectFilter] | None
    ):
        """
        id: URD.4 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.4
        """
        if isinstance(what_subject_filter, tuple):
            self._c_data[3] = what_subject_filter
        else:
            self._c_data[3] = (what_subject_filter,)

    @property
    def r_or_u_what_department_code(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: URD.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.5
        """
        return self._c_data[4]

    @r_or_u_what_department_code.setter  # set URD.5
    def r_or_u_what_department_code(self, ce: CE | tuple[CE] | None):
        """
        id: URD.5 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.5
        """
        if isinstance(ce, tuple):
            self._c_data[4] = ce
        else:
            self._c_data[4] = (ce,)

    @property
    def r_or_u_display_or_print_locations(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: URD.6 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.6
        """
        return self._c_data[5]

    @r_or_u_display_or_print_locations.setter  # set URD.6
    def r_or_u_display_or_print_locations(self, st: ST | tuple[ST] | None):
        """
        id: URD.6 | len: 20 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.6
        """
        if isinstance(st, tuple):
            self._c_data[5] = st
        else:
            self._c_data[5] = (st,)

    @property  # get URD.7
    def r_or_u_results_level(self) -> QueryResultsLevel | None:
        """
        id: URD.7 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.7
        """
        return self._c_data[6][0]

    @r_or_u_results_level.setter  # set URD.7
    def r_or_u_results_level(self, query_results_level: QueryResultsLevel | None):
        """
        id: URD.7 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URD.7
        """
        self._c_data[6] = (query_results_level,)
