from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2


"""
VISIT - RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
from utils.hl7.v2_5_1.segments import (
    PV2, PV1
)

rsp_z88_query_response_group_patient_group_allergy_group_visit_group = RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP(  # VISIT - Segment group for RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP - ALLERGY consisting of PV1, PV2|None
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP TEMPLATE-----
"""


class RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP"""
    _hl7_name = """VISIT"""
    _hl7_description = """Segment group for RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP - ALLERGY consisting of PV1, PV2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("12", "13")
    _c_components = (PV1, PV2)
    _c_name = ("PV1", "PV2")
    _c_is_group = (False, False)
    _c_attrs = ("patient_visit", "patient_visit_additional_information",)
    # fmt: on

    def __init__(
        self,
        patient_visit: PV1,  #  Required. PV1.12
        patient_visit_additional_information: PV2 | None = None,  #  PV2.13
    ):
        """
        None - `RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP>`_
        Segment group for RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP - ALLERGY consisting of PV1, PV2|None

        :param patient_visit: Patient Visit (id: PV1 | seq: 12 | use: R | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information

    @property  # get PV1.12
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 12
        ---
        return_type: PV1.12: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[0][0]

    @patient_visit.setter  # set PV1.12
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 12
        ---
        param_type: PV1.12: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[0] = (pv1,)

    @property  # get PV2.13
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 13
        ---
        return_type: PV2.13: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[1][0]

    @patient_visit_additional_information.setter  # set PV2.13
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 13
        ---
        param_type: PV2.13: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[1] = (pv2,)
