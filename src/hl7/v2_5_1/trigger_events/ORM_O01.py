from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.ORM_O01_PATIENT_GROUP import ORM_O01_PATIENT_GROUP
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segment_groups.ORM_O01_ORDER_GROUP import ORM_O01_ORDER_GROUP


"""
General Order - ORM_O01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ORM_O01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORM_O01
from utils.hl7.v2_5_1.segments import (
    NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    ORM_O01_ORDER_GROUP, ORM_O01_PATIENT_GROUP
)

orm_o01 = ORM_O01(  #  - Left for backward compatibility only
    message_header=msh,  # MSH(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # ORM_O01_PATIENT_GROUP(...) 
    order=orm_o01_order_group,  # ORM_O01_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::ORM_O01 TEMPLATE-----
"""


class ORM_O01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ORM_O01"""
    _hl7_name = """General Order"""
    _hl7_description = """Left for backward compatibility only"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORM_O01"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "R")
    _c_aliases = ("1", "2", "None", "None")
    _c_components = (MSH, NTE, ORM_O01_PATIENT_GROUP, ORM_O01_ORDER_GROUP)
    _c_name = ("MSH", "NTE", "PATIENT", "ORDER")
    _c_is_group = (False, False, True, True)
    _c_attrs = ("message_header", "notes_and_comments", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        order: ORM_O01_ORDER_GROUP
        | tuple[
            ORM_O01_ORDER_GROUP, ...
        ],  #  Required. (ORC.13, FT1.25, CTI.26, BLG.27, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.2
        patient: ORM_O01_PATIENT_GROUP
        | None = None,  #  PID.3, PD1.4, NTE.5, GT1.11, AL1.12
    ):
        """
                 - `ORM_O01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORM_O01>`_
                Left for backward compatibility only.  It is recommended that the trigger events OMG, OML, OMD, OMS, OMN, OMI, and OMP be used instead when communicating orders and order related events.

        The function of this message is to initiate the transmission of information about an order.  This includes placing new orders, cancellation of existing orders, discontinuation, holding, etc.  ORM messages can originate also with a placer, filler, or an interested third part

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param notes_and_comments: Notes and Comments (id: NTE | seq: 2 | use: O | rpt: *)
                :param patient: Patient segment group: [PID, PD1|None, NTE|None, PATIENT VISIT|None, INSURANCE|None, GT1|None, AL1|None] (id: PATIENT | seq: 3, 4, 5, None, None, 11, 12 | use: O | rpt: 1)
                :param order: Order segment group: [ORC, ORDER DETAIL|None, FT1|None, CTI|None, BLG|None] (id: ORDER | seq: 13, None, 25, 26, 27 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: NTE.2 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get ORM_O01_PATIENT_GROUP.None
    def patient(self) -> ORM_O01_PATIENT_GROUP | None:
        """
        id: ORM_O01_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORM_O01_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_PATIENT_GROUP
        """
        return self._c_data[2][0]

    @patient.setter  # set ORM_O01_PATIENT_GROUP.None
    def patient(self, patient: ORM_O01_PATIENT_GROUP | None):
        """
        id: ORM_O01_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORM_O01_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_PATIENT_GROUP
        """
        self._c_data[2] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[ORM_O01_ORDER_GROUP, ...]:
        """
        id: ORM_O01_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORM_O01_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP
        """
        return self._c_data[3]

    @order.setter  # set ORDER
    def order(self, order: ORM_O01_ORDER_GROUP | tuple[ORM_O01_ORDER_GROUP, ...]):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORM_O01_ORDER_GROUP.None | tuple[ORM_O01_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[3] = order
        else:
            self._c_data[3] = (order,)
