from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBR import OBR
from ..segments.ORC import ORC
from ..segments.NTE import NTE
from ..segment_groups.ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.IPC import IPC


"""
ORDER - ORI_O24_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORI_O24_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORI_O24_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    IPC, OBR, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

ori_o24_response_group_order_group = ORI_O24_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORI_O24_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, OBR, NTE|None, IPC
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    imaging_procedure_control_segment=ipc,  # IPC(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORI_O24_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORI_O24_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORI_O24_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORI_O24_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, OBR, NTE|None, IPC"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORI_O24_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "R")
    _c_aliases = ("8", "None", "11", "12", "13")
    _c_components = (ORC, ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, OBR, NTE, IPC)
    _c_name = ("ORC", "TIMING", "OBR", "NTE", "IPC")
    _c_is_group = (False, True, False, False, False)
    _c_attrs = ("common_order", "timing", "observation_request", "notes_and_comments", "imaging_procedure_control_segment",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        observation_request: OBR,  #  Required. OBR.11
        imaging_procedure_control_segment: IPC | tuple[IPC, ...],  #  Required. IPC.13
        timing: ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
    ):
        """
        None - `ORI_O24_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORI_O24_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for ORI_O24_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, OBR, NTE|None, IPC

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 9, 10 | use: O | rpt: *)
        :param observation_request: Observation Request (id: OBR | seq: 11 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        :param imaging_procedure_control_segment: Imaging Procedure Control Segment (id: IPC | seq: 13 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments
        self.imaging_procedure_control_segment = imaging_procedure_control_segment

    @property  # get ORC.8
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        return_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.8
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        param_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORI_O24_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OBR.11
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 11
        ---
        return_type: OBR.11: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.11
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 11
        ---
        param_type: OBR.11: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: NTE.12 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get IPC
    def imaging_procedure_control_segment(self) -> tuple[IPC, ...]:
        """
        id: IPC SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[IPC, ...]: (Imaging Procedure Control Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IPC
        """
        return self._c_data[4]

    @imaging_procedure_control_segment.setter  # set IPC
    def imaging_procedure_control_segment(self, ipc: IPC | tuple[IPC, ...]):
        """
        id: IPC SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: IPC.13 | tuple[IPC, ...]: (Imaging Procedure Control Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IPC
        """
        if isinstance(ipc, tuple):
            self._c_data[4] = ipc
        else:
            self._c_data[4] = (ipc,)
