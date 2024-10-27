from ...base import HL7Table

"""
HL7 Version: 2.5.1
Alternate character sets - 0211
Table Type: HL7
"""


class AlternateCharacterSets(HL7Table):
    """
    Alternate character sets - 0211 // HL7 table type
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_1_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_2_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_3_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_4_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_5_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_6_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_7_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_8_CHARACTER_SET
    - THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_9_CHARACTER_SET
    - THE_PRINTABLE_7_BIT_ASCII_CHARACTER_SET
    - CODE_FOR_TAIWANESE_CHARACTER_SET
    - CNS_11643_1992
    - CODE_FOR_CHINESE_CHARACTER_SET
    - CODE_FOR_INFORMATION_EXCHANGE
    - CODE_OF_THE_SUPPLEMENTARY_JAPANESE_GRAPHIC_CHARACTER_SET_FOR_INFORMATION_INTERCHANGE
    - CODE_FOR_THE_JAPANESE_GRAPHIC_CHARACTER_SET_FOR_INFORMATION_INTERCHANGE
    - CODE_FOR_KOREAN_CHARACTER_SET
    - THE_WORLD_WIDE_CHARACTER_STANDARD_FROM_ISO_OR_IEC_10646_1_1993_6
    - UCS_TRANSFORMATION_FORMAT_16_BIT_FORM
    - UCS_TRANSFORMATION_FORMAT_32_BIT_FORM
    - UCS_TRANSFORMATION_FORMAT_8_BIT_FORM
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0211
    """

    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_1_CHARACTER_SET = "8859/1"
    """The printable characters from the ISO 8859/1 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_2_CHARACTER_SET = "8859/2"
    """The printable characters from the ISO 8859/2 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_3_CHARACTER_SET = "8859/3"
    """The printable characters from the ISO 8859/3 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_4_CHARACTER_SET = "8859/4"
    """The printable characters from the ISO 8859/4 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_5_CHARACTER_SET = "8859/5"
    """The printable characters from the ISO 8859/5 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_6_CHARACTER_SET = "8859/6"
    """The printable characters from the ISO 8859/6 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_7_CHARACTER_SET = "8859/7"
    """The printable characters from the ISO 8859/7 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_8_CHARACTER_SET = "8859/8"
    """The printable characters from the ISO 8859/8 Character set"""
    THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_9_CHARACTER_SET = "8859/9"
    """The printable characters from the ISO 8859/9 Character set"""
    THE_PRINTABLE_7_BIT_ASCII_CHARACTER_SET = (
        "ASCII"  # (This is the default if this field is omitted)
    )
    """The printable 7-bit ASCII character set."""
    CODE_FOR_TAIWANESE_CHARACTER_SET = "BIG-5"  # Does not need an escape sequence. BIG-5 does not need an escape sequence. ASCII is a 7 bit character set, which means that the top bit of the byte is 0. The parser knows that when the top bit of the byte is 0, the character set is ASCII. When it is 1, the following bytes should be handled as 2 bytes (or more). No escape technique is needed. However, since some servers do not correctly interpret when they receive a top bit 1, it is advised, in internet RFC, to not use these kind of non-safe non-escape extension.
    """Code for Taiwanese Character Set (BIG-5)"""
    CNS_11643_1992 = "CNS 11643-1992"  # Does not need an escape sequence.
    """Code for Taiwanese Character Set (CNS 11643-1992)"""
    CODE_FOR_CHINESE_CHARACTER_SET = (
        "GB 18030-2000"  # Does not need an escape sequence.
    )
    """Code for Chinese Character Set (GB 18030-2000)"""
    CODE_FOR_INFORMATION_EXCHANGE = (
        "ISO IR14"  # Note that the code contains a space, i.e. ISO IR14.
    )
    """Code for Information Exchange (one byte)(JIS X 0201-1976)."""
    CODE_OF_THE_SUPPLEMENTARY_JAPANESE_GRAPHIC_CHARACTER_SET_FOR_INFORMATION_INTERCHANGE = "ISO IR159"  # Note that the code contains a space, i.e. ISO IR159.
    """Code of the supplementary Japanese Graphic Character set for information interchange (JIS X 0212-1990)."""
    CODE_FOR_THE_JAPANESE_GRAPHIC_CHARACTER_SET_FOR_INFORMATION_INTERCHANGE = "ISO IR87"  # Note that the code contains a space, i.e. ISO IR87. The JIS X 0208 needs an escape sequence. In Japan, the escape technique is ISO 2022. From basic ASCII, escape sequence escape $ B (in HEX, 1B 24 42) lets the parser know that following bytes should be handled 2-byte wise. Back to ASCII is 1B 28 42.
    """Code for the Japanese Graphic Character set for information interchange (JIS X 0208-1990),"""
    CODE_FOR_KOREAN_CHARACTER_SET = "KS X 1001"
    """Code for Korean Character Set (KS X 1001)"""
    THE_WORLD_WIDE_CHARACTER_STANDARD_FROM_ISO_OR_IEC_10646_1_1993_6 = "UNICODE"  # Deprecated. Retained for backward compatibility only as v 2.5. Replaced by specific Unicode encoding codes.
    """The world wide character standard from ISO/IEC 10646-1-1993[6]"""
    UCS_TRANSFORMATION_FORMAT_16_BIT_FORM = "UNICODE UTF-16"  # UTF-16 is identical to ISO/IEC 10646 UCS-2. Note that the code contains a space before UTF but not before and after the hyphen.
    """UCS Transformation Format, 16-bit form"""
    UCS_TRANSFORMATION_FORMAT_32_BIT_FORM = "UNICODE UTF-32"  # UTF-32 is defined by Unicode Technical Report #19, and is an officially recognized encoding as of Unicode Version 3.1. UTF-32 is a proper subset of ISO/IEC 10646 UCS-4. Note that the code contains a space before UTF but not before and after the hyphen.
    """UCS Transformation Format, 32-bit form"""
    UCS_TRANSFORMATION_FORMAT_8_BIT_FORM = "UNICODE UTF-8"  # UTF-8 is a variable-length encoding, each code value is represented by 1,2 or 3 bytes, depending on the code value. 7 bit ASCII is a proper subset of UTF-8. Note that the code contains a space before UTF but not before and after the hyphen.
    """UCS Transformation Format, 8-bit form"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_1_CHARACTER_SET: "The printable characters from the ISO 8859/1 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_2_CHARACTER_SET: "The printable characters from the ISO 8859/2 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_3_CHARACTER_SET: "The printable characters from the ISO 8859/3 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_4_CHARACTER_SET: "The printable characters from the ISO 8859/4 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_5_CHARACTER_SET: "The printable characters from the ISO 8859/5 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_6_CHARACTER_SET: "The printable characters from the ISO 8859/6 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_7_CHARACTER_SET: "The printable characters from the ISO 8859/7 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_8_CHARACTER_SET: "The printable characters from the ISO 8859/8 Character set",
    AlternateCharacterSets.THE_PRINTABLE_CHARACTERS_FROM_THE_ISO_8859_OR_9_CHARACTER_SET: "The printable characters from the ISO 8859/9 Character set",
    AlternateCharacterSets.THE_PRINTABLE_7_BIT_ASCII_CHARACTER_SET: "The printable 7-bit ASCII character set.",
    AlternateCharacterSets.CODE_FOR_TAIWANESE_CHARACTER_SET: "Code for Taiwanese Character Set (BIG-5)",
    AlternateCharacterSets.CNS_11643_1992: "Code for Taiwanese Character Set (CNS 11643-1992)",
    AlternateCharacterSets.CODE_FOR_CHINESE_CHARACTER_SET: "Code for Chinese Character Set (GB 18030-2000)",
    AlternateCharacterSets.CODE_FOR_INFORMATION_EXCHANGE: "Code for Information Exchange (one byte)(JIS X 0201-1976).",
    AlternateCharacterSets.CODE_OF_THE_SUPPLEMENTARY_JAPANESE_GRAPHIC_CHARACTER_SET_FOR_INFORMATION_INTERCHANGE: "Code of the supplementary Japanese Graphic Character set for information interchange (JIS X 0212-1990).",
    AlternateCharacterSets.CODE_FOR_THE_JAPANESE_GRAPHIC_CHARACTER_SET_FOR_INFORMATION_INTERCHANGE: "Code for the Japanese Graphic Character set for information interchange (JIS X 0208-1990),",
    AlternateCharacterSets.CODE_FOR_KOREAN_CHARACTER_SET: "Code for Korean Character Set (KS X 1001)",
    AlternateCharacterSets.THE_WORLD_WIDE_CHARACTER_STANDARD_FROM_ISO_OR_IEC_10646_1_1993_6: "The world wide character standard from ISO/IEC 10646-1-1993[6]",
    AlternateCharacterSets.UCS_TRANSFORMATION_FORMAT_16_BIT_FORM: "UCS Transformation Format, 16-bit form",
    AlternateCharacterSets.UCS_TRANSFORMATION_FORMAT_32_BIT_FORM: "UCS Transformation Format, 32-bit form",
    AlternateCharacterSets.UCS_TRANSFORMATION_FORMAT_8_BIT_FORM: "UCS Transformation Format, 8-bit form",
}
