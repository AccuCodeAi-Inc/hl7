from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RER_RER_DEFINITION_GROUP_ORDER_GROUP import (
    RER_RER_DEFINITION_GROUP_ORDER_GROUP,
)
from ..segments.QRD import QRD
from ..segment_groups.RER_RER_DEFINITION_GROUP_PATIENT_GROUP import (
    RER_RER_DEFINITION_GROUP_PATIENT_GROUP,
)
from ..segments.QRF import QRF


"""
DEFINITION - RER_RER_DEFINITION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RER_RER_DEFINITION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RER_RER_DEFINITION_GROUP
from utils.hl7.v2_5_1.segments import (
    QRF, QRD
)
from utils.hl7.v2_5_1.segment_groups import (
    RER_RER_DEFINITION_GROUP_PATIENT_GROUP, RER_RER_DEFINITION_GROUP_ORDER_GROUP
)

rer_rer_definition_group = RER_RER_DEFINITION_GROUP(  # DEFINITION - Segment group for RER_RER - Pharmacy/Treatment Encoded Order Information Response consisting of QRD, QRF|None, PATIENT|None, ORDER
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    patient=None,  # RER_RER_DEFINITION_GROUP_PATIENT_GROUP(...) 
    order=rer_rer_definition_group_order_group,  # RER_RER_DEFINITION_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RER_RER_DEFINITION_GROUP TEMPLATE-----
"""


class RER_RER_DEFINITION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RER_RER_DEFINITION_GROUP"""
    _hl7_name = """DEFINITION"""
    _hl7_description = """Segment group for RER_RER - Pharmacy/Treatment Encoded Order Information Response consisting of QRD, QRF|None, PATIENT|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RER_RER_DEFINITION_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 65535)
    _c_usage = ("R", "O", "O", "R")
    _c_aliases = ("5", "6", "None", "None")
    _c_components = (QRD, QRF, RER_RER_DEFINITION_GROUP_PATIENT_GROUP, RER_RER_DEFINITION_GROUP_ORDER_GROUP)
    _c_name = ("QRD", "QRF", "PATIENT", "ORDER")
    _c_is_group = (False, False, True, True)
    _c_attrs = ("original_style_query_definition", "original_style_query_filter", "patient", "order",)
    # fmt: on

    def __init__(
        self,
        original_style_query_definition: QRD,  #  Required. QRD.5
        order: RER_RER_DEFINITION_GROUP_ORDER_GROUP
        | tuple[
            RER_RER_DEFINITION_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.9, RXE.10, RXR.11, RXC.12, ...)
        original_style_query_filter: QRF | None = None,  #  QRF.6
        patient: RER_RER_DEFINITION_GROUP_PATIENT_GROUP | None = None,  #  PID.7, NTE.8
    ):
        """
        None - `RER_RER_DEFINITION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RER_RER_DEFINITION_GROUP>`_
        Segment group for RER_RER - Pharmacy/Treatment Encoded Order Information Response consisting of QRD, QRF|None, PATIENT|None, ORDER

        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 5 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 6 | use: O | rpt: 1)
        :param patient: Patient segment group: [PID, NTE|None] (id: PATIENT | seq: 7, 8 | use: O | rpt: 1)
        :param order: Order segment group: [ORC, RXE, RXR, RXC|None] (id: ORDER | seq: 9, 10, 11, 12 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.patient = patient
        self.order = order

    @property  # get QRD.5
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 5
        ---
        return_type: QRD.5: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[0][0]

    @original_style_query_definition.setter  # set QRD.5
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 5
        ---
        param_type: QRD.5: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[0] = (qrd,)

    @property  # get QRF.6
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 6
        ---
        return_type: QRF.6: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[1][0]

    @original_style_query_filter.setter  # set QRF.6
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 6
        ---
        param_type: QRF.6: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[1] = (qrf,)

    @property  # get RER_RER_DEFINITION_GROUP_PATIENT_GROUP.None
    def patient(self) -> RER_RER_DEFINITION_GROUP_PATIENT_GROUP | None:
        """
        id: RER_RER_DEFINITION_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RER_RER_DEFINITION_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RER_RER_DEFINITION_GROUP_PATIENT_GROUP
        """
        return self._c_data[2][0]

    @patient.setter  # set RER_RER_DEFINITION_GROUP_PATIENT_GROUP.None
    def patient(self, patient: RER_RER_DEFINITION_GROUP_PATIENT_GROUP | None):
        """
        id: RER_RER_DEFINITION_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RER_RER_DEFINITION_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RER_RER_DEFINITION_GROUP_PATIENT_GROUP
        """
        self._c_data[2] = (patient,)

    @property  # get ORDER
    def order(self) -> tuple[RER_RER_DEFINITION_GROUP_ORDER_GROUP, ...]:
        """
        id: RER_RER_DEFINITION_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RER_RER_DEFINITION_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RER_RER_DEFINITION_GROUP_ORDER_GROUP
        """
        return self._c_data[3]

    @order.setter  # set ORDER
    def order(
        self,
        order: RER_RER_DEFINITION_GROUP_ORDER_GROUP
        | tuple[RER_RER_DEFINITION_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RER_RER_DEFINITION_GROUP_ORDER_GROUP.None | tuple[RER_RER_DEFINITION_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RER_RER_DEFINITION_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[3] = order
        else:
            self._c_data[3] = (order,)
