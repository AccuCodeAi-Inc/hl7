from ...base import HL7Table

"""
HL7 Version: 2.5.1
Modifier Edit Code - 0467
Table Type: User
"""


class ModifierEditCode(HL7Table):
    """
    Modifier Edit Code - 0467 // User table type
    - MODIFIER_DOES_NOT_EXIST
    - MODIFIER_PRESENT_NO_ERRORS
    - MODIFIER_INVALID
    - MODIFIER_NOT_APPROVED_FOR_ASC_OR_HOPD_USE
    - MODIFIER_APPROVED_FOR_ASC_OR_HOPD_USE_INAPPROPRIATE_FOR_CODE
    - MODIFIER_EDIT_CODE_UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0467
    """

    MODIFIER_DOES_NOT_EXIST = "0"
    """Modifier does NOT exist"""
    MODIFIER_PRESENT_NO_ERRORS = "1"
    """Modifier present, no errors"""
    MODIFIER_INVALID = "2"
    """Modifier invalid"""
    MODIFIER_NOT_APPROVED_FOR_ASC_OR_HOPD_USE = "3"
    """Modifier NOT approved for ASC/HOPD use"""
    MODIFIER_APPROVED_FOR_ASC_OR_HOPD_USE_INAPPROPRIATE_FOR_CODE = "4"
    """Modifier approved for ASC/HOPD use, inappropriate for code"""
    MODIFIER_EDIT_CODE_UNKNOWN = "U"
    """Modifier edit code unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ModifierEditCode.MODIFIER_DOES_NOT_EXIST: "Modifier does NOT exist",
    ModifierEditCode.MODIFIER_PRESENT_NO_ERRORS: "Modifier present, no errors",
    ModifierEditCode.MODIFIER_INVALID: "Modifier invalid",
    ModifierEditCode.MODIFIER_NOT_APPROVED_FOR_ASC_OR_HOPD_USE: "Modifier NOT approved for ASC/HOPD use",
    ModifierEditCode.MODIFIER_APPROVED_FOR_ASC_OR_HOPD_USE_INAPPROPRIATE_FOR_CODE: "Modifier approved for ASC/HOPD use, inappropriate for code",
    ModifierEditCode.MODIFIER_EDIT_CODE_UNKNOWN: "Modifier edit code unknown",
}
