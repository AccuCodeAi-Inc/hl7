from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP import (
    RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP,
)
from ..segments.RXG import RXG
from ..segments.RXC import RXC
from ..segments.RXR import RXR
from ..segment_groups.RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP import (
    RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP,
)


"""
GIVE - RGV_O15_ORDER_GROUP_GIVE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_ORDER_GROUP_GIVE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RGV_O15_ORDER_GROUP_GIVE_GROUP
from utils.hl7.v2_5_1.segments import (
    RXG, RXR, RXC
)
from utils.hl7.v2_5_1.segment_groups import (
    RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP
)

rgv_o15_order_group_give_group = RGV_O15_ORDER_GROUP_GIVE_GROUP(  # GIVE - Segment group for RGV_O15_ORDER_GROUP - ORDER consisting of RXG, TIMING GIVE, RXR, RXC|None, OBSERVATION
    pharmacy_or_treatment_give=rxg,  # RXG(...)  # Required.
    timing_give=rgv_o15_order_group_give_group_timing_give_group,  # RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
    observation=rgv_o15_order_group_give_group_observation_group,  # RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_ORDER_GROUP_GIVE_GROUP TEMPLATE-----
"""


class RGV_O15_ORDER_GROUP_GIVE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RGV_O15_ORDER_GROUP_GIVE_GROUP"""
    _hl7_name = """GIVE"""
    _hl7_description = """Segment group for RGV_O15_ORDER_GROUP - ORDER consisting of RXG, TIMING GIVE, RXR, RXC|None, OBSERVATION"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_ORDER_GROUP_GIVE_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "R", "R", "O", "R")
    _c_aliases = ("22", "None", "25", "26", "None")
    _c_components = (RXG, RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, RXR, RXC, RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP)
    _c_name = ("RXG", "TIMING GIVE", "RXR", "RXC", "OBSERVATION")
    _c_is_group = (False, True, False, False, True)
    _c_attrs = ("pharmacy_or_treatment_give", "timing_give", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order", "observation",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_give: RXG,  #  Required. RXG.22
        timing_give: RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        | tuple[
            RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...
        ],  #  Required. (TQ1.23, TQ2.24, ...)
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.25
        observation: RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP
        | tuple[
            RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.27, NTE.28, ...)
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.26
    ):
        """
        None - `RGV_O15_ORDER_GROUP_GIVE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_ORDER_GROUP_GIVE_GROUP>`_
        Segment group for RGV_O15_ORDER_GROUP - ORDER consisting of RXG, TIMING GIVE, RXR, RXC|None, OBSERVATION

        :param pharmacy_or_treatment_give: Pharmacy/Treatment Give (id: RXG | seq: 22 | use: R | rpt: 1)
        :param timing_give: Timing Give segment group: [TQ1, TQ2|None] (id: TIMING GIVE | seq: 23, 24 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 25 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 26 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX|None, NTE|None] (id: OBSERVATION | seq: 27, 28 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.pharmacy_or_treatment_give = pharmacy_or_treatment_give
        self.timing_give = timing_give
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )
        self.observation = observation

    @property  # get RXG.22
    def pharmacy_or_treatment_give(self) -> RXG:
        """
        id: RXG | use: R | rpt: 1 | seq: 22
        ---
        return_type: RXG.22: Pharmacy/Treatment Give
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_give.setter  # set RXG.22
    def pharmacy_or_treatment_give(self, rxg: RXG):
        """
        id: RXG | use: R | rpt: 1 | seq: 22
        ---
        param_type: RXG.22: Pharmacy/Treatment Give
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        self._c_data[0] = (rxg,)

    @property  # get TIMING GIVE
    def timing_give(
        self,
    ) -> tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...]:
        """
        id: RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        """
        return self._c_data[1]

    @timing_give.setter  # set TIMING GIVE
    def timing_give(
        self,
        timing_give: RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        | tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...],
    ):
        """
        id: TIMING GIVE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP.None | tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_GIVE_GROUP_TIMING_GIVE_GROUP
        """
        if isinstance(timing_give, tuple):
            self._c_data[1] = timing_give
        else:
            self._c_data[1] = (timing_give,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 25
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 25
        ---
        param_type: RXR.25 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
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
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 26
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[3]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 26
        ---
        param_type: RXC.26 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[3] = rxc
        else:
            self._c_data[3] = (rxc,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP, ...]:
        """
        id: RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP
        | tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP.None | tuple[RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_GIVE_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)
