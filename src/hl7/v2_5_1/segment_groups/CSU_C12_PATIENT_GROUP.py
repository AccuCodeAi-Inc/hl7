from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PD1 import PD1
from ..segment_groups.CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP import (
    CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP,
)
from ..segments.CSR import CSR
from ..segment_groups.CSU_C12_PATIENT_GROUP_VISIT_GROUP import (
    CSU_C12_PATIENT_GROUP_VISIT_GROUP,
)
from ..segments.PID import PID
from ..segments.NTE import NTE


"""
PATIENT - CSU_C12_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CSU_C12_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C12_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PD1, CSR, NTE, PID
)
from utils.hl7.v2_5_1.segment_groups import (
    CSU_C12_PATIENT_GROUP_VISIT_GROUP, CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP
)

csu_c12_patient_group = CSU_C12_PATIENT_GROUP(  # PATIENT - Segment group for CSU_C12 - Update/correction of patient order/result information consisting of PID, PD1|None, NTE|None, VISIT|None, CSR, STUDY PHASE
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
    visit=None,  # CSU_C12_PATIENT_GROUP_VISIT_GROUP(...) 
    clinical_study_registration=csr,  # CSR(...)  # Required.
    study_phase=csu_c12_patient_group_study_phase_group,  # CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CSU_C12_PATIENT_GROUP TEMPLATE-----
"""


class CSU_C12_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CSU_C12_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for CSU_C12 - Update/correction of patient order/result information consisting of PID, PD1|None, NTE|None, VISIT|None, CSR, STUDY PHASE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C12_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R", "R")
    _c_aliases = ("3", "4", "5", "None", "8", "None")
    _c_components = (PID, PD1, NTE, CSU_C12_PATIENT_GROUP_VISIT_GROUP, CSR, CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP)
    _c_name = ("PID", "PD1", "NTE", "VISIT", "CSR", "STUDY PHASE")
    _c_is_group = (False, False, False, True, False, True)
    _c_attrs = ("patient_identification", "patient_additional_demographic", "notes_and_comments", "visit", "clinical_study_registration", "study_phase",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.3
        clinical_study_registration: CSR,  #  Required. CSR.8
        study_phase: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP
        | tuple[
            CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP, ...
        ],  #  Required. (CSP.9, ...)
        patient_additional_demographic: PD1 | None = None,  #  PD1.4
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.5
        visit: CSU_C12_PATIENT_GROUP_VISIT_GROUP | None = None,  #  PV1.6, PV2.7
    ):
        """
        None - `CSU_C12_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C12_PATIENT_GROUP>`_
        Segment group for CSU_C12 - Update/correction of patient order/result information consisting of PID, PD1|None, NTE|None, VISIT|None, CSR, STUDY PHASE

        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 4 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 5 | use: O | rpt: *)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 6, 7 | use: O | rpt: 1)
        :param clinical_study_registration: Clinical Study Registration (id: CSR | seq: 8 | use: R | rpt: 1)
        :param study_phase: Study Phase segment group: [CSP|None, STUDY SCHEDULE] (id: STUDY PHASE | seq: 9, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments
        self.visit = visit
        self.clinical_study_registration = clinical_study_registration
        self.study_phase = study_phase

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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: NTE.5 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get CSU_C12_PATIENT_GROUP_VISIT_GROUP.None
    def visit(self) -> CSU_C12_PATIENT_GROUP_VISIT_GROUP | None:
        """
        id: CSU_C12_PATIENT_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: CSU_C12_PATIENT_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C12_PATIENT_GROUP_VISIT_GROUP
        """
        return self._c_data[3][0]

    @visit.setter  # set CSU_C12_PATIENT_GROUP_VISIT_GROUP.None
    def visit(self, v_isit: CSU_C12_PATIENT_GROUP_VISIT_GROUP | None):
        """
        id: CSU_C12_PATIENT_GROUP_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: CSU_C12_PATIENT_GROUP_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C12_PATIENT_GROUP_VISIT_GROUP
        """
        self._c_data[3] = (v_isit,)

    @property  # get CSR.8
    def clinical_study_registration(self) -> CSR:
        """
        id: CSR | use: R | rpt: 1 | seq: 8
        ---
        return_type: CSR.8: Clinical Study Registration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR
        """
        return self._c_data[4][0]

    @clinical_study_registration.setter  # set CSR.8
    def clinical_study_registration(self, csr: CSR):
        """
        id: CSR | use: R | rpt: 1 | seq: 8
        ---
        param_type: CSR.8: Clinical Study Registration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR
        """
        self._c_data[4] = (csr,)

    @property  # get STUDY PHASE
    def study_phase(self) -> tuple[CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP, ...]:
        """
        id: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP
        """
        return self._c_data[5]

    @study_phase.setter  # set STUDY PHASE
    def study_phase(
        self,
        study_phase: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP
        | tuple[CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP, ...],
    ):
        """
        id: STUDY PHASE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP.None | tuple[CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C12_PATIENT_GROUP_STUDY_PHASE_GROUP
        """
        if isinstance(study_phase, tuple):
            self._c_data[5] = study_phase
        else:
            self._c_data[5] = (study_phase,)
