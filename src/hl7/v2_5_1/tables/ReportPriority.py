from ...base import HL7Table

"""
HL7 Version: 2.5.1
Report priority - 0109
Table Type: HL7
"""


class ReportPriority(HL7Table):
    """
    Report priority - 0109 // HL7 table type
    - ROUTINE
    - STAT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0109
    """

    ROUTINE = "R"
    """Routine"""
    STAT = "S"
    """Stat"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ReportPriority.ROUTINE: "Routine",
    ReportPriority.STAT: "Stat",
}
