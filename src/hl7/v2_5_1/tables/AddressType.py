from ...base import HL7Table

"""
HL7 Version: 2.5.1
Address type - 0190
Table Type: HL7
"""


class AddressType(HL7Table):
    """
    Address type - 0190 // HL7 table type
    - FIRM_OR_BUSINESS
    - BAD_ADDRESS
    - BIRTH_DELIVERY_LOCATION
    - RESIDENCE_AT_BIRTH
    - CURRENT_OR_TEMPORARY
    - COUNTRY_OF_ORIGIN
    - HOME
    - LEGAL_ADDRESS
    - MAILING
    - BIRTH
    - OFFICE
    - PERMANENT
    - REGISTRY_HOME_REFERS_TO_THE_INFORMATION_SYSTEM_TYPICALLY_MANAGED_BY_A_PUBLIC_HEALTH_AGENCY_THAT_STORES_PATIENT_INFORMATION_SUCH_AS_IMMUNIZATION_HISTORIES_OR_CANCER_DATA_REGARDLESS_OF_WHERE_THE_PATIENT_OBTAINS_SERVICES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0190
    """

    FIRM_OR_BUSINESS = "B"
    """Firm/Business"""
    BAD_ADDRESS = "BA"
    """Bad address"""
    BIRTH_DELIVERY_LOCATION = "BDL"
    """Birth delivery location (address where birth occurred)"""
    RESIDENCE_AT_BIRTH = "BR"
    """Residence at birth (home address at time of birth)"""
    CURRENT_OR_TEMPORARY = "C"
    """Current Or Temporary"""
    COUNTRY_OF_ORIGIN = "F"
    """Country Of Origin"""
    HOME = "H"
    """Home"""
    LEGAL_ADDRESS = "L"
    """Legal Address"""
    MAILING = "M"
    """Mailing"""
    BIRTH = "N"
    """Birth (nee) (birth address, not otherwise specified)"""
    OFFICE = "O"
    """Office"""
    PERMANENT = "P"
    """Permanent"""
    REGISTRY_HOME_REFERS_TO_THE_INFORMATION_SYSTEM_TYPICALLY_MANAGED_BY_A_PUBLIC_HEALTH_AGENCY_THAT_STORES_PATIENT_INFORMATION_SUCH_AS_IMMUNIZATION_HISTORIES_OR_CANCER_DATA_REGARDLESS_OF_WHERE_THE_PATIENT_OBTAINS_SERVICES = "RH"
    """Registry home. Refers to the information system, typically managed by a public health agency, that stores patient information such as immunization histories or cancer data, regardless of where the patient obtains services."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AddressType.FIRM_OR_BUSINESS: "Firm/Business",
    AddressType.BAD_ADDRESS: "Bad address",
    AddressType.BIRTH_DELIVERY_LOCATION: "Birth delivery location (address where birth occurred)",
    AddressType.RESIDENCE_AT_BIRTH: "Residence at birth (home address at time of birth)",
    AddressType.CURRENT_OR_TEMPORARY: "Current Or Temporary",
    AddressType.COUNTRY_OF_ORIGIN: "Country Of Origin",
    AddressType.HOME: "Home",
    AddressType.LEGAL_ADDRESS: "Legal Address",
    AddressType.MAILING: "Mailing",
    AddressType.BIRTH: "Birth (nee) (birth address, not otherwise specified)",
    AddressType.OFFICE: "Office",
    AddressType.PERMANENT: "Permanent",
    AddressType.REGISTRY_HOME_REFERS_TO_THE_INFORMATION_SYSTEM_TYPICALLY_MANAGED_BY_A_PUBLIC_HEALTH_AGENCY_THAT_STORES_PATIENT_INFORMATION_SUCH_AS_IMMUNIZATION_HISTORIES_OR_CANCER_DATA_REGARDLESS_OF_WHERE_THE_PATIENT_OBTAINS_SERVICES: "Registry home. Refers to the information system, typically managed by a public health agency, that stores patient information such as immunization histories or cancer data, regardless of where the patient obtains services.",
}
