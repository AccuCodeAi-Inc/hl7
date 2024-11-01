from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP import (
    OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.OMD_O03_ORDER_DIET_GROUP_DIET_GROUP import (
    OMD_O03_ORDER_DIET_GROUP_DIET_GROUP,
)


"""
ORDER DIET - OMD_O03_ORDER_DIET_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMD_O03_ORDER_DIET_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMD_O03_ORDER_DIET_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, OMD_O03_ORDER_DIET_GROUP_DIET_GROUP
)

omd_o03_order_diet_group = OMD_O03_ORDER_DIET_GROUP(  # ORDER DIET - Segment group for OMD_O03 - Dietary Order consisting of ORC, TIMING DIET|None, DIET|None
    common_order=orc,  # ORC(...)  # Required.
    timing_diet=None,  # OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP(...) 
    diet=None,  # OMD_O03_ORDER_DIET_GROUP_DIET_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMD_O03_ORDER_DIET_GROUP TEMPLATE-----
"""


class OMD_O03_ORDER_DIET_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMD_O03_ORDER_DIET_GROUP"""
    _hl7_name = """ORDER DIET"""
    _hl7_description = """Segment group for OMD_O03 - Dietary Order consisting of ORC, TIMING DIET|None, DIET|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03_ORDER_DIET_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 1)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("14", "None", "None")
    _c_components = (ORC, OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, OMD_O03_ORDER_DIET_GROUP_DIET_GROUP)
    _c_name = ("ORC", "TIMING DIET", "DIET")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "timing_diet", "diet",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.14
        timing_diet: OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        | tuple[OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]
        | None = None,  #  (TQ1.15, TQ2.16, ...)
        diet: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP | None = None,  #  ODS.17, NTE.18
    ):
        """
        None - `OMD_O03_ORDER_DIET_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03_ORDER_DIET_GROUP>`_
        Segment group for OMD_O03 - Dietary Order consisting of ORC, TIMING DIET|None, DIET|None

        :param common_order: Common Order (id: ORC | seq: 14 | use: R | rpt: 1)
        :param timing_diet: Timing Diet segment group: [TQ1, TQ2|None] (id: TIMING DIET | seq: 15, 16 | use: O | rpt: *)
        :param diet: Diet segment group: [ODS, NTE|None, OBSERVATION|None] (id: DIET | seq: 17, 18, None | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.timing_diet = timing_diet
        self.diet = diet

    @property  # get ORC.14
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        return_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.14
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 14
        ---
        param_type: ORC.14: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING DIET
    def timing_diet(
        self,
    ) -> tuple[OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...] | tuple[None]:
        """
        id: OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        """
        return self._c_data[1]

    @timing_diet.setter  # set TIMING DIET
    def timing_diet(
        self,
        timing_diet: OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        | tuple[OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]
        | None,
    ):
        """
        id: TIMING DIET SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP.None | tuple[OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP_TIMING_DIET_GROUP
        """
        if isinstance(timing_diet, tuple):
            self._c_data[1] = timing_diet
        else:
            self._c_data[1] = (timing_diet,)

    @property  # get OMD_O03_ORDER_DIET_GROUP_DIET_GROUP.None
    def diet(self) -> OMD_O03_ORDER_DIET_GROUP_DIET_GROUP | None:
        """
        id: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP_DIET_GROUP
        """
        return self._c_data[2][0]

    @diet.setter  # set OMD_O03_ORDER_DIET_GROUP_DIET_GROUP.None
    def diet(self, diet: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP | None):
        """
        id: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OMD_O03_ORDER_DIET_GROUP_DIET_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_DIET_GROUP_DIET_GROUP
        """
        self._c_data[2] = (diet,)
