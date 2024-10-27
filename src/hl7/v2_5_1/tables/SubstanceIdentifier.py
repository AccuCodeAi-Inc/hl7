from ...base import HL7Table

"""
HL7 Version: 2.5.1
Substance identifier - 0451
Table Type: User
"""


class SubstanceIdentifier(HL7Table):
    """
    Substance identifier - 0451 // User table type
    - USED_FOR_QUERY_OF_ALL_INVENTORY_ITEMS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0451
    """

    USED_FOR_QUERY_OF_ALL_INVENTORY_ITEMS = "ALL"
    """Used for query of all inventory items"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SubstanceIdentifier.USED_FOR_QUERY_OF_ALL_INVENTORY_ITEMS: "Used for query of all inventory items",
}
