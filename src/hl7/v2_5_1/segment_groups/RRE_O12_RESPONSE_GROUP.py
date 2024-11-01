from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RRE_O12_RESPONSE_GROUP_ORDER_GROUP import (
    RRE_O12_RESPONSE_GROUP_ORDER_GROUP,
)
from ..segment_groups.RRE_O12_RESPONSE_GROUP_PATIENT_GROUP import (
    RRE_O12_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - RRE_O12_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRE_O12_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRE_O12_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    RRE_O12_RESPONSE_GROUP_ORDER_GROUP, RRE_O12_RESPONSE_GROUP_PATIENT_GROUP
)

rre_o12_response_group = RRE_O12_RESPONSE_GROUP(  # RESPONSE - Segment group for RRE_O12 - Pharmacy/Treatment Encoded Order Acknowledgement consisting of PATIENT|None, ORDER
    patient=None,  # RRE_O12_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order=rre_o12_response_group_order_group,  # RRE_O12_RESPONSE_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRE_O12_RESPONSE_GROUP TEMPLATE-----
"""


class RRE_O12_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRE_O12_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for RRE_O12 - Pharmacy/Treatment Encoded Order Acknowledgement consisting of PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRE_O12_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (RRE_O12_RESPONSE_GROUP_PATIENT_GROUP, RRE_O12_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PATIENT", "ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order",)
    # fmt: on

    def __init__(
        self,
        order: RRE_O12_RESPONSE_GROUP_ORDER_GROUP
        | tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP, ...],  #  Required. (ORC.8, ...)
        patient: RRE_O12_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.6, NTE.7
    ):
        """
        None - `RRE_O12_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRE_O12_RESPONSE_GROUP>`_
        Segment group for RRE_O12 - Pharmacy/Treatment Encoded Order Acknowledgement consisting of PATIENT|None, ORDER

        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 6, 7 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, ENCODING|None] (id: ORDER | seq: 8, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order = order

    @property  # get RRE_O12_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> RRE_O12_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: RRE_O12_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRE_O12_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set RRE_O12_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: RRE_O12_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: RRE_O12_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRE_O12_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP, ...]:
        """
        id: RRE_O12_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: RRE_O12_RESPONSE_GROUP_ORDER_GROUP
        | tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RRE_O12_RESPONSE_GROUP_ORDER_GROUP.None | tuple[RRE_O12_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRE_O12_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
