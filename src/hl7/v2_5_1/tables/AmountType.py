from ...base import HL7Table

"""
HL7 Version: 2.5.1
Amount type - 0146
Table Type: User
"""


class AmountType(HL7Table):
    """
    Amount type - 0146 // User table type
    - DIFFERENTIAL
    - LIMIT
    - PERCENTAGE
    - RATE
    - UNLIMITED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0146
    """

    DIFFERENTIAL = "DF"
    """Differential"""
    LIMIT = "LM"
    """Limit"""
    PERCENTAGE = "PC"  # Retained for backward compatibility only as of v 2.5
    """Percentage"""
    RATE = "RT"
    """Rate"""
    UNLIMITED = "UL"
    """Unlimited"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AmountType.DIFFERENTIAL: "Differential",
    AmountType.LIMIT: "Limit",
    AmountType.PERCENTAGE: "Percentage",
    AmountType.RATE: "Rate",
    AmountType.UNLIMITED: "Unlimited",
}
