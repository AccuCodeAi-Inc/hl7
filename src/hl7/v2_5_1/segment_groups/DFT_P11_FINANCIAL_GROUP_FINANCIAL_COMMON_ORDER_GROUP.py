from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP,
)
from ..segment_groups.DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP,
)
from ..segments.ORC import ORC
from ..segment_groups.DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP,
)


"""
FINANCIAL COMMON ORDER - DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP
)

dft_p11_financial_group_financial_common_order_group = DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP(  # FINANCIAL COMMON ORDER - Segment group for DFT_P11_FINANCIAL_GROUP - FINANCIAL consisting of ORC|None, FINANCIAL TIMING QUANTITY|None, FINANCIAL ORDER|None, FINANCIAL OBSERVATION|None
    common_order=None,  # ORC(...) 
    financial_timing_quantity=None,  # DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP(...) 
    financial_order=None,  # DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP(...) 
    financial_observation=None,  # DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP TEMPLATE-----
"""


class DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP"""
    _hl7_name = """FINANCIAL COMMON ORDER"""
    _hl7_description = """Segment group for DFT_P11_FINANCIAL_GROUP - FINANCIAL consisting of ORC|None, FINANCIAL TIMING QUANTITY|None, FINANCIAL ORDER|None, FINANCIAL OBSERVATION|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("O", "O", "O", "O")
    _c_aliases = ("29", "None", "None", "None")
    _c_components = (ORC, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP, DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP)
    _c_name = ("ORC", "FINANCIAL TIMING QUANTITY", "FINANCIAL ORDER", "FINANCIAL OBSERVATION")
    _c_is_group = (False, True, True, True)
    _c_attrs = ("common_order", "financial_timing_quantity", "financial_order", "financial_observation",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC | None = None,  #  ORC.29
        financial_timing_quantity: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP
        | tuple[
            DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP,
            ...,
        ]
        | None = None,  #  (TQ1.30, TQ2.31, ...)
        financial_order: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP
        | None = None,  #  OBR.32, NTE.33
        financial_observation: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP
        | tuple[
            DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP,
            ...,
        ]
        | None = None,  #  (OBX.34, NTE.35, ...)
    ):
        """
        None - `DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP>`_
        Segment group for DFT_P11_FINANCIAL_GROUP - FINANCIAL consisting of ORC|None, FINANCIAL TIMING QUANTITY|None, FINANCIAL ORDER|None, FINANCIAL OBSERVATION|None

        :param common_order: Common Order (id: ORC | seq: 29 | use: O | rpt: 1)
        :param financial_timing_quantity: Financial Timing Quantity segment group: [TQ1, TQ2|None] (id: FINANCIAL TIMING QUANTITY | seq: 30, 31 | use: O | rpt: *)
        :param financial_order: Financial Order segment group: [OBR, NTE|None] (id: FINANCIAL ORDER | seq: 32, 33 | use: O | rpt: 1)
        :param financial_observation: Financial Observation segment group: [OBX, NTE|None] (id: FINANCIAL OBSERVATION | seq: 34, 35 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.financial_timing_quantity = financial_timing_quantity
        self.financial_order = financial_order
        self.financial_observation = financial_observation

    @property  # get ORC.29
    def common_order(self) -> ORC | None:
        """
        id: ORC | use: O | rpt: 1 | seq: 29
        ---
        return_type: ORC.29: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.29
    def common_order(self, orc: ORC | None):
        """
        id: ORC | use: O | rpt: 1 | seq: 29
        ---
        param_type: ORC.29: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get FINANCIAL TIMING QUANTITY
    def financial_timing_quantity(
        self,
    ) -> (
        tuple[
            DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP
        """
        return self._c_data[1]

    @financial_timing_quantity.setter  # set FINANCIAL TIMING QUANTITY
    def financial_timing_quantity(
        self,
        financial_timing_quantity: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP
        | tuple[
            DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: FINANCIAL TIMING QUANTITY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP.None | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_TIMING_QUANTITY_GROUP
        """
        if isinstance(financial_timing_quantity, tuple):
            self._c_data[1] = financial_timing_quantity
        else:
            self._c_data[1] = (financial_timing_quantity,)

    @property  # get DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP.None
    def financial_order(
        self,
    ) -> (
        DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP
        | None
    ):
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP
        """
        return self._c_data[2][0]

    @financial_order.setter  # set DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP.None
    def financial_order(
        self,
        financial_order: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP
        | None,
    ):
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_ORDER_GROUP
        """
        self._c_data[2] = (financial_order,)

    @property  # get FINANCIAL OBSERVATION
    def financial_observation(
        self,
    ) -> (
        tuple[
            DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP
        """
        return self._c_data[3]

    @financial_observation.setter  # set FINANCIAL OBSERVATION
    def financial_observation(
        self,
        financial_observation: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP
        | tuple[
            DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: FINANCIAL OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP.None | tuple[DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P11_FINANCIAL_GROUP_FINANCIAL_COMMON_ORDER_GROUP_FINANCIAL_OBSERVATION_GROUP
        """
        if isinstance(financial_observation, tuple):
            self._c_data[3] = financial_observation
        else:
            self._c_data[3] = (financial_observation,)
