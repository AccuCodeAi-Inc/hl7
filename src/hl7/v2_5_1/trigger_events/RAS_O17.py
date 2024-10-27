from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segment_groups.RAS_O17_PATIENT_GROUP import RAS_O17_PATIENT_GROUP
from ..segments.NTE import NTE
from ..segment_groups.RAS_O17_ORDER_GROUP import RAS_O17_ORDER_GROUP
from ..segments.MSH import MSH


"""
Pharmacy/Treatment Administration - RAS_O17
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RAS_O17 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RAS_O17
from utils.hl7.v2_5_1.segments import (
    SFT, NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    RAS_O17_PATIENT_GROUP, RAS_O17_ORDER_GROUP
)

ras_o17 = RAS_O17(  #  - The RAS message may be created by the administering application (e
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # RAS_O17_PATIENT_GROUP(...) 
    order=ras_o17_order_group,  # RAS_O17_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::RAS_O17 TEMPLATE-----
"""


class RAS_O17(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RAS_O17"""
    _hl7_name = """Pharmacy/Treatment Administration"""
    _hl7_description = """The RAS message may be created by the administering application (e"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, NTE, RAS_O17_PATIENT_GROUP, RAS_O17_ORDER_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "ORDER")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order: RAS_O17_ORDER_GROUP
        | tuple[RAS_O17_ORDER_GROUP, ...],  #  Required. (ORC.10, CTI.27, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: RAS_O17_PATIENT_GROUP | None = None,  #  PID.4, PD1.5, NTE.6, AL1.7
    ):
        """
         - `RAS_O17 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17>`_
        The RAS message may be created by the administering application (e.g., nursing application) for each instance of administration for an existing order.  If the administering application wants to report several administrations of medication/treatment for a given order with a single RAS message, each instance is reported by a separate (repeating) RXA segment.  In addition, the administration records for a group of orders may be sent in a single message by creating repeating groups of segments at the ORC level.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PD1|None, NTE|None, AL1|None, PATIENT VISIT|None] (id: PATIENT | seq: 4, 5, 6, 7, None | use: O | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, ADMINISTRATION, CTI|None] (id: ORDER | seq: 10, None, None, None, None, 27 | use: R | rpt: *)
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

    @property  # get RAS_O17_PATIENT_GROUP.None
    def patient(self) -> RAS_O17_PATIENT_GROUP | None:
        """
        id: RAS_O17_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RAS_O17_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set RAS_O17_PATIENT_GROUP.None
    def patient(self, patient: RAS_O17_PATIENT_GROUP | None):
        """
        id: RAS_O17_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RAS_O17_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[RAS_O17_ORDER_GROUP, ...]:
        """
        id: RAS_O17_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RAS_O17_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP
        """
        return self._c_data[4]

    @order.setter  # set ORDER
    def order(self, order: RAS_O17_ORDER_GROUP | tuple[RAS_O17_ORDER_GROUP, ...]):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP.None | tuple[RAS_O17_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[4] = order
        else:
            self._c_data[4] = (order,)
