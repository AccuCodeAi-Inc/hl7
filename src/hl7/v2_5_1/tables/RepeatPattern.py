from ...base import HL7Table

"""
HL7 Version: 2.5.1
Repeat pattern - 0335
Table Type: User
"""


class RepeatPattern(HL7Table):
    """
    Repeat pattern - 0335 // User table type
    - ANTE
    - TWICE_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES
    - SERVICE_IS_PROVIDED_CONTINUOUSLY_BETWEEN_START_TIME_AND_STOP_TIME
    - CIBUS_DIURNUS
    - INTER
    - CIBUS_MATUTINUS
    - BELOW_TIMING_ABOVE_C
    - ONE_TIME_ONLY
    - POST
    - GIVEN_AS_NEEDED
    - WHERE_XXX_IS_SOME_FREQUENCY_CODE
    - EVERY_BELOW_INTEGER_ABOVE_DAYS
    - EVERY_BELOW_INTEGER_ABOVE_HOURS
    - REPEATS_ON_A_PARTICULAR_DAY_OF_THE_WEEK
    - EVERY_BELOW_INTEGER_ABOVE_MONTHS
    - EVERY_BELOW_INTEGER_ABOVE_MINUTES
    - EVERY_BELOW_INTEGER_ABOVE_SECONDS
    - EVERY_BELOW_INTEGER_ABOVE_WEEKS
    - IN_THE_MORNING_AT_INSTITUTION_SPECIFIED_TIME
    - EVERY_DAY_BEFORE_THE_HOUR_OF_SLEEP
    - FOUR_TIMES_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES
    - EVERY_OTHER_DAY
    - IN_THE_EVENING_AT_INSTITUTION_SPECIFIED_TIME
    - DURING_EACH_OF_THREE_EIGHT_HOUR_SHIFTS_AT_INSTITUTION_SPECIFIED_TIMES
    - THREE_TIMES_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES
    - FOR_FUTURE_USE_WHERE_BELOW_SPEC_ABOVE_IS_AN_INTERVAL_SPECIFICATION_AS_DEFINED_BY_THE_UNIX_CRON_SPECIFICATION
    - CIBUS_VESPERTINUS
    - X_TIMES_PER_DAY_AT_INSTITUTION_SPECIFIED_TIMES_WHERE_X_IS_A_NUMERAL_5_OR_GREATER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0335
    """

    ANTE = "A"
    """Ante (before)"""
    TWICE_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES = "BID"  # (e.g., 9AM-4PM)
    """twice a day at institution-specified times"""
    SERVICE_IS_PROVIDED_CONTINUOUSLY_BETWEEN_START_TIME_AND_STOP_TIME = "C"
    """service is provided continuously between start time and stop time"""
    CIBUS_DIURNUS = "D"
    """Cibus Diurnus (lunch)"""
    INTER = "I"  # (e.g., between this meal and the next, between dinner and sleep
    """Inter"""
    CIBUS_MATUTINUS = "M"
    """Cibus Matutinus (breakfast)"""
    BELOW_TIMING_ABOVE_C = "Meal Related Timings"
    """&lt;timing&gt;C (cum)&lt;meal&gt;"""
    ONE_TIME_ONLY = "Once"  # This is also the default when this component is null.
    """one time only."""
    POST = "P"
    """Post (after)"""
    GIVEN_AS_NEEDED = "PRN"
    """given as needed"""
    WHERE_XXX_IS_SOME_FREQUENCY_CODE = (
        "PRNxxx"  # (e.g., PRNQ6H); given as needed over the frequency period.
    )
    """where xxx is some frequency code"""
    EVERY_BELOW_INTEGER_ABOVE_DAYS = "Q<integer>D"
    """every &lt;integer&gt; days"""
    EVERY_BELOW_INTEGER_ABOVE_HOURS = "Q<integer>H"
    """every &lt;integer&gt; hours"""
    REPEATS_ON_A_PARTICULAR_DAY_OF_THE_WEEK = "Q<integer>J<day#>"  # From the French jour (day). If &lt;integer&gt; is missing, the repeat rate is assumed to be 1. Day numbers are counted from 1=Monday to 7=Sunday. So Q2J2 means every second Tuesday; Q1J6 means every Saturday.
    """repeats on a particular day of the week,"""
    EVERY_BELOW_INTEGER_ABOVE_MONTHS = "Q<integer>L"
    """every &lt;integer&gt; months (Lunar cycle)"""
    EVERY_BELOW_INTEGER_ABOVE_MINUTES = "Q<integer>M"
    """every &lt;integer&gt; minutes"""
    EVERY_BELOW_INTEGER_ABOVE_SECONDS = "Q<integer>S"
    """every &lt;integer&gt; seconds"""
    EVERY_BELOW_INTEGER_ABOVE_WEEKS = "Q<integer>W"
    """every &lt;integer&gt; weeks"""
    IN_THE_MORNING_AT_INSTITUTION_SPECIFIED_TIME = "QAM"
    """in the morning at institution-specified time"""
    EVERY_DAY_BEFORE_THE_HOUR_OF_SLEEP = "QHS"
    """every day before the hour of sleep"""
    FOUR_TIMES_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES = "QID"  # (e.g., 9AM-11AM-4PM-9PM)
    """four times a day at institution-specified times"""
    EVERY_OTHER_DAY = "QOD"  # (same as Q2D)
    """every other day"""
    IN_THE_EVENING_AT_INSTITUTION_SPECIFIED_TIME = "QPM"
    """in the evening at institution-specified time"""
    DURING_EACH_OF_THREE_EIGHT_HOUR_SHIFTS_AT_INSTITUTION_SPECIFIED_TIMES = "QSHIFT"
    """during each of three eight-hour shifts at institution-specified times"""
    THREE_TIMES_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES = "TID"  # (e.g., 9AM-4PM-9PM)
    """three times a day at institution-specified times"""
    FOR_FUTURE_USE_WHERE_BELOW_SPEC_ABOVE_IS_AN_INTERVAL_SPECIFICATION_AS_DEFINED_BY_THE_UNIX_CRON_SPECIFICATION = "U <spec>"
    """for future use, where &lt;spec&gt; is an interval specification as defined by the UNIX cron specification."""
    CIBUS_VESPERTINUS = "V"
    """Cibus Vespertinus (dinner)"""
    X_TIMES_PER_DAY_AT_INSTITUTION_SPECIFIED_TIMES_WHERE_X_IS_A_NUMERAL_5_OR_GREATER = (
        "xID"  # (e.g., 5ID=five times per day; 8ID=8 times per day)
    )
    """X times per day at institution-specified times, where X is a numeral 5 or greater."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RepeatPattern.ANTE: "Ante (before)",
    RepeatPattern.TWICE_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES: "twice a day at institution-specified times",
    RepeatPattern.SERVICE_IS_PROVIDED_CONTINUOUSLY_BETWEEN_START_TIME_AND_STOP_TIME: "service is provided continuously between start time and stop time",
    RepeatPattern.CIBUS_DIURNUS: "Cibus Diurnus (lunch)",
    RepeatPattern.INTER: "Inter",
    RepeatPattern.CIBUS_MATUTINUS: "Cibus Matutinus (breakfast)",
    RepeatPattern.BELOW_TIMING_ABOVE_C: "&lt;timing&gt;C (cum)&lt;meal&gt;",
    RepeatPattern.ONE_TIME_ONLY: "one time only.",
    RepeatPattern.POST: "Post (after)",
    RepeatPattern.GIVEN_AS_NEEDED: "given as needed",
    RepeatPattern.WHERE_XXX_IS_SOME_FREQUENCY_CODE: "where xxx is some frequency code",
    RepeatPattern.EVERY_BELOW_INTEGER_ABOVE_DAYS: "every &lt;integer&gt; days",
    RepeatPattern.EVERY_BELOW_INTEGER_ABOVE_HOURS: "every &lt;integer&gt; hours",
    RepeatPattern.REPEATS_ON_A_PARTICULAR_DAY_OF_THE_WEEK: "repeats on a particular day of the week,",
    RepeatPattern.EVERY_BELOW_INTEGER_ABOVE_MONTHS: "every &lt;integer&gt; months (Lunar cycle)",
    RepeatPattern.EVERY_BELOW_INTEGER_ABOVE_MINUTES: "every &lt;integer&gt; minutes",
    RepeatPattern.EVERY_BELOW_INTEGER_ABOVE_SECONDS: "every &lt;integer&gt; seconds",
    RepeatPattern.EVERY_BELOW_INTEGER_ABOVE_WEEKS: "every &lt;integer&gt; weeks",
    RepeatPattern.IN_THE_MORNING_AT_INSTITUTION_SPECIFIED_TIME: "in the morning at institution-specified time",
    RepeatPattern.EVERY_DAY_BEFORE_THE_HOUR_OF_SLEEP: "every day before the hour of sleep",
    RepeatPattern.FOUR_TIMES_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES: "four times a day at institution-specified times",
    RepeatPattern.EVERY_OTHER_DAY: "every other day",
    RepeatPattern.IN_THE_EVENING_AT_INSTITUTION_SPECIFIED_TIME: "in the evening at institution-specified time",
    RepeatPattern.DURING_EACH_OF_THREE_EIGHT_HOUR_SHIFTS_AT_INSTITUTION_SPECIFIED_TIMES: "during each of three eight-hour shifts at institution-specified times",
    RepeatPattern.THREE_TIMES_A_DAY_AT_INSTITUTION_SPECIFIED_TIMES: "three times a day at institution-specified times",
    RepeatPattern.FOR_FUTURE_USE_WHERE_BELOW_SPEC_ABOVE_IS_AN_INTERVAL_SPECIFICATION_AS_DEFINED_BY_THE_UNIX_CRON_SPECIFICATION: "for future use, where &lt;spec&gt; is an interval specification as defined by the UNIX cron specification.",
    RepeatPattern.CIBUS_VESPERTINUS: "Cibus Vespertinus (dinner)",
    RepeatPattern.X_TIMES_PER_DAY_AT_INSTITUTION_SPECIFIED_TIMES_WHERE_X_IS_A_NUMERAL_5_OR_GREATER: "X times per day at institution-specified times, where X is a numeral 5 or greater.",
}
