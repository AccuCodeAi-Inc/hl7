from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP import (
    ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP,
)
from ..segment_groups.ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP import (
    ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP,
)
from ..segment_groups.ORD_O04_RESPONSE_GROUP_PATIENT_GROUP import (
    ORD_O04_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - ORD_O04_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORD_O04_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORD_O04_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP, ORD_O04_RESPONSE_GROUP_PATIENT_GROUP, ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
)

ord_o04_response_group = ORD_O04_RESPONSE_GROUP(  # RESPONSE - Segment group for ORD_O04 - Dietary Order Acknowledgement consisting of PATIENT|None, ORDER DIET, ORDER TRAY|None
    patient=None,  # ORD_O04_RESPONSE_GROUP_PATIENT_GROUP(...) 
    order_diet=ord_o04_response_group_order_diet_group,  # ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP(...)  # Required.
    order_tray=None,  # ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORD_O04_RESPONSE_GROUP TEMPLATE-----
"""


class ORD_O04_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORD_O04_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for ORD_O04 - Dietary Order Acknowledgement consisting of PATIENT|None, ORDER DIET, ORDER TRAY|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORD_O04_RESPONSE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("O", "R", "O")
    _c_aliases = ("None", "None", "None")
    _c_components = (ORD_O04_RESPONSE_GROUP_PATIENT_GROUP, ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP, ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP)
    _c_name = ("PATIENT", "ORDER DIET", "ORDER TRAY")
    _c_is_group = (True, True, True)
    _c_attrs = ("patient", "order_diet", "order_tray",)
    # fmt: on

    def __init__(
        self,
        order_diet: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
        | tuple[
            ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP, ...
        ],  #  Required. (ORC.8, ODS.11, NTE.12, ...)
        patient: ORD_O04_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.6, NTE.7
        order_tray: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP, ...]
        | None = None,  #  (ORC.13, ODT.16, NTE.17, ...)
    ):
        """
        None - `ORD_O04_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORD_O04_RESPONSE_GROUP>`_
        Segment group for ORD_O04 - Dietary Order Acknowledgement consisting of PATIENT|None, ORDER DIET, ORDER TRAY|None

        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 6, 7 | use: O | rpt: 1)
        :param order_diet: Order Diet segment group: [ORC, TIMING DIET|None, ODS|None, NTE|None] (id: ORDER DIET | seq: 8, None, 11, 12 | use: R | rpt: *)
        :param order_tray: Order Tray segment group: [ORC, TIMING TRAY|None, ODT|None, NTE|None] (id: ORDER TRAY | seq: 13, None, 16, 17 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient = patient
        self.order_diet = order_diet
        self.order_tray = order_tray

    @property  # get ORD_O04_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> ORD_O04_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: ORD_O04_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORD_O04_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set ORD_O04_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: ORD_O04_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: ORD_O04_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORD_O04_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get ORDER DIET
    def order_diet(self) -> tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP, ...]:
        """
        id: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
        """
        return self._c_data[1]

    @order_diet.setter  # set ORDER DIET
    def order_diet(
        self,
        order_diet: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP, ...],
    ):
        """
        id: ORDER DIET SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP.None | tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
        """
        if isinstance(order_diet, tuple):
            self._c_data[1] = order_diet
        else:
            self._c_data[1] = (order_diet,)

    @property  # get ORDER TRAY
    def order_tray(
        self,
    ) -> tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP, ...] | tuple[None]:
        """
        id: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP
        """
        return self._c_data[2]

    @order_tray.setter  # set ORDER TRAY
    def order_tray(
        self,
        order_tray: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP, ...]
        | None,
    ):
        """
        id: ORDER TRAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP.None | tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP
        """
        if isinstance(order_tray, tuple):
            self._c_data[2] = order_tray
        else:
            self._c_data[2] = (order_tray,)
