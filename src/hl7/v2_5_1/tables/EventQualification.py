from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event Qualification - 0237
Table Type: HL7
"""


class EventQualification(HL7Table):
    """
    Event Qualification - 0237 // HL7 table type
    - ABUSE
    - UNEXPECTED_BENEFICIAL_EFFECT
    - DEPENDENCY
    - INTERACTION
    - LACK_OF_EXPECT_THERAPEUTIC_EFFECT
    - MISUSE
    - OVERDOSE
    - DRUG_WITHDRAWAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0237
    """

    ABUSE = "A"
    """Abuse"""
    UNEXPECTED_BENEFICIAL_EFFECT = "B"
    """Unexpected beneficial effect"""
    DEPENDENCY = "D"
    """Dependency"""
    INTERACTION = "I"
    """Interaction"""
    LACK_OF_EXPECT_THERAPEUTIC_EFFECT = "L"
    """Lack of expect therapeutic effect"""
    MISUSE = "M"
    """Misuse"""
    OVERDOSE = "O"
    """Overdose"""
    DRUG_WITHDRAWAL = "W"
    """Drug withdrawal"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventQualification.ABUSE: "Abuse",
    EventQualification.UNEXPECTED_BENEFICIAL_EFFECT: "Unexpected beneficial effect",
    EventQualification.DEPENDENCY: "Dependency",
    EventQualification.INTERACTION: "Interaction",
    EventQualification.LACK_OF_EXPECT_THERAPEUTIC_EFFECT: "Lack of expect therapeutic effect",
    EventQualification.MISUSE: "Misuse",
    EventQualification.OVERDOSE: "Overdose",
    EventQualification.DRUG_WITHDRAWAL: "Drug withdrawal",
}
