from ...base import HL7Table

"""
HL7 Version: 2.5.1
Abnormal flags - 0078
Table Type: User
"""


class AbnormalFlags(HL7Table):
    """
    Abnormal flags - 0078 // User table type
    - BELOW_ABSOLUTE_LOW_OFF_INSTRUMENT_SCALE
    - ABOVE_ABSOLUTE_HIGH_OFF_INSTRUMENT_SCALE
    - ABNORMAL
    - VERY_ABNORMAL
    - BETTER_USE_WHEN_DIRECTION_NOT_RELEVANT
    - SIGNIFICANT_CHANGE_DOWN
    - ABOVE_HIGH_NORMAL
    - ABOVE_UPPER_PANIC_LIMITS
    - INTERMEDIATE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY
    - BELOW_LOW_NORMAL
    - BELOW_LOWER_PANIC_LIMITS
    - MODERATELY_SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY
    - NORMAL
    - NO_RANGE_DEFINED_OR_NORMAL_RANGES_DONT_APPLY
    - RESISTANT_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY
    - SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY
    - SIGNIFICANT_CHANGE_UP
    - VERY_SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY
    - WORSE_USE_WHEN_DIRECTION_NOT_RELEVANT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0078
    """

    BELOW_ABSOLUTE_LOW_OFF_INSTRUMENT_SCALE = "<"
    """Below absolute low-off instrument scale"""
    ABOVE_ABSOLUTE_HIGH_OFF_INSTRUMENT_SCALE = ">"
    """Above absolute high-off instrument scale"""
    ABNORMAL = "A"
    """Abnormal (applies to non-numeric results)"""
    VERY_ABNORMAL = "AA"
    """Very abnormal (applies to non-numeric units, analogous to panic limits for numeric units)"""
    BETTER_USE_WHEN_DIRECTION_NOT_RELEVANT = "B"
    """Better--use when direction not relevant"""
    SIGNIFICANT_CHANGE_DOWN = "D"
    """Significant change down"""
    ABOVE_HIGH_NORMAL = "H"
    """Above high normal"""
    ABOVE_UPPER_PANIC_LIMITS = "HH"
    """Above upper panic limits"""
    INTERMEDIATE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY = "I"
    """Intermediate. Indicates for microbiology susceptibilities only."""
    BELOW_LOW_NORMAL = "L"
    """Below low normal"""
    BELOW_LOWER_PANIC_LIMITS = "LL"
    """Below lower panic limits"""
    MODERATELY_SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY = "MS"
    """Moderately susceptible. Indicates for microbiology susceptibilities only."""
    NORMAL = "N"
    """Normal (applies to non-numeric results)"""
    NO_RANGE_DEFINED_OR_NORMAL_RANGES_DONT_APPLY = "null"
    """No range defined, or normal ranges dont apply"""
    RESISTANT_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY = "R"
    """Resistant. Indicates for microbiology susceptibilities only."""
    SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY = "S"
    """Susceptible. Indicates for microbiology susceptibilities only."""
    SIGNIFICANT_CHANGE_UP = "U"
    """Significant change up"""
    VERY_SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY = "VS"
    """Very susceptible. Indicates for microbiology susceptibilities only."""
    WORSE_USE_WHEN_DIRECTION_NOT_RELEVANT = "W"
    """Worse--use when direction not relevant"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AbnormalFlags.BELOW_ABSOLUTE_LOW_OFF_INSTRUMENT_SCALE: "Below absolute low-off instrument scale",
    AbnormalFlags.ABOVE_ABSOLUTE_HIGH_OFF_INSTRUMENT_SCALE: "Above absolute high-off instrument scale",
    AbnormalFlags.ABNORMAL: "Abnormal (applies to non-numeric results)",
    AbnormalFlags.VERY_ABNORMAL: "Very abnormal (applies to non-numeric units, analogous to panic limits for numeric units)",
    AbnormalFlags.BETTER_USE_WHEN_DIRECTION_NOT_RELEVANT: "Better--use when direction not relevant",
    AbnormalFlags.SIGNIFICANT_CHANGE_DOWN: "Significant change down",
    AbnormalFlags.ABOVE_HIGH_NORMAL: "Above high normal",
    AbnormalFlags.ABOVE_UPPER_PANIC_LIMITS: "Above upper panic limits",
    AbnormalFlags.INTERMEDIATE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY: "Intermediate. Indicates for microbiology susceptibilities only.",
    AbnormalFlags.BELOW_LOW_NORMAL: "Below low normal",
    AbnormalFlags.BELOW_LOWER_PANIC_LIMITS: "Below lower panic limits",
    AbnormalFlags.MODERATELY_SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY: "Moderately susceptible. Indicates for microbiology susceptibilities only.",
    AbnormalFlags.NORMAL: "Normal (applies to non-numeric results)",
    AbnormalFlags.NO_RANGE_DEFINED_OR_NORMAL_RANGES_DONT_APPLY: "No range defined, or normal ranges dont apply",
    AbnormalFlags.RESISTANT_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY: "Resistant. Indicates for microbiology susceptibilities only.",
    AbnormalFlags.SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY: "Susceptible. Indicates for microbiology susceptibilities only.",
    AbnormalFlags.SIGNIFICANT_CHANGE_UP: "Significant change up",
    AbnormalFlags.VERY_SUSCEPTIBLE_INDICATES_FOR_MICROBIOLOGY_SUSCEPTIBILITIES_ONLY: "Very susceptible. Indicates for microbiology susceptibilities only.",
    AbnormalFlags.WORSE_USE_WHEN_DIRECTION_NOT_RELEVANT: "Worse--use when direction not relevant",
}
