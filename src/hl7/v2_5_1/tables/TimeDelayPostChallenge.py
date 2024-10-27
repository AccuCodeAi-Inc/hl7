from ...base import HL7Table

"""
HL7 Version: 2.5.1
Time delay post challenge - 0256
Table Type: HL7
"""


class TimeDelayPostChallenge(HL7Table):
    """
    Time delay post challenge - 0256 // HL7 table type
    - _10_DAYS
    - _10_MINUTES_POST_CHALLENGE
    - _12_HOURS_POST_CHALLENGE
    - _15_MINUTES_POST_CHALLENGE
    - _1_HOUR_POST_CHALLENGE
    - _1_MONTH
    - _1_MINUTE_POST_CHALLENGE
    - _1_WEEK
    - _2_1_OR_2_HOURS_POST_CHALLENGE
    - _20_MINUTES_POST_CHALLENGE
    - _24_HOURS_POST_CHALLENGE
    - _25_MINUTES_POST_CHALLENGE
    - _2_DAYS
    - _2_HOURS_POST_CHALLENGE
    - _2_MONTHS
    - _2_MINUTES_POST_CHALLENGE
    - _2_WEEKS
    - _30_MINUTES_POST_CHALLENGE
    - _3_DAYS
    - _3_HOURS_POST_CHALLENGE
    - _3_MONTHS
    - _3_MINUTES_POST_CHALLENGE
    - _3_WEEKS
    - _4_DAYS
    - _4_HOURS_POST_CHALLENGE
    - _4_MINUTES_POST_CHALLENGE
    - _4_WEEKS
    - _5_DAYS
    - _5_HOURS_POST_CHALLENGE
    - _5_MINUTES_POST_CHALLENGE
    - _6_DAYS
    - _6_HOURS_POST_CHALLENGE
    - _6_MINUTES_POST_CHALLENGE
    - _7_DAYS
    - _7_HOURS_POST_CHALLENGE
    - _7_MINUTES_POST_CHALLENGE
    - _8_HOURS_POST_CHALLENGE
    - _8_HOURS_ALIGNED_ON_NURSING_SHIFTS
    - _8_MINUTES_POST_CHALLENGE
    - _9_MINUTES_POST_CHALLENGE
    - BASELINE
    - THE_TIME_POST_DRUG_DOSE_AT_WHICH_THE_HIGHEST_DRUG_LEVEL_IS_REACHED
    - TIME_FROM_THE_CHALLENGE_OR_DOSE_NOT_SPECIFIED
    - THE_TIME_POST_DRUG_DOSE_AT_WHICH_THE_LOWEST_DRUG_LEVEL_IS_REACHED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0256
    """

    _10_DAYS = "10D"
    """10 days"""
    _10_MINUTES_POST_CHALLENGE = "10M"
    """10 minutes post challenge"""
    _12_HOURS_POST_CHALLENGE = "12H"
    """12 hours post challenge"""
    _15_MINUTES_POST_CHALLENGE = "15M"
    """15 minutes post challenge"""
    _1_HOUR_POST_CHALLENGE = "1H"
    """1 hour post challenge"""
    _1_MONTH = "1L"
    """1 month (30 days) post challenge"""
    _1_MINUTE_POST_CHALLENGE = "1M"
    """1 minute post challenge"""
    _1_WEEK = "1W"
    """1 week"""
    _2_1_OR_2_HOURS_POST_CHALLENGE = "2.5H"
    """2 1/2 hours post challenge"""
    _20_MINUTES_POST_CHALLENGE = "20M"
    """20 minutes post challenge"""
    _24_HOURS_POST_CHALLENGE = "24H"
    """24 hours post challenge"""
    _25_MINUTES_POST_CHALLENGE = "25M"
    """25 minutes post challenge"""
    _2_DAYS = "2D"
    """2 days"""
    _2_HOURS_POST_CHALLENGE = "2H"
    """2 hours post challenge"""
    _2_MONTHS = "2L"
    """2 months (60 days) post challenge"""
    _2_MINUTES_POST_CHALLENGE = "2M"
    """2 minutes post challenge"""
    _2_WEEKS = "2W"
    """2 weeks"""
    _30_MINUTES_POST_CHALLENGE = "30M"
    """30 minutes post challenge"""
    _3_DAYS = "3D"
    """3 days"""
    _3_HOURS_POST_CHALLENGE = "3H"
    """3 hours post challenge"""
    _3_MONTHS = "3L"
    """3 months (90 days) post challenge"""
    _3_MINUTES_POST_CHALLENGE = "3M"
    """3 minutes post challenge"""
    _3_WEEKS = "3W"
    """3 weeks"""
    _4_DAYS = "4D"
    """4 days"""
    _4_HOURS_POST_CHALLENGE = "4H"
    """4 hours post challenge"""
    _4_MINUTES_POST_CHALLENGE = "4M"
    """4 minutes post challenge"""
    _4_WEEKS = "4W"
    """4 weeks"""
    _5_DAYS = "5D"
    """5 days"""
    _5_HOURS_POST_CHALLENGE = "5H"
    """5 hours post challenge"""
    _5_MINUTES_POST_CHALLENGE = "5M"
    """5 minutes post challenge"""
    _6_DAYS = "6D"
    """6 days"""
    _6_HOURS_POST_CHALLENGE = "6H"
    """6 hours post challenge"""
    _6_MINUTES_POST_CHALLENGE = "6M"
    """6 minutes post challenge"""
    _7_DAYS = "7D"
    """7 days"""
    _7_HOURS_POST_CHALLENGE = "7H"
    """7 hours post challenge"""
    _7_MINUTES_POST_CHALLENGE = "7M"
    """7 minutes post challenge"""
    _8_HOURS_POST_CHALLENGE = "8H"
    """8 hours post challenge"""
    _8_HOURS_ALIGNED_ON_NURSING_SHIFTS = "8H SHIFT"
    """8 hours aligned on nursing shifts"""
    _8_MINUTES_POST_CHALLENGE = "8M"
    """8 minutes post challenge"""
    _9_MINUTES_POST_CHALLENGE = "9M"
    """9 minutes post challenge"""
    BASELINE = "BS"
    """Baseline (time just before the challenge)"""
    THE_TIME_POST_DRUG_DOSE_AT_WHICH_THE_HIGHEST_DRUG_LEVEL_IS_REACHED = "PEAK"
    """The time post drug dose at which the highest drug level is reached (differs by drug)"""
    TIME_FROM_THE_CHALLENGE_OR_DOSE_NOT_SPECIFIED = "RANDOM"
    """Time from the challenge, or dose not specified. (random)"""
    THE_TIME_POST_DRUG_DOSE_AT_WHICH_THE_LOWEST_DRUG_LEVEL_IS_REACHED = "TROUGH"
    """The time post drug dose at which the lowest drug level is reached (varies with drug)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TimeDelayPostChallenge._10_DAYS: "10 days",
    TimeDelayPostChallenge._10_MINUTES_POST_CHALLENGE: "10 minutes post challenge",
    TimeDelayPostChallenge._12_HOURS_POST_CHALLENGE: "12 hours post challenge",
    TimeDelayPostChallenge._15_MINUTES_POST_CHALLENGE: "15 minutes post challenge",
    TimeDelayPostChallenge._1_HOUR_POST_CHALLENGE: "1 hour post challenge",
    TimeDelayPostChallenge._1_MONTH: "1 month (30 days) post challenge",
    TimeDelayPostChallenge._1_MINUTE_POST_CHALLENGE: "1 minute post challenge",
    TimeDelayPostChallenge._1_WEEK: "1 week",
    TimeDelayPostChallenge._2_1_OR_2_HOURS_POST_CHALLENGE: "2 1/2 hours post challenge",
    TimeDelayPostChallenge._20_MINUTES_POST_CHALLENGE: "20 minutes post challenge",
    TimeDelayPostChallenge._24_HOURS_POST_CHALLENGE: "24 hours post challenge",
    TimeDelayPostChallenge._25_MINUTES_POST_CHALLENGE: "25 minutes post challenge",
    TimeDelayPostChallenge._2_DAYS: "2 days",
    TimeDelayPostChallenge._2_HOURS_POST_CHALLENGE: "2 hours post challenge",
    TimeDelayPostChallenge._2_MONTHS: "2 months (60 days) post challenge",
    TimeDelayPostChallenge._2_MINUTES_POST_CHALLENGE: "2 minutes post challenge",
    TimeDelayPostChallenge._2_WEEKS: "2 weeks",
    TimeDelayPostChallenge._30_MINUTES_POST_CHALLENGE: "30 minutes post challenge",
    TimeDelayPostChallenge._3_DAYS: "3 days",
    TimeDelayPostChallenge._3_HOURS_POST_CHALLENGE: "3 hours post challenge",
    TimeDelayPostChallenge._3_MONTHS: "3 months (90 days) post challenge",
    TimeDelayPostChallenge._3_MINUTES_POST_CHALLENGE: "3 minutes post challenge",
    TimeDelayPostChallenge._3_WEEKS: "3 weeks",
    TimeDelayPostChallenge._4_DAYS: "4 days",
    TimeDelayPostChallenge._4_HOURS_POST_CHALLENGE: "4 hours post challenge",
    TimeDelayPostChallenge._4_MINUTES_POST_CHALLENGE: "4 minutes post challenge",
    TimeDelayPostChallenge._4_WEEKS: "4 weeks",
    TimeDelayPostChallenge._5_DAYS: "5 days",
    TimeDelayPostChallenge._5_HOURS_POST_CHALLENGE: "5 hours post challenge",
    TimeDelayPostChallenge._5_MINUTES_POST_CHALLENGE: "5 minutes post challenge",
    TimeDelayPostChallenge._6_DAYS: "6 days",
    TimeDelayPostChallenge._6_HOURS_POST_CHALLENGE: "6 hours post challenge",
    TimeDelayPostChallenge._6_MINUTES_POST_CHALLENGE: "6 minutes post challenge",
    TimeDelayPostChallenge._7_DAYS: "7 days",
    TimeDelayPostChallenge._7_HOURS_POST_CHALLENGE: "7 hours post challenge",
    TimeDelayPostChallenge._7_MINUTES_POST_CHALLENGE: "7 minutes post challenge",
    TimeDelayPostChallenge._8_HOURS_POST_CHALLENGE: "8 hours post challenge",
    TimeDelayPostChallenge._8_HOURS_ALIGNED_ON_NURSING_SHIFTS: "8 hours aligned on nursing shifts",
    TimeDelayPostChallenge._8_MINUTES_POST_CHALLENGE: "8 minutes post challenge",
    TimeDelayPostChallenge._9_MINUTES_POST_CHALLENGE: "9 minutes post challenge",
    TimeDelayPostChallenge.BASELINE: "Baseline (time just before the challenge)",
    TimeDelayPostChallenge.THE_TIME_POST_DRUG_DOSE_AT_WHICH_THE_HIGHEST_DRUG_LEVEL_IS_REACHED: "The time post drug dose at which the highest drug level is reached (differs by drug)",
    TimeDelayPostChallenge.TIME_FROM_THE_CHALLENGE_OR_DOSE_NOT_SPECIFIED: "Time from the challenge, or dose not specified. (random)",
    TimeDelayPostChallenge.THE_TIME_POST_DRUG_DOSE_AT_WHICH_THE_LOWEST_DRUG_LEVEL_IS_REACHED: "The time post drug dose at which the lowest drug level is reached (varies with drug)",
}
