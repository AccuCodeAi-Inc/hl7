from ...base import HL7Table

"""
HL7 Version: 2.5.1
Location Service Code - 0442
Table Type: User
"""


class LocationServiceCode(HL7Table):
    """
    Location Service Code - 0442 // User table type
    - DIAGNOSTIC
    - EMERGENCY_ROOM_CASUALTY
    - PRIMARY_CARE
    - THERAPEUTIC
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0442
    """

    DIAGNOSTIC = "D"
    """Diagnostic"""
    EMERGENCY_ROOM_CASUALTY = "E"
    """Emergency Room Casualty"""
    PRIMARY_CARE = "P"
    """Primary Care"""
    THERAPEUTIC = "T"
    """Therapeutic"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LocationServiceCode.DIAGNOSTIC: "Diagnostic",
    LocationServiceCode.EMERGENCY_ROOM_CASUALTY: "Emergency Room Casualty",
    LocationServiceCode.PRIMARY_CARE: "Primary Care",
    LocationServiceCode.THERAPEUTIC: "Therapeutic",
}
