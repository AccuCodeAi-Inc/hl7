from ...base import HL7Table

"""
HL7 Version: 2.5.1
Invocation event - 0100
Table Type: HL7
"""


class InvocationEvent(HL7Table):
    """
    Invocation event - 0100 // HL7 table type
    - ON_DISCHARGE
    - ON_RECEIPT_OF_ORDER
    - AT_TIME_SERVICE_IS_COMPLETED
    - AT_TIME_SERVICE_IS_STARTED
    - AT_A_DESIGNATED_DATE_OR_TIME
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0100
    """

    ON_DISCHARGE = "D"
    """On discharge"""
    ON_RECEIPT_OF_ORDER = "O"
    """On receipt of order"""
    AT_TIME_SERVICE_IS_COMPLETED = "R"
    """At time service is completed"""
    AT_TIME_SERVICE_IS_STARTED = "S"
    """At time service is started"""
    AT_A_DESIGNATED_DATE_OR_TIME = "T"
    """At a designated date/time"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    InvocationEvent.ON_DISCHARGE: "On discharge",
    InvocationEvent.ON_RECEIPT_OF_ORDER: "On receipt of order",
    InvocationEvent.AT_TIME_SERVICE_IS_COMPLETED: "At time service is completed",
    InvocationEvent.AT_TIME_SERVICE_IS_STARTED: "At time service is started",
    InvocationEvent.AT_A_DESIGNATED_DATE_OR_TIME: "At a designated date/time",
}
