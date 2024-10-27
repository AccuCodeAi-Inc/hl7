from ...base import HL7Table

"""
HL7 Version: 2.5.1
Immunization Registry Status - 0441
Table Type: User
"""


class ImmunizationRegistryStatus(HL7Table):
    """
    Immunization Registry Status - 0441 // User table type
    - ACTIVE
    - INACTIVE
    - INACTIVE_LOST_TO_FOLLOW_UP
    - INACTIVE_MOVED_OR_GONE_ELSEWHERE
    - OTHER
    - INACTIVE_PERMANENTLY_INACTIVE
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0441
    """

    ACTIVE = "A"
    """Active"""
    INACTIVE = "I"
    """Inactive"""
    INACTIVE_LOST_TO_FOLLOW_UP = "L"
    """Inactive - Lost to follow-up (cancel contract)"""
    INACTIVE_MOVED_OR_GONE_ELSEWHERE = "M"
    """Inactive - Moved or gone elsewhere (cancel contract)"""
    OTHER = "O"
    """Other"""
    INACTIVE_PERMANENTLY_INACTIVE = "P"
    """Inactive - Permanently inactive (Do not reactivate or add new entries to the record)"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ImmunizationRegistryStatus.ACTIVE: "Active",
    ImmunizationRegistryStatus.INACTIVE: "Inactive",
    ImmunizationRegistryStatus.INACTIVE_LOST_TO_FOLLOW_UP: "Inactive - Lost to follow-up (cancel contract)",
    ImmunizationRegistryStatus.INACTIVE_MOVED_OR_GONE_ELSEWHERE: "Inactive - Moved or gone elsewhere (cancel contract)",
    ImmunizationRegistryStatus.OTHER: "Other",
    ImmunizationRegistryStatus.INACTIVE_PERMANENTLY_INACTIVE: "Inactive - Permanently inactive (Do not reactivate or add new entries to the record)",
    ImmunizationRegistryStatus.UNKNOWN: "Unknown",
}
