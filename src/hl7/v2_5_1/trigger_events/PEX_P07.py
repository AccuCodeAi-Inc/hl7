from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.PEX_P07_EXPERIENCE_GROUP import PEX_P07_EXPERIENCE_GROUP
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.EVN import EVN
from ..segment_groups.PEX_P07_VISIT_GROUP import PEX_P07_VISIT_GROUP


"""
Unsolicited initial individual product experience report - PEX_P07
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PEX_P07 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PEX_P07
from utils.hl7.v2_5_1.segments import (
    PID, MSH, PD1, SFT, NTE, EVN
)
from utils.hl7.v2_5_1.segment_groups import (
    PEX_P07_VISIT_GROUP, PEX_P07_EXPERIENCE_GROUP
)

pex_p07 = PEX_P07(  #  - The primary application of this message is to transfer information related to an adverse event occurring while a patient was exposed to a product
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    notes_and_comments=None,  # NTE(...) 
    visit=None,  # PEX_P07_VISIT_GROUP(...) 
    experience=pex_p07_experience_group,  # PEX_P07_EXPERIENCE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::PEX_P07 TEMPLATE-----
"""


class PEX_P07(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PEX_P07"""
    _hl7_name = """Unsolicited initial individual product experience report"""
    _hl7_description = """The primary application of this message is to transfer information related to an adverse event occurring while a patient was exposed to a product"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "None", "None")
    _c_components = (MSH, SFT, EVN, PID, PD1, NTE, PEX_P07_VISIT_GROUP, PEX_P07_EXPERIENCE_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "NTE", "VISIT", "EXPERIENCE")
    _c_is_group = (False, False, False, False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "notes_and_comments", "visit", "experience",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        experience: PEX_P07_EXPERIENCE_GROUP
        | tuple[PEX_P07_EXPERIENCE_GROUP, ...],  #  Required. (PES.9, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        visit: PEX_P07_VISIT_GROUP | None = None,  #  PV1.7, PV2.8
    ):
        """
         - `PEX_P07 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PEX_P07>`_
        The primary application of this message is to transfer information related to an adverse event occurring while a patient was exposed to a product

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 7, 8 | use: O | rpt: 1)
        :param experience: Experience segment group: [PES, PEX OBSERVATION] (id: EXPERIENCE | seq: 9, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.notes_and_comments = notes_and_comments
        self.visit = visit
        self.experience = experience

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

    @property  # get EVN.3
    def event_type(self) -> EVN:
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        return_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[2][0]

    @event_type.setter  # set EVN.3
    def event_type(self, evn: EVN):
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        param_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[2] = (evn,)

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[3][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[3] = (pid,)

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[4][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[4] = (pd1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[5]

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
            self._c_data[5] = nte
        else:
            self._c_data[5] = (nte,)

    @property  # get PEX_P07_VISIT_GROUP.None
    def visit(self) -> PEX_P07_VISIT_GROUP | None:
        """
        id: PEX_P07_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: PEX_P07_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_VISIT_GROUP
        """
        return self._c_data[6][0]

    @visit.setter  # set PEX_P07_VISIT_GROUP.None
    def visit(self, v_isit: PEX_P07_VISIT_GROUP | None):
        """
        id: PEX_P07_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: PEX_P07_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_VISIT_GROUP
        """
        self._c_data[6] = (v_isit,)

    @property  # get EXPERIENCE
    def experience(self) -> tuple[PEX_P07_EXPERIENCE_GROUP, ...]:
        """
        id: PEX_P07_EXPERIENCE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PEX_P07_EXPERIENCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP
        """
        return self._c_data[7]

    @experience.setter  # set EXPERIENCE
    def experience(
        self,
        experience: PEX_P07_EXPERIENCE_GROUP | tuple[PEX_P07_EXPERIENCE_GROUP, ...],
    ):
        """
        id: EXPERIENCE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PEX_P07_EXPERIENCE_GROUP.None | tuple[PEX_P07_EXPERIENCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PEX_P07_EXPERIENCE_GROUP
        """
        if isinstance(experience, tuple):
            self._c_data[7] = experience
        else:
            self._c_data[7] = (experience,)
