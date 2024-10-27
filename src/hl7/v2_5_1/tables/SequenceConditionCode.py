from ...base import HL7Table

"""
HL7 Version: 2.5.1
Sequence Condition Code - 0504
Table Type: HL7
"""


class SequenceConditionCode(HL7Table):
    """
    Sequence Condition Code - 0504 // HL7 table type
    - END_RELATED_SERVICE_REQUEST
    - ES
    - START_RELATED_SERVICE_REQUEST
    - SS
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0504
    """

    END_RELATED_SERVICE_REQUEST = "EE"
    """End related service request(s), end current service request."""
    ES = "ES"
    """End related service request(s), start current service request."""
    START_RELATED_SERVICE_REQUEST = "SE"
    """Start related service request(s), end current service request."""
    SS = "SS"
    """Start related service request(s), start current service request."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    SequenceConditionCode.END_RELATED_SERVICE_REQUEST: "End related service request(s), end current service request.",
    SequenceConditionCode.ES: "End related service request(s), start current service request.",
    SequenceConditionCode.START_RELATED_SERVICE_REQUEST: "Start related service request(s), end current service request.",
    SequenceConditionCode.SS: "Start related service request(s), start current service request.",
}
