from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.DG1 import DG1
from ..segments.PV1 import PV1
from ..segments.PID import PID
from ..segments.PV2 import PV2


"""
PATIENT - SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    DG1, PID, PV1, PV2
)

sqr_s25_schedule_group_patient_group = SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for SQR_S25_SCHEDULE_GROUP - SCHEDULE consisting of PID, PV1|None, PV2|None, DG1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PV1(...) 
    patient_visit_additional_information=None,  # PV2(...) 
    diagnosis=None,  # DG1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for SQR_S25_SCHEDULE_GROUP - SCHEDULE consisting of PID, PV1|None, PV2|None, DG1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 1)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("8", "9", "10", "11")
    _c_components = (PID, PV1, PV2, DG1)
    _c_name = ("PID", "PV1", "PV2", "DG1")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("patient_identification", "patient_visit", "patient_visit_additional_information", "diagnosis",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.8
        patient_visit: PV1 | None = None,  #  PV1.9
        patient_visit_additional_information: PV2 | None = None,  #  PV2.10
        diagnosis: DG1 | None = None,  #  DG1.11
    ):
        """
        None - `SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP>`_
        Segment group for SQR_S25_SCHEDULE_GROUP - SCHEDULE consisting of PID, PV1|None, PV2|None, DG1|None

        :param patient_identification: Patient Identification (id: PID | seq: 8 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 9 | use: O | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 10 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 11 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.diagnosis = diagnosis

    @property  # get PID.8
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        return_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.8
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        param_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PV1.9
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 9
        ---
        return_type: PV1.9: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PV1.9
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 9
        ---
        param_type: PV1.9: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[1] = (pv1,)

    @property  # get PV2.10
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 10
        ---
        return_type: PV2.10: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[2][0]

    @patient_visit_additional_information.setter  # set PV2.10
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 10
        ---
        param_type: PV2.10: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[2] = (pv2,)

    @property  # get DG1.11
    def diagnosis(self) -> DG1 | None:
        """
        id: DG1 | use: O | rpt: 1 | seq: 11
        ---
        return_type: DG1.11: Diagnosis
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[3][0]

    @diagnosis.setter  # set DG1.11
    def diagnosis(self, dg1: DG1 | None):
        """
        id: DG1 | use: O | rpt: 1 | seq: 11
        ---
        param_type: DG1.11: Diagnosis
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        self._c_data[3] = (dg1,)
