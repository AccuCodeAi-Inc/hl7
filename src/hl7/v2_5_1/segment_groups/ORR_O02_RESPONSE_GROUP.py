from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORR_O02_RESPONSE_GROUP_ORDER_GROUP import (
    ORR_O02_RESPONSE_GROUP_ORDER_GROUP,
)
from ..segment_groups.ORR_O02_RESPONSE_GROUP_PATIENT_GROUP import (
    ORR_O02_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - ORR_O02_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORR_O02_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORR_O02_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    ORR_O02_RESPONSE_GROUP_ORDER_GROUP, ORR_O02_RESPONSE_GROUP_PATIENT_GROUP
)

orr_o02_response_group = ORR_O02_RESPONSE_GROUP(  # RESPONSE - Segment group for ORR_O02 - General Order Response consisting of PATIENT|None, ORDER
    patient=None,  # ORR_O02_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order=orr_o02_response_group_order_group,  # ORR_O02_RESPONSE_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORR_O02_RESPONSE_GROUP TEMPLATE-----
"""


class ORR_O02_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORR_O02_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for ORR_O02 - General Order Response consisting of PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORR_O02_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (ORR_O02_RESPONSE_GROUP_PATIENT_GROUP, ORR_O02_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PATIENT", "ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order",)
    # fmt: on

    def __init__(
        self,
        order: ORR_O02_RESPONSE_GROUP_ORDER_GROUP
        | tuple[
            ORR_O02_RESPONSE_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.7, NTE.14, CTI.15, ...)
        patient: ORR_O02_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.5, NTE.6
    ):
        """
        None - `ORR_O02_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORR_O02_RESPONSE_GROUP>`_
        Segment group for ORR_O02 - General Order Response consisting of PATIENT|None, ORDER

        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 5, 6 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None] (id: ORDER | seq: 7, None, 14, 15 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order = order

    @property  # get ORR_O02_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> ORR_O02_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: ORR_O02_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORR_O02_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORR_O02_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set ORR_O02_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: ORR_O02_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: ORR_O02_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORR_O02_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORR_O02_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[ORR_O02_RESPONSE_GROUP_ORDER_GROUP, ...]:
        """
        id: ORR_O02_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORR_O02_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORR_O02_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: ORR_O02_RESPONSE_GROUP_ORDER_GROUP
        | tuple[ORR_O02_RESPONSE_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORR_O02_RESPONSE_GROUP_ORDER_GROUP.None | tuple[ORR_O02_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORR_O02_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
