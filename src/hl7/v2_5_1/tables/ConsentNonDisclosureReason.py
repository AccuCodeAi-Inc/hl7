from ...base import HL7Table

"""
HL7 Version: 2.5.1
Consent Non-Disclosure Reason - 0501
Table Type: User
"""


class ConsentNonDisclosureReason(HL7Table):
    """
    Consent Non-Disclosure Reason - 0501 // User table type
    - EMERGENCY
    - PATIENT_REQUEST
    - RX_PRIVATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0501
    """

    EMERGENCY = "E"
    """Emergency"""
    PATIENT_REQUEST = "PR"
    """Patient Request"""
    RX_PRIVATE = "RX"
    """Rx Private"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConsentNonDisclosureReason.EMERGENCY: "Emergency",
    ConsentNonDisclosureReason.PATIENT_REQUEST: "Patient Request",
    ConsentNonDisclosureReason.RX_PRIVATE: "Rx Private",
}
