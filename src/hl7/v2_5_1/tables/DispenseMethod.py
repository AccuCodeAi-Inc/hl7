from ...base import HL7Table

"""
HL7 Version: 2.5.1
Dispense Method - 0321
Table Type: HL7
"""


class DispenseMethod(HL7Table):
    """
    Dispense Method - 0321 // HL7 table type
    - AUTOMATIC_DISPENSING
    - FLOOR_STOCK
    - TRADITIONAL
    - UNIT_DOSE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0321
    """

    AUTOMATIC_DISPENSING = "AD"
    """Automatic Dispensing"""
    FLOOR_STOCK = "F"
    """Floor Stock"""
    TRADITIONAL = "TR"
    """Traditional"""
    UNIT_DOSE = "UD"
    """Unit Dose"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DispenseMethod.AUTOMATIC_DISPENSING: "Automatic Dispensing",
    DispenseMethod.FLOOR_STOCK: "Floor Stock",
    DispenseMethod.TRADITIONAL: "Traditional",
    DispenseMethod.UNIT_DOSE: "Unit Dose",
}
