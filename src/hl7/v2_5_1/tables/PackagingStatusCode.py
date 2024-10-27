from ...base import HL7Table

"""
HL7 Version: 2.5.1
Packaging Status Code - 0469
Table Type: User
"""


class PackagingStatusCode(HL7Table):
    """
    Packaging Status Code - 0469 // User table type
    - NOT_PACKAGED
    - PACKAGED_SERVICE
    - PACKAGED_AS_PART_OF_PARTIAL_HOSPITALIZATION_PER_DIEM_OR_DAILY_MENTAL_HEALTH_SERVICE_PER_DIEM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0469
    """

    NOT_PACKAGED = "0"
    """Not packaged"""
    PACKAGED_SERVICE = "1"
    """Packaged service (status indicator N, or no HCPCS code and certain revenue codes)"""
    PACKAGED_AS_PART_OF_PARTIAL_HOSPITALIZATION_PER_DIEM_OR_DAILY_MENTAL_HEALTH_SERVICE_PER_DIEM = "2"
    """Packaged as part of partial hospitalization per diem or daily mental health service per diem"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    PackagingStatusCode.NOT_PACKAGED: "Not packaged",
    PackagingStatusCode.PACKAGED_SERVICE: "Packaged service (status indicator N, or no HCPCS code and certain revenue codes)",
    PackagingStatusCode.PACKAGED_AS_PART_OF_PARTIAL_HOSPITALIZATION_PER_DIEM_OR_DAILY_MENTAL_HEALTH_SERVICE_PER_DIEM: "Packaged as part of partial hospitalization per diem or daily mental health service per diem",
}
