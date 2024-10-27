from __future__ import annotations
from ...base import HL7Table

"""
HL7 Version: 2.5.1
Yes/no indicator - 0136
Table Type: HL7
"""


class YesOrNoIndicator(HL7Table):
    """
    Yes/no indicator - 0136 // HL7 table type
    - NO
    - YES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0136
    """

    NO = "N"
    """No"""
    YES = "Y"
    """Yes"""

    @property
    def description(self) -> str:
        return _desc[self]

    @classmethod
    def from_bool(cls, x: bool) -> YesOrNoIndicator:
        """
        - True: YES
        - False: NO
        """
        return YesOrNoIndicator.YES if x else YesOrNoIndicator.NO


_desc = {
    YesOrNoIndicator.NO: "No",
    YesOrNoIndicator.YES: "Yes",
}
