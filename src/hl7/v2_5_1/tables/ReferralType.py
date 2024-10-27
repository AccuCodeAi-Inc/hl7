from ...base import HL7Table

"""
HL7 Version: 2.5.1
Referral type - 0281
Table Type: User
"""


class ReferralType(HL7Table):
    """
    Referral type - 0281 // User table type
    - HOME_CARE
    - LABORATORY
    - MEDICAL
    - PSYCHIATRIC
    - RADIOLOGY
    - SKILLED_NURSING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0281
    """

    HOME_CARE = "Hom"
    """Home Care"""
    LABORATORY = "Lab"
    """Laboratory"""
    MEDICAL = "Med"
    """Medical"""
    PSYCHIATRIC = "Psy"
    """Psychiatric"""
    RADIOLOGY = "Rad"
    """Radiology"""
    SKILLED_NURSING = "Skn"
    """Skilled Nursing"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReferralType.HOME_CARE: "Home Care",
    ReferralType.LABORATORY: "Laboratory",
    ReferralType.MEDICAL: "Medical",
    ReferralType.PSYCHIATRIC: "Psychiatric",
    ReferralType.RADIOLOGY: "Radiology",
    ReferralType.SKILLED_NURSING: "Skilled Nursing",
}
