from ...base import HL7Table

"""
HL7 Version: 2.5.1
RX Component Type - 0166
Table Type: HL7
"""


class RxComponentType(HL7Table):
    """
    RX Component Type - 0166 // HL7 table type
    - ADDITIVE
    - BASE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0166
    """

    ADDITIVE = "A"
    """Additive"""
    BASE = "B"
    """Base"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RxComponentType.ADDITIVE: "Additive",
    RxComponentType.BASE: "Base",
}
