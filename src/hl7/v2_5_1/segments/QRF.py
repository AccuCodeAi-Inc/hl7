from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.TQ import TQ
from ..data_types.ST import ST
from ..data_types.NM import NM
from ..tables.DateOrTimeSelectionQualifier import DateOrTimeSelectionQualifier
from ..tables.WhichDateOrTimeQualifier import WhichDateOrTimeQualifier
from ..tables.WhichDateOrTimeStatusQualifier import WhichDateOrTimeStatusQualifier


"""
Original style query filter - QRF
HL7 Version: 2.5.1

-----BEGIN SEGMENT::QRF TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    QRF,
    ID, TS, TQ, ST, NM
)

qrf = QRF(  #  - This segment is not carried forward to the recommended queries for v 2
    where_subject_filter=st,  # ST(...)  # Required.
    when_data_start_date_or_time=None,  # TS(...) 
    when_data_end_date_or_time=None,  # TS(...) 
    what_user_qualifier=None,  # ST(...) 
    other_qry_subject_filter=None,  # ST(...) 
    which_date_or_time_qualifier=None,  # ID(...) 
    which_date_or_time_status_qualifier=None,  # ID(...) 
    date_or_time_selection_qualifier=None,  # ID(...) 
    when_quantity_or_timing_qualifier=None,  # TQ(...) 
    search_confidence_threshold=None,  # NM(...) 
)

-----END SEGMENT::QRF TEMPLATE-----
"""


