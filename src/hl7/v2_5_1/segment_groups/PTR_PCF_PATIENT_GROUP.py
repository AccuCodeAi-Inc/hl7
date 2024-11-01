from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.PID import PID
from ..segment_groups.PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)
from ..segment_groups.PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP import (
    PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP,
)


"""
PATIENT - PTR_PCF_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PTR_PCF_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PTR_PCF_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP
)

ptr_pcf_patient_group = PTR_PCF_PATIENT_GROUP(  # PATIENT - Segment group for PTR_PCF - Pathway (problem-oriented) query response consisting of PID, PATIENT VISIT|None, PATHWAY
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
    pathway=ptr_pcf_patient_group_pathway_group,  # PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PTR_PCF_PATIENT_GROUP TEMPLATE-----
"""


class PTR_PCF_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PTR_PCF_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for PTR_PCF - Pathway (problem-oriented) query response consisting of PID, PATIENT VISIT|None, PATHWAY"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PTR_PCF_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("7", "None", "None")
    _c_components = (PID, PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP, PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP)
    _c_name = ("PID", "PATIENT VISIT", "PATHWAY")
    _c_is_group = (False, True, True)
    _c_attrs = ("patient_identification", "patient_visit", "pathway",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        pathway: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP
        | tuple[
            PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP, ...
        ],  #  Required. (PTH.10, NTE.11, VAR.12, ...)
        patient_visit: PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.8, PV2.9
    ):
        """
        None - `PTR_PCF_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PTR_PCF_PATIENT_GROUP>`_
        Segment group for PTR_PCF - Pathway (problem-oriented) query response consisting of PID, PATIENT VISIT|None, PATHWAY

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 8, 9 | use: O | rpt: 1)
        :param pathway: Pathway segment group: [PTH, NTE|None, VAR|None, PATHWAY ROLE|None, PROBLEM|None] (id: PATHWAY | seq: 10, 11, 12, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.pathway = pathway

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

    @property  # get PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[1] = (patient_v_isit,)

    @property  # get PATHWAY
    def pathway(self) -> tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP, ...]:
        """
        id: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP
        """
        return self._c_data[2]

    @pathway.setter  # set PATHWAY
    def pathway(
        self,
        pathway: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP
        | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP, ...],
    ):
        """
        id: PATHWAY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP.None | tuple[PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP_PATHWAY_GROUP
        """
        if isinstance(pathway, tuple):
            self._c_data[2] = pathway
        else:
            self._c_data[2] = (pathway,)
