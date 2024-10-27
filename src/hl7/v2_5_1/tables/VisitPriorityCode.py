from ...base import HL7Table

"""
HL7 Version: 2.5.1
Visit Priority Code - 0217
Table Type: User
"""


class VisitPriorityCode(HL7Table):
    """
    Visit Priority Code - 0217 // User table type
    - EMERGENCY
    - URGENT
    - ELECTIVE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0217
    """

    EMERGENCY = "1"
    """Emergency"""
    URGENT = "2"
    """Urgent"""
    ELECTIVE = "3"
    """Elective"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    VisitPriorityCode.EMERGENCY: "Emergency",
    VisitPriorityCode.URGENT: "Urgent",
    VisitPriorityCode.ELECTIVE: "Elective",
}
