from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.OMB_O27_ORDER_GROUP import OMB_O27_ORDER_GROUP
from ..segment_groups.OMB_O27_PATIENT_GROUP import OMB_O27_PATIENT_GROUP
from ..segments.NTE import NTE
from ..segments.SFT import SFT


"""
Blood Product Order - OMB_O27
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::OMB_O27 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMB_O27
from utils.hl7.v2_5_1.segments import (
    SFT, NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    OMB_O27_PATIENT_GROUP, OMB_O27_ORDER_GROUP
)

omb_o27 = OMB_O27(  #  - Blood product orders use the OMB message with the BPO segment for the detail segment and the acknowledgment message, ORB
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # OMB_O27_PATIENT_GROUP(...) 
    order=omb_o27_order_group,  # OMB_O27_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::OMB_O27 TEMPLATE-----
"""


class OMB_O27(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """OMB_O27"""
    _hl7_name = """Blood Product Order"""
    _hl7_description = """Blood product orders use the OMB message with the BPO segment for the detail segment and the acknowledgment message, ORB"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMB_O27"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, NTE, OMB_O27_PATIENT_GROUP, OMB_O27_ORDER_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "ORDER")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order: OMB_O27_ORDER_GROUP
        | tuple[
            OMB_O27_ORDER_GROUP, ...
        ],  #  Required. (ORC.14, BPO.17, SPM.18, NTE.19, DG1.20, FT1.23, BLG.24, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: OMB_O27_PATIENT_GROUP
        | None = None,  #  PID.4, PD1.5, NTE.6, GT1.12, AL1.13
    ):
        """
         - `OMB_O27 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMB_O27>`_
        Blood product orders use the OMB message with the BPO segment for the detail segment and the acknowledgment message, ORB.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None] (id: PATIENT | seq: 4, 5, 6, None, None, 12, 13 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, BPO, SPM|None, NTE|None, DG1|None, OBSERVATION|None, FT1|None, BLG|None] (id: ORDER | seq: 14, None, 17, 18, 19, 20, None, 23, 24 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.message_header = message_header
        self.software_segment = software_segment
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.order = order

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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        param_type: NTE.3 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get OMB_O27_PATIENT_GROUP.None
    def patient(self) -> OMB_O27_PATIENT_GROUP | None:
        """
        id: OMB_O27_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OMB_O27_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set OMB_O27_PATIENT_GROUP.None
    def patient(self, patient: OMB_O27_PATIENT_GROUP | None):
        """
        id: OMB_O27_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OMB_O27_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[OMB_O27_ORDER_GROUP, ...]:
        """
        id: OMB_O27_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OMB_O27_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_ORDER_GROUP
        """
        return self._c_data[4]

    @order.setter  # set ORDER
    def order(self, order: OMB_O27_ORDER_GROUP | tuple[OMB_O27_ORDER_GROUP, ...]):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OMB_O27_ORDER_GROUP.None | tuple[OMB_O27_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMB_O27_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[4] = order
        else:
            self._c_data[4] = (order,)
