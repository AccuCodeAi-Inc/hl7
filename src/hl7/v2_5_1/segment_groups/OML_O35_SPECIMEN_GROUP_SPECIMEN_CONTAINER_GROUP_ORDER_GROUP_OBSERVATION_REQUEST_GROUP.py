from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.TCD import TCD
from ..segment_groups.OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP,
)
from ..segment_groups.OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP,
)


"""
OBSERVATION REQUEST - OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, TCD, DG1, OBR
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
)

oml_o35_specimen_group_specimen_container_group_order_group_observation_request_group = OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(  # OBSERVATION REQUEST - Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP - ORDER consisting of OBR, TCD|None, NTE|None, DG1|None, OBSERVATION|None, PRIOR RESULT|None
    observation_request=obr,  # OBR(...)  # Required.
    test_code_detail=None,  # TCD(...) 
    notes_and_comments=None,  # NTE(...) 
    diagnosis=None,  # DG1(...) 
    observation=None,  # OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP(...) 
    prior_result=None,  # OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP TEMPLATE-----
"""


class OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP"""
    _hl7_name = """OBSERVATION REQUEST"""
    _hl7_description = """Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP - ORDER consisting of OBR, TCD|None, NTE|None, DG1|None, OBSERVATION|None, PRIOR RESULT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "O")
    _c_aliases = ("21", "22", "23", "24", "None", "None")
    _c_components = (OBR, TCD, NTE, DG1, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP)
    _c_name = ("OBR", "TCD", "NTE", "DG1", "OBSERVATION", "PRIOR RESULT")
    _c_is_group = (False, False, False, False, True, True)
    _c_attrs = ("observation_request", "test_code_detail", "notes_and_comments", "diagnosis", "observation", "prior_result",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.21
        test_code_detail: TCD | None = None,  #  TCD.22
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.23
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.24
        observation: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.25, TCD.26, NTE.27, ...)
        prior_result: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP,
            ...,
        ]
        | None = None,  #  (AL1.32, ...)
    ):
        """
        None - `OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP>`_
        Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP - ORDER consisting of OBR, TCD|None, NTE|None, DG1|None, OBSERVATION|None, PRIOR RESULT|None

        :param observation_request: Observation Request (id: OBR | seq: 21 | use: R | rpt: 1)
        :param test_code_detail: Test Code Detail (id: TCD | seq: 22 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 23 | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 24 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, TCD|None, NTE|None] (id: OBSERVATION | seq: 25, 26, 27 | use: O | rpt: *)
        :param prior_result: Prior Result segment group: [PATIENT PRIOR|None, PATIENT VISIT PRIOR|None, AL1|None, ORDER PRIOR] (id: PRIOR RESULT | seq: None, None, 32, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.observation_request = observation_request
        self.test_code_detail = test_code_detail
        self.notes_and_comments = notes_and_comments
        self.diagnosis = diagnosis
        self.observation = observation
        self.prior_result = prior_result

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

    @property  # get TCD.22
    def test_code_detail(self) -> TCD | None:
        """
        id: TCD | use: O | rpt: 1 | seq: 22
        ---
        return_type: TCD.22: Test Code Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD
        """
        return self._c_data[1][0]

    @test_code_detail.setter  # set TCD.22
    def test_code_detail(self, tcd: TCD | None):
        """
        id: TCD | use: O | rpt: 1 | seq: 22
        ---
        param_type: TCD.22: Test Code Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD
        """
        self._c_data[1] = (tcd,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: NTE.23 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[3]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 24
        ---
        param_type: DG1.24 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[3] = dg1
        else:
            self._c_data[3] = (dg1,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> (
        tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[4]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP.None | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[4] = observation
        else:
            self._c_data[4] = (observation,)

    @property  # get PRIOR RESULT
    def prior_result(
        self,
    ) -> (
        tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP
        """
        return self._c_data[5]

    @prior_result.setter  # set PRIOR RESULT
    def prior_result(
        self,
        prior_result: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: PRIOR RESULT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP.None | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP
        """
        if isinstance(prior_result, tuple):
            self._c_data[5] = prior_result
        else:
            self._c_data[5] = (prior_result,)
