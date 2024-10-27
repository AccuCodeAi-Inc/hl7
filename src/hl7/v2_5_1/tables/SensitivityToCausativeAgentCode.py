from ...base import HL7Table

"""
HL7 Version: 2.5.1
Sensitivity to Causative Agent Code - 0436
Table Type: User
"""


class SensitivityToCausativeAgentCode(HL7Table):
    """
    Sensitivity to Causative Agent Code - 0436 // User table type
    - ADVERSE_REACTION
    - ALLERGY
    - CONTRAINDICATION
    - INTOLERANCE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0436
    """

    ADVERSE_REACTION = "AD"
    """Adverse Reaction (Not otherwise classified)"""
    ALLERGY = "AL"
    """Allergy"""
    CONTRAINDICATION = "CT"
    """Contraindication"""
    INTOLERANCE = "IN"
    """Intolerance"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SensitivityToCausativeAgentCode.ADVERSE_REACTION: "Adverse Reaction (Not otherwise classified)",
    SensitivityToCausativeAgentCode.ALLERGY: "Allergy",
    SensitivityToCausativeAgentCode.CONTRAINDICATION: "Contraindication",
    SensitivityToCausativeAgentCode.INTOLERANCE: "Intolerance",
}
