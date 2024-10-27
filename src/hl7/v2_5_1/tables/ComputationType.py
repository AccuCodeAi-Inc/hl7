from ...base import HL7Table

"""
HL7 Version: 2.5.1
Computation type - 0523
Table Type: HL7
"""


class ComputationType(HL7Table):
    """
    Computation type - 0523 // HL7 table type
    - INDICATES_A_PERCENT_CHANGE
    - ABSOLUTE_CHANGE
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0523
    """

    INDICATES_A_PERCENT_CHANGE = "%"
    """Indicates a percent change"""
    ABSOLUTE_CHANGE = "a"
    """Absolute Change"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ComputationType.INDICATES_A_PERCENT_CHANGE: "Indicates a percent change",
    ComputationType.ABSOLUTE_CHANGE: "Absolute Change",
}
