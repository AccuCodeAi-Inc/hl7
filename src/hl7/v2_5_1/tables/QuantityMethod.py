from ...base import HL7Table

"""
HL7 Version: 2.5.1
Quantity method - 0329
Table Type: HL7
"""


class QuantityMethod(HL7Table):
    """
    Quantity method - 0329 // HL7 table type
    - ACTUAL_COUNT
    - ESTIMATED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0329
    """

    ACTUAL_COUNT = "A"
    """Actual count"""
    ESTIMATED = "E"
    """Estimated (see comment)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    QuantityMethod.ACTUAL_COUNT: "Actual count",
    QuantityMethod.ESTIMATED: "Estimated (see comment)",
}
