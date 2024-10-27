from ...base import HL7Table

"""
HL7 Version: 2.5.1
DRG Transfer Type - 0415
Table Type: User
"""


class DrgTransferType(HL7Table):
    """
    DRG Transfer Type - 0415 // User table type
    - DRG_EXEMPT
    - DRG_NON_EXEMPT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0415
    """

    DRG_EXEMPT = "E"
    """DRG Exempt"""
    DRG_NON_EXEMPT = "N"
    """DRG Non Exempt"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DrgTransferType.DRG_EXEMPT: "DRG Exempt",
    DrgTransferType.DRG_NON_EXEMPT: "DRG Non Exempt",
}
