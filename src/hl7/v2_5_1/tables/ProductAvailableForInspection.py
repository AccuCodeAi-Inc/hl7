"""
HL7 Version: 2.5.1
Product Available for Inspection - 0246
Table Type: User
"""


class ProductAvailableForInspection(str):
    """
    Product Available for Inspection - 0246 // User table type
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0246
    User Defined Tables - Tables with data suggested by HL7 organization.
    Most table are customized to reflect system workflows and coded values (such as lab values).
    There are no suggested values for this table."""

    @property
    def description(self) -> str:
        return self
