from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BLG import BLG
from ..segments.RXE import RXE
from ..segment_groups.RDE_O11_ORDER_GROUP_TIMING_GROUP import (
    RDE_O11_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.NTE import NTE
from ..segments.RXR import RXR
from ..segments.FT1 import FT1
from ..segments.CTI import CTI
from ..segment_groups.RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP,
)
from ..segment_groups.RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP import (
    RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP,
)
from ..segments.RXC import RXC
from ..segment_groups.RDE_O11_ORDER_GROUP_OBSERVATION_GROUP import (
    RDE_O11_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - RDE_O11_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDE_O11_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDE_O11_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXC, RXE, NTE, BLG, ORC, CTI, FT1
)
from utils.hl7.v2_5_1.segment_groups import (
    RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, RDE_O11_ORDER_GROUP_TIMING_GROUP, RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP
)

rde_o11_order_group = RDE_O11_ORDER_GROUP(  # ORDER - Segment group for RDE_O11 - Pharmacy/Treatment Encoded Order consisting of ORC, TIMING|None, ORDER DETAIL|None, RXE, NTE|None, TIMING ENCODED, RXR, RXC|None, OBSERVATION|None, FT1|None, BLG|None, CTI|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RDE_O11_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    pharmacy_or_treatment_encoded_order=rxe,  # RXE(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    timing_encoded=rde_o11_order_group_timing_encoded_group,  # RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
    observation=None,  # RDE_O11_ORDER_GROUP_OBSERVATION_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    billing=None,  # BLG(...) 
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDE_O11_ORDER_GROUP TEMPLATE-----
"""


class RDE_O11_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDE_O11_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RDE_O11 - Pharmacy/Treatment Encoded Order consisting of ORC, TIMING|None, ORDER DETAIL|None, RXE, NTE|None, TIMING ENCODED, RXR, RXC|None, OBSERVATION|None, FT1|None, BLG|None, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O11_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "R", "O", "R", "R", "O", "O", "O", "O", "O")
    _c_aliases = ("14", "None", "None", "22", "23", "None", "26", "27", "None", "30", "31", "32")
    _c_components = (ORC, RDE_O11_ORDER_GROUP_TIMING_GROUP, RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP, RXE, NTE, RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, RXR, RXC, RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, FT1, BLG, CTI)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL", "RXE", "NTE", "TIMING ENCODED", "RXR", "RXC", "OBSERVATION", "FT1", "BLG", "CTI")
    _c_is_group = (False, True, True, False, False, True, False, False, True, False, False, False)
    _c_attrs = ("common_order", "timing", "order_detail", "pharmacy_or_treatment_encoded_order", "notes_and_comments", "timing_encoded", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order", "observation", "financial_transaction", "billing", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        pharmacy_or_treatment_encoded_order: RXE,  #  Required. RXE.22
        timing_encoded: RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP
        | tuple[
            RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, ...
        ],  #  Required. (TQ1.24, TQ2.25, ...)
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.26
        timing: RDE_O11_ORDER_GROUP_TIMING_GROUP
        | tuple[RDE_O11_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        order_detail: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None = None,  #  RXO.17, NTE.18, RXR.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.23
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.27
        observation: RDE_O11_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.28, NTE.29, ...)
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.30
        billing: BLG | None = None,  #  BLG.31
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.32
    ):
        """
        None - `RDE_O11_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O11_ORDER_GROUP>`_
        Segment group for RDE_O11 - Pharmacy/Treatment Encoded Order consisting of ORC, TIMING|None, ORDER DETAIL|None, RXE, NTE|None, TIMING ENCODED, RXR, RXC|None, OBSERVATION|None, FT1|None, BLG|None, CTI|None

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, NTE|None, RXR, COMPONENT|None] (id: ORDER DETAIL | seq: 17, 18, 19, None | use: O | rpt: 1)
        :param pharmacy_or_treatment_encoded_order: Pharmacy/Treatment Encoded Order (id: RXE | seq: 22 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 23 | use: O | rpt: *)
        :param timing_encoded: Timing Encoded segment group: [TQ1, TQ2|None] (id: TIMING ENCODED | seq: 24, 25 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 26 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 27 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 28, 29 | use: O | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 30 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 31 | use: O | rpt: 1)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 32 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail
        self.pharmacy_or_treatment_encoded_order = pharmacy_or_treatment_encoded_order
        self.notes_and_comments = notes_and_comments
        self.timing_encoded = timing_encoded
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )
        self.observation = observation
        self.financial_transaction = financial_transaction
        self.billing = billing
        self.clinical_trial_identification = clinical_trial_identification

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
    def timing(self) -> tuple[RDE_O11_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RDE_O11_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDE_O11_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RDE_O11_ORDER_GROUP_TIMING_GROUP
        | tuple[RDE_O11_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDE_O11_ORDER_GROUP_TIMING_GROUP.None | tuple[RDE_O11_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self) -> RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self, order_detail: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP | None):
        """
        id: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)

    @property  # get RXE.22
    def pharmacy_or_treatment_encoded_order(self) -> RXE:
        """
        id: RXE | use: R | rpt: 1 | seq: 22
        ---
        return_type: RXE.22: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        return self._c_data[3][0]

    @pharmacy_or_treatment_encoded_order.setter  # set RXE.22
    def pharmacy_or_treatment_encoded_order(self, rxe: RXE):
        """
        id: RXE | use: R | rpt: 1 | seq: 22
        ---
        param_type: RXE.22: Pharmacy/Treatment Encoded Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXE
        """
        self._c_data[3] = (rxe,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[4]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: NTE.23 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[4] = nte
        else:
            self._c_data[4] = (nte,)

    @property  # get TIMING ENCODED
    def timing_encoded(self) -> tuple[RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, ...]:
        """
        id: RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP
        """
        return self._c_data[5]

    @timing_encoded.setter  # set TIMING ENCODED
    def timing_encoded(
        self,
        timing_encoded: RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP
        | tuple[RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, ...],
    ):
        """
        id: TIMING ENCODED SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP.None | tuple[RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_TIMING_ENCODED_GROUP
        """
        if isinstance(timing_encoded, tuple):
            self._c_data[5] = timing_encoded
        else:
            self._c_data[5] = (timing_encoded,)

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
    ) -> tuple[RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: RDE_O11_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[8]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RDE_O11_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDE_O11_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[RDE_O11_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_OBSERVATION_GROUP
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

    @property  # get BLG.31
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 31
        ---
        return_type: BLG.31: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[10][0]

    @billing.setter  # set BLG.31
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 31
        ---
        param_type: BLG.31: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[10] = (blg,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 32
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[11]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 32
        ---
        param_type: CTI.32 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[11] = cti
        else:
            self._c_data[11] = (cti,)
