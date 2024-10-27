from ...base import HL7Table

"""
HL7 Version: 2.5.1
Room type - 0145
Table Type: User
"""


class RoomType(HL7Table):
    """
    Room type - 0145 // User table type
    - SECOND_INTENSIVE_CARE_UNIT
    - SECOND_PRIVATE_ROOM
    - SECOND_SEMI_PRIVATE_ROOM
    - INTENSIVE_CARE_UNIT
    - PRIVATE_ROOM
    - SEMI_PRIVATE_ROOM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0145
    """

    SECOND_INTENSIVE_CARE_UNIT = "2ICU"
    """Second intensive care unit"""
    SECOND_PRIVATE_ROOM = "2PRI"
    """Second private room"""
    SECOND_SEMI_PRIVATE_ROOM = "2SPR"
    """Second semi-private room"""
    INTENSIVE_CARE_UNIT = "ICU"
    """Intensive care unit"""
    PRIVATE_ROOM = "PRI"
    """Private room"""
    SEMI_PRIVATE_ROOM = "SPR"
    """Semi-private room"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RoomType.SECOND_INTENSIVE_CARE_UNIT: "Second intensive care unit",
    RoomType.SECOND_PRIVATE_ROOM: "Second private room",
    RoomType.SECOND_SEMI_PRIVATE_ROOM: "Second semi-private room",
    RoomType.INTENSIVE_CARE_UNIT: "Intensive care unit",
    RoomType.PRIVATE_ROOM: "Private room",
    RoomType.SEMI_PRIVATE_ROOM: "Semi-private room",
}
