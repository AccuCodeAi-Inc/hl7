from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXO import RXO
from ..segment_groups.RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP import (
    RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP,
)


"""
ORDER DETAIL - RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    RXO
)
from utils.hl7.v2_5_1.segment_groups import (
    RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
)

ras_o17_order_group_order_detail_group = RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for RAS_O17_ORDER_GROUP - ORDER consisting of RXO, ORDER DETAIL SUPPLEMENT|None
    pharmacy_or_treatment_order=rxo,  # RXO(...)  # Required.
    order_detail_supplement=None,  # RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for RAS_O17_ORDER_GROUP - ORDER consisting of RXO, ORDER DETAIL SUPPLEMENT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("13", "None")
    _c_components = (RXO, RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP)
    _c_name = ("RXO", "ORDER DETAIL SUPPLEMENT")
    _c_is_group = (False, True)
    _c_attrs = ("pharmacy_or_treatment_order", "order_detail_supplement",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_order: RXO,  #  Required. RXO.13
        order_detail_supplement: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
        | None = None,  #  NTE.14, RXR.15
    ):
        """
        None - `RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for RAS_O17_ORDER_GROUP - ORDER consisting of RXO, ORDER DETAIL SUPPLEMENT|None

        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 13 | use: R | rpt: 1)
        :param order_detail_supplement: Order Detail Supplement segment group: [NTE, RXR, COMPONENTS|None] (id: ORDER DETAIL SUPPLEMENT | seq: 14, 15, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.order_detail_supplement = order_detail_supplement

    @property  # get RXO.13
    def pharmacy_or_treatment_order(self) -> RXO:
        """
        id: RXO | use: R | rpt: 1 | seq: 13
        ---
        return_type: RXO.13: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_order.setter  # set RXO.13
    def pharmacy_or_treatment_order(self, rxo: RXO):
        """
        id: RXO | use: R | rpt: 1 | seq: 13
        ---
        param_type: RXO.13: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[0] = (rxo,)

    @property  # get RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP.None
    def order_detail_supplement(
        self,
    ) -> RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP | None:
        """
        id: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
        """
        return self._c_data[1][0]

    @order_detail_supplement.setter  # set RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP.None
    def order_detail_supplement(
        self,
        order_detail_supplement: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
        | None,
    ):
        """
        id: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
        """
        self._c_data[1] = (order_detail_supplement,)
