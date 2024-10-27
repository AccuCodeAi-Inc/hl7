from ...base import HL7Table

"""
HL7 Version: 2.5.1
Event type - 0450
Table Type: HL7
"""


class EventType(HL7Table):
    """
    Event type - 0450 // HL7 table type
    - LOG_EVENT
    - SERVICE_EVENT
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0450
    """

    LOG_EVENT = "LOG"
    """Log Event"""
    SERVICE_EVENT = "SER"
    """Service Event"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    EventType.LOG_EVENT: "Log Event",
    EventType.SERVICE_EVENT: "Service Event",
}
