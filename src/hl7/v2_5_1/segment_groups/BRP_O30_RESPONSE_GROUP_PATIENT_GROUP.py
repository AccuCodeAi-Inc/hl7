from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segment_groups.BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP import (
    BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP,
)


"""
PATIENT - BRP_O30_RESPONSE_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BRP_O30_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BRP_O30_RESPONSE_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
)

brp_o30_response_group_patient_group = BRP_O30_RESPONSE_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for BRP_O30_RESPONSE_GROUP - RESPONSE consisting of PID, ORDER|None
    patient_identification=pid,  # PID(...)  # Required.
    order=None,  # BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BRP_O30_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class BRP_O30_RESPONSE_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BRP_O30_RESPONSE_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for BRP_O30_RESPONSE_GROUP - RESPONSE consisting of PID, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BRP_O30_RESPONSE_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "None")
    _c_components = (PID, BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP)
    _c_name = ("PID", "ORDER")
    _c_is_group = (False, True)
    _c_attrs = ("patient_identification", "order",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.6
        order: BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        | tuple[BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.7, BPO.10, BPX.11, ...)
    ):
        """
        None - `BRP_O30_RESPONSE_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BRP_O30_RESPONSE_GROUP_PATIENT_GROUP>`_
        Segment group for BRP_O30_RESPONSE_GROUP - RESPONSE consisting of PID, ORDER|None

        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: R | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, BPO|None, BPX|None] (id: ORDER | seq: 7, None, 10, 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.order = order

    @property  # get PID.6
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        return_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.6
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        param_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get ORDER
    def order(
        self,
    ) -> tuple[BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...] | tuple[None]:
        """
        id: BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        | tuple[BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP.None | tuple[BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BRP_O30_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
