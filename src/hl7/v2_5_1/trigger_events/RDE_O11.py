from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.NTE import NTE
from ..segment_groups.RDE_O11_ORDER_GROUP import RDE_O11_ORDER_GROUP
from ..segment_groups.RDE_O11_PATIENT_GROUP import RDE_O11_PATIENT_GROUP
from ..segments.MSH import MSH


"""
Pharmacy/Treatment Encoded Order - RDE_O11
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RDE_O11 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDE_O11
from utils.hl7.v2_5_1.segments import (
    SFT, NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    RDE_O11_PATIENT_GROUP, RDE_O11_ORDER_GROUP
)

rde_o11 = RDE_O11(  #  - This message communicates the pharmacy or treatment application's encoding of the pharmacy/treatment order (ORM message with RXO segment, see above)
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # RDE_O11_PATIENT_GROUP(...) 
    order=rde_o11_order_group,  # RDE_O11_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::RDE_O11 TEMPLATE-----
"""


class RDE_O11(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RDE_O11"""
    _hl7_name = """Pharmacy/Treatment Encoded Order"""
    _hl7_description = """This message communicates the pharmacy or treatment application's encoding of the pharmacy/treatment order (ORM message with RXO segment, see above)"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O11"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, NTE, RDE_O11_PATIENT_GROUP, RDE_O11_ORDER_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "ORDER")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order: RDE_O11_ORDER_GROUP
        | tuple[
            RDE_O11_ORDER_GROUP, ...
        ],  #  Required. (ORC.14, RXE.22, NTE.23, RXR.26, RXC.27, FT1.30, BLG.31, CTI.32, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: RDE_O11_PATIENT_GROUP
        | None = None,  #  PID.4, PD1.5, NTE.6, GT1.12, AL1.13
    ):
        """
         - `RDE_O11 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O11>`_
        This message communicates the pharmacy or treatment application's encoding of the pharmacy/treatment order (ORM message with RXO segment, see above).  It may be sent as an unsolicited message to report on either a single order or multiple pharmacy/treatment orders for a patient.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None] (id: PATIENT | seq: 4, 5, 6, None, None, 12, 13 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, ORDER DETAIL|None, RXE, NTE|None, TIMING ENCODED, RXR, RXC|None, OBSERVATION|None, FT1|None, BLG|None, CTI|None] (id: ORDER | seq: 14, None, None, 22, 23, None, 26, 27, None, 30, 31, 32 | use: R | rpt: *)
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

    @property  # get RDE_O11_PATIENT_GROUP.None
    def patient(self) -> RDE_O11_PATIENT_GROUP | None:
        """
        id: RDE_O11_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RDE_O11_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set RDE_O11_PATIENT_GROUP.None
    def patient(self, patient: RDE_O11_PATIENT_GROUP | None):
        """
        id: RDE_O11_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RDE_O11_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[RDE_O11_ORDER_GROUP, ...]:
        """
        id: RDE_O11_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RDE_O11_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP
        """
        return self._c_data[4]

    @order.setter  # set ORDER
    def order(self, order: RDE_O11_ORDER_GROUP | tuple[RDE_O11_ORDER_GROUP, ...]):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RDE_O11_ORDER_GROUP.None | tuple[RDE_O11_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[4] = order
        else:
            self._c_data[4] = (order,)
