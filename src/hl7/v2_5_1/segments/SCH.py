from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TQ import TQ
from ..data_types.XTN import XTN
from ..data_types.NM import NM
from ..data_types.PL import PL
from ..data_types.XCN import XCN
from ..data_types.CE import CE
from ..data_types.XAD import XAD
from ..data_types.EI import EI
from ..tables.AppointmentReasonCodes import AppointmentReasonCodes
from ..tables.FillerStatusCodes import FillerStatusCodes
from ..tables.AppointmentTypeCodes import AppointmentTypeCodes


"""
Scheduling Activity Information - SCH
HL7 Version: 2.5.1

-----BEGIN SEGMENT::SCH TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SCH,
    TQ, XTN, NM, PL, XCN, CE, XAD, EI
)

sch = SCH(  #  - The SCH segment contains general information about the scheduled appointment
    placer_appointment_id=None,  # EI(...) 
    filler_appointment_id=None,  # EI(...) 
    occurrence_number=None,  # NM(...) 
    placer_group_number=None,  # EI(...) 
    schedule_id=None,  # CE(...) 
    event_reason=ce,  # CE(...)  # Required.
    appointment_reason=None,  # CE(...) 
    appointment_type=None,  # CE(...) 
    appointment_duration=None,  # NM(...) 
    appointment_duration_units=None,  # CE(...) 
    appointment_timing_quantity=None,  # TQ(...) 
    placer_contact_person=None,  # XCN(...) 
    placer_contact_phone_number=None,  # XTN(...) 
    placer_contact_address=None,  # XAD(...) 
    placer_contact_location=None,  # PL(...) 
    filler_contact_person=xcn,  # XCN(...)  # Required.
    filler_contact_phone_number=None,  # XTN(...) 
    filler_contact_address=None,  # XAD(...) 
    filler_contact_location=None,  # PL(...) 
    entered_by_person=xcn,  # XCN(...)  # Required.
    entered_by_phone_number=None,  # XTN(...) 
    entered_by_location=None,  # PL(...) 
    parent_placer_appointment_id=None,  # EI(...) 
    parent_filler_appointment_id=None,  # EI(...) 
    filler_status_code=None,  # CE(...) 
    placer_order_number=None,  # EI(...) 
    filler_order_number=None,  # EI(...) 
)

-----END SEGMENT::SCH TEMPLATE-----
"""


