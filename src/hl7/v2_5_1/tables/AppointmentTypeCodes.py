from ...base import HL7Table

"""
HL7 Version: 2.5.1
Appointment Type Codes - 0277
Table Type: User
"""


class AppointmentTypeCodes(HL7Table):
    """
    Appointment Type Codes - 0277 // User table type
    - A_REQUEST_TO_ADD_A_COMPLETED_APPOINTMENT_USED_TO_MAINTAIN_RECORDS_OF_COMPLETED_APPOINTMENTS_THAT_DID_NOT_APPEAR_IN_THE_SCHEDULE
    - ROUTINE_SCHEDULE_REQUEST_TYPE_DEFAULT_IF_NOT_VALUED
    - A_REQUEST_FOR_A_TENTATIVE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0277
    """

    A_REQUEST_TO_ADD_A_COMPLETED_APPOINTMENT_USED_TO_MAINTAIN_RECORDS_OF_COMPLETED_APPOINTMENTS_THAT_DID_NOT_APPEAR_IN_THE_SCHEDULE = "Complete"
    """A request to add a completed appointment, used to maintain records of completed appointments that did not appear in the schedule (e.g., STAT, walk-in, etc.)"""
    ROUTINE_SCHEDULE_REQUEST_TYPE_DEFAULT_IF_NOT_VALUED = "Normal"
    """Routine schedule request type - default if not valued"""
    A_REQUEST_FOR_A_TENTATIVE = "Tentative"
    """A request for a tentative (e.g., penciled in) appointment"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AppointmentTypeCodes.A_REQUEST_TO_ADD_A_COMPLETED_APPOINTMENT_USED_TO_MAINTAIN_RECORDS_OF_COMPLETED_APPOINTMENTS_THAT_DID_NOT_APPEAR_IN_THE_SCHEDULE: "A request to add a completed appointment, used to maintain records of completed appointments that did not appear in the schedule (e.g., STAT, walk-in, etc.)",
    AppointmentTypeCodes.ROUTINE_SCHEDULE_REQUEST_TYPE_DEFAULT_IF_NOT_VALUED: "Routine schedule request type - default if not valued",
    AppointmentTypeCodes.A_REQUEST_FOR_A_TENTATIVE: "A request for a tentative (e.g., penciled in) appointment",
}
