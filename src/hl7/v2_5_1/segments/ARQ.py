from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XTN import XTN
from ..data_types.XAD import XAD
from ..data_types.NM import NM
from ..data_types.PL import PL
from ..data_types.DR import DR
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.RI import RI
from ..data_types.EI import EI
from ..data_types.XCN import XCN
from ..tables.AppointmentReasonCodes import AppointmentReasonCodes
from ..tables.AppointmentTypeCodes import AppointmentTypeCodes


"""
Appointment Request - ARQ
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ARQ TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ARQ,
    XTN, XAD, NM, PL, DR, ST, CE, RI, EI, XCN
)

arq = ARQ(  #  - The ARQ segment defines a request for the booking of an appointment
    placer_appointment_id=ei,  # EI(...)  # Required.
    filler_appointment_id=None,  # EI(...) 
    occurrence_number=None,  # NM(...) 
    placer_group_number=None,  # EI(...) 
    schedule_id=None,  # CE(...) 
    request_event_reason=None,  # CE(...) 
    appointment_reason=None,  # CE(...) 
    appointment_type=None,  # CE(...) 
    appointment_duration=None,  # NM(...) 
    appointment_duration_units=None,  # CE(...) 
    requested_start_date_or_time_range=None,  # DR(...) 
    priority_arq=None,  # ST(...) 
    repeating_interval=None,  # RI(...) 
    repeating_interval_duration=None,  # ST(...) 
    placer_contact_person=xcn,  # XCN(...)  # Required.
    placer_contact_phone_number=None,  # XTN(...) 
    placer_contact_address=None,  # XAD(...) 
    placer_contact_location=None,  # PL(...) 
    entered_by_person=xcn,  # XCN(...)  # Required.
    entered_by_phone_number=None,  # XTN(...) 
    entered_by_location=None,  # PL(...) 
    parent_placer_appointment_id=None,  # EI(...) 
    parent_filler_appointment_id=None,  # EI(...) 
    placer_order_number=None,  # EI(...) 
    filler_order_number=None,  # EI(...) 
)

-----END SEGMENT::ARQ TEMPLATE-----
"""


