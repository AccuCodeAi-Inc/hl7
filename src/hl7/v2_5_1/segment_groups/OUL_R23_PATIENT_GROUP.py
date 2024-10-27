from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segments.PD1 import PD1
from ..segments.NTE import NTE


"""
PATIENT - OUL_R23_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R23_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R23_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID, NTE, PD1
)

oul_r23_patient_group = OUL_R23_PATIENT_GROUP(  # PATIENT - Segment group for OUL_R23 - Unsolicited Specimen Container Oriented Observation Message consisting of PID, PD1|None, NTE|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R23_PATIENT_GROUP TEMPLATE-----
"""


class OUL_R23_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R23_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for OUL_R23 - Unsolicited Specimen Container Oriented Observation Message consisting of PID, PD1|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("4", "5", "6")
    _c_components = (PID, PD1, NTE)
    _c_name = ("PID", "PD1", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.4
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
    ):
        """
        None - `OUL_R23_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23_PATIENT_GROUP>`_
        Segment group for OUL_R23 - Unsolicited Specimen Container Oriented Observation Message consisting of PID, PD1|None, NTE|None

        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments

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

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: NTE.6 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)
