from ...base import HL7Table

"""
HL7 Version: 2.5.1
Ambulatory Payment Classification Code - 0466
Table Type: User
"""


class AmbulatoryPaymentClassificationCode(HL7Table):
    """
    Ambulatory Payment Classification Code - 0466 // User table type
    - DENTAL_PROCEDURES
    - EXCISION_OR_BIOPSY
    - LEVEL_1_SKIN_REPAIR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0466
    """

    DENTAL_PROCEDURES = "031"
    """Dental procedures"""
    EXCISION_OR_BIOPSY = "163"
    """Excision/biopsy"""
    LEVEL_1_SKIN_REPAIR = "181"
    """Level 1 skin repair."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AmbulatoryPaymentClassificationCode.DENTAL_PROCEDURES: "Dental procedures",
    AmbulatoryPaymentClassificationCode.EXCISION_OR_BIOPSY: "Excision/biopsy",
    AmbulatoryPaymentClassificationCode.LEVEL_1_SKIN_REPAIR: "Level 1 skin repair.",
}
