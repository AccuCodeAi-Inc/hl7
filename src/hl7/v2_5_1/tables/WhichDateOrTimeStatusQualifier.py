from ...base import HL7Table

"""
HL7 Version: 2.5.1
Which date/time status qualifier - 0157
Table Type: HL7
"""


class WhichDateOrTimeStatusQualifier(HL7Table):
    """
    Which date/time status qualifier - 0157 // HL7 table type
    - ANY_STATUS
    - CURRENT_FINAL_VALUE_WHETHER_FINAL_OR_CORRECTED
    - CORRECTED_ONLY
    - FINAL_ONLY
    - PRELIMINARY
    - REPORT_COMPLETION_DATE_OR_TIME
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0157
    """

    ANY_STATUS = "ANY"
    """Any status"""
    CURRENT_FINAL_VALUE_WHETHER_FINAL_OR_CORRECTED = "CFN"
    """Current final value, whether final or corrected"""
    CORRECTED_ONLY = "COR"
    """Corrected only (no final with corrections)"""
    FINAL_ONLY = "FIN"
    """Final only (no corrections)"""
    PRELIMINARY = "PRE"
    """Preliminary"""
    REPORT_COMPLETION_DATE_OR_TIME = "REP"
    """Report completion date/time"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    WhichDateOrTimeStatusQualifier.ANY_STATUS: "Any status",
    WhichDateOrTimeStatusQualifier.CURRENT_FINAL_VALUE_WHETHER_FINAL_OR_CORRECTED: "Current final value, whether final or corrected",
    WhichDateOrTimeStatusQualifier.CORRECTED_ONLY: "Corrected only (no final with corrections)",
    WhichDateOrTimeStatusQualifier.FINAL_ONLY: "Final only (no corrections)",
    WhichDateOrTimeStatusQualifier.PRELIMINARY: "Preliminary",
    WhichDateOrTimeStatusQualifier.REPORT_COMPLETION_DATE_OR_TIME: "Report completion date/time",
}
