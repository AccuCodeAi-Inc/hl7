from ...base import HL7Table

"""
HL7 Version: 2.5.1
Language Proficiency - 0404
Table Type: HL7
"""


class LanguageProficiency(HL7Table):
    """
    Language Proficiency - 0404 // HL7 table type
    - EXCELLENT
    - GOOD
    - FAIR
    - POOR
    - SOME
    - NONE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0404
    """

    EXCELLENT = "1"
    """Excellent"""
    GOOD = "2"
    """Good"""
    FAIR = "3"
    """Fair"""
    POOR = "4"
    """Poor"""
    SOME = "5"
    """Some (level unknown)"""
    NONE = "6"
    """None"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LanguageProficiency.EXCELLENT: "Excellent",
    LanguageProficiency.GOOD: "Good",
    LanguageProficiency.FAIR: "Fair",
    LanguageProficiency.POOR: "Poor",
    LanguageProficiency.SOME: "Some (level unknown)",
    LanguageProficiency.NONE: "None",
}
