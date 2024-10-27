from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event related period - 0528
Table Type: HL7
"""


class EventRelatedPeriod(HL7Table):
    """
    Event related period - 0528 // HL7 table type
    - BEFORE_MEAL
    - BEFORE_LUNCH
    - BEFORE_BREAKFAST
    - BEFORE_DINNER
    - THE_HOUR_OF_SLEEP
    - BETWEEN_MEALS
    - BETWEEN_LUNCH_AND_DINNER
    - BETWEEN_BREAKFAST_AND_LUNCH
    - BETWEEN_DINNER_AND_THE_HOUR_OF_SLEEP
    - AFTER_MEAL
    - AFTER_LUNCH
    - AFTER_BREAKFAST
    - AFTER_DINNER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0528
    """

    BEFORE_MEAL = "AC"
    """before meal (from lat. ante cibus)"""
    BEFORE_LUNCH = "ACD"
    """before lunch (from lat. ante cibus diurnus)"""
    BEFORE_BREAKFAST = "ACM"
    """before breakfast (from lat. ante cibus matutinus)"""
    BEFORE_DINNER = "ACV"
    """before dinner (from lat. ante cibus vespertinus)"""
    THE_HOUR_OF_SLEEP = "HS"
    """the hour of sleep (e.g., H18-22)"""
    BETWEEN_MEALS = "IC"
    """between meals (from lat. inter cibus)"""
    BETWEEN_LUNCH_AND_DINNER = "ICD"
    """between lunch and dinner"""
    BETWEEN_BREAKFAST_AND_LUNCH = "ICM"
    """between breakfast and lunch"""
    BETWEEN_DINNER_AND_THE_HOUR_OF_SLEEP = "ICV"
    """between dinner and the hour of sleep"""
    AFTER_MEAL = "PC"
    """after meal (from lat. post cibus)"""
    AFTER_LUNCH = "PCD"
    """after lunch (from lat. post cibus diurnus)"""
    AFTER_BREAKFAST = "PCM"
    """after breakfast (from lat. post cibus matutinus)"""
    AFTER_DINNER = "PCV"
    """after dinner (from lat. post cibus vespertinus)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventRelatedPeriod.BEFORE_MEAL: "before meal (from lat. ante cibus)",
    EventRelatedPeriod.BEFORE_LUNCH: "before lunch (from lat. ante cibus diurnus)",
    EventRelatedPeriod.BEFORE_BREAKFAST: "before breakfast (from lat. ante cibus matutinus)",
    EventRelatedPeriod.BEFORE_DINNER: "before dinner (from lat. ante cibus vespertinus)",
    EventRelatedPeriod.THE_HOUR_OF_SLEEP: "the hour of sleep (e.g., H18-22)",
    EventRelatedPeriod.BETWEEN_MEALS: "between meals (from lat. inter cibus)",
    EventRelatedPeriod.BETWEEN_LUNCH_AND_DINNER: "between lunch and dinner",
    EventRelatedPeriod.BETWEEN_BREAKFAST_AND_LUNCH: "between breakfast and lunch",
    EventRelatedPeriod.BETWEEN_DINNER_AND_THE_HOUR_OF_SLEEP: "between dinner and the hour of sleep",
    EventRelatedPeriod.AFTER_MEAL: "after meal (from lat. post cibus)",
    EventRelatedPeriod.AFTER_LUNCH: "after lunch (from lat. post cibus diurnus)",
    EventRelatedPeriod.AFTER_BREAKFAST: "after breakfast (from lat. post cibus matutinus)",
    EventRelatedPeriod.AFTER_DINNER: "after dinner (from lat. post cibus vespertinus)",
}
