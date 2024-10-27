from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event Consequence - 0240
Table Type: HL7
"""


class EventConsequence(HL7Table):
    """
    Event Consequence - 0240 // HL7 table type
    - CONGENITAL_ANOMALY_OR_BIRTH_DEFECT
    - DEATH
    - CAUSED_HOSPITALIZED
    - INCAPACITY_WHICH_IS_SIGNIFICANT_PERSISTENT_OR_PERMANENT
    - DISABILITY_WHICH_IS_SIGNIFICANT_PERSISTENT_OR_PERMANENT
    - LIFE_THREATENING
    - OTHER
    - PROLONGED_HOSPITALIZATION
    - REQUIRED_INTERVENTION_TO_PREVENT_PERMANENT_IMPAIRMENT_OR_DAMAGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0240
    """

    CONGENITAL_ANOMALY_OR_BIRTH_DEFECT = "C"
    """Congenital anomaly/birth defect"""
    DEATH = "D"
    """Death"""
    CAUSED_HOSPITALIZED = "H"
    """Caused hospitalized"""
    INCAPACITY_WHICH_IS_SIGNIFICANT_PERSISTENT_OR_PERMANENT = "I"
    """Incapacity which is significant, persistent or permanent"""
    DISABILITY_WHICH_IS_SIGNIFICANT_PERSISTENT_OR_PERMANENT = "J"
    """Disability which is significant, persistent or permanent"""
    LIFE_THREATENING = "L"
    """Life threatening"""
    OTHER = "O"
    """Other"""
    PROLONGED_HOSPITALIZATION = "P"
    """Prolonged hospitalization"""
    REQUIRED_INTERVENTION_TO_PREVENT_PERMANENT_IMPAIRMENT_OR_DAMAGE = "R"
    """Required intervention to prevent permanent impairment/damage"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventConsequence.CONGENITAL_ANOMALY_OR_BIRTH_DEFECT: "Congenital anomaly/birth defect",
    EventConsequence.DEATH: "Death",
    EventConsequence.CAUSED_HOSPITALIZED: "Caused hospitalized",
    EventConsequence.INCAPACITY_WHICH_IS_SIGNIFICANT_PERSISTENT_OR_PERMANENT: "Incapacity which is significant, persistent or permanent",
    EventConsequence.DISABILITY_WHICH_IS_SIGNIFICANT_PERSISTENT_OR_PERMANENT: "Disability which is significant, persistent or permanent",
    EventConsequence.LIFE_THREATENING: "Life threatening",
    EventConsequence.OTHER: "Other",
    EventConsequence.PROLONGED_HOSPITALIZATION: "Prolonged hospitalization",
    EventConsequence.REQUIRED_INTERVENTION_TO_PREVENT_PERMANENT_IMPAIRMENT_OR_DAMAGE: "Required intervention to prevent permanent impairment/damage",
}
