from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OMI_O23_ORDER_GROUP_OBSERVATION_GROUP import (
    OMI_O23_ORDER_GROUP_OBSERVATION_GROUP,
)
from ..segments.CTD import CTD
from ..segments.IPC import IPC
from ..segments.ORC import ORC
from ..segments.NTE import NTE
from ..segment_groups.OMI_O23_ORDER_GROUP_TIMING_GROUP import (
    OMI_O23_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.DG1 import DG1
from ..segments.OBR import OBR


"""
ORDER - OMI_O23_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMI_O23_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMI_O23_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTD, OBR, IPC, DG1, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    OMI_O23_ORDER_GROUP_TIMING_GROUP, OMI_O23_ORDER_GROUP_OBSERVATION_GROUP
)

omi_o23_order_group = OMI_O23_ORDER_GROUP(  # ORDER - Segment group for OMI_O23 - Imaging Order consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, DG1|None, OBSERVATION|None, IPC
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # OMI_O23_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    contact_data=None,  # CTD(...) 
    diagnosis=None,  # DG1(...) 
    observation=None,  # OMI_O23_ORDER_GROUP_OBSERVATION_GROUP(...) 
    imaging_procedure_control_segment=ipc,  # IPC(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMI_O23_ORDER_GROUP TEMPLATE-----
"""


class OMI_O23_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMI_O23_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OMI_O23 - Imaging Order consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, DG1|None, OBSERVATION|None, IPC"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMI_O23_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "R")
    _c_aliases = ("14", "None", "17", "18", "19", "20", "None", "23")
    _c_components = (ORC, OMI_O23_ORDER_GROUP_TIMING_GROUP, OBR, NTE, CTD, DG1, OMI_O23_ORDER_GROUP_OBSERVATION_GROUP, IPC)
    _c_name = ("ORC", "TIMING", "OBR", "NTE", "CTD", "DG1", "OBSERVATION", "IPC")
    _c_is_group = (False, True, False, False, False, False, True, False)
    _c_attrs = ("common_order", "timing", "observation_request", "notes_and_comments", "contact_data", "diagnosis", "observation", "imaging_procedure_control_segment",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        observation_request: OBR,  #  Required. OBR.17
        imaging_procedure_control_segment: IPC | tuple[IPC, ...],  #  Required. IPC.23
        timing: OMI_O23_ORDER_GROUP_TIMING_GROUP
        | tuple[OMI_O23_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.18
        contact_data: CTD | None = None,  #  CTD.19
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.20
        observation: OMI_O23_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMI_O23_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.21, NTE.22, ...)
    ):
        """
        None - `OMI_O23_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMI_O23_ORDER_GROUP>`_
        Segment group for OMI_O23 - Imaging Order consisting of ORC, TIMING|None, OBR, NTE|None, CTD|None, DG1|None, OBSERVATION|None, IPC

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 15, 16 | use: O | rpt: *)
        :param observation_request: Observation Request (id: OBR | seq: 17 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 18 | use: O | rpt: *)
        :param contact_data: Contact Data (id: CTD | seq: 19 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 20 | use: O | rpt: *)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 21, 22 | use: O | rpt: *)
        :param imaging_procedure_control_segment: Imaging Procedure Control Segment (id: IPC | seq: 23 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.contact_data = contact_data
        self.diagnosis = diagnosis
        self.observation = observation
        self.imaging_procedure_control_segment = imaging_procedure_control_segment

    @property  # get ORC.14
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        return_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.14
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        param_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[OMI_O23_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: OMI_O23_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMI_O23_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMI_O23_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: OMI_O23_ORDER_GROUP_TIMING_GROUP
        | tuple[OMI_O23_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMI_O23_ORDER_GROUP_TIMING_GROUP.None | tuple[OMI_O23_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMI_O23_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OBR.17
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 17
        ---
        return_type: OBR.17: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.17
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 17
        ---
        param_type: OBR.17: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: NTE.18 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get CTD.19
    def contact_data(self) -> CTD | None:
        """
        id: CTD | use: O | rpt: 1 | seq: 19
        ---
        return_type: CTD.19: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        return self._c_data[4][0]

    @contact_data.setter  # set CTD.19
    def contact_data(self, ctd: CTD | None):
        """
        id: CTD | use: O | rpt: 1 | seq: 19
        ---
        param_type: CTD.19: Contact Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTD
        """
        self._c_data[4] = (ctd,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[5]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: DG1.20 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[5] = dg1
        else:
            self._c_data[5] = (dg1,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[OMI_O23_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: OMI_O23_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMI_O23_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMI_O23_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[6]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: OMI_O23_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[OMI_O23_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMI_O23_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[OMI_O23_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMI_O23_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[6] = observation
        else:
            self._c_data[6] = (observation,)

    @property  # get IPC
    def imaging_procedure_control_segment(self) -> tuple[IPC, ...]:
        """
        id: IPC SEGMENT GROUP | use: R | rpt: * | seq: 23
        ---
        return_type: tuple[IPC, ...]: (Imaging Procedure Control Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IPC
        """
        return self._c_data[7]

    @imaging_procedure_control_segment.setter  # set IPC
    def imaging_procedure_control_segment(self, ipc: IPC | tuple[IPC, ...]):
        """
        id: IPC SEGMENT GROUP | use: R | rpt: * | seq: 23
        ---
        param_type: IPC.23 | tuple[IPC, ...]: (Imaging Procedure Control Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IPC
        """
        if isinstance(ipc, tuple):
            self._c_data[7] = ipc
        else:
            self._c_data[7] = (ipc,)
