from ...base import HL7Table

"""
HL7 Version: 2.5.1
Certification status - 0337
Table Type: HL7
"""


class CertificationStatus(HL7Table):
    """
    Certification status - 0337 // HL7 table type
    - CERTIFIED
    - ELIGIBLE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0337
    """

    CERTIFIED = "C"
    """Certified"""
    ELIGIBLE = "E"
    """Eligible"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CertificationStatus.CERTIFIED: "Certified",
    CertificationStatus.ELIGIBLE: "Eligible",
}
