from ...base import HL7Table

"""
HL7 Version: 2.5.1
Body Site Modifier - 0495
Table Type: HL7
"""


class BodySiteModifier(HL7Table):
    """
    Body Site Modifier - 0495 // HL7 table type
    - ANTERIOR
    - BILATERAL
    - DISTAL
    - EXTERNAL
    - LEFT
    - LATERAL
    - QUADRANT_LEFT_LOWER
    - LOWER
    - QUADRANT_LEFT_UPPER
    - MEDIAL
    - POSTERIOR
    - PROXIMAL
    - RIGHT
    - QUADRANT_RIGHT_LOWER
    - QUADRANT_RIGHT_UPPER
    - UPPER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0495
    """

    ANTERIOR = "ANT"
    """Anterior"""
    BILATERAL = "BIL"
    """Bilateral"""
    DISTAL = "DIS"
    """Distal"""
    EXTERNAL = "EXT"
    """External"""
    LEFT = "L"
    """Left"""
    LATERAL = "LAT"
    """Lateral"""
    QUADRANT_LEFT_LOWER = "LLQ"
    """Quadrant, Left Lower"""
    LOWER = "LOW"
    """Lower"""
    QUADRANT_LEFT_UPPER = "LUQ"
    """Quadrant, Left Upper"""
    MEDIAL = "MED"
    """Medial"""
    POSTERIOR = "POS"
    """Posterior"""
    PROXIMAL = "PRO"
    """Proximal"""
    RIGHT = "R"
    """Right"""
    QUADRANT_RIGHT_LOWER = "RLQ"
    """Quadrant, Right Lower"""
    QUADRANT_RIGHT_UPPER = "RUQ"
    """Quadrant, Right Upper"""
    UPPER = "UPP"
    """Upper"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BodySiteModifier.ANTERIOR: "Anterior",
    BodySiteModifier.BILATERAL: "Bilateral",
    BodySiteModifier.DISTAL: "Distal",
    BodySiteModifier.EXTERNAL: "External",
    BodySiteModifier.LEFT: "Left",
    BodySiteModifier.LATERAL: "Lateral",
    BodySiteModifier.QUADRANT_LEFT_LOWER: "Quadrant, Left Lower",
    BodySiteModifier.LOWER: "Lower",
    BodySiteModifier.QUADRANT_LEFT_UPPER: "Quadrant, Left Upper",
    BodySiteModifier.MEDIAL: "Medial",
    BodySiteModifier.POSTERIOR: "Posterior",
    BodySiteModifier.PROXIMAL: "Proximal",
    BodySiteModifier.RIGHT: "Right",
    BodySiteModifier.QUADRANT_RIGHT_LOWER: "Quadrant, Right Lower",
    BodySiteModifier.QUADRANT_RIGHT_UPPER: "Quadrant, Right Upper",
    BodySiteModifier.UPPER: "Upper",
}
