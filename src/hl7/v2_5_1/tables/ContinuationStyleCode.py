from ...base import HL7Table

"""
HL7 Version: 2.5.1
Continuation style code - 0398
Table Type: HL7
"""


class ContinuationStyleCode(HL7Table):
    """
    Continuation style code - 0398 // HL7 table type
    - FRAGMENTATION
    - INTERACTIVE_CONTINUATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0398
    """

    FRAGMENTATION = "F"
    """Fragmentation"""
    INTERACTIVE_CONTINUATION = "I"
    """Interactive Continuation"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ContinuationStyleCode.FRAGMENTATION: "Fragmentation",
    ContinuationStyleCode.INTERACTIVE_CONTINUATION: "Interactive Continuation",
}
