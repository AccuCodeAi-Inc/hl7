from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen component - 0372
Table Type: User
"""


class SpecimenComponent(HL7Table):
    """
    Specimen component - 0372 // User table type
    - WHOLE_BLOOD_HOMOGENEOUS
    - WHOLE_BLOOD_SEPARATED
    - PLASMA_NOS
    - PLATELET_POOR_PLASMA
    - PLATELET_RICH_PLASMA
    - SEDIMENT
    - SERUM_NOS
    - SUPERNATANT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0372
    """

    WHOLE_BLOOD_HOMOGENEOUS = "BLD"
    """Whole blood, homogeneous"""
    WHOLE_BLOOD_SEPARATED = "BSEP"
    """Whole blood, separated"""
    PLASMA_NOS = "PLAS"
    """Plasma, NOS (not otherwise specified)"""
    PLATELET_POOR_PLASMA = "PPP"
    """Platelet poor plasma"""
    PLATELET_RICH_PLASMA = "PRP"
    """Platelet rich plasma"""
    SEDIMENT = "SED"
    """Sediment"""
    SERUM_NOS = "SER"
    """Serum, NOS (not otherwise specified)"""
    SUPERNATANT = "SUP"
    """Supernatant"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenComponent.WHOLE_BLOOD_HOMOGENEOUS: "Whole blood, homogeneous",
    SpecimenComponent.WHOLE_BLOOD_SEPARATED: "Whole blood, separated",
    SpecimenComponent.PLASMA_NOS: "Plasma, NOS (not otherwise specified)",
    SpecimenComponent.PLATELET_POOR_PLASMA: "Platelet poor plasma",
    SpecimenComponent.PLATELET_RICH_PLASMA: "Platelet rich plasma",
    SpecimenComponent.SEDIMENT: "Sediment",
    SpecimenComponent.SERUM_NOS: "Serum, NOS (not otherwise specified)",
    SpecimenComponent.SUPERNATANT: "Supernatant",
}
