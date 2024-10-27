from ...base import HL7Table

"""
HL7 Version: 2.5.1
Amount class - 0193
Table Type: User
"""


class AmountClass(HL7Table):
    """
    Amount class - 0193 // User table type
    - AMOUNT
    - LIMIT
    - PERCENTAGE
    - UNLIMITED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0193
    """

    AMOUNT = "AT"  # Retained for backward compatibility only as of v 2.5
    """Amount"""
    LIMIT = "LM"
    """Limit"""
    PERCENTAGE = "PC"  # Retained for backward compatibility only as of v 2.5
    """Percentage"""
    UNLIMITED = "UL"
    """Unlimited"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AmountClass.AMOUNT: "Amount",
    AmountClass.LIMIT: "Limit",
    AmountClass.PERCENTAGE: "Percentage",
    AmountClass.UNLIMITED: "Unlimited",
}
