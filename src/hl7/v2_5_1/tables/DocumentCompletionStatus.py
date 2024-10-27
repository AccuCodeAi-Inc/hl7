from ...base import HL7Table

"""
HL7 Version: 2.5.1
Document completion status - 0271
Table Type: HL7
"""


class DocumentCompletionStatus(HL7Table):
    """
    Document completion status - 0271 // HL7 table type
    - AUTHENTICATED
    - DICTATED
    - DOCUMENTED
    - INCOMPLETE
    - IN_PROGRESS
    - LEGALLY_AUTHENTICATED
    - PRE_AUTHENTICATED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0271
    """

    AUTHENTICATED = "AU"
    """Authenticated"""
    DICTATED = "DI"
    """Dictated"""
    DOCUMENTED = "DO"
    """Documented"""
    INCOMPLETE = "IN"
    """Incomplete"""
    IN_PROGRESS = "IP"
    """In Progress"""
    LEGALLY_AUTHENTICATED = "LA"
    """Legally authenticated"""
    PRE_AUTHENTICATED = "PA"
    """Pre-authenticated"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DocumentCompletionStatus.AUTHENTICATED: "Authenticated",
    DocumentCompletionStatus.DICTATED: "Dictated",
    DocumentCompletionStatus.DOCUMENTED: "Documented",
    DocumentCompletionStatus.INCOMPLETE: "Incomplete",
    DocumentCompletionStatus.IN_PROGRESS: "In Progress",
    DocumentCompletionStatus.LEGALLY_AUTHENTICATED: "Legally authenticated",
    DocumentCompletionStatus.PRE_AUTHENTICATED: "Pre-authenticated",
}
