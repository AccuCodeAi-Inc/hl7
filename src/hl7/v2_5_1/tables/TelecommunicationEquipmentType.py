from ...base import HL7Table

"""
HL7 Version: 2.5.1
Telecommunication equipment type - 0202
Table Type: HL7
"""


class TelecommunicationEquipmentType(HL7Table):
    """
    Telecommunication equipment type - 0202 // HL7 table type
    - BEEPER
    - CELLULAR_PHONE
    - FAX
    - INTERNET_ADDRESS_USE_ONLY_IF_TELECOMMUNICATION_USE_CODE_IS_NET
    - MODEM
    - TELEPHONE
    - TELECOMMUNICATIONS_DEVICE_FOR_THE_DEAF
    - TELETYPEWRITER
    - X_400_EMAIL_ADDRESS_USE_ONLY_IF_TELECOMMUNICATION_USE_CODE_IS_NET
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0202
    """

    BEEPER = "BP"
    """Beeper"""
    CELLULAR_PHONE = "CP"
    """Cellular Phone"""
    FAX = "FX"
    """Fax"""
    INTERNET_ADDRESS_USE_ONLY_IF_TELECOMMUNICATION_USE_CODE_IS_NET = "Internet"
    """Internet Address: Use Only If Telecommunication Use Code Is NET"""
    MODEM = "MD"
    """Modem"""
    TELEPHONE = "PH"
    """Telephone"""
    TELECOMMUNICATIONS_DEVICE_FOR_THE_DEAF = "TDD"
    """Telecommunications Device for the Deaf"""
    TELETYPEWRITER = "TTY"
    """Teletypewriter"""
    X_400_EMAIL_ADDRESS_USE_ONLY_IF_TELECOMMUNICATION_USE_CODE_IS_NET = "X.400"
    """X.400 email address: Use Only If Telecommunication Use Code Is NET"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    TelecommunicationEquipmentType.BEEPER: "Beeper",
    TelecommunicationEquipmentType.CELLULAR_PHONE: "Cellular Phone",
    TelecommunicationEquipmentType.FAX: "Fax",
    TelecommunicationEquipmentType.INTERNET_ADDRESS_USE_ONLY_IF_TELECOMMUNICATION_USE_CODE_IS_NET: "Internet Address: Use Only If Telecommunication Use Code Is NET",
    TelecommunicationEquipmentType.MODEM: "Modem",
    TelecommunicationEquipmentType.TELEPHONE: "Telephone",
    TelecommunicationEquipmentType.TELECOMMUNICATIONS_DEVICE_FOR_THE_DEAF: "Telecommunications Device for the Deaf",
    TelecommunicationEquipmentType.TELETYPEWRITER: "Teletypewriter",
    TelecommunicationEquipmentType.X_400_EMAIL_ADDRESS_USE_ONLY_IF_TELECOMMUNICATION_USE_CODE_IS_NET: "X.400 email address: Use Only If Telecommunication Use Code Is NET",
}
