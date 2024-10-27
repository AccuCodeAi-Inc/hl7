from ...base import HL7Table

"""
HL7 Version: 2.5.1
Living Arrangement - 0220
Table Type: User
"""


class LivingArrangement(HL7Table):
    """
    Living Arrangement - 0220 // User table type
    - ALONE
    - FAMILY
    - INSTITUTION
    - RELATIVE
    - SPOUSE_ONLY
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0220
    """

    ALONE = "A"
    """Alone"""
    FAMILY = "F"
    """Family"""
    INSTITUTION = "I"
    """Institution"""
    RELATIVE = "R"
    """Relative"""
    SPOUSE_ONLY = "S"
    """Spouse Only"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LivingArrangement.ALONE: "Alone",
    LivingArrangement.FAMILY: "Family",
    LivingArrangement.INSTITUTION: "Institution",
    LivingArrangement.RELATIVE: "Relative",
    LivingArrangement.SPOUSE_ONLY: "Spouse Only",
    LivingArrangement.UNKNOWN: "Unknown",
}
