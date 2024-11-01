from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXO import RXO
from ..segments.NTE import NTE
from ..segment_groups.RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP import (
    RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP,
)


"""
ORDER DETAIL - RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP
from utils.hl7.v2_5_1.segments import (
    RXO, NTE, RXR
)
from utils.hl7.v2_5_1.segment_groups import (
    RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
)

rde_o11_order_group_order_detail_group = RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP(  # ORDER DETAIL - Segment group for RDE_O11_ORDER_GROUP - ORDER consisting of RXO, NTE|None, RXR, COMPONENT|None
    pharmacy_or_treatment_order=rxo,  # RXO(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    component=None,  # RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP TEMPLATE-----
"""


class RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _hl7_name = """ORDER DETAIL"""
    _hl7_description = """Segment group for RDE_O11_ORDER_GROUP - ORDER consisting of RXO, NTE|None, RXR, COMPONENT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("17", "18", "19", "None")
    _c_components = (RXO, NTE, RXR, RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP)
    _c_name = ("RXO", "NTE", "RXR", "COMPONENT")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("pharmacy_or_treatment_order", "notes_and_comments", "pharmacy_or_treatment_route", "component",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_order: RXO,  #  Required. RXO.17
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.19
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.18
        component: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        | tuple[RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...]
        | None = None,  #  (RXC.20, NTE.21, ...)
    ):
        """
        None - `RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP>`_
        Segment group for RDE_O11_ORDER_GROUP - ORDER consisting of RXO, NTE|None, RXR, COMPONENT|None

        :param pharmacy_or_treatment_order: Pharmacy/Treatment Order (id: RXO | seq: 17 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 18 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 19 | use: R | rpt: *)
        :param component: Component segment group: [RXC, NTE|None] (id: COMPONENT | seq: 20, 21 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pharmacy_or_treatment_order = pharmacy_or_treatment_order
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.component = component

    @property  # get RXO.17
    def pharmacy_or_treatment_order(self) -> RXO:
        """
        id: RXO | use: R | rpt: 1 | seq: 17
        ---
        return_type: RXO.17: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_order.setter  # set RXO.17
    def pharmacy_or_treatment_order(self, rxo: RXO):
        """
        id: RXO | use: R | rpt: 1 | seq: 17
        ---
        param_type: RXO.17: Pharmacy/Treatment Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXO
        """
        self._c_data[0] = (rxo,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: NTE.18 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 19
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 19
        ---
        param_type: RXR.19 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
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
        tuple[RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...] | tuple[None]
    ):
        """
        id: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        """
        return self._c_data[3]

    @component.setter  # set COMPONENT
    def component(
        self,
        component: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        | tuple[RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...]
        | None,
    ):
        """
        id: COMPONENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP.None | tuple[RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDE_O11_ORDER_GROUP_ORDER_DETAIL_GROUP_COMPONENT_GROUP
        """
        if isinstance(component, tuple):
            self._c_data[3] = component
        else:
            self._c_data[3] = (component,)
