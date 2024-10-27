from ...base import HL7Table

"""
HL7 Version: 2.5.1
Name assembly order - 0444
Table Type: HL7
"""


class NameAssemblyOrder(HL7Table):
    """
    Name assembly order - 0444 // HL7 table type
    - PREFIX_FAMILY_MIDDLE_GIVEN_SUFFIX
    - PREFIX_GIVEN_MIDDLE_FAMILY_SUFFIX
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0444
    """

    PREFIX_FAMILY_MIDDLE_GIVEN_SUFFIX = "F"
    """Prefix Family Middle Given Suffix"""
    PREFIX_GIVEN_MIDDLE_FAMILY_SUFFIX = "G"
    """Prefix Given Middle Family Suffix"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    NameAssemblyOrder.PREFIX_FAMILY_MIDDLE_GIVEN_SUFFIX: "Prefix Family Middle Given Suffix",
    NameAssemblyOrder.PREFIX_GIVEN_MIDDLE_FAMILY_SUFFIX: "Prefix Given Middle Family Suffix",
}
