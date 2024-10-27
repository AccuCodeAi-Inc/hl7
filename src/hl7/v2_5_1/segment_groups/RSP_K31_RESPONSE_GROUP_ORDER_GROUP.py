from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP import (
    RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC
from ..segments.RXD import RXD
from ..segment_groups.RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP import (
    RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP,
)
from ..segments.RXC import RXC
from ..segments.RXR import RXR
from ..segment_groups.RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP,
)


"""
ORDER - RSP_K31_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_K31_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K31_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, ORC, RXD, RXC
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

rsp_k31_response_group_order_group = RSP_K31_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for RSP_K31_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, RXR, RXC|None, OBSERVATION
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    encoding=None,  # RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP(...) 
    pharmacy_or_treatment_dispense=rxd,  # RXD(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
    observation=rsp_k31_response_group_order_group_observation_group,  # RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_K31_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RSP_K31_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_K31_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RSP_K31_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, RXR, RXC|None, OBSERVATION"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K31_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "R", "R", "O", "R")
    _c_aliases = ("14", "None", "None", "None", "27", "28", "29", "None")
    _c_components = (ORC, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP, RXD, RXR, RXC, RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL", "ENCODING", "RXD", "RXR", "RXC", "OBSERVATION")
    _c_is_group = (False, True, True, True, False, False, False, True)
    _c_attrs = ("common_order", "timing", "order_detail", "encoding", "pharmacy_or_treatment_dispense", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order", "observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        pharmacy_or_treatment_dispense: RXD,  #  Required. RXD.27
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.28
        observation: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[
            RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.30, NTE.31, ...)
        timing: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        order_detail: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None = None,  #  RXO.17, NTE.18, RXR.19
        encoding: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.22, RXR.25, RXC.26
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.29
    ):
        """
        None - `RSP_K31_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K31_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for RSP_K31_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, RXR, RXC|None, OBSERVATION

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, NTE|None, RXR, COMPONENTS|None] (id: ORDER DETAIL | seq: 17, 18, 19, None | use: O | rpt: 1)
        :param encoding: Encoding segment group: [RXE, TIMING ENCODED, RXR, RXC|None] (id: ENCODING | seq: 22, None, 25, 26 | use: O | rpt: 1)
        :param pharmacy_or_treatment_dispense: Pharmacy/Treatment Dispense (id: RXD | seq: 27 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 28 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 29 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX|None, NTE|None] (id: OBSERVATION | seq: 30, 31 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail
        self.encoding = encoding
        self.pharmacy_or_treatment_dispense = pharmacy_or_treatment_dispense
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )
        self.observation = observation

    @property  # get ORC.14
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        return_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.14
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        param_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self,
    ) -> RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(
        self, order_detail: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | None
    ):
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)

    @property  # get RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[3][0]

    @encoding.setter  # set RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(
        self, encoding: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | None
    ):
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[3] = (encoding,)

    @property  # get RXD.27
    def pharmacy_or_treatment_dispense(self) -> RXD:
        """
        id: RXD | use: R | rpt: 1 | seq: 27
        ---
        return_type: RXD.27: Pharmacy/Treatment Dispense
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD
        """
        return self._c_data[4][0]

    @pharmacy_or_treatment_dispense.setter  # set RXD.27
    def pharmacy_or_treatment_dispense(self, rxd: RXD):
        """
        id: RXD | use: R | rpt: 1 | seq: 27
        ---
        param_type: RXD.27: Pharmacy/Treatment Dispense
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD
        """
        self._c_data[4] = (rxd,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 28
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[5]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 28
        ---
        param_type: RXR.28 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[5] = rxr
        else:
            self._c_data[5] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[6]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        param_type: RXC.29 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[6] = rxc
        else:
            self._c_data[6] = (rxc,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...]:
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[7]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[7] = observation
        else:
            self._c_data[7] = (observation,)
