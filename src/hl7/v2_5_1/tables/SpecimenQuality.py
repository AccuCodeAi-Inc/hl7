from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Quality - 0491
Table Type: User
"""


class SpecimenQuality(HL7Table):
    """
    Specimen Quality - 0491 // User table type
    - EXCELLENT
    - FAIR
    - GOOD
    - POOR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0491
    """

    EXCELLENT = "E"
    """Excellent"""
    FAIR = "F"
    """Fair"""
    GOOD = "G"
    """Good"""
    POOR = "P"
    """Poor"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenQuality.EXCELLENT: "Excellent",
    SpecimenQuality.FAIR: "Fair",
    SpecimenQuality.GOOD: "Good",
    SpecimenQuality.POOR: "Poor",
}
