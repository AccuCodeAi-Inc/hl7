from ...base import HL7Table

"""
HL7 Version: 2.5.1
Newborn Code - 0425
Table Type: User
"""


class NewbornCode(HL7Table):
    """
    Newborn Code - 0425 // User table type
    - BORN_IN_FACILITY
    - TRANSFER_IN
    - BORN_EN_ROUTE
    - OTHER
    - BORN_AT_HOME
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0425
    """

    BORN_IN_FACILITY = "1"
    """Born in facility"""
    TRANSFER_IN = "2"
    """Transfer in"""
    BORN_EN_ROUTE = "3"
    """Born en route"""
    OTHER = "4"
    """Other"""
    BORN_AT_HOME = "5"
    """Born at home"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NewbornCode.BORN_IN_FACILITY: "Born in facility",
    NewbornCode.TRANSFER_IN: "Transfer in",
    NewbornCode.BORN_EN_ROUTE: "Born en route",
    NewbornCode.OTHER: "Other",
    NewbornCode.BORN_AT_HOME: "Born at home",
}
