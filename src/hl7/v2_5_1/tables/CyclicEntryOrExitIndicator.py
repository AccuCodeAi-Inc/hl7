from ...base import HL7Table

"""
HL7 Version: 2.5.1
Cyclic Entry/Exit Indicator - 0505
Table Type: HL7
"""


class CyclicEntryOrExitIndicator(HL7Table):
    """
    Cyclic Entry/Exit Indicator - 0505 // HL7 table type
    - THE_LAST_SERVICE_REQUEST_IN_A_CYCLIC_GROUP
    - THE_FIRST_SERVICE_REQUEST_IN_A_CYCLIC_GROUP
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0505
    """

    THE_LAST_SERVICE_REQUEST_IN_A_CYCLIC_GROUP = "#"
    """The last service request in a cyclic group."""
    THE_FIRST_SERVICE_REQUEST_IN_A_CYCLIC_GROUP = "*"
    """The first service request in a cyclic group"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CyclicEntryOrExitIndicator.THE_LAST_SERVICE_REQUEST_IN_A_CYCLIC_GROUP: "The last service request in a cyclic group.",
    CyclicEntryOrExitIndicator.THE_FIRST_SERVICE_REQUEST_IN_A_CYCLIC_GROUP: "The first service request in a cyclic group",
}
