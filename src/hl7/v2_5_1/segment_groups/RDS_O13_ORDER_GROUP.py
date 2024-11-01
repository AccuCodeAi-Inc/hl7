from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXD import RXD
from ..segment_groups.RDS_O13_ORDER_GROUP_OBSERVATION_GROUP import (
    RDS_O13_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.RXC import RXC
from ..segment_groups.RDS_O13_ORDER_GROUP_ENCODING_GROUP import (
    RDS_O13_ORDER_GROUP_ENCODING_GROUP,
)
from ..segments.ORC import ORC
from ..segments.RXR import RXR
from ..segments.NTE import NTE
from ..segments.FT1 import FT1
from ..segment_groups.RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP,
)
from ..segment_groups.RDS_O13_ORDER_GROUP_TIMING_GROUP import (
    RDS_O13_ORDER_GROUP_TIMING_GROUP,
)


"""
ORDER - RDS_O13_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDS_O13_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    FT1, RXR, NTE, RXD, RXC, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP, RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, RDS_O13_ORDER_GROUP_ENCODING_GROUP, RDS_O13_ORDER_GROUP_TIMING_GROUP
)

rds_o13_order_group = RDS_O13_ORDER_GROUP(  # ORDER - Segment group for RDS_O13 - Pharmacy/Treatment Dispense consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, NTE|None, RXR, RXC|None, OBSERVATION|None, FT1|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RDS_O13_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    encoding=None,  # RDS_O13_ORDER_GROUP_ENCODING_GROUP(...) 
    pharmacy_or_treatment_dispense=rxd,  # RXD(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
    observation=None,  # RDS_O13_ORDER_GROUP_OBSERVATION_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP TEMPLATE-----
"""


class RDS_O13_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDS_O13_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RDS_O13 - Pharmacy/Treatment Dispense consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, NTE|None, RXR, RXC|None, OBSERVATION|None, FT1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "R", "O", "R", "O", "O", "O")
    _c_aliases = ("10", "None", "None", "None", "24", "25", "26", "27", "None", "30")
    _c_components = (ORC, RDS_O13_ORDER_GROUP_TIMING_GROUP, RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP, RDS_O13_ORDER_GROUP_ENCODING_GROUP, RXD, NTE, RXR, RXC, RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, FT1)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL", "ENCODING", "RXD", "NTE", "RXR", "RXC", "OBSERVATION", "FT1")
    _c_is_group = (False, True, True, True, False, False, False, False, True, False)
    _c_attrs = ("common_order", "timing", "order_detail", "encoding", "pharmacy_or_treatment_dispense", "notes_and_comments", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order", "observation", "financial_transaction",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.10
        pharmacy_or_treatment_dispense: RXD,  #  Required. RXD.24
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.26
        timing: RDS_O13_ORDER_GROUP_TIMING_GROUP
        | tuple[RDS_O13_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.11, TQ2.12, ...)
        order_detail: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP | None = None,  #  RXO.13
        encoding: RDS_O13_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.18, NTE.19, RXR.22, RXC.23
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.25
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.27
        observation: RDS_O13_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.28, NTE.29, ...)
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.30
    ):
        """
        None - `RDS_O13_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP>`_
        Segment group for RDS_O13 - Pharmacy/Treatment Dispense consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, NTE|None, RXR, RXC|None, OBSERVATION|None, FT1|None

        :param common_order: Common Order (id: ORC | seq: 10 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 11, 12 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, ORDER DETAIL SUPPLEMENT|None] (id: ORDER DETAIL | seq: 13, None | use: O | rpt: 1)
        :param encoding: Encoding segment group: [RXE, NTE|None, TIMING ENCODED, RXR, RXC|None] (id: ENCODING | seq: 18, 19, None, 22, 23 | use: O | rpt: 1)
        :param pharmacy_or_treatment_dispense: Pharmacy/Treatment Dispense (id: RXD | seq: 24 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 25 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 26 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 27 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 28, 29 | use: O | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 30 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail
        self.encoding = encoding
        self.pharmacy_or_treatment_dispense = pharmacy_or_treatment_dispense
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )
        self.observation = observation
        self.financial_transaction = financial_transaction

    @property  # get ORC.10
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 10
        ---
        return_type: ORC.10: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.10
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 10
        ---
        param_type: ORC.10: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[RDS_O13_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RDS_O13_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDS_O13_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RDS_O13_ORDER_GROUP_TIMING_GROUP
        | tuple[RDS_O13_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDS_O13_ORDER_GROUP_TIMING_GROUP.None | tuple[RDS_O13_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self) -> RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self, order_detail: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP | None):
        """
        id: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)

    @property  # get RDS_O13_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RDS_O13_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RDS_O13_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RDS_O13_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[3][0]

    @encoding.setter  # set RDS_O13_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self, encoding: RDS_O13_ORDER_GROUP_ENCODING_GROUP | None):
        """
        id: RDS_O13_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RDS_O13_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[3] = (encoding,)

    @property  # get RXD.24
    def pharmacy_or_treatment_dispense(self) -> RXD:
        """
        id: RXD | use: R | rpt: 1 | seq: 24
        ---
        return_type: RXD.24: Pharmacy/Treatment Dispense
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD
        """
        return self._c_data[4][0]

    @pharmacy_or_treatment_dispense.setter  # set RXD.24
    def pharmacy_or_treatment_dispense(self, rxd: RXD):
        """
        id: RXD | use: R | rpt: 1 | seq: 24
        ---
        param_type: RXD.24: Pharmacy/Treatment Dispense
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD
        """
        self._c_data[4] = (rxd,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[5]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        param_type: NTE.25 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[5] = nte
        else:
            self._c_data[5] = (nte,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 26
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[6]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 26
        ---
        param_type: RXR.26 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[6] = rxr
        else:
            self._c_data[6] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[7]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        param_type: RXC.27 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[7] = rxc
        else:
            self._c_data[7] = (rxc,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: RDS_O13_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[8]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RDS_O13_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDS_O13_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[RDS_O13_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[8] = observation
        else:
            self._c_data[8] = (observation,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 30
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[9]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 30
        ---
        param_type: FT1.30 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[9] = ft1
        else:
            self._c_data[9] = (ft1,)
