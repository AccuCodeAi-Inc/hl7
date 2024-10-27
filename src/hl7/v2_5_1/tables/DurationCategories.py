from ...base import HL7Table

"""
HL7 Version: 2.5.1
Duration categories - 0255
Table Type: User
"""


class DurationCategories(HL7Table):
    """
    Duration categories - 0255 // User table type
    - STAR
    - _12_HOURS
    - _1_HOUR
    - _1_MONTHS
    - _1_WEEK
    - _2_HOURS
    - _24_HOURS
    - _2_DAYS
    - _2H
    - _2_MONTHS
    - _2_WEEKS
    - _30_MINUTES
    - _3_DAYS
    - _3_HOURS
    - _3_MONTHS
    - _3_WEEKS
    - _4_DAYS
    - _4_HOURS
    - _4_WEEKS
    - _5_DAYS
    - _5_HOURS
    - _6_DAYS
    - _6_HOURS
    - _7_HOURS
    - _8_HOURS
    - TO_IDENTIFY_MEASURES_AT_A_POINT_IN_TIME_THIS_IS_A_SYNONYM_FOR_SPOT_OR_RANDOM_AS_APPLIED_TO_URINE_MEASUREMENTS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0255
    """

    STAR = "*"
    """(asterisk) Life of the unit. Used for blood products."""
    _12_HOURS = "12H"
    """12 hours"""
    _1_HOUR = "1H"
    """1 hour"""
    _1_MONTHS = "1L"
    """1 months (30 days)"""
    _1_WEEK = "1W"
    """1 week"""
    _2_HOURS = "2.5H"
    """2 hours"""
    _24_HOURS = "24H"
    """24 hours"""
    _2_DAYS = "2D"
    """2 days"""
    _2H = "2H"
    """2 hours"""
    _2_MONTHS = "2L"
    """2 months"""
    _2_WEEKS = "2W"
    """2 weeks"""
    _30_MINUTES = "30M"
    """30 minutes"""
    _3_DAYS = "3D"
    """3 days"""
    _3_HOURS = "3H"
    """3 hours"""
    _3_MONTHS = "3L"
    """3 months"""
    _3_WEEKS = "3W"
    """3 weeks"""
    _4_DAYS = "4D"
    """4 days"""
    _4_HOURS = "4H"
    """4 hours"""
    _4_WEEKS = "4W"
    """4 weeks"""
    _5_DAYS = "5D"
    """5 days"""
    _5_HOURS = "5H"
    """5 hours"""
    _6_DAYS = "6D"
    """6 days"""
    _6_HOURS = "6H"
    """6 hours"""
    _7_HOURS = "7H"
    """7 hours"""
    _8_HOURS = "8H"
    """8 hours"""
    TO_IDENTIFY_MEASURES_AT_A_POINT_IN_TIME_THIS_IS_A_SYNONYM_FOR_SPOT_OR_RANDOM_AS_APPLIED_TO_URINE_MEASUREMENTS = "PT"
    """To identify measures at a point in time. This is a synonym for spot or random as applied to urine measurements."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DurationCategories.STAR: "(asterisk) Life of the unit. Used for blood products.",
    DurationCategories._12_HOURS: "12 hours",
    DurationCategories._1_HOUR: "1 hour",
    DurationCategories._1_MONTHS: "1 months (30 days)",
    DurationCategories._1_WEEK: "1 week",
    DurationCategories._2_HOURS: "2 hours",
    DurationCategories._24_HOURS: "24 hours",
    DurationCategories._2_DAYS: "2 days",
    DurationCategories._2H: "2 hours",
    DurationCategories._2_MONTHS: "2 months",
    DurationCategories._2_WEEKS: "2 weeks",
    DurationCategories._30_MINUTES: "30 minutes",
    DurationCategories._3_DAYS: "3 days",
    DurationCategories._3_HOURS: "3 hours",
    DurationCategories._3_MONTHS: "3 months",
    DurationCategories._3_WEEKS: "3 weeks",
    DurationCategories._4_DAYS: "4 days",
    DurationCategories._4_HOURS: "4 hours",
    DurationCategories._4_WEEKS: "4 weeks",
    DurationCategories._5_DAYS: "5 days",
    DurationCategories._5_HOURS: "5 hours",
    DurationCategories._6_DAYS: "6 days",
    DurationCategories._6_HOURS: "6 hours",
    DurationCategories._7_HOURS: "7 hours",
    DurationCategories._8_HOURS: "8 hours",
    DurationCategories.TO_IDENTIFY_MEASURES_AT_A_POINT_IN_TIME_THIS_IS_A_SYNONYM_FOR_SPOT_OR_RANDOM_AS_APPLIED_TO_URINE_MEASUREMENTS: "To identify measures at a point in time. This is a synonym for spot or random as applied to urine measurements.",
}
