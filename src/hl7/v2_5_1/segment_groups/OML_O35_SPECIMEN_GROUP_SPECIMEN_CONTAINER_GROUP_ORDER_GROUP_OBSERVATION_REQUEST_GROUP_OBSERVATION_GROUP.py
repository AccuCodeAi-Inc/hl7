from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.TCD import TCD


"""
OBSERVATION - OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, OBX, TCD
)

oml_o35_specimen_group_specimen_container_group_order_group_observation_request_group_observation_group = OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP(  # OBSERVATION - Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of OBX, TCD|None, NTE|None
    observation_or_result=obx,  # OBX(...)  # Required.
    test_code_detail=None,  # TCD(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP TEMPLATE-----
"""


class OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP"""
    _hl7_name = """OBSERVATION"""
    _hl7_description = """Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of OBX, TCD|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("25", "26", "27")
    _c_components = (OBX, TCD, NTE)
    _c_name = ("OBX", "TCD", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("observation_or_result", "test_code_detail", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX,  #  Required. OBX.25
        test_code_detail: TCD | None = None,  #  TCD.26
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.27
    ):
        """
        None - `OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_OBSERVATION_GROUP>`_
        Segment group for OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of OBX, TCD|None, NTE|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 25 | use: R | rpt: 1)
        :param test_code_detail: Test Code Detail (id: TCD | seq: 26 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 27 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.observation_or_result = observation_or_result
        self.test_code_detail = test_code_detail
        self.notes_and_comments = notes_and_comments

    @property  # get OBX.25
    def observation_or_result(self) -> OBX:
        """
        id: OBX | use: R | rpt: 1 | seq: 25
        ---
        return_type: OBX.25: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.25
    def observation_or_result(self, obx: OBX):
        """
        id: OBX | use: R | rpt: 1 | seq: 25
        ---
        param_type: OBX.25: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get TCD.26
    def test_code_detail(self) -> TCD | None:
        """
        id: TCD | use: O | rpt: 1 | seq: 26
        ---
        return_type: TCD.26: Test Code Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD
        """
        return self._c_data[1][0]

    @test_code_detail.setter  # set TCD.26
    def test_code_detail(self, tcd: TCD | None):
        """
        id: TCD | use: O | rpt: 1 | seq: 26
        ---
        param_type: TCD.26: Test Code Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD
        """
        self._c_data[1] = (tcd,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        param_type: NTE.27 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)
