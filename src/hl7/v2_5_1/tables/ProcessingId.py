from ...base import HL7Table

"""
HL7 Version: 2.5.1
Processing ID - 0103
Table Type: HL7
"""


class ProcessingId(HL7Table):
    """
    Processing ID - 0103 // HL7 table type
    - DEBUGGING
    - PRODUCTION
    - TRAINING
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0103
    """

    DEBUGGING = "D"
    """Debugging"""
    PRODUCTION = "P"
    """Production"""
    TRAINING = "T"
    """Training"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ProcessingId.DEBUGGING: "Debugging",
    ProcessingId.PRODUCTION: "Production",
    ProcessingId.TRAINING: "Training",
}
