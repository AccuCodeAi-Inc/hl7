from ...base import HL7Table

"""
HL7 Version: 2.5.1
Filler status codes - 0278
Table Type: User
"""


class FillerStatusCodes(HL7Table):
    """
    Filler status codes - 0278 // User table type
    - THE_INDICATED_TIME_SLOT
    - THE_INDICATED_APPOINTMENT_IS_BOOKED
    - THE_INDICATED_APPOINTMENT_WAS_STOPPED_FROM_OCCURRING
    - THE_INDICATED_APPOINTMENT_HAS_COMPLETED_NORMALLY
    - THE_INDICATED_APPOINTMENT_WAS_DISCONTINUED
    - THE_INDICATED_APPOINTMENT_WAS_DELETED_FROM_THE_FILLER_APPLICATION
    - THE_PATIENT_DID_NOT_SHOW_UP_FOR_THE_APPOINTMENT
    - THE_APPOINTMENT_HAS_BEEN_CONFIRMED_HOWEVER_IT_IS_CONFIRMED_IN_AN_OVERBOOKED_STATE
    - APPOINTMENT_HAS_NOT_YET_BEEN_CONFIRMED
    - THE_INDICATED_APPOINTMENT_HAS_BEGUN_AND_IS_CURRENTLY_IN_PROGRESS
    - APPOINTMENT_HAS_BEEN_PLACED_ON_A_WAITING_LIST_FOR_A_PARTICULAR_SLOT_OR_SET_OF_SLOTS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0278
    """

    THE_INDICATED_TIME_SLOT = "Blocked"
    """The indicated time slot(s) is(are) blocked"""
    THE_INDICATED_APPOINTMENT_IS_BOOKED = "Booked"
    """The indicated appointment is booked"""
    THE_INDICATED_APPOINTMENT_WAS_STOPPED_FROM_OCCURRING = "Cancelled"
    """The indicated appointment was stopped from occurring (canceled prior to starting)"""
    THE_INDICATED_APPOINTMENT_HAS_COMPLETED_NORMALLY = "Complete"
    """The indicated appointment has completed normally (was not discontinued, canceled, or deleted)"""
    THE_INDICATED_APPOINTMENT_WAS_DISCONTINUED = "Dc"
    """The indicated appointment was discontinued (DCed while in progress, discontinued parent appointment, or discontinued child appointment)"""
    THE_INDICATED_APPOINTMENT_WAS_DELETED_FROM_THE_FILLER_APPLICATION = "Deleted"
    """The indicated appointment was deleted from the filler application"""
    THE_PATIENT_DID_NOT_SHOW_UP_FOR_THE_APPOINTMENT = "Noshow"
    """The patient did not show up for the appointment"""
    THE_APPOINTMENT_HAS_BEEN_CONFIRMED_HOWEVER_IT_IS_CONFIRMED_IN_AN_OVERBOOKED_STATE = "Overbook"
    """The appointment has been confirmed; however it is confirmed in an overbooked state"""
    APPOINTMENT_HAS_NOT_YET_BEEN_CONFIRMED = "Pending"
    """Appointment has not yet been confirmed"""
    THE_INDICATED_APPOINTMENT_HAS_BEGUN_AND_IS_CURRENTLY_IN_PROGRESS = "Started"
    """The indicated appointment has begun and is currently in progress"""
    APPOINTMENT_HAS_BEEN_PLACED_ON_A_WAITING_LIST_FOR_A_PARTICULAR_SLOT_OR_SET_OF_SLOTS = "Waitlist"
    """Appointment has been placed on a waiting list for a particular slot, or set of slots"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    FillerStatusCodes.THE_INDICATED_TIME_SLOT: "The indicated time slot(s) is(are) blocked",
    FillerStatusCodes.THE_INDICATED_APPOINTMENT_IS_BOOKED: "The indicated appointment is booked",
    FillerStatusCodes.THE_INDICATED_APPOINTMENT_WAS_STOPPED_FROM_OCCURRING: "The indicated appointment was stopped from occurring (canceled prior to starting)",
    FillerStatusCodes.THE_INDICATED_APPOINTMENT_HAS_COMPLETED_NORMALLY: "The indicated appointment has completed normally (was not discontinued, canceled, or deleted)",
    FillerStatusCodes.THE_INDICATED_APPOINTMENT_WAS_DISCONTINUED: "The indicated appointment was discontinued (DCed while in progress, discontinued parent appointment, or discontinued child appointment)",
    FillerStatusCodes.THE_INDICATED_APPOINTMENT_WAS_DELETED_FROM_THE_FILLER_APPLICATION: "The indicated appointment was deleted from the filler application",
    FillerStatusCodes.THE_PATIENT_DID_NOT_SHOW_UP_FOR_THE_APPOINTMENT: "The patient did not show up for the appointment",
    FillerStatusCodes.THE_APPOINTMENT_HAS_BEEN_CONFIRMED_HOWEVER_IT_IS_CONFIRMED_IN_AN_OVERBOOKED_STATE: "The appointment has been confirmed; however it is confirmed in an overbooked state",
    FillerStatusCodes.APPOINTMENT_HAS_NOT_YET_BEEN_CONFIRMED: "Appointment has not yet been confirmed",
    FillerStatusCodes.THE_INDICATED_APPOINTMENT_HAS_BEGUN_AND_IS_CURRENTLY_IN_PROGRESS: "The indicated appointment has begun and is currently in progress",
    FillerStatusCodes.APPOINTMENT_HAS_BEEN_PLACED_ON_A_WAITING_LIST_FOR_A_PARTICULAR_SLOT_OR_SET_OF_SLOTS: "Appointment has been placed on a waiting list for a particular slot, or set of slots",
}
