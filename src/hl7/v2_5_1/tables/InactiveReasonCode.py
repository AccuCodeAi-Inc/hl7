from ...base import HL7Table

"""
HL7 Version: 2.5.1
Inactive Reason Code - 0540
Table Type: User
"""


class InactiveReasonCode(HL7Table):
    """
    Inactive Reason Code - 0540 // User table type
    - LEAVE_OF_ABSENCE
    - RETIRED
    - TERMINATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0540
    """

    LEAVE_OF_ABSENCE = "L"
    """Leave of Absence"""
    RETIRED = "R"
    """Retired"""
    TERMINATION = "T"
    """Termination"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    InactiveReasonCode.LEAVE_OF_ABSENCE: "Leave of Absence",
    InactiveReasonCode.RETIRED: "Retired",
    InactiveReasonCode.TERMINATION: "Termination",
}
