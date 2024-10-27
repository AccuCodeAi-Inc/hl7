from ...base import HL7Table

"""
HL7 Version: 2.5.1
Source of comment - 0105
Table Type: HL7
"""


class SourceOfComment(HL7Table):
    """
    Source of comment - 0105 // HL7 table type
    - ANCILLARY
    - OTHER_SYSTEM_IS_SOURCE_OF_COMMENT
    - ORDERER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0105
    """

    ANCILLARY = "L"
    """Ancillary (filler) department is source of comment"""
    OTHER_SYSTEM_IS_SOURCE_OF_COMMENT = "O"
    """Other system is source of comment"""
    ORDERER = "P"
    """Orderer (placer) is source of comment"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SourceOfComment.ANCILLARY: "Ancillary (filler) department is source of comment",
    SourceOfComment.OTHER_SYSTEM_IS_SOURCE_OF_COMMENT: "Other system is source of comment",
    SourceOfComment.ORDERER: "Orderer (placer) is source of comment",
}
