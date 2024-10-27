from ...base import HL7Table

"""
HL7 Version: 2.5.1
System induced contaminants - 0374
Table Type: User
"""


class SystemInducedContaminants(HL7Table):
    """
    System induced contaminants - 0374 // User table type
    - PRESENT_TYPE_OF_CONTAMINATION_UNSPECIFIED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0374
    """

    PRESENT_TYPE_OF_CONTAMINATION_UNSPECIFIED = "CNTM"
    """Present, type of contamination unspecified"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SystemInducedContaminants.PRESENT_TYPE_OF_CONTAMINATION_UNSPECIFIED: "Present, type of contamination unspecified",
}
