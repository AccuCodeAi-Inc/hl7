from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXA import RXA
from ..segment_groups.VXU_V04_ORDER_GROUP_TIMING_GROUP import (
    VXU_V04_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.RXR import RXR
from ..segment_groups.VXU_V04_ORDER_GROUP_OBSERVATION_GROUP import (
    VXU_V04_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - VXU_V04_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::VXU_V04_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXU_V04_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXA, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    VXU_V04_ORDER_GROUP_OBSERVATION_GROUP, VXU_V04_ORDER_GROUP_TIMING_GROUP
)

vxu_v04_order_group = VXU_V04_ORDER_GROUP(  # ORDER - Segment group for VXU_V04 - Unsolicited Vaccination Record Update consisting of ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # VXU_V04_ORDER_GROUP_TIMING_GROUP(...) 
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=None,  # RXR(...) 
    observation=None,  # VXU_V04_ORDER_GROUP_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::VXU_V04_ORDER_GROUP TEMPLATE-----
"""


class VXU_V04_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """VXU_V04_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for VXU_V04 - Unsolicited Vaccination Record Update consisting of ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXU_V04_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O")
    _c_aliases = ("12", "None", "15", "16", "None")
    _c_components = (ORC, VXU_V04_ORDER_GROUP_TIMING_GROUP, RXA, RXR, VXU_V04_ORDER_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORC", "TIMING", "RXA", "RXR", "OBSERVATION")
    _c_is_group = (False, True, False, False, True)
    _c_attrs = ("common_order", "timing", "pharmacy_or_treatment_administration", "pharmacy_or_treatment_route", "observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.12
        pharmacy_or_treatment_administration: RXA,  #  Required. RXA.15
        timing: VXU_V04_ORDER_GROUP_TIMING_GROUP
        | tuple[VXU_V04_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.13, TQ2.14, ...)
        pharmacy_or_treatment_route: RXR | None = None,  #  RXR.16
        observation: VXU_V04_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[VXU_V04_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.17, NTE.18, ...)
    ):
        """
        None - `VXU_V04_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXU_V04_ORDER_GROUP>`_
        Segment group for VXU_V04 - Unsolicited Vaccination Record Update consisting of ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None

        :param common_order: Common Order (id: ORC | seq: 12 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 13, 14 | use: O | rpt: *)
        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 15 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 16 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 17, 18 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.observation = observation

    @property  # get ORC.12
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 12
        ---
        return_type: ORC.12: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.12
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 12
        ---
        param_type: ORC.12: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[VXU_V04_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: VXU_V04_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXU_V04_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: VXU_V04_ORDER_GROUP_TIMING_GROUP
        | tuple[VXU_V04_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXU_V04_ORDER_GROUP_TIMING_GROUP.None | tuple[VXU_V04_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RXA.15
    def pharmacy_or_treatment_administration(self) -> RXA:
        """
        id: RXA | use: R | rpt: 1 | seq: 15
        ---
        return_type: RXA.15: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[2][0]

    @pharmacy_or_treatment_administration.setter  # set RXA.15
    def pharmacy_or_treatment_administration(self, rxa: RXA):
        """
        id: RXA | use: R | rpt: 1 | seq: 15
        ---
        param_type: RXA.15: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        self._c_data[2] = (rxa,)

    @property  # get RXR.16
    def pharmacy_or_treatment_route(self) -> RXR | None:
        """
        id: RXR | use: O | rpt: 1 | seq: 16
        ---
        return_type: RXR.16: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[3][0]

    @pharmacy_or_treatment_route.setter  # set RXR.16
    def pharmacy_or_treatment_route(self, rxr: RXR | None):
        """
        id: RXR | use: O | rpt: 1 | seq: 16
        ---
        param_type: RXR.16: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[3] = (rxr,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[VXU_V04_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: VXU_V04_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXU_V04_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: VXU_V04_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[VXU_V04_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXU_V04_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[VXU_V04_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)
