from ...base import HL7Table

"""
HL7 Version: 2.5.1
Processing type - 0388
Table Type: HL7
"""


class ProcessingType(HL7Table):
    """
    Processing type - 0388 // HL7 table type
    - EVALUATION
    - REGULAR_PRODUCTION
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0388
    """

    EVALUATION = "E"
    """Evaluation"""
    REGULAR_PRODUCTION = "P"
    """Regular Production"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcessingType.EVALUATION: "Evaluation",
    ProcessingType.REGULAR_PRODUCTION: "Regular Production",
}
