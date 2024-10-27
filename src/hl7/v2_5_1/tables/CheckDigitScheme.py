from ...base import HL7Table

"""
HL7 Version: 2.5.1
Check digit scheme - 0061
Table Type: HL7
"""


class CheckDigitScheme(HL7Table):
    """
    Check digit scheme - 0061 // HL7 table type
    - ISO_7064_1983
    - MOD_10_ALGORITHM
    - MOD_11_ALGORITHM
    - CHECK_DIGIT_ALGORITHM_IN_THE_US_NATIONAL_PROVIDER_IDENTIFIER
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0061
    """

    ISO_7064_1983 = "ISO"
    """ISO 7064: 1983"""
    MOD_10_ALGORITHM = "M10"
    """Mod 10 algorithm"""
    MOD_11_ALGORITHM = "M11"
    """Mod 11 algorithm"""
    CHECK_DIGIT_ALGORITHM_IN_THE_US_NATIONAL_PROVIDER_IDENTIFIER = "NPI"
    """Check digit algorithm in the US National Provider Identifier"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    CheckDigitScheme.ISO_7064_1983: "ISO 7064: 1983",
    CheckDigitScheme.MOD_10_ALGORITHM: "Mod 10 algorithm",
    CheckDigitScheme.MOD_11_ALGORITHM: "Mod 11 algorithm",
    CheckDigitScheme.CHECK_DIGIT_ALGORITHM_IN_THE_US_NATIONAL_PROVIDER_IDENTIFIER: "Check digit algorithm in the US National Provider Identifier",
}
