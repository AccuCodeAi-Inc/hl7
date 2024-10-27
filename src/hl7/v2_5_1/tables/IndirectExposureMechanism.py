from ...base import HL7Table

"""
HL7 Version: 2.5.1
Indirect exposure mechanism - 0253
Table Type: HL7
"""


class IndirectExposureMechanism(HL7Table):
    """
    Indirect exposure mechanism - 0253 // HL7 table type
    - BREAST_MILK
    - FATHER
    - OTHER
    - TRANSPLACENTAL
    - BLOOD_PRODUCT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0253
    """

    BREAST_MILK = "B"
    """Breast milk"""
    FATHER = "F"
    """Father"""
    OTHER = "O"
    """Other"""
    TRANSPLACENTAL = "P"
    """Transplacental"""
    BLOOD_PRODUCT = "X"
    """Blood product"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    IndirectExposureMechanism.BREAST_MILK: "Breast milk",
    IndirectExposureMechanism.FATHER: "Father",
    IndirectExposureMechanism.OTHER: "Other",
    IndirectExposureMechanism.TRANSPLACENTAL: "Transplacental",
    IndirectExposureMechanism.BLOOD_PRODUCT: "Blood product",
}
