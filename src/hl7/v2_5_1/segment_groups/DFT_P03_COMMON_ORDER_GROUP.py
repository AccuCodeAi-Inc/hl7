from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP import (
    DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP,
)
from ..segment_groups.DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP import (
    DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP import (
    DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP,
)


"""
COMMON ORDER - DFT_P03_COMMON_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DFT_P03_COMMON_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P03_COMMON_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP, DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP, DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP
)

dft_p03_common_order_group = DFT_P03_COMMON_ORDER_GROUP(  # COMMON ORDER - Segment group for DFT_P03 - Post Detail Financial Transactions consisting of ORC|None, TIMING QUANTITY|None, ORDER|None, OBSERVATION|None
    common_order=None,  # ORC(...) 
    timing_quantity=None,  # DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP(...) 
    order=None,  # DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP(...) 
    observation=None,  # DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DFT_P03_COMMON_ORDER_GROUP TEMPLATE-----
"""


class DFT_P03_COMMON_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DFT_P03_COMMON_ORDER_GROUP"""
    _hl7_name = """COMMON ORDER"""
    _hl7_description = """Segment group for DFT_P03 - Post Detail Financial Transactions consisting of ORC|None, TIMING QUANTITY|None, ORDER|None, OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03_COMMON_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("O", "O", "O", "O")
    _c_aliases = ("11", "None", "None", "None")
    _c_components = (ORC, DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP, DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP, DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP)
    _c_name = ("ORC", "TIMING QUANTITY", "ORDER", "OBSERVATION")
    _c_is_group = (False, True, True, True)
    _c_attrs = ("common_order", "timing_quantity", "order", "observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC | None = None,  #  ORC.11
        timing_quantity: DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP
        | tuple[DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP, ...]
        | None = None,  #  (TQ1.12, TQ2.13, ...)
        order: DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP | None = None,  #  OBR.14, NTE.15
        observation: DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBX.16, NTE.17, ...)
    ):
        """
        None - `DFT_P03_COMMON_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03_COMMON_ORDER_GROUP>`_
        Segment group for DFT_P03 - Post Detail Financial Transactions consisting of ORC|None, TIMING QUANTITY|None, ORDER|None, OBSERVATION|None

        :param common_order: Common Order (id: ORC | seq: 11 | use: O | rpt: 1)
        :param timing_quantity: Timing Quantity segment group: [TQ1, TQ2|None] (id: TIMING QUANTITY | seq: 12, 13 | use: O | rpt: *)
        :param order: Order segment group: [OBR, NTE|None] (id: ORDER | seq: 14, 15 | use: O | rpt: 1)
        :param observation: Observation segment group: [OBX, NTE|None] (id: OBSERVATION | seq: 16, 17 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.timing_quantity = timing_quantity
        self.order = order
        self.observation = observation

    @property  # get ORC.11
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 11
        ---
        return_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.11
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 11
        ---
        param_type: ORC.11: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING QUANTITY
    def timing_quantity(
        self,
    ) -> tuple[DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP, ...] | tuple[None]:
        """
        id: DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP
        """
        return self._c_data[1]

    @timing_quantity.setter  # set TIMING QUANTITY
    def timing_quantity(
        self,
        timing_quantity: DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP
        | tuple[DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING QUANTITY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP.None | tuple[DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP_TIMING_QUANTITY_GROUP
        """
        if isinstance(timing_quantity, tuple):
            self._c_data[1] = timing_quantity
        else:
            self._c_data[1] = (timing_quantity,)

    @property  # get DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP.None
    def order(self) -> DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP | None:
        """
        id: DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP
        """
        return self._c_data[2][0]

    @order.setter  # set DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP.None
    def order(self, order: DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP | None):
        """
        id: DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP_ORDER_GROUP
        """
        self._c_data[2] = (order,)

    @property  # get OBSERVATION
    def observation(
        self,
    ) -> tuple[DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        """
        return self._c_data[3]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        | tuple[DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP.None | tuple[DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[3] = observation
        else:
            self._c_data[3] = (observation,)
