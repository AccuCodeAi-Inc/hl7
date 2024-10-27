from ...base import HL7Table

"""
HL7 Version: 2.5.1
Processing priority - 0168
Table Type: HL7
"""


class ProcessingPriority(HL7Table):
    """
    Processing priority - 0168 // HL7 table type
    - AS_SOON_AS_POSSIBLE
    - DO_AT_BEDSIDE_OR_PORTABLE
    - MEASURE_CONTINUOUSLY
    - PREOPERATIVE
    - ROUTINE
    - STAT
    - TIMING_CRITICAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0168
    """

    AS_SOON_AS_POSSIBLE = "A"
    """As soon as possible (a priority lower than stat)"""
    DO_AT_BEDSIDE_OR_PORTABLE = "B"
    """Do at bedside or portable (may be used with other codes)"""
    MEASURE_CONTINUOUSLY = "C"
    """Measure continuously (e.g., arterial line blood pressure)"""
    PREOPERATIVE = "P"
    """Preoperative (to be done prior to surgery)"""
    ROUTINE = "R"
    """Routine"""
    STAT = "S"
    """Stat (do immediately)"""
    TIMING_CRITICAL = "T"
    """Timing critical (do as near as possible to requested time)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcessingPriority.AS_SOON_AS_POSSIBLE: "As soon as possible (a priority lower than stat)",
    ProcessingPriority.DO_AT_BEDSIDE_OR_PORTABLE: "Do at bedside or portable (may be used with other codes)",
    ProcessingPriority.MEASURE_CONTINUOUSLY: "Measure continuously (e.g., arterial line blood pressure)",
    ProcessingPriority.PREOPERATIVE: "Preoperative (to be done prior to surgery)",
    ProcessingPriority.ROUTINE: "Routine",
    ProcessingPriority.STAT: "Stat (do immediately)",
    ProcessingPriority.TIMING_CRITICAL: "Timing critical (do as near as possible to requested time)",
}
