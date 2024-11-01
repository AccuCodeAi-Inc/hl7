from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.PPP_PCC_PATIENT_VISIT_GROUP import PPP_PCC_PATIENT_VISIT_GROUP
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH
from ..segment_groups.PPP_PCC_PATHWAY_GROUP import PPP_PCC_PATHWAY_GROUP


"""
Pathway (problem-oriented) update - PPP_PCC
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PPP_PCC TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PPP_PCC
from utils.hl7.v2_5_1.segments import (
    PID, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    PPP_PCC_PATHWAY_GROUP, PPP_PCC_PATIENT_VISIT_GROUP
)

ppp_pcc = PPP_PCC(  #  - 
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PPP_PCC_PATIENT_VISIT_GROUP(...) 
    pathway=ppp_pcc_pathway_group,  # PPP_PCC_PATHWAY_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::PPP_PCC TEMPLATE-----
"""


class PPP_PCC(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PPP_PCC"""
    _hl7_name = """Pathway (problem-oriented) update"""
    _hl7_description = """"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCC"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, PID, PPP_PCC_PATIENT_VISIT_GROUP, PPP_PCC_PATHWAY_GROUP)
    _c_name = ("MSH", "SFT", "PID", "PATIENT VISIT", "PATHWAY")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "patient_identification", "patient_visit", "pathway",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient_identification: PID,  #  Required. PID.3
        pathway: PPP_PCC_PATHWAY_GROUP
        | tuple[PPP_PCC_PATHWAY_GROUP, ...],  #  Required. (PTH.6, NTE.7, VAR.8, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_visit: PPP_PCC_PATIENT_VISIT_GROUP | None = None,  #  PV1.4, PV2.5
    ):
        """
         - `PPP_PCC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PPP_PCC>`_


        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 4, 5 | use: O | rpt: 1)
        :param pathway: Pathway segment group: [PTH, NTE|None, VAR|None, PATHWAY ROLE|None, PROBLEM|None] (id: PATHWAY | seq: 6, 7, 8, None, None | use: R | rpt: *)
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

    @property  # get PPP_PCC_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PPP_PCC_PATIENT_VISIT_GROUP | None:
        """
        id: PPP_PCC_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PPP_PCC_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATIENT_VISIT_GROUP
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set PPP_PCC_PATIENT_VISIT_GROUP.None
    def patient_visit(self, patient_v_isit: PPP_PCC_PATIENT_VISIT_GROUP | None):
        """
        id: PPP_PCC_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PPP_PCC_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATIENT_VISIT_GROUP
        """
        self._c_data[3] = (patient_v_isit,)

    @property  # get PATHWAY
    def pathway(self) -> tuple[PPP_PCC_PATHWAY_GROUP, ...]:
        """
        id: PPP_PCC_PATHWAY_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PPP_PCC_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATHWAY_GROUP
        """
        return self._c_data[4]

    @pathway.setter  # set PATHWAY
    def pathway(
        self, pathway: PPP_PCC_PATHWAY_GROUP | tuple[PPP_PCC_PATHWAY_GROUP, ...]
    ):
        """
        id: PATHWAY SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PPP_PCC_PATHWAY_GROUP.None | tuple[PPP_PCC_PATHWAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PPP_PCC_PATHWAY_GROUP
        """
        if isinstance(pathway, tuple):
            self._c_data[4] = pathway
        else:
            self._c_data[4] = (pathway,)
