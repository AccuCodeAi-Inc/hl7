from ...base import HL7Table

"""
HL7 Version: 2.5.1
Name type - 0200
Table Type: HL7
"""


class NameType(HL7Table):
    """
    Name type - 0200 // HL7 table type
    - ALIAS_NAME
    - NAME_AT_BIRTH
    - ADOPTED_NAME
    - DISPLAY_NAME
    - LICENSING_NAME
    - LEGAL_NAME
    - MAIDEN_NAME
    - NICKNAME_OR_CALL_ME_NAME_OR_STREET_NAME
    - NAME_OF_PARTNER_OR_SPOUSE
    - REGISTERED_NAME
    - CODED_PSEUDO_NAME_TO_ENSURE_ANONYMITY
    - INDIGENOUS_OR_TRIBAL_OR_COMMUNITY_NAME
    - UNSPECIFIED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0200
    """

    ALIAS_NAME = "A"
    """Alias Name"""
    NAME_AT_BIRTH = "B"
    """Name at Birth"""
    ADOPTED_NAME = "C"
    """Adopted Name"""
    DISPLAY_NAME = "D"
    """Display Name"""
    LICENSING_NAME = "I"
    """Licensing Name"""
    LEGAL_NAME = "L"
    """Legal Name"""
    MAIDEN_NAME = "M"
    """Maiden Name"""
    NICKNAME_OR_CALL_ME_NAME_OR_STREET_NAME = "N"
    """Nickname /Call me Name/Street Name"""
    NAME_OF_PARTNER_OR_SPOUSE = "P"
    """Name of Partner/Spouse (retained for backward compatibility only)"""
    REGISTERED_NAME = "R"
    """Registered Name (animals only)"""
    CODED_PSEUDO_NAME_TO_ENSURE_ANONYMITY = "S"
    """Coded Pseudo-Name to ensure anonymity"""
    INDIGENOUS_OR_TRIBAL_OR_COMMUNITY_NAME = "T"
    """Indigenous/Tribal/Community Name"""
    UNSPECIFIED = "U"
    """Unspecified"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NameType.ALIAS_NAME: "Alias Name",
    NameType.NAME_AT_BIRTH: "Name at Birth",
    NameType.ADOPTED_NAME: "Adopted Name",
    NameType.DISPLAY_NAME: "Display Name",
    NameType.LICENSING_NAME: "Licensing Name",
    NameType.LEGAL_NAME: "Legal Name",
    NameType.MAIDEN_NAME: "Maiden Name",
    NameType.NICKNAME_OR_CALL_ME_NAME_OR_STREET_NAME: "Nickname /Call me Name/Street Name",
    NameType.NAME_OF_PARTNER_OR_SPOUSE: "Name of Partner/Spouse (retained for backward compatibility only)",
    NameType.REGISTERED_NAME: "Registered Name (animals only)",
    NameType.CODED_PSEUDO_NAME_TO_ENSURE_ANONYMITY: "Coded Pseudo-Name to ensure anonymity",
    NameType.INDIGENOUS_OR_TRIBAL_OR_COMMUNITY_NAME: "Indigenous/Tribal/Community Name",
    NameType.UNSPECIFIED: "Unspecified",
}
