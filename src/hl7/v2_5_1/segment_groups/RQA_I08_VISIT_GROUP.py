from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2


"""
VISIT - RQA_I08_VISIT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RQA_I08_VISIT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RQA_I08_VISIT_GROUP
from utils.hl7.v2_5_1.segments import (
    PV1, PV2
)

rqa_i08_visit_group = RQA_I08_VISIT_GROUP(  # VISIT - Segment group for RQA_I08 - Request for treatment authorization information consisting of PV1, PV2|None
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RQA_I08_VISIT_GROUP TEMPLATE-----
"""


class RQA_I08_VISIT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RQA_I08_VISIT_GROUP"""
    _hl7_name = """VISIT"""
    _hl7_description = """Segment group for RQA_I08 - Request for treatment authorization information consisting of PV1, PV2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQA_I08_VISIT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("25", "26")
    _c_components = (PV1, PV2)
    _c_name = ("PV1", "PV2")
    _c_is_group = (False, False)
    _c_attrs = ("patient_visit", "patient_visit_additional_information",)
    # fmt: on

    def __init__(
        self,
        patient_visit: PV1,  #  Required. PV1.25
        patient_visit_additional_information: PV2 | None = None,  #  PV2.26
    ):
        """
        None - `RQA_I08_VISIT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQA_I08_VISIT_GROUP>`_
        Segment group for RQA_I08 - Request for treatment authorization information consisting of PV1, PV2|None

        :param patient_visit: Patient Visit (id: PV1 | seq: 25 | use: R | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information

    @property  # get PV1.25
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 25
        ---
        return_type: PV1.25: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[0][0]

    @patient_visit.setter  # set PV1.25
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 25
        ---
        param_type: PV1.25: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[0] = (pv1,)

    @property  # get PV2.26
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 26
        ---
        return_type: PV2.26: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[1][0]

    @patient_visit_additional_information.setter  # set PV2.26
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 26
        ---
        param_type: PV2.26: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[1] = (pv2,)
