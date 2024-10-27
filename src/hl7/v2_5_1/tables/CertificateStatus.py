from ...base import HL7Table

"""
HL7 Version: 2.5.1
Certificate Status - 0536
Table Type: User
"""


class CertificateStatus(HL7Table):
    """
    Certificate Status - 0536 // User table type
    - EXPIRED
    - INACTIVE
    - PROVISIONAL
    - REVOKED
    - ACTIVE_OR_VALID
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0536
    """

    EXPIRED = "E"
    """Expired"""
    INACTIVE = "I"
    """Inactive"""
    PROVISIONAL = "P"
    """Provisional"""
    REVOKED = "R"
    """Revoked"""
    ACTIVE_OR_VALID = "V"
    """Active/Valid"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CertificateStatus.EXPIRED: "Expired",
    CertificateStatus.INACTIVE: "Inactive",
    CertificateStatus.PROVISIONAL: "Provisional",
    CertificateStatus.REVOKED: "Revoked",
    CertificateStatus.ACTIVE_OR_VALID: "Active/Valid",
}
