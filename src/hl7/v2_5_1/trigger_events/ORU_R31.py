from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.ORU_R31_VISIT_GROUP import ORU_R31_VISIT_GROUP
from ..segments.PD1 import PD1
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segment_groups.ORU_R31_TIMING_QTY_GROUP import ORU_R31_TIMING_QTY_GROUP
from ..segments.MSH import MSH
from ..segment_groups.ORU_R31_OBSERVATION_GROUP import ORU_R31_OBSERVATION_GROUP
from ..segments.ORC import ORC


"""
Unsolicited New Point-Of-Care Observation Message - Search For An Order - ORU_R31
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ORU_R31 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORU_R31
from utils.hl7.v2_5_1.segments import (
    NTE, SFT, OBR, PID, ORC, MSH, PD1
)
from utils.hl7.v2_5_1.segment_groups import (
    ORU_R31_TIMING_QTY_GROUP, ORU_R31_VISIT_GROUP, ORU_R31_OBSERVATION_GROUP
)

oru_r31 = ORU_R31(  #  - This event trigger instructs the receiving system to search for an existing order for the observation(s) contained in the message
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    visit=None,  # ORU_R31_VISIT_GROUP(...) 
    common_order=orc,  # ORC(...)  # Required.
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    timing_qty=None,  # ORU_R31_TIMING_QTY_GROUP(...) 
    observation=oru_r31_observation_group,  # ORU_R31_OBSERVATION_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::ORU_R31 TEMPLATE-----
"""


class ORU_R31(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ORU_R31"""
    _hl7_name = """Unsolicited New Point-Of-Care Observation Message - Search For An Order"""
    _hl7_description = """This event trigger instructs the receiving system to search for an existing order for the observation(s) contained in the message"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_R31"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "R", "R", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "None", "7", "8", "9", "None", "None")
    _c_components = (MSH, SFT, PID, PD1, ORU_R31_VISIT_GROUP, ORC, OBR, NTE, ORU_R31_TIMING_QTY_GROUP, ORU_R31_OBSERVATION_GROUP)
    _c_name = ("MSH", "SFT", "PID", "PD1", "VISIT", "ORC", "OBR", "NTE", "TIMING QTY", "OBSERVATION")
    _c_is_group = (False, False, False, False, True, False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "patient_identification", "patient_additional_demographic", "visit", "common_order", "observation_request", "notes_and_comments", "timing_qty", "observation",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient_identification: PID,  #  Required. PID.3
        common_order: ORC,  #  Required. ORC.7
        observation_request: OBR,  #  Required. OBR.8
        observation: ORU_R31_OBSERVATION_GROUP
        | tuple[ORU_R31_OBSERVATION_GROUP, ...],  #  Required. (OBX.12, NTE.13, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.4
        visit: ORU_R31_VISIT_GROUP | None = None,  #  PV1.5, PV2.6
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.9
        timing_qty: ORU_R31_TIMING_QTY_GROUP
        | tuple[ORU_R31_TIMING_QTY_GROUP, ...]
        | None = None,  #  (TQ1.10, TQ2.11, ...)
    ):
        """
         - `ORU_R31 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORU_R31>`_
        This event trigger instructs the receiving system to search for an existing order for the observation(s) contained in the message.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 4 | use: O | rpt: 1)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 5, 6 | use: O | rpt: 1)
        :param common_order: Common Order (id: ORC | seq: 7 | use: R | rpt: 1)
        :param observation_request: Observation Request (id: OBR | seq: 8 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 9 | use: O | rpt: *)
        :param timing_qty: Timing Qty segment group: [TQ1, TQ2|None] (id: TIMING QTY | seq: 10, 11 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 12, 13 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.message_header = message_header
        self.software_segment = software_segment
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.visit = visit
        self.common_order = common_order
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.timing_qty = timing_qty
        self.observation = observation

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

    @property  # get PD1.4
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 4
        ---
        return_type: PD1.4: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[3][0]

    @patient_additional_demographic.setter  # set PD1.4
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 4
        ---
        param_type: PD1.4: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[3] = (pd1,)

    @property  # get ORU_R31_VISIT_GROUP.None
    def visit(self) -> ORU_R31_VISIT_GROUP | None:
        """
        id: ORU_R31_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORU_R31_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R31_VISIT_GROUP
        """
        return self._c_data[4][0]

    @visit.setter  # set ORU_R31_VISIT_GROUP.None
    def visit(self, v_isit: ORU_R31_VISIT_GROUP | None):
        """
        id: ORU_R31_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORU_R31_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R31_VISIT_GROUP
        """
        self._c_data[4] = (v_isit,)

    @property  # get ORC.7
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 7
        ---
        return_type: ORC.7: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[5][0]

    @common_order.setter  # set ORC.7
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 7
        ---
        param_type: ORC.7: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[5] = (orc,)

    @property  # get OBR.8
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 8
        ---
        return_type: OBR.8: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[6][0]

    @observation_request.setter  # set OBR.8
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 8
        ---
        param_type: OBR.8: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[6] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[7]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: NTE.9 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[7] = nte
        else:
            self._c_data[7] = (nte,)

    @property  # get TIMING QTY
    def timing_qty(self) -> tuple[ORU_R31_TIMING_QTY_GROUP, ...] | tuple[None]:
        """
        id: ORU_R31_TIMING_QTY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORU_R31_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R31_TIMING_QTY_GROUP
        """
        return self._c_data[8]

    @timing_qty.setter  # set TIMING QTY
    def timing_qty(
        self,
        timing_qty: ORU_R31_TIMING_QTY_GROUP
        | tuple[ORU_R31_TIMING_QTY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING QTY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORU_R31_TIMING_QTY_GROUP.None | tuple[ORU_R31_TIMING_QTY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R31_TIMING_QTY_GROUP
        """
        if isinstance(timing_qty, tuple):
            self._c_data[8] = timing_qty
        else:
            self._c_data[8] = (timing_qty,)

    @property  # get OBSERVATION
    def observation(self) -> tuple[ORU_R31_OBSERVATION_GROUP, ...]:
        """
        id: ORU_R31_OBSERVATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORU_R31_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R31_OBSERVATION_GROUP
        """
        return self._c_data[9]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: ORU_R31_OBSERVATION_GROUP | tuple[ORU_R31_OBSERVATION_GROUP, ...],
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORU_R31_OBSERVATION_GROUP.None | tuple[ORU_R31_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORU_R31_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[9] = observation
        else:
            self._c_data[9] = (observation,)
