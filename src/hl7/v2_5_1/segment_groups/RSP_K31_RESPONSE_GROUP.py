from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_K31_RESPONSE_GROUP_ORDER_GROUP import (
    RSP_K31_RESPONSE_GROUP_ORDER_GROUP,
)
from ..segment_groups.RSP_K31_RESPONSE_GROUP_PATIENT_GROUP import (
    RSP_K31_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - RSP_K31_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_K31_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K31_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_K31_RESPONSE_GROUP_PATIENT_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP
)

rsp_k31_response_group = RSP_K31_RESPONSE_GROUP(  # RESPONSE - Segment group for RSP_K31 - Dispense History Response consisting of PATIENT|None, ORDER
    patient=None,  # RSP_K31_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order=rsp_k31_response_group_order_group,  # RSP_K31_RESPONSE_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_K31_RESPONSE_GROUP TEMPLATE-----
"""


class RSP_K31_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_K31_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for RSP_K31 - Dispense History Response consisting of PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K31_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (RSP_K31_RESPONSE_GROUP_PATIENT_GROUP, RSP_K31_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PATIENT", "ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order",)
    # fmt: on

    def __init__(
        self,
        order: RSP_K31_RESPONSE_GROUP_ORDER_GROUP
        | tuple[
            RSP_K31_RESPONSE_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.14, RXD.27, RXR.28, RXC.29, ...)
        patient: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP
        | None = None,  #  PID.8, PD1.9, NTE.10, AL1.11
    ):
        """
        None - `RSP_K31_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K31_RESPONSE_GROUP>`_
        Segment group for RSP_K31 - Dispense History Response consisting of PATIENT|None, ORDER

        :param patient: Patient segment group: [PID, PD1|None, NTE|None, AL1|None, PATIENT VISIT|None] (id: PATIENT | seq: 8, 9, 10, 11, None | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, RXD, RXR, RXC|None, OBSERVATION] (id: ORDER | seq: 14, None, None, None, 27, 28, 29, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order = order

    @property  # get RSP_K31_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> RSP_K31_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set RSP_K31_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP, ...]:
        """
        id: RSP_K31_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: RSP_K31_RESPONSE_GROUP_ORDER_GROUP
        | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_K31_RESPONSE_GROUP_ORDER_GROUP.None | tuple[RSP_K31_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_K31_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
