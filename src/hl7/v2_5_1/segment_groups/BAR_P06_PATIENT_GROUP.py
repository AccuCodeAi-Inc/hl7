from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PV1 import PV1
from ..segments.PID import PID


"""
PATIENT - BAR_P06_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BAR_P06_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P06_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID, PV1
)

bar_p06_patient_group = BAR_P06_PATIENT_GROUP(  # PATIENT - Segment group for BAR_P06 - End account consisting of PID, PV1|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PV1(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BAR_P06_PATIENT_GROUP TEMPLATE-----
"""


class BAR_P06_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BAR_P06_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for BAR_P06 - End account consisting of PID, PV1|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P06_PATIENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("4", "5")
    _c_components = (PID, PV1)
    _c_name = ("PID", "PV1")
    _c_is_group = (False, False)
    _c_attrs = ("patient_identification", "patient_visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1 | None = None,  #  PV1.5
    ):
        """
        None - `BAR_P06_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P06_PATIENT_GROUP>`_
        Segment group for BAR_P06 - End account consisting of PID, PV1|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 5 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PV1.5
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PV1.5
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[1] = (pv1,)
