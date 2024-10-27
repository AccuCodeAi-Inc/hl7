from ...base import HL7Table

"""
HL7 Version: 2.5.1
Report timing - 0234
Table Type: HL7
"""


class ReportTiming(HL7Table):
    """
    Report timing - 0234 // HL7 table type
    - _10_DAY_REPORT
    - _15_DAY_REPORT
    - _30_DAY_REPORT
    - _3_DAY_REPORT
    - _7_DAY_REPORT
    - ADDITIONAL_INFORMATION
    - CORRECTION
    - DEVICE_EVALUATION
    - PERIODIC
    - REQUESTED_INFORMATION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0234
    """

    _10_DAY_REPORT = "10D"
    """10 day report"""
    _15_DAY_REPORT = "15D"
    """15 day report"""
    _30_DAY_REPORT = "30D"
    """30 day report"""
    _3_DAY_REPORT = "3D"
    """3 day report"""
    _7_DAY_REPORT = "7D"
    """7 day report"""
    ADDITIONAL_INFORMATION = "AD"
    """Additional information"""
    CORRECTION = "CO"
    """Correction"""
    DEVICE_EVALUATION = "DE"
    """Device evaluation"""
    PERIODIC = "PD"
    """Periodic"""
    REQUESTED_INFORMATION = "RQ"
    """Requested information"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReportTiming._10_DAY_REPORT: "10 day report",
    ReportTiming._15_DAY_REPORT: "15 day report",
    ReportTiming._30_DAY_REPORT: "30 day report",
    ReportTiming._3_DAY_REPORT: "3 day report",
    ReportTiming._7_DAY_REPORT: "7 day report",
    ReportTiming.ADDITIONAL_INFORMATION: "Additional information",
    ReportTiming.CORRECTION: "Correction",
    ReportTiming.DEVICE_EVALUATION: "Device evaluation",
    ReportTiming.PERIODIC: "Periodic",
    ReportTiming.REQUESTED_INFORMATION: "Requested information",
}
