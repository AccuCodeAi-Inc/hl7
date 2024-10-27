from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID


"""
QUERY RESPONSE - RSP_K24_QUERY_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_K24_QUERY_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_K24_QUERY_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)

rsp_k24_query_response_group = RSP_K24_QUERY_RESPONSE_GROUP(  # QUERY RESPONSE - Segment group for RSP_K24 - Allocate Identifiers Response consisting of PID
    patient_identification=pid,  # PID(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_K24_QUERY_RESPONSE_GROUP TEMPLATE-----
"""


class RSP_K24_QUERY_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_K24_QUERY_RESPONSE_GROUP"""
    _hl7_name = """QUERY RESPONSE"""
    _hl7_description = """Segment group for RSP_K24 - Allocate Identifiers Response consisting of PID"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K24_QUERY_RESPONSE_GROUP"""
    _c_length = (-1,)
    _c_rpt = (1)
    _c_usage = ("R")
    _c_aliases = ("7")
    _c_components = (PID)
    _c_name = ("PID")
    _c_is_group = (False)
    _c_attrs = ("patient_identification",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
    ):
        """
        None - `RSP_K24_QUERY_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_K24_QUERY_RESPONSE_GROUP>`_
        Segment group for RSP_K24 - Allocate Identifiers Response consisting of PID

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 1
        self.patient_identification = patient_identification

    @property  # get PID.7
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        return_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.7
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        param_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)
