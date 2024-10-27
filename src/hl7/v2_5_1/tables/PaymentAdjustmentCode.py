from ...base import HL7Table

"""
HL7 Version: 2.5.1
Payment Adjustment Code - 0468
Table Type: User
"""


class PaymentAdjustmentCode(HL7Table):
    """
    Payment Adjustment Code - 0468 // User table type
    - NO_PAYMENT_ADJUSTMENT
    - DESIGNATED_CURRENT_DRUG_OR_BIOLOGICAL_PAYMENT_ADJUSTMENT_APPLIES_TO_APC
    - DESIGNATED_NEW_DEVICE_PAYMENT_ADJUSTMENT_APPLIES_TO_APC
    - DESIGNATED_NEW_DRUG_OR_NEW_BIOLOGICAL_PAYMENT_ADJUSTMENT_APPLIES_TO_APC
    - DEDUCTIBLE_NOT_APPLICABLE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0468
    """

    NO_PAYMENT_ADJUSTMENT = "1"
    """No payment adjustment"""
    DESIGNATED_CURRENT_DRUG_OR_BIOLOGICAL_PAYMENT_ADJUSTMENT_APPLIES_TO_APC = "2"
    """Designated current drug or biological payment adjustment applies to APC (status indicator G)"""
    DESIGNATED_NEW_DEVICE_PAYMENT_ADJUSTMENT_APPLIES_TO_APC = "3"
    """Designated new device payment adjustment applies to APC (status indicator H)"""
    DESIGNATED_NEW_DRUG_OR_NEW_BIOLOGICAL_PAYMENT_ADJUSTMENT_APPLIES_TO_APC = "4"
    """Designated new drug or new biological payment adjustment applies to APC (status indicator J)"""
    DEDUCTIBLE_NOT_APPLICABLE = "5"
    """Deductible not applicable (specific list of HCPCS codes)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PaymentAdjustmentCode.NO_PAYMENT_ADJUSTMENT: "No payment adjustment",
    PaymentAdjustmentCode.DESIGNATED_CURRENT_DRUG_OR_BIOLOGICAL_PAYMENT_ADJUSTMENT_APPLIES_TO_APC: "Designated current drug or biological payment adjustment applies to APC (status indicator G)",
    PaymentAdjustmentCode.DESIGNATED_NEW_DEVICE_PAYMENT_ADJUSTMENT_APPLIES_TO_APC: "Designated new device payment adjustment applies to APC (status indicator H)",
    PaymentAdjustmentCode.DESIGNATED_NEW_DRUG_OR_NEW_BIOLOGICAL_PAYMENT_ADJUSTMENT_APPLIES_TO_APC: "Designated new drug or new biological payment adjustment applies to APC (status indicator J)",
    PaymentAdjustmentCode.DEDUCTIBLE_NOT_APPLICABLE: "Deductible not applicable (specific list of HCPCS codes)",
}
