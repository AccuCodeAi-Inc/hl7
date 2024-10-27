from ...base import HL7Table

"""
HL7 Version: 2.5.1
Visit Indicator - 0326
Table Type: User
"""


class VisitIndicator(HL7Table):
    """
    Visit Indicator - 0326 // User table type
    - ACCOUNT_LEVEL
    - VISIT_LEVEL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0326
    """

    ACCOUNT_LEVEL = "A"
    """Account level (default)"""
    VISIT_LEVEL = "V"
    """Visit level"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    VisitIndicator.ACCOUNT_LEVEL: "Account level (default)",
    VisitIndicator.VISIT_LEVEL: "Visit level",
}
