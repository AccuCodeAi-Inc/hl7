from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.PPG_PCG_PATHWAY_GROUP import PPG_PCG_PATHWAY_GROUP
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segment_groups.PPG_PCG_PATIENT_VISIT_GROUP import PPG_PCG_PATIENT_VISIT_GROUP


"""
Pathway (goal-oriented) add - PPG_PCG
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PPG_PCG TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPG_PCG
from utils.hl7.v2_5_1.segments import (
    PID, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    PPG_PCG_PATIENT_VISIT_GROUP, PPG_PCG_PATHWAY_GROUP
)

ppg_pcg = PPG_PCG(  #  - 
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PPG_PCG_PATIENT_VISIT_GROUP(...) 
    pathway=ppg_pcg_pathway_group,  # PPG_PCG_PATHWAY_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::PPG_PCG TEMPLATE-----
"""


class PPG_PCG(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PPG_PCG"""
    _hl7_name = """Pathway (goal-oriented) add"""
    _hl7_description = """"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPG_PCG"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, PID, PPG_PCG_PATIENT_VISIT_GROUP, PPG_PCG_PATHWAY_GROUP)
    _c_name = ("MSH", "SFT", "PID", "PATIENT VISIT", "PATHWAY")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "patient_identification", "patient_visit", "pathway",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient_identification: PID,  #  Required. PID.3
        pathway: PPG_PCG_PATHWAY_GROUP
        | tuple[PPG_PCG_PATHWAY_GROUP, ...],  #  Required. (PTH.6, NTE.7, VAR.8, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_visit: PPG_PCG_PATIENT_VISIT_GROUP | None = None,  #  PV1.4, PV2.5
    ):
        """
         - `PPG_PCG <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPG_PCG>`_


        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 4, 5 | use: O | rpt: 1)
        :param pathway: Pathway segment group: [PTH, NTE|None, VAR|None, PATHWAY ROLE|None, GOAL|None] (id: PATHWAY | seq: 6, 7, 8, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.pathway = pathway

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get PID.3
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 3
        ---
        return_type: PID.3: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[2][0]

    @patient_identification.setter  # set PID.3
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 3
        ---
        param_type: PID.3: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[2] = (pid,)

    @property  # get PPG_PCG_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PPG_PCG_PATIENT_VISIT_GROUP | None:
        """
        id: PPG_PCG_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PPG_PCG_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATIENT_VISIT_GROUP
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set PPG_PCG_PATIENT_VISIT_GROUP.None
    def patient_visit(self, patient_v_isit: PPG_PCG_PATIENT_VISIT_GROUP | None):
        """
        id: PPG_PCG_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PPG_PCG_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATIENT_VISIT_GROUP
        """
        self._c_data[3] = (patient_v_isit,)

    @property  # get PATHWAY
    def pathway(self) -> tuple[PPG_PCG_PATHWAY_GROUP, ...]:
        """
        id: PPG_PCG_PATHWAY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PPG_PCG_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATHWAY_GROUP
        """
        return self._c_data[4]

    @pathway.setter  # set PATHWAY
    def pathway(
        self, pathway: PPG_PCG_PATHWAY_GROUP | tuple[PPG_PCG_PATHWAY_GROUP, ...]
    ):
        """
        id: PATHWAY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PPG_PCG_PATHWAY_GROUP.None | tuple[PPG_PCG_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPG_PCG_PATHWAY_GROUP
        """
        if isinstance(pathway, tuple):
            self._c_data[4] = pathway
        else:
            self._c_data[4] = (pathway,)
