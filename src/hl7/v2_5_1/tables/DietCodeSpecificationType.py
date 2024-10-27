from ...base import HL7Table

"""
HL7 Version: 2.5.1
Diet Code Specification Type - 0159
Table Type: HL7
"""


class DietCodeSpecificationType(HL7Table):
    """
    Diet Code Specification Type - 0159 // HL7 table type
    - DIET
    - PREFERENCE
    - SUPPLEMENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0159
    """

    DIET = "D"
    """Diet"""
    PREFERENCE = "P"
    """Preference"""
    SUPPLEMENT = "S"
    """Supplement"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DietCodeSpecificationType.DIET: "Diet",
    DietCodeSpecificationType.PREFERENCE: "Preference",
    DietCodeSpecificationType.SUPPLEMENT: "Supplement",
}
