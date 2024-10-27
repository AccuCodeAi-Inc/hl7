from ...base import HL7Table

"""
HL7 Version: 2.5.1
Modify indicator - 0395
Table Type: HL7
"""


class ModifyIndicator(HL7Table):
    """
    Modify indicator - 0395 // HL7 table type
    - MODIFIED_SUBSCRIPTION
    - NEW_SUBSCRIPTION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0395
    """

    MODIFIED_SUBSCRIPTION = "M"
    """Modified Subscription"""
    NEW_SUBSCRIPTION = "N"
    """New Subscription"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ModifyIndicator.MODIFIED_SUBSCRIPTION: "Modified Subscription",
    ModifyIndicator.NEW_SUBSCRIPTION: "New Subscription",
}
