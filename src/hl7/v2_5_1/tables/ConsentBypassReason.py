from ...base import HL7Table

"""
HL7 Version: 2.5.1
Consent Bypass Reason - 0499
Table Type: User
"""


class ConsentBypassReason(HL7Table):
    """
    Consent Bypass Reason - 0499 // User table type
    - EMERGENCY
    - PROFESSIONAL_JUDGMENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0499
    """

    EMERGENCY = "E"
    """Emergency"""
    PROFESSIONAL_JUDGMENT = "PJ"
    """Professional Judgment"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConsentBypassReason.EMERGENCY: "Emergency",
    ConsentBypassReason.PROFESSIONAL_JUDGMENT: "Professional Judgment",
}
