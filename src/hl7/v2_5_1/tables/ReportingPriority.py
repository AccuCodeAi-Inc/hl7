from ...base import HL7Table

"""
HL7 Version: 2.5.1
Reporting priority - 0169
Table Type: HL7
"""


class ReportingPriority(HL7Table):
    """
    Reporting priority - 0169 // HL7 table type
    - CALL_BACK_RESULTS
    - RUSH_REPORTING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0169
    """

    CALL_BACK_RESULTS = "C"
    """Call back results"""
    RUSH_REPORTING = "R"
    """Rush reporting"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReportingPriority.CALL_BACK_RESULTS: "Call back results",
    ReportingPriority.RUSH_REPORTING: "Rush reporting",
}
