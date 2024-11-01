from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.VXR_V03_ORDER_GROUP_OBSERVATION_GROUP import (
    VXR_V03_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC
from ..segments.RXR import RXR
from ..segments.RXA import RXA
from ..segment_groups.VXR_V03_ORDER_GROUP_TIMING_GROUP import (
    VXR_V03_ORDER_GROUP_TIMING_GROUP,
)


"""
ORDER - VXR_V03_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::VXR_V03_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXR_V03_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXA, RXR, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    VXR_V03_ORDER_GROUP_TIMING_GROUP, VXR_V03_ORDER_GROUP_OBSERVATION_GROUP
)

vxr_v03_order_group = VXR_V03_ORDER_GROUP(  # ORDER - Segment group for VXR_V03 - Vaccination Record Response consisting of ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # VXR_V03_ORDER_GROUP_TIMING_GROUP(...) 
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=None,  # RXR(...) 
    observation=None,  # VXR_V03_ORDER_GROUP_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::VXR_V03_ORDER_GROUP TEMPLATE-----
"""


class VXR_V03_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """VXR_V03_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for VXR_V03 - Vaccination Record Response consisting of ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXR_V03_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O")
    _c_aliases = ("15", "None", "18", "19", "None")
    _c_components = (ORC, VXR_V03_ORDER_GROUP_TIMING_GROUP, RXA, RXR, VXR_V03_ORDER_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORC", "TIMING", "RXA", "RXR", "OBSERVATION")
    _c_is_group = (False, True, False, False, True)
    _c_attrs = ("common_order", "timing", "pharmacy_or_treatment_administration", "pharmacy_or_treatment_route", "observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.15
        pharmacy_or_treatment_administration: RXA,  #  Required. RXA.18
        timing: VXR_V03_ORDER_GROUP_TIMING_GROUP
        | tuple[VXR_V03_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.16, TQ2.17, ...)
        pharmacy_or_treatment_route: RXR | None = None,  #  RXR.19
        observation: VXR_V03_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[VXR_V03_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.20, NTE.21, ...)
    ):
        """
        None - `VXR_V03_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXR_V03_ORDER_GROUP>`_
        Segment group for VXR_V03 - Vaccination Record Response consisting of ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None

        :param common_order: Common Order (id: ORC | seq: 15 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 16, 17 | use: O | rpt: *)
        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 18 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 19 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 20, 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.observation = observation

    @property  # get ORC.15
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 15
        ---
        return_type: ORC.15: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.15
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 15
        ---
        param_type: ORC.15: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[VXR_V03_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: VXR_V03_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXR_V03_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: VXR_V03_ORDER_GROUP_TIMING_GROUP
        | tuple[VXR_V03_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXR_V03_ORDER_GROUP_TIMING_GROUP.None | tuple[VXR_V03_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RXA.18
    def pharmacy_or_treatment_administration(self) -> RXA:
        """
        id: RXA | use: R | rpt: 1 | seq: 18
        ---
        return_type: RXA.18: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[2][0]

    @pharmacy_or_treatment_administration.setter  # set RXA.18
    def pharmacy_or_treatment_administration(self, rxa: RXA):
        """
        id: RXA | use: R | rpt: 1 | seq: 18
        ---
        param_type: RXA.18: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        self._c_data[2] = (rxa,)

    @property  # get RXR.19
    def pharmacy_or_treatment_route(self) -> RXR | None:
        """
        id: RXR | use: O | rpt: 1 | seq: 19
        ---
        return_type: RXR.19: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[3][0]

    @pharmacy_or_treatment_route.setter  # set RXR.19
    def pharmacy_or_treatment_route(self, rxr: RXR | None):
        """
        id: RXR | use: O | rpt: 1 | seq: 19
        ---
        param_type: RXR.19: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[3] = (rxr,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[VXR_V03_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: VXR_V03_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXR_V03_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: VXR_V03_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[VXR_V03_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXR_V03_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[VXR_V03_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)
