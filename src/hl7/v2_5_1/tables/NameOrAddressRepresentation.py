from ...base import HL7Table

"""
HL7 Version: 2.5.1
Name/address representation - 0465
Table Type: HL7
"""


class NameOrAddressRepresentation(HL7Table):
    """
    Name/address representation - 0465 // HL7 table type
    - ALPHABETIC
    - IDEOGRAPHIC
    - PHONETIC
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0465
    """

    ALPHABETIC = "A"
    """Alphabetic (i.e., Default or some single-byte)"""
    IDEOGRAPHIC = "I"
    """Ideographic (i.e., Kanji)"""
    PHONETIC = "P"
    """Phonetic (i.e., ASCII, Katakana, Hiragana, etc.)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NameOrAddressRepresentation.ALPHABETIC: "Alphabetic (i.e., Default or some single-byte)",
    NameOrAddressRepresentation.IDEOGRAPHIC: "Ideographic (i.e., Kanji)",
    NameOrAddressRepresentation.PHONETIC: "Phonetic (i.e., ASCII, Katakana, Hiragana, etc.)",
}
