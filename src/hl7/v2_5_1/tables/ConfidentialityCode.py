from ...base import HL7Table

"""
HL7 Version: 2.5.1
Confidentiality code - 0177
Table Type: User
"""


class ConfidentialityCode(HL7Table):
    """
    Confidentiality code - 0177 // User table type
    - AIDS_PATIENT
    - EMPLOYEE
    - ALCOHOL_OR_DRUG_TREATMENT_PATIENT
    - HIV
    - PSYCHIATRIC_PATIENT
    - RESTRICTED
    - USUAL_CONTROL
    - UNWED_MOTHER
    - VERY_RESTRICTED
    - VERY_IMPORTANT_PERSON_OR_CELEBRITY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0177
    """

    AIDS_PATIENT = "AID"
    """AIDS patient"""
    EMPLOYEE = "EMP"
    """Employee"""
    ALCOHOL_OR_DRUG_TREATMENT_PATIENT = "ETH"
    """Alcohol/drug treatment patient"""
    HIV = "HIV"
    """HIV(+) patient"""
    PSYCHIATRIC_PATIENT = "PSY"
    """Psychiatric patient"""
    RESTRICTED = "R"
    """Restricted"""
    USUAL_CONTROL = "U"
    """Usual control"""
    UNWED_MOTHER = "UWM"
    """Unwed mother"""
    VERY_RESTRICTED = "V"
    """Very restricted"""
    VERY_IMPORTANT_PERSON_OR_CELEBRITY = "VIP"
    """Very important person or celebrity"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConfidentialityCode.AIDS_PATIENT: "AIDS patient",
    ConfidentialityCode.EMPLOYEE: "Employee",
    ConfidentialityCode.ALCOHOL_OR_DRUG_TREATMENT_PATIENT: "Alcohol/drug treatment patient",
    ConfidentialityCode.HIV: "HIV(+) patient",
    ConfidentialityCode.PSYCHIATRIC_PATIENT: "Psychiatric patient",
    ConfidentialityCode.RESTRICTED: "Restricted",
    ConfidentialityCode.USUAL_CONTROL: "Usual control",
    ConfidentialityCode.UNWED_MOTHER: "Unwed mother",
    ConfidentialityCode.VERY_RESTRICTED: "Very restricted",
    ConfidentialityCode.VERY_IMPORTANT_PERSON_OR_CELEBRITY: "Very important person or celebrity",
}
