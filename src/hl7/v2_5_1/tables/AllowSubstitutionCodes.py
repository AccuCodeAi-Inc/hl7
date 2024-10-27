from ...base import HL7Table

"""
HL7 Version: 2.5.1
Allow Substitution Codes - 0279
Table Type: User
"""


class AllowSubstitutionCodes(HL7Table):
    """
    Allow Substitution Codes - 0279 // User table type
    - CONTACT_THE_PLACER_CONTACT_PERSON_PRIOR_TO_MAKING_ANY_SUBSTITUTIONS_OF_THIS_RESOURCE
    - SUBSTITUTION_OF_THIS_RESOURCE_IS_NOT_ALLOWED
    - NOTIFY_THE_PLACER_CONTACT_PERSON_THROUGH_NORMAL_INSTITUTIONAL_PROCEDURES_THAT_A_SUBSTITUTION_OF_THIS_RESOURCE_HAS_BEEN_MADE
    - SUBSTITUTION_OF_THIS_RESOURCE_IS_ALLOWED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0279
    """

    CONTACT_THE_PLACER_CONTACT_PERSON_PRIOR_TO_MAKING_ANY_SUBSTITUTIONS_OF_THIS_RESOURCE = "Confirm"
    """Contact the Placer Contact Person prior to making any substitutions of this resource"""
    SUBSTITUTION_OF_THIS_RESOURCE_IS_NOT_ALLOWED = "No"
    """Substitution of this resource is not allowed"""
    NOTIFY_THE_PLACER_CONTACT_PERSON_THROUGH_NORMAL_INSTITUTIONAL_PROCEDURES_THAT_A_SUBSTITUTION_OF_THIS_RESOURCE_HAS_BEEN_MADE = "Notify"
    """Notify the Placer Contact Person, through normal institutional procedures, that a substitution of this resource has been made"""
    SUBSTITUTION_OF_THIS_RESOURCE_IS_ALLOWED = "Yes"
    """Substitution of this resource is allowed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AllowSubstitutionCodes.CONTACT_THE_PLACER_CONTACT_PERSON_PRIOR_TO_MAKING_ANY_SUBSTITUTIONS_OF_THIS_RESOURCE: "Contact the Placer Contact Person prior to making any substitutions of this resource",
    AllowSubstitutionCodes.SUBSTITUTION_OF_THIS_RESOURCE_IS_NOT_ALLOWED: "Substitution of this resource is not allowed",
    AllowSubstitutionCodes.NOTIFY_THE_PLACER_CONTACT_PERSON_THROUGH_NORMAL_INSTITUTIONAL_PROCEDURES_THAT_A_SUBSTITUTION_OF_THIS_RESOURCE_HAS_BEEN_MADE: "Notify the Placer Contact Person, through normal institutional procedures, that a substitution of this resource has been made",
    AllowSubstitutionCodes.SUBSTITUTION_OF_THIS_RESOURCE_IS_ALLOWED: "Substitution of this resource is allowed",
}
