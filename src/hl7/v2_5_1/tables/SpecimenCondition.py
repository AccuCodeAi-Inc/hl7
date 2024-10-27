from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Condition - 0493
Table Type: User
"""


class SpecimenCondition(HL7Table):
    """
    Specimen Condition - 0493 // User table type
    - AUTOLYZED
    - CLOTTED
    - CONTAMINATED
    - COOL
    - FROZEN
    - HEMOLYZED
    - LIVE
    - ROOM_TEMPERATURE
    - SAMPLE_NOT_RECEIVED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0493
    """

    AUTOLYZED = "AUT"
    """Autolyzed"""
    CLOTTED = "CLOT"
    """Clotted"""
    CONTAMINATED = "CON"
    """Contaminated"""
    COOL = "COOL"
    """Cool"""
    FROZEN = "FROZ"
    """Frozen"""
    HEMOLYZED = "HEM"
    """Hemolyzed"""
    LIVE = "LIVE"
    """Live"""
    ROOM_TEMPERATURE = "ROOM"
    """Room temperature"""
    SAMPLE_NOT_RECEIVED = "SNR"
    """Sample not received"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenCondition.AUTOLYZED: "Autolyzed",
    SpecimenCondition.CLOTTED: "Clotted",
    SpecimenCondition.CONTAMINATED: "Contaminated",
    SpecimenCondition.COOL: "Cool",
    SpecimenCondition.FROZEN: "Frozen",
    SpecimenCondition.HEMOLYZED: "Hemolyzed",
    SpecimenCondition.LIVE: "Live",
    SpecimenCondition.ROOM_TEMPERATURE: "Room temperature",
    SpecimenCondition.SAMPLE_NOT_RECEIVED: "Sample not received",
}
