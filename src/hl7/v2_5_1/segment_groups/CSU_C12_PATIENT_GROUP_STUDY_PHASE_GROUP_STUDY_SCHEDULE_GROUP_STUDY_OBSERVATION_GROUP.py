from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP import (
    CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP,
)
from ..segments.OBR import OBR
from ..segments.OBX import OBX
from ..segments.ORC import ORC


"""
STUDY OBSERVATION - CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, OBX, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP
)

csu_c12_patient_group_study_phase_group_study_schedule_group_study_observation_group = CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP(  # STUDY OBSERVATION - Segment group for CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP - STUDY SCHEDULE consisting of ORC|None, OBR, TIMING QTY|None, OBX
    common_order=None,  # ORC(...) 
    observation_request=obr,  # OBR(...)  # Required.
    timing_qty=None,  # CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP(...) 
    observation_or_result=obx,  # OBX(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP TEMPLATE-----
"""


class CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP"""
    _hl7_name = """STUDY OBSERVATION"""
    _hl7_description = """Segment group for CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP - STUDY SCHEDULE consisting of ORC|None, OBR, TIMING QTY|None, OBX"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("O", "R", "O", "R")
    _c_aliases = ("11", "12", "None", "15")
    _c_components = (ORC, OBR, CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP, OBX)
    _c_name = ("ORC", "OBR", "TIMING QTY", "OBX")
    _c_is_group = (False, False, True, False)
    _c_attrs = ("common_order", "observation_request", "timing_qty", "observation_or_result",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.12
        observation_or_result: OBX | tuple[OBX, ...],  #  Required. OBX.15
        common_order: ORC | None = None,  #  ORC.11
        timing_qty: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP
        | tuple[
            CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.13, TQ2.14, ...)
    ):
        """
        None - `CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP>`_
        Segment group for CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP - STUDY SCHEDULE consisting of ORC|None, OBR, TIMING QTY|None, OBX

        :param common_order: Common Order (id: ORC | seq: 11 | use: O | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 12 | use: R | rpt: 1)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 13, 14 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 15 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.observation_request = observation_request
        self.timing_qty = timing_qty
        self.observation_or_result = observation_or_result

    @property  # get ORC.11
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 11
        ---
        return_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.11
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 11
        ---
        param_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get OBR.12
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 12
        ---
        return_type: OBR.12: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[1][0]

    @observation_request.setter  # set OBR.12
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 12
        ---
        param_type: OBR.12: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[1] = (obr,)

    @property  # get TIMING QTY
    def timing_qty(
        self,
    ) -> (
        tuple[
            CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP
        """
        return self._c_data[2]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP
        | tuple[
            CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP.None | tuple[CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_OBSERVATION_GROUP_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[2] = timing_qty
        else:
            self._c_data[2] = (timing_qty,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...]:
        """
        id: OBX SEGMENT GROUP | use: R | rpt: * | seq: 15
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[3]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...]):
        """
        id: OBX SEGMENT GROUP | use: R | rpt: * | seq: 15
        ---
        param_type: OBX.15 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[3] = obx
        else:
            self._c_data[3] = (obx,)
