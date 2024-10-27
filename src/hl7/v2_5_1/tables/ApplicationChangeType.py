from ...base import HL7Table

"""
HL7 Version: 2.5.1
Application change type - 0409
Table Type: User
"""


class ApplicationChangeType(HL7Table):
    """
    Application change type - 0409 // User table type
    - MIGRATES_TO_DIFFERENT_CPU
    - SHUT_DOWN
    - START_UP
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0409
    """

    MIGRATES_TO_DIFFERENT_CPU = "M"
    """Migrates to different CPU"""
    SHUT_DOWN = "SD"
    """Shut down"""
    START_UP = "SU"
    """Start up"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ApplicationChangeType.MIGRATES_TO_DIFFERENT_CPU: "Migrates to different CPU",
    ApplicationChangeType.SHUT_DOWN: "Shut down",
    ApplicationChangeType.START_UP: "Start up",
}
