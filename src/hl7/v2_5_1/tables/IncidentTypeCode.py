from ...base import HL7Table

"""
HL7 Version: 2.5.1
Incident Type Code - 0428
Table Type: User
"""


class IncidentTypeCode(HL7Table):
    """
    Incident Type Code - 0428 // User table type
    - OTHER
    - PREVENTABLE
    - USER_ERROR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0428
    """

    OTHER = "O"
    """Other"""
    PREVENTABLE = "P"
    """Preventable"""
    USER_ERROR = "U"
    """User Error"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    IncidentTypeCode.OTHER: "Other",
    IncidentTypeCode.PREVENTABLE: "Preventable",
    IncidentTypeCode.USER_ERROR: "User Error",
}
