from ...base import HL7Table

"""
HL7 Version: 2.5.1
Mail Claim Party - 0137
Table Type: User
"""


class MailClaimParty(HL7Table):
    """
    Mail Claim Party - 0137 // User table type
    - EMPLOYER
    - GUARANTOR
    - INSURANCE_COMPANY
    - OTHER
    - PATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0137
    """

    EMPLOYER = "E"
    """Employer"""
    GUARANTOR = "G"
    """Guarantor"""
    INSURANCE_COMPANY = "I"
    """Insurance company"""
    OTHER = "O"
    """Other"""
    PATIENT = "P"
    """Patient"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MailClaimParty.EMPLOYER: "Employer",
    MailClaimParty.GUARANTOR: "Guarantor",
    MailClaimParty.INSURANCE_COMPANY: "Insurance company",
    MailClaimParty.OTHER: "Other",
    MailClaimParty.PATIENT: "Patient",
}
