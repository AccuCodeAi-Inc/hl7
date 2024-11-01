from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BLG import BLG
from ..segments.RXO import RXO
from ..segments.FT1 import FT1
from ..segments.ORC import ORC
from ..segments.RXR import RXR
from ..segment_groups.OMP_O09_ORDER_GROUP_TIMING_GROUP import (
    OMP_O09_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.OMP_O09_ORDER_GROUP_COMPONENT_GROUP import (
    OMP_O09_ORDER_GROUP_COMPONENT_GROUP,
)
from ..segments.NTE import NTE
from ..segment_groups.OMP_O09_ORDER_GROUP_OBSERVATION_GROUP import (
    OMP_O09_ORDER_GROUP_OBSERVATION_GROUP,
)


"""
ORDER - OMP_O09_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMP_O09_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMP_O09_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, ORC, RXR, RXO, FT1, BLG
)
from utils.hl7.v2_5_1.segment_groups import (
    OMP_O09_ORDER_GROUP_COMPONENT_GROUP, OMP_O09_ORDER_GROUP_TIMING_GROUP, OMP_O09_ORDER_GROUP_OBSERVATION_GROUP
)

omp_o09_order_group = OMP_O09_ORDER_GROUP(  # ORDER - Segment group for OMP_O09 - Pharmacy/Treatment Order consisting of ORC, TIMING|None, RXO, NTE|None, RXR, COMPONENT|None, OBSERVATION|None, FT1|None, BLG|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # OMP_O09_ORDER_GROUP_TIMING_GROUP(...) 
    pharmacy_or_treatment_order=rxo,  # RXO(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    component=None,  # OMP_O09_ORDER_GROUP_COMPONENT_GROUP(...) 
    observation=None,  # OMP_O09_ORDER_GROUP_OBSERVATION_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    billing=None,  # BLG(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMP_O09_ORDER_GROUP TEMPLATE-----
"""


class OMP_O09_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMP_O09_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OMP_O09 - Pharmacy/Treatment Order consisting of ORC, TIMING|None, RXO, NTE|None, RXR, COMPONENT|None, OBSERVATION|None, FT1|None, BLG|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMP_O09_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535, 65535, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "O", "R", "O", "O", "O", "O")
    _c_aliases = ("14", "None", "17", "18", "19", "None", "None", "24", "25")
    _c_components = (ORC, OMP_O09_ORDER_GROUP_TIMING_GROUP, RXO, NTE, RXR, OMP_O09_ORDER_GROUP_COMPONENT_GROUP, OMP_O09_ORDER_GROUP_OBSERVATION_GROUP, FT1, BLG)
    _c_name = ("ORC", "TIMING", "RXO", "NTE", "RXR", "COMPONENT", "OBSERVATION", "FT1", "BLG")
    _c_is_group = (False, True, False, False, False, True, True, False, False)
    _c_attrs = ("common_order", "timing", "pharmacy_or_treatment_order", "notes_and_comments", "pharmacy_or_treatment_route", "component", "observation", "financial_transaction", "billing",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        pharmacy_or_treatment_order: RXO,  #  Required. RXO.17
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.19
        timing: OMP_O09_ORDER_GROUP_TIMING_GROUP
        | tuple[OMP_O09_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.18
        component: OMP_O09_ORDER_GROUP_COMPONENT_GROUP
        | tuple[OMP_O09_ORDER_GROUP_COMPONENT_GROUP, ...]
        | None = None,  #  (RXC.20, NTE.21, ...)
        observation: OMP_O09_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMP_O09_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.22, NTE.23, ...)
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.24
        billing: BLG | None = None,  #  BLG.25
    ):
        """
        None - `OMP_O09_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMP_O09_ORDER_GROUP>`_
        Segment group for OMP_O09 - Pharmacy/Treatment Order consisting of ORC, TIMING|None, RXO, NTE|None, RXR, COMPONENT|None, OBSERVATION|None, FT1|None, BLG|None

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 17 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 18 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 19 | use: R | rpt: *)
        :param component: Component segment group: [RXC, NTE|None] (id: COMPONENT | seq: 20, 21 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 22, 23 | use: O | rpt: *)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 24 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 25 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.common_order = common_order
        self.timing = timing
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.component = component
        self.observation = observation
        self.financial_transaction = financial_transaction
        self.billing = billing

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
    def timing(self) -> tuple[OMP_O09_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: OMP_O09_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMP_O09_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMP_O09_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: OMP_O09_ORDER_GROUP_TIMING_GROUP
        | tuple[OMP_O09_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMP_O09_ORDER_GROUP_TIMING_GROUP.None | tuple[OMP_O09_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMP_O09_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RXO.17
    def pharmacy_or_treatment_order(self) -> RXO:
        """
        id: RXO | use: R | rpt: 1 | seq: 17
        ---
        return_type: RXO.17: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[2][0]

    @pharmacy_or_treatment_order.setter  # set RXO.17
    def pharmacy_or_treatment_order(self, rxo: RXO):
        """
        id: RXO | use: R | rpt: 1 | seq: 17
        ---
        param_type: RXO.17: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[2] = (rxo,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: NTE.18 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 19
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[4]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 19
        ---
        param_type: RXR.19 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[4] = rxr
        else:
            self._c_data[4] = (rxr,)

    @property  # get COMPONENT
    def component(
        self,
    ) -> tuple[OMP_O09_ORDER_GROUP_COMPONENT_GROUP, ...] | tuple[None]:
        """
        id: OMP_O09_ORDER_GROUP_COMPONENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMP_O09_ORDER_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMP_O09_ORDER_GROUP_COMPONENT_GROUP
        """
        return self._c_data[5]

    @component.setter  # set COMPONENT
    def component(
        self,
        component: OMP_O09_ORDER_GROUP_COMPONENT_GROUP
        | tuple[OMP_O09_ORDER_GROUP_COMPONENT_GROUP, ...]
        | None,
    ):
        """
        id: COMPONENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMP_O09_ORDER_GROUP_COMPONENT_GROUP.None | tuple[OMP_O09_ORDER_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMP_O09_ORDER_GROUP_COMPONENT_GROUP
        """
        if isinstance(component, tuple):
            self._c_data[5] = component
        else:
            self._c_data[5] = (component,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[OMP_O09_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: OMP_O09_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMP_O09_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMP_O09_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[6]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OMP_O09_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMP_O09_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMP_O09_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[OMP_O09_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMP_O09_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[6] = observation
        else:
            self._c_data[6] = (observation,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[7]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        param_type: FT1.24 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[7] = ft1
        else:
            self._c_data[7] = (ft1,)

    @property  # get BLG.25
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 25
        ---
        return_type: BLG.25: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[8][0]

    @billing.setter  # set BLG.25
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 25
        ---
        param_type: BLG.25: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[8] = (blg,)
