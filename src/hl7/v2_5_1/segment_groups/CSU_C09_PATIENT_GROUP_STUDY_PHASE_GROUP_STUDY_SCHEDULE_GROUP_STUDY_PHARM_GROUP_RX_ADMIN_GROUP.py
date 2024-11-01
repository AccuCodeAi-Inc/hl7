from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXA import RXA
from ..segments.RXR import RXR


"""
RX ADMIN - CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP
from utils.hl7.v2_5_1.segments import (
    RXA, RXR
)

csu_c09_patient_group_study_phase_group_study_schedule_group_study_pharm_group_rx_admin_group = CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP(  # RX ADMIN - Segment group for CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP - STUDY PHARM consisting of RXA, RXR
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP TEMPLATE-----
"""


class CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP"""
    _hl7_name = """RX ADMIN"""
    _hl7_description = """Segment group for CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP - STUDY PHARM consisting of RXA, RXR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "R")
    _c_aliases = ("17", "18")
    _c_components = (RXA, RXR)
    _c_name = ("RXA", "RXR")
    _c_is_group = (False, False)
    _c_attrs = ("pharmacy_or_treatment_administration", "pharmacy_or_treatment_route",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_administration: RXA,  #  Required. RXA.17
        pharmacy_or_treatment_route: RXR,  #  Required. RXR.18
    ):
        """
        None - `CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP_RX_ADMIN_GROUP>`_
        Segment group for CSU_C09_PATIENT_GROUP_STUDY_PHASE_GROUP_STUDY_SCHEDULE_GROUP_STUDY_PHARM_GROUP - STUDY PHARM consisting of RXA, RXR

        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 17 | use: R | rpt: 1)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 18 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route

    @property  # get RXA.17
    def pharmacy_or_treatment_administration(self) -> RXA:
        """
        id: RXA | use: R | rpt: 1 | seq: 17
        ---
        return_type: RXA.17: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_administration.setter  # set RXA.17
    def pharmacy_or_treatment_administration(self, rxa: RXA):
        """
        id: RXA | use: R | rpt: 1 | seq: 17
        ---
        param_type: RXA.17: Pharmacy/Treatment Administration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        self._c_data[0] = (rxa,)

    @property  # get RXR.18
    def pharmacy_or_treatment_route(self) -> RXR:
        """
        id: RXR | use: R | rpt: 1 | seq: 18
        ---
        return_type: RXR.18: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1][0]

    @pharmacy_or_treatment_route.setter  # set RXR.18
    def pharmacy_or_treatment_route(self, rxr: RXR):
        """
        id: RXR | use: R | rpt: 1 | seq: 18
        ---
        param_type: RXR.18: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[1] = (rxr,)
