from ...base import HL7Table

"""
HL7 Version: 2.5.1
Outlier Type - 0083
Table Type: User
"""


class OutlierType(HL7Table):
    """
    Outlier Type - 0083 // User table type
    - OUTLIER_COST
    - OUTLIER_DAYS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0083
    """

    OUTLIER_COST = "C"
    """Outlier cost"""
    OUTLIER_DAYS = "D"
    """Outlier days"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OutlierType.OUTLIER_COST: "Outlier cost",
    OutlierType.OUTLIER_DAYS: "Outlier days",
}
