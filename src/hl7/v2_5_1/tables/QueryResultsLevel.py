from ...base import HL7Table

"""
HL7 Version: 2.5.1
Query results level - 0108
Table Type: HL7
"""


class QueryResultsLevel(HL7Table):
    """
    Query results level - 0108 // HL7 table type
    - ORDER_PLUS_ORDER_STATUS
    - RESULTS_WITHOUT_BULK_TEXT
    - STATUS_ONLY
    - FULL_RESULTS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0108
    """

    ORDER_PLUS_ORDER_STATUS = "O"
    """Order plus order status"""
    RESULTS_WITHOUT_BULK_TEXT = "R"
    """Results without bulk text"""
    STATUS_ONLY = "S"
    """Status only"""
    FULL_RESULTS = "T"
    """Full results"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    QueryResultsLevel.ORDER_PLUS_ORDER_STATUS: "Order plus order status",
    QueryResultsLevel.RESULTS_WITHOUT_BULK_TEXT: "Results without bulk text",
    QueryResultsLevel.STATUS_ONLY: "Status only",
    QueryResultsLevel.FULL_RESULTS: "Full results",
}
