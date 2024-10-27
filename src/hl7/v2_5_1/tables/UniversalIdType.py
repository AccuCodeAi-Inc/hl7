from ...base import HL7Table

"""
HL7 Version: 2.5.1
Universal ID type - 0301
Table Type: HL7
"""


class UniversalIdType(HL7Table):
    """
    Universal ID type - 0301 // HL7 table type
    - AN_INTERNET_DOTTED_NAME_EITHER_IN_ASCII_OR_AS_INTEGERS
    - SAME_AS_UUID
    - THE_CEN_HEALTHCARE_CODING_SCHEME_DESIGNATOR
    - RESERVED_FOR_FUTURE_HL7_REGISTRATION_SCHEMES
    - AN_INTERNATIONAL_STANDARDS_ORGANIZATION_OBJECT_IDENTIFIER
    - THESE_ARE_RESERVED_FOR_LOCALLY_DEFINED_CODING_SCHEMES
    - USUALLY_A_BASE64_ENCODED_STRING_OF_RANDOM_BITS_THE_UNIQUENESS_DEPENDS_ON_THE_LENGTH_OF_THE_BITS_MAIL_SYSTEMS_OFTEN_GENERATE_ASCII_STRING_UNIQUE_NAMES_FROM_A_COMBINATION_OF_RANDOM_BITS_AND_SYSTEM_NAMES_OBVIOUSLY_SUCH_IDENTIFIERS_WILL_NOT_BE_CONSTRAINED_TO_T
    - UNIFORM_RESOURCE_IDENTIFIER
    - THE_DCE_UNIVERSAL_UNIQUE_IDENTIFIER
    - AN_X_400_MHS_FORMAT_IDENTIFIER
    - AN_X_500_DIRECTORY_NAME
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0301
    """

    AN_INTERNET_DOTTED_NAME_EITHER_IN_ASCII_OR_AS_INTEGERS = "DNS"
    """An Internet dotted name. Either in ASCII or as integers"""
    SAME_AS_UUID = "GUID"
    """Same as UUID."""
    THE_CEN_HEALTHCARE_CODING_SCHEME_DESIGNATOR = "HCD"
    """The CEN Healthcare Coding Scheme Designator. (Identifiers used in DICOM follow this assignment scheme.)"""
    RESERVED_FOR_FUTURE_HL7_REGISTRATION_SCHEMES = "HL7"
    """Reserved for future HL7 registration schemes"""
    AN_INTERNATIONAL_STANDARDS_ORGANIZATION_OBJECT_IDENTIFIER = "ISO"
    """An International Standards Organization Object Identifier"""
    THESE_ARE_RESERVED_FOR_LOCALLY_DEFINED_CODING_SCHEMES = "L,M,N"
    """These are reserved for locally defined coding schemes."""
    USUALLY_A_BASE64_ENCODED_STRING_OF_RANDOM_BITS_THE_UNIQUENESS_DEPENDS_ON_THE_LENGTH_OF_THE_BITS_MAIL_SYSTEMS_OFTEN_GENERATE_ASCII_STRING_UNIQUE_NAMES_FROM_A_COMBINATION_OF_RANDOM_BITS_AND_SYSTEM_NAMES_OBVIOUSLY_SUCH_IDENTIFIERS_WILL_NOT_BE_CONSTRAINED_TO_T = "Random"
    """Usually a base64 encoded string of random bits. The uniqueness depends on the length of the bits. Mail systems often generate ASCII string unique names, from a combination of random bits and system names. Obviously, such identifiers will not be constrained to the base64 character set."""
    UNIFORM_RESOURCE_IDENTIFIER = "URI"
    """Uniform Resource Identifier"""
    THE_DCE_UNIVERSAL_UNIQUE_IDENTIFIER = "UUID"
    """The DCE Universal Unique Identifier"""
    AN_X_400_MHS_FORMAT_IDENTIFIER = "x400"
    """An X.400 MHS format identifier"""
    AN_X_500_DIRECTORY_NAME = "x500"
    """An X.500 directory name"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    UniversalIdType.AN_INTERNET_DOTTED_NAME_EITHER_IN_ASCII_OR_AS_INTEGERS: "An Internet dotted name. Either in ASCII or as integers",
    UniversalIdType.SAME_AS_UUID: "Same as UUID.",
    UniversalIdType.THE_CEN_HEALTHCARE_CODING_SCHEME_DESIGNATOR: "The CEN Healthcare Coding Scheme Designator. (Identifiers used in DICOM follow this assignment scheme.)",
    UniversalIdType.RESERVED_FOR_FUTURE_HL7_REGISTRATION_SCHEMES: "Reserved for future HL7 registration schemes",
    UniversalIdType.AN_INTERNATIONAL_STANDARDS_ORGANIZATION_OBJECT_IDENTIFIER: "An International Standards Organization Object Identifier",
    UniversalIdType.THESE_ARE_RESERVED_FOR_LOCALLY_DEFINED_CODING_SCHEMES: "These are reserved for locally defined coding schemes.",
    UniversalIdType.USUALLY_A_BASE64_ENCODED_STRING_OF_RANDOM_BITS_THE_UNIQUENESS_DEPENDS_ON_THE_LENGTH_OF_THE_BITS_MAIL_SYSTEMS_OFTEN_GENERATE_ASCII_STRING_UNIQUE_NAMES_FROM_A_COMBINATION_OF_RANDOM_BITS_AND_SYSTEM_NAMES_OBVIOUSLY_SUCH_IDENTIFIERS_WILL_NOT_BE_CONSTRAINED_TO_T: "Usually a base64 encoded string of random bits. The uniqueness depends on the length of the bits. Mail systems often generate ASCII string unique names, from a combination of random bits and system names. Obviously, such identifiers will not be constrained to the base64 character set.",
    UniversalIdType.UNIFORM_RESOURCE_IDENTIFIER: "Uniform Resource Identifier",
    UniversalIdType.THE_DCE_UNIVERSAL_UNIQUE_IDENTIFIER: "The DCE Universal Unique Identifier",
    UniversalIdType.AN_X_400_MHS_FORMAT_IDENTIFIER: "An X.400 MHS format identifier",
    UniversalIdType.AN_X_500_DIRECTORY_NAME: "An X.500 directory name",
}
