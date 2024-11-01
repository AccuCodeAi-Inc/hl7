from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.OMD_O03_ORDER_DIET_GROUP import OMD_O03_ORDER_DIET_GROUP
from ..segment_groups.OMD_O03_ORDER_TRAY_GROUP import OMD_O03_ORDER_TRAY_GROUP
from ..segment_groups.OMD_O03_PATIENT_GROUP import OMD_O03_PATIENT_GROUP
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT


"""
Dietary Order - OMD_O03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::OMD_O03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMD_O03
from utils.hl7.v2_5_1.segments import (
    SFT, NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    OMD_O03_PATIENT_GROUP, OMD_O03_ORDER_DIET_GROUP, OMD_O03_ORDER_TRAY_GROUP
)

omd_o03 = OMD_O03(  #  - A diet office needs to receive specific information, the most important being the diet order itself
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # OMD_O03_PATIENT_GROUP(...) 
    order_diet=omd_o03_order_diet_group,  # OMD_O03_ORDER_DIET_GROUP(...)  # Required.
    order_tray=None,  # OMD_O03_ORDER_TRAY_GROUP(...) 
)

-----END TRIGGER_EVENT::OMD_O03 TEMPLATE-----
"""


class OMD_O03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """OMD_O03"""
    _hl7_name = """Dietary Order"""
    _hl7_description = """A diet office needs to receive specific information, the most important being the diet order itself"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "None", "None", "None")
    _c_components = (MSH, SFT, NTE, OMD_O03_PATIENT_GROUP, OMD_O03_ORDER_DIET_GROUP, OMD_O03_ORDER_TRAY_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "ORDER DIET", "ORDER TRAY")
    _c_is_group = (False, False, False, True, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "order_diet", "order_tray",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order_diet: OMD_O03_ORDER_DIET_GROUP
        | tuple[OMD_O03_ORDER_DIET_GROUP, ...],  #  Required. (ORC.14, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: OMD_O03_PATIENT_GROUP
        | None = None,  #  PID.4, PD1.5, NTE.6, GT1.12, AL1.13
        order_tray: OMD_O03_ORDER_TRAY_GROUP
        | tuple[OMD_O03_ORDER_TRAY_GROUP, ...]
        | None = None,  #  (ORC.21, ODT.24, NTE.25, ...)
    ):
        """
         - `OMD_O03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03>`_
        A diet office needs to receive specific information, the most important being the diet order itself.  Diet restrictions (often called diet codes) are the basic building blocks of a diet order.  The diet order segments may be sent as part of the ORM and ORR message structure to support backwards compatibility, or may be sent as part of the OMD and ORD dedicated message structures.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None] (id: PATIENT | seq: 4, 5, 6, None, None, 12, 13 | use: O | rpt: 1)
        :param order_diet: Order Diet segment group: [ORC, TIMING DIET|None, DIET|None] (id: ORDER DIET | seq: 14, None, None | use: R | rpt: *)
        :param order_tray: Order Tray segment group: [ORC, TIMING TRAY|None, ODT, NTE|None] (id: ORDER TRAY | seq: 21, None, 24, 25 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.order_diet = order_diet
        self.order_tray = order_tray

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

    @property  # get OMD_O03_PATIENT_GROUP.None
    def patient(self) -> OMD_O03_PATIENT_GROUP | None:
        """
        id: OMD_O03_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OMD_O03_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set OMD_O03_PATIENT_GROUP.None
    def patient(self, patient: OMD_O03_PATIENT_GROUP | None):
        """
        id: OMD_O03_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OMD_O03_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get ORDER DIET
    def order_diet(self) -> tuple[OMD_O03_ORDER_DIET_GROUP, ...]:
        """
        id: OMD_O03_ORDER_DIET_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OMD_O03_ORDER_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP
        """
        return self._c_data[4]

    @order_diet.setter  # set ORDER DIET
    def order_diet(
        self,
        order_diet: OMD_O03_ORDER_DIET_GROUP | tuple[OMD_O03_ORDER_DIET_GROUP, ...],
    ):
        """
        id: ORDER DIET SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OMD_O03_ORDER_DIET_GROUP.None | tuple[OMD_O03_ORDER_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP
        """
        if isinstance(order_diet, tuple):
            self._c_data[4] = order_diet
        else:
            self._c_data[4] = (order_diet,)

    @property  # get ORDER TRAY
    def order_tray(self) -> tuple[OMD_O03_ORDER_TRAY_GROUP, ...] | tuple[None]:
        """
        id: OMD_O03_ORDER_TRAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMD_O03_ORDER_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_TRAY_GROUP
        """
        return self._c_data[5]

    @order_tray.setter  # set ORDER TRAY
    def order_tray(
        self,
        order_tray: OMD_O03_ORDER_TRAY_GROUP
        | tuple[OMD_O03_ORDER_TRAY_GROUP, ...]
        | None,
    ):
        """
        id: ORDER TRAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMD_O03_ORDER_TRAY_GROUP.None | tuple[OMD_O03_ORDER_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_TRAY_GROUP
        """
        if isinstance(order_tray, tuple):
            self._c_data[5] = order_tray
        else:
            self._c_data[5] = (order_tray,)
