from ...base import HL7Table

"""
HL7 Version: 2.5.1
Record-level event code - 0180
Table Type: HL7
"""


class RecordLevelEventCode(HL7Table):
    """
    Record-level event code - 0180 // HL7 table type
    - REACTIVATE_DEACTIVATED_RECORD
    - ADD_RECORD_TO_MASTER_FILE
    - DEACTIVATE_DISCONTINUE_USING_RECORD_IN_MASTER_FILE_BUT_DO_NOT_DELETE_FROM_DATABASE
    - DELETE_RECORD_FROM_MASTER_FILE
    - UPDATE_RECORD_FOR_MASTER_FILE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0180
    """

    REACTIVATE_DEACTIVATED_RECORD = "MAC"
    """Reactivate deactivated record"""
    ADD_RECORD_TO_MASTER_FILE = "MAD"
    """Add record to master file"""
    DEACTIVATE_DISCONTINUE_USING_RECORD_IN_MASTER_FILE_BUT_DO_NOT_DELETE_FROM_DATABASE = "MDC"
    """Deactivate: discontinue using record in master file, but do not delete from database"""
    DELETE_RECORD_FROM_MASTER_FILE = "MDL"
    """Delete record from master file"""
    UPDATE_RECORD_FOR_MASTER_FILE = "MUP"
    """Update record for master file"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RecordLevelEventCode.REACTIVATE_DEACTIVATED_RECORD: "Reactivate deactivated record",
    RecordLevelEventCode.ADD_RECORD_TO_MASTER_FILE: "Add record to master file",
    RecordLevelEventCode.DEACTIVATE_DISCONTINUE_USING_RECORD_IN_MASTER_FILE_BUT_DO_NOT_DELETE_FROM_DATABASE: "Deactivate: discontinue using record in master file, but do not delete from database",
    RecordLevelEventCode.DELETE_RECORD_FROM_MASTER_FILE: "Delete record from master file",
    RecordLevelEventCode.UPDATE_RECORD_FOR_MASTER_FILE: "Update record for master file",
}
