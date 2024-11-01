from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OSR_Q06_RESPONSE_GROUP_ORDER_GROUP import (
    OSR_Q06_RESPONSE_GROUP_ORDER_GROUP,
)
from ..segment_groups.OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP import (
    OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - OSR_Q06_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OSR_Q06_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OSR_Q06_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    OSR_Q06_RESPONSE_GROUP_ORDER_GROUP, OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP
)

osr_q06_response_group = OSR_Q06_RESPONSE_GROUP(  # RESPONSE - Segment group for OSR_Q06 - Query Response for Order Status consisting of PATIENT|None, ORDER
    patient=None,  # OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order=osr_q06_response_group_order_group,  # OSR_Q06_RESPONSE_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OSR_Q06_RESPONSE_GROUP TEMPLATE-----
"""


class OSR_Q06_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OSR_Q06_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for OSR_Q06 - Query Response for Order Status consisting of PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OSR_Q06_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP, OSR_Q06_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PATIENT", "ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order",)
    # fmt: on

    def __init__(
        self,
        order: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP
        | tuple[
            OSR_Q06_RESPONSE_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.10, NTE.19, CTI.20, ...)
        patient: OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.8, NTE.9
    ):
        """
        None - `OSR_Q06_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OSR_Q06_RESPONSE_GROUP>`_
        Segment group for OSR_Q06 - Query Response for Order Status consisting of PATIENT|None, ORDER

        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 8, 9 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None] (id: ORDER | seq: 10, None, None, 19, 20 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order = order

    @property  # get OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP, ...]:
        """
        id: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP
        | tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP.None | tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
