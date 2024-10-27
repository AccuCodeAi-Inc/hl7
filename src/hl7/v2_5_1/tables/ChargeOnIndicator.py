from ...base import HL7Table

"""
HL7 Version: 2.5.1
Charge On Indicator - 0269
Table Type: User
"""


class ChargeOnIndicator(HL7Table):
    """
    Charge On Indicator - 0269 // User table type
    - CHARGE_ON_ORDER
    - CHARGE_ON_RESULT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0269
    """

    CHARGE_ON_ORDER = "O"
    """Charge on Order"""
    CHARGE_ON_RESULT = "R"
    """Charge on Result"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ChargeOnIndicator.CHARGE_ON_ORDER: "Charge on Order",
    ChargeOnIndicator.CHARGE_ON_RESULT: "Charge on Result",
}
