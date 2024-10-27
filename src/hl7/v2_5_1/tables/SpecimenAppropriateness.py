from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Appropriateness - 0492
Table Type: User
"""


class SpecimenAppropriateness(HL7Table):
    """
    Specimen Appropriateness - 0492 // User table type
    - INAPPROPRIATE_DUE_TO
    - APPROPRIATE
    - INAPPROPRIATE
    - PREFERRED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0492
    """

    INAPPROPRIATE_DUE_TO = "??"
    """Inappropriate due to"""
    APPROPRIATE = "A"
    """Appropriate"""
    INAPPROPRIATE = "I"
    """Inappropriate"""
    PREFERRED = "P"
    """Preferred"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenAppropriateness.INAPPROPRIATE_DUE_TO: "Inappropriate due to",
    SpecimenAppropriateness.APPROPRIATE: "Appropriate",
    SpecimenAppropriateness.INAPPROPRIATE: "Inappropriate",
    SpecimenAppropriateness.PREFERRED: "Preferred",
}
