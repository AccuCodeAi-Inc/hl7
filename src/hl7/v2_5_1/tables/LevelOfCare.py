from ...base import HL7Table

"""
HL7 Version: 2.5.1
Level of Care - 0263
Table Type: User
"""


class LevelOfCare(HL7Table):
    """
    Level of Care - 0263 // User table type
    - AMBULATORY
    - CRITICAL_CARE
    - EMERGENCY
    - ISOLATION
    - INTENSIVE_CARE
    - ROUTINE
    - SURGERY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0263
    """

    AMBULATORY = "A"
    """Ambulatory"""
    CRITICAL_CARE = "C"
    """Critical care"""
    EMERGENCY = "E"
    """Emergency"""
    ISOLATION = "F"
    """Isolation"""
    INTENSIVE_CARE = "N"
    """Intensive care"""
    ROUTINE = "R"
    """Routine"""
    SURGERY = "S"
    """Surgery"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LevelOfCare.AMBULATORY: "Ambulatory",
    LevelOfCare.CRITICAL_CARE: "Critical care",
    LevelOfCare.EMERGENCY: "Emergency",
    LevelOfCare.ISOLATION: "Isolation",
    LevelOfCare.INTENSIVE_CARE: "Intensive care",
    LevelOfCare.ROUTINE: "Routine",
    LevelOfCare.SURGERY: "Surgery",
}
