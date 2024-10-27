from ...base import HL7Table

"""
HL7 Version: 2.5.1
Ethnic Group - 0189
Table Type: User
"""


class EthnicGroup(HL7Table):
    """
    Ethnic Group - 0189 // User table type
    - HISPANIC_OR_LATINO
    - NOT_HISPANIC_OR_LATINO
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0189
    """

    HISPANIC_OR_LATINO = "H"
    """Hispanic or Latino"""
    NOT_HISPANIC_OR_LATINO = "N"
    """Not Hispanic or Latino"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EthnicGroup.HISPANIC_OR_LATINO: "Hispanic or Latino",
    EthnicGroup.NOT_HISPANIC_OR_LATINO: "Not Hispanic or Latino",
    EthnicGroup.UNKNOWN: "Unknown",
}
