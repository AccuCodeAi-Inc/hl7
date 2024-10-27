from ...base import HL7Table

"""
HL7 Version: 2.5.1
Mode of Arrival Code - 0430
Table Type: User
"""


class ModeOfArrivalCode(HL7Table):
    """
    Mode of Arrival Code - 0430 // User table type
    - AMBULANCE
    - CAR
    - ON_FOOT
    - HELICOPTER
    - OTHER
    - PUBLIC_TRANSPORT
    - UNKNOWN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0430
    """

    AMBULANCE = "A"
    """Ambulance"""
    CAR = "C"
    """Car"""
    ON_FOOT = "F"
    """On foot"""
    HELICOPTER = "H"
    """Helicopter"""
    OTHER = "O"
    """Other"""
    PUBLIC_TRANSPORT = "P"
    """Public Transport"""
    UNKNOWN = "U"
    """Unknown"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ModeOfArrivalCode.AMBULANCE: "Ambulance",
    ModeOfArrivalCode.CAR: "Car",
    ModeOfArrivalCode.ON_FOOT: "On foot",
    ModeOfArrivalCode.HELICOPTER: "Helicopter",
    ModeOfArrivalCode.OTHER: "Other",
    ModeOfArrivalCode.PUBLIC_TRANSPORT: "Public Transport",
    ModeOfArrivalCode.UNKNOWN: "Unknown",
}