class ARQ(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ARQ"""
    _hl7_name = """Appointment Request"""
    _hl7_description = """The ARQ segment defines a request for the booking of an appointment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ARQ"
    _c_length = (75, 75, 5, 22, 250, 250, 250, 250, 20, 250, 53, 5, 100, 5, 250, 250, 250, 80, 250, 250, 80, 75, 75, 22, 22,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 65535, 65535, 65535, 1, 65535, 65535, 1, 1, 1, 65535, 65535,)
    _c_usage = ("R", "C", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "R", "O", "O", "O", "R", "O", "O", "O", "O", "C", "C",)
    _c_components = (EI, EI, NM, EI, CE, CE, CE, CE, NM, CE, DR, ST, RI, ST, XCN, XTN, XAD, PL, XCN, XTN, PL, EI, EI, EI, EI,)
    _c_aliases = ("ARQ.1", "ARQ.2", "ARQ.3", "ARQ.4", "ARQ.5", "ARQ.6", "ARQ.7", "ARQ.8", "ARQ.9", "ARQ.10", "ARQ.11", "ARQ.12", "ARQ.13", "ARQ.14", "ARQ.15", "ARQ.16", "ARQ.17", "ARQ.18", "ARQ.19", "ARQ.20", "ARQ.21", "ARQ.22", "ARQ.23", "ARQ.24", "ARQ.25",)
    _c_names = ("Placer Appointment ID", "Filler Appointment ID", "Occurrence Number", "Placer Group Number", "Schedule ID", "Request Event Reason", "Appointment Reason", "Appointment Type", "Appointment Duration", "Appointment Duration Units", "Requested Start Date/Time Range", "Priority-ARQ", "Repeating Interval", "Repeating Interval Duration", "Placer Contact Person", "Placer Contact Phone Number", "Placer Contact Address", "Placer Contact Location", "Entered By Person", "Entered By Phone Number", "Entered By Location", "Parent Placer Appointment ID", "Parent Filler Appointment ID", "Placer Order Number", "Filler Order Number",)
    _c_attrs = ("placer_appointment_id", "filler_appointment_id", "occurrence_number", "placer_group_number", "schedule_id", "request_event_reason", "appointment_reason", "appointment_type", "appointment_duration", "appointment_duration_units", "requested_start_date_or_time_range", "priority_arq", "repeating_interval", "repeating_interval_duration", "placer_contact_person", "placer_contact_phone_number", "placer_contact_address", "placer_contact_location", "entered_by_person", "entered_by_phone_number", "entered_by_location", "parent_placer_appointment_id", "parent_filler_appointment_id", "placer_order_number", "filler_order_number",)
    # fmt: on

    def __init__(
        self,
        placer_appointment_id: EI | tuple[EI],  # ARQ.1
        placer_contact_person: XCN | tuple[XCN],  # ARQ.15
        entered_by_person: XCN | tuple[XCN],  # ARQ.19
        filler_appointment_id: EI | tuple[EI] | None = None,  # ARQ.2
        occurrence_number: NM | tuple[NM] | None = None,  # ARQ.3
        placer_group_number: EI | tuple[EI] | None = None,  # ARQ.4
        schedule_id: CE | tuple[CE] | None = None,  # ARQ.5
        request_event_reason: CE | tuple[CE] | None = None,  # ARQ.6
        appointment_reason: AppointmentReasonCodes
        | CE
        | tuple[AppointmentReasonCodes | CE]
        | None = None,  # ARQ.7
        appointment_type: AppointmentTypeCodes
        | CE
        | tuple[AppointmentTypeCodes | CE]
        | None = None,  # ARQ.8
        appointment_duration: NM | tuple[NM] | None = None,  # ARQ.9
        appointment_duration_units: CE | tuple[CE] | None = None,  # ARQ.10
        requested_start_date_or_time_range: DR | tuple[DR] | None = None,  # ARQ.11
        priority_arq: ST | tuple[ST] | None = None,  # ARQ.12
        repeating_interval: RI | tuple[RI] | None = None,  # ARQ.13
        repeating_interval_duration: ST | tuple[ST] | None = None,  # ARQ.14
        placer_contact_phone_number: XTN | tuple[XTN] | None = None,  # ARQ.16
        placer_contact_address: XAD | tuple[XAD] | None = None,  # ARQ.17
        placer_contact_location: PL | tuple[PL] | None = None,  # ARQ.18
        entered_by_phone_number: XTN | tuple[XTN] | None = None,  # ARQ.20
        entered_by_location: PL | tuple[PL] | None = None,  # ARQ.21
        parent_placer_appointment_id: EI | tuple[EI] | None = None,  # ARQ.22
        parent_filler_appointment_id: EI | tuple[EI] | None = None,  # ARQ.23
        placer_order_number: EI | tuple[EI] | None = None,  # ARQ.24
        filler_order_number: EI | tuple[EI] | None = None,  # ARQ.25
    ):
        """
        Appointment Request - `ARQ <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ARQ>`_
        The ARQ segment defines a request for the booking of an appointment. It is used in transactions sent from an application acting in the role of a placer.

        :param placer_appointment_id: Entity Identifier (id: ARQ.1 | len: 75 | use: R | rpt: 1)
        :param filler_appointment_id: Entity Identifier (id: ARQ.2 | len: 75 | use: C | rpt: 1)
        :param occurrence_number: Numeric (id: ARQ.3 | len: 5 | use: C | rpt: 1)
        :param placer_group_number: Entity Identifier (id: ARQ.4 | len: 22 | use: O | rpt: 1)
        :param schedule_id: Coded Element (id: ARQ.5 | len: 250 | use: O | rpt: 1)
        :param request_event_reason: Coded Element (id: ARQ.6 | len: 250 | use: O | rpt: 1)
        :param appointment_reason: Coded Element (id: ARQ.7 | len: 250 | use: O | rpt: 1)
        :param appointment_type: Coded Element (id: ARQ.8 | len: 250 | use: O | rpt: 1)
        :param appointment_duration: Numeric (id: ARQ.9 | len: 20 | use: O | rpt: 1)
        :param appointment_duration_units: Coded Element (id: ARQ.10 | len: 250 | use: O | rpt: 1)
        :param requested_start_date_or_time_range: Date/Time Range (id: ARQ.11 | len: 53 | use: O | rpt: *)
        :param priority_arq: String Data (id: ARQ.12 | len: 5 | use: O | rpt: 1)
        :param repeating_interval: Repeat Interval (id: ARQ.13 | len: 100 | use: O | rpt: 1)
        :param repeating_interval_duration: String Data (id: ARQ.14 | len: 5 | use: O | rpt: 1)
        :param placer_contact_person: Extended Composite ID Number and Name for Persons (id: ARQ.15 | len: 250 | use: R | rpt: *)
        :param placer_contact_phone_number: Extended Telecommunication Number (id: ARQ.16 | len: 250 | use: O | rpt: *)
        :param placer_contact_address: Extended Address (id: ARQ.17 | len: 250 | use: O | rpt: *)
        :param placer_contact_location: Person Location (id: ARQ.18 | len: 80 | use: O | rpt: 1)
        :param entered_by_person: Extended Composite ID Number and Name for Persons (id: ARQ.19 | len: 250 | use: R | rpt: *)
        :param entered_by_phone_number: Extended Telecommunication Number (id: ARQ.20 | len: 250 | use: O | rpt: *)
        :param entered_by_location: Person Location (id: ARQ.21 | len: 80 | use: O | rpt: 1)
        :param parent_placer_appointment_id: Entity Identifier (id: ARQ.22 | len: 75 | use: O | rpt: 1)
        :param parent_filler_appointment_id: Entity Identifier (id: ARQ.23 | len: 75 | use: O | rpt: 1)
        :param placer_order_number: Entity Identifier (id: ARQ.24 | len: 22 | use: C | rpt: *)
        :param filler_order_number: Entity Identifier (id: ARQ.25 | len: 22 | use: C | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 25
        self.placer_appointment_id = placer_appointment_id
        self.filler_appointment_id = filler_appointment_id
        self.occurrence_number = occurrence_number
        self.placer_group_number = placer_group_number
        self.schedule_id = schedule_id
        self.request_event_reason = request_event_reason
        self.appointment_reason = appointment_reason
        self.appointment_type = appointment_type
        self.appointment_duration = appointment_duration
        self.appointment_duration_units = appointment_duration_units
        self.requested_start_date_or_time_range = requested_start_date_or_time_range
        self.priority_arq = priority_arq
        self.repeating_interval = repeating_interval
        self.repeating_interval_duration = repeating_interval_duration
        self.placer_contact_person = placer_contact_person
        self.placer_contact_phone_number = placer_contact_phone_number
        self.placer_contact_address = placer_contact_address
        self.placer_contact_location = placer_contact_location
        self.entered_by_person = entered_by_person
        self.entered_by_phone_number = entered_by_phone_number
        self.entered_by_location = entered_by_location
        self.parent_placer_appointment_id = parent_placer_appointment_id
        self.parent_filler_appointment_id = parent_filler_appointment_id
        self.placer_order_number = placer_order_number
        self.filler_order_number = filler_order_number

    @property  # get ARQ.1
    def placer_appointment_id(self) -> EI:
        """
        id: ARQ.1 | len: 75 | use: R | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.1
        """
        return self._c_data[0][0]

    @placer_appointment_id.setter  # set ARQ.1
    def placer_appointment_id(self, ei: EI):
        """
        id: ARQ.1 | len: 75 | use: R | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.1
        """
        self._c_data[0] = (ei,)

    @property  # get ARQ.2
    def filler_appointment_id(self) -> EI | None:
        """
        id: ARQ.2 | len: 75 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.2
        """
        return self._c_data[1][0]

    @filler_appointment_id.setter  # set ARQ.2
    def filler_appointment_id(self, ei: EI | None):
        """
        id: ARQ.2 | len: 75 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.2
        """
        self._c_data[1] = (ei,)

    @property  # get ARQ.3
    def occurrence_number(self) -> NM | None:
        """
        id: ARQ.3 | len: 5 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.3
        """
        return self._c_data[2][0]

    @occurrence_number.setter  # set ARQ.3
    def occurrence_number(self, nm: NM | None):
        """
        id: ARQ.3 | len: 5 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.3
        """
        self._c_data[2] = (nm,)

    @property  # get ARQ.4
    def placer_group_number(self) -> EI | None:
        """
        id: ARQ.4 | len: 22 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.4
        """
        return self._c_data[3][0]

    @placer_group_number.setter  # set ARQ.4
    def placer_group_number(self, ei: EI | None):
        """
        id: ARQ.4 | len: 22 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.4
        """
        self._c_data[3] = (ei,)

    @property  # get ARQ.5
    def schedule_id(self) -> CE | None:
        """
        id: ARQ.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.5
        """
        return self._c_data[4][0]

    @schedule_id.setter  # set ARQ.5
    def schedule_id(self, ce: CE | None):
        """
        id: ARQ.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.5
        """
        self._c_data[4] = (ce,)

    @property  # get ARQ.6
    def request_event_reason(self) -> CE | None:
        """
        id: ARQ.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.6
        """
        return self._c_data[5][0]

    @request_event_reason.setter  # set ARQ.6
    def request_event_reason(self, ce: CE | None):
        """
        id: ARQ.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.6
        """
        self._c_data[5] = (ce,)

    @property  # get ARQ.7
    def appointment_reason(self) -> AppointmentReasonCodes | None:
        """
        id: ARQ.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.7
        """
        return self._c_data[6][0]

    @appointment_reason.setter  # set ARQ.7
    def appointment_reason(
        self, appointment_reason_codes: AppointmentReasonCodes | None
    ):
        """
        id: ARQ.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.7
        """
        self._c_data[6] = (appointment_reason_codes,)

    @property  # get ARQ.8
    def appointment_type(self) -> AppointmentTypeCodes | None:
        """
        id: ARQ.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.8
        """
        return self._c_data[7][0]

    @appointment_type.setter  # set ARQ.8
    def appointment_type(self, appointment_type_codes: AppointmentTypeCodes | None):
        """
        id: ARQ.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.8
        """
        self._c_data[7] = (appointment_type_codes,)

    @property  # get ARQ.9
    def appointment_duration(self) -> NM | None:
        """
        id: ARQ.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.9
        """
        return self._c_data[8][0]

    @appointment_duration.setter  # set ARQ.9
    def appointment_duration(self, nm: NM | None):
        """
        id: ARQ.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.9
        """
        self._c_data[8] = (nm,)

    @property  # get ARQ.10
    def appointment_duration_units(self) -> CE | None:
        """
        id: ARQ.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.10
        """
        return self._c_data[9][0]

    @appointment_duration_units.setter  # set ARQ.10
    def appointment_duration_units(self, ce: CE | None):
        """
        id: ARQ.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.10
        """
        self._c_data[9] = (ce,)

    @property
    def requested_start_date_or_time_range(self) -> tuple[DR, ...] | tuple[None]:
        """
        id: ARQ.11 | len: 53 | use: O | rpt: *
        ---
        return_type: tuple[DR, ...]: (Date/Time Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.11
        """
        return self._c_data[10]

    @requested_start_date_or_time_range.setter  # set ARQ.11
    def requested_start_date_or_time_range(self, dr: DR | tuple[DR] | None):
        """
        id: ARQ.11 | len: 53 | use: O | rpt: *
        ---
        param_type: DR | tuple[DR, ...]: (Date/Time Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.11
        """
        if isinstance(dr, tuple):
            self._c_data[10] = dr
        else:
            self._c_data[10] = (dr,)

    @property  # get ARQ.12
    def priority_arq(self) -> ST | None:
        """
        id: ARQ.12 | len: 5 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.12
        """
        return self._c_data[11][0]

    @priority_arq.setter  # set ARQ.12
    def priority_arq(self, st: ST | None):
        """
        id: ARQ.12 | len: 5 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.12
        """
        self._c_data[11] = (st,)

    @property  # get ARQ.13
    def repeating_interval(self) -> RI | None:
        """
        id: ARQ.13 | len: 100 | use: O | rpt: 1
        ---
        return_type: RI: Repeat Interval
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.13
        """
        return self._c_data[12][0]

    @repeating_interval.setter  # set ARQ.13
    def repeating_interval(self, ri: RI | None):
        """
        id: ARQ.13 | len: 100 | use: O | rpt: 1
        ---
        param_type: RI: Repeat Interval
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.13
        """
        self._c_data[12] = (ri,)

    @property  # get ARQ.14
    def repeating_interval_duration(self) -> ST | None:
        """
        id: ARQ.14 | len: 5 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.14
        """
        return self._c_data[13][0]

    @repeating_interval_duration.setter  # set ARQ.14
    def repeating_interval_duration(self, st: ST | None):
        """
        id: ARQ.14 | len: 5 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.14
        """
        self._c_data[13] = (st,)

    @property
    def placer_contact_person(self) -> tuple[XCN, ...]:
        """
        id: ARQ.15 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.15
        """
        return self._c_data[14]

    @placer_contact_person.setter  # set ARQ.15
    def placer_contact_person(self, xcn: XCN | tuple[XCN]):
        """
        id: ARQ.15 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.15
        """
        if isinstance(xcn, tuple):
            self._c_data[14] = xcn
        else:
            self._c_data[14] = (xcn,)

    @property
    def placer_contact_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: ARQ.16 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.16
        """
        return self._c_data[15]

    @placer_contact_phone_number.setter  # set ARQ.16
    def placer_contact_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: ARQ.16 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.16
        """
        if isinstance(xtn, tuple):
            self._c_data[15] = xtn
        else:
            self._c_data[15] = (xtn,)

    @property
    def placer_contact_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: ARQ.17 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.17
        """
        return self._c_data[16]

    @placer_contact_address.setter  # set ARQ.17
    def placer_contact_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: ARQ.17 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.17
        """
        if isinstance(xad, tuple):
            self._c_data[16] = xad
        else:
            self._c_data[16] = (xad,)

    @property  # get ARQ.18
    def placer_contact_location(self) -> PL | None:
        """
        id: ARQ.18 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.18
        """
        return self._c_data[17][0]

    @placer_contact_location.setter  # set ARQ.18
    def placer_contact_location(self, pl: PL | None):
        """
        id: ARQ.18 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.18
        """
        self._c_data[17] = (pl,)

    @property
    def entered_by_person(self) -> tuple[XCN, ...]:
        """
        id: ARQ.19 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.19
        """
        return self._c_data[18]

    @entered_by_person.setter  # set ARQ.19
    def entered_by_person(self, xcn: XCN | tuple[XCN]):
        """
        id: ARQ.19 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.19
        """
        if isinstance(xcn, tuple):
            self._c_data[18] = xcn
        else:
            self._c_data[18] = (xcn,)

    @property
    def entered_by_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: ARQ.20 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.20
        """
        return self._c_data[19]

    @entered_by_phone_number.setter  # set ARQ.20
    def entered_by_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: ARQ.20 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.20
        """
        if isinstance(xtn, tuple):
            self._c_data[19] = xtn
        else:
            self._c_data[19] = (xtn,)

    @property  # get ARQ.21
    def entered_by_location(self) -> PL | None:
        """
        id: ARQ.21 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.21
        """
        return self._c_data[20][0]

    @entered_by_location.setter  # set ARQ.21
    def entered_by_location(self, pl: PL | None):
        """
        id: ARQ.21 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.21
        """
        self._c_data[20] = (pl,)

    @property  # get ARQ.22
    def parent_placer_appointment_id(self) -> EI | None:
        """
        id: ARQ.22 | len: 75 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.22
        """
        return self._c_data[21][0]

    @parent_placer_appointment_id.setter  # set ARQ.22
    def parent_placer_appointment_id(self, ei: EI | None):
        """
        id: ARQ.22 | len: 75 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.22
        """
        self._c_data[21] = (ei,)

    @property  # get ARQ.23
    def parent_filler_appointment_id(self) -> EI | None:
        """
        id: ARQ.23 | len: 75 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.23
        """
        return self._c_data[22][0]

    @parent_filler_appointment_id.setter  # set ARQ.23
    def parent_filler_appointment_id(self, ei: EI | None):
        """
        id: ARQ.23 | len: 75 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.23
        """
        self._c_data[22] = (ei,)

    @property
    def placer_order_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: ARQ.24 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.24
        """
        return self._c_data[23]

    @placer_order_number.setter  # set ARQ.24
    def placer_order_number(self, ei: EI | tuple[EI] | None):
        """
        id: ARQ.24 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.24
        """
        if isinstance(ei, tuple):
            self._c_data[23] = ei
        else:
            self._c_data[23] = (ei,)

    @property
    def filler_order_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: ARQ.25 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.25
        """
        return self._c_data[24]

    @filler_order_number.setter  # set ARQ.25
    def filler_order_number(self, ei: EI | tuple[EI] | None):
        """
        id: ARQ.25 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ARQ.25
        """
        if isinstance(ei, tuple):
            self._c_data[24] = ei
        else:
            self._c_data[24] = (ei,)
