from ...base import HL7Table

"""
HL7 Version: 2.5.1
Order control codes - 0119
Table Type: HL7
"""


class OrderControlCodes(HL7Table):
    """
    Order control codes - 0119 // HL7 table type
    - ORDER_OR_SERVICE_REFILL_REQUEST_APPROVAL
    - CANCEL_ORDER_OR_SERVICE_REQUEST
    - CHILD_ORDER_OR_SERVICE
    - COMBINED_RESULT
    - CANCELED_AS_REQUESTED
    - DISCONTINUE_ORDER_OR_SERVICE_REQUEST
    - DATA_ERRORS
    - ORDER_OR_SERVICE_REFILL_REQUEST_DENIED
    - DISCONTINUED_AS_REQUESTED
    - ORDER_OR_SERVICE_REFILLED_UNSOLICITED
    - HOLD_ORDER_REQUEST
    - ON_HOLD_AS_REQUESTED
    - LINK_ORDER_OR_SERVICE_TO_PATIENT_CARE_PROBLEM_OR_GOAL
    - NUMBER_ASSIGNED
    - NEW_ORDER_OR_SERVICE
    - ORDER_OR_SERVICE_CANCELED
    - ORDER_OR_SERVICE_DISCONTINUED
    - ORDER_OR_SERVICE_RELEASED
    - ORDER_OR_SERVICE_REFILLED_AS_REQUESTED
    - ORDER_OR_SERVICE_HELD
    - ORDER_OR_SERVICE_ACCEPTED_AND_OK
    - NOTIFICATION_OF_ORDER_FOR_OUTSIDE_DISPENSE
    - RELEASED_AS_REQUESTED
    - PARENT_ORDER_OR_SERVICE
    - NOTIFICATION_OF_REPLACEMENT_ORDER_FOR_OUTSIDE_DISPENSE
    - OBSERVATIONS_OR_PERFORMED_SERVICE_TO_FOLLOW
    - REFILL_ORDER_OR_SERVICE_REQUEST
    - RELEASE_PREVIOUS_HOLD
    - REPLACEMENT_ORDER
    - ORDER_OR_SERVICE_REPLACE_REQUEST
    - REPLACED_AS_REQUESTED
    - REQUEST_RECEIVED
    - REPLACED_UNSOLICITED
    - STATUS_CHANGED
    - SEND_ORDER_OR_SERVICE_NUMBER
    - RESPONSE_TO_SEND_ORDER_OR_SERVICE_STATUS_REQUEST
    - SEND_ORDER_OR_SERVICE_STATUS_REQUEST
    - UNABLE_TO_ACCEPT_ORDER_OR_SERVICE
    - UNABLE_TO_CANCEL
    - UNABLE_TO_DISCONTINUE
    - UNABLE_TO_REFILL
    - UNABLE_TO_PUT_ON_HOLD
    - UNABLE_TO_REPLACE
    - UNLINK_ORDER_OR_SERVICE_FROM_PATIENT_CARE_PROBLEM_OR_GOAL
    - UNABLE_TO_RELEASE
    - UNABLE_TO_CHANGE
    - CHANGE_ORDER_OR_SERVICE_REQUEST
    - CHANGED_AS_REQUESTED
    - ORDER_OR_SERVICE_CHANGED_UNSOL
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0119
    """

    ORDER_OR_SERVICE_REFILL_REQUEST_APPROVAL = "AF"
    """Order/service refill request approval"""
    CANCEL_ORDER_OR_SERVICE_REQUEST = "CA"
    """Cancel order/service request"""
    CHILD_ORDER_OR_SERVICE = "CH"
    """Child order/service"""
    COMBINED_RESULT = "CN"
    """Combined result"""
    CANCELED_AS_REQUESTED = "CR"
    """Canceled as requested"""
    DISCONTINUE_ORDER_OR_SERVICE_REQUEST = "DC"
    """Discontinue order/service request"""
    DATA_ERRORS = "DE"
    """Data errors"""
    ORDER_OR_SERVICE_REFILL_REQUEST_DENIED = "DF"
    """Order/service refill request denied"""
    DISCONTINUED_AS_REQUESTED = "DR"
    """Discontinued as requested"""
    ORDER_OR_SERVICE_REFILLED_UNSOLICITED = "FU"
    """Order/service refilled, unsolicited"""
    HOLD_ORDER_REQUEST = "HD"
    """Hold order request"""
    ON_HOLD_AS_REQUESTED = "HR"
    """On hold as requested"""
    LINK_ORDER_OR_SERVICE_TO_PATIENT_CARE_PROBLEM_OR_GOAL = "LI"
    """Link order/service to patient care problem or goal"""
    NUMBER_ASSIGNED = "NA"
    """Number assigned"""
    NEW_ORDER_OR_SERVICE = "NW"
    """New order/service"""
    ORDER_OR_SERVICE_CANCELED = "OC"
    """Order/service canceled"""
    ORDER_OR_SERVICE_DISCONTINUED = "OD"
    """Order/service discontinued"""
    ORDER_OR_SERVICE_RELEASED = "OE"
    """Order/service released"""
    ORDER_OR_SERVICE_REFILLED_AS_REQUESTED = "OF"
    """Order/service refilled as requested"""
    ORDER_OR_SERVICE_HELD = "OH"
    """Order/service held"""
    ORDER_OR_SERVICE_ACCEPTED_AND_OK = "OK"
    """Order/service accepted &amp; OK"""
    NOTIFICATION_OF_ORDER_FOR_OUTSIDE_DISPENSE = "OP"
    """Notification of order for outside dispense"""
    RELEASED_AS_REQUESTED = "OR"
    """Released as requested"""
    PARENT_ORDER_OR_SERVICE = "PA"
    """Parent order/service"""
    NOTIFICATION_OF_REPLACEMENT_ORDER_FOR_OUTSIDE_DISPENSE = "PY"
    """Notification of replacement order for outside dispense"""
    OBSERVATIONS_OR_PERFORMED_SERVICE_TO_FOLLOW = "RE"
    """Observations/Performed Service to follow"""
    REFILL_ORDER_OR_SERVICE_REQUEST = "RF"
    """Refill order/service request"""
    RELEASE_PREVIOUS_HOLD = "RL"
    """Release previous hold"""
    REPLACEMENT_ORDER = "RO"
    """Replacement order"""
    ORDER_OR_SERVICE_REPLACE_REQUEST = "RP"
    """Order/service replace request"""
    REPLACED_AS_REQUESTED = "RQ"
    """Replaced as requested"""
    REQUEST_RECEIVED = "RR"
    """Request received"""
    REPLACED_UNSOLICITED = "RU"
    """Replaced unsolicited"""
    STATUS_CHANGED = "SC"
    """Status changed"""
    SEND_ORDER_OR_SERVICE_NUMBER = "SN"
    """Send order/service number"""
    RESPONSE_TO_SEND_ORDER_OR_SERVICE_STATUS_REQUEST = "SR"
    """Response to send order/service status request"""
    SEND_ORDER_OR_SERVICE_STATUS_REQUEST = "SS"
    """Send order/service status request"""
    UNABLE_TO_ACCEPT_ORDER_OR_SERVICE = "UA"
    """Unable to accept order/service"""
    UNABLE_TO_CANCEL = "UC"
    """Unable to cancel"""
    UNABLE_TO_DISCONTINUE = "UD"
    """Unable to discontinue"""
    UNABLE_TO_REFILL = "UF"
    """Unable to refill"""
    UNABLE_TO_PUT_ON_HOLD = "UH"
    """Unable to put on hold"""
    UNABLE_TO_REPLACE = "UM"
    """Unable to replace"""
    UNLINK_ORDER_OR_SERVICE_FROM_PATIENT_CARE_PROBLEM_OR_GOAL = "UN"
    """Unlink order/service from patient care problem or goal"""
    UNABLE_TO_RELEASE = "UR"
    """Unable to release"""
    UNABLE_TO_CHANGE = "UX"
    """Unable to change"""
    CHANGE_ORDER_OR_SERVICE_REQUEST = "XO"
    """Change order/service request"""
    CHANGED_AS_REQUESTED = "XR"
    """Changed as requested"""
    ORDER_OR_SERVICE_CHANGED_UNSOL = "XX"
    """Order/service changed, unsol."""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OrderControlCodes.ORDER_OR_SERVICE_REFILL_REQUEST_APPROVAL: "Order/service refill request approval",
    OrderControlCodes.CANCEL_ORDER_OR_SERVICE_REQUEST: "Cancel order/service request",
    OrderControlCodes.CHILD_ORDER_OR_SERVICE: "Child order/service",
    OrderControlCodes.COMBINED_RESULT: "Combined result",
    OrderControlCodes.CANCELED_AS_REQUESTED: "Canceled as requested",
    OrderControlCodes.DISCONTINUE_ORDER_OR_SERVICE_REQUEST: "Discontinue order/service request",
    OrderControlCodes.DATA_ERRORS: "Data errors",
    OrderControlCodes.ORDER_OR_SERVICE_REFILL_REQUEST_DENIED: "Order/service refill request denied",
    OrderControlCodes.DISCONTINUED_AS_REQUESTED: "Discontinued as requested",
    OrderControlCodes.ORDER_OR_SERVICE_REFILLED_UNSOLICITED: "Order/service refilled, unsolicited",
    OrderControlCodes.HOLD_ORDER_REQUEST: "Hold order request",
    OrderControlCodes.ON_HOLD_AS_REQUESTED: "On hold as requested",
    OrderControlCodes.LINK_ORDER_OR_SERVICE_TO_PATIENT_CARE_PROBLEM_OR_GOAL: "Link order/service to patient care problem or goal",
    OrderControlCodes.NUMBER_ASSIGNED: "Number assigned",
    OrderControlCodes.NEW_ORDER_OR_SERVICE: "New order/service",
    OrderControlCodes.ORDER_OR_SERVICE_CANCELED: "Order/service canceled",
    OrderControlCodes.ORDER_OR_SERVICE_DISCONTINUED: "Order/service discontinued",
    OrderControlCodes.ORDER_OR_SERVICE_RELEASED: "Order/service released",
    OrderControlCodes.ORDER_OR_SERVICE_REFILLED_AS_REQUESTED: "Order/service refilled as requested",
    OrderControlCodes.ORDER_OR_SERVICE_HELD: "Order/service held",
    OrderControlCodes.ORDER_OR_SERVICE_ACCEPTED_AND_OK: "Order/service accepted &amp; OK",
    OrderControlCodes.NOTIFICATION_OF_ORDER_FOR_OUTSIDE_DISPENSE: "Notification of order for outside dispense",
    OrderControlCodes.RELEASED_AS_REQUESTED: "Released as requested",
    OrderControlCodes.PARENT_ORDER_OR_SERVICE: "Parent order/service",
    OrderControlCodes.NOTIFICATION_OF_REPLACEMENT_ORDER_FOR_OUTSIDE_DISPENSE: "Notification of replacement order for outside dispense",
    OrderControlCodes.OBSERVATIONS_OR_PERFORMED_SERVICE_TO_FOLLOW: "Observations/Performed Service to follow",
    OrderControlCodes.REFILL_ORDER_OR_SERVICE_REQUEST: "Refill order/service request",
    OrderControlCodes.RELEASE_PREVIOUS_HOLD: "Release previous hold",
    OrderControlCodes.REPLACEMENT_ORDER: "Replacement order",
    OrderControlCodes.ORDER_OR_SERVICE_REPLACE_REQUEST: "Order/service replace request",
    OrderControlCodes.REPLACED_AS_REQUESTED: "Replaced as requested",
    OrderControlCodes.REQUEST_RECEIVED: "Request received",
    OrderControlCodes.REPLACED_UNSOLICITED: "Replaced unsolicited",
    OrderControlCodes.STATUS_CHANGED: "Status changed",
    OrderControlCodes.SEND_ORDER_OR_SERVICE_NUMBER: "Send order/service number",
    OrderControlCodes.RESPONSE_TO_SEND_ORDER_OR_SERVICE_STATUS_REQUEST: "Response to send order/service status request",
    OrderControlCodes.SEND_ORDER_OR_SERVICE_STATUS_REQUEST: "Send order/service status request",
    OrderControlCodes.UNABLE_TO_ACCEPT_ORDER_OR_SERVICE: "Unable to accept order/service",
    OrderControlCodes.UNABLE_TO_CANCEL: "Unable to cancel",
    OrderControlCodes.UNABLE_TO_DISCONTINUE: "Unable to discontinue",
    OrderControlCodes.UNABLE_TO_REFILL: "Unable to refill",
    OrderControlCodes.UNABLE_TO_PUT_ON_HOLD: "Unable to put on hold",
    OrderControlCodes.UNABLE_TO_REPLACE: "Unable to replace",
    OrderControlCodes.UNLINK_ORDER_OR_SERVICE_FROM_PATIENT_CARE_PROBLEM_OR_GOAL: "Unlink order/service from patient care problem or goal",
    OrderControlCodes.UNABLE_TO_RELEASE: "Unable to release",
    OrderControlCodes.UNABLE_TO_CHANGE: "Unable to change",
    OrderControlCodes.CHANGE_ORDER_OR_SERVICE_REQUEST: "Change order/service request",
    OrderControlCodes.CHANGED_AS_REQUESTED: "Changed as requested",
    OrderControlCodes.ORDER_OR_SERVICE_CHANGED_UNSOL: "Order/service changed, unsol.",
}
