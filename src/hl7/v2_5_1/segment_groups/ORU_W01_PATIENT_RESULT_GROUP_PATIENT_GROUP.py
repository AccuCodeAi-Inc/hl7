from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP import (
    ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP,
)
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1


"""
PATIENT - ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID, NK1, NTE, PD1
)
from utils.hl7.v2_5_1.segment_groups import (
    ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP
)

oru_w01_patient_result_group_patient_group = ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP(  # PATIENT - Segment group for ORU_W01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of PID, PD1|None, NK1|None, NTE|None, VISIT|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    notes_and_comments=None,  # NTE(...) 
    visit=None,  # ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP TEMPLATE-----
"""


class ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for ORU_W01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of PID, PD1|None, NK1|None, NTE|None, VISIT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("3", "4", "5", "6", "None")
    _c_components = (PID, PD1, NK1, NTE, ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP)
    _c_name = ("PID", "PD1", "NK1", "NTE", "VISIT")
    _c_is_group = (False, False, False, False, True)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "next_of_kin_or_associated_parties", "notes_and_comments", "visit",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.3
        patient_additional_demographic: PD1 | None = None,  #  PD1.4
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        visit: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP
        | None = None,  #  PV1.7, PV2.8
    ):
        """
        None - `ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP>`_
        Segment group for ORU_W01_PATIENT_RESULT_GROUP - PATIENT RESULT consisting of PID, PD1|None, NK1|None, NTE|None, VISIT|None

        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 4 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 5 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 7, 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.notes_and_comments = notes_and_comments
        self.visit = visit

    @property  # get PID.3
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 3
        ---
        return_type: PID.3: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[0][0]

    @patient_identification.setter  # set PID.3
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 3
        ---
        param_type: PID.3: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[0] = (pid,)

    @property  # get PD1.4
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 4
        ---
        return_type: PD1.4: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[1][0]

    @patient_additional_demographic.setter  # set PD1.4
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 4
        ---
        param_type: PD1.4: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[1] = (pd1,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[2]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: NK1.5 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[2] = nk1
        else:
            self._c_data[2] = (nk1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

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
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP.None
    def visit(self) -> ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP | None:
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP
        """
        return self._c_data[4][0]

    @visit.setter  # set ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP.None
    def visit(
        self, v_isit: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP | None
    ):
        """
        id: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_W01_PATIENT_RESULT_GROUP_PATIENT_GROUP_VISIT_GROUP
        """
        self._c_data[4] = (v_isit,)
