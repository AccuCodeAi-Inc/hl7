from ...base import HL7Table

"""
HL7 Version: 2.5.1
Annotations - 0317
Table Type: User
"""


class Annotations(HL7Table):
    """
    Annotations - 0317 // User table type
    - PACE_SPIKE
    - SAS_MARKER
    - SENSE_MARKER
    - BEAT_MARKER
    - ETC
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0317
    """

    PACE_SPIKE = "9900"
    """Pace spike"""
    SAS_MARKER = "9901"
    """SAS marker"""
    SENSE_MARKER = "9902"
    """Sense marker"""
    BEAT_MARKER = "9903"
    """Beat marker"""
    ETC = "9904"
    """etc."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Annotations.PACE_SPIKE: "Pace spike",
    Annotations.SAS_MARKER: "SAS marker",
    Annotations.SENSE_MARKER: "Sense marker",
    Annotations.BEAT_MARKER: "Beat marker",
    Annotations.ETC: "etc.",
}
