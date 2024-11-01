from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segment_groups.RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP import (
    RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP,
)
from ..segments.NTE import NTE


"""
ORDER DETAIL SUPPLEMENT - RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, RXR
)
from utils.hl7.v2_5_1.segment_groups import (
    RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP
)

rgv_o15_order_group_order_detail_group_order_detail_supplement_group = RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP(  # ORDER DETAIL SUPPLEMENT - Segment group for RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of NTE, RXR, COMPONENTS|None
    notes_and_comments=nte,  # NTE(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    components=None,  # RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP TEMPLATE-----
"""


class RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP"""
    _hl7_name = """ORDER DETAIL SUPPLEMENT"""
    _hl7_description = """Segment group for RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of NTE, RXR, COMPONENTS|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (65535, 65535, 65535)
    _c_usage = ("R", "R", "O")
    _c_aliases = ("13", "14", "None")
    _c_components = (NTE, RXR, RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP)
    _c_name = ("NTE", "RXR", "COMPONENTS")
    _c_is_group = (False, False, True)
    _c_attrs = ("notes_and_comments", "pharmacy_or_treatment_route", "components",)
    # fmt: on

    def __init__(
        self,
        notes_and_comments: NTE | tuple[NTE, ...],  #  Required. NTE.13
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.14
        components: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP
        | tuple[
            RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP,
            ...,
        ]
        | None = None,  #  (RXC.15, NTE.16, ...)
    ):
        """
        None - `RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP>`_
        Segment group for RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP - ORDER DETAIL consisting of NTE, RXR, COMPONENTS|None

        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 14 | use: R | rpt: *)
        :param components: Components segment group: [RXC, NTE|None] (id: COMPONENTS | seq: 15, 16 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.components = components

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...]:
        """
        id: NTE SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[0]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...]):
        """
        id: NTE SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: NTE.13 | tuple[NTE, ...]: (Notes and Comments, ...)
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
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        param_type: RXR.14 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[1] = rxr
        else:
            self._c_data[1] = (rxr,)

    @property  # get COMPONENTS
    def components(
        self,
    ) -> (
        tuple[
            RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP
        """
        return self._c_data[2]

    @components.setter  # set COMPONENTS
    def components(
        self,
        components: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP
        | tuple[
            RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: COMPONENTS SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP.None | tuple[RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGV_O15_ORDER_GROUP_ORDER_DETAIL_GROUP_ORDER_DETAIL_SUPPLEMENT_GROUP_COMPONENTS_GROUP
        """
        if isinstance(components, tuple):
            self._c_data[2] = components
        else:
            self._c_data[2] = (components,)
