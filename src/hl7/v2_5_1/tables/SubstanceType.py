from ...base import HL7Table

"""
HL7 Version: 2.5.1
Substance type - 0384
Table Type: HL7
"""


class SubstanceType(HL7Table):
    """
    Substance type - 0384 // HL7 table type
    - CONTROL
    - DILUENT
    - MEASURABLE_LIQUID_ITEM
    - LIQUID_WASTE
    - MULTIPLE_TEST_REAGENT
    - OTHER
    - PRETREATMENT
    - PURIFIED_WATER
    - REAGENT_CALIBRATOR
    - COUNTABLE_SOLID_ITEM
    - SINGLE_TEST_REAGENT
    - SOLID_WASTE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0384
    """

    CONTROL = "CO"
    """Control"""
    DILUENT = "DI"
    """Diluent"""
    MEASURABLE_LIQUID_ITEM = "LI"
    """Measurable Liquid Item"""
    LIQUID_WASTE = "LW"
    """Liquid Waste"""
    MULTIPLE_TEST_REAGENT = (
        "MR"  # The consumption cannot be tied to orders for a single test
    )
    """Multiple Test Reagent"""
    OTHER = "OT"
    """Other"""
    PRETREATMENT = "PT"
    """Pretreatment"""
    PURIFIED_WATER = "PW"
    """Purified Water"""
    REAGENT_CALIBRATOR = "RC"
    """Reagent Calibrator"""
    COUNTABLE_SOLID_ITEM = "SC"  # E.g., Pipetting tip
    """Countable Solid Item"""
    SINGLE_TEST_REAGENT = "SR"
    """Single Test Reagent"""
    SOLID_WASTE = "SW"
    """Solid Waste"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SubstanceType.CONTROL: "Control",
    SubstanceType.DILUENT: "Diluent",
    SubstanceType.MEASURABLE_LIQUID_ITEM: "Measurable Liquid Item",
    SubstanceType.LIQUID_WASTE: "Liquid Waste",
    SubstanceType.MULTIPLE_TEST_REAGENT: "Multiple Test Reagent",
    SubstanceType.OTHER: "Other",
    SubstanceType.PRETREATMENT: "Pretreatment",
    SubstanceType.PURIFIED_WATER: "Purified Water",
    SubstanceType.REAGENT_CALIBRATOR: "Reagent Calibrator",
    SubstanceType.COUNTABLE_SOLID_ITEM: "Countable Solid Item",
    SubstanceType.SINGLE_TEST_REAGENT: "Single Test Reagent",
    SubstanceType.SOLID_WASTE: "Solid Waste",
}
