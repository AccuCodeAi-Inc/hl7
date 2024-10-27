from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBR import OBR
from ..segments.NTE import NTE
from ..segment_groups.REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP import (
    REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP,
)


"""
OBSERVATION - REF_I12_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::REF_I12_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import REF_I12_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
)

ref_i12_observation_group = REF_I12_OBSERVATION_GROUP(  # OBSERVATION - Segment group for REF_I12 - Patient referral consisting of OBR, NTE|None, RESULTS NOTES|None
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    results_notes=None,  # REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::REF_I12_OBSERVATION_GROUP TEMPLATE-----
"""


class REF_I12_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """REF_I12_OBSERVATION_GROUP"""
    _hl7_name = """OBSERVATION"""
    _hl7_description = """Segment group for REF_I12 - Patient referral consisting of OBR, NTE|None, RESULTS NOTES|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I12_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("21", "22", "None")
    _c_components = (OBR, NTE, REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP)
    _c_name = ("OBR", "NTE", "RESULTS NOTES")
    _c_is_group = (False, False, True)
    _c_attrs = ("observation_request", "notes_and_comments", "results_notes",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.21
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.22
        results_notes: REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
        | tuple[REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP, ...]
        | None = None,  #  (OBX.23, NTE.24, ...)
    ):
        """
        None - `REF_I12_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I12_OBSERVATION_GROUP>`_
        Segment group for REF_I12 - Patient referral consisting of OBR, NTE|None, RESULTS NOTES|None

        :param observation_request: Observation Request (id: OBR | seq: 21 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 22 | use: O | rpt: *)
        :param results_notes: Results Notes segment group: [OBX, NTE|None] (id: RESULTS NOTES | seq: 23, 24 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.results_notes = results_notes

    @property  # get OBR.21
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 21
        ---
        return_type: OBR.21: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.21
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 21
        ---
        param_type: OBR.21: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        param_type: NTE.22 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get RESULTS NOTES
    def results_notes(
        self,
    ) -> tuple[REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP, ...] | tuple[None]:
        """
        id: REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
        """
        return self._c_data[2]

    @results_notes.setter  # set RESULTS NOTES
    def results_notes(
        self,
        results_notes: REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
        | tuple[REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP, ...]
        | None,
    ):
        """
        id: RESULTS NOTES SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP.None | tuple[REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_OBSERVATION_GROUP_RESULTS_NOTES_GROUP
        """
        if isinstance(results_notes, tuple):
            self._c_data[2] = results_notes
        else:
            self._c_data[2] = (results_notes,)
