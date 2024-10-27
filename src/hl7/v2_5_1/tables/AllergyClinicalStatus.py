from ...base import HL7Table

"""
HL7 Version: 2.5.1
Allergy Clinical Status - 0438
Table Type: User
"""


class AllergyClinicalStatus(HL7Table):
    """
    Allergy Clinical Status - 0438 // User table type
    - CONFIRMED_OR_VERIFIED
    - DOUBT_RAISED
    - ERRONEOUS
    - CONFIRMED_BUT_INACTIVE
    - PENDING
    - SUSPECT
    - UNCONFIRMED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0438
    """

    CONFIRMED_OR_VERIFIED = "C"
    """Confirmed or verified"""
    DOUBT_RAISED = "D"
    """Doubt raised"""
    ERRONEOUS = "E"
    """Erroneous"""
    CONFIRMED_BUT_INACTIVE = "I"
    """Confirmed but inactive"""
    PENDING = "P"
    """Pending"""
    SUSPECT = "S"
    """Suspect"""
    UNCONFIRMED = "U"
    """Unconfirmed"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AllergyClinicalStatus.CONFIRMED_OR_VERIFIED: "Confirmed or verified",
    AllergyClinicalStatus.DOUBT_RAISED: "Doubt raised",
    AllergyClinicalStatus.ERRONEOUS: "Erroneous",
    AllergyClinicalStatus.CONFIRMED_BUT_INACTIVE: "Confirmed but inactive",
    AllergyClinicalStatus.PENDING: "Pending",
    AllergyClinicalStatus.SUSPECT: "Suspect",
    AllergyClinicalStatus.UNCONFIRMED: "Unconfirmed",
}
