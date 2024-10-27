from ...base import HL7Table

"""
HL7 Version: 2.5.1
Living Will Code - 0315
Table Type: User
"""


class LivingWillCode(HL7Table):
    """
    Living Will Code - 0315 // User table type
    - YES_PATIENT_HAS_A_LIVING_WILL_BUT_IT_IS_NOT_ON_FILE
    - NO_PATIENT_DOES_NOT_HAVE_A_LIVING_WILL_BUT_INFORMATION_WAS_PROVIDED
    - NO_PATIENT_DOES_NOT_HAVE_A_LIVING_WILL_AND_NO_INFORMATION_WAS_PROVIDED
    - UNKNOWN
    - YES_PATIENT_HAS_A_LIVING_WILL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0315
    """

    YES_PATIENT_HAS_A_LIVING_WILL_BUT_IT_IS_NOT_ON_FILE = "F"
    """Yes, patient has a living will but it is not on file"""
    NO_PATIENT_DOES_NOT_HAVE_A_LIVING_WILL_BUT_INFORMATION_WAS_PROVIDED = "I"
    """No, patient does not have a living will but information was provided"""
    NO_PATIENT_DOES_NOT_HAVE_A_LIVING_WILL_AND_NO_INFORMATION_WAS_PROVIDED = "N"
    """No, patient does not have a living will and no information was provided"""
    UNKNOWN = "U"
    """Unknown"""
    YES_PATIENT_HAS_A_LIVING_WILL = "Y"
    """Yes, patient has a living will"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LivingWillCode.YES_PATIENT_HAS_A_LIVING_WILL_BUT_IT_IS_NOT_ON_FILE: "Yes, patient has a living will but it is not on file",
    LivingWillCode.NO_PATIENT_DOES_NOT_HAVE_A_LIVING_WILL_BUT_INFORMATION_WAS_PROVIDED: "No, patient does not have a living will but information was provided",
    LivingWillCode.NO_PATIENT_DOES_NOT_HAVE_A_LIVING_WILL_AND_NO_INFORMATION_WAS_PROVIDED: "No, patient does not have a living will and no information was provided",
    LivingWillCode.UNKNOWN: "Unknown",
    LivingWillCode.YES_PATIENT_HAS_A_LIVING_WILL: "Yes, patient has a living will",
}
