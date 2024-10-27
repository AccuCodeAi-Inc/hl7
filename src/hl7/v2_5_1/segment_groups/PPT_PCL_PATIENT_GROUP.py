from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP,
)
from ..segments.PID import PID
from ..segment_groups.PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP import (
    PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP,
)


"""
PATIENT - PPT_PCL_PATIENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::PPT_PCL_PATIENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPT_PCL_PATIENT_GROUP
from utils.hl7.v2_5_1.segments import (
    PID
)
from utils.hl7.v2_5_1.segment_groups import (
    PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP, PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP
)

ppt_pcl_patient_group = PPT_PCL_PATIENT_GROUP(  # PATIENT - Segment group for PPT_PCL - Pathway (goal-oriented) query response consisting of PID, PATIENT VISIT|None, PATHWAY
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP(...) 
    pathway=ppt_pcl_patient_group_pathway_group,  # PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::PPT_PCL_PATIENT_GROUP TEMPLATE-----
"""


class PPT_PCL_PATIENT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """PPT_PCL_PATIENT_GROUP"""
    _hl7_name = """PATIENT"""
    _hl7_description = """Segment group for PPT_PCL - Pathway (goal-oriented) query response consisting of PID, PATIENT VISIT|None, PATHWAY"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPT_PCL_PATIENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("7", "None", "None")
    _c_components = (PID, PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP, PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP)
    _c_name = ("PID", "PATIENT VISIT", "PATHWAY")
    _c_is_group = (False, True, True)
    _c_attrs = ("patient_identification", "patient_visit", "pathway",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.7
        pathway: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP
        | tuple[
            PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP, ...
        ],  #  Required. (PTH.10, NTE.11, VAR.12, ...)
        patient_visit: PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP
        | None = None,  #  PV1.8, PV2.9
    ):
        """
        None - `PPT_PCL_PATIENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPT_PCL_PATIENT_GROUP>`_
        Segment group for PPT_PCL - Pathway (goal-oriented) query response consisting of PID, PATIENT VISIT|None, PATHWAY

        :param patient_identification: Patient Identification (id: PID | seq: 7 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 8, 9 | use: O | rpt: 1)
        :param pathway: Pathway segment group: [PTH, NTE|None, VAR|None, PATHWAY ROLE|None, GOAL|None] (id: PATHWAY | seq: 10, 11, 12, None, None | use: R | rpt: *)
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

    @property  # get PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP | None:
        """
        id: PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        return self._c_data[1][0]

    @patient_visit.setter  # set PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP.None
    def patient_visit(
        self, patient_v_isit: PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP | None
    ):
        """
        id: PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATIENT_VISIT_GROUP
        """
        self._c_data[1] = (patient_v_isit,)

    @property  # get PATHWAY
    def pathway(self) -> tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP, ...]:
        """
        id: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP
        """
        return self._c_data[2]

    @pathway.setter  # set PATHWAY
    def pathway(
        self,
        pathway: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP
        | tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP, ...],
    ):
        """
        id: PATHWAY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP.None | tuple[PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPT_PCL_PATIENT_GROUP_PATHWAY_GROUP
        """
        if isinstance(pathway, tuple):
            self._c_data[2] = pathway
        else:
            self._c_data[2] = (pathway,)
