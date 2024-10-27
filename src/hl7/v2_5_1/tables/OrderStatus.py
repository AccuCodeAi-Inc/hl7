from ...base import HL7Table

"""
HL7 Version: 2.5.1
Order status - 0038
Table Type: HL7
"""


class OrderStatus(HL7Table):
    """
    Order status - 0038 // HL7 table type
    - SOME_BUT_NOT_ALL_RESULTS_AVAILABLE
    - ORDER_WAS_CANCELED
    - ORDER_IS_COMPLETED
    - ORDER_WAS_DISCONTINUED
    - ERROR_ORDER_NOT_FOUND
    - ORDER_IS_ON_HOLD
    - IN_PROCESS_UNSPECIFIED
    - ORDER_HAS_BEEN_REPLACED
    - IN_PROCESS_SCHEDULED
    https://hl7-definition.caristix.com/v2/HL7v2.5.1/Tables/0038
    """

    SOME_BUT_NOT_ALL_RESULTS_AVAILABLE = "A"
    """Some, but not all, results available"""
    ORDER_WAS_CANCELED = "CA"
    """Order was canceled"""
    ORDER_IS_COMPLETED = "CM"
    """Order is completed"""
    ORDER_WAS_DISCONTINUED = "DC"
    """Order was discontinued"""
    ERROR_ORDER_NOT_FOUND = "ER"
    """Error, order not found"""
    ORDER_IS_ON_HOLD = "HD"
    """Order is on hold"""
    IN_PROCESS_UNSPECIFIED = "IP"
    """In process, unspecified"""
    ORDER_HAS_BEEN_REPLACED = "RP"
    """Order has been replaced"""
    IN_PROCESS_SCHEDULED = "SC"
    """In process, scheduled"""

    @property
    def description(self) -> str:
        return _desc[self]


_desc = {
    OrderStatus.SOME_BUT_NOT_ALL_RESULTS_AVAILABLE: "Some, but not all, results available",
    OrderStatus.ORDER_WAS_CANCELED: "Order was canceled",
    OrderStatus.ORDER_IS_COMPLETED: "Order is completed",
    OrderStatus.ORDER_WAS_DISCONTINUED: "Order was discontinued",
    OrderStatus.ERROR_ORDER_NOT_FOUND: "Error, order not found",
    OrderStatus.ORDER_IS_ON_HOLD: "Order is on hold",
    OrderStatus.IN_PROCESS_UNSPECIFIED: "In process, unspecified",
    OrderStatus.ORDER_HAS_BEEN_REPLACED: "Order has been replaced",
    OrderStatus.IN_PROCESS_SCHEDULED: "In process, scheduled",
}
