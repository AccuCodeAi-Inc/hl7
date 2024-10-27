from ...base import HL7Table

"""
HL7 Version: 2.5.1
Provider billing - 0187
Table Type: HL7
"""


class ProviderBilling(HL7Table):
    """
    Provider billing - 0187 // HL7 table type
    - INSTITUTION_BILLS_FOR_PROVIDER
    - PROVIDER_DOES_OWN_BILLING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0187
    """

    INSTITUTION_BILLS_FOR_PROVIDER = "I"
    """Institution bills for provider"""
    PROVIDER_DOES_OWN_BILLING = "P"
    """Provider does own billing"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProviderBilling.INSTITUTION_BILLS_FOR_PROVIDER: "Institution bills for provider",
    ProviderBilling.PROVIDER_DOES_OWN_BILLING: "Provider does own billing",
}
