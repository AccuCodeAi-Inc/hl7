from ...base import HL7Table

"""
HL7 Version: 2.5.1
Procedure DRG Type - 0416
Table Type: User
"""


class ProcedureDrgType(HL7Table):
    """
    Procedure DRG Type - 0416 // User table type
    - _1ST_NON_OPERATIVE
    - _2ND_NON_OPERATIVE
    - MAJOR_OPERATIVE
    - _2ND_OPERATIVE
    - _3RD_OPERATIVE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0416
    """

    _1ST_NON_OPERATIVE = "1"
    """1st non-Operative"""
    _2ND_NON_OPERATIVE = "2"
    """2nd non-Operative"""
    MAJOR_OPERATIVE = "3"
    """Major Operative"""
    _2ND_OPERATIVE = "4"
    """2nd Operative"""
    _3RD_OPERATIVE = "5"
    """3rd Operative"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcedureDrgType._1ST_NON_OPERATIVE: "1st non-Operative",
    ProcedureDrgType._2ND_NON_OPERATIVE: "2nd non-Operative",
    ProcedureDrgType.MAJOR_OPERATIVE: "Major Operative",
    ProcedureDrgType._2ND_OPERATIVE: "2nd Operative",
    ProcedureDrgType._3RD_OPERATIVE: "3rd Operative",
}
