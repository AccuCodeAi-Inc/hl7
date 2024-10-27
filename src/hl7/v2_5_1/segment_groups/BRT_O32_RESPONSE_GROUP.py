from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.BRT_O32_RESPONSE_GROUP_ORDER_GROUP import (
    BRT_O32_RESPONSE_GROUP_ORDER_GROUP,
)
from ..segments.PID import PID


"""
RESPONSE - BRT_O32_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BRT_O32_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BRT_O32_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    BRT_O32_RESPONSE_GROUP_ORDER_GROUP
)

brt_o32_response_group = BRT_O32_RESPONSE_GROUP(  # RESPONSE - Segment group for BRT_O32 - Blood Product Transfusion/Disposition Acknowledgment consisting of PID|None, ORDER|None
    patient_identification=None,  # PID(...) 
    order=None,  # BRT_O32_RESPONSE_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BRT_O32_RESPONSE_GROUP TEMPLATE-----
"""


class BRT_O32_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BRT_O32_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for BRT_O32 - Blood Product Transfusion/Disposition Acknowledgment consisting of PID|None, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BRT_O32_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "O")
    _c_aliases = ("6", "None")
    _c_components = (PID, BRT_O32_RESPONSE_GROUP_ORDER_GROUP)
    _c_name = ("PID", "ORDER")
    _c_is_group = (False, True)
    _c_attrs = ("patient_identification", "order",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID | None = None,  #  PID.6
        order: BRT_O32_RESPONSE_GROUP_ORDER_GROUP
        | tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.7, BPO.10, BTX.11, ...)
    ):
        """
        None - `BRT_O32_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BRT_O32_RESPONSE_GROUP>`_
        Segment group for BRT_O32 - Blood Product Transfusion/Disposition Acknowledgment consisting of PID|None, ORDER|None

        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, BPO|None, BTX|None] (id: ORDER | seq: 7, None, 10, 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.order = order

    @property  # get PID.6
    def patient_identification(self) -> PID | None:
        """
        id: PID | use: O | rpt: 1 | seq: 6
        ---
        return_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.6
    def patient_identification(self, pid: PID | None):
        """
        id: PID | use: O | rpt: 1 | seq: 6
        ---
        param_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get ORDER
    def order(self) -> tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP, ...] | tuple[None]:
        """
        id: BRT_O32_RESPONSE_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BRT_O32_RESPONSE_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: BRT_O32_RESPONSE_GROUP_ORDER_GROUP
        | tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BRT_O32_RESPONSE_GROUP_ORDER_GROUP.None | tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BRT_O32_RESPONSE_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
