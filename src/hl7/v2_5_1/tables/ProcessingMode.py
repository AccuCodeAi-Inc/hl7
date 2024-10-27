from ...base import HL7Table

"""
HL7 Version: 2.5.1
Processing mode - 0207
Table Type: HL7
"""


class ProcessingMode(HL7Table):
    """
    Processing mode - 0207 // HL7 table type
    - ARCHIVE
    - INITIAL_LOAD
    - NOT_PRESENT
    - RESTORE_FROM_ARCHIVE
    - CURRENT_PROCESSING_TRANSMITTED_AT_INTERVALS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0207
    """

    ARCHIVE = "A"
    """Archive"""
    INITIAL_LOAD = "I"
    """Initial load"""
    NOT_PRESENT = "Not present"
    """Not present (the default, meaning current processing)"""
    RESTORE_FROM_ARCHIVE = "R"
    """Restore from archive"""
    CURRENT_PROCESSING_TRANSMITTED_AT_INTERVALS = "T"
    """Current processing, transmitted at intervals (scheduled or on demand)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcessingMode.ARCHIVE: "Archive",
    ProcessingMode.INITIAL_LOAD: "Initial load",
    ProcessingMode.NOT_PRESENT: "Not present (the default, meaning current processing)",
    ProcessingMode.RESTORE_FROM_ARCHIVE: "Restore from archive",
    ProcessingMode.CURRENT_PROCESSING_TRANSMITTED_AT_INTERVALS: "Current processing, transmitted at intervals (scheduled or on demand)",
}
