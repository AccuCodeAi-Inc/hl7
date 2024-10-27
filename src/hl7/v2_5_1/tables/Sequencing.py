from ...base import HL7Table

"""
HL7 Version: 2.5.1
Sequencing - 0397
Table Type: HL7
"""


class Sequencing(HL7Table):
    """
    Sequencing - 0397 // HL7 table type
    - ASCENDING
    - ASCENDING_CASE_INSENSITIVE
    - DESCENDING
    - DESCENDING_CASE_INSENSITIVE
    - NONE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0397
    """

    ASCENDING = "A"
    """Ascending"""
    ASCENDING_CASE_INSENSITIVE = "AN"
    """Ascending, case insensitive"""
    DESCENDING = "D"
    """Descending"""
    DESCENDING_CASE_INSENSITIVE = "DN"
    """Descending, case insensitive"""
    NONE = "N"
    """None"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Sequencing.ASCENDING: "Ascending",
    Sequencing.ASCENDING_CASE_INSENSITIVE: "Ascending, case insensitive",
    Sequencing.DESCENDING: "Descending",
    Sequencing.DESCENDING_CASE_INSENSITIVE: "Descending, case insensitive",
    Sequencing.NONE: "None",
}
