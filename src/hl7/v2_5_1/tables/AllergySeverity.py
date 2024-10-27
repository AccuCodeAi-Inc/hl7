from ...base import HL7Table

"""
HL7 Version: 2.5.1
Allergy Severity - 0128
Table Type: User
"""


class AllergySeverity(HL7Table):
    """
    Allergy Severity - 0128 // User table type
    - MILD
    - MODERATE
    - SEVERE
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0128
    """

    MILD = "MI"
    """Mild"""
    MODERATE = "MO"
    """Moderate"""
    SEVERE = "SV"
    """Severe"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AllergySeverity.MILD: "Mild",
    AllergySeverity.MODERATE: "Moderate",
    AllergySeverity.SEVERE: "Severe",
    AllergySeverity.UNKNOWN: "Unknown",
}
