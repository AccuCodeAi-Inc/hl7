from ...base import HL7Table

"""
HL7 Version: 2.5.1
Referral category - 0284
Table Type: User
"""


class ReferralCategory(HL7Table):
    """
    Referral category - 0284 // User table type
    - AMBULATORY
    - EMERGENCY
    - INPATIENT
    - OUTPATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0284
    """

    AMBULATORY = "A"
    """Ambulatory"""
    EMERGENCY = "E"
    """Emergency"""
    INPATIENT = "I"
    """Inpatient"""
    OUTPATIENT = "O"
    """Outpatient"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReferralCategory.AMBULATORY: "Ambulatory",
    ReferralCategory.EMERGENCY: "Emergency",
    ReferralCategory.INPATIENT: "Inpatient",
    ReferralCategory.OUTPATIENT: "Outpatient",
}
