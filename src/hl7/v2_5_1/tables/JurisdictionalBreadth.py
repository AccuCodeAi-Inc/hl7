from ...base import HL7Table

"""
HL7 Version: 2.5.1
Jurisdictional Breadth - 0547
Table Type: User
"""


class JurisdictionalBreadth(HL7Table):
    """
    Jurisdictional Breadth - 0547 // User table type
    - COUNTY_OR_PARISH
    - COUNTRY
    - STATE_OR_PROVINCE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0547
    """

    COUNTY_OR_PARISH = "C"
    """County/Parish"""
    COUNTRY = "N"
    """Country"""
    STATE_OR_PROVINCE = "S"
    """State/Province"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    JurisdictionalBreadth.COUNTY_OR_PARISH: "County/Parish",
    JurisdictionalBreadth.COUNTRY: "Country",
    JurisdictionalBreadth.STATE_OR_PROVINCE: "State/Province",
}
