from ...base import HL7Table

"""
HL7 Version: 2.5.1
Sequence/Results Flag - 0503
Table Type: HL7
"""


class SequenceOrResultsFlag(HL7Table):
    """
    Sequence/Results Flag - 0503 // HL7 table type
    - CYCLICAL
    - RESERVED_FOR_FUTURE_USE
    - SEQUENTIAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0503
    """

    CYCLICAL = "C"  # Used for indicating a repeating cycle of service requests; for example, individual intravenous solutions used in a cyclical sequence (a.k.a. Alternating IVs). This value would be compatible with linking separate service requests or with having all cyclical service request components in a single service request. Likewise, the value would be compatible with either Parent-Child messages or a single service request message to communicate the service requests sequencing
    """Cyclical"""
    RESERVED_FOR_FUTURE_USE = "R"
    """Reserved for future use"""
    SEQUENTIAL = "S"
    """Sequential"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SequenceOrResultsFlag.CYCLICAL: "Cyclical",
    SequenceOrResultsFlag.RESERVED_FOR_FUTURE_USE: "Reserved for future use",
    SequenceOrResultsFlag.SEQUENTIAL: "Sequential",
}
