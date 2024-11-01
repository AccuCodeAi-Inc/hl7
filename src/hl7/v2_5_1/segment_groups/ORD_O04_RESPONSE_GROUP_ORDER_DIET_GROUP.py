from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP import (
    ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP,
)
from ..segments.ODS import ODS
from ..segments.NTE import NTE
from ..segments.ORC import ORC


"""
ORDER DIET - ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, ODS, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP
)

ord_o04_response_group_order_diet_group = ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP(  # ORDER DIET - Segment group for ORD_O04_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING DIET|None, ODS|None, NTE|None
    common_order=orc,  # ORC(...)  # Required.
    timing_diet=None,  # ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP(...) 
    dietary_orders_supplements_and_preferences=None,  # ODS(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP TEMPLATE-----
"""


class ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP"""
    _hl7_name = """ORDER DIET"""
    _hl7_description = """Segment group for ORD_O04_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING DIET|None, ODS|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("8", "None", "11", "12")
    _c_components = (ORC, ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ODS, NTE)
    _c_name = ("ORC", "TIMING DIET", "ODS", "NTE")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "timing_diet", "dietary_orders_supplements_and_preferences", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.8
        timing_diet: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]
        | None = None,  #  (TQ1.9, TQ2.10, ...)
        dietary_orders_supplements_and_preferences: ODS
        | tuple[ODS, ...]
        | None = None,  #  ODS.11
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
    ):
        """
        None - `ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP>`_
        Segment group for ORD_O04_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING DIET|None, ODS|None, NTE|None

        :param common_order: Common Order (id: ORC | seq: 8 | use: R | rpt: 1)
        :param timing_diet: Timing Diet segment group: [TQ1, TQ2|None] (id: TIMING DIET | seq: 9, 10 | use: O | rpt: *)
        :param dietary_orders_supplements_and_preferences: Dietary Orders, Supplements, and Preferences (id: ODS | seq: 11 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.timing_diet = timing_diet
        self.dietary_orders_supplements_and_preferences = (
            dietary_orders_supplements_and_preferences
        )
        self.notes_and_comments = notes_and_comments

    @property  # get ORC.8
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        return_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.8
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 8
        ---
        param_type: ORC.8: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING DIET
    def timing_diet(
        self,
    ) -> (
        tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]
        | tuple[None]
    ):
        """
        id: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        """
        return self._c_data[1]

    @timing_diet.setter  # set TIMING DIET
    def timing_diet(
        self,
        timing_diet: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]
        | None,
    ):
        """
        id: TIMING DIET SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP.None | tuple[ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        """
        if isinstance(timing_diet, tuple):
            self._c_data[1] = timing_diet
        else:
            self._c_data[1] = (timing_diet,)

    @property  # get ODS
    def dietary_orders_supplements_and_preferences(
        self,
    ) -> tuple[ODS, ...] | tuple[None]:
        """
        id: ODS SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[ODS, ...]: (Dietary Orders, Supplements, and Preferences, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS
        """
        return self._c_data[2]

    @dietary_orders_supplements_and_preferences.setter  # set ODS
    def dietary_orders_supplements_and_preferences(
        self, ods: ODS | tuple[ODS, ...] | None
    ):
        """
        id: ODS SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: ODS.11 | tuple[ODS, ...]: (Dietary Orders, Supplements, and Preferences, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODS
        """
        if isinstance(ods, tuple):
            self._c_data[2] = ods
        else:
            self._c_data[2] = (ods,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

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
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)
