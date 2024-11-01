from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segment_groups.RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP import (
    RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP,
)
from ..segments.RXA import RXA


"""
ADMINISTRATION - RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP
from utils.hl7.v2_5_1.segments import (
    RXA, RXR
)
from utils.hl7.v2_5_1.segment_groups import (
    RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP
)

ras_o17_order_group_administration_group = RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP(  # ADMINISTRATION - Segment group for RAS_O17_ORDER_GROUP - ORDER consisting of RXA, RXR, OBSERVATION|None
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    observation=None,  # RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP TEMPLATE-----
"""


class RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP"""
    _hl7_name = """ADMINISTRATION"""
    _hl7_description = """Segment group for RAS_O17_ORDER_GROUP - ORDER consisting of RXA, RXR, OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (65535, 1, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("23", "24", "None")
    _c_components = (RXA, RXR, RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP)
    _c_name = ("RXA", "RXR", "OBSERVATION")
    _c_is_group = (False, False, True)
    _c_attrs = ("pharmacy_or_treatment_administration", "pharmacy_or_treatment_route", "observation",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_administration: RXA
        | tuple[RXA, ...],  #  Required. RXA.23
        pharmacy_or_treatment_route: RXR,  #  Required. RXR.24
        observation: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP
        | tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.25, NTE.26, ...)
    ):
        """
        None - `RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP>`_
        Segment group for RAS_O17_ORDER_GROUP - ORDER consisting of RXA, RXR, OBSERVATION|None

        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 23 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 24 | use: R | rpt: 1)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 25, 26 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.observation = observation

    @property  # get RXA
    def pharmacy_or_treatment_administration(self) -> tuple[RXA, ...]:
        """
        id: RXA SEGMENT GROUP | use: R | rpt: * | seq: 23
        ---
        return_type: tuple[RXA, ...]: (Pharmacy/Treatment Administration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[0]

    @pharmacy_or_treatment_administration.setter  # set RXA
    def pharmacy_or_treatment_administration(self, rxa: RXA | tuple[RXA, ...]):
        """
        id: RXA SEGMENT GROUP | use: R | rpt: * | seq: 23
        ---
        param_type: RXA.23 | tuple[RXA, ...]: (Pharmacy/Treatment Administration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        if isinstance(rxa, tuple):
            self._c_data[0] = rxa
        else:
            self._c_data[0] = (rxa,)

    @property  # get RXR.24
    def pharmacy_or_treatment_route(self) -> RXR:
        """
        id: RXR | use: R | rpt: 1 | seq: 24
        ---
        return_type: RXR.24: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1][0]

    @pharmacy_or_treatment_route.setter  # set RXR.24
    def pharmacy_or_treatment_route(self, rxr: RXR):
        """
        id: RXR | use: R | rpt: 1 | seq: 24
        ---
        param_type: RXR.24: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[1] = (rxr,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> (
        tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP, ...]
        | tuple[None]
    ):
        """
        id: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[2]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP
        | tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP.None | tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[2] = observation
        else:
            self._c_data[2] = (observation,)
