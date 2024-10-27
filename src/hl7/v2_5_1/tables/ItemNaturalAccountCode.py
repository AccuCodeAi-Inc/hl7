"""
HL7 Version: 2.5.1
Item Natural Account Code - 0320
Table Type: User
"""


class ItemNaturalAccountCode(str):
    """
    Item Natural Account Code - 0320 // User table type
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0320
    User Defined Tables - Tables with data suggested by HL7 organization.
    Most table are customized to reflect system workflows and coded values (such as lab values).
    There are no suggested values for this table."""

    @property
    def description(self) -> str:
        return self
