from ...base import HL7Table

"""
HL7 Version: 2.5.1
State/province - 0347
Table Type: User
"""


class StateOrProvince(HL7Table):
    """
    State/province - 0347 // User table type
    - ALBERTA
    - MICHIGAN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0347
    """

    ALBERTA = "AB"
    """Alberta (US and Canada)"""
    MICHIGAN = "MI"
    """Michigan (US)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    StateOrProvince.ALBERTA: "Alberta (US and Canada)",
    StateOrProvince.MICHIGAN: "Michigan (US)",
}
