from ...base import HL7Table

"""
HL7 Version: 2.5.1
Allow Substitution - 0161
Table Type: HL7
"""


class AllowSubstitution(HL7Table):
    """
    Allow Substitution - 0161 // HL7 table type
    - ALLOW_GENERIC_SUBSTITUTIONS
    - SUBSTITUTIONS_ARE_NOT_AUTHORIZED
    - ALLOW_THERAPEUTIC_SUBSTITUTIONS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0161
    """

    ALLOW_GENERIC_SUBSTITUTIONS = "G"
    """Allow generic substitutions."""
    SUBSTITUTIONS_ARE_NOT_AUTHORIZED = "N"
    """Substitutions are NOT authorized. (This is the default - null.)"""
    ALLOW_THERAPEUTIC_SUBSTITUTIONS = "T"
    """Allow therapeutic substitutions"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    AllowSubstitution.ALLOW_GENERIC_SUBSTITUTIONS: "Allow generic substitutions.",
    AllowSubstitution.SUBSTITUTIONS_ARE_NOT_AUTHORIZED: "Substitutions are NOT authorized. (This is the default - null.)",
    AllowSubstitution.ALLOW_THERAPEUTIC_SUBSTITUTIONS: "Allow therapeutic substitutions",
}
