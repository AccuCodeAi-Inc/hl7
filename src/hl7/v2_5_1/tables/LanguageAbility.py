from ...base import HL7Table

"""
HL7 Version: 2.5.1
Language Ability - 0403
Table Type: HL7
"""


class LanguageAbility(HL7Table):
    """
    Language Ability - 0403 // HL7 table type
    - READ
    - WRITE
    - SPEAK
    - UNDERSTAND
    - SIGN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0403
    """

    READ = "1"
    """Read"""
    WRITE = "2"
    """Write"""
    SPEAK = "3"
    """Speak"""
    UNDERSTAND = "4"
    """Understand"""
    SIGN = "5"
    """Sign"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LanguageAbility.READ: "Read",
    LanguageAbility.WRITE: "Write",
    LanguageAbility.SPEAK: "Speak",
    LanguageAbility.UNDERSTAND: "Understand",
    LanguageAbility.SIGN: "Sign",
}
