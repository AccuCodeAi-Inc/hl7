from ...base import HL7Table

"""
HL7 Version: 2.5.1
Quantity limited request - 0126
Table Type: HL7
"""


class QuantityLimitedRequest(HL7Table):
    """
    Quantity limited request - 0126 // HL7 table type
    - CHARACTERS
    - LINES
    - PAGES
    - RECORDS
    - LOCALLY_DEFINED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0126
    """

    CHARACTERS = "CH"  # RSP/RTB/RDY
    """Characters"""
    LINES = "LI"  # RTB/RDY
    """Lines"""
    PAGES = "PG"  # RDY
    """Pages"""
    RECORDS = "RD"  # RSP/RTB/RDY
    """Records"""
    LOCALLY_DEFINED = "ZO"
    """Locally defined"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    QuantityLimitedRequest.CHARACTERS: "Characters",
    QuantityLimitedRequest.LINES: "Lines",
    QuantityLimitedRequest.PAGES: "Pages",
    QuantityLimitedRequest.RECORDS: "Records",
    QuantityLimitedRequest.LOCALLY_DEFINED: "Locally defined",
}
