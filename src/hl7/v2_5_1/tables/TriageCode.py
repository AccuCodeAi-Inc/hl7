from ...base import HL7Table

"""
HL7 Version: 2.5.1
Triage Code - 0422
Table Type: User
"""


class TriageCode(HL7Table):
    """
    Triage Code - 0422 // User table type
    - NON_ACUTE
    - ACUTE
    - URGENT
    - SEVERE
    - DEAD_ON_ARRIVAL
    - OTHER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0422
    """

    NON_ACUTE = "1"
    """Non-acute"""
    ACUTE = "2"
    """Acute"""
    URGENT = "3"
    """Urgent"""
    SEVERE = "4"
    """Severe"""
    DEAD_ON_ARRIVAL = "5"
    """Dead on Arrival (DOA)"""
    OTHER = "99"
    """Other"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TriageCode.NON_ACUTE: "Non-acute",
    TriageCode.ACUTE: "Acute",
    TriageCode.URGENT: "Urgent",
    TriageCode.SEVERE: "Severe",
    TriageCode.DEAD_ON_ARRIVAL: "Dead on Arrival (DOA)",
    TriageCode.OTHER: "Other",
}
