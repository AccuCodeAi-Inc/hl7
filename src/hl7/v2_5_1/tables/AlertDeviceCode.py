from ...base import HL7Table

"""
HL7 Version: 2.5.1
Alert Device Code - 0437
Table Type: User
"""


class AlertDeviceCode(HL7Table):
    """
    Alert Device Code - 0437 // User table type
    - BRACELET
    - NECKLACE
    - WALLET_CARD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0437
    """

    BRACELET = "B"
    """Bracelet"""
    NECKLACE = "N"
    """Necklace"""
    WALLET_CARD = "W"
    """Wallet Card"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AlertDeviceCode.BRACELET: "Bracelet",
    AlertDeviceCode.NECKLACE: "Necklace",
    AlertDeviceCode.WALLET_CARD: "Wallet Card",
}
