from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event reason - 0062
Table Type: User
"""


class EventReason(HL7Table):
    """
    Event reason - 0062 // User table type
    - PATIENT_REQUEST
    - PHYSICIAN_OR_HEALTH_PRACTITIONER_ORDER
    - CENSUS_MANAGEMENT
    - OTHER
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0062
    """

    PATIENT_REQUEST = "01"
    """Patient request"""
    PHYSICIAN_OR_HEALTH_PRACTITIONER_ORDER = "02"
    """Physician/health practitioner order"""
    CENSUS_MANAGEMENT = "03"
    """Census management"""
    OTHER = "O"
    """Other"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventReason.PATIENT_REQUEST: "Patient request",
    EventReason.PHYSICIAN_OR_HEALTH_PRACTITIONER_ORDER: "Physician/health practitioner order",
    EventReason.CENSUS_MANAGEMENT: "Census management",
    EventReason.OTHER: "Other",
    EventReason.UNKNOWN: "Unknown",
}
