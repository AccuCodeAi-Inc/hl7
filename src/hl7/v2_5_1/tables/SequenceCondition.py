from ...base import HL7Table

"""
HL7 Version: 2.5.1
Sequence condition - 0524
Table Type: HL7
"""


class SequenceCondition(HL7Table):
    """
    Sequence condition - 0524 // HL7 table type
    - REPEATING_CYCLE_OF_ORDERS
    - RESERVED_FOR_POSSIBLE_FUTURE_USE
    - SEQUENCE_CONDITIONS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0524
    """

    REPEATING_CYCLE_OF_ORDERS = "C"
    """Repeating cycle of orders"""
    RESERVED_FOR_POSSIBLE_FUTURE_USE = "R"
    """Reserved for possible future use"""
    SEQUENCE_CONDITIONS = "S"
    """Sequence conditions"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SequenceCondition.REPEATING_CYCLE_OF_ORDERS: "Repeating cycle of orders",
    SequenceCondition.RESERVED_FOR_POSSIBLE_FUTURE_USE: "Reserved for possible future use",
    SequenceCondition.SEQUENCE_CONDITIONS: "Sequence conditions",
}
