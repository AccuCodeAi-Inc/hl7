from ...base import HL7Table

"""
HL7 Version: 2.5.1
Military Rank/Grade - 0141
Table Type: User
"""


class MilitaryRankOrGrade(HL7Table):
    """
    Military Rank/Grade - 0141 // User table type
    - ENLISTED
    - OFFICERS
    - WARRANT_OFFICERS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0141
    """

    ENLISTED = "E1... E9"
    """Enlisted"""
    OFFICERS = "O1 ... O9"
    """Officers"""
    WARRANT_OFFICERS = "W1 ... W4"
    """Warrant Officers"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    MilitaryRankOrGrade.ENLISTED: "Enlisted",
    MilitaryRankOrGrade.OFFICERS: "Officers",
    MilitaryRankOrGrade.WARRANT_OFFICERS: "Warrant Officers",
}
