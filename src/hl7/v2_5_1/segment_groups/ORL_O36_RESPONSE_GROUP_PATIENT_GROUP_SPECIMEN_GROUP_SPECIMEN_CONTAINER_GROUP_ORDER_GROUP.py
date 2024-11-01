from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP,
)


"""
ORDER - ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP, ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP
)

orl_o36_response_group_patient_group_specimen_group_specimen_container_group_order_group = ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of ORC, TIMING|None, OBSERVATION REQUEST|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=None,  # ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of ORC, TIMING|None, OBSERVATION REQUEST|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("10", "None", "None")
    _c_components = (ORC, ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP, ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP)
    _c_name = ("ORC", "TIMING", "OBSERVATION REQUEST")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "timing", "observation_request",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.10
        timing: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.11, TQ2.12, ...)
        observation_request: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        | None = None,  #  OBR.13
    ):
        """
        None - `ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP>`_
        Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of ORC, TIMING|None, OBSERVATION REQUEST|None

        :param common_order: Common Order (id: ORC | seq: 10 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 11, 12 | use: O | rpt: *)
        :param observation_request: Observation Request segment group: [OBR] (id: OBSERVATION REQUEST | seq: 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request

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
    def timing(
        self,
    ) -> (
        tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None
    def observation_request(
        self,
    ) -> (
        ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        | None
    ):
        """
        id: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        """
        return self._c_data[2][0]

    @observation_request.setter  # set ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None
    def observation_request(
        self,
        observation_request: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        | None,
    ):
        """
        id: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
        """
        self._c_data[2] = (observation_request,)
