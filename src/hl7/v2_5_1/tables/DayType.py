from ...base import HL7Table

"""
HL7 Version: 2.5.1
Day type - 0149
Table Type: User
"""


class DayType(HL7Table):
    """
    Day type - 0149 // User table type
    - APPROVED
    - DENIED
    - PENDING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0149
    """

    APPROVED = "AP"
    """Approved"""
    DENIED = "DE"
    """Denied"""
    PENDING = "PE"
    """Pending"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DayType.APPROVED: "Approved",
    DayType.DENIED: "Denied",
    DayType.PENDING: "Pending",
}
