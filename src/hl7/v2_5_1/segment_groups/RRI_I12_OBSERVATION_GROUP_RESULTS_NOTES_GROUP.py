from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBX import OBX


"""
RESULTS NOTES - RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, NTE
)

rri_i12_observation_group_results_notes_group = RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP(  # RESULTS NOTES - Segment group for RRI_I12_OBSERVATION_GROUP - OBSERVATION consisting of OBX, NTE|None
    observation_or_result=obx,  # OBX(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP TEMPLATE-----
"""


class RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP"""
    _hl7_name = """RESULTS NOTES"""
    _hl7_description = """Segment group for RRI_I12_OBSERVATION_GROUP - OBSERVATION consisting of OBX, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("19", "20")
    _c_components = (OBX, NTE)
    _c_name = ("OBX", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("observation_or_result", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX,  #  Required. OBX.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.20
    ):
        """
        None - `RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP>`_
        Segment group for RRI_I12_OBSERVATION_GROUP - OBSERVATION consisting of OBX, NTE|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 19 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_or_result = observation_or_result
        self.notes_and_comments = notes_and_comments

    @property  # get OBX.19
    def observation_or_result(self) -> OBX:
        """
        id: OBX | use: R | rpt: 1 | seq: 19
        ---
        return_type: OBX.19: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.19
    def observation_or_result(self, obx: OBX):
        """
        id: OBX | use: R | rpt: 1 | seq: 19
        ---
        param_type: OBX.19: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: NTE.20 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
