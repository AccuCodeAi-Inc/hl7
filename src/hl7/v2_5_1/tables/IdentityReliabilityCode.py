from ...base import HL7Table

"""
HL7 Version: 2.5.1
Identity Reliability Code - 0445
Table Type: User
"""


class IdentityReliabilityCode(HL7Table):
    """
    Identity Reliability Code - 0445 // User table type
    - PATIENT_OR_PERSON_NAME_IS_AN_ALIAS
    - UNKNOWN_OR_DEFAULT_ADDRESS
    - UNKNOWN_OR_DEFAULT_DATE_OF_BIRTH
    - UNKNOWN_OR_DEFAULT_SOCIAL_SECURITY_NUMBER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0445
    """

    PATIENT_OR_PERSON_NAME_IS_AN_ALIAS = "AL"
    """Patient/Person Name is an Alias"""
    UNKNOWN_OR_DEFAULT_ADDRESS = "UA"
    """Unknown/Default Address"""
    UNKNOWN_OR_DEFAULT_DATE_OF_BIRTH = "UD"
    """Unknown/Default Date of Birth"""
    UNKNOWN_OR_DEFAULT_SOCIAL_SECURITY_NUMBER = "US"
    """Unknown/Default Social Security Number"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    IdentityReliabilityCode.PATIENT_OR_PERSON_NAME_IS_AN_ALIAS: "Patient/Person Name is an Alias",
    IdentityReliabilityCode.UNKNOWN_OR_DEFAULT_ADDRESS: "Unknown/Default Address",
    IdentityReliabilityCode.UNKNOWN_OR_DEFAULT_DATE_OF_BIRTH: "Unknown/Default Date of Birth",
    IdentityReliabilityCode.UNKNOWN_OR_DEFAULT_SOCIAL_SECURITY_NUMBER: "Unknown/Default Social Security Number",
}
