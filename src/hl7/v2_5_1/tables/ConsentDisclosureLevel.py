from ...base import HL7Table

"""
HL7 Version: 2.5.1
Consent Disclosure Level - 0500
Table Type: HL7
"""


class ConsentDisclosureLevel(HL7Table):
    """
    Consent Disclosure Level - 0500 // HL7 table type
    - FULL_DISCLOSURE
    - NO_DISCLOSURE
    - PARTIAL_DISCLOSURE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0500
    """

    FULL_DISCLOSURE = "F"
    """Full Disclosure"""
    NO_DISCLOSURE = "N"
    """No Disclosure"""
    PARTIAL_DISCLOSURE = "P"
    """Partial Disclosure"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConsentDisclosureLevel.FULL_DISCLOSURE: "Full Disclosure",
    ConsentDisclosureLevel.NO_DISCLOSURE: "No Disclosure",
    ConsentDisclosureLevel.PARTIAL_DISCLOSURE: "Partial Disclosure",
}
