from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.TQ2 import TQ2
from ..segments.TQ1 import TQ1


"""
TIMING ENCODED - RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
from utils.hl7.v2_5_1.segments import (
    TQ1, TQ2
)

rsp_z82_query_response_group_common_order_group_encoded_order_group_timing_encoded_group = RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP(  # TIMING ENCODED - Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP - ENCODED ORDER consisting of TQ1, TQ2|None
    timing_or_quantity=tq1,  # TQ1(...)  # Required.
    timing_or_quantity_relationship=None,  # TQ2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP TEMPLATE-----
"""


class RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP"""
    _hl7_name = """TIMING ENCODED"""
    _hl7_description = """Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP - ENCODED ORDER consisting of TQ1, TQ2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("23", "24")
    _c_components = (TQ1, TQ2)
    _c_name = ("TQ1", "TQ2")
    _c_is_group = (False, False)
    _c_attrs = ("timing_or_quantity", "timing_or_quantity_relationship",)
    # fmt: on

    def __init__(
        self,
        timing_or_quantity: TQ1,  #  Required. TQ1.23
        timing_or_quantity_relationship: TQ2 | tuple[TQ2, ...] | None = None,  #  TQ2.24
    ):
        """
        None - `RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP>`_
        Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP - ENCODED ORDER consisting of TQ1, TQ2|None

        :param timing_or_quantity: Timing/Quantity (id: TQ1 | seq: 23 | use: R | rpt: 1)
        :param timing_or_quantity_relationship: Timing/Quantity Relationship (id: TQ2 | seq: 24 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.timing_or_quantity = timing_or_quantity
        self.timing_or_quantity_relationship = timing_or_quantity_relationship

    @property  # get TQ1.23
    def timing_or_quantity(self) -> TQ1:
        """
        id: TQ1 | use: R | rpt: 1 | seq: 23
        ---
        return_type: TQ1.23: Timing/Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        return self._c_data[0][0]

    @timing_or_quantity.setter  # set TQ1.23
    def timing_or_quantity(self, tq1: TQ1):
        """
        id: TQ1 | use: R | rpt: 1 | seq: 23
        ---
        param_type: TQ1.23: Timing/Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        self._c_data[0] = (tq1,)

    @property  # get TQ2
    def timing_or_quantity_relationship(self) -> tuple[TQ2, ...] | tuple[None]:
        """
        id: TQ2 SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        return_type: tuple[TQ2, ...]: (Timing/Quantity Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ2
        """
        return self._c_data[1]

    @timing_or_quantity_relationship.setter  # set TQ2
    def timing_or_quantity_relationship(self, tq2: TQ2 | tuple[TQ2, ...] | None):
        """
        id: TQ2 SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        param_type: TQ2.24 | tuple[TQ2, ...]: (Timing/Quantity Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ2
        """
        if isinstance(tq2, tuple):
            self._c_data[1] = tq2
        else:
            self._c_data[1] = (tq2,)