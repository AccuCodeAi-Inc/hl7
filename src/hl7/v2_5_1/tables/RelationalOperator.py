from ...base import HL7Table

"""
HL7 Version: 2.5.1
Relational operator - 0209
Table Type: HL7
"""


class RelationalOperator(HL7Table):
    """
    Relational operator - 0209 // HL7 table type
    - CONTAINS
    - EQUAL
    - GREATER_THAN_OR_EQUAL
    - GENERIC
    - GREATER_THAN
    - LESS_THAN_OR_EQUAL
    - LESS_THAN
    - NOT_EQUAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0209
    """

    CONTAINS = "CT"
    """Contains"""
    EQUAL = "EQ"
    """Equal"""
    GREATER_THAN_OR_EQUAL = "GE"
    """Greater than or equal"""
    GENERIC = "GN"
    """Generic"""
    GREATER_THAN = "GT"
    """Greater than"""
    LESS_THAN_OR_EQUAL = "LE"
    """Less than or equal"""
    LESS_THAN = "LT"
    """Less than"""
    NOT_EQUAL = "NE"
    """Not Equal"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RelationalOperator.CONTAINS: "Contains",
    RelationalOperator.EQUAL: "Equal",
    RelationalOperator.GREATER_THAN_OR_EQUAL: "Greater than or equal",
    RelationalOperator.GENERIC: "Generic",
    RelationalOperator.GREATER_THAN: "Greater than",
    RelationalOperator.LESS_THAN_OR_EQUAL: "Less than or equal",
    RelationalOperator.LESS_THAN: "Less than",
    RelationalOperator.NOT_EQUAL: "Not Equal",
}
