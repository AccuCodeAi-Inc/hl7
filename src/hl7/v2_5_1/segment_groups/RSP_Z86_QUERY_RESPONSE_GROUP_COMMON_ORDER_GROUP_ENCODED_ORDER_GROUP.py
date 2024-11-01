from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXC import RXC
from ..segment_groups.RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP,
)
from ..segments.RXE import RXE


"""
ENCODED ORDER - RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXC, RXR, RXE
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
)

rsp_z86_query_response_group_common_order_group_encoded_order_group = RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP(  # ENCODED ORDER - Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXE, TIMING ENCODED|None, RXR, RXC|None
    pharmacy_or_treatment_encoded_order=rxe,  # RXE(...)  # Required.
    timing_encoded=None,  # RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP TEMPLATE-----
"""


class RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP"""
    _hl7_name = """ENCODED ORDER"""
    _hl7_description = """Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXE, TIMING ENCODED|None, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("17", "None", "20", "21")
    _c_components = (RXE, RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP, RXR, RXC)
    _c_name = ("RXE", "TIMING ENCODED", "RXR", "RXC")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("pharmacy_or_treatment_encoded_order", "timing_encoded", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_encoded_order: RXE,  #  Required. RXE.17
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.20
        timing_encoded: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
        | tuple[
            RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.18, TQ2.19, ...)
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.21
    ):
        """
        None - `RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP>`_
        Segment group for RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of RXE, TIMING ENCODED|None, RXR, RXC|None

        :param pharmacy_or_treatment_encoded_order: Pharmacy/Treatment Encoded Order (id: RXE | seq: 17 | use: R | rpt: 1)
        :param timing_encoded: Timing Encoded segment group: [TQ1, TQ2|None] (id: TIMING ENCODED | seq: 18, 19 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 20 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pharmacy_or_treatment_encoded_order = pharmacy_or_treatment_encoded_order
        self.timing_encoded = timing_encoded
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXE.17
    def pharmacy_or_treatment_encoded_order(self) -> RXE:
        """
        id: RXE | use: R | rpt: 1 | seq: 17
        ---
        return_type: RXE.17: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_encoded_order.setter  # set RXE.17
    def pharmacy_or_treatment_encoded_order(self, rxe: RXE):
        """
        id: RXE | use: R | rpt: 1 | seq: 17
        ---
        param_type: RXE.17: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        self._c_data[0] = (rxe,)

    @property  # get TIMING ENCODED
    def timing_encoded(
        self,
    ) -> (
        tuple[
            RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
        """
        return self._c_data[1]

    @timing_encoded.setter  # set TIMING ENCODED
    def timing_encoded(
        self,
        timing_encoded: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
        | tuple[
            RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: TIMING ENCODED SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP.None | tuple[RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z86_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_ENCODED_ORDER_GROUP_TIMING_ENCODED_GROUP
        """
        if isinstance(timing_encoded, tuple):
            self._c_data[1] = timing_encoded
        else:
            self._c_data[1] = (timing_encoded,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 20
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 20
        ---
        param_type: RXR.20 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[3]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: RXC.21 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[3] = rxc
        else:
            self._c_data[3] = (rxc,)
