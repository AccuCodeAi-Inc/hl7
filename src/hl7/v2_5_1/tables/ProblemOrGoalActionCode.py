from ...base import HL7Table

"""
HL7 Version: 2.5.1
Problem/goal action code - 0287
Table Type: HL7
"""


class ProblemOrGoalActionCode(HL7Table):
    """
    Problem/goal action code - 0287 // HL7 table type
    - ADD
    - CORRECT
    - DELETE
    - LINK
    - UNCHANGED_STAR
    - UNLINK
    - UPDATE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0287
    """

    ADD = "AD"
    """ADD"""
    CORRECT = "CO"
    """CORRECT"""
    DELETE = "DE"
    """DELETE"""
    LINK = "LI"
    """LINK"""
    UNCHANGED_STAR = "UC"
    """UNCHANGED *"""
    UNLINK = "UN"
    """UNLINK"""
    UPDATE = "UP"
    """UPDATE"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProblemOrGoalActionCode.ADD: "ADD",
    ProblemOrGoalActionCode.CORRECT: "CORRECT",
    ProblemOrGoalActionCode.DELETE: "DELETE",
    ProblemOrGoalActionCode.LINK: "LINK",
    ProblemOrGoalActionCode.UNCHANGED_STAR: "UNCHANGED *",
    ProblemOrGoalActionCode.UNLINK: "UNLINK",
    ProblemOrGoalActionCode.UPDATE: "UPDATE",
}
