from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BPO import BPO
from ..segment_groups.BPS_O29_ORDER_GROUP_PRODUCT_GROUP import (
    BPS_O29_ORDER_GROUP_PRODUCT_GROUP,
)
from ..segment_groups.BPS_O29_ORDER_GROUP_TIMING_GROUP import (
    BPS_O29_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.ORC import ORC
from ..segments.NTE import NTE


"""
ORDER - BPS_O29_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BPS_O29_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BPS_O29_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, BPO, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    BPS_O29_ORDER_GROUP_TIMING_GROUP, BPS_O29_ORDER_GROUP_PRODUCT_GROUP
)

bps_o29_order_group = BPS_O29_ORDER_GROUP(  # ORDER - Segment group for BPS_O29 - Blood Product Dispense Status Message consisting of ORC, TIMING|None, BPO, NTE|None, PRODUCT|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # BPS_O29_ORDER_GROUP_TIMING_GROUP(...) 
    blood_product_order=bpo,  # BPO(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    product=None,  # BPS_O29_ORDER_GROUP_PRODUCT_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BPS_O29_ORDER_GROUP TEMPLATE-----
"""


class BPS_O29_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BPS_O29_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for BPS_O29 - Blood Product Dispense Status Message consisting of ORC, TIMING|None, BPO, NTE|None, PRODUCT|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BPS_O29_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "O")
    _c_aliases = ("9", "None", "12", "13", "None")
    _c_components = (ORC, BPS_O29_ORDER_GROUP_TIMING_GROUP, BPO, NTE, BPS_O29_ORDER_GROUP_PRODUCT_GROUP)
    _c_name = ("ORC", "TIMING", "BPO", "NTE", "PRODUCT")
    _c_is_group = (False, True, False, False, True)
    _c_attrs = ("common_order", "timing", "blood_product_order", "notes_and_comments", "product",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.9
        blood_product_order: BPO,  #  Required. BPO.12
        timing: BPS_O29_ORDER_GROUP_TIMING_GROUP
        | tuple[BPS_O29_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.10, TQ2.11, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
        product: BPS_O29_ORDER_GROUP_PRODUCT_GROUP
        | tuple[BPS_O29_ORDER_GROUP_PRODUCT_GROUP, ...]
        | None = None,  #  (BPX.14, NTE.15, ...)
    ):
        """
        None - `BPS_O29_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BPS_O29_ORDER_GROUP>`_
        Segment group for BPS_O29 - Blood Product Dispense Status Message consisting of ORC, TIMING|None, BPO, NTE|None, PRODUCT|None

        :param common_order: Common Order (id: ORC | seq: 9 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 10, 11 | use: O | rpt: *)
        :param blood_product_order: Blood product order (id: BPO | seq: 12 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        :param product: Product segment group: [BPX, NTE|None] (id: PRODUCT | seq: 14, 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.blood_product_order = blood_product_order
        self.notes_and_comments = notes_and_comments
        self.product = product

    @property  # get ORC.9
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 9
        ---
        return_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.9
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 9
        ---
        param_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(self) -> tuple[BPS_O29_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: BPS_O29_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BPS_O29_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPS_O29_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: BPS_O29_ORDER_GROUP_TIMING_GROUP
        | tuple[BPS_O29_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BPS_O29_ORDER_GROUP_TIMING_GROUP.None | tuple[BPS_O29_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPS_O29_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get BPO.12
    def blood_product_order(self) -> BPO:
        """
        id: BPO | use: R | rpt: 1 | seq: 12
        ---
        return_type: BPO.12: Blood product order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO
        """
        return self._c_data[2][0]

    @blood_product_order.setter  # set BPO.12
    def blood_product_order(self, bpo: BPO):
        """
        id: BPO | use: R | rpt: 1 | seq: 12
        ---
        param_type: BPO.12: Blood product order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPO
        """
        self._c_data[2] = (bpo,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: NTE.13 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get PRODUCT
    def product(self) -> tuple[BPS_O29_ORDER_GROUP_PRODUCT_GROUP, ...] | tuple[None]:
        """
        id: BPS_O29_ORDER_GROUP_PRODUCT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BPS_O29_ORDER_GROUP_PRODUCT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPS_O29_ORDER_GROUP_PRODUCT_GROUP
        """
        return self._c_data[4]

    @product.setter  # set PRODUCT
    def product(
        self,
        product: BPS_O29_ORDER_GROUP_PRODUCT_GROUP
        | tuple[BPS_O29_ORDER_GROUP_PRODUCT_GROUP, ...]
        | None,
    ):
        """
        id: PRODUCT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BPS_O29_ORDER_GROUP_PRODUCT_GROUP.None | tuple[BPS_O29_ORDER_GROUP_PRODUCT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPS_O29_ORDER_GROUP_PRODUCT_GROUP
        """
        if isinstance(product, tuple):
            self._c_data[4] = product
        else:
            self._c_data[4] = (product,)
