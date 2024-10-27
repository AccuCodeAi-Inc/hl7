from ...base import HL7Table

"""
HL7 Version: 2.5.1
Transport Arranged - 0224
Table Type: HL7
"""


class TransportArranged(HL7Table):
    """
    Transport Arranged - 0224 // HL7 table type
    - ARRANGED
    - NOT_ARRANGED
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0224
    """

    ARRANGED = "A"
    """Arranged"""
    NOT_ARRANGED = "N"
    """Not Arranged"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TransportArranged.ARRANGED: "Arranged",
    TransportArranged.NOT_ARRANGED: "Not Arranged",
    TransportArranged.UNKNOWN: "Unknown",
}
