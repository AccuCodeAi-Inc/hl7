from ...base import HL7Table

"""
HL7 Version: 2.5.1
Dispense Type - 0484
Table Type: User
"""


class DispenseType(HL7Table):
    """
    Dispense Type - 0484 // User table type
    - TRIAL_QUANTITY_BALANCE
    - COMPASSIONATE_FILL
    - NEW_OR_RENEW_FULL_FILL
    - NEW_OR_RENEW_PART_FILL
    - REFILL_PART_FILL
    - REFILL_FULL_FILL
    - MANUFACTURER_SAMPLE
    - TRIAL_QUANTITY
    - NON_PRESCRIPTION_FILL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0484
    """

    TRIAL_QUANTITY_BALANCE = "B"
    """Trial Quantity Balance"""
    COMPASSIONATE_FILL = "C"
    """Compassionate Fill"""
    NEW_OR_RENEW_FULL_FILL = "N"
    """New/Renew - Full Fill"""
    NEW_OR_RENEW_PART_FILL = "P"
    """New/Renew - Part Fill"""
    REFILL_PART_FILL = "Q"
    """Refill - Part Fill"""
    REFILL_FULL_FILL = "R"
    """Refill - Full Fill"""
    MANUFACTURER_SAMPLE = "S"
    """Manufacturer Sample"""
    TRIAL_QUANTITY = "T"
    """Trial Quantity"""
    NON_PRESCRIPTION_FILL = "Z"
    """Non-Prescription Fill"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DispenseType.TRIAL_QUANTITY_BALANCE: "Trial Quantity Balance",
    DispenseType.COMPASSIONATE_FILL: "Compassionate Fill",
    DispenseType.NEW_OR_RENEW_FULL_FILL: "New/Renew - Full Fill",
    DispenseType.NEW_OR_RENEW_PART_FILL: "New/Renew - Part Fill",
    DispenseType.REFILL_PART_FILL: "Refill - Part Fill",
    DispenseType.REFILL_FULL_FILL: "Refill - Full Fill",
    DispenseType.MANUFACTURER_SAMPLE: "Manufacturer Sample",
    DispenseType.TRIAL_QUANTITY: "Trial Quantity",
    DispenseType.NON_PRESCRIPTION_FILL: "Non-Prescription Fill",
}
