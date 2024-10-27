from ...base import HL7Table

"""
HL7 Version: 2.5.1
Provider role - 0443
Table Type: User
"""


class ProviderRole(HL7Table):
    """
    Provider role - 0443 // User table type
    - ADMITTING
    - ATTENDING
    - CONSULTING_PROVIDER
    - FAMILY_HEALTH_CARE_PROFESSIONAL
    - PRIMARY_CARE_PROVIDER
    - REFERRING_PROVIDER
    - REFERRED_TO_PROVIDER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0443
    """

    ADMITTING = "AD"  # PV1-17 Admitting doctor
    """Admitting"""
    ATTENDING = "AT"  # PV1-7 Attending doctor
    """Attending"""
    CONSULTING_PROVIDER = "CP"
    """Consulting Provider"""
    FAMILY_HEALTH_CARE_PROFESSIONAL = "FHCP"
    """Family Health Care Professional"""
    PRIMARY_CARE_PROVIDER = "PP"
    """Primary Care Provider"""
    REFERRING_PROVIDER = "RP"  # PV1-8 Referring doctor
    """Referring Provider"""
    REFERRED_TO_PROVIDER = "RT"
    """Referred to Provider"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProviderRole.ADMITTING: "Admitting",
    ProviderRole.ATTENDING: "Attending",
    ProviderRole.CONSULTING_PROVIDER: "Consulting Provider",
    ProviderRole.FAMILY_HEALTH_CARE_PROFESSIONAL: "Family Health Care Professional",
    ProviderRole.PRIMARY_CARE_PROVIDER: "Primary Care Provider",
    ProviderRole.REFERRING_PROVIDER: "Referring Provider",
    ProviderRole.REFERRED_TO_PROVIDER: "Referred to Provider",
}
