from ...base import HL7Table

"""
HL7 Version: 2.5.1
Relationship modifier - 0258
Table Type: HL7
"""


class RelationshipModifier(HL7Table):
    """
    Relationship modifier - 0258 // HL7 table type
    - BLOOD_PRODUCT_UNIT
    - CONTROL
    - DONOR
    - PATIENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0258
    """

    BLOOD_PRODUCT_UNIT = "BPU"
    """Blood product unit"""
    CONTROL = "CONTROL"
    """Control"""
    DONOR = "DONOR"
    """Donor"""
    PATIENT = "PATIENT"
    """Patient"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RelationshipModifier.BLOOD_PRODUCT_UNIT: "Blood product unit",
    RelationshipModifier.CONTROL: "Control",
    RelationshipModifier.DONOR: "Donor",
    RelationshipModifier.PATIENT: "Patient",
}
