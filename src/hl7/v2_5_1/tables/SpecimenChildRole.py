from ...base import HL7Table

"""
HL7 Version: 2.5.1
Specimen Child Role - 0494
Table Type: HL7
"""


class SpecimenChildRole(HL7Table):
    """
    Specimen Child Role - 0494 // HL7 table type
    - ALIQUOT
    - COMPONENT
    - MODIFIED_FROM_ORIGINAL_SPECIMEN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0494
    """

    ALIQUOT = "A"
    """Aliquot"""
    COMPONENT = "C"
    """Component"""
    MODIFIED_FROM_ORIGINAL_SPECIMEN = "M"
    """Modified from original specimen"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SpecimenChildRole.ALIQUOT: "Aliquot",
    SpecimenChildRole.COMPONENT: "Component",
    SpecimenChildRole.MODIFIED_FROM_ORIGINAL_SPECIMEN: "Modified from original specimen",
}
