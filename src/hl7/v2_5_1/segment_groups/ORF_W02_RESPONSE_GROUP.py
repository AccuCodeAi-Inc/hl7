from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORF_W02_RESPONSE_GROUP_PATIENT_GROUP import (
    ORF_W02_RESPONSE_GROUP_PATIENT_GROUP,
)
from ..segment_groups.ORF_W02_RESPONSE_GROUP_ORDER_GROUP import (
    ORF_W02_RESPONSE_GROUP_ORDER_GROUP,
)


"""
RESPONSE - ORF_W02_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORF_W02_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORF_W02_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    ORF_W02_RESPONSE_GROUP_ORDER_GROUP, ORF_W02_RESPONSE_GROUP_PATIENT_GROUP
)

orf_w02_response_group = ORF_W02_RESPONSE_GROUP(  # RESPONSE - Segment group for ORF_W02 - Waveform result, response to query consisting of PATIENT|None, ORDER
    patient=None,  # ORF_W02_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order=orf_w02_response_group_order_group,  # ORF_W02_RESPONSE_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORF_W02_RESPONSE_GROUP TEMPLATE-----
"""


class ORF_W02_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORF_W02_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for ORF_W02 - Waveform result, response to query consisting of PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (ORF_W02_RESPONSE_GROUP_PATIENT_GROUP, ORF_W02_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PATIENT", "ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order",)
    # fmt: on

    def __init__(
        self,
        order: ORF_W02_RESPONSE_GROUP_ORDER_GROUP
        | tuple[
            ORF_W02_RESPONSE_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.8, OBR.9, NTE.10, CTD.11, CTI.14, ...)
        patient: ORF_W02_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.6, NTE.7
    ):
        """
        None - `ORF_W02_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORF_W02_RESPONSE_GROUP>`_
        Segment group for ORF_W02 - Waveform result, response to query consisting of PATIENT|None, ORDER

        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 6, 7 | use: O | rpt: 1)
        :param order: Order segment group: [ORC|None, OBR, NTE|None, CTD|None, OBSERVATION, CTI|None] (id: ORDER | seq: 8, 9, 10, 11, None, 14 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order = order

    @property  # get ORF_W02_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> ORF_W02_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: ORF_W02_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORF_W02_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set ORF_W02_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: ORF_W02_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: ORF_W02_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORF_W02_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP, ...]:
        """
        id: ORF_W02_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: ORF_W02_RESPONSE_GROUP_ORDER_GROUP
        | tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORF_W02_RESPONSE_GROUP_ORDER_GROUP.None | tuple[ORF_W02_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORF_W02_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
