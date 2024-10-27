from ...base import HL7Table

"""
HL7 Version: 2.5.1
Appointment reason codes - 0276
Table Type: User
"""


class AppointmentReasonCodes(HL7Table):
    """
    Appointment reason codes - 0276 // User table type
    - A_ROUTINE_CHECK_UP_SUCH_AS_AN_ANNUAL_PHYSICAL
    - EMERGENCY_APPOINTMENT
    - A_FOLLOW_UP_VISIT_FROM_A_PREVIOUS_APPOINTMENT
    - ROUTINE_APPOINTMENT_DEFAULT_IF_NOT_VALUED
    - A_PREVIOUSLY_UNSCHEDULED_WALK_IN_VISIT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0276
    """

    A_ROUTINE_CHECK_UP_SUCH_AS_AN_ANNUAL_PHYSICAL = "CHECKUP"
    """A routine check-up, such as an annual physical"""
    EMERGENCY_APPOINTMENT = "EMERGENCY"
    """Emergency appointment"""
    A_FOLLOW_UP_VISIT_FROM_A_PREVIOUS_APPOINTMENT = "FOLLOWUP"
    """A follow up visit from a previous appointment"""
    ROUTINE_APPOINTMENT_DEFAULT_IF_NOT_VALUED = "ROUTINE"
    """Routine appointment - default if not valued"""
    A_PREVIOUSLY_UNSCHEDULED_WALK_IN_VISIT = "WALKIN"
    """A previously unscheduled walk-in visit"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AppointmentReasonCodes.A_ROUTINE_CHECK_UP_SUCH_AS_AN_ANNUAL_PHYSICAL: "A routine check-up, such as an annual physical",
    AppointmentReasonCodes.EMERGENCY_APPOINTMENT: "Emergency appointment",
    AppointmentReasonCodes.A_FOLLOW_UP_VISIT_FROM_A_PREVIOUS_APPOINTMENT: "A follow up visit from a previous appointment",
    AppointmentReasonCodes.ROUTINE_APPOINTMENT_DEFAULT_IF_NOT_VALUED: "Routine appointment - default if not valued",
    AppointmentReasonCodes.A_PREVIOUSLY_UNSCHEDULED_WALK_IN_VISIT: "A previously unscheduled walk-in visit",
}
