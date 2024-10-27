from ...base import HL7Table

"""
HL7 Version: 2.5.1
Purge Status Code - 0213
Table Type: User
"""


class PurgeStatusCode(HL7Table):
    """
    Purge Status Code - 0213 // User table type
    - THE_VISIT_IS_MARKED_FOR_DELETION_AND_THE_USER_CANNOT_ENTER_NEW_DATA_AGAINST_IT
    - THE_VISIT_IS_MARKED_INACTIVE_AND_THE_USER_CANNOT_ENTER_NEW_DATA_AGAINST_IT
    - MARKED_FOR_PURGE_USER_IS_NO_LONGER_ABLE_TO_UPDATE_THE_VISIT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0213
    """

    THE_VISIT_IS_MARKED_FOR_DELETION_AND_THE_USER_CANNOT_ENTER_NEW_DATA_AGAINST_IT = "D"
    """The visit is marked for deletion and the user cannot enter new data against it."""
    THE_VISIT_IS_MARKED_INACTIVE_AND_THE_USER_CANNOT_ENTER_NEW_DATA_AGAINST_IT = "I"
    """The visit is marked inactive and the user cannot enter new data against it."""
    MARKED_FOR_PURGE_USER_IS_NO_LONGER_ABLE_TO_UPDATE_THE_VISIT = "P"
    """Marked for purge. User is no longer able to update the visit."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PurgeStatusCode.THE_VISIT_IS_MARKED_FOR_DELETION_AND_THE_USER_CANNOT_ENTER_NEW_DATA_AGAINST_IT: "The visit is marked for deletion and the user cannot enter new data against it.",
    PurgeStatusCode.THE_VISIT_IS_MARKED_INACTIVE_AND_THE_USER_CANNOT_ENTER_NEW_DATA_AGAINST_IT: "The visit is marked inactive and the user cannot enter new data against it.",
    PurgeStatusCode.MARKED_FOR_PURGE_USER_IS_NO_LONGER_ABLE_TO_UPDATE_THE_VISIT: "Marked for purge. User is no longer able to update the visit.",
}
