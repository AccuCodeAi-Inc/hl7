from ...base import HL7Table

"""
HL7 Version: 2.5.1
Recreational Drug Use Code - 0431
Table Type: User
"""


class RecreationalDrugUseCode(HL7Table):
    """
    Recreational Drug Use Code - 0431 // User table type
    - ALCOHOL
    - TOBACCO_CHEWED
    - KAVA
    - MARIJUANA
    - OTHER
    - TOBACCO_SMOKED
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0431
    """

    ALCOHOL = "A"
    """Alcohol"""
    TOBACCO_CHEWED = "C"
    """Tobacco - chewed"""
    KAVA = "K"
    """Kava"""
    MARIJUANA = "M"
    """Marijuana"""
    OTHER = "O"
    """Other"""
    TOBACCO_SMOKED = "T"
    """Tobacco - smoked"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RecreationalDrugUseCode.ALCOHOL: "Alcohol",
    RecreationalDrugUseCode.TOBACCO_CHEWED: "Tobacco - chewed",
    RecreationalDrugUseCode.KAVA: "Kava",
    RecreationalDrugUseCode.MARIJUANA: "Marijuana",
    RecreationalDrugUseCode.OTHER: "Other",
    RecreationalDrugUseCode.TOBACCO_SMOKED: "Tobacco - smoked",
    RecreationalDrugUseCode.UNKNOWN: "Unknown",
}
