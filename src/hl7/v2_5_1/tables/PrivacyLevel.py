from ...base import HL7Table

"""
HL7 Version: 2.5.1
Privacy Level - 0262
Table Type: User
"""


class PrivacyLevel(HL7Table):
    """
    Privacy Level - 0262 // User table type
    - ISOLATION
    - PRIVATE_ROOM_MEDICALLY_JUSTIFIED
    - PRIVATE_ROOM
    - PRIVATE_ROOM_DUE_TO_OVERFLOW
    - SEMI_PRIVATE_ROOM
    - WARD
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0262
    """

    ISOLATION = "F"
    """Isolation"""
    PRIVATE_ROOM_MEDICALLY_JUSTIFIED = "J"
    """Private room - medically justified"""
    PRIVATE_ROOM = "P"
    """Private room"""
    PRIVATE_ROOM_DUE_TO_OVERFLOW = "Q"
    """Private room - due to overflow"""
    SEMI_PRIVATE_ROOM = "S"
    """Semi-private room"""
    WARD = "W"
    """Ward"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PrivacyLevel.ISOLATION: "Isolation",
    PrivacyLevel.PRIVATE_ROOM_MEDICALLY_JUSTIFIED: "Private room - medically justified",
    PrivacyLevel.PRIVATE_ROOM: "Private room",
    PrivacyLevel.PRIVATE_ROOM_DUE_TO_OVERFLOW: "Private room - due to overflow",
    PrivacyLevel.SEMI_PRIVATE_ROOM: "Semi-private room",
    PrivacyLevel.WARD: "Ward",
}
