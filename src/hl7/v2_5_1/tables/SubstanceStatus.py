from ...base import HL7Table

"""
HL7 Version: 2.5.1
Substance status - 0383
Table Type: HL7
"""


class SubstanceStatus(HL7Table):
    """
    Substance status - 0383 // HL7 table type
    - CALIBRATION_ERROR
    - CALIBRATION_WARNING
    - EXPIRED_ERROR
    - EXPIRED_WARNING
    - NOT_AVAILABLE_ERROR
    - NOT_AVAILABLE_WARNING
    - OTHER_ERROR
    - OK_STATUS
    - OTHER_WARNING
    - QC_ERROR
    - QC_WARNING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0383
    """

    CALIBRATION_ERROR = "CE"
    """Calibration Error"""
    CALIBRATION_WARNING = "CW"
    """Calibration Warning"""
    EXPIRED_ERROR = "EE"
    """Expired Error"""
    EXPIRED_WARNING = "EW"
    """Expired Warning"""
    NOT_AVAILABLE_ERROR = "NE"
    """Not Available Error"""
    NOT_AVAILABLE_WARNING = "NW"
    """Not Available Warning"""
    OTHER_ERROR = "OE"
    """Other Error"""
    OK_STATUS = "OK"
    """OK Status"""
    OTHER_WARNING = "OW"
    """Other Warning"""
    QC_ERROR = "QE"
    """QC Error"""
    QC_WARNING = "QW"
    """QC Warning"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SubstanceStatus.CALIBRATION_ERROR: "Calibration Error",
    SubstanceStatus.CALIBRATION_WARNING: "Calibration Warning",
    SubstanceStatus.EXPIRED_ERROR: "Expired Error",
    SubstanceStatus.EXPIRED_WARNING: "Expired Warning",
    SubstanceStatus.NOT_AVAILABLE_ERROR: "Not Available Error",
    SubstanceStatus.NOT_AVAILABLE_WARNING: "Not Available Warning",
    SubstanceStatus.OTHER_ERROR: "Other Error",
    SubstanceStatus.OK_STATUS: "OK Status",
    SubstanceStatus.OTHER_WARNING: "Other Warning",
    SubstanceStatus.QC_ERROR: "QC Error",
    SubstanceStatus.QC_WARNING: "QC Warning",
}
