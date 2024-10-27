from ...base import HL7Table

"""
HL7 Version: 2.5.1
Action Code - 0323
Table Type: HL7
"""


class ActionCode(HL7Table):
    """
    Action Code - 0323 // HL7 table type
    - ADD_OR_INSERT
    - DELETE
    - UPDATE
    - NO_CHANGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0323
    """

    ADD_OR_INSERT = "A"
    """Add/Insert"""
    DELETE = "D"
    """Delete"""
    UPDATE = "U"
    """Update"""
    NO_CHANGE = "X"
    """No change"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ActionCode.ADD_OR_INSERT: "Add/Insert",
    ActionCode.DELETE: "Delete",
    ActionCode.UPDATE: "Update",
    ActionCode.NO_CHANGE: "No change",
}
