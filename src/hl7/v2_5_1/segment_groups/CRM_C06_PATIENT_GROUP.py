from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CSP import CSP
from ..segments.PV1 import PV1
from ..segments.PID import PID
from ..segments.CSR import CSR


"""
PATIENT - CRM_C06_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::CRM_C06_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CRM_C06_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    CSR, PID, CSP, PV1
)

crm_c06_patient_group = CRM_C06_PATIENT_GROUP(  # PATIENT - Segment group for CRM_C06 - Cancel patient entering a phase (clerical mistake) consisting of PID, PV1|None, CSR, CSP|None
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PV1(...) 
    clinical_study_registration=csr,  # CSR(...)  # Required.
    clinical_study_phase=None,  # CSP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::CRM_C06_PATIENT_GROUP TEMPLATE-----
"""


class CRM_C06_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """CRM_C06_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for CRM_C06 - Cancel patient entering a phase (clerical mistake) consisting of PID, PV1|None, CSR, CSP|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CRM_C06_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("3", "4", "5", "6")
    _c_components = (PID, PV1, CSR, CSP)
    _c_name = ("PID", "PV1", "CSR", "CSP")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("patient_identification", "patient_visit", "clinical_study_registration", "clinical_study_phase",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.3
        clinical_study_registration: CSR,  #  Required. CSR.5
        patient_visit: PV1 | None = None,  #  PV1.4
        clinical_study_phase: CSP | tuple[CSP, ...] | None = None,  #  CSP.6
    ):
        """
        None - `CRM_C06_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CRM_C06_PATIENT_GROUP>`_
        Segment group for CRM_C06 - Cancel patient entering a phase (clerical mistake) consisting of PID, PV1|None, CSR, CSP|None

        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 4 | use: O | rpt: 1)
        :param clinical_study_registration: Clinical Study Registration (id: CSR | seq: 5 | use: R | rpt: 1)
        :param clinical_study_phase: Clinical Study Phase (id: CSP | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.clinical_study_registration = clinical_study_registration
        self.clinical_study_phase = clinical_study_phase

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

    @property  # get PV1.4
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 4
        ---
        return_type: PV1.4: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PV1.4
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 4
        ---
        param_type: PV1.4: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[1] = (pv1,)

    @property  # get CSR.5
    def clinical_study_registration(self) -> CSR:
        """
        id: CSR | use: R | rpt: 1 | seq: 5
        ---
        return_type: CSR.5: Clinical Study Registration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR
        """
        return self._c_data[2][0]

    @clinical_study_registration.setter  # set CSR.5
    def clinical_study_registration(self, csr: CSR):
        """
        id: CSR | use: R | rpt: 1 | seq: 5
        ---
        param_type: CSR.5: Clinical Study Registration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR
        """
        self._c_data[2] = (csr,)

    @property  # get CSP
    def clinical_study_phase(self) -> tuple[CSP, ...] | tuple[None]:
        """
        id: CSP SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[CSP, ...]: (Clinical Study Phase, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP
        """
        return self._c_data[3]

    @clinical_study_phase.setter  # set CSP
    def clinical_study_phase(self, csp: CSP | tuple[CSP, ...] | None):
        """
        id: CSP SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: CSP.6 | tuple[CSP, ...]: (Clinical Study Phase, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP
        """
        if isinstance(csp, tuple):
            self._c_data[3] = csp
        else:
            self._c_data[3] = (csp,)
