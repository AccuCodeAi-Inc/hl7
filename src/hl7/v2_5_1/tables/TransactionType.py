from ...base import HL7Table

"""
HL7 Version: 2.5.1
Transaction Type - 0017
Table Type: User
"""


class TransactionType(HL7Table):
    """
    Transaction Type - 0017 // User table type
    - ADJUSTMENT
    - CREDIT
    - CHARGE
    - CO_PAYMENT
    - PAYMENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0017
    """

    ADJUSTMENT = "AJ"
    """Adjustment"""
    CREDIT = "CD"
    """Credit"""
    CHARGE = "CG"
    """Charge"""
    CO_PAYMENT = "CO"
    """Co-payment"""
    PAYMENT = "PY"
    """Payment"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TransactionType.ADJUSTMENT: "Adjustment",
    TransactionType.CREDIT: "Credit",
    TransactionType.CHARGE: "Charge",
    TransactionType.CO_PAYMENT: "Co-payment",
    TransactionType.PAYMENT: "Payment",
}
