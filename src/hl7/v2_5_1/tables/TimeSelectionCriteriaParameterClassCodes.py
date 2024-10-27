from ...base import HL7Table

"""
HL7 Version: 2.5.1
Time selection criteria parameter class codes - 0294
Table Type: User
"""


class TimeSelectionCriteriaParameterClassCodes(HL7Table):
    """
    Time selection criteria parameter class codes - 0294 // User table type
    - AN_INDICATOR_THAT_FRIDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    - AN_INDICATOR_THAT_MONDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    - AN_INDICATOR_THAT_THERE_IS_A_PREFERRED_END_TIME_FOR_THE_APPOINTMENT_REQUEST_SERVICE_OR_RESOURCE
    - AN_INDICATOR_THAT_THERE_IS_A_PREFERRED_START_TIME_FOR_THE_APPOINTMENT_REQUEST_SERVICE_OR_RESOURCE
    - AN_INDICATOR_THAT_SATURDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    - AN_INDICATOR_THAT_SUNDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    - AN_INDICATOR_THAT_THURSDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    - AN_INDICATOR_THAT_TUESDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    - AN_INDICATOR_THAT_WEDNESDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0294
    """

    AN_INDICATOR_THAT_FRIDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Fri"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Friday is or is not preferred for the day on which the appointment will occur."""
    AN_INDICATOR_THAT_MONDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Mon"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Monday is or is not preferred for the day on which the appointment will occur."""
    AN_INDICATOR_THAT_THERE_IS_A_PREFERRED_END_TIME_FOR_THE_APPOINTMENT_REQUEST_SERVICE_OR_RESOURCE = "Prefend"  # In component 2, specify any valid time in the format HHMM, using 24-hour clock notation where HH = hour and MM = minutes
    """An indicator that there is a preferred end time for the appointment request, service or resource."""
    AN_INDICATOR_THAT_THERE_IS_A_PREFERRED_START_TIME_FOR_THE_APPOINTMENT_REQUEST_SERVICE_OR_RESOURCE = "Prefstart"  # In component 2, specify any valid time in the format HHMM, using 24-hour clock notation where HH = hour and MM = minutes
    """An indicator that there is a preferred start time for the appointment request, service or resource."""
    AN_INDICATOR_THAT_SATURDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Sat"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Saturday is or is not preferred for the day on which the appointment will occur."""
    AN_INDICATOR_THAT_SUNDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Sun"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Sunday is or is not preferred for the day on which the appointment will occur."""
    AN_INDICATOR_THAT_THURSDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Thu"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Thursday is or is not preferred for the day on which the appointment will occur."""
    AN_INDICATOR_THAT_TUESDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Tue"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Tuesday is or is not preferred for the day on which the appointment will occur."""
    AN_INDICATOR_THAT_WEDNESDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR = "Wed"  # In component 2, specify OK or NO. OK = Preferred appointment day NO = Day is not preferred
    """An indicator that Wednesday is or is not preferred for the day on which the appointment will occur."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_FRIDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Friday is or is not preferred for the day on which the appointment will occur.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_MONDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Monday is or is not preferred for the day on which the appointment will occur.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_THERE_IS_A_PREFERRED_END_TIME_FOR_THE_APPOINTMENT_REQUEST_SERVICE_OR_RESOURCE: "An indicator that there is a preferred end time for the appointment request, service or resource.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_THERE_IS_A_PREFERRED_START_TIME_FOR_THE_APPOINTMENT_REQUEST_SERVICE_OR_RESOURCE: "An indicator that there is a preferred start time for the appointment request, service or resource.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_SATURDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Saturday is or is not preferred for the day on which the appointment will occur.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_SUNDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Sunday is or is not preferred for the day on which the appointment will occur.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_THURSDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Thursday is or is not preferred for the day on which the appointment will occur.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_TUESDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Tuesday is or is not preferred for the day on which the appointment will occur.",
    TimeSelectionCriteriaParameterClassCodes.AN_INDICATOR_THAT_WEDNESDAY_IS_OR_IS_NOT_PREFERRED_FOR_THE_DAY_ON_WHICH_THE_APPOINTMENT_WILL_OCCUR: "An indicator that Wednesday is or is not preferred for the day on which the appointment will occur.",
}
