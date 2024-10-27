from ...base import HL7Table

"""
HL7 Version: 2.5.1
Consent Mode - 0497
Table Type: HL7
"""


class ConsentMode(HL7Table):
    """
    Consent Mode - 0497 // HL7 table type
    - TELEPHONE
    - VERBAL
    - WRITTEN
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0497
    """

    TELEPHONE = "T"
    """Telephone"""
    VERBAL = "V"
    """Verbal"""
    WRITTEN = "W"
    """Written"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ConsentMode.TELEPHONE: "Telephone",
    ConsentMode.VERBAL: "Verbal",
    ConsentMode.WRITTEN: "Written",
}
