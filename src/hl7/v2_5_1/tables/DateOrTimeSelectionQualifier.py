from ...base import HL7Table

"""
HL7 Version: 2.5.1
Date/time selection qualifier - 0158
Table Type: HL7
"""


class DateOrTimeSelectionQualifier(HL7Table):
    """
    Date/time selection qualifier - 0158 // HL7 table type
    - FIRST_VALUE_WITHIN_RANGE
    - ALL_VALUES_WITHIN_THE_RANGE
    - LAST_VALUE_WITHIN_THE_RANGE
    - ALL_VALUES_WITHIN_THE_RANGE_RETURNED_IN_REVERSE_CHRONOLOGICAL_ORDER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0158
    """

    FIRST_VALUE_WITHIN_RANGE = "1ST"
    """First value within range"""
    ALL_VALUES_WITHIN_THE_RANGE = "ALL"
    """All values within the range"""
    LAST_VALUE_WITHIN_THE_RANGE = "LST"
    """Last value within the range"""
    ALL_VALUES_WITHIN_THE_RANGE_RETURNED_IN_REVERSE_CHRONOLOGICAL_ORDER = "REV"
    """All values within the range returned in reverse chronological order (This is the default if not otherwise specified.)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DateOrTimeSelectionQualifier.FIRST_VALUE_WITHIN_RANGE: "First value within range",
    DateOrTimeSelectionQualifier.ALL_VALUES_WITHIN_THE_RANGE: "All values within the range",
    DateOrTimeSelectionQualifier.LAST_VALUE_WITHIN_THE_RANGE: "Last value within the range",
    DateOrTimeSelectionQualifier.ALL_VALUES_WITHIN_THE_RANGE_RETURNED_IN_REVERSE_CHRONOLOGICAL_ORDER: "All values within the range returned in reverse chronological order (This is the default if not otherwise specified.)",
}
