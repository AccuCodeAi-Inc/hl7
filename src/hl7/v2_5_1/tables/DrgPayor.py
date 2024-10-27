from ...base import HL7Table

"""
HL7 Version: 2.5.1
DRG Payor - 0229
Table Type: User
"""


class DrgPayor(HL7Table):
    """
    DRG Payor - 0229 // User table type
    - CHAMPUS
    - MANAGED_CARE_ORGANIZATION
    - MEDICARE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0229
    """

    CHAMPUS = "C"
    """Champus"""
    MANAGED_CARE_ORGANIZATION = "G"
    """Managed Care Organization"""
    MEDICARE = "M"
    """Medicare"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DrgPayor.CHAMPUS: "Champus",
    DrgPayor.MANAGED_CARE_ORGANIZATION: "Managed Care Organization",
    DrgPayor.MEDICARE: "Medicare",
}
