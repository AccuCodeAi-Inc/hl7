from ...base import HL7Table

"""
HL7 Version: 2.5.1
Response modality - 0394
Table Type: HL7
"""


class ResponseModality(HL7Table):
    """
    Response modality - 0394 // HL7 table type
    - BATCH
    - REAL_TIME
    - BOLUS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0394
    """

    BATCH = "B"
    """Batch"""
    REAL_TIME = "R"
    """Real Time"""
    BOLUS = "T"
    """Bolus (a series of responses sent at the same time without use of batch formatting)"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    ResponseModality.BATCH: "Batch",
    ResponseModality.REAL_TIME: "Real Time",
    ResponseModality.BOLUS: "Bolus (a series of responses sent at the same time without use of batch formatting)",
}
