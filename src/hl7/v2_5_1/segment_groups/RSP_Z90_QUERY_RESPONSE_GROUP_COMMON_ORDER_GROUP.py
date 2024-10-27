from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segment_groups.RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP import (
    RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.NTE import NTE
from ..segments.CTD import CTD
from ..segment_groups.RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP import (
    RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP,
)


"""
COMMON ORDER - RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, OBR, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
)

rsp_z90_query_response_group_common_order_group = RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP(  # COMMON ORDER - Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, OBSERVATION
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    observation=rsp_z90_query_response_group_common_order_group_observation_group,  # RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP TEMPLATE-----
"""


class RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP"""
    _hl7_name = """COMMON ORDER"""
    _hl7_description = """Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, OBSERVATION"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "R")
    _c_aliases = ("14", "None", "17", "18", "19", "None")
    _c_components = (ORC, RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, OBR, NTE, CTD, RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORC", "TIMING", "OBR", "NTE", "CTD", "OBSERVATION")
    _c_is_group = (False, True, False, False, False, True)
    _c_attrs = ("common_order", "timing", "observation_request", "notes_and_comments", "contact_data", "observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        observation_request: OBR,  #  Required. OBR.17
        observation: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[
            RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...
        ],  #  Required. (OBX.20, NTE.21, ...)
        timing: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.18
        contact_data: CTD | None = None,  #  CTD.19
    ):
        """
        None - `RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP>`_
        Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, OBSERVATION

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param observation_request: Observation Request (id: OBR | seq: 17 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 18 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 19 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX|None, NTE|None] (id: OBSERVATION | seq: 20, 21 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.contact_data = contact_data
        self.observation = observation

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
    def timing(
        self,
    ) -> (
        tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | tuple[None]
    ):
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP.None | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OBR.17
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 17
        ---
        return_type: OBR.17: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.17
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 17
        ---
        param_type: OBR.17: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

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

    @property  # get CTD.19
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 19
        ---
        return_type: CTD.19: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[4][0]

    @contact_data.setter  # set CTD.19
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 19
        ---
        param_type: CTD.19: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[4] = (ctd,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]:
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[5]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[5] = observation
        else:
            self._c_data[5] = (observation,)
