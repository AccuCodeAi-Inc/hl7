"""
HL7 Version: 2.5.1
Cap type - 0381
Table Type: User
"""


class CapType(str):
    """
    Cap type - 0381 // User table type
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0381
    User Defined Tables - Tables with data suggested by HL7 organization.
    Most table are customized to reflect system workflows and coded values (such as lab values).
    There are no suggested values for this table."""

    @property
    def description(self) -> str:
        return self
