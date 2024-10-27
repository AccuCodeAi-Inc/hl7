from ...base import HL7Table

"""
HL7 Version: 2.5.1
Priority - 0027
Table Type: HL7
"""


class Priority(HL7Table):
    """
    Priority - 0027 // HL7 table type
    - AS_SOON_AS_POSSIBLE
    - PREOPERATIVE
    - ROUTINE
    - STAT
    - TIMING_CRITICAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0027
    """

    AS_SOON_AS_POSSIBLE = "A"
    """As soon as possible (a priority lower than stat)"""
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
    Priority.AS_SOON_AS_POSSIBLE: "As soon as possible (a priority lower than stat)",
    Priority.PREOPERATIVE: "Preoperative (to be done prior to surgery)",
    Priority.ROUTINE: "Routine",
    Priority.STAT: "Stat (do immediately)",
    Priority.TIMING_CRITICAL: "Timing critical (do as near as possible to requested time)",
}
