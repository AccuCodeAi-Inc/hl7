from ...base import HL7Table

"""
HL7 Version: 2.5.1
Document Storage Status - 0275
Table Type: HL7
"""


class DocumentStorageStatus(HL7Table):
    """
    Document Storage Status - 0275 // HL7 table type
    - ACTIVE_AND_ARCHIVED
    - ACTIVE
    - ARCHIVED
    - PURGED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0275
    """

    ACTIVE_AND_ARCHIVED = "AA"
    """Active and archived"""
    ACTIVE = "AC"
    """Active"""
    ARCHIVED = "AR"
    """Archived (not active)"""
    PURGED = "PU"
    """Purged"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DocumentStorageStatus.ACTIVE_AND_ARCHIVED: "Active and archived",
    DocumentStorageStatus.ACTIVE: "Active",
    DocumentStorageStatus.ARCHIVED: "Archived (not active)",
    DocumentStorageStatus.PURGED: "Purged",
}