class SCH(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """SCH"""
    _hl7_name = """Scheduling Activity Information"""
    _hl7_description = """The SCH segment contains general information about the scheduled appointment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH"
    _c_length = (75, 75, 5, 22, 250, 250, 250, 250, 20, 250, 200, 250, 250, 250, 80, 250, 250, 250, 80, 250, 250, 80, 75, 75, 250, 22, 22,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 65535, 1, 65535, 1, 65535, 1, 65535, 1, 65535, 65535, 1, 1, 1, 1, 65535, 65535,)
    _c_usage = ("C", "C", "C", "O", "O", "R", "O", "O", "B", "B", "B", "O", "O", "O", "O", "R", "O", "O", "O", "R", "O", "O", "O", "C", "O", "C", "C",)
    _c_components = (EI, EI, NM, EI, CE, CE, CE, CE, NM, CE, TQ, XCN, XTN, XAD, PL, XCN, XTN, XAD, PL, XCN, XTN, PL, EI, EI, CE, EI, EI,)
    _c_aliases = ("SCH.1", "SCH.2", "SCH.3", "SCH.4", "SCH.5", "SCH.6", "SCH.7", "SCH.8", "SCH.9", "SCH.10", "SCH.11", "SCH.12", "SCH.13", "SCH.14", "SCH.15", "SCH.16", "SCH.17", "SCH.18", "SCH.19", "SCH.20", "SCH.21", "SCH.22", "SCH.23", "SCH.24", "SCH.25", "SCH.26", "SCH.27",)
    _c_names = ("Placer Appointment ID", "Filler Appointment ID", "Occurrence Number", "Placer Group Number", "Schedule ID", "Event Reason", "Appointment Reason", "Appointment Type", "Appointment Duration", "Appointment Duration Units", "Appointment Timing Quantity", "Placer Contact Person", "Placer Contact Phone Number", "Placer Contact Address", "Placer Contact Location", "Filler Contact Person", "Filler Contact Phone Number", "Filler Contact Address", "Filler Contact Location", "Entered By Person", "Entered By Phone Number", "Entered By Location", "Parent Placer Appointment ID", "Parent Filler Appointment ID", "Filler Status Code", "Placer Order Number", "Filler Order Number",)
    _c_attrs = ("placer_appointment_id", "filler_appointment_id", "occurrence_number", "placer_group_number", "schedule_id", "event_reason", "appointment_reason", "appointment_type", "appointment_duration", "appointment_duration_units", "appointment_timing_quantity", "placer_contact_person", "placer_contact_phone_number", "placer_contact_address", "placer_contact_location", "filler_contact_person", "filler_contact_phone_number", "filler_contact_address", "filler_contact_location", "entered_by_person", "entered_by_phone_number", "entered_by_location", "parent_placer_appointment_id", "parent_filler_appointment_id", "filler_status_code", "placer_order_number", "filler_order_number",)
    # fmt: on

    def __init__(
        self,
        event_reason: CE | tuple[CE],  # SCH.6
        filler_contact_person: XCN | tuple[XCN],  # SCH.16
        entered_by_person: XCN | tuple[XCN],  # SCH.20
        placer_appointment_id: EI | tuple[EI] | None = None,  # SCH.1
        filler_appointment_id: EI | tuple[EI] | None = None,  # SCH.2
        occurrence_number: NM | tuple[NM] | None = None,  # SCH.3
        placer_group_number: EI | tuple[EI] | None = None,  # SCH.4
        schedule_id: CE | tuple[CE] | None = None,  # SCH.5
        appointment_reason: AppointmentReasonCodes
        | CE
        | tuple[AppointmentReasonCodes | CE]
        | None = None,  # SCH.7
        appointment_type: AppointmentTypeCodes
        | CE
        | tuple[AppointmentTypeCodes | CE]
        | None = None,  # SCH.8
        appointment_duration: NM | tuple[NM] | None = None,  # SCH.9
        appointment_duration_units: CE | tuple[CE] | None = None,  # SCH.10
        appointment_timing_quantity: TQ | tuple[TQ] | None = None,  # SCH.11
        placer_contact_person: XCN | tuple[XCN] | None = None,  # SCH.12
        placer_contact_phone_number: XTN | tuple[XTN] | None = None,  # SCH.13
        placer_contact_address: XAD | tuple[XAD] | None = None,  # SCH.14
        placer_contact_location: PL | tuple[PL] | None = None,  # SCH.15
        filler_contact_phone_number: XTN | tuple[XTN] | None = None,  # SCH.17
        filler_contact_address: XAD | tuple[XAD] | None = None,  # SCH.18
        filler_contact_location: PL | tuple[PL] | None = None,  # SCH.19
        entered_by_phone_number: XTN | tuple[XTN] | None = None,  # SCH.21
        entered_by_location: PL | tuple[PL] | None = None,  # SCH.22
        parent_placer_appointment_id: EI | tuple[EI] | None = None,  # SCH.23
        parent_filler_appointment_id: EI | tuple[EI] | None = None,  # SCH.24
        filler_status_code: FillerStatusCodes
        | CE
        | tuple[FillerStatusCodes | CE]
        | None = None,  # SCH.25
        placer_order_number: EI | tuple[EI] | None = None,  # SCH.26
        filler_order_number: EI | tuple[EI] | None = None,  # SCH.27
    ):
        """
        Scheduling Activity Information - `SCH <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH>`_
        The SCH segment contains general information about the scheduled appointment.

        :param placer_appointment_id: Entity Identifier (id: SCH.1 | len: 75 | use: C | rpt: 1)
        :param filler_appointment_id: Entity Identifier (id: SCH.2 | len: 75 | use: C | rpt: 1)
        :param occurrence_number: Numeric (id: SCH.3 | len: 5 | use: C | rpt: 1)
        :param placer_group_number: Entity Identifier (id: SCH.4 | len: 22 | use: O | rpt: 1)
        :param schedule_id: Coded Element (id: SCH.5 | len: 250 | use: O | rpt: 1)
        :param event_reason: Coded Element (id: SCH.6 | len: 250 | use: R | rpt: 1)
        :param appointment_reason: Coded Element (id: SCH.7 | len: 250 | use: O | rpt: 1)
        :param appointment_type: Coded Element (id: SCH.8 | len: 250 | use: O | rpt: 1)
        :param appointment_duration: Numeric (id: SCH.9 | len: 20 | use: B | rpt: 1)
        :param appointment_duration_units: Coded Element (id: SCH.10 | len: 250 | use: B | rpt: 1)
        :param appointment_timing_quantity: Timing Quantity (id: SCH.11 | len: 200 | use: B | rpt: *)
        :param placer_contact_person: Extended Composite ID Number and Name for Persons (id: SCH.12 | len: 250 | use: O | rpt: *)
        :param placer_contact_phone_number: Extended Telecommunication Number (id: SCH.13 | len: 250 | use: O | rpt: 1)
        :param placer_contact_address: Extended Address (id: SCH.14 | len: 250 | use: O | rpt: *)
        :param placer_contact_location: Person Location (id: SCH.15 | len: 80 | use: O | rpt: 1)
        :param filler_contact_person: Extended Composite ID Number and Name for Persons (id: SCH.16 | len: 250 | use: R | rpt: *)
        :param filler_contact_phone_number: Extended Telecommunication Number (id: SCH.17 | len: 250 | use: O | rpt: 1)
        :param filler_contact_address: Extended Address (id: SCH.18 | len: 250 | use: O | rpt: *)
        :param filler_contact_location: Person Location (id: SCH.19 | len: 80 | use: O | rpt: 1)
        :param entered_by_person: Extended Composite ID Number and Name for Persons (id: SCH.20 | len: 250 | use: R | rpt: *)
        :param entered_by_phone_number: Extended Telecommunication Number (id: SCH.21 | len: 250 | use: O | rpt: *)
        :param entered_by_location: Person Location (id: SCH.22 | len: 80 | use: O | rpt: 1)
        :param parent_placer_appointment_id: Entity Identifier (id: SCH.23 | len: 75 | use: O | rpt: 1)
        :param parent_filler_appointment_id: Entity Identifier (id: SCH.24 | len: 75 | use: C | rpt: 1)
        :param filler_status_code: Coded Element (id: SCH.25 | len: 250 | use: O | rpt: 1)
        :param placer_order_number: Entity Identifier (id: SCH.26 | len: 22 | use: C | rpt: *)
        :param filler_order_number: Entity Identifier (id: SCH.27 | len: 22 | use: C | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 27
        self.placer_appointment_id = placer_appointment_id
        self.filler_appointment_id = filler_appointment_id
        self.occurrence_number = occurrence_number
        self.placer_group_number = placer_group_number
        self.schedule_id = schedule_id
        self.event_reason = event_reason
        self.appointment_reason = appointment_reason
        self.appointment_type = appointment_type
        self.appointment_duration = appointment_duration
        self.appointment_duration_units = appointment_duration_units
        self.appointment_timing_quantity = appointment_timing_quantity
        self.placer_contact_person = placer_contact_person
        self.placer_contact_phone_number = placer_contact_phone_number
        self.placer_contact_address = placer_contact_address
        self.placer_contact_location = placer_contact_location
        self.filler_contact_person = filler_contact_person
        self.filler_contact_phone_number = filler_contact_phone_number
        self.filler_contact_address = filler_contact_address
        self.filler_contact_location = filler_contact_location
        self.entered_by_person = entered_by_person
        self.entered_by_phone_number = entered_by_phone_number
        self.entered_by_location = entered_by_location
        self.parent_placer_appointment_id = parent_placer_appointment_id
        self.parent_filler_appointment_id = parent_filler_appointment_id
        self.filler_status_code = filler_status_code
        self.placer_order_number = placer_order_number
        self.filler_order_number = filler_order_number

    @property  # get SCH.1
    def placer_appointment_id(self) -> EI | None:
        """
        id: SCH.1 | len: 75 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.1
        """
        return self._c_data[0][0]

    @placer_appointment_id.setter  # set SCH.1
    def placer_appointment_id(self, ei: EI | None):
        """
        id: SCH.1 | len: 75 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.1
        """
        self._c_data[0] = (ei,)

    @property  # get SCH.2
    def filler_appointment_id(self) -> EI | None:
        """
        id: SCH.2 | len: 75 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.2
        """
        return self._c_data[1][0]

    @filler_appointment_id.setter  # set SCH.2
    def filler_appointment_id(self, ei: EI | None):
        """
        id: SCH.2 | len: 75 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.2
        """
        self._c_data[1] = (ei,)

    @property  # get SCH.3
    def occurrence_number(self) -> NM | None:
        """
        id: SCH.3 | len: 5 | use: C | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.3
        """
        return self._c_data[2][0]

    @occurrence_number.setter  # set SCH.3
    def occurrence_number(self, nm: NM | None):
        """
        id: SCH.3 | len: 5 | use: C | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.3
        """
        self._c_data[2] = (nm,)

    @property  # get SCH.4
    def placer_group_number(self) -> EI | None:
        """
        id: SCH.4 | len: 22 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.4
        """
        return self._c_data[3][0]

    @placer_group_number.setter  # set SCH.4
    def placer_group_number(self, ei: EI | None):
        """
        id: SCH.4 | len: 22 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.4
        """
        self._c_data[3] = (ei,)

    @property  # get SCH.5
    def schedule_id(self) -> CE | None:
        """
        id: SCH.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.5
        """
        return self._c_data[4][0]

    @schedule_id.setter  # set SCH.5
    def schedule_id(self, ce: CE | None):
        """
        id: SCH.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.5
        """
        self._c_data[4] = (ce,)

    @property  # get SCH.6
    def event_reason(self) -> CE:
        """
        id: SCH.6 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.6
        """
        return self._c_data[5][0]

    @event_reason.setter  # set SCH.6
    def event_reason(self, ce: CE):
        """
        id: SCH.6 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.6
        """
        self._c_data[5] = (ce,)

    @property  # get SCH.7
    def appointment_reason(self) -> AppointmentReasonCodes | None:
        """
        id: SCH.7 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.7
        """
        return self._c_data[6][0]

    @appointment_reason.setter  # set SCH.7
    def appointment_reason(
        self, appointment_reason_codes: AppointmentReasonCodes | None
    ):
        """
        id: SCH.7 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.7
        """
        self._c_data[6] = (appointment_reason_codes,)

    @property  # get SCH.8
    def appointment_type(self) -> AppointmentTypeCodes | None:
        """
        id: SCH.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.8
        """
        return self._c_data[7][0]

    @appointment_type.setter  # set SCH.8
    def appointment_type(self, appointment_type_codes: AppointmentTypeCodes | None):
        """
        id: SCH.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.8
        """
        self._c_data[7] = (appointment_type_codes,)

    @property  # get SCH.9
    def appointment_duration(self) -> NM | None:
        """
        id: SCH.9 | len: 20 | use: B | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.9
        """
        return self._c_data[8][0]

    @appointment_duration.setter  # set SCH.9
    def appointment_duration(self, nm: NM | None):
        """
        id: SCH.9 | len: 20 | use: B | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.9
        """
        self._c_data[8] = (nm,)

    @property  # get SCH.10
    def appointment_duration_units(self) -> CE | None:
        """
        id: SCH.10 | len: 250 | use: B | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.10
        """
        return self._c_data[9][0]

    @appointment_duration_units.setter  # set SCH.10
    def appointment_duration_units(self, ce: CE | None):
        """
        id: SCH.10 | len: 250 | use: B | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.10
        """
        self._c_data[9] = (ce,)

    @property
    def appointment_timing_quantity(self) -> tuple[TQ, ...] | tuple[None]:
        """
        id: SCH.11 | len: 200 | use: B | rpt: *
        ---
        return_type: tuple[TQ, ...]: (Timing Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.11
        """
        return self._c_data[10]

    @appointment_timing_quantity.setter  # set SCH.11
    def appointment_timing_quantity(self, tq: TQ | tuple[TQ] | None):
        """
        id: SCH.11 | len: 200 | use: B | rpt: *
        ---
        param_type: TQ | tuple[TQ, ...]: (Timing Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.11
        """
        if isinstance(tq, tuple):
            self._c_data[10] = tq
        else:
            self._c_data[10] = (tq,)

    @property
    def placer_contact_person(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: SCH.12 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.12
        """
        return self._c_data[11]

    @placer_contact_person.setter  # set SCH.12
    def placer_contact_person(self, xcn: XCN | tuple[XCN] | None):
        """
        id: SCH.12 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.12
        """
        if isinstance(xcn, tuple):
            self._c_data[11] = xcn
        else:
            self._c_data[11] = (xcn,)

    @property  # get SCH.13
    def placer_contact_phone_number(self) -> XTN | None:
        """
        id: SCH.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.13
        """
        return self._c_data[12][0]

    @placer_contact_phone_number.setter  # set SCH.13
    def placer_contact_phone_number(self, xtn: XTN | None):
        """
        id: SCH.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.13
        """
        self._c_data[12] = (xtn,)

    @property
    def placer_contact_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: SCH.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.14
        """
        return self._c_data[13]

    @placer_contact_address.setter  # set SCH.14
    def placer_contact_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: SCH.14 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.14
        """
        if isinstance(xad, tuple):
            self._c_data[13] = xad
        else:
            self._c_data[13] = (xad,)

    @property  # get SCH.15
    def placer_contact_location(self) -> PL | None:
        """
        id: SCH.15 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.15
        """
        return self._c_data[14][0]

    @placer_contact_location.setter  # set SCH.15
    def placer_contact_location(self, pl: PL | None):
        """
        id: SCH.15 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.15
        """
        self._c_data[14] = (pl,)

    @property
    def filler_contact_person(self) -> tuple[XCN, ...]:
        """
        id: SCH.16 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.16
        """
        return self._c_data[15]

    @filler_contact_person.setter  # set SCH.16
    def filler_contact_person(self, xcn: XCN | tuple[XCN]):
        """
        id: SCH.16 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.16
        """
        if isinstance(xcn, tuple):
            self._c_data[15] = xcn
        else:
            self._c_data[15] = (xcn,)

    @property  # get SCH.17
    def filler_contact_phone_number(self) -> XTN | None:
        """
        id: SCH.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.17
        """
        return self._c_data[16][0]

    @filler_contact_phone_number.setter  # set SCH.17
    def filler_contact_phone_number(self, xtn: XTN | None):
        """
        id: SCH.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: XTN: Extended Telecommunication Number
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.17
        """
        self._c_data[16] = (xtn,)

    @property
    def filler_contact_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: SCH.18 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.18
        """
        return self._c_data[17]

    @filler_contact_address.setter  # set SCH.18
    def filler_contact_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: SCH.18 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.18
        """
        if isinstance(xad, tuple):
            self._c_data[17] = xad
        else:
            self._c_data[17] = (xad,)

    @property  # get SCH.19
    def filler_contact_location(self) -> PL | None:
        """
        id: SCH.19 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.19
        """
        return self._c_data[18][0]

    @filler_contact_location.setter  # set SCH.19
    def filler_contact_location(self, pl: PL | None):
        """
        id: SCH.19 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.19
        """
        self._c_data[18] = (pl,)

    @property
    def entered_by_person(self) -> tuple[XCN, ...]:
        """
        id: SCH.20 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.20
        """
        return self._c_data[19]

    @entered_by_person.setter  # set SCH.20
    def entered_by_person(self, xcn: XCN | tuple[XCN]):
        """
        id: SCH.20 | len: 250 | use: R | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.20
        """
        if isinstance(xcn, tuple):
            self._c_data[19] = xcn
        else:
            self._c_data[19] = (xcn,)

    @property
    def entered_by_phone_number(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: SCH.21 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.21
        """
        return self._c_data[20]

    @entered_by_phone_number.setter  # set SCH.21
    def entered_by_phone_number(self, xtn: XTN | tuple[XTN] | None):
        """
        id: SCH.21 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.21
        """
        if isinstance(xtn, tuple):
            self._c_data[20] = xtn
        else:
            self._c_data[20] = (xtn,)

    @property  # get SCH.22
    def entered_by_location(self) -> PL | None:
        """
        id: SCH.22 | len: 80 | use: O | rpt: 1
        ---
        return_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.22
        """
        return self._c_data[21][0]

    @entered_by_location.setter  # set SCH.22
    def entered_by_location(self, pl: PL | None):
        """
        id: SCH.22 | len: 80 | use: O | rpt: 1
        ---
        param_type: PL: Person Location
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.22
        """
        self._c_data[21] = (pl,)

    @property  # get SCH.23
    def parent_placer_appointment_id(self) -> EI | None:
        """
        id: SCH.23 | len: 75 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.23
        """
        return self._c_data[22][0]

    @parent_placer_appointment_id.setter  # set SCH.23
    def parent_placer_appointment_id(self, ei: EI | None):
        """
        id: SCH.23 | len: 75 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.23
        """
        self._c_data[22] = (ei,)

    @property  # get SCH.24
    def parent_filler_appointment_id(self) -> EI | None:
        """
        id: SCH.24 | len: 75 | use: C | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.24
        """
        return self._c_data[23][0]

    @parent_filler_appointment_id.setter  # set SCH.24
    def parent_filler_appointment_id(self, ei: EI | None):
        """
        id: SCH.24 | len: 75 | use: C | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.24
        """
        self._c_data[23] = (ei,)

    @property  # get SCH.25
    def filler_status_code(self) -> FillerStatusCodes | None:
        """
        id: SCH.25 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.25
        """
        return self._c_data[24][0]

    @filler_status_code.setter  # set SCH.25
    def filler_status_code(self, filler_status_codes: FillerStatusCodes | None):
        """
        id: SCH.25 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.25
        """
        self._c_data[24] = (filler_status_codes,)

    @property
    def placer_order_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: SCH.26 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.26
        """
        return self._c_data[25]

    @placer_order_number.setter  # set SCH.26
    def placer_order_number(self, ei: EI | tuple[EI] | None):
        """
        id: SCH.26 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.26
        """
        if isinstance(ei, tuple):
            self._c_data[25] = ei
        else:
            self._c_data[25] = (ei,)

    @property
    def filler_order_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: SCH.27 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.27
        """
        return self._c_data[26]

    @filler_order_number.setter  # set SCH.27
    def filler_order_number(self, ei: EI | tuple[EI] | None):
        """
        id: SCH.27 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SCH.27
        """
        if isinstance(ei, tuple):
            self._c_data[26] = ei
        else:
            self._c_data[26] = (ei,)
