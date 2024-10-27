from ...base import HL7Table

"""
HL7 Version: 2.5.1
Bed Status - 0116
Table Type: User
"""


class BedStatus(HL7Table):
    """
    Bed Status - 0116 // User table type
    - CLOSED
    - HOUSEKEEPING
    - ISOLATED
    - CONTAMINATED
    - OCCUPIED
    - UNOCCUPIED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0116
    """

    CLOSED = "C"
    """Closed"""
    HOUSEKEEPING = "H"
    """Housekeeping"""
    ISOLATED = "I"
    """Isolated"""
    CONTAMINATED = "K"
    """Contaminated"""
    OCCUPIED = "O"
    """Occupied"""
    UNOCCUPIED = "U"
    """Unoccupied"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    BedStatus.CLOSED: "Closed",
    BedStatus.HOUSEKEEPING: "Housekeeping",
    BedStatus.ISOLATED: "Isolated",
    BedStatus.CONTAMINATED: "Contaminated",
    BedStatus.OCCUPIED: "Occupied",
    BedStatus.UNOCCUPIED: "Unoccupied",
}
