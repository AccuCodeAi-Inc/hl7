from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.IS import IS
from ..data_types.XCN import XCN
from ..data_types.HD import HD
from ..tables.EventType import EventType
from ..tables.EventReason import EventReason
from ..tables.OperatorId import OperatorId


"""
Event Type - EVN
HL7 Version: 2.5.1

-----BEGIN SEGMENT::EVN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EVN,
    TS, ID, IS, XCN, HD
)

evn = EVN(  #  - The EVN segment is used to communicate necessary trigger event information to receiving applications
    event_type_code=None,  # ID(...) 
    recorded_date_or_time=ts,  # TS(...)  # Required.
    date_or_time_planned_event=None,  # TS(...) 
    event_reason_code=None,  # IS(...) 
    operator_id=None,  # XCN(...) 
    event_occurred=None,  # TS(...) 
    event_facility=None,  # HD(...) 
)

-----END SEGMENT::EVN TEMPLATE-----
"""


class EVN(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """EVN"""
    _hl7_name = """Event Type"""
    _hl7_description = """The EVN segment is used to communicate necessary trigger event information to receiving applications"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN"
    _c_length = (3, 26, 26, 3, 250, 26, 241,)
    _c_rpt = (1, 1, 1, 1, 65535, 1, 1,)
    _c_usage = ("B", "R", "O", "O", "O", "O", "O",)
    _c_components = (ID, TS, TS, IS, XCN, TS, HD,)
    _c_aliases = ("EVN.1", "EVN.2", "EVN.3", "EVN.4", "EVN.5", "EVN.6", "EVN.7",)
    _c_names = ("Event Type Code", "Recorded Date/Time", "Date/Time Planned Event", "Event Reason Code", "Operator ID", "Event Occurred", "Event Facility",)
    _c_attrs = ("event_type_code", "recorded_date_or_time", "date_or_time_planned_event", "event_reason_code", "operator_id", "event_occurred", "event_facility",)
    # fmt: on

    def __init__(
        self,
        recorded_date_or_time: TS | tuple[TS],  # EVN.2
        event_type_code: EventType | ID | tuple[EventType | ID] | None = None,  # EVN.1
        date_or_time_planned_event: TS | tuple[TS] | None = None,  # EVN.3
        event_reason_code: EventReason
        | IS
        | tuple[EventReason | IS]
        | None = None,  # EVN.4
        operator_id: OperatorId | XCN | tuple[OperatorId | XCN] | None = None,  # EVN.5
        event_occurred: TS | tuple[TS] | None = None,  # EVN.6
        event_facility: HD | tuple[HD] | None = None,  # EVN.7
    ):
        """
        Event Type - `EVN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN>`_
        The EVN segment is used to communicate necessary trigger event information to receiving applications. Valid event types for all chapters are contained in HL7 Table 0003 - Event Type .

        :param event_type_code: Coded values for HL7 tables (id: EVN.1 | len: 3 | use: B | rpt: 1)
        :param recorded_date_or_time: Time Stamp (id: EVN.2 | len: 26 | use: R | rpt: 1)
        :param date_or_time_planned_event: Time Stamp (id: EVN.3 | len: 26 | use: O | rpt: 1)
        :param event_reason_code: Coded value for user-defined tables (id: EVN.4 | len: 3 | use: O | rpt: 1)
        :param operator_id: Extended Composite ID Number and Name for Persons (id: EVN.5 | len: 250 | use: O | rpt: *)
        :param event_occurred: Time Stamp (id: EVN.6 | len: 26 | use: O | rpt: 1)
        :param event_facility: Hierarchic Designator (id: EVN.7 | len: 241 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.event_type_code = event_type_code
        self.recorded_date_or_time = recorded_date_or_time
        self.date_or_time_planned_event = date_or_time_planned_event
        self.event_reason_code = event_reason_code
        self.operator_id = operator_id
        self.event_occurred = event_occurred
        self.event_facility = event_facility

    @property  # get EVN.1
    def event_type_code(self) -> EventType | None:
        """
        id: EVN.1 | len: 3 | use: B | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.1
        """
        return self._c_data[0][0]

    @event_type_code.setter  # set EVN.1
    def event_type_code(self, event_type: EventType | None):
        """
        id: EVN.1 | len: 3 | use: B | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.1
        """
        self._c_data[0] = (event_type,)

    @property  # get EVN.2
    def recorded_date_or_time(self) -> TS:
        """
        id: EVN.2 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.2
        """
        return self._c_data[1][0]

    @recorded_date_or_time.setter  # set EVN.2
    def recorded_date_or_time(self, ts: TS):
        """
        id: EVN.2 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.2
        """
        self._c_data[1] = (ts,)

    @property  # get EVN.3
    def date_or_time_planned_event(self) -> TS | None:
        """
        id: EVN.3 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.3
        """
        return self._c_data[2][0]

    @date_or_time_planned_event.setter  # set EVN.3
    def date_or_time_planned_event(self, ts: TS | None):
        """
        id: EVN.3 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.3
        """
        self._c_data[2] = (ts,)

    @property  # get EVN.4
    def event_reason_code(self) -> EventReason | None:
        """
        id: EVN.4 | len: 3 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.4
        """
        return self._c_data[3][0]

    @event_reason_code.setter  # set EVN.4
    def event_reason_code(self, event_reason: EventReason | None):
        """
        id: EVN.4 | len: 3 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.4
        """
        self._c_data[3] = (event_reason,)

    @property
    def operator_id(self) -> tuple[OperatorId, ...] | tuple[None]:
        """
        id: EVN.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.5
        """
        return self._c_data[4]

    @operator_id.setter  # set EVN.5
    def operator_id(self, operator_id: OperatorId | tuple[OperatorId] | None):
        """
        id: EVN.5 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.5
        """
        if isinstance(operator_id, tuple):
            self._c_data[4] = operator_id
        else:
            self._c_data[4] = (operator_id,)

    @property  # get EVN.6
    def event_occurred(self) -> TS | None:
        """
        id: EVN.6 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.6
        """
        return self._c_data[5][0]

    @event_occurred.setter  # set EVN.6
    def event_occurred(self, ts: TS | None):
        """
        id: EVN.6 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.6
        """
        self._c_data[5] = (ts,)

    @property  # get EVN.7
    def event_facility(self) -> HD | None:
        """
        id: EVN.7 | len: 241 | use: O | rpt: 1
        ---
        return_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.7
        """
        return self._c_data[6][0]

    @event_facility.setter  # set EVN.7
    def event_facility(self, hd: HD | None):
        """
        id: EVN.7 | len: 241 | use: O | rpt: 1
        ---
        param_type: HD: Hierarchic Designator
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EVN.7
        """
        self._c_data[6] = (hd,)
