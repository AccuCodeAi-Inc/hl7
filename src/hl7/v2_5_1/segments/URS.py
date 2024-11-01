from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..data_types.TQ import TQ
from ..data_types.TS import TS
from ..tables.WhichDateOrTimeQualifier import WhichDateOrTimeQualifier
from ..tables.WhichDateOrTimeStatusQualifier import WhichDateOrTimeStatusQualifier
from ..tables.DateOrTimeSelectionQualifier import DateOrTimeSelectionQualifier


"""
Unsolicited Selection - URS
HL7 Version: 2.5.1

-----BEGIN SEGMENT::URS TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    URS,
    ST, ID, TQ, TS
)

urs = URS(  #  - This segment is not carried forward to the recommended queries for v 2
    r_or_u_where_subject_definition=st,  # ST(...)  # Required.
    r_or_u_when_data_start_date_or_time=None,  # TS(...) 
    r_or_u_when_data_end_date_or_time=None,  # TS(...) 
    r_or_u_what_user_qualifier=None,  # ST(...) 
    r_or_u_other_results_subject_definition=None,  # ST(...) 
    r_or_u_which_date_or_time_qualifier=None,  # ID(...) 
    r_or_u_which_date_or_time_status_qualifier=None,  # ID(...) 
    r_or_u_date_or_time_selection_qualifier=None,  # ID(...) 
    r_or_u_quantity_or_timing_qualifier=None,  # TQ(...) 
)

-----END SEGMENT::URS TEMPLATE-----
"""


