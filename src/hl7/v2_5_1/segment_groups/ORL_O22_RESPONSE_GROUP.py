from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORL_O22_RESPONSE_GROUP_PATIENT_GROUP import (
    ORL_O22_RESPONSE_GROUP_PATIENT_GROUP,
)


"""
RESPONSE - ORL_O22_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O22_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O22_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O22_RESPONSE_GROUP_PATIENT_GROUP
)

orl_o22_response_group = ORL_O22_RESPONSE_GROUP(  # RESPONSE - Segment group for ORL_O22 - General Laboratory Order Response consisting of PATIENT|None
    patient=None,  # ORL_O22_RESPONSE_GROUP_PATIENT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O22_RESPONSE_GROUP TEMPLATE-----
"""


class ORL_O22_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O22_RESPONSE_GROUP"""
    _hl7_name = """RESPONSE"""
    _hl7_description = """Segment group for ORL_O22 - General Laboratory Order Response consisting of PATIENT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O22_RESPONSE_GROUP"""
    _c_length = (-1,)
    _c_rpt = (1)
    _c_usage = ("O")
    _c_aliases = ("None")
    _c_components = (ORL_O22_RESPONSE_GROUP_PATIENT_GROUP)
    _c_name = ("PATIENT")
    _c_is_group = (True)
    _c_attrs = ("patient",)
    # fmt: on

    def __init__(
        self,
        patient: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP | None = None,  #  PID.6
    ):
        """
        None - `ORL_O22_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O22_RESPONSE_GROUP>`_
        Segment group for ORL_O22 - General Laboratory Order Response consisting of PATIENT|None

        :param patient: Patient segment group: [PID, ORDER|None] (id: PATIENT | seq: 6, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 1
        self.patient = patient

    @property  # get ORL_O22_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self) -> ORL_O22_RESPONSE_GROUP_PATIENT_GROUP | None:
        """
        id: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP
        """
        return self._c_data[0][0]

    @patient.setter  # set ORL_O22_RESPONSE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP | None):
        """
        id: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORL_O22_RESPONSE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP
        """
        self._c_data[0] = (patient,)
