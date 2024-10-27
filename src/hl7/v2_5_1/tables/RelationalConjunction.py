from ...base import HL7Table

"""
HL7 Version: 2.5.1
Relational conjunction - 0210
Table Type: HL7
"""


class RelationalConjunction(HL7Table):
    """
    Relational conjunction - 0210 // HL7 table type
    - DEFAULT
    - OR
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0210
    """

    DEFAULT = "AND"
    """Default"""
    OR = "OR"
    """"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    RelationalConjunction.DEFAULT: "Default",
    RelationalConjunction.OR: "",
}
