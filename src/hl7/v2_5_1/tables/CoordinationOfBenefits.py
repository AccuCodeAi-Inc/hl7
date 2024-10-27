from ...base import HL7Table

"""
HL7 Version: 2.5.1
Coordination of Benefits - 0173
Table Type: User
"""


class CoordinationOfBenefits(HL7Table):
    """
    Coordination of Benefits - 0173 // User table type
    - COORDINATION
    - INDEPENDENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0173
    """

    COORDINATION = "CO"
    """Coordination"""
    INDEPENDENT = "IN"
    """Independent"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CoordinationOfBenefits.COORDINATION: "Coordination",
    CoordinationOfBenefits.INDEPENDENT: "Independent",
}
