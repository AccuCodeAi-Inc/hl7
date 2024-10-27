from ...base import HL7Table

"""
HL7 Version: 2.5.1
Source type - 0332
Table Type: HL7
"""


class SourceType(HL7Table):
    """
    Source type - 0332 // HL7 table type
    - ACCEPT
    - INITIATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0332
    """

    ACCEPT = "A"
    """Accept"""
    INITIATE = "I"
    """Initiate"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SourceType.ACCEPT: "Accept",
    SourceType.INITIATE: "Initiate",
}
