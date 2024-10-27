from ...base import HL7Table

"""
HL7 Version: 2.5.1
Eligibility Source - 0144
Table Type: User
"""


class EligibilitySource(HL7Table):
    """
    Eligibility Source - 0144 // User table type
    - INSURANCE_COMPANY
    - EMPLOYER
    - INSURED_PRESENTED_POLICY
    - INSURED_PRESENTED_CARD
    - SIGNED_STATEMENT_ON_FILE
    - VERBAL_INFORMATION
    - NONE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0144
    """

    INSURANCE_COMPANY = "1"
    """Insurance company"""
    EMPLOYER = "2"
    """Employer"""
    INSURED_PRESENTED_POLICY = "3"
    """Insured presented policy"""
    INSURED_PRESENTED_CARD = "4"
    """Insured presented card"""
    SIGNED_STATEMENT_ON_FILE = "5"
    """Signed statement on file"""
    VERBAL_INFORMATION = "6"
    """Verbal information"""
    NONE = "7"
    """None"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EligibilitySource.INSURANCE_COMPANY: "Insurance company",
    EligibilitySource.EMPLOYER: "Employer",
    EligibilitySource.INSURED_PRESENTED_POLICY: "Insured presented policy",
    EligibilitySource.INSURED_PRESENTED_CARD: "Insured presented card",
    EligibilitySource.SIGNED_STATEMENT_ON_FILE: "Signed statement on file",
    EligibilitySource.VERBAL_INFORMATION: "Verbal information",
    EligibilitySource.NONE: "None",
}
