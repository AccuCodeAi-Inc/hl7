from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORS_O06_RESPONSE_GROUP_ORDER_GROUP import (
    ORS_O06_RESPONSE_GROUP_ORDER_GROUP,
)
from ..segment_groups.ORS_O06_RESPONSE_GROUP_PATIENT_GROUP import (
    ORS_O06_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - ORS_O06_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORS_O06_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORS_O06_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    ORS_O06_RESPONSE_GROUP_ORDER_GROUP, ORS_O06_RESPONSE_GROUP_PATIENT_GROUP
)

ors_o06_response_group = ORS_O06_RESPONSE_GROUP(  # RESPONSE - Segment group for ORS_O06 - Stock Requisition Order Acknowledgement consisting of PATIENT|None, ORDER
    patient=None,  # ORS_O06_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order=ors_o06_response_group_order_group,  # ORS_O06_RESPONSE_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORS_O06_RESPONSE_GROUP TEMPLATE-----
"""


class ORS_O06_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORS_O06_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for ORS_O06 - Stock Requisition Order Acknowledgement consisting of PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORS_O06_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (ORS_O06_RESPONSE_GROUP_PATIENT_GROUP, ORS_O06_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PATIENT", "ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "order",)
    # fmt: on

    def __init__(
        self,
        order: ORS_O06_RESPONSE_GROUP_ORDER_GROUP
        | tuple[
            ORS_O06_RESPONSE_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.8, RQD.11, RQ1.12, NTE.13, ...)
        patient: ORS_O06_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.6, NTE.7
    ):
        """
        None - `ORS_O06_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORS_O06_RESPONSE_GROUP>`_
        Segment group for ORS_O06 - Stock Requisition Order Acknowledgement consisting of PATIENT|None, ORDER

        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 6, 7 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, RQD, RQ1|None, NTE|None] (id: ORDER | seq: 8, None, 11, 12, 13 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.order = order

    @property  # get ORS_O06_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> ORS_O06_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: ORS_O06_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORS_O06_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORS_O06_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set ORS_O06_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: ORS_O06_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: ORS_O06_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORS_O06_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORS_O06_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[ORS_O06_RESPONSE_GROUP_ORDER_GROUP, ...]:
        """
        id: ORS_O06_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORS_O06_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORS_O06_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: ORS_O06_RESPONSE_GROUP_ORDER_GROUP
        | tuple[ORS_O06_RESPONSE_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORS_O06_RESPONSE_GROUP_ORDER_GROUP.None | tuple[ORS_O06_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORS_O06_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
