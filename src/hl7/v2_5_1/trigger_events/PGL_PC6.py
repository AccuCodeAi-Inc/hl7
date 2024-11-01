from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.PGL_PC6_GOAL_GROUP import PGL_PC6_GOAL_GROUP
from ..segment_groups.PGL_PC6_PATIENT_VISIT_GROUP import PGL_PC6_PATIENT_VISIT_GROUP
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH


"""
Goal add - PGL_PC6
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PGL_PC6 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PGL_PC6
from utils.hl7.v2_5_1.segments import (
    PID, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    PGL_PC6_PATIENT_VISIT_GROUP, PGL_PC6_GOAL_GROUP
)

pgl_pc6 = PGL_PC6(  #  - This message is used to send goals from one application to another (e
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=None,  # PGL_PC6_PATIENT_VISIT_GROUP(...) 
    goal=pgl_pc6_goal_group,  # PGL_PC6_GOAL_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::PGL_PC6 TEMPLATE-----
"""


class PGL_PC6(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PGL_PC6"""
    _hl7_name = """Goal add"""
    _hl7_description = """This message is used to send goals from one application to another (e"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC6"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, PID, PGL_PC6_PATIENT_VISIT_GROUP, PGL_PC6_GOAL_GROUP)
    _c_name = ("MSH", "SFT", "PID", "PATIENT VISIT", "GOAL")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "patient_identification", "patient_visit", "goal",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient_identification: PID,  #  Required. PID.3
        goal: PGL_PC6_GOAL_GROUP
        | tuple[PGL_PC6_GOAL_GROUP, ...],  #  Required. (GOL.6, NTE.7, VAR.8, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_visit: PGL_PC6_PATIENT_VISIT_GROUP | None = None,  #  PV1.4, PV2.5
    ):
        """
         - `PGL_PC6 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PGL_PC6>`_
        This message is used to send goals from one application to another (e.g., a point of care system to a clinical repository).  Many of the segments associated with this event are optional.  This optionality allows systems in need of this information to set up transactions that fulfill their requirements.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 4, 5 | use: O | rpt: 1)
        :param goal: Goal segment group: [GOL, NTE|None, VAR|None, GOAL ROLE|None, PATHWAY|None, OBSERVATION|None, PROBLEM|None, ORDER|None] (id: GOAL | seq: 6, 7, 8, None, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.goal = goal

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

    @property  # get PGL_PC6_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> PGL_PC6_PATIENT_VISIT_GROUP | None:
        """
        id: PGL_PC6_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PGL_PC6_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC6_PATIENT_VISIT_GROUP
        """
        return self._c_data[3][0]

    @patient_visit.setter  # set PGL_PC6_PATIENT_VISIT_GROUP.None
    def patient_visit(self, patient_v_isit: PGL_PC6_PATIENT_VISIT_GROUP | None):
        """
        id: PGL_PC6_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PGL_PC6_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC6_PATIENT_VISIT_GROUP
        """
        self._c_data[3] = (patient_v_isit,)

    @property  # get GOAL
    def goal(self) -> tuple[PGL_PC6_GOAL_GROUP, ...]:
        """
        id: PGL_PC6_GOAL_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PGL_PC6_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC6_GOAL_GROUP
        """
        return self._c_data[4]

    @goal.setter  # set GOAL
    def goal(self, goal: PGL_PC6_GOAL_GROUP | tuple[PGL_PC6_GOAL_GROUP, ...]):
        """
        id: GOAL SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PGL_PC6_GOAL_GROUP.None | tuple[PGL_PC6_GOAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PGL_PC6_GOAL_GROUP
        """
        if isinstance(goal, tuple):
            self._c_data[4] = goal
        else:
            self._c_data[4] = (goal,)
