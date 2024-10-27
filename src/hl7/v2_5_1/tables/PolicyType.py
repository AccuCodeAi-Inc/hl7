from ...base import HL7Table

"""
HL7 Version: 2.5.1
Policy type - 0147
Table Type: User
"""


class PolicyType(HL7Table):
    """
    Policy type - 0147 // User table type
    - SECOND_ANCILLARY
    - SECOND_MAJOR_MEDICAL
    - THIRD_MAJOR_MEDICAL
    - ANCILLARY
    - MAJOR_MEDICAL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0147
    """

    SECOND_ANCILLARY = "2ANC"
    """Second ancillary"""
    SECOND_MAJOR_MEDICAL = "2MMD"
    """Second major medical"""
    THIRD_MAJOR_MEDICAL = "3MMD"
    """Third major medical"""
    ANCILLARY = "ANC"
    """Ancillary"""
    MAJOR_MEDICAL = "MMD"
    """Major medical"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PolicyType.SECOND_ANCILLARY: "Second ancillary",
    PolicyType.SECOND_MAJOR_MEDICAL: "Second major medical",
    PolicyType.THIRD_MAJOR_MEDICAL: "Third major medical",
    PolicyType.ANCILLARY: "Ancillary",
    PolicyType.MAJOR_MEDICAL: "Major medical",
}
