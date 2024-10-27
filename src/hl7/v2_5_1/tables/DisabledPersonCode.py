from ...base import HL7Table

"""
HL7 Version: 2.5.1
Disabled Person Code - 0334
Table Type: User
"""


class DisabledPersonCode(HL7Table):
    """
    Disabled Person Code - 0334 // User table type
    - ASSOCIATED_PARTY
    - GUARANTOR
    - INSURED
    - PATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0334
    """

    ASSOCIATED_PARTY = "AP"
    """Associated party"""
    GUARANTOR = "GT"
    """Guarantor"""
    INSURED = "IN"
    """Insured"""
    PATIENT = "PT"
    """Patient"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DisabledPersonCode.ASSOCIATED_PARTY: "Associated party",
    DisabledPersonCode.GUARANTOR: "Guarantor",
    DisabledPersonCode.INSURED: "Insured",
    DisabledPersonCode.PATIENT: "Patient",
}
