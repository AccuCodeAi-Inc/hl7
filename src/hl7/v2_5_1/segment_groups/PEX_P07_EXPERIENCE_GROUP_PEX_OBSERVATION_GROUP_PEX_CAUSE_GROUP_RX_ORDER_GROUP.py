from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP import (
    PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP,
)
from ..segments.RXE import RXE
from ..segments.RXR import RXR


"""
RX ORDER - PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXE, RXR
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP
)

pex_p07_experience_group_pex_observation_group_pex_cause_group_rx_order_group = PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP(  # RX ORDER - Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of RXE, TIMING QTY, RXR|None
    pharmacy_or_treatment_encoded_order=rxe,  # RXE(...)  # Required.
    timing_qty=pex_p07_experience_group_pex_observation_group_pex_cause_group_rx_order_group_timing_qty_group,  # PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP(...)  # Required.
    pharmacy_or_treatment_route=None,  # RXR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP TEMPLATE-----
"""


class PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP"""
    _hl7_name = """RX ORDER"""
    _hl7_description = """Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of RXE, TIMING QTY, RXR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("12", "None", "15")
    _c_components = (RXE, PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP, RXR)
    _c_name = ("RXE", "TIMING QTY", "RXR")
    _c_is_group = (False, True, False)
    _c_attrs = ("pharmacy_or_treatment_encoded_order", "timing_qty", "pharmacy_or_treatment_route",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_encoded_order: RXE,  #  Required. RXE.12
        timing_qty: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP
        | tuple[
            PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP,
            ...,
        ],  #  Required. (TQ1.13, TQ2.14, ...)
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...] | None = None,  #  RXR.15
    ):
        """
        None - `PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP>`_
        Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of RXE, TIMING QTY, RXR|None

        :param pharmacy_or_treatment_encoded_order: Pharmacy/Treatment Encoded Order (id: RXE | seq: 12 | use: R | rpt: 1)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 13, 14 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.pharmacy_or_treatment_encoded_order = pharmacy_or_treatment_encoded_order
        self.timing_qty = timing_qty
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route

    @property  # get RXE.12
    def pharmacy_or_treatment_encoded_order(self) -> RXE:
        """
        id: RXE | use: R | rpt: 1 | seq: 12
        ---
        return_type: RXE.12: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_encoded_order.setter  # set RXE.12
    def pharmacy_or_treatment_encoded_order(self, rxe: RXE):
        """
        id: RXE | use: R | rpt: 1 | seq: 12
        ---
        param_type: RXE.12: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        self._c_data[0] = (rxe,)

    @property  # get TIMING QTY
    def timing_qty(
        self,
    ) -> tuple[
        PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP,
        ...,
    ]:
        """
        id: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP
        """
        return self._c_data[1]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP
        | tuple[
            PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP,
            ...,
        ],
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP.None | tuple[PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_RX_ORDER_GROUP_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[1] = timing_qty
        else:
            self._c_data[1] = (timing_qty,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...] | tuple[None]:
        """
        id: RXR SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...] | None):
        """
        id: RXR SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: RXR.15 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)
