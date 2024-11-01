from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segment_groups.RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP import (
    RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP,
)
from ..segments.OBR import OBR


"""
OBSERVATION - RQA_I11_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RQA_I11_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RQA_I11_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP
)

rqa_i11_observation_group = RQA_I11_OBSERVATION_GROUP(  # OBSERVATION - Segment group for RQA_I11 - Request for cancellation of an authorization consisting of OBR, NTE|None, RESULTS|None
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    results=None,  # RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RQA_I11_OBSERVATION_GROUP TEMPLATE-----
"""


class RQA_I11_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RQA_I11_OBSERVATION_GROUP"""
    _hl7_name = """OBSERVATION"""
    _hl7_description = """Segment group for RQA_I11 - Request for cancellation of an authorization consisting of OBR, NTE|None, RESULTS|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQA_I11_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("21", "22", "None")
    _c_components = (OBR, NTE, RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP)
    _c_name = ("OBR", "NTE", "RESULTS")
    _c_is_group = (False, False, True)
    _c_attrs = ("observation_request", "notes_and_comments", "results",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.21
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.22
        results: RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP
        | tuple[RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP, ...]
        | None = None,  #  (OBX.23, NTE.24, ...)
    ):
        """
        None - `RQA_I11_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQA_I11_OBSERVATION_GROUP>`_
        Segment group for RQA_I11 - Request for cancellation of an authorization consisting of OBR, NTE|None, RESULTS|None

        :param observation_request: Observation Request (id: OBR | seq: 21 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 22 | use: O | rpt: *)
        :param results: Results segment group: [OBX, NTE|None] (id: RESULTS | seq: 23, 24 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.results = results

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

    @property  # get RESULTS
    def results(
        self,
    ) -> tuple[RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP, ...] | tuple[None]:
        """
        id: RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP
        """
        return self._c_data[2]

    @results.setter  # set RESULTS
    def results(
        self,
        results: RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP
        | tuple[RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP, ...]
        | None,
    ):
        """
        id: RESULTS SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP.None | tuple[RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQA_I11_OBSERVATION_GROUP_RESULTS_GROUP
        """
        if isinstance(results, tuple):
            self._c_data[2] = results
        else:
            self._c_data[2] = (results,)
