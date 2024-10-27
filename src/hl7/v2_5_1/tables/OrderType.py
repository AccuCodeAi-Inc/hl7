from ...base import HL7Table

"""
HL7 Version: 2.5.1
Order Type - 0482
Table Type: HL7
"""


class OrderType(HL7Table):
    """
    Order Type - 0482 // HL7 table type
    - INPATIENT_ORDER
    - OUTPATIENT_ORDER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0482
    """

    INPATIENT_ORDER = "I"
    """Inpatient Order"""
    OUTPATIENT_ORDER = "O"
    """Outpatient Order"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OrderType.INPATIENT_ORDER: "Inpatient Order",
    OrderType.OUTPATIENT_ORDER: "Outpatient Order",
}