class URS(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """URS"""
    _hl7_name = """Unsolicited Selection"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URS"
    _c_length = (20, 26, 26, 20, 20, 12, 12, 12, 60,)
    _c_rpt = (65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ST, TS, TS, ST, ST, ID, ID, ID, TQ,)
    _c_aliases = ("URS.1", "URS.2", "URS.3", "URS.4", "URS.5", "URS.6", "URS.7", "URS.8", "URS.9",)
    _c_names = ("R/U Where Subject Definition", "R/U When Data Start Date/Time", "R/U When Data End Date/Time", "R/U What User Qualifier", "R/U Other Results Subject Definition", "R/U Which Date/Time Qualifier", "R/U Which Date/Time Status Qualifier", "R/U Date/Time Selection Qualifier", "R/U Quantity/Timing Qualifier",)
    _c_attrs = ("r_or_u_where_subject_definition", "r_or_u_when_data_start_date_or_time", "r_or_u_when_data_end_date_or_time", "r_or_u_what_user_qualifier", "r_or_u_other_results_subject_definition", "r_or_u_which_date_or_time_qualifier", "r_or_u_which_date_or_time_status_qualifier", "r_or_u_date_or_time_selection_qualifier", "r_or_u_quantity_or_timing_qualifier",)
    # fmt: on

    def __init__(
        self,
        r_or_u_where_subject_definition: ST,  # URS.1
        r_or_u_when_data_start_date_or_time: TS | None = None,  # URS.2
        r_or_u_when_data_end_date_or_time: TS | None = None,  # URS.3
        r_or_u_what_user_qualifier: ST | None = None,  # URS.4
        r_or_u_other_results_subject_definition: ST | None = None,  # URS.5
        r_or_u_which_date_or_time_qualifier: WhichDateOrTimeQualifier
        | ID
        | None = None,  # URS.6
        r_or_u_which_date_or_time_status_qualifier: WhichDateOrTimeStatusQualifier
        | ID
        | None = None,  # URS.7
        r_or_u_date_or_time_selection_qualifier: DateOrTimeSelectionQualifier
        | ID
        | None = None,  # URS.8
        r_or_u_quantity_or_timing_qualifier: TQ | None = None,  # URS.9
    ):
        """
                Unsolicited Selection - `URS <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/URS>`_
                This segment is not carried forward to the recommended queries for v 2.4.

        The URS segment is identical with the QRF segment, except that if the name of any field contains Query (of QRY), this word has been changed to Results (see URS-5-R/U other results subject definition).

                :param r_or_u_where_subject_definition: String Data (id: URS.1 | len: 20 | use: R | rpt: *)
                :param r_or_u_when_data_start_date_or_time: Time Stamp (id: URS.2 | len: 26 | use: O | rpt: 1)
                :param r_or_u_when_data_end_date_or_time: Time Stamp (id: URS.3 | len: 26 | use: O | rpt: 1)
                :param r_or_u_what_user_qualifier: String Data (id: URS.4 | len: 20 | use: O | rpt: *)
                :param r_or_u_other_results_subject_definition: String Data (id: URS.5 | len: 20 | use: O | rpt: *)
                :param r_or_u_which_date_or_time_qualifier: Coded values for HL7 tables (id: URS.6 | len: 12 | use: O | rpt: *)
                :param r_or_u_which_date_or_time_status_qualifier: Coded values for HL7 tables (id: URS.7 | len: 12 | use: O | rpt: *)
                :param r_or_u_date_or_time_selection_qualifier: Coded values for HL7 tables (id: URS.8 | len: 12 | use: O | rpt: *)
                :param r_or_u_quantity_or_timing_qualifier: Timing Quantity (id: URS.9 | len: 60 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.r_or_u_where_subject_definition = r_or_u_where_subject_definition
        self.r_or_u_when_data_start_date_or_time = r_or_u_when_data_start_date_or_time
        self.r_or_u_when_data_end_date_or_time = r_or_u_when_data_end_date_or_time
        self.r_or_u_what_user_qualifier = r_or_u_what_user_qualifier
        self.r_or_u_other_results_subject_definition = (
            r_or_u_other_results_subject_definition
        )
        self.r_or_u_which_date_or_time_qualifier = r_or_u_which_date_or_time_qualifier
        self.r_or_u_which_date_or_time_status_qualifier = (
            r_or_u_which_date_or_time_status_qualifier
        )
        self.r_or_u_date_or_time_selection_qualifier = (
            r_or_u_date_or_time_selection_qualifier
        )
        self.r_or_u_quantity_or_timing_qualifier = r_or_u_quantity_or_timing_qualifier

    @property
    def r_or_u_where_subject_definition(self) -> tuple[ST, ...]:
        """
        id: URS.1 | len: 20 | use: R | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.1
        """
        return self._c_data[0]

    @r_or_u_where_subject_definition.setter  # set URS.1
    def r_or_u_where_subject_definition(self, st: ST | tuple[ST]):
        """
        id: URS.1 | len: 20 | use: R | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.1
        """
        if isinstance(st, tuple):
            self._c_data[0] = st
        else:
            self._c_data[0] = (st,)

    @property  # get URS.2
    def r_or_u_when_data_start_date_or_time(self) -> TS | None:
        """
        id: URS.2 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.2
        """
        return self._c_data[1][0]

    @r_or_u_when_data_start_date_or_time.setter  # set URS.2
    def r_or_u_when_data_start_date_or_time(self, ts: TS | None):
        """
        id: URS.2 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.2
        """
        self._c_data[1] = (ts,)

    @property  # get URS.3
    def r_or_u_when_data_end_date_or_time(self) -> TS | None:
        """
        id: URS.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.3
        """
        return self._c_data[2][0]

    @r_or_u_when_data_end_date_or_time.setter  # set URS.3
    def r_or_u_when_data_end_date_or_time(self, ts: TS | None):
        """
        id: URS.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.3
        """
        self._c_data[2] = (ts,)

    @property
    def r_or_u_what_user_qualifier(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: URS.4 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.4
        """
        return self._c_data[3]

    @r_or_u_what_user_qualifier.setter  # set URS.4
    def r_or_u_what_user_qualifier(self, st: ST | tuple[ST] | None):
        """
        id: URS.4 | len: 20 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.4
        """
        if isinstance(st, tuple):
            self._c_data[3] = st
        else:
            self._c_data[3] = (st,)

    @property
    def r_or_u_other_results_subject_definition(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: URS.5 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.5
        """
        return self._c_data[4]

    @r_or_u_other_results_subject_definition.setter  # set URS.5
    def r_or_u_other_results_subject_definition(self, st: ST | tuple[ST] | None):
        """
        id: URS.5 | len: 20 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.5
        """
        if isinstance(st, tuple):
            self._c_data[4] = st
        else:
            self._c_data[4] = (st,)

    @property
    def r_or_u_which_date_or_time_qualifier(
        self,
    ) -> tuple[WhichDateOrTimeQualifier, ...] | tuple[None]:
        """
        id: URS.6 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.6
        """
        return self._c_data[5]

    @r_or_u_which_date_or_time_qualifier.setter  # set URS.6
    def r_or_u_which_date_or_time_qualifier(
        self,
        which_date_or_time_qualifier: WhichDateOrTimeQualifier
        | tuple[WhichDateOrTimeQualifier]
        | None,
    ):
        """
        id: URS.6 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.6
        """
        if isinstance(which_date_or_time_qualifier, tuple):
            self._c_data[5] = which_date_or_time_qualifier
        else:
            self._c_data[5] = (which_date_or_time_qualifier,)

    @property
    def r_or_u_which_date_or_time_status_qualifier(
        self,
    ) -> tuple[WhichDateOrTimeStatusQualifier, ...] | tuple[None]:
        """
        id: URS.7 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.7
        """
        return self._c_data[6]

    @r_or_u_which_date_or_time_status_qualifier.setter  # set URS.7
    def r_or_u_which_date_or_time_status_qualifier(
        self,
        which_date_or_time_status_qualifier: WhichDateOrTimeStatusQualifier
        | tuple[WhichDateOrTimeStatusQualifier]
        | None,
    ):
        """
        id: URS.7 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.7
        """
        if isinstance(which_date_or_time_status_qualifier, tuple):
            self._c_data[6] = which_date_or_time_status_qualifier
        else:
            self._c_data[6] = (which_date_or_time_status_qualifier,)

    @property
    def r_or_u_date_or_time_selection_qualifier(
        self,
    ) -> tuple[DateOrTimeSelectionQualifier, ...] | tuple[None]:
        """
        id: URS.8 | len: 12 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.8
        """
        return self._c_data[7]

    @r_or_u_date_or_time_selection_qualifier.setter  # set URS.8
    def r_or_u_date_or_time_selection_qualifier(
        self,
        date_or_time_selection_qualifier: DateOrTimeSelectionQualifier
        | tuple[DateOrTimeSelectionQualifier]
        | None,
    ):
        """
        id: URS.8 | len: 12 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.8
        """
        if isinstance(date_or_time_selection_qualifier, tuple):
            self._c_data[7] = date_or_time_selection_qualifier
        else:
            self._c_data[7] = (date_or_time_selection_qualifier,)

    @property  # get URS.9
    def r_or_u_quantity_or_timing_qualifier(self) -> TQ | None:
        """
        id: URS.9 | len: 60 | use: O | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.9
        """
        return self._c_data[8][0]

    @r_or_u_quantity_or_timing_qualifier.setter  # set URS.9
    def r_or_u_quantity_or_timing_qualifier(self, tq: TQ | None):
        """
        id: URS.9 | len: 60 | use: O | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/URS.9
        """
        self._c_data[8] = (tq,)
