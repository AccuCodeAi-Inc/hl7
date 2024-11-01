from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.OML_O21_PATIENT_GROUP import OML_O21_PATIENT_GROUP
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segment_groups.OML_O21_ORDER_GROUP import OML_O21_ORDER_GROUP


"""
Laboratory Order - OML_O21
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::OML_O21 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O21
from utils.hl7.v2_5_1.segments import (
    NTE, SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O21_ORDER_GROUP, OML_O21_PATIENT_GROUP
)

oml_o21 = OML_O21(  #  - The following message structure may be used for the communication of laboratory and other order messages and must be used for lab automation messages where it is required that the Specimen/Container information is within the ORC/OBR segment group
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # OML_O21_PATIENT_GROUP(...) 
    order=oml_o21_order_group,  # OML_O21_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::OML_O21 TEMPLATE-----
"""


class OML_O21(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """OML_O21"""
    _hl7_name = """Laboratory Order"""
    _hl7_description = """The following message structure may be used for the communication of laboratory and other order messages and must be used for lab automation messages where it is required that the Specimen/Container information is within the ORC/OBR segment group"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "None", "None")
    _c_components = (MSH, SFT, NTE, OML_O21_PATIENT_GROUP, OML_O21_ORDER_GROUP)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "ORDER")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order: OML_O21_ORDER_GROUP
        | tuple[
            OML_O21_ORDER_GROUP, ...
        ],  #  Required. (ORC.15, FT1.42, CTI.43, BLG.44, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.3
        patient: OML_O21_PATIENT_GROUP
        | None = None,  #  PID.4, PD1.5, NTE.6, NK1.7, GT1.13, AL1.14
    ):
        """
                 - `OML_O21 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21>`_
                The following message structure may be used for the communication of laboratory and other order messages and must be used for lab automation messages where it is required that the Specimen/Container information is within the ORC/OBR segment group.  While the ORM message with the OBR segment can be used for backwards compatibility for general lab messages, only the OML message should be used to take advantage of the specimen and container extensions required in laboratory automation.

        The trigger event for this message is any change to a laboratory order.  Such changes include submission of new orders, cancellations, updates, etc.  OML messages can originate also with a placer, filler, or an interested third party

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: *)
                :param patient: Patient segment group: [PID, PD1|None, NTE|None, NK1|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None] (id: PATIENT | seq: 4, 5, 6, 7, None, None, 13, 14 | use: O | rpt: 1)
                :param order: Order segment group: [ORC, TIIMING|None, OBSERVATION REQUEST|None, FT1|None, CTI|None, BLG|None] (id: ORDER | seq: 15, None, None, 42, 43, 44 | use: R | rpt: *)
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

    @property  # get OML_O21_PATIENT_GROUP.None
    def patient(self) -> OML_O21_PATIENT_GROUP | None:
        """
        id: OML_O21_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OML_O21_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set OML_O21_PATIENT_GROUP.None
    def patient(self, patient: OML_O21_PATIENT_GROUP | None):
        """
        id: OML_O21_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OML_O21_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[OML_O21_ORDER_GROUP, ...]:
        """
        id: OML_O21_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O21_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP
        """
        return self._c_data[4]

    @order.setter  # set ORDER
    def order(self, order: OML_O21_ORDER_GROUP | tuple[OML_O21_ORDER_GROUP, ...]):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O21_ORDER_GROUP.None | tuple[OML_O21_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O21_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[4] = order
        else:
            self._c_data[4] = (order,)
