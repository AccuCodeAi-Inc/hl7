from ...base import HL7Table

"""
HL7 Version: 2.5.1
Procedure Priority - 0418
Table Type: HL7
"""


class ProcedurePriority(HL7Table):
    """
    Procedure Priority - 0418 // HL7 table type
    - THE_ADMITTING_PROCEDURE
    - THE_PRIMARY_PROCEDURE
    - FOR_RANKED_SECONDARY_PROCEDURES
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0418
    """

    THE_ADMITTING_PROCEDURE = "0"
    """the admitting procedure"""
    THE_PRIMARY_PROCEDURE = "1"
    """the primary procedure"""
    FOR_RANKED_SECONDARY_PROCEDURES = "2 …"
    """for ranked secondary procedures"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcedurePriority.THE_ADMITTING_PROCEDURE: "the admitting procedure",
    ProcedurePriority.THE_PRIMARY_PROCEDURE: "the primary procedure",
    ProcedurePriority.FOR_RANKED_SECONDARY_PROCEDURES: "for ranked secondary procedures",
}
