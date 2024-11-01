from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segment_groups.ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP import (
    ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP,
)


"""
PATIENT - ORL_O22_RESPONSE_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O22_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O22_RESPONSE_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
)

orl_o22_response_group_patient_group = ORL_O22_RESPONSE_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for ORL_O22_RESPONSE_GROUP - RESPONSE consisting of PID, ORDER|None
    patient_identification=pid,  # PID(...)  # Required.
    order=None,  # ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O22_RESPONSE_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class ORL_O22_RESPONSE_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O22_RESPONSE_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for ORL_O22_RESPONSE_GROUP - RESPONSE consisting of PID, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "None")
    _c_components = (PID, ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP)
    _c_name = ("PID", "ORDER")
    _c_is_group = (False, True)
    _c_attrs = ("patient_identification", "order",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.6
        order: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        | tuple[ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]
        | None = None,  #  (ORC.7, ...)
    ):
        """
        None - `ORL_O22_RESPONSE_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP>`_
        Segment group for ORL_O22_RESPONSE_GROUP - RESPONSE consisting of PID, ORDER|None

        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: R | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, OBSERVATION REQUEST|None] (id: ORDER | seq: 7, None, None | use: O | rpt: *)
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
    ) -> tuple[ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...] | tuple[None]:
        """
        id: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        | tuple[ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP.None | tuple[ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
