"""
HL7 Version: 2.5.1
Specimen Type Modifier - 0541
Table Type: User
"""


class SpecimenTypeModifier(str):
    """
    Specimen Type Modifier - 0541 // User table type
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0541
    User Defined Tables - Tables with data suggested by HL7 organization.
    Most table are customized to reflect system workflows and coded values (such as lab values).
    There are no suggested values for this table."""

    @property
    def description(self) -> str:
        return self
