from ...base import HL7Table

"""
HL7 Version: 2.5.1
Treatment - 0373
Table Type: User
"""


class Treatment(HL7Table):
    """
    Treatment - 0373 // User table type
    - ACIDIFICATION
    - ALKALIZATION
    - DEFIBRINATION
    - FILTRATION
    - LDL_PRECIPITATION
    - NEUTRALIZATION
    - RECALIFICATION
    - ULTRAFILTRATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0373
    """

    ACIDIFICATION = "ACID"
    """Acidification"""
    ALKALIZATION = "ALK"
    """Alkalization"""
    DEFIBRINATION = "DEFB"
    """Defibrination"""
    FILTRATION = "FILT"
    """Filtration"""
    LDL_PRECIPITATION = "LDLP"
    """LDL Precipitation"""
    NEUTRALIZATION = "NEUT"
    """Neutralization"""
    RECALIFICATION = "RECA"
    """Recalification"""
    ULTRAFILTRATION = "UFIL"
    """Ultrafiltration"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Treatment.ACIDIFICATION: "Acidification",
    Treatment.ALKALIZATION: "Alkalization",
    Treatment.DEFIBRINATION: "Defibrination",
    Treatment.FILTRATION: "Filtration",
    Treatment.LDL_PRECIPITATION: "LDL Precipitation",
    Treatment.NEUTRALIZATION: "Neutralization",
    Treatment.RECALIFICATION: "Recalification",
    Treatment.ULTRAFILTRATION: "Ultrafiltration",
}
