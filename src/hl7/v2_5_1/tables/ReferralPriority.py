from ...base import HL7Table

"""
HL7 Version: 2.5.1
Referral priority - 0280
Table Type: User
"""


class ReferralPriority(HL7Table):
    """
    Referral priority - 0280 // User table type
    - ASAP
    - ROUTINE
    - STAT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0280
    """

    ASAP = "A"
    """ASAP"""
    ROUTINE = "R"
    """Routine"""
    STAT = "S"
    """STAT"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReferralPriority.ASAP: "ASAP",
    ReferralPriority.ROUTINE: "Routine",
    ReferralPriority.STAT: "STAT",
}
