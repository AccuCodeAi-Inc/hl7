from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BTX import BTX
from ..segment_groups.BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.ORC import ORC
from ..segments.BPO import BPO


"""
ORDER - BRT_O32_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BRT_O32_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BRT_O32_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    BTX, BPO, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

brt_o32_response_group_order_group = BRT_O32_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for BRT_O32_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, BPO|None, BTX|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    blood_product_order=None,  # BPO(...) 
    blood_product_transfusion_or_disposition=None,  # BTX(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BRT_O32_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class BRT_O32_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BRT_O32_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for BRT_O32_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, BPO|None, BTX|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BRT_O32_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("7", "None", "10", "11")
    _c_components = (ORC, BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, BPO, BTX)
    _c_name = ("ORC", "TIMING", "BPO", "BTX")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "timing", "blood_product_order", "blood_product_transfusion_or_disposition",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.7
        timing: BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.8, TQ2.9, ...)
        blood_product_order: BPO | None = None,  #  BPO.10
        blood_product_transfusion_or_disposition: BTX
        | tuple[BTX, ...]
        | None = None,  #  BTX.11
    ):
        """
        None - `BRT_O32_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BRT_O32_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for BRT_O32_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, BPO|None, BTX|None

        :param common_order: Common Order (id: ORC | seq: 7 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 8, 9 | use: O | rpt: *)
        :param blood_product_order: Blood product order (id: BPO | seq: 10 | use: O | rpt: 1)
        :param blood_product_transfusion_or_disposition: Blood Product Transfusion/Disposition (id: BTX | seq: 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.timing = timing
        self.blood_product_order = blood_product_order
        self.blood_product_transfusion_or_disposition = (
            blood_product_transfusion_or_disposition
        )

    @property  # get ORC.7
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 7
        ---
        return_type: ORC.7: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.7
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 7
        ---
        param_type: ORC.7: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BRT_O32_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get BPO.10
    def blood_product_order(self) -> BPO | None:
        """
        id: BPO | use: O | rpt: 1 | seq: 10
        ---
        return_type: BPO.10: Blood product order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO
        """
        return self._c_data[2][0]

    @blood_product_order.setter  # set BPO.10
    def blood_product_order(self, bpo: BPO | None):
        """
        id: BPO | use: O | rpt: 1 | seq: 10
        ---
        param_type: BPO.10: Blood product order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO
        """
        self._c_data[2] = (bpo,)

    @property  # get BTX
    def blood_product_transfusion_or_disposition(self) -> tuple[BTX, ...] | tuple[None]:
        """
        id: BTX SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[BTX, ...]: (Blood Product Transfusion/Disposition, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTX
        """
        return self._c_data[3]

    @blood_product_transfusion_or_disposition.setter  # set BTX
    def blood_product_transfusion_or_disposition(
        self, btx: BTX | tuple[BTX, ...] | None
    ):
        """
        id: BTX SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: BTX.11 | tuple[BTX, ...]: (Blood Product Transfusion/Disposition, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTX
        """
        if isinstance(btx, tuple):
            self._c_data[3] = btx
        else:
            self._c_data[3] = (btx,)
