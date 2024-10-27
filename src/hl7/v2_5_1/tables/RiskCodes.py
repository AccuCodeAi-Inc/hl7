from ...base import HL7Table

"""
HL7 Version: 2.5.1
Risk Codes - 0489
Table Type: User
"""


class RiskCodes(HL7Table):
    """
    Risk Codes - 0489 // User table type
    - AGGRESSIVE
    - BIOHAZARD
    - BIOLOGICAL
    - CORROSIVE
    - ESCAPE_RISK
    - EXPLOSIVE
    - MATERIALDANGERINFLAMMABLE
    - MATERIALDANGERINFECTIOUS
    - INJURY_HAZARD
    - POISON
    - RADIOACTIVE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0489
    """

    AGGRESSIVE = "AGG"
    """Aggressive"""
    BIOHAZARD = "BHZ"
    """Biohazard"""
    BIOLOGICAL = "BIO"
    """Biological"""
    CORROSIVE = "COR"
    """Corrosive"""
    ESCAPE_RISK = "ESC"
    """Escape Risk"""
    EXPLOSIVE = "EXP"
    """Explosive"""
    MATERIALDANGERINFLAMMABLE = "IFL"
    """MaterialDangerInflammable"""
    MATERIALDANGERINFECTIOUS = "INF"
    """MaterialDangerInfectious"""
    INJURY_HAZARD = "INJ"
    """Injury Hazard"""
    POISON = "POI"
    """Poison"""
    RADIOACTIVE = "RAD"
    """Radioactive"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RiskCodes.AGGRESSIVE: "Aggressive",
    RiskCodes.BIOHAZARD: "Biohazard",
    RiskCodes.BIOLOGICAL: "Biological",
    RiskCodes.CORROSIVE: "Corrosive",
    RiskCodes.ESCAPE_RISK: "Escape Risk",
    RiskCodes.EXPLOSIVE: "Explosive",
    RiskCodes.MATERIALDANGERINFLAMMABLE: "MaterialDangerInflammable",
    RiskCodes.MATERIALDANGERINFECTIOUS: "MaterialDangerInfectious",
    RiskCodes.INJURY_HAZARD: "Injury Hazard",
    RiskCodes.POISON: "Poison",
    RiskCodes.RADIOACTIVE: "Radioactive",
}
