from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBX import OBX


"""
OBSERVATION - RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, NTE
)

rsp_z90_query_response_group_common_order_group_observation_group = RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP(  # OBSERVATION - Segment group for RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of OBX|None, NTE|None
    observation_or_result=None,  # OBX(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP TEMPLATE-----
"""


class RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP"""
    _hl7_name = """OBSERVATION"""
    _hl7_description = """Segment group for RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of OBX|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "O")
    _c_aliases = ("20", "21")
    _c_components = (OBX, NTE)
    _c_name = ("OBX", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("observation_or_result", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX | None = None,  #  OBX.20
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.21
    ):
        """
        None - `RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP_OBSERVATION_GROUP>`_
        Segment group for RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP - COMMON ORDER consisting of OBX|None, NTE|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 20 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_or_result = observation_or_result
        self.notes_and_comments = notes_and_comments

    @property  # get OBX.20
    def observation_or_result(self) -> OBX | None:
        """
        id: OBX | use: O | rpt: 1 | seq: 20
        ---
        return_type: OBX.20: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.20
    def observation_or_result(self, obx: OBX | None):
        """
        id: OBX | use: O | rpt: 1 | seq: 20
        ---
        param_type: OBX.20: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        param_type: NTE.21 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
