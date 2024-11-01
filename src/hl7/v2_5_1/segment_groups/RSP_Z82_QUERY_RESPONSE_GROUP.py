from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP import (
    RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP,
)
from ..segment_groups.RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP import (
    RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP,
)


"""
QUERY RESPONSE - RSP_Z82_QUERY_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z82_QUERY_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP
)

rsp_z82_query_response_group = RSP_Z82_QUERY_RESPONSE_GROUP(  # QUERY RESPONSE - Segment group for RSP_Z82 - Dispense History Response consisting of PATIENT|None, COMMON ORDER
    patient=None,  # RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP(...) 
    common_order=rsp_z82_query_response_group_common_order_group,  # RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP TEMPLATE-----
"""


class RSP_Z82_QUERY_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z82_QUERY_RESPONSE_GROUP"""
    _hl7_name = """QUERY RESPONSE"""
    _hl7_description = """Segment group for RSP_Z82 - Dispense History Response consisting of PATIENT|None, COMMON ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("O", "R")
    _c_aliases = ("None", "None")
    _c_components = (RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP, RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP)
    _c_name = ("PATIENT", "COMMON ORDER")
    _c_is_group = (True, True)
    _c_attrs = ("patient", "common_order",)
    # fmt: on

    def __init__(
        self,
        common_order: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        | tuple[
            RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...
        ],  #  Required. (ORC.14, RXD.27, RXR.28, RXC.29, ...)
        patient: RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP
        | None = None,  #  PID.8, PD1.9, NTE.10
    ):
        """
        None - `RSP_Z82_QUERY_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP>`_
        Segment group for RSP_Z82 - Dispense History Response consisting of PATIENT|None, COMMON ORDER

        :param patient: Patient segment group: [PID, PD1|None, NTE|None, VISIT|None] (id: PATIENT | seq: 8, 9, 10, None | use: O | rpt: 1)
        :param common_order: Common Order segment group: [ORC, TIMING, ORDER DETAIL|None, ENCODED ORDER|None, RXD, RXR, RXC|None, OBSERVATION] (id: COMMON ORDER | seq: 14, None, None, None, 27, 28, 29, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient = patient
        self.common_order = common_order

    @property  # get RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get COMMON ORDER
    def common_order(
        self,
    ) -> tuple[RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...]:
        """
        id: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        """
        return self._c_data[1]

    @common_order.setter  # set COMMON ORDER
    def common_order(
        self,
        common_order: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        | tuple[RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...],
    ):
        """
        id: COMMON ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP.None | tuple[RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z82_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        """
        if isinstance(common_order, tuple):
            self._c_data[1] = common_order
        else:
            self._c_data[1] = (common_order,)
