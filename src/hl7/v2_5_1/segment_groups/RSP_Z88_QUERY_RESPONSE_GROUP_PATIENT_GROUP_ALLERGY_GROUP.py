from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP import (
    RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP,
)
from ..segments.AL1 import AL1


"""
ALLERGY - RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP
from utils.hl7.v2_5_1.segments import (
    AL1
)
from utils.hl7.v2_5_1.segment_groups import (
    RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
)

rsp_z88_query_response_group_patient_group_allergy_group = RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP(  # ALLERGY - Segment group for RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of AL1, VISIT|None
    patient_allergy_information=al1,  # AL1(...)  # Required.
    visit=None,  # RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP TEMPLATE-----
"""


class RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP"""
    _hl7_name = """ALLERGY"""
    _hl7_description = """Segment group for RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of AL1, VISIT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (65535, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("11", "None")
    _c_components = (AL1, RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP)
    _c_name = ("AL1", "VISIT")
    _c_is_group = (False, True)
    _c_attrs = ("patient_allergy_information", "visit",)
    # fmt: on

    def __init__(
        self,
        patient_allergy_information: AL1 | tuple[AL1, ...],  #  Required. AL1.11
        visit: RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
        | None = None,  #  PV1.12, PV2.13
    ):
        """
        None - `RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP>`_
        Segment group for RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of AL1, VISIT|None

        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 11 | use: R | rpt: *)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 12, 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_allergy_information = patient_allergy_information
        self.visit = visit

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

    @property  # get RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP.None
    def visit(
        self,
    ) -> RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP | None:
        """
        id: RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
        """
        return self._c_data[1][0]

    @visit.setter  # set RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP.None
    def visit(
        self,
        v_isit: RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
        | None,
    ):
        """
        id: RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RSP_Z88_QUERY_RESPONSE_GROUP_PATIENT_GROUP_ALLERGY_GROUP_VISIT_GROUP
        """
        self._c_data[1] = (v_isit,)
