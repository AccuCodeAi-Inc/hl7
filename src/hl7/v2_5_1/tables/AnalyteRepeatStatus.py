from ...base import HL7Table

"""
HL7 Version: 2.5.1
Analyte repeat status - 0389
Table Type: HL7
"""


class AnalyteRepeatStatus(HL7Table):
    """
    Analyte repeat status - 0389 // HL7 table type
    - REPEATED_WITH_DILUTION
    - REFLEX_TEST
    - ORIGINAL_FIRST_RUN
    - REPEATED_WITHOUT_DILUTION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0389
    """

    REPEATED_WITH_DILUTION = "D"
    """Repeated with dilution"""
    REFLEX_TEST = "F"
    """Reflex test"""
    ORIGINAL_FIRST_RUN = "O"
    """Original, first run"""
    REPEATED_WITHOUT_DILUTION = "R"
    """Repeated without dilution"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AnalyteRepeatStatus.REPEATED_WITH_DILUTION: "Repeated with dilution",
    AnalyteRepeatStatus.REFLEX_TEST: "Reflex test",
    AnalyteRepeatStatus.ORIGINAL_FIRST_RUN: "Original, first run",
    AnalyteRepeatStatus.REPEATED_WITHOUT_DILUTION: "Repeated without dilution",
}
