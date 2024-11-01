from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.RXC import RXC


"""
COMPONENT - RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, RXC
)

rds_o13_order_group_order_detail_group_order_detail_supplement_group_component_group = RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP(  # COMPONENT - Segment group for RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP - ORDER DETAIL SUPPLEMENT consisting of RXC, NTE|None
    pharmacy_or_treatment_component_order=rxc,  # RXC(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP TEMPLATE-----
"""


class RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP"""
    _hl7_name = """COMPONENT"""
    _hl7_description = """Segment group for RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP - ORDER DETAIL SUPPLEMENT consisting of RXC, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("16", "17")
    _c_components = (RXC, NTE)
    _c_name = ("RXC", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("pharmacy_or_treatment_component_order", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_component_order: RXC,  #  Required. RXC.16
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.17
    ):
        """
        None - `RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP>`_
        Segment group for RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP - ORDER DETAIL SUPPLEMENT consisting of RXC, NTE|None

        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 16 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 17 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )
        self.notes_and_comments = notes_and_comments

    @property  # get RXC.16
    def pharmacy_or_treatment_component_order(self) -> RXC:
        """
        id: RXC | use: R | rpt: 1 | seq: 16
        ---
        return_type: RXC.16: Pharmacy/Treatment Component Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_component_order.setter  # set RXC.16
    def pharmacy_or_treatment_component_order(self, rxc: RXC):
        """
        id: RXC | use: R | rpt: 1 | seq: 16
        ---
        param_type: RXC.16: Pharmacy/Treatment Component Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        self._c_data[0] = (rxc,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: NTE.17 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
