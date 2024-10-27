from ...base import HL7Table

"""
HL7 Version: 2.5.1
Money or percentage indicator - 0148
Table Type: HL7
"""


class MoneyOrPercentageIndicator(HL7Table):
    """
    Money or percentage indicator - 0148 // HL7 table type
    - CURRENCY_AMOUNT
    - PERCENTAGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0148
    """

    CURRENCY_AMOUNT = "AT"
    """Currency amount"""
    PERCENTAGE = "PC"
    """Percentage"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MoneyOrPercentageIndicator.CURRENCY_AMOUNT: "Currency amount",
    MoneyOrPercentageIndicator.PERCENTAGE: "Percentage",
}
