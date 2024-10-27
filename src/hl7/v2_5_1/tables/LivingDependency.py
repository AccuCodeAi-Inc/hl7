from ...base import HL7Table

"""
HL7 Version: 2.5.1
Living Dependency - 0223
Table Type: User
"""


class LivingDependency(HL7Table):
    """
    Living Dependency - 0223 // User table type
    - SMALL_CHILDREN_DEPENDENT
    - MEDICAL_SUPERVISION_REQUIRED
    - OTHER
    - SPOUSE_DEPENDENT
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0223
    """

    SMALL_CHILDREN_DEPENDENT = "C"
    """Small Children Dependent"""
    MEDICAL_SUPERVISION_REQUIRED = "M"
    """Medical Supervision Required"""
    OTHER = "O"
    """Other"""
    SPOUSE_DEPENDENT = "S"
    """Spouse Dependent"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LivingDependency.SMALL_CHILDREN_DEPENDENT: "Small Children Dependent",
    LivingDependency.MEDICAL_SUPERVISION_REQUIRED: "Medical Supervision Required",
    LivingDependency.OTHER: "Other",
    LivingDependency.SPOUSE_DEPENDENT: "Spouse Dependent",
    LivingDependency.UNKNOWN: "Unknown",
}
