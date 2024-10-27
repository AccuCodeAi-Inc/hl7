from ...base import HL7Table

"""
HL7 Version: 2.5.1
Authorization Mode - 0483
Table Type: HL7
"""


class AuthorizationMode(HL7Table):
    """
    Authorization Mode - 0483 // HL7 table type
    - ELECTRONIC
    - E_MAIL
    - FAX
    - IN_PERSON
    - MAIL
    - PAPER
    - PHONE
    - REFLEXIVE
    - VIDEO_CONFERENCE
    - VOICE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0483
    """

    ELECTRONIC = "EL"
    """Electronic"""
    E_MAIL = "EM"
    """E-mail"""
    FAX = "FX"
    """Fax"""
    IN_PERSON = "IP"
    """In Person"""
    MAIL = "MA"
    """Mail"""
    PAPER = "PA"
    """Paper"""
    PHONE = "PH"
    """Phone"""
    REFLEXIVE = "RE"
    """Reflexive (Automated system)"""
    VIDEO_CONFERENCE = "VC"
    """Video-conference"""
    VOICE = "VO"
    """Voice"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AuthorizationMode.ELECTRONIC: "Electronic",
    AuthorizationMode.E_MAIL: "E-mail",
    AuthorizationMode.FAX: "Fax",
    AuthorizationMode.IN_PERSON: "In Person",
    AuthorizationMode.MAIL: "Mail",
    AuthorizationMode.PAPER: "Paper",
    AuthorizationMode.PHONE: "Phone",
    AuthorizationMode.REFLEXIVE: "Reflexive (Automated system)",
    AuthorizationMode.VIDEO_CONFERENCE: "Video-conference",
    AuthorizationMode.VOICE: "Voice",
}
