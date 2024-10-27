from ...base import HL7Table

"""
HL7 Version: 2.5.1
Marital Status - 0002
Table Type: User
"""


class MaritalStatus(HL7Table):
    """
    Marital Status - 0002 // User table type
    - SEPARATED
    - UNMARRIED
    - COMMON_LAW
    - DIVORCED
    - LEGALLY_SEPARATED
    - LIVING_TOGETHER
    - INTERLOCUTORY
    - MARRIED
    - ANNULLED
    - OTHER
    - DOMESTIC_PARTNER
    - REGISTERED_DOMESTIC_PARTNER
    - SINGLE
    - UNREPORTED
    - UNKNOWN
    - WIDOWED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0002
    """

    SEPARATED = "A"
    """Separated"""
    UNMARRIED = "B"
    """Unmarried"""
    COMMON_LAW = "C"
    """Common law"""
    DIVORCED = "D"
    """Divorced"""
    LEGALLY_SEPARATED = "E"
    """Legally Separated"""
    LIVING_TOGETHER = "G"
    """Living together"""
    INTERLOCUTORY = "I"
    """Interlocutory"""
    MARRIED = "M"
    """Married"""
    ANNULLED = "N"
    """Annulled"""
    OTHER = "O"
    """Other"""
    DOMESTIC_PARTNER = "P"
    """Domestic partner"""
    REGISTERED_DOMESTIC_PARTNER = "R"
    """Registered domestic partner"""
    SINGLE = "S"
    """Single"""
    UNREPORTED = "T"
    """Unreported"""
    UNKNOWN = "U"
    """Unknown"""
    WIDOWED = "W"
    """Widowed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MaritalStatus.SEPARATED: "Separated",
    MaritalStatus.UNMARRIED: "Unmarried",
    MaritalStatus.COMMON_LAW: "Common law",
    MaritalStatus.DIVORCED: "Divorced",
    MaritalStatus.LEGALLY_SEPARATED: "Legally Separated",
    MaritalStatus.LIVING_TOGETHER: "Living together",
    MaritalStatus.INTERLOCUTORY: "Interlocutory",
    MaritalStatus.MARRIED: "Married",
    MaritalStatus.ANNULLED: "Annulled",
    MaritalStatus.OTHER: "Other",
    MaritalStatus.DOMESTIC_PARTNER: "Domestic partner",
    MaritalStatus.REGISTERED_DOMESTIC_PARTNER: "Registered domestic partner",
    MaritalStatus.SINGLE: "Single",
    MaritalStatus.UNREPORTED: "Unreported",
    MaritalStatus.UNKNOWN: "Unknown",
    MaritalStatus.WIDOWED: "Widowed",
}
