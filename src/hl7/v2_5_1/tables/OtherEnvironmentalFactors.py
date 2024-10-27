from ...base import HL7Table

"""
HL7 Version: 2.5.1
Other environmental factors - 0377
Table Type: User
"""


class OtherEnvironmentalFactors(HL7Table):
    """
    Other environmental factors - 0377 // User table type
    - OPENED_CONTAINER_INDOOR_ATMOSPHERE_60_MINUTES_DURATION
    - OPENED_CONTAINER_ATMOSPHERE_AND_DURATION_UNSPECIFIED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0377
    """

    OPENED_CONTAINER_INDOOR_ATMOSPHERE_60_MINUTES_DURATION = "A60"
    """Opened container, indoor atmosphere, 60 minutes duration"""
    OPENED_CONTAINER_ATMOSPHERE_AND_DURATION_UNSPECIFIED = "ATM"
    """Opened container, atmosphere and duration unspecified"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OtherEnvironmentalFactors.OPENED_CONTAINER_INDOOR_ATMOSPHERE_60_MINUTES_DURATION: "Opened container, indoor atmosphere, 60 minutes duration",
    OtherEnvironmentalFactors.OPENED_CONTAINER_ATMOSPHERE_AND_DURATION_UNSPECIFIED: "Opened container, atmosphere and duration unspecified",
}
