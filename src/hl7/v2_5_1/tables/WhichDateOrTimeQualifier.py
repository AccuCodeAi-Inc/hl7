from ...base import HL7Table

"""
HL7 Version: 2.5.1
Which date/time qualifier - 0156
Table Type: HL7
"""


class WhichDateOrTimeQualifier(HL7Table):
    """
    Which date/time qualifier - 0156 // HL7 table type
    - ANY_DATE_OR_TIME_WITHIN_A_RANGE
    - COLLECTION_DATE_OR_TIME_EQUIVALENT_TO_FILM_OR_SAMPLE_COLLECTION_DATE_OR_TIME
    - ORDER_DATE_OR_TIME
    - SPECIMEN_RECEIPT_DATE_OR_TIME_RECEIPT_OF_SPECIMEN_IN_FILLING_ANCILLARY
    - REPORT_DATE_OR_TIME_REPORT_DATE_OR_TIME_AT_FILING_ANCILLARY
    - SCHEDULE_DATE_OR_TIME
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0156
    """

    ANY_DATE_OR_TIME_WITHIN_A_RANGE = "ANY"
    """Any date/time within a range"""
    COLLECTION_DATE_OR_TIME_EQUIVALENT_TO_FILM_OR_SAMPLE_COLLECTION_DATE_OR_TIME = "COL"
    """Collection date/time, equivalent to film or sample collection date/time"""
    ORDER_DATE_OR_TIME = "ORD"
    """Order date/time"""
    SPECIMEN_RECEIPT_DATE_OR_TIME_RECEIPT_OF_SPECIMEN_IN_FILLING_ANCILLARY = "RCT"
    """Specimen receipt date/time, receipt of specimen in filling ancillary (Lab)"""
    REPORT_DATE_OR_TIME_REPORT_DATE_OR_TIME_AT_FILING_ANCILLARY = "REP"
    """Report date/time, report date/time at filing ancillary (i.e., Lab)"""
    SCHEDULE_DATE_OR_TIME = "SCHED"
    """Schedule date/time"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    WhichDateOrTimeQualifier.ANY_DATE_OR_TIME_WITHIN_A_RANGE: "Any date/time within a range",
    WhichDateOrTimeQualifier.COLLECTION_DATE_OR_TIME_EQUIVALENT_TO_FILM_OR_SAMPLE_COLLECTION_DATE_OR_TIME: "Collection date/time, equivalent to film or sample collection date/time",
    WhichDateOrTimeQualifier.ORDER_DATE_OR_TIME: "Order date/time",
    WhichDateOrTimeQualifier.SPECIMEN_RECEIPT_DATE_OR_TIME_RECEIPT_OF_SPECIMEN_IN_FILLING_ANCILLARY: "Specimen receipt date/time, receipt of specimen in filling ancillary (Lab)",
    WhichDateOrTimeQualifier.REPORT_DATE_OR_TIME_REPORT_DATE_OR_TIME_AT_FILING_ANCILLARY: "Report date/time, report date/time at filing ancillary (i.e., Lab)",
    WhichDateOrTimeQualifier.SCHEDULE_DATE_OR_TIME: "Schedule date/time",
}
