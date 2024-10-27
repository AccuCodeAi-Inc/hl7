"""
HL7 Version: 2.5.1
Department Cost Center - 0319
Table Type: User
"""


class DepartmentCostCenter(str):
    """
    Department Cost Center - 0319 // User table type
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0319
    User Defined Tables - Tables with data suggested by HL7 organization.
    Most table are customized to reflect system workflows and coded values (such as lab values).
    There are no suggested values for this table."""

    @property
    def description(self) -> str:
        return self
