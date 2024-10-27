from ...base import HL7Table

"""
HL7 Version: 2.5.1
File level event code - 0178
Table Type: HL7
"""


class FileLevelEventCode(HL7Table):
    """
    File level event code - 0178 // HL7 table type
    - REPLACE_CURRENT_VERSION_OF_THIS_MASTER_FILE_WITH_THE_VERSION_CONTAINED_IN_THIS_MESSAGE
    - CHANGE_FILE_RECORDS_AS_DEFINED_IN_THE_RECORD_LEVEL_EVENT_CODES_FOR_EACH_RECORD_THAT_FOLLOWS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0178
    """

    REPLACE_CURRENT_VERSION_OF_THIS_MASTER_FILE_WITH_THE_VERSION_CONTAINED_IN_THIS_MESSAGE = "REP"
    """Replace current version of this master file with the version contained in this message"""
    CHANGE_FILE_RECORDS_AS_DEFINED_IN_THE_RECORD_LEVEL_EVENT_CODES_FOR_EACH_RECORD_THAT_FOLLOWS = "UPD"
    """Change file records as defined in the record-level event codes for each record that follows"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    FileLevelEventCode.REPLACE_CURRENT_VERSION_OF_THIS_MASTER_FILE_WITH_THE_VERSION_CONTAINED_IN_THIS_MESSAGE: "Replace current version of this master file with the version contained in this message",
    FileLevelEventCode.CHANGE_FILE_RECORDS_AS_DEFINED_IN_THE_RECORD_LEVEL_EVENT_CODES_FOR_EACH_RECORD_THAT_FOLLOWS: "Change file records as defined in the record-level event codes for each record that follows",
}
