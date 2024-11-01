from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segments.PD1 import PD1


"""
PATIENT PRIOR - OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP
from utils.hl7.v2_5_1.segments import (
    PD1, PID
)

oml_o21_order_group_observation_request_group_prior_result_group_patient_prior_group = OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP(  # PATIENT PRIOR - Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of PID, PD1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP TEMPLATE-----
"""


class OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP"""
    _hl7_name = """PATIENT PRIOR"""
    _hl7_description = """Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of PID, PD1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("30", "31")
    _c_components = (PID, PD1)
    _c_name = ("PID", "PD1")
    _c_is_group = (False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.30
        patient_additional_demographic: PD1 | None = None,  #  PD1.31
    ):
        """
        None - `OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP_PATIENT_PRIOR_GROUP>`_
        Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_PRIOR_RESULT_GROUP - PRIOR RESULT consisting of PID, PD1|None

        :param patient_identification: Patient Identification (id: PID | seq: 30 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 31 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic

    @property  # get PID.30
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 30
        ---
        return_type: PID.30: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.30
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 30
        ---
        param_type: PID.30: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.31
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 31
        ---
        return_type: PD1.31: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.31
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 31
        ---
        param_type: PD1.31: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)
