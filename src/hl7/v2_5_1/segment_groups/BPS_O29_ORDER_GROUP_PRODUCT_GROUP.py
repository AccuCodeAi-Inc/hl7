from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.BPX import BPX


"""
PRODUCT - BPS_O29_ORDER_GROUP_PRODUCT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BPS_O29_ORDER_GROUP_PRODUCT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BPS_O29_ORDER_GROUP_PRODUCT_GROUP
from utils.hl7.v2_5_1.segments import (
    BPX, NTE
)

bps_o29_order_group_product_group = BPS_O29_ORDER_GROUP_PRODUCT_GROUP(  # PRODUCT - Segment group for BPS_O29_ORDER_GROUP - ORDER consisting of BPX, NTE|None
    blood_product_dispense_status=bpx,  # BPX(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BPS_O29_ORDER_GROUP_PRODUCT_GROUP TEMPLATE-----
"""


class BPS_O29_ORDER_GROUP_PRODUCT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BPS_O29_ORDER_GROUP_PRODUCT_GROUP"""
    _hl7_name = """PRODUCT"""
    _hl7_description = """Segment group for BPS_O29_ORDER_GROUP - ORDER consisting of BPX, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BPS_O29_ORDER_GROUP_PRODUCT_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (BPX, NTE)
    _c_name = ("BPX", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("blood_product_dispense_status", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        blood_product_dispense_status: BPX,  #  Required. BPX.14
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.15
    ):
        """
        None - `BPS_O29_ORDER_GROUP_PRODUCT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BPS_O29_ORDER_GROUP_PRODUCT_GROUP>`_
        Segment group for BPS_O29_ORDER_GROUP - ORDER consisting of BPX, NTE|None

        :param blood_product_dispense_status: Blood product dispense status (id: BPX | seq: 14 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.blood_product_dispense_status = blood_product_dispense_status
        self.notes_and_comments = notes_and_comments

    @property  # get BPX.14
    def blood_product_dispense_status(self) -> BPX:
        """
        id: BPX | use: R | rpt: 1 | seq: 14
        ---
        return_type: BPX.14: Blood product dispense status
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPX
        """
        return self._c_data[0][0]

    @blood_product_dispense_status.setter  # set BPX.14
    def blood_product_dispense_status(self, bpx: BPX):
        """
        id: BPX | use: R | rpt: 1 | seq: 14
        ---
        param_type: BPX.14: Blood product dispense status
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BPX
        """
        self._c_data[0] = (bpx,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: NTE.15 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
