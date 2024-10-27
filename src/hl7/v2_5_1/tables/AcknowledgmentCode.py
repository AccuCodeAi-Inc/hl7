from ...base import HL7Table

"""
HL7 Version: 2.5.1
Acknowledgment code - 0008
Table Type: HL7
"""


class AcknowledgmentCode(HL7Table):
    """
    Acknowledgment code - 0008 // HL7 table type
    - ORIGINAL_MODE_APPLICATION_ACCEPT_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_ACCEPT
    - ORIGINAL_MODE_APPLICATION_ERROR_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_ERROR
    - ORIGINAL_MODE_APPLICATION_REJECT_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_REJECT
    - ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_ACCEPT
    - ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_ERROR
    - ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_REJECT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0008
    """

    ORIGINAL_MODE_APPLICATION_ACCEPT_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_ACCEPT = (
        "AA"
    )
    """Original mode: Application Accept - Enhanced mode: Application acknowledgment: Accept"""
    ORIGINAL_MODE_APPLICATION_ERROR_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_ERROR = (
        "AE"
    )
    """Original mode: Application Error - Enhanced mode: Application acknowledgment: Error"""
    ORIGINAL_MODE_APPLICATION_REJECT_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_REJECT = (
        "AR"
    )
    """Original mode: Application Reject - Enhanced mode: Application acknowledgment: Reject"""
    ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_ACCEPT = "CA"
    """Enhanced mode: Accept acknowledgment: Commit Accept"""
    ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_ERROR = "CE"
    """Enhanced mode: Accept acknowledgment: Commit Error"""
    ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_REJECT = "CR"
    """Enhanced mode: Accept acknowledgment: Commit Reject"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AcknowledgmentCode.ORIGINAL_MODE_APPLICATION_ACCEPT_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_ACCEPT: "Original mode: Application Accept - Enhanced mode: Application acknowledgment: Accept",
    AcknowledgmentCode.ORIGINAL_MODE_APPLICATION_ERROR_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_ERROR: "Original mode: Application Error - Enhanced mode: Application acknowledgment: Error",
    AcknowledgmentCode.ORIGINAL_MODE_APPLICATION_REJECT_ENHANCED_MODE_APPLICATION_ACKNOWLEDGMENT_REJECT: "Original mode: Application Reject - Enhanced mode: Application acknowledgment: Reject",
    AcknowledgmentCode.ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_ACCEPT: "Enhanced mode: Accept acknowledgment: Commit Accept",
    AcknowledgmentCode.ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_ERROR: "Enhanced mode: Accept acknowledgment: Commit Error",
    AcknowledgmentCode.ENHANCED_MODE_ACCEPT_ACKNOWLEDGMENT_COMMIT_REJECT: "Enhanced mode: Accept acknowledgment: Commit Reject",
}
