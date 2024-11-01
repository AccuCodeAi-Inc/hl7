from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PV2 import PV2
from ..segments.PV1 import PV1
from ..segments.AL1 import AL1


"""
VISIT - RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP
from utils.hl7.v2_5_1.segments import (
    PV2, PV1, AL1
)

rsp_z82_query_response_group_patient_group_visit_group = RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP(  # VISIT - Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of AL1, PV1, PV2|None
    patient_allergy_information=al1,  # AL1(...)  # Required.
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP TEMPLATE-----
"""


class RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP"""
    _hl7_name = """VISIT"""
    _hl7_description = """Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of AL1, PV1, PV2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (65535, 1, 1)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("11", "12", "13")
    _c_components = (AL1, PV1, PV2)
    _c_name = ("AL1", "PV1", "PV2")
    _c_is_group = (False, False, False)
    _c_attrs = ("patient_allergy_information", "patient_visit", "patient_visit_additional_information",)
    # fmt: on

    def __init__(
        self,
        patient_allergy_information: AL1 | tuple[AL1, ...],  #  Required. AL1.11
        patient_visit: PV1,  #  Required. PV1.12
        patient_visit_additional_information: PV2 | None = None,  #  PV2.13
    ):
        """
        None - `RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP_VISIT_GROUP>`_
        Segment group for RSP_Z82_QUERY_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of AL1, PV1, PV2|None

        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 11 | use: R | rpt: *)
        :param patient_visit: Patient Visit (id: PV1 | seq: 12 | use: R | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient_allergy_information = patient_allergy_information
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...]:
        """
        id: AL1 SEGMENT GROUP | use: R | rpt: * | seq: 11
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[0]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...]):
        """
        id: AL1 SEGMENT GROUP | use: R | rpt: * | seq: 11
        ---
        param_type: AL1.11 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[0] = al1
        else:
            self._c_data[0] = (al1,)

    @property  # get PV1.12
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 12
        ---
        return_type: PV1.12: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PV1.12
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 12
        ---
        param_type: PV1.12: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[1] = (pv1,)

    @property  # get PV2.13
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 13
        ---
        return_type: PV2.13: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[2][0]

    @patient_visit_additional_information.setter  # set PV2.13
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 13
        ---
        param_type: PV2.13: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[2] = (pv2,)
