from ...base import HL7Table

"""
HL7 Version: 2.5.1
Match reason - 0392
Table Type: User
"""


class MatchReason(HL7Table):
    """
    Match reason - 0392 // User table type
    - MATCH_ON_DATE_OF_BIRTH
    - MATCH_ON_NAME
    - NP
    - MATCH_ON_SOCIAL_SECURITY_NUMBER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0392
    """

    MATCH_ON_DATE_OF_BIRTH = "DB"
    """Match on Date of Birth"""
    MATCH_ON_NAME = "NA"
    """Match on Name (Alpha Match)"""
    NP = "NP"
    """Match on Name (Phonetic Match)"""
    MATCH_ON_SOCIAL_SECURITY_NUMBER = "SS"
    """Match on Social Security Number"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MatchReason.MATCH_ON_DATE_OF_BIRTH: "Match on Date of Birth",
    MatchReason.MATCH_ON_NAME: "Match on Name (Alpha Match)",
    MatchReason.NP: "Match on Name (Phonetic Match)",
    MatchReason.MATCH_ON_SOCIAL_SECURITY_NUMBER: "Match on Social Security Number",
}
