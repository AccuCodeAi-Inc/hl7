from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.RGV_O15_ORDER_GROUP import RGV_O15_ORDER_GROUP
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segment_groups.RGV_O15_PATIENT_GROUP import RGV_O15_PATIENT_GROUP


"""
Pharmacy/Treatment Give - RGV_O15
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RGV_O15 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RGV_O15
from utils.hl7.v2_5_1.segments import (
    NTE, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    RGV_O15_PATIENT_GROUP, RGV_O15_ORDER_GROUP
)

rgv_o15 = RGV_O15(  #  - The RDS message's RXD segment carries the dispense data for a given issuance of medication: thus it may describe a single dose, a half-day dose, a daily dose, a refill of a prescription, etc
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # RGV_O15_PATIENT_GROUP(...) 
    order=rgv_o15_order_group,  # RGV_O15_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::RGV_O15 TEMPLATE-----
"""


class RGV_O15(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RGV_O15"""
    _hl7_name = """Pharmacy/Treatment Give"""
    _hl7_description = """The RDS message's RXD segment carries the dispense data for a given issuance of medication: thus it may describe a single dose, a half-day dose, a daily dose, a refill of a prescription, etc"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, NTE, RGV_O15_PATIENT_GROUP, RGV_O15_ORDER_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "ORDER")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order: RGV_O15_ORDER_GROUP
        | tuple[RGV_O15_ORDER_GROUP, ...],  #  Required. (ORC.9, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: RGV_O15_PATIENT_GROUP | None = None,  #  PID.4, NTE.5, AL1.6
    ):
        """
                 - `RGV_O15 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15>`_
                The RDS message's RXD segment carries the dispense data for a given issuance of medication: thus it may describe a single dose, a half-day dose, a daily dose, a refill of a prescription, etc.  It does not contain the given instructions or scheduling information.  When this "give" (i.e., administration) information needs to be transmitted from the pharmacy or treatment application to another application, it is done with the RGV message.

        The RGV message uses the RXG segment to record drug or treatment administration instructions.  It may carry information about a single scheduled administration on a drug or treatment, or it may carry information about multiple administrations.  If the pharmacy or treatment application (or some other application) needs to create a nonambiguous MAR report where each administration is matched to a particular give date/time instruction, it may use the RGV message as described in the following way:

        For each scheduled administration of the medication, the pharmacy/treatment issues either a single RGV message or a single RGV message with multiple RXG segments, one for each scheduled administration.  The actual administrations (transmitted by one or more RAS messages) are matched against the scheduled ones by recording in each RXA segment the Give Sub-ID of the corresponding RXG segment.  If more than one administration needs to be matched (as in the case of recording a change or rate of an IV solution) the administering application issues additional RXA segment(s) (corresponding to the same RXG segment).  If no matching is needed, the Give Sub-ID of the RXA segments has the value zero (0).

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
                :param patient: Patient segment group: [PID, NTE|None, AL1|None, PATIENT VISIT|None] (id: PATIENT | seq: 4, 5, 6, None | use: O | rpt: 1)
                :param order: Order segment group: [ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, GIVE] (id: ORDER | seq: 9, None, None, None, None | use: R | rpt: *)
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

    @property  # get RGV_O15_PATIENT_GROUP.None
    def patient(self) -> RGV_O15_PATIENT_GROUP | None:
        """
        id: RGV_O15_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RGV_O15_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set RGV_O15_PATIENT_GROUP.None
    def patient(self, patient: RGV_O15_PATIENT_GROUP | None):
        """
        id: RGV_O15_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RGV_O15_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[RGV_O15_ORDER_GROUP, ...]:
        """
        id: RGV_O15_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RGV_O15_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP
        """
        return self._c_data[4]

    @order.setter  # set ORDER
    def order(self, order: RGV_O15_ORDER_GROUP | tuple[RGV_O15_ORDER_GROUP, ...]):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP.None | tuple[RGV_O15_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[4] = order
        else:
            self._c_data[4] = (order,)
