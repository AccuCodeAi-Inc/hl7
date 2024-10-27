from ...base import HL7Table

"""
HL7 Version: 2.5.1
Response level - 0179
Table Type: HL7
"""


class ResponseLevel(HL7Table):
    """
    Response level - 0179 // HL7 table type
    - ALWAYS_ALL_MFA_SEGMENTS
    - ERROR_OR_REJECT_CONDITIONS_ONLY_ONLY_MFA_SEGMENTS_DENOTING_ERRORS_MUST_BE_RETURNED_VIA_THE_APPLICATION_LEVEL_ACKNOWLEDGMENT_FOR_THIS_MESSAGE
    - NEVER_NO_APPLICATION_LEVEL_RESPONSE_NEEDED
    - SUCCESS_ONLY_MFA_SEGMENTS_DENOTING_SUCCESS_MUST_BE_RETURNED_VIA_THE_APPLICATION_LEVEL_ACKNOWLEDGMENT_FOR_THIS_MESSAGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0179
    """

    ALWAYS_ALL_MFA_SEGMENTS = "AL"
    """Always. All MFA segments (whether denoting errors or not) must be returned via the application-level acknowledgment message"""
    ERROR_OR_REJECT_CONDITIONS_ONLY_ONLY_MFA_SEGMENTS_DENOTING_ERRORS_MUST_BE_RETURNED_VIA_THE_APPLICATION_LEVEL_ACKNOWLEDGMENT_FOR_THIS_MESSAGE = "ER"
    """Error/Reject conditions only. Only MFA segments denoting errors must be returned via the application-level acknowledgment for this message"""
    NEVER_NO_APPLICATION_LEVEL_RESPONSE_NEEDED = "NE"
    """Never. No application-level response needed"""
    SUCCESS_ONLY_MFA_SEGMENTS_DENOTING_SUCCESS_MUST_BE_RETURNED_VIA_THE_APPLICATION_LEVEL_ACKNOWLEDGMENT_FOR_THIS_MESSAGE = "SU"
    """Success. Only MFA segments denoting success must be returned via the application-level acknowledgment for this message"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ResponseLevel.ALWAYS_ALL_MFA_SEGMENTS: "Always. All MFA segments (whether denoting errors or not) must be returned via the application-level acknowledgment message",
    ResponseLevel.ERROR_OR_REJECT_CONDITIONS_ONLY_ONLY_MFA_SEGMENTS_DENOTING_ERRORS_MUST_BE_RETURNED_VIA_THE_APPLICATION_LEVEL_ACKNOWLEDGMENT_FOR_THIS_MESSAGE: "Error/Reject conditions only. Only MFA segments denoting errors must be returned via the application-level acknowledgment for this message",
    ResponseLevel.NEVER_NO_APPLICATION_LEVEL_RESPONSE_NEEDED: "Never. No application-level response needed",
    ResponseLevel.SUCCESS_ONLY_MFA_SEGMENTS_DENOTING_SUCCESS_MUST_BE_RETURNED_VIA_THE_APPLICATION_LEVEL_ACKNOWLEDGMENT_FOR_THIS_MESSAGE: "Success. Only MFA segments denoting success must be returned via the application-level acknowledgment for this message",
}
