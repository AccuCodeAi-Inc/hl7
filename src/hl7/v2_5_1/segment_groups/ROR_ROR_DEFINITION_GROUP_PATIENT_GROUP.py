from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segments.NTE import NTE


"""
PATIENT - ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID, NTE
)

ror_ror_definition_group_patient_group = ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for ROR_ROR_DEFINITION_GROUP - DEFINITION consisting of PID, NTE|None
    patient_identification=pid,  # PID(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for ROR_ROR_DEFINITION_GROUP - DEFINITION consisting of PID, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("7", "8")
    _c_components = (PID, NTE)
    _c_name = ("PID", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("patient_identification", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.8
    ):
        """
        None - `ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ROR_ROR_DEFINITION_GROUP_PATIENT_GROUP>`_
        Segment group for ROR_ROR_DEFINITION_GROUP - DEFINITION consisting of PID, NTE|None

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 8 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.patient_identification = patient_identification
        self.notes_and_comments = notes_and_comments

    @property  # get PID.7
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        return_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.7
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 7
        ---
        param_type: PID.7: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: NTE.8 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
