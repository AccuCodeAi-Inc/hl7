from ...base import HL7Table

"""
HL7 Version: 2.5.1
Days of the week - 0267
Table Type: HL7
"""


class DaysOfTheWeek(HL7Table):
    """
    Days of the week - 0267 // HL7 table type
    - FRIDAY
    - MONDAY
    - SATURDAY
    - SUNDAY
    - THURSDAY
    - TUESDAY
    - WEDNESDAY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0267
    """

    FRIDAY = "FRI"
    """Friday"""
    MONDAY = "MON"
    """Monday"""
    SATURDAY = "SAT"
    """Saturday"""
    SUNDAY = "SUN"
    """Sunday"""
    THURSDAY = "THU"
    """Thursday"""
    TUESDAY = "TUE"
    """Tuesday"""
    WEDNESDAY = "WED"
    """Wednesday"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DaysOfTheWeek.FRIDAY: "Friday",
    DaysOfTheWeek.MONDAY: "Monday",
    DaysOfTheWeek.SATURDAY: "Saturday",
    DaysOfTheWeek.SUNDAY: "Sunday",
    DaysOfTheWeek.THURSDAY: "Thursday",
    DaysOfTheWeek.TUESDAY: "Tuesday",
    DaysOfTheWeek.WEDNESDAY: "Wednesday",
}
