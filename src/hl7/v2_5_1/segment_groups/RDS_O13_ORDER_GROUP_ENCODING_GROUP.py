from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXC import RXC
from ..segment_groups.RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP import (
    RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP,
)
from ..segments.RXE import RXE
from ..segments.NTE import NTE


"""
ENCODING - RDS_O13_ORDER_GROUP_ENCODING_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP_ENCODING_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDS_O13_ORDER_GROUP_ENCODING_GROUP
from utils.hl7.v2_5_1.segments import (
    RXC, NTE, RXR, RXE
)
from utils.hl7.v2_5_1.segment_groups import (
    RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP
)

rds_o13_order_group_encoding_group = RDS_O13_ORDER_GROUP_ENCODING_GROUP(  # ENCODING - Segment group for RDS_O13_ORDER_GROUP - ORDER consisting of RXE, NTE|None, TIMING ENCODED, RXR, RXC|None
    pharmacy_or_treatment_encoded_order=rxe,  # RXE(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    timing_encoded=rds_o13_order_group_encoding_group_timing_encoded_group,  # RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP_ENCODING_GROUP TEMPLATE-----
"""


class RDS_O13_ORDER_GROUP_ENCODING_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDS_O13_ORDER_GROUP_ENCODING_GROUP"""
    _hl7_name = """ENCODING"""
    _hl7_description = """Segment group for RDS_O13_ORDER_GROUP - ORDER consisting of RXE, NTE|None, TIMING ENCODED, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP_ENCODING_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O")
    _c_aliases = ("18", "19", "None", "22", "23")
    _c_components = (RXE, NTE, RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP, RXR, RXC)
    _c_name = ("RXE", "NTE", "TIMING ENCODED", "RXR", "RXC")
    _c_is_group = (False, False, True, False, False)
    _c_attrs = ("pharmacy_or_treatment_encoded_order", "notes_and_comments", "timing_encoded", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_encoded_order: RXE,  #  Required. RXE.18
        timing_encoded: RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP
        | tuple[
            RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP, ...
        ],  #  Required. (TQ1.20, TQ2.21, ...)
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.22
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.23
    ):
        """
        None - `RDS_O13_ORDER_GROUP_ENCODING_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP_ENCODING_GROUP>`_
        Segment group for RDS_O13_ORDER_GROUP - ORDER consisting of RXE, NTE|None, TIMING ENCODED, RXR, RXC|None

        :param pharmacy_or_treatment_encoded_order: Pharmacy/Treatment Encoded Order (id: RXE | seq: 18 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        :param timing_encoded: Timing Encoded segment group: [TQ1, TQ2|None] (id: TIMING ENCODED | seq: 20, 21 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 22 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 23 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.pharmacy_or_treatment_encoded_order = pharmacy_or_treatment_encoded_order
        self.notes_and_comments = notes_and_comments
        self.timing_encoded = timing_encoded
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXE.18
    def pharmacy_or_treatment_encoded_order(self) -> RXE:
        """
        id: RXE | use: R | rpt: 1 | seq: 18
        ---
        return_type: RXE.18: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_encoded_order.setter  # set RXE.18
    def pharmacy_or_treatment_encoded_order(self, rxe: RXE):
        """
        id: RXE | use: R | rpt: 1 | seq: 18
        ---
        param_type: RXE.18: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        self._c_data[0] = (rxe,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: NTE.19 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get TIMING ENCODED
    def timing_encoded(
        self,
    ) -> tuple[RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP, ...]:
        """
        id: RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP
        """
        return self._c_data[2]

    @timing_encoded.setter  # set TIMING ENCODED
    def timing_encoded(
        self,
        timing_encoded: RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP
        | tuple[RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP, ...],
    ):
        """
        id: TIMING ENCODED SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP.None | tuple[RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ENCODING_GROUP_TIMING_ENCODED_GROUP
        """
        if isinstance(timing_encoded, tuple):
            self._c_data[2] = timing_encoded
        else:
            self._c_data[2] = (timing_encoded,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 22
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[3]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 22
        ---
        param_type: RXR.22 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[3] = rxr
        else:
            self._c_data[3] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[4]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: RXC.23 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[4] = rxc
        else:
            self._c_data[4] = (rxc,)
