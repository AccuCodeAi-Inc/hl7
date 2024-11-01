from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.TCD import TCD
from ..segments.SID import SID
from ..segments.OBX import OBX


"""
RESULT - OUL_R24_ORDER_GROUP_RESULT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R24_ORDER_GROUP_RESULT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R24_ORDER_GROUP_RESULT_GROUP
from utils.hl7.v2_5_1.segments import (
    TCD, NTE, SID, OBX
)

oul_r24_order_group_result_group = OUL_R24_ORDER_GROUP_RESULT_GROUP(  # RESULT - Segment group for OUL_R24_ORDER_GROUP - ORDER consisting of OBX, TCD|None, SID|None, NTE|None
    observation_or_result=obx,  # OBX(...)  # Required.
    test_code_detail=None,  # TCD(...) 
    substance_identifier=None,  # SID(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R24_ORDER_GROUP_RESULT_GROUP TEMPLATE-----
"""


class OUL_R24_ORDER_GROUP_RESULT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R24_ORDER_GROUP_RESULT_GROUP"""
    _hl7_name = """RESULT"""
    _hl7_description = """Segment group for OUL_R24_ORDER_GROUP - ORDER consisting of OBX, TCD|None, SID|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R24_ORDER_GROUP_RESULT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("18", "19", "20", "21")
    _c_components = (OBX, TCD, SID, NTE)
    _c_name = ("OBX", "TCD", "SID", "NTE")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("observation_or_result", "test_code_detail", "substance_identifier", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        observation_or_result: OBX,  #  Required. OBX.18
        test_code_detail: TCD | None = None,  #  TCD.19
        substance_identifier: SID | tuple[SID, ...] | None = None,  #  SID.20
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.21
    ):
        """
        None - `OUL_R24_ORDER_GROUP_RESULT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R24_ORDER_GROUP_RESULT_GROUP>`_
        Segment group for OUL_R24_ORDER_GROUP - ORDER consisting of OBX, TCD|None, SID|None, NTE|None

        :param observation_or_result: Observation/Result (id: OBX | seq: 18 | use: R | rpt: 1)
        :param test_code_detail: Test Code Detail (id: TCD | seq: 19 | use: O | rpt: 1)
        :param substance_identifier: Substance Identifier (id: SID | seq: 20 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.observation_or_result = observation_or_result
        self.test_code_detail = test_code_detail
        self.substance_identifier = substance_identifier
        self.notes_and_comments = notes_and_comments

    @property  # get OBX.18
    def observation_or_result(self) -> OBX:
        """
        id: OBX | use: R | rpt: 1 | seq: 18
        ---
        return_type: OBX.18: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[0][0]

    @observation_or_result.setter  # set OBX.18
    def observation_or_result(self, obx: OBX):
        """
        id: OBX | use: R | rpt: 1 | seq: 18
        ---
        param_type: OBX.18: Observation/Result
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        self._c_data[0] = (obx,)

    @property  # get TCD.19
    def test_code_detail(self) -> TCD | None:
        """
        id: TCD | use: O | rpt: 1 | seq: 19
        ---
        return_type: TCD.19: Test Code Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD
        """
        return self._c_data[1][0]

    @test_code_detail.setter  # set TCD.19
    def test_code_detail(self, tcd: TCD | None):
        """
        id: TCD | use: O | rpt: 1 | seq: 19
        ---
        param_type: TCD.19: Test Code Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TCD
        """
        self._c_data[1] = (tcd,)

    @property  # get SID
    def substance_identifier(self) -> tuple[SID, ...] | tuple[None]:
        """
        id: SID SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[SID, ...]: (Substance Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SID
        """
        return self._c_data[2]

    @substance_identifier.setter  # set SID
    def substance_identifier(self, sid: SID | tuple[SID, ...] | None):
        """
        id: SID SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: SID.20 | tuple[SID, ...]: (Substance Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SID
        """
        if isinstance(sid, tuple):
            self._c_data[2] = sid
        else:
            self._c_data[2] = (sid,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 21
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

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
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)
