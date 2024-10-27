from ...base import HL7Table

"""
HL7 Version: 2.5.1
Military Service - 0140
Table Type: User
"""


class MilitaryService(HL7Table):
    """
    Military Service - 0140 // User table type
    - AUSTRALIAN_ARMY
    - AUSTRALIAN_AIR_FORCE
    - AUSTRALIAN_NAVY
    - NORTH_ATLANTIC_TREATY_ORGANIZATION
    - NATIONAL_OCEANIC_AND_ATMOSPHERIC_ADMINISTRATION
    - US_ARMY
    - US_AIR_FORCE
    - US_COAST_GUARD
    - US_MARINE_CORPS
    - US_NAVY
    - US_PUBLIC_HEALTH_SERVICE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0140
    """

    AUSTRALIAN_ARMY = "AUSA"
    """Australian Army"""
    AUSTRALIAN_AIR_FORCE = "AUSAF"
    """Australian Air Force"""
    AUSTRALIAN_NAVY = "AUSN"
    """Australian Navy"""
    NORTH_ATLANTIC_TREATY_ORGANIZATION = "NATO"
    """North Atlantic Treaty Organization"""
    NATIONAL_OCEANIC_AND_ATMOSPHERIC_ADMINISTRATION = "NOAA"
    """National Oceanic and Atmospheric Administration"""
    US_ARMY = "USA"
    """US Army"""
    US_AIR_FORCE = "USAF"
    """US Air Force"""
    US_COAST_GUARD = "USCG"
    """US Coast Guard"""
    US_MARINE_CORPS = "USMC"
    """US Marine Corps"""
    US_NAVY = "USN"
    """US Navy"""
    US_PUBLIC_HEALTH_SERVICE = "USPHS"
    """US Public Health Service"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MilitaryService.AUSTRALIAN_ARMY: "Australian Army",
    MilitaryService.AUSTRALIAN_AIR_FORCE: "Australian Air Force",
    MilitaryService.AUSTRALIAN_NAVY: "Australian Navy",
    MilitaryService.NORTH_ATLANTIC_TREATY_ORGANIZATION: "North Atlantic Treaty Organization",
    MilitaryService.NATIONAL_OCEANIC_AND_ATMOSPHERIC_ADMINISTRATION: "National Oceanic and Atmospheric Administration",
    MilitaryService.US_ARMY: "US Army",
    MilitaryService.US_AIR_FORCE: "US Air Force",
    MilitaryService.US_COAST_GUARD: "US Coast Guard",
    MilitaryService.US_MARINE_CORPS: "US Marine Corps",
    MilitaryService.US_NAVY: "US Navy",
    MilitaryService.US_PUBLIC_HEALTH_SERVICE: "US Public Health Service",
}
