from __future__ import annotations
from ...base import DataType
from .GTS import GTS
from .IS import IS
from .NM import NM
from .CWE import CWE
from .ID import ID
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.EventRelatedPeriod import EventRelatedPeriod
from ..tables.RepeatPattern import RepeatPattern
from ..tables.CalendarAlignment import CalendarAlignment


"""
DataType - RPT
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::RPT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RPT,
    GTS, IS, NM, CWE, ID
)

rpt = RPT(  # Repeat Pattern - The repeat pattern data type should be used where it is necessary to define the frequency at which an event is to take place
    repeat_pattern_code=cwe,  # CWE(...)  # Required.
    calendar_alignment=None,  # ID(...) 
    phase_range_begin_value=None,  # NM(...) 
    phase_range_end_value=None,  # NM(...) 
    period_quantity=None,  # NM(...) 
    period_units=None,  # IS(...) 
    institution_specified_time=None,  # ID(...) 
    event=None,  # ID(...) 
    event_offset_quantity=None,  # NM(...) 
    event_offset_units=None,  # IS(...) 
    general_timing_specification=None,  # GTS(...) 
)

-----END COMPOSITE_DATA_TYPE::RPT TEMPLATE-----
"""


class RPT(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 984
    _hl7_id = """RPT"""
    _hl7_name = """Repeat Pattern"""
    _hl7_description = """The repeat pattern data type should be used where it is necessary to define the frequency at which an event is to take place"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT"
    _c_length = (705, 2, 10, 10, 10, 10, 1, 6, 10, 10, 200,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "C", "O", "O", "O", "C", "O",)
    _c_aliases = ("RPT.1", "RPT.2", "RPT.3", "RPT.4", "RPT.5", "RPT.6", "RPT.7", "RPT.8", "RPT.9", "RPT.10", "RPT.11",)
    _c_components = (CWE, ID, NM, NM, NM, IS, ID, ID, NM, IS, GTS,)
    _c_names = ("Repeat Pattern Code", "Calendar Alignment", "Phase Range Begin Value", "Phase Range End Value", "Period Quantity", "Period Units", "Institution Specified Time", "Event", "Event Offset Quantity", "Event Offset Units", "General Timing Specification",)
    _c_attrs = ("repeat_pattern_code", "calendar_alignment", "phase_range_begin_value", "phase_range_end_value", "period_quantity", "period_units", "institution_specified_time", "event", "event_offset_quantity", "event_offset_units", "general_timing_specification",)
    # fmt: on

    def __init__(
        self,
        repeat_pattern_code: RepeatPattern
        | CWE
        | tuple[RepeatPattern | CWE, ...],  # RPT.1
        calendar_alignment: CalendarAlignment
        | ID
        | tuple[CalendarAlignment | ID, ...]
        | None = None,  # RPT.2
        phase_range_begin_value: NM | tuple[NM, ...] | None = None,  # RPT.3
        phase_range_end_value: NM | tuple[NM, ...] | None = None,  # RPT.4
        period_quantity: NM | tuple[NM, ...] | None = None,  # RPT.5
        period_units: IS | tuple[IS, ...] | None = None,  # RPT.6
        institution_specified_time: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...]
        | None = None,  # RPT.7
        event: EventRelatedPeriod
        | ID
        | tuple[EventRelatedPeriod | ID, ...]
        | None = None,  # RPT.8
        event_offset_quantity: NM | tuple[NM, ...] | None = None,  # RPT.9
        event_offset_units: IS | tuple[IS, ...] | None = None,  # RPT.10
        general_timing_specification: GTS | tuple[GTS, ...] | None = None,  # RPT.11
    ):
        """
                Repeat Pattern - `RPT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPT>`_
                The repeat pattern data type should be used where it is necessary to define the frequency at which an event is to take place. This data type provides a way to define repeat pattern codes "on the fly". The repeat pattern code is equivalent to the TQ data type, component 2, sub-component 1 (repeat pattern). The additional components define the meaning of the repeat pattern code. Components 2 - 10 are used to define relatively simple repeat patterns. Component 11 is provided to define complex repeat patterns. This data type forms a bridge between the 2.x Repeat Pattern concept from Quantity/Timing, and the Version 3.0 GTS General Timing Specification. Component 1 is the 2.x concept of repeat pattern. Components 2-7 are derived from the version 3.0 data type PIVL. Components 8-10 are derived from the version 3.0 EIVL data type. If a repeat pattern cannot be defined using components 2-10, then component 11, General Timing Specification is provided. This allows the full literal form of the version 3.0 GTS to be specified.

        Examples:
        |Q1H&Every 1 Hour&HL7xxx^^^^1^h|
        |Q2J2&Every second Tuesday&HL7xxx^DW^2^^2^wk|

                :param repeat_pattern_code: A code representing the repeat pattern defined by the other components of this data type (id: RPT.1 | len: 705 | use: R | rpt: 1)
                :param calendar_alignment: Specifies an alignment of the repetition to a calendar (e (id: RPT.2 | len: 2 | use: O | rpt: 1)
                :param phase_range_begin_value: Used for Calendar aligned repeat patterns to determine the amount of time from the beginning of particular RPT-2 (Calendar Alignment) to the beginning of the phase (id: RPT.3 | len: 10 | use: O | rpt: 1)
                :param phase_range_end_value: Used for Calendar aligned repeat patterns to determine the amount of time from the beginning of particular RPT-2 (Calendar Alignment) to the end of the phase (id: RPT.4 | len: 10 | use: O | rpt: 1)
                :param period_quantity: A time duration specifying the frequency at which the periodic interval repeats (id: RPT.5 | len: 10 | use: O | rpt: 1)
                :param period_units: Defines the units used for RPT-5 (Period Quantity) (id: RPT.6 | len: 10 | use: C | rpt: 1)
                :param institution_specified_time: A code that indicates whether the exact timing is up to the party executing the schedule (e (id: RPT.7 | len: 1 | use: O | rpt: 1)
                :param event: A code for a common (periodical) activity of daily living (id: RPT.8 | len: 6 | use: O | rpt: 1)
                :param event_offset_quantity: An interval that marks the offsets for the beginning, width and end of the event-related periodic interval measured from the time each such event actually occurred (id: RPT.9 | len: 10 | use: O | rpt: 1)
                :param event_offset_units: Defines the units used for RPT-9 (Event Offset Quantity) (id: RPT.10 | len: 10 | use: C | rpt: 1)
                :param general_timing_specification: The General Timing Specification as defined by the Version 3 Data Types document (id: RPT.11 | len: 200 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 11
        self.repeat_pattern_code = repeat_pattern_code
        self.calendar_alignment = calendar_alignment
        self.phase_range_begin_value = phase_range_begin_value
        self.phase_range_end_value = phase_range_end_value
        self.period_quantity = period_quantity
        self.period_units = period_units
        self.institution_specified_time = institution_specified_time
        self.event = event
        self.event_offset_quantity = event_offset_quantity
        self.event_offset_units = event_offset_units
        self.general_timing_specification = general_timing_specification

    @property  # get RPT.1
    def repeat_pattern_code(self) -> CWE:
        """
        id: RPT.1 | len: 705 | use: R | rpt: 1
        ---
        A code representing the repeat pattern defined by the other components of this data type. Refer to User-defined Table 335 - Repeat Pattern for suggested values.
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.1
        """
        return self._c_data[0][0]

    @repeat_pattern_code.setter  # set RPT.1
    def repeat_pattern_code(self, cwe: CWE):
        """
        id: RPT.1 | len: 705 | use: R | rpt: 1
        ---
        A code representing the repeat pattern defined by the other components of this data type. Refer to User-defined Table 335 - Repeat Pattern for suggested values.
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.1
        """
        self._c_data[0] = (cwe,)

    @property  # get RPT.2
    def calendar_alignment(self) -> CalendarAlignment | None:
        """
        id: RPT.2 | len: 2 | use: O | rpt: 1
        ---
        Specifies an alignment of the repetition to a calendar (e.g., to distinguish every 30 days from the 5th of every month). Refer to HL7 Table 0527 - Calendar Alignment for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.2
        """
        return self._c_data[1][0]

    @calendar_alignment.setter  # set RPT.2
    def calendar_alignment(self, calendar_alignment: CalendarAlignment | None):
        """
        id: RPT.2 | len: 2 | use: O | rpt: 1
        ---
        Specifies an alignment of the repetition to a calendar (e.g., to distinguish every 30 days from the 5th of every month). Refer to HL7 Table 0527 - Calendar Alignment for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.2
        """
        self._c_data[1] = (calendar_alignment,)

    @property  # get RPT.3
    def phase_range_begin_value(self) -> NM | None:
        """
        id: RPT.3 | len: 10 | use: O | rpt: 1
        ---
        Used for Calendar aligned repeat patterns to determine the amount of time from the beginning of particular RPT-2 (Calendar Alignment) to the beginning of the phase. If Calendar Alignment is DW (days of week), then this would be the offset from the beginning of the week.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.3
        """
        return self._c_data[2][0]

    @phase_range_begin_value.setter  # set RPT.3
    def phase_range_begin_value(self, nm: NM | None):
        """
        id: RPT.3 | len: 10 | use: O | rpt: 1
        ---
        Used for Calendar aligned repeat patterns to determine the amount of time from the beginning of particular RPT-2 (Calendar Alignment) to the beginning of the phase. If Calendar Alignment is DW (days of week), then this would be the offset from the beginning of the week.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.3
        """
        self._c_data[2] = (nm,)

    @property  # get RPT.4
    def phase_range_end_value(self) -> NM | None:
        """
        id: RPT.4 | len: 10 | use: O | rpt: 1
        ---
        Used for Calendar aligned repeat patterns to determine the amount of time from the beginning of particular RPT-2 (Calendar Alignment) to the end of the phase.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.4
        """
        return self._c_data[3][0]

    @phase_range_end_value.setter  # set RPT.4
    def phase_range_end_value(self, nm: NM | None):
        """
        id: RPT.4 | len: 10 | use: O | rpt: 1
        ---
        Used for Calendar aligned repeat patterns to determine the amount of time from the beginning of particular RPT-2 (Calendar Alignment) to the end of the phase.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.4
        """
        self._c_data[3] = (nm,)

    @property  # get RPT.5
    def period_quantity(self) -> NM | None:
        """
        id: RPT.5 | len: 10 | use: O | rpt: 1
        ---
        A time duration specifying the frequency at which the periodic interval repeats. RPT-6 (Period Units) defines the units of time for this component.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.5
        """
        return self._c_data[4][0]

    @period_quantity.setter  # set RPT.5
    def period_quantity(self, nm: NM | None):
        """
        id: RPT.5 | len: 10 | use: O | rpt: 1
        ---
        A time duration specifying the frequency at which the periodic interval repeats. RPT-6 (Period Units) defines the units of time for this component.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.5
        """
        self._c_data[4] = (nm,)

    @property  # get RPT.6
    def period_units(self) -> IS | None:
        """
        id: RPT.6 | len: 10 | use: C | rpt: 1
        ---
        Defines the units used for RPT-5 (Period Quantity). Constrained to units of time. The codes for unit of measure are specified in the Unified Code for Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.6
        """
        return self._c_data[5][0]

    @period_units.setter  # set RPT.6
    def period_units(self, _is: IS | None):
        """
        id: RPT.6 | len: 10 | use: C | rpt: 1
        ---
        Defines the units used for RPT-5 (Period Quantity). Constrained to units of time. The codes for unit of measure are specified in the Unified Code for Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.6
        """
        self._c_data[5] = (_is,)

    @property  # get RPT.7
    def institution_specified_time(self) -> YesOrNoIndicator | None:
        """
        id: RPT.7 | len: 1 | use: O | rpt: 1
        ---
        A code that indicates whether the exact timing is up to the party executing the schedule (e.g., to distinguish every 8 hours from 3 times a day.) Refer to HL7 Table 0136 - Yes/No Indicator for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.7
        """
        return self._c_data[6][0]

    @institution_specified_time.setter  # set RPT.7
    def institution_specified_time(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RPT.7 | len: 1 | use: O | rpt: 1
        ---
        A code that indicates whether the exact timing is up to the party executing the schedule (e.g., to distinguish every 8 hours from 3 times a day.) Refer to HL7 Table 0136 - Yes/No Indicator for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.7
        """
        self._c_data[6] = (yes_or_no_indicator,)

    @property  # get RPT.8
    def event(self) -> EventRelatedPeriod | None:
        """
        id: RPT.8 | len: 6 | use: O | rpt: 1
        ---
        A code for a common (periodical) activity of daily living. Refer to HL7 Table 0528, Event-Related Period for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.8
        """
        return self._c_data[7][0]

    @event.setter  # set RPT.8
    def event(self, event_related_period: EventRelatedPeriod | None):
        """
        id: RPT.8 | len: 6 | use: O | rpt: 1
        ---
        A code for a common (periodical) activity of daily living. Refer to HL7 Table 0528, Event-Related Period for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.8
        """
        self._c_data[7] = (event_related_period,)

    @property  # get RPT.9
    def event_offset_quantity(self) -> NM | None:
        """
        id: RPT.9 | len: 10 | use: O | rpt: 1
        ---
        An interval that marks the offsets for the beginning, width and end of the event-related periodic interval measured from the time each such event actually occurred. A positive numeric value indicates the amount of time after the event in RPT-8. A negative numeric value indicates the amount of time prior to the event in RPT-8. RPT-10 (Event Offset Units) defines the units of time for this component.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.9
        """
        return self._c_data[8][0]

    @event_offset_quantity.setter  # set RPT.9
    def event_offset_quantity(self, nm: NM | None):
        """
        id: RPT.9 | len: 10 | use: O | rpt: 1
        ---
        An interval that marks the offsets for the beginning, width and end of the event-related periodic interval measured from the time each such event actually occurred. A positive numeric value indicates the amount of time after the event in RPT-8. A negative numeric value indicates the amount of time prior to the event in RPT-8. RPT-10 (Event Offset Units) defines the units of time for this component.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.9
        """
        self._c_data[8] = (nm,)

    @property  # get RPT.10
    def event_offset_units(self) -> IS | None:
        """
        id: RPT.10 | len: 10 | use: C | rpt: 1
        ---
        Defines the units used for RPT-9 (Event Offset Quantity). Constrained to units of time. The codes for unit of measure are specified in the Unified Code for Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.10
        """
        return self._c_data[9][0]

    @event_offset_units.setter  # set RPT.10
    def event_offset_units(self, _is: IS | None):
        """
        id: RPT.10 | len: 10 | use: C | rpt: 1
        ---
        Defines the units used for RPT-9 (Event Offset Quantity). Constrained to units of time. The codes for unit of measure are specified in the Unified Code for Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.10
        """
        self._c_data[9] = (_is,)

    @property  # get RPT.11
    def general_timing_specification(self) -> GTS | None:
        """
        id: RPT.11 | len: 200 | use: O | rpt: 1
        ---
        The General Timing Specification as defined by the Version 3 Data Types document.
        ---
        return_type: GTS: General Timing Specification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.11
        """
        return self._c_data[10][0]

    @general_timing_specification.setter  # set RPT.11
    def general_timing_specification(self, gts: GTS | None):
        """
        id: RPT.11 | len: 200 | use: O | rpt: 1
        ---
        The General Timing Specification as defined by the Version 3 Data Types document.
        ---
        param_type: GTS: General Timing Specification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RPT.11
        """
        self._c_data[10] = (gts,)
