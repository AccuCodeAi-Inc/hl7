from ...base import HL7Table

"""
HL7 Version: 2.5.1
Location Relationship ID - 0325
Table Type: User
"""


class LocationRelationshipId(HL7Table):
    """
    Location Relationship ID - 0325 // User table type
    - LOCATION_ALIAS
    - NEAREST_DIETARY_LOCATION
    - NEAREST_LAB
    - SECOND_NEAREST_LAB
    - PARENT_LOCATION
    - NEAREST_PHARMACY
    - SECOND_NEAREST_PHARMACY
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0325
    """

    LOCATION_ALIAS = "ALI"
    """Location Alias(es)"""
    NEAREST_DIETARY_LOCATION = "DTY"
    """Nearest dietary location"""
    NEAREST_LAB = "LAB"
    """Nearest lab"""
    SECOND_NEAREST_LAB = "LB2"
    """Second nearest lab"""
    PARENT_LOCATION = "PAR"
    """Parent location"""
    NEAREST_PHARMACY = "RX"
    """Nearest pharmacy"""
    SECOND_NEAREST_PHARMACY = "RX2"
    """Second nearest pharmacy"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    LocationRelationshipId.LOCATION_ALIAS: "Location Alias(es)",
    LocationRelationshipId.NEAREST_DIETARY_LOCATION: "Nearest dietary location",
    LocationRelationshipId.NEAREST_LAB: "Nearest lab",
    LocationRelationshipId.SECOND_NEAREST_LAB: "Second nearest lab",
    LocationRelationshipId.PARENT_LOCATION: "Parent location",
    LocationRelationshipId.NEAREST_PHARMACY: "Nearest pharmacy",
    LocationRelationshipId.SECOND_NEAREST_PHARMACY: "Second nearest pharmacy",
}
