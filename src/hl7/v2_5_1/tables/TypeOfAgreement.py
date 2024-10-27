from ...base import HL7Table

"""
HL7 Version: 2.5.1
Type of Agreement - 0098
Table Type: User
"""


class TypeOfAgreement(HL7Table):
    """
    Type of Agreement - 0098 // User table type
    - MATERNITY
    - STANDARD
    - UNIFIED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0098
    """

    MATERNITY = "M"
    """Maternity"""
    STANDARD = "S"
    """Standard"""
    UNIFIED = "U"
    """Unified"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TypeOfAgreement.MATERNITY: "Maternity",
    TypeOfAgreement.STANDARD: "Standard",
    TypeOfAgreement.UNIFIED: "Unified",
}
