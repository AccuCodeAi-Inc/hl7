from ...base import HL7Table

"""
HL7 Version: 2.5.1
Alternate character set handling scheme - 0356
Table Type: HL7
"""


class AlternateCharacterSetHandlingScheme(HL7Table):
    """
    Alternate character set handling scheme - 0356 // HL7 table type
    - THIS_IS_THE_DEFAULT_INDICATING_THAT_THERE_IS_NO_CHARACTER_SET_SWITCHING_OCCURRING_IN_THIS_MESSAGE
    - THE_CHARACTER_SET_SWITCHING_MODE_SPECIFIED_IN_HL7_2_5_SECTION_2_7_2_ESCAPE_SEQUENCES_SUPPORTING_MULTIPLE_CHARACTER_SETS_AND_SECTION_2_A_46_XPN_EXTENDED_PERSON_NAME
    - THIS_STANDARD_IS_TITLED_INFORMATION_TECHNOLOGY_CHARACTER_CODE_STRUCTURE_AND_EXTENSION_TECHNIQUE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0356
    """

    THIS_IS_THE_DEFAULT_INDICATING_THAT_THERE_IS_NO_CHARACTER_SET_SWITCHING_OCCURRING_IN_THIS_MESSAGE = "<null>"  # This is the default.
    """This is the default, indicating that there is no character set switching occurring in this message."""
    THE_CHARACTER_SET_SWITCHING_MODE_SPECIFIED_IN_HL7_2_5_SECTION_2_7_2_ESCAPE_SEQUENCES_SUPPORTING_MULTIPLE_CHARACTER_SETS_AND_SECTION_2_A_46_XPN_EXTENDED_PERSON_NAME = "2.3"  # Note that the escape sequences used in this mode do not use the ASCII esc character, as defined in ISO 2022-1994. They are HL7 escape sequences as first defined in HL7 2.3, sec. 2.9.2. (Also, note that sections 2.8.28.6.1and 2.9.2 in HL7 2.3 correspond to sections 2.16.93 and 2.7.2 in HL7 2. 5.)
    """The character set switching mode specified in HL7 2.5, section 2.7.2, Escape sequences supporting multiple character sets and section 2.A.46, XPN - extended person name."""
    THIS_STANDARD_IS_TITLED_INFORMATION_TECHNOLOGY_CHARACTER_CODE_STRUCTURE_AND_EXTENSION_TECHNIQUE = "ISO 2022-1994"  # This standard specifies an escape sequence from basic one byte character set to specified other character set, and vice versa. The escape sequence explicitly specifies what alternate character set to be evoked. Note that in this mode, the actual ASCII escape character is used as defined in the referenced ISO document. As noted in 1.7.1, escape sequences to/from alternate character set should occur within HL7 delimiters. In other words, HL7 delimiters are basic one byte characters only, and just before and just after delimiters, character encoding status should be the basic one byte set.
    """This standard is titled Information Technology - Character Code Structure and Extension Technique. ."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AlternateCharacterSetHandlingScheme.THIS_IS_THE_DEFAULT_INDICATING_THAT_THERE_IS_NO_CHARACTER_SET_SWITCHING_OCCURRING_IN_THIS_MESSAGE: "This is the default, indicating that there is no character set switching occurring in this message.",
    AlternateCharacterSetHandlingScheme.THE_CHARACTER_SET_SWITCHING_MODE_SPECIFIED_IN_HL7_2_5_SECTION_2_7_2_ESCAPE_SEQUENCES_SUPPORTING_MULTIPLE_CHARACTER_SETS_AND_SECTION_2_A_46_XPN_EXTENDED_PERSON_NAME: "The character set switching mode specified in HL7 2.5, section 2.7.2, Escape sequences supporting multiple character sets and section 2.A.46, XPN - extended person name.",
    AlternateCharacterSetHandlingScheme.THIS_STANDARD_IS_TITLED_INFORMATION_TECHNOLOGY_CHARACTER_CODE_STRUCTURE_AND_EXTENSION_TECHNIQUE: "This standard is titled Information Technology - Character Code Structure and Extension Technique. .",
}
