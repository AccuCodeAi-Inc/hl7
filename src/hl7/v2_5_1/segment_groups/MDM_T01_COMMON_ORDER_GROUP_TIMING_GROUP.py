from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.TQ2 import TQ2
from ..segments.TQ1 import TQ1


"""
TIMING - MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP
from utils.hl7.v2_5_1.segments import (
    TQ1, TQ2
)

mdm_t01_common_order_group_timing_group = MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP(  # TIMING - Segment group for MDM_T01_COMMON_ORDER_GROUP - COMMON ORDER consisting of TQ1, TQ2|None
    timing_or_quantity=tq1,  # TQ1(...)  # Required.
    timing_or_quantity_relationship=None,  # TQ2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP TEMPLATE-----
"""


class MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP"""
    _hl7_name = """TIMING"""
    _hl7_description = """Segment group for MDM_T01_COMMON_ORDER_GROUP - COMMON ORDER consisting of TQ1, TQ2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("7", "8")
    _c_components = (TQ1, TQ2)
    _c_name = ("TQ1", "TQ2")
    _c_is_group = (False, False)
    _c_attrs = ("timing_or_quantity", "timing_or_quantity_relationship",)
    # fmt: on

    def __init__(
        self,
        timing_or_quantity: TQ1,  #  Required. TQ1.7
        timing_or_quantity_relationship: TQ2 | tuple[TQ2, ...] | None = None,  #  TQ2.8
    ):
        """
        None - `MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MDM_T01_COMMON_ORDER_GROUP_TIMING_GROUP>`_
        Segment group for MDM_T01_COMMON_ORDER_GROUP - COMMON ORDER consisting of TQ1, TQ2|None

        :param timing_or_quantity: Timing/Quantity (id: TQ1 | seq: 7 | use: R | rpt: 1)
        :param timing_or_quantity_relationship: Timing/Quantity Relationship (id: TQ2 | seq: 8 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.timing_or_quantity = timing_or_quantity
        self.timing_or_quantity_relationship = timing_or_quantity_relationship

    @property  # get TQ1.7
    def timing_or_quantity(self) -> TQ1:
        """
        id: TQ1 | use: R | rpt: 1 | seq: 7
        ---
        return_type: TQ1.7: Timing/Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        return self._c_data[0][0]

    @timing_or_quantity.setter  # set TQ1.7
    def timing_or_quantity(self, tq1: TQ1):
        """
        id: TQ1 | use: R | rpt: 1 | seq: 7
        ---
        param_type: TQ1.7: Timing/Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        self._c_data[0] = (tq1,)

    @property  # get TQ2
    def timing_or_quantity_relationship(self) -> tuple[TQ2, ...] | tuple[None]:
        """
        id: TQ2 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[TQ2, ...]: (Timing/Quantity Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ2
        """
        return self._c_data[1]

    @timing_or_quantity_relationship.setter  # set TQ2
    def timing_or_quantity_relationship(self, tq2: TQ2 | tuple[TQ2, ...] | None):
        """
        id: TQ2 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: TQ2.8 | tuple[TQ2, ...]: (Timing/Quantity Relationship, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ2
        """
        if isinstance(tq2, tuple):
            self._c_data[1] = tq2
        else:
            self._c_data[1] = (tq2,)
