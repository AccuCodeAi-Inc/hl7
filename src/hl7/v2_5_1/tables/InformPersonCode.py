from ...base import HL7Table

"""
HL7 Version: 2.5.1
Inform person code - 0517
Table Type: User
"""


class InformPersonCode(HL7Table):
    """
    Inform person code - 0517 // User table type
    - INFORM_HELP_DESK
    - DO_NOT_INFORM_PATIENT
    - INFORM_PATIENT
    - INFORM_USER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0517
    """

    INFORM_HELP_DESK = "HD"
    """Inform help desk"""
    DO_NOT_INFORM_PATIENT = "NPAT"
    """Do NOT inform patient"""
    INFORM_PATIENT = "PAT"
    """Inform patient"""
    INFORM_USER = "USR"
    """Inform User"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    InformPersonCode.INFORM_HELP_DESK: "Inform help desk",
    InformPersonCode.DO_NOT_INFORM_PATIENT: "Do NOT inform patient",
    InformPersonCode.INFORM_PATIENT: "Inform patient",
    InformPersonCode.INFORM_USER: "Inform User",
}
