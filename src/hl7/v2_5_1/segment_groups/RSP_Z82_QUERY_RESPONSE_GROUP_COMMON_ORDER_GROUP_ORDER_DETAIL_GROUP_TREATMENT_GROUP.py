from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXC import RXC
from ..segments.NTE import NTE


"""
TREATMENT - RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, RXC
)

rsp_z82_query_response_group_common_order_group_order_detail_group_treatment_group = RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP(  # TREATMENT - Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of RXC, NTE|None
    pharmacy_or_treatment_component_order=rxc,  # RXC(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP TEMPLATE-----
"""


class RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP"""
    _hl7_name = """TREATMENT"""
    _hl7_description = """Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of RXC, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (65535, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("20", "21")
    _c_components = (RXC, NTE)
    _c_name = ("RXC", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("pharmacy_or_treatment_component_order", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...],  #  Required. RXC.20
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.21
    ):
        """
        None - `RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP_TREATMENT_GROUP>`_
        Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of RXC, NTE|None

        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 20 | use: R | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )
        self.notes_and_comments = notes_and_comments

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...]:
        """
        id: RXC SEGMENT GROUP | use: R | rpt: * | seq: 20
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[0]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...]):
        """
        id: RXC SEGMENT GROUP | use: R | rpt: * | seq: 20
        ---
        param_type: RXC.20 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[0] = rxc
        else:
            self._c_data[0] = (rxc,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: NTE.21 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
