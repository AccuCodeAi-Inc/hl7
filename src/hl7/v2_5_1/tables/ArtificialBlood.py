from ...base import HL7Table

"""
HL7 Version: 2.5.1
Artificial blood - 0375
Table Type: User
"""


class ArtificialBlood(HL7Table):
    """
    Artificial blood - 0375 // User table type
    - FLUOROCARBONS
    - STROMAL_FREE_HEMOGLOBIN_PREPARATIONS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0375
    """

    FLUOROCARBONS = "FLUR"
    """Fluorocarbons"""
    STROMAL_FREE_HEMOGLOBIN_PREPARATIONS = "SFHB"
    """Stromal free hemoglobin preparations"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ArtificialBlood.FLUOROCARBONS: "Fluorocarbons",
    ArtificialBlood.STROMAL_FREE_HEMOGLOBIN_PREPARATIONS: "Stromal free hemoglobin preparations",
}
