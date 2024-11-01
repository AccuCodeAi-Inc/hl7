from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP import (
    ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP,
)
from ..segment_groups.ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP import (
    ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP,
)


"""
PATIENT RESULT - ORU_W01_PATIENT_RESULT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORU_W01_PATIENT_RESULT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORU_W01_PATIENT_RESULT_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP, ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP
)

oru_w01_patient_result_group = ORU_W01_PATIENT_RESULT_GROUP(  # PATIENT RESULT - Segment group for ORU_W01 - Waveform result, unsolicited transmission of requested information consisting of PATIENT|None, ORDER OBSERVATION
    patient=None,  # ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP(...) 
    order_observation=oru_w01_patient_result_group_order_observation_group,  # ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORU_W01_PATIENT_RESULT_GROUP TEMPLATE-----
"""


class ORU_W01_PATIENT_RESULT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORU_W01_PATIENT_RESULT_GROUP"""
    _hl7_name = """PATIENT RESULT"""
    _hl7_description = """Segment group for ORU_W01 - Waveform result, unsolicited transmission of requested information consisting of PATIENT|None, ORDER OBSERVATION"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01_PATIENT_RESULT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP, ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP)
    _c_name = ("PATIENT", "ORDER OBSERVATION")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order_observation",)
    # fmt: on

    def __init__(
        self,
        order_observation: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[
            ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP, ...
        ],  #  Required. (ORC.9, OBR.10, NTE.11, CTD.12, FT1.15, CTI.16, ...)
        patient: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP
        | None = None,  #  PID.3, PD1.4, NK1.5, NTE.6
    ):
        """
        None - `ORU_W01_PATIENT_RESULT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01_PATIENT_RESULT_GROUP>`_
        Segment group for ORU_W01 - Waveform result, unsolicited transmission of requested information consisting of PATIENT|None, ORDER OBSERVATION

        :param patient: Patient segment group: [PID, PD1|None, NK1|None, NTE|None, VISIT|None] (id: PATIENT | seq: 3, 4, 5, 6, None | use: O | rpt: 1)
        :param order_observation: Order Observation segment group: [ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, FT1|None, CTI|None, SPECIMEN|None] (id: ORDER OBSERVATION | seq: 9, 10, 11, 12, None, 15, 16, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order_observation = order_observation

    @property  # get ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP.None
    def patient(self) -> ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP | None:
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP.None
    def patient(self, patient: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP | None):
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER OBSERVATION
    def order_observation(
        self,
    ) -> tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP, ...]:
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
        """
        return self._c_data[1]

    @order_observation.setter  # set ORDER OBSERVATION
    def order_observation(
        self,
        order_observation: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
        | tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP, ...],
    ):
        """
        id: ORDER OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP.None | tuple[ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_ORDER_OBSERVATION_GROUP
        """
        if isinstance(order_observation, tuple):
            self._c_data[1] = order_observation
        else:
            self._c_data[1] = (order_observation,)
