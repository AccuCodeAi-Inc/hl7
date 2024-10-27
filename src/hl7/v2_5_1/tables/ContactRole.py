from ...base import HL7Table

"""
HL7 Version: 2.5.1
Contact Role - 0131
Table Type: User
"""


class ContactRole(HL7Table):
    """
    Contact Role - 0131 // User table type
    - EMERGENCY_CONTACT
    - EMPLOYER
    - FEDERAL_AGENCY
    - INSURANCE_COMPANY
    - NEXT_OF_KIN
    - OTHER
    - STATE_AGENCY
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0131
    """

    EMERGENCY_CONTACT = "C"
    """Emergency Contact"""
    EMPLOYER = "E"
    """Employer"""
    FEDERAL_AGENCY = "F"
    """Federal Agency"""
    INSURANCE_COMPANY = "I"
    """Insurance Company"""
    NEXT_OF_KIN = "N"
    """Next-of-Kin"""
    OTHER = "O"
    """Other"""
    STATE_AGENCY = "S"
    """State Agency"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ContactRole.EMERGENCY_CONTACT: "Emergency Contact",
    ContactRole.EMPLOYER: "Employer",
    ContactRole.FEDERAL_AGENCY: "Federal Agency",
    ContactRole.INSURANCE_COMPANY: "Insurance Company",
    ContactRole.NEXT_OF_KIN: "Next-of-Kin",
    ContactRole.OTHER: "Other",
    ContactRole.STATE_AGENCY: "State Agency",
    ContactRole.UNKNOWN: "Unknown",
}
