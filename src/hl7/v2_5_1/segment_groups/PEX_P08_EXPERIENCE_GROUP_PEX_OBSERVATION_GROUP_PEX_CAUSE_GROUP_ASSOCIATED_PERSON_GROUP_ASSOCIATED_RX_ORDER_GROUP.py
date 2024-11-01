from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP,
)
from ..segments.RXR import RXR
from ..segments.RXE import RXE


"""
ASSOCIATED RX ORDER - PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXE
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP
)

pex_p08_experience_group_pex_observation_group_pex_cause_group_associated_person_group_associated_rx_order_group = PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP(  # ASSOCIATED RX ORDER - Segment group for PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP - ASSOCIATED PERSON consisting of RXE, NK1 TIMING QTY, RXR|None
    pharmacy_or_treatment_encoded_order=rxe,  # RXE(...)  # Required.
    nk1_timing_qty=pex_p08_experience_group_pex_observation_group_pex_cause_group_associated_person_group_associated_rx_order_group_nk1_timing_qty_group,  # PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP(...)  # Required.
    pharmacy_or_treatment_route=None,  # RXR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP TEMPLATE-----
"""


class PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP"""
    _hl7_name = """ASSOCIATED RX ORDER"""
    _hl7_description = """Segment group for PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP - ASSOCIATED PERSON consisting of RXE, NK1 TIMING QTY, RXR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("22", "None", "25")
    _c_components = (RXE, PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP, RXR)
    _c_name = ("RXE", "NK1 TIMING QTY", "RXR")
    _c_is_group = (False, True, False)
    _c_attrs = ("pharmacy_or_treatment_encoded_order", "nk1_timing_qty", "pharmacy_or_treatment_route",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_encoded_order: RXE,  #  Required. RXE.22
        nk1_timing_qty: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP,
            ...,
        ],  #  Required. (TQ1.23, TQ2.24, ...)
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...] | None = None,  #  RXR.25
    ):
        """
        None - `PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP>`_
        Segment group for PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP - ASSOCIATED PERSON consisting of RXE, NK1 TIMING QTY, RXR|None

        :param pharmacy_or_treatment_encoded_order: Pharmacy/Treatment Encoded Order (id: RXE | seq: 22 | use: R | rpt: 1)
        :param nk1_timing_qty: Nk1 Timing Qty segment group: [TQ1, TQ2|None] (id: NK1 TIMING QTY | seq: 23, 24 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 25 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.pharmacy_or_treatment_encoded_order = pharmacy_or_treatment_encoded_order
        self.nk1_timing_qty = nk1_timing_qty
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route

    @property  # get RXE.22
    def pharmacy_or_treatment_encoded_order(self) -> RXE:
        """
        id: RXE | use: R | rpt: 1 | seq: 22
        ---
        return_type: RXE.22: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_encoded_order.setter  # set RXE.22
    def pharmacy_or_treatment_encoded_order(self, rxe: RXE):
        """
        id: RXE | use: R | rpt: 1 | seq: 22
        ---
        param_type: RXE.22: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        self._c_data[0] = (rxe,)

    @property  # get NK1 TIMING QTY
    def nk1_timing_qty(
        self,
    ) -> tuple[
        PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP,
        ...,
    ]:
        """
        id: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP
        """
        return self._c_data[1]

    @nk1_timing_qty.setter  # set NK1 TIMING QTY
    def nk1_timing_qty(
        self,
        nk1_timing_qty: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP
        | tuple[
            PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP,
            ...,
        ],
    ):
        """
        id: NK1 TIMING QTY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP.None | tuple[PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P08_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_ASSOCIATED_PERSON_GROUP_ASSOCIATED_RX_ORDER_GROUP_NK1_TIMING_QTY_GROUP
        """
        if isinstance(nk1_timing_qty, tuple):
            self._c_data[1] = nk1_timing_qty
        else:
            self._c_data[1] = (nk1_timing_qty,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...] | tuple[None]:
        """
        id: RXR SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...] | None):
        """
        id: RXR SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        param_type: RXR.25 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)
