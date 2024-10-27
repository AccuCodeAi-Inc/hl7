from ...base import HL7Table

"""
HL7 Version: 2.5.1
Encoding - 0299
Table Type: HL7
"""


class Encoding(HL7Table):
    """
    Encoding - 0299 // HL7 table type
    - NO_ENCODING_DATA_ARE_DISPLAYABLE_ASCII_CHARACTERS
    - ENCODING_AS_DEFINED_BY_MIME
    - HEXADECIMAL_ENCODING_CONSECUTIVE_PAIRS_OF_HEXADECIMAL_DIGITS_REPRESENT_CONSECUTIVE_SINGLE_OCTETS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0299
    """

    NO_ENCODING_DATA_ARE_DISPLAYABLE_ASCII_CHARACTERS = "A"
    """No encoding - data are displayable ASCII characters."""
    ENCODING_AS_DEFINED_BY_MIME = "Base64"  # The Request For Comment (RFC) 1521 standard is available at: http://www.ietf.org/rfc/rfc1521.txt
    """Encoding as defined by MIME (Multipurpose Internet Mail Extensions) standard RFC 1521. Four consecutive ASCII characters represent three consecutive octets of binary data. Base64 utilizes a 65-character subset of US-ASCII, consisting of both the upper and lower case alphabetic characters, digits 0 through 9, +, /, and =."""
    HEXADECIMAL_ENCODING_CONSECUTIVE_PAIRS_OF_HEXADECIMAL_DIGITS_REPRESENT_CONSECUTIVE_SINGLE_OCTETS = "Hex"
    """Hexadecimal encoding - consecutive pairs of hexadecimal digits represent consecutive single octets."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    Encoding.NO_ENCODING_DATA_ARE_DISPLAYABLE_ASCII_CHARACTERS: "No encoding - data are displayable ASCII characters.",
    Encoding.ENCODING_AS_DEFINED_BY_MIME: "Encoding as defined by MIME (Multipurpose Internet Mail Extensions) standard RFC 1521. Four consecutive ASCII characters represent three consecutive octets of binary data. Base64 utilizes a 65-character subset of US-ASCII, consisting of both the upper and lower case alphabetic characters, digits 0 through 9, +, /, and =.",
    Encoding.HEXADECIMAL_ENCODING_CONSECUTIVE_PAIRS_OF_HEXADECIMAL_DIGITS_REPRESENT_CONSECUTIVE_SINGLE_OCTETS: "Hexadecimal encoding - consecutive pairs of hexadecimal digits represent consecutive single octets.",
}
