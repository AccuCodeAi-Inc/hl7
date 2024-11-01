from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.RXR import RXR
from ..segment_groups.ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP import (
    ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP,
)
from ..segments.RXO import RXO


"""
ORDER DETAIL - ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, RXR, RXO
)
from utils.hl7.v2_5_1.segment_groups import (
    ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
)

orp_o10_response_group_order_group_order_detail_group = ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for ORP_O10_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXO, NTE|None, RXR, COMPONENT|None
    pharmacy_or_treatment_order=rxo,  # RXO(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    component=None,  # ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for ORP_O10_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXO, NTE|None, RXR, COMPONENT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("11", "12", "13", "None")
    _c_components = (RXO, NTE, RXR, ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP)
    _c_name = ("RXO", "NTE", "RXR", "COMPONENT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("pharmacy_or_treatment_order", "notes_and_comments", "pharmacy_or_treatment_route", "component",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_order: RXO,  #  Required. RXO.11
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.13
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
        component: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        | tuple[
            ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...
        ]
        | None = None,  #  (RXC.14, NTE.15, ...)
    ):
        """
        None - `ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for ORP_O10_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXO, NTE|None, RXR, COMPONENT|None

        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 11 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 13 | use: R | rpt: *)
        :param component: Component segment group: [RXC, NTE|None] (id: COMPONENT | seq: 14, 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.component = component

    @property  # get RXO.11
    def pharmacy_or_treatment_order(self) -> RXO:
        """
        id: RXO | use: R | rpt: 1 | seq: 11
        ---
        return_type: RXO.11: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_order.setter  # set RXO.11
    def pharmacy_or_treatment_order(self, rxo: RXO):
        """
        id: RXO | use: R | rpt: 1 | seq: 11
        ---
        param_type: RXO.11: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[0] = (rxo,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

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
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: RXR.13 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)

    @property  # get COMPONENT
    def component(
        self,
    ) -> (
        tuple[
            ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...
        ]
        | tuple[None]
    ):
        """
        id: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        """
        return self._c_data[3]

    @component.setter  # set COMPONENT
    def component(
        self,
        component: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        | tuple[
            ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...
        ]
        | None,
    ):
        """
        id: COMPONENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP.None | tuple[ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORP_O10_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        """
        if isinstance(component, tuple):
            self._c_data[3] = component
        else:
            self._c_data[3] = (component,)
