from ...base import HL7Table

"""
HL7 Version: 2.5.1
Non-Subject Consenter Reason - 0502
Table Type: User
"""


class NonSubjectConsenterReason(HL7Table):
    """
    Non-Subject Consenter Reason - 0502 // User table type
    - LEGALLY_MANDATED
    - SUBJECT_IS_A_MINOR
    - SUBJECT_IS_NOT_COMPETENT_TO_CONSENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0502
    """

    LEGALLY_MANDATED = "LM"
    """Legally mandated"""
    SUBJECT_IS_A_MINOR = "MIN"
    """Subject is a minor"""
    SUBJECT_IS_NOT_COMPETENT_TO_CONSENT = "NC"
    """Subject is not competent to consent"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NonSubjectConsenterReason.LEGALLY_MANDATED: "Legally mandated",
    NonSubjectConsenterReason.SUBJECT_IS_A_MINOR: "Subject is a minor",
    NonSubjectConsenterReason.SUBJECT_IS_NOT_COMPETENT_TO_CONSENT: "Subject is not competent to consent",
}
