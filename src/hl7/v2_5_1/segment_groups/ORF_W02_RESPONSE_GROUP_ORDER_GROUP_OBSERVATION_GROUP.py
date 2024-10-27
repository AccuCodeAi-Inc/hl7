from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBX import OBX


"""
OBSERVATION - ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, NTE
)

orf_w02_response_group_order_group_observation_group = ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP(  # OBSERVATION - Segment group for ORF_W02_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of OBX|None, NTE|None
    observation_or_result=None,  # OBX(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP TEMPLATE-----
"""


class ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP"""
    _hl7_name = """OBSERVATION"""
    _hl7_description = """Segment group for ORF_W02_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of OBX|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "O")
    _c_aliases = ("12", "13")
    _c_components = (OBX, NTE)
    _c_name = ("OBX", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("observation_or_result", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX | None = None,  #  OBX.12
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
    ):
        """
        None - `ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02_RESPONSE_GROUP_ORDER_GROUP_OBSERVATION_GROUP>`_
        Segment group for ORF_W02_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of OBX|None, NTE|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 12 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_or_result = observation_or_result
        self.notes_and_comments = notes_and_comments

    @property  # get OBX.12
    def observation_or_result(self) -> OBX | None:
        """
        id: OBX | use: O | rpt: 1 | seq: 12
        ---
        return_type: OBX.12: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.12
    def observation_or_result(self, obx: OBX | None):
        """
        id: OBX | use: O | rpt: 1 | seq: 12
        ---
        param_type: OBX.12: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: NTE.13 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)