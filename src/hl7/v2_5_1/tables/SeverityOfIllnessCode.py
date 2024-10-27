from ...base import HL7Table

"""
HL7 Version: 2.5.1
Severity of Illness Code - 0421
Table Type: User
"""


class SeverityOfIllnessCode(HL7Table):
    """
    Severity of Illness Code - 0421 // User table type
    - MILD
    - MODERATE
    - SEVERE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0421
    """

    MILD = "MI"
    """Mild"""
    MODERATE = "MO"
    """Moderate"""
    SEVERE = "SE"
    """Severe"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SeverityOfIllnessCode.MILD: "Mild",
    SeverityOfIllnessCode.MODERATE: "Moderate",
    SeverityOfIllnessCode.SEVERE: "Severe",
}
