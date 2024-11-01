from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CSP import CSP
from ..segments.CSR import CSR


"""
STUDY - PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP
from utils.hl7.v2_5_1.segments import (
    CSR, CSP
)

pex_p07_experience_group_pex_observation_group_pex_cause_group_study_group = PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP(  # STUDY - Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of CSR, CSP|None
    clinical_study_registration=csr,  # CSR(...)  # Required.
    clinical_study_phase=None,  # CSP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP TEMPLATE-----
"""


class PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP"""
    _hl7_name = """STUDY"""
    _hl7_description = """Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of CSR, CSP|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("30", "31")
    _c_components = (CSR, CSP)
    _c_name = ("CSR", "CSP")
    _c_is_group = (False, False)
    _c_attrs = ("clinical_study_registration", "clinical_study_phase",)
    # fmt: on

    def __init__(
        self,
        clinical_study_registration: CSR,  #  Required. CSR.30
        clinical_study_phase: CSP | tuple[CSP, ...] | None = None,  #  CSP.31
    ):
        """
        None - `PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP_STUDY_GROUP>`_
        Segment group for PEX_P07_EXPERIENCE_GROUP_PEX_OBSERVATION_GROUP_PEX_CAUSE_GROUP - PEX CAUSE consisting of CSR, CSP|None

        :param clinical_study_registration: Clinical Study Registration (id: CSR | seq: 30 | use: R | rpt: 1)
        :param clinical_study_phase: Clinical Study Phase (id: CSP | seq: 31 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.clinical_study_registration = clinical_study_registration
        self.clinical_study_phase = clinical_study_phase

    @property  # get CSR.30
    def clinical_study_registration(self) -> CSR:
        """
        id: CSR | use: R | rpt: 1 | seq: 30
        ---
        return_type: CSR.30: Clinical Study Registration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR
        """
        return self._c_data[0][0]

    @clinical_study_registration.setter  # set CSR.30
    def clinical_study_registration(self, csr: CSR):
        """
        id: CSR | use: R | rpt: 1 | seq: 30
        ---
        param_type: CSR.30: Clinical Study Registration
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSR
        """
        self._c_data[0] = (csr,)

    @property  # get CSP
    def clinical_study_phase(self) -> tuple[CSP, ...] | tuple[None]:
        """
        id: CSP SEGMENT GROUP | use: O | rpt: * | seq: 31
        ---
        return_type: tuple[CSP, ...]: (Clinical Study Phase, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP
        """
        return self._c_data[1]

    @clinical_study_phase.setter  # set CSP
    def clinical_study_phase(self, csp: CSP | tuple[CSP, ...] | None):
        """
        id: CSP SEGMENT GROUP | use: O | rpt: * | seq: 31
        ---
        param_type: CSP.31 | tuple[CSP, ...]: (Clinical Study Phase, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSP
        """
        if isinstance(csp, tuple):
            self._c_data[1] = csp
        else:
            self._c_data[1] = (csp,)