class QRF(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """QRF"""
    _hl7_name = """Original style query filter"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF"
    _c_length = (20, 26, 26, 60, 60, 12, 12, 12, 60, 10,)
    _c_rpt = (65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 1,)
    _c_usage = ("R", "B", "B", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ST, TS, TS, ST, ST, ID, ID, ID, TQ, NM,)
    _c_aliases = ("QRF.1", "QRF.2", "QRF.3", "QRF.4", "QRF.5", "QRF.6", "QRF.7", "QRF.8", "QRF.9", "QRF.10",)
    _c_names = ("Where Subject Filter", "When Data Start Date/Time", "When Data End Date/Time", "What User Qualifier", "Other QRY Subject Filter", "Which Date/Time Qualifier", "Which Date/Time Status Qualifier", "Date/Time Selection Qualifier", "When Quantity/Timing Qualifier", "Search Confidence Threshold",)
    _c_attrs = ("where_subject_filter", "when_data_start_date_or_time", "when_data_end_date_or_time", "what_user_qualifier", "other_qry_subject_filter", "which_date_or_time_qualifier", "which_date_or_time_status_qualifier", "date_or_time_selection_qualifier", "when_quantity_or_timing_qualifier", "search_confidence_threshold",)
    # fmt: on

    def __init__(
        self,
        where_subject_filter: ST,  # QRF.1
        when_data_start_date_or_time: TS | None = None,  # QRF.2
        when_data_end_date_or_time: TS | None = None,  # QRF.3
        what_user_qualifier: ST | None = None,  # QRF.4
        other_qry_subject_filter: ST | None = None,  # QRF.5
        which_date_or_time_qualifier: WhichDateOrTimeQualifier
        | ID
        | None = None,  # QRF.6
        which_date_or_time_status_qualifier: WhichDateOrTimeStatusQualifier
        | ID
        | None = None,  # QRF.7
        date_or_time_selection_qualifier: DateOrTimeSelectionQualifier
        | ID
        | None = None,  # QRF.8
        when_quantity_or_timing_qualifier: TQ | None = None,  # QRF.9
        search_confidence_threshold: NM | None = None,  # QRF.10
    ):
        """
                Original style query filter - `QRF <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF>`_
                This segment is not carried forward to the recommended queries for v 2.4.

        The QRF segment is used with the QRD segment to further refine the content of an original style query.

                :param where_subject_filter: String Data (id: QRF.1 | len: 20 | use: R | rpt: *)
                :param when_data_start_date_or_time: Time Stamp (id: QRF.2 | len: 26 | use: B | rpt: 1)
                :param when_data_end_date_or_time: Time Stamp (id: QRF.3 | len: 26 | use: B | rpt: 1)
                :param what_user_qualifier: String Data (id: QRF.4 | len: 60 | use: O | rpt: *)
                :param other_qry_subject_filter: String Data (id: QRF.5 | len: 60 | use: O | rpt: *)
                :param which_date_or_time_qualifier: Coded values for HL7 tables (id: QRF.6 | len: 12 | use: O | rpt: *)
                :param which_date_or_time_status_qualifier: Coded values for HL7 tables (id: QRF.7 | len: 12 | use: O | rpt: *)
                :param date_or_time_selection_qualifier: Coded values for HL7 tables (id: QRF.8 | len: 12 | use: O | rpt: *)
                :param when_quantity_or_timing_qualifier: Timing Quantity (id: QRF.9 | len: 60 | use: O | rpt: 1)
                :param search_confidence_threshold: Numeric (id: QRF.10 | len: 10 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.where_subject_filter = where_subject_filter
        self.when_data_start_date_or_time = when_data_start_date_or_time
        self.when_data_end_date_or_time = when_data_end_date_or_time
        self.what_user_qualifier = what_user_qualifier
        self.other_qry_subject_filter = other_qry_subject_filter
        self.which_date_or_time_qualifier = which_date_or_time_qualifier
        self.which_date_or_time_status_qualifier = which_date_or_time_status_qualifier
        self.date_or_time_selection_qualifier = date_or_time_selection_qualifier
        self.when_quantity_or_timing_qualifier = when_quantity_or_timing_qualifier
        self.search_confidence_threshold = search_confidence_threshold

    @property
    def where_subject_filter(self) -> tuple[ST, ...]:
        """
        id: QRF.1 | len: 20 | use: R | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.1
        """
        return self._c_data[0]

    @where_subject_filter.setter  # set QRF.1
    def where_subject_filter(self, st: ST | tuple[ST]):
        """
        id: QRF.1 | len: 20 | use: R | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.1
        """
        if isinstance(st, tuple):
            self._c_data[0] = st
        else:
            self._c_data[0] = (st,)

    @property  # get QRF.2
    def when_data_start_date_or_time(self) -> TS | None:
        """
        id: QRF.2 | len: 26 | use: B | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.2
        """
        return self._c_data[1][0]

    @when_data_start_date_or_time.setter  # set QRF.2
    def when_data_start_date_or_time(self, ts: TS | None):
        """
        id: QRF.2 | len: 26 | use: B | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.2
        """
        self._c_data[1] = (ts,)

    @property  # get QRF.3
    def when_data_end_date_or_time(self) -> TS | None:
        """
        id: QRF.3 | len: 26 | use: B | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.3
        """
        return self._c_data[2][0]

    @when_data_end_date_or_time.setter  # set QRF.3
    def when_data_end_date_or_time(self, ts: TS | None):
        """
        id: QRF.3 | len: 26 | use: B | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.3
        """
        self._c_data[2] = (ts,)

    @property
    def what_user_qualifier(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: QRF.4 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.4
        """
        return self._c_data[3]

    @what_user_qualifier.setter  # set QRF.4
    def what_user_qualifier(self, st: ST | tuple[ST] | None):
        """
        id: QRF.4 | len: 60 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.4
        """
        if isinstance(st, tuple):
            self._c_data[3] = st
        else:
            self._c_data[3] = (st,)

    @property
    def other_qry_subject_filter(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: QRF.5 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.5
        """
        return self._c_data[4]

    @other_qry_subject_filter.setter  # set QRF.5
    def other_qry_subject_filter(self, st: ST | tuple[ST] | None):
        """
        id: QRF.5 | len: 60 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.5
        """
        if isinstance(st, tuple):
            self._c_data[4] = st
        else:
            self._c_data[4] = (st,)

    @property
    def which_date_or_time_qualifier(
        self,
    ) -> tuple[WhichDateOrTimeQualifier, ...] | tuple[None]:
        """
        id: QRF.6 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.6
        """
        return self._c_data[5]

    @which_date_or_time_qualifier.setter  # set QRF.6
    def which_date_or_time_qualifier(
        self,
        which_date_or_time_qualifier: WhichDateOrTimeQualifier
        | tuple[WhichDateOrTimeQualifier]
        | None,
    ):
        """
        id: QRF.6 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.6
        """
        if isinstance(which_date_or_time_qualifier, tuple):
            self._c_data[5] = which_date_or_time_qualifier
        else:
            self._c_data[5] = (which_date_or_time_qualifier,)

    @property
    def which_date_or_time_status_qualifier(
        self,
    ) -> tuple[WhichDateOrTimeStatusQualifier, ...] | tuple[None]:
        """
        id: QRF.7 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.7
        """
        return self._c_data[6]

    @which_date_or_time_status_qualifier.setter  # set QRF.7
    def which_date_or_time_status_qualifier(
        self,
        which_date_or_time_status_qualifier: WhichDateOrTimeStatusQualifier
        | tuple[WhichDateOrTimeStatusQualifier]
        | None,
    ):
        """
        id: QRF.7 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.7
        """
        if isinstance(which_date_or_time_status_qualifier, tuple):
            self._c_data[6] = which_date_or_time_status_qualifier
        else:
            self._c_data[6] = (which_date_or_time_status_qualifier,)

    @property
    def date_or_time_selection_qualifier(
        self,
    ) -> tuple[DateOrTimeSelectionQualifier, ...] | tuple[None]:
        """
        id: QRF.8 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.8
        """
        return self._c_data[7]

    @date_or_time_selection_qualifier.setter  # set QRF.8
    def date_or_time_selection_qualifier(
        self,
        date_or_time_selection_qualifier: DateOrTimeSelectionQualifier
        | tuple[DateOrTimeSelectionQualifier]
        | None,
    ):
        """
        id: QRF.8 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.8
        """
        if isinstance(date_or_time_selection_qualifier, tuple):
            self._c_data[7] = date_or_time_selection_qualifier
        else:
            self._c_data[7] = (date_or_time_selection_qualifier,)

    @property  # get QRF.9
    def when_quantity_or_timing_qualifier(self) -> TQ | None:
        """
        id: QRF.9 | len: 60 | use: O | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.9
        """
        return self._c_data[8][0]

    @when_quantity_or_timing_qualifier.setter  # set QRF.9
    def when_quantity_or_timing_qualifier(self, tq: TQ | None):
        """
        id: QRF.9 | len: 60 | use: O | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.9
        """
        self._c_data[8] = (tq,)

    @property  # get QRF.10
    def search_confidence_threshold(self) -> NM | None:
        """
        id: QRF.10 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.10
        """
        return self._c_data[9][0]

    @search_confidence_threshold.setter  # set QRF.10
    def search_confidence_threshold(self, nm: NM | None):
        """
        id: QRF.10 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/QRF.10
        """
        self._c_data[9] = (nm,)
