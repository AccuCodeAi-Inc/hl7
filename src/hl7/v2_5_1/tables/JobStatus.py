from ...base import HL7Table

"""
HL7 Version: 2.5.1
Job Status - 0311
Table Type: User
"""


class JobStatus(HL7Table):
    """
    Job Status - 0311 // User table type
    - OTHER
    - PERMANENT
    - TEMPORARY
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0311
    """

    OTHER = "O"
    """Other"""
    PERMANENT = "P"
    """Permanent"""
    TEMPORARY = "T"
    """Temporary"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    JobStatus.OTHER: "Other",
    JobStatus.PERMANENT: "Permanent",
    JobStatus.TEMPORARY: "Temporary",
    JobStatus.UNKNOWN: "Unknown",
}
