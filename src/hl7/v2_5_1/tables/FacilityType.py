from ...base import HL7Table

"""
HL7 Version: 2.5.1
Facility type - 0331
Table Type: HL7
"""


class FacilityType(HL7Table):
    """
    Facility type - 0331 // HL7 table type
    - AGENT_FOR_A_FOREIGN_MANUFACTURER
    - DISTRIBUTOR
    - MANUFACTURER
    - USER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0331
    """

    AGENT_FOR_A_FOREIGN_MANUFACTURER = "A"
    """Agent for a foreign manufacturer"""
    DISTRIBUTOR = "D"
    """Distributor"""
    MANUFACTURER = "M"
    """Manufacturer"""
    USER = "U"
    """User"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    FacilityType.AGENT_FOR_A_FOREIGN_MANUFACTURER: "Agent for a foreign manufacturer",
    FacilityType.DISTRIBUTOR: "Distributor",
    FacilityType.MANUFACTURER: "Manufacturer",
    FacilityType.USER: "User",
}
