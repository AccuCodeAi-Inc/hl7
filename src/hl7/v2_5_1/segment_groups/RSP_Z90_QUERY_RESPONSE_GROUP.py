from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP import (
    RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP,
)
from ..segment_groups.RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP import (
    RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP,
)
from ..segment_groups.RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP import (
    RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
QUERY RESPONSE - RSP_Z90_QUERY_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z90_QUERY_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP, RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP
)

rsp_z90_query_response_group = RSP_Z90_QUERY_RESPONSE_GROUP(  # QUERY RESPONSE - Segment group for RSP_Z90 - Lab Results History Response consisting of PATIENT|None, COMMON ORDER, SPECIMEN|None
    patient=None,  # RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP(...) 
    common_order=rsp_z90_query_response_group_common_order_group,  # RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP(...)  # Required.
    specimen=None,  # RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP TEMPLATE-----
"""


class RSP_Z90_QUERY_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z90_QUERY_RESPONSE_GROUP"""
    _hl7_name = """QUERY RESPONSE"""
    _hl7_description = """Segment group for RSP_Z90 - Lab Results History Response consisting of PATIENT|None, COMMON ORDER, SPECIMEN|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("O", "R", "O")
    _c_aliases = ("None", "None", "None")
    _c_components = (RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP, RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP)
    _c_name = ("PATIENT", "COMMON ORDER", "SPECIMEN")
    _c_is_group = (True, True, True)
    _c_attrs = ("patient", "common_order", "specimen",)
    # fmt: on

    def __init__(
        self,
        common_order: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        | tuple[
            RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...
        ],  #  Required. (ORC.14, OBR.17, NTE.18, CTD.19, ...)
        patient: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP
        | None = None,  #  PID.8, PD1.9, NK1.10, NTE.11
        specimen: RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP
        | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP, ...]
        | None = None,  #  (SPM.22, OBX.23, ...)
    ):
        """
        None - `RSP_Z90_QUERY_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP>`_
        Segment group for RSP_Z90 - Lab Results History Response consisting of PATIENT|None, COMMON ORDER, SPECIMEN|None

        :param patient: Patient segment group: [PID, PD1|None, NK1|None, NTE|None, VISIT|None] (id: PATIENT | seq: 8, 9, 10, 11, None | use: O | rpt: 1)
        :param common_order: Common Order segment group: [ORC, TIMING|None, OBR, NTE|None, CTD|None, OBSERVATION] (id: COMMON ORDER | seq: 14, None, 17, 18, 19, None | use: R | rpt: *)
        :param specimen: Specimen segment group: [SPM, OBX|None] (id: SPECIMEN | seq: 22, 23 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient = patient
        self.common_order = common_order
        self.specimen = specimen

    @property  # get RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)

    @property  # get COMMON ORDER
    def common_order(
        self,
    ) -> tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...]:
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        """
        return self._c_data[1]

    @common_order.setter  # set COMMON ORDER
    def common_order(
        self,
        common_order: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...],
    ):
        """
        id: COMMON ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP.None | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_COMMON_ORDER_GROUP
        """
        if isinstance(common_order, tuple):
            self._c_data[1] = common_order
        else:
            self._c_data[1] = (common_order,)

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> tuple[RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP, ...] | tuple[None]:
        """
        id: RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[2]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP
        | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP, ...]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP.None | tuple[RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[2] = specimen
        else:
            self._c_data[2] = (specimen,)
