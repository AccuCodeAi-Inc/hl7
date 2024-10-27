from ...base import HL7Table

"""
HL7 Version: 2.5.1
Pharmacy Order Types - 0480
Table Type: HL7
"""


class PharmacyOrderTypes(HL7Table):
    """
    Pharmacy Order Types - 0480 // HL7 table type
    - MEDICATION
    - OTHER_SOLUTION_AS_MEDICATION_ORDERS
    - IV_LARGE_VOLUME_SOLUTIONS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0480
    """

    MEDICATION = "M"  # Default value.  Includes, but is not limited to, tables, capsules, powders, puffs, and other non-injected/non-infused products.
    """Medication"""
    OTHER_SOLUTION_AS_MEDICATION_ORDERS = (
        "O"  # Includes, but is not limited to, piggybacks and syringes
    )
    """Other solution as medication orders"""
    IV_LARGE_VOLUME_SOLUTIONS = (
        "S"  # Includes, but is not limited to, TPNs, admixtures, solutions and drips.
    )
    """IV Large Volume Solutions"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PharmacyOrderTypes.MEDICATION: "Medication",
    PharmacyOrderTypes.OTHER_SOLUTION_AS_MEDICATION_ORDERS: "Other solution as medication orders",
    PharmacyOrderTypes.IV_LARGE_VOLUME_SOLUTIONS: "IV Large Volume Solutions",
}
