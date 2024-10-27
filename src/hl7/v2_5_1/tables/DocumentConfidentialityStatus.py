from ...base import HL7Table

"""
HL7 Version: 2.5.1
Document Confidentiality Status - 0272
Table Type: HL7
"""


class DocumentConfidentialityStatus(HL7Table):
    """
    Document Confidentiality Status - 0272 // HL7 table type
    - RESTRICTED
    - USUAL_CONTROL
    - VERY_RESTRICTED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0272
    """

    RESTRICTED = "R"
    """Restricted"""
    USUAL_CONTROL = "U"
    """Usual control"""
    VERY_RESTRICTED = "V"
    """Very restricted"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    DocumentConfidentialityStatus.RESTRICTED: "Restricted",
    DocumentConfidentialityStatus.USUAL_CONTROL: "Usual control",
    DocumentConfidentialityStatus.VERY_RESTRICTED: "Very restricted",
}
