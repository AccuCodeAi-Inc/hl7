from ...base import HL7Table

"""
HL7 Version: 2.5.1
Consent Status - 0498
Table Type: HL7
"""


class ConsentStatus(HL7Table):
    """
    Consent Status - 0498 // HL7 table type
    - ACTIVE_CONSENT_HAS_BEEN_GRANTED
    - BYPASSED
    - LIMITED_CONSENT_HAS_BEEN_GRANTED_WITH_LIMITATIONS
    - PENDING_CONSENT_HAS_NOT_YET_BEEN_SOUGHT
    - REFUSED_CONSENT_HAS_BEEN_REFUSED
    - RESCINDED_CONSENT_WAS_INITIALLY_GRANTED_BUT_WAS_SUBSEQUENTLY_REVOKED_OR_ENDED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0498
    """

    ACTIVE_CONSENT_HAS_BEEN_GRANTED = "A"
    """Active - Consent has been granted"""
    BYPASSED = "B"
    """Bypassed (Consent not sought)"""
    LIMITED_CONSENT_HAS_BEEN_GRANTED_WITH_LIMITATIONS = "L"
    """Limited - Consent has been granted with limitations"""
    PENDING_CONSENT_HAS_NOT_YET_BEEN_SOUGHT = "P"
    """Pending - Consent has not yet been sought"""
    REFUSED_CONSENT_HAS_BEEN_REFUSED = "R"
    """Refused - Consent has been refused"""
    RESCINDED_CONSENT_WAS_INITIALLY_GRANTED_BUT_WAS_SUBSEQUENTLY_REVOKED_OR_ENDED = "X"
    """Rescinded - Consent was initially granted, but was subsequently revoked or ended."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConsentStatus.ACTIVE_CONSENT_HAS_BEEN_GRANTED: "Active - Consent has been granted",
    ConsentStatus.BYPASSED: "Bypassed (Consent not sought)",
    ConsentStatus.LIMITED_CONSENT_HAS_BEEN_GRANTED_WITH_LIMITATIONS: "Limited - Consent has been granted with limitations",
    ConsentStatus.PENDING_CONSENT_HAS_NOT_YET_BEEN_SOUGHT: "Pending - Consent has not yet been sought",
    ConsentStatus.REFUSED_CONSENT_HAS_BEEN_REFUSED: "Refused - Consent has been refused",
    ConsentStatus.RESCINDED_CONSENT_WAS_INITIALLY_GRANTED_BUT_WAS_SUBSEQUENTLY_REVOKED_OR_ENDED: "Rescinded - Consent was initially granted, but was subsequently revoked or ended.",
}
