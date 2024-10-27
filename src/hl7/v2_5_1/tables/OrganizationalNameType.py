from ...base import HL7Table

"""
HL7 Version: 2.5.1
Organizational name type - 0204
Table Type: User
"""


class OrganizationalNameType(HL7Table):
    """
    Organizational name type - 0204 // User table type
    - ALIAS_NAME
    - DISPLAY_NAME
    - LEGAL_NAME
    - STOCK_EXCHANGE_LISTING_NAME
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0204
    """

    ALIAS_NAME = "A"
    """Alias name"""
    DISPLAY_NAME = "D"
    """Display name"""
    LEGAL_NAME = "L"
    """Legal name"""
    STOCK_EXCHANGE_LISTING_NAME = "SL"
    """Stock exchange listing name"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OrganizationalNameType.ALIAS_NAME: "Alias name",
    OrganizationalNameType.DISPLAY_NAME: "Display name",
    OrganizationalNameType.LEGAL_NAME: "Legal name",
    OrganizationalNameType.STOCK_EXCHANGE_LISTING_NAME: "Stock exchange listing name",
}
