from ...base import HL7Table

"""
HL7 Version: 2.5.1
Segment action code - 0206
Table Type: HL7
"""


class SegmentActionCode(HL7Table):
    """
    Segment action code - 0206 // HL7 table type
    - ADD_OR_INSERT
    - DELETE
    - UPDATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0206
    """

    ADD_OR_INSERT = "A"
    """Add/Insert"""
    DELETE = "D"
    """Delete"""
    UPDATE = "U"
    """Update"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SegmentActionCode.ADD_OR_INSERT: "Add/Insert",
    SegmentActionCode.DELETE: "Delete",
    SegmentActionCode.UPDATE: "Update",
}
