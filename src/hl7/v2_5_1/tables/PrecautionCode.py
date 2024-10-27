from ...base import HL7Table

"""
HL7 Version: 2.5.1
Precaution Code - 0433
Table Type: User
"""


class PrecautionCode(HL7Table):
    """
    Precaution Code - 0433 // User table type
    - AGGRESSIVE
    - BLIND
    - CONFUSED
    - DEAF
    - ON_IV
    - NO_CODE
    - OTHER
    - PARAPLEGIC
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0433
    """

    AGGRESSIVE = "A"
    """Aggressive"""
    BLIND = "B"
    """Blind"""
    CONFUSED = "C"
    """Confused"""
    DEAF = "D"
    """Deaf"""
    ON_IV = "I"
    """On IV"""
    NO_CODE = "N"
    """No-code (i.e. Do not resuscitate)"""
    OTHER = "O"
    """Other"""
    PARAPLEGIC = "P"
    """Paraplegic"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PrecautionCode.AGGRESSIVE: "Aggressive",
    PrecautionCode.BLIND: "Blind",
    PrecautionCode.CONFUSED: "Confused",
    PrecautionCode.DEAF: "Deaf",
    PrecautionCode.ON_IV: "On IV",
    PrecautionCode.NO_CODE: "No-code (i.e. Do not resuscitate)",
    PrecautionCode.OTHER: "Other",
    PrecautionCode.PARAPLEGIC: "Paraplegic",
    PrecautionCode.UNKNOWN: "Unknown",
}
