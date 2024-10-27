from ...base import HL7Table

"""
HL7 Version: 2.5.1
Escort Required - 0225
Table Type: HL7
"""


class EscortRequired(HL7Table):
    """
    Escort Required - 0225 // HL7 table type
    - NOT_REQUIRED
    - REQUIRED
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0225
    """

    NOT_REQUIRED = "N"
    """Not Required"""
    REQUIRED = "R"
    """Required"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EscortRequired.NOT_REQUIRED: "Not Required",
    EscortRequired.REQUIRED: "Required",
    EscortRequired.UNKNOWN: "Unknown",
}
