from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segment_groups.RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP import (
    RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP,
)


"""
OBSERVATION - RCI_I05_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RCI_I05_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RCI_I05_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP
)

rci_i05_observation_group = RCI_I05_OBSERVATION_GROUP(  # OBSERVATION - Segment group for RCI_I05 - Request for patient clinical information acknowledgement consisting of OBR, NTE|None, RESULTS|None
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    results=None,  # RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RCI_I05_OBSERVATION_GROUP TEMPLATE-----
"""


class RCI_I05_OBSERVATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RCI_I05_OBSERVATION_GROUP"""
    _hl7_name = """OBSERVATION"""
    _hl7_description = """Segment group for RCI_I05 - Request for patient clinical information acknowledgement consisting of OBR, NTE|None, RESULTS|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RCI_I05_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("12", "13", "None")
    _c_components = (OBR, NTE, RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP)
    _c_name = ("OBR", "NTE", "RESULTS")
    _c_is_group = (False, False, True)
    _c_attrs = ("observation_request", "notes_and_comments", "results",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.12
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
        results: RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP
        | tuple[RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP, ...]
        | None = None,  #  (OBX.14, NTE.15, ...)
    ):
        """
        None - `RCI_I05_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RCI_I05_OBSERVATION_GROUP>`_
        Segment group for RCI_I05 - Request for patient clinical information acknowledgement consisting of OBR, NTE|None, RESULTS|None

        :param observation_request: Observation Request (id: OBR | seq: 12 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        :param results: Results segment group: [OBX, NTE|None] (id: RESULTS | seq: 14, 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.results = results

    @property  # get OBR.12
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 12
        ---
        return_type: OBR.12: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.12
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 12
        ---
        param_type: OBR.12: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)

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

    @property  # get RESULTS
    def results(
        self,
    ) -> tuple[RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP, ...] | tuple[None]:
        """
        id: RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP
        """
        return self._c_data[2]

    @results.setter  # set RESULTS
    def results(
        self,
        results: RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP
        | tuple[RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP, ...]
        | None,
    ):
        """
        id: RESULTS SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP.None | tuple[RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCI_I05_OBSERVATION_GROUP_RESULTS_GROUP
        """
        if isinstance(results, tuple):
            self._c_data[2] = results
        else:
            self._c_data[2] = (results,)
