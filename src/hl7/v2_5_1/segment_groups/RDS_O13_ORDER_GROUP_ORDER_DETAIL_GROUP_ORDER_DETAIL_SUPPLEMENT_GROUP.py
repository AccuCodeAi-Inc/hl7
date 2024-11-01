from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.RXR import RXR
from ..segment_groups.RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP import (
    RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP,
)


"""
ORDER DETAIL SUPPLEMENT - RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
)

rds_o13_order_group_order_detail_group_order_detail_supplement_group = RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP(  # ORDER DETAIL SUPPLEMENT - Segment group for RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of NTE, RXR, COMPONENT|None
    notes_and_comments=nte,  # NTE(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    component=None,  # RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP TEMPLATE-----
"""


class RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP"""
    _hl7_name = """ORDER DETAIL SUPPLEMENT"""
    _hl7_description = """Segment group for RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of NTE, RXR, COMPONENT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (65535, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("14", "15", "None")
    _c_components = (NTE, RXR, RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP)
    _c_name = ("NTE", "RXR", "COMPONENT")
    _c_is_group = (False, False, True)
    _c_attrs = ("notes_and_comments", "pharmacy_or_treatment_route", "component",)
    # fmt: on

    def __init__(
        self,
        notes_and_comments: NTE | tuple[NTE, ...],  #  Required. NTE.14
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.15
        component: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
        | tuple[
            RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP,
            ...,
        ]
        | None = None,  #  (RXC.16, NTE.17, ...)
    ):
        """
        None - `RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP>`_
        Segment group for RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of NTE, RXR, COMPONENT|None

        :param notes_and_comments: Notes and Comments (id: NTE | seq: 14 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 15 | use: R | rpt: *)
        :param component: Component segment group: [RXC, NTE|None] (id: COMPONENT | seq: 16, 17 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.component = component

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...]:
        """
        id: NTE SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[0]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...]):
        """
        id: NTE SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        param_type: NTE.14 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[0] = nte
        else:
            self._c_data[0] = (nte,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 15
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 15
        ---
        param_type: RXR.15 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[1] = rxr
        else:
            self._c_data[1] = (rxr,)

    @property  # get COMPONENT
    def component(
        self,
    ) -> (
        tuple[
            RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
        """
        return self._c_data[2]

    @component.setter  # set COMPONENT
    def component(
        self,
        component: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
        | tuple[
            RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: COMPONENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP.None | tuple[RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDS_O13_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENT_GROUP
        """
        if isinstance(component, tuple):
            self._c_data[2] = component
        else:
            self._c_data[2] = (component,)
