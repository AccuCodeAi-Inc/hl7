from ...base import HL7Table

"""
HL7 Version: 2.5.1
Query priority - 0091
Table Type: HL7
"""


class QueryPriority(HL7Table):
    """
    Query priority - 0091 // HL7 table type
    - DEFERRED
    - IMMEDIATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0091
    """

    DEFERRED = "D"
    """Deferred"""
    IMMEDIATE = "I"
    """Immediate"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    QueryPriority.DEFERRED: "Deferred",
    QueryPriority.IMMEDIATE: "Immediate",
}
