from ...base import HL7Table

"""
HL7 Version: 2.5.1
Production Class Code - 0429
Table Type: User
"""


class ProductionClassCode(HL7Table):
    """
    Production Class Code - 0429 // User table type
    - BREEDING_OR_GENETIC_STOCK
    - DAIRY
    - DRAFT
    - DUAL_PURPOSE
    - LAYER_INCLUDES_MULTIPLIER_FLOCKS
    - MEAT
    - NOT_APPLICABLE
    - OTHER
    - PLEASURE
    - RACING
    - SHOW
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0429
    """

    BREEDING_OR_GENETIC_STOCK = "BR"
    """Breeding/genetic stock"""
    DAIRY = "DA"
    """Dairy"""
    DRAFT = "DR"
    """Draft"""
    DUAL_PURPOSE = "DU"
    """Dual Purpose"""
    LAYER_INCLUDES_MULTIPLIER_FLOCKS = "LY"
    """Layer, Includes Multiplier flocks"""
    MEAT = "MT"
    """Meat"""
    NOT_APPLICABLE = "NA"
    """Not Applicable"""
    OTHER = "OT"
    """Other"""
    PLEASURE = "PL"
    """Pleasure"""
    RACING = "RA"
    """Racing"""
    SHOW = "SH"
    """Show"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProductionClassCode.BREEDING_OR_GENETIC_STOCK: "Breeding/genetic stock",
    ProductionClassCode.DAIRY: "Dairy",
    ProductionClassCode.DRAFT: "Draft",
    ProductionClassCode.DUAL_PURPOSE: "Dual Purpose",
    ProductionClassCode.LAYER_INCLUDES_MULTIPLIER_FLOCKS: "Layer, Includes Multiplier flocks",
    ProductionClassCode.MEAT: "Meat",
    ProductionClassCode.NOT_APPLICABLE: "Not Applicable",
    ProductionClassCode.OTHER: "Other",
    ProductionClassCode.PLEASURE: "Pleasure",
    ProductionClassCode.RACING: "Racing",
    ProductionClassCode.SHOW: "Show",
    ProductionClassCode.UNKNOWN: "Unknown",
}
