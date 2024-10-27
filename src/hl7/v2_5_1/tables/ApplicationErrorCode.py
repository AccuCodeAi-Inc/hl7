"""
HL7 Version: 2.5.1
Application error code - 0533
Table Type: User
"""


class ApplicationErrorCode(str):
    """
    Application error code - 0533 // User table type
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0533
    User Defined Tables - Tables with data suggested by HL7 organization.
    Most table are customized to reflect system workflows and coded values (such as lab values).
    There are no suggested values for this table."""

    @property
    def description(self) -> str:
        return self
