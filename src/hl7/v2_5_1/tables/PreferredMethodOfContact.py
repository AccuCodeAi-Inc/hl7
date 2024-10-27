from ...base import HL7Table

"""
HL7 Version: 2.5.1
Preferred method of contact - 0185
Table Type: HL7
"""


class PreferredMethodOfContact(HL7Table):
    """
    Preferred method of contact - 0185 // HL7 table type
    - BEEPER_NUMBER
    - CELLULAR_PHONE_NUMBER
    - E_MAIL_ADDRESS
    - FAX_NUMBER
    - HOME_PHONE_NUMBER
    - OFFICE_PHONE_NUMBER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0185
    """

    BEEPER_NUMBER = "B"
    """Beeper Number"""
    CELLULAR_PHONE_NUMBER = "C"
    """Cellular Phone Number"""
    E_MAIL_ADDRESS = "E"
    """E-Mail Address (for backward compatibility)"""
    FAX_NUMBER = "F"
    """FAX Number"""
    HOME_PHONE_NUMBER = "H"
    """Home Phone Number"""
    OFFICE_PHONE_NUMBER = "O"
    """Office Phone Number"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PreferredMethodOfContact.BEEPER_NUMBER: "Beeper Number",
    PreferredMethodOfContact.CELLULAR_PHONE_NUMBER: "Cellular Phone Number",
    PreferredMethodOfContact.E_MAIL_ADDRESS: "E-Mail Address (for backward compatibility)",
    PreferredMethodOfContact.FAX_NUMBER: "FAX Number",
    PreferredMethodOfContact.HOME_PHONE_NUMBER: "Home Phone Number",
    PreferredMethodOfContact.OFFICE_PHONE_NUMBER: "Office Phone Number",
}
