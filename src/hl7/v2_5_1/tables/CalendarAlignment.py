from ...base import HL7Table

"""
HL7 Version: 2.5.1
Calendar alignment - 0527
Table Type: HL7
"""


class CalendarAlignment(HL7Table):
    """
    Calendar alignment - 0527 // HL7 table type
    - DAY_OF_THE_MONTH
    - DAY_OF_THE_WEEK
    - DAY_OF_THE_YEAR
    - HOUR_OF_THE_DAY
    - MONTH_OF_THE_YEAR
    - MINUTE_OF_THE_HOUR
    - SECOND_OF_THE_MINUTE
    - WEEK_OF_THE_YEAR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0527
    """

    DAY_OF_THE_MONTH = "DM"  # d
    """day of the month"""
    DAY_OF_THE_WEEK = "DW"  # d
    """day of the week (begins with Monday)"""
    DAY_OF_THE_YEAR = "DY"  # d
    """day of the year"""
    HOUR_OF_THE_DAY = "HD"  # h
    """hour of the day"""
    MONTH_OF_THE_YEAR = "MY"  # mo
    """month of the year"""
    MINUTE_OF_THE_HOUR = "NH"  # min
    """minute of the hour"""
    SECOND_OF_THE_MINUTE = "SN"  # s
    """second of the minute"""
    WEEK_OF_THE_YEAR = "WY"  # wk
    """week of the year"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CalendarAlignment.DAY_OF_THE_MONTH: "day of the month",
    CalendarAlignment.DAY_OF_THE_WEEK: "day of the week (begins with Monday)",
    CalendarAlignment.DAY_OF_THE_YEAR: "day of the year",
    CalendarAlignment.HOUR_OF_THE_DAY: "hour of the day",
    CalendarAlignment.MONTH_OF_THE_YEAR: "month of the year",
    CalendarAlignment.MINUTE_OF_THE_HOUR: "minute of the hour",
    CalendarAlignment.SECOND_OF_THE_MINUTE: "second of the minute",
    CalendarAlignment.WEEK_OF_THE_YEAR: "week of the year",
}
