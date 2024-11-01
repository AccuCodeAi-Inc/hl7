from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BTX import BTX
from ..segments.NTE import NTE


"""
PRODUCT STATUS - BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP
from utils.hl7.v2_5_1.segments import (
    BTX, NTE
)

bts_o31_order_group_product_status_group = BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP(  # PRODUCT STATUS - Segment group for BTS_O31_ORDER_GROUP - ORDER consisting of BTX, NTE|None
    blood_product_transfusion_or_disposition=btx,  # BTX(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP TEMPLATE-----
"""


class BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP"""
    _hl7_name = """PRODUCT STATUS"""
    _hl7_description = """Segment group for BTS_O31_ORDER_GROUP - ORDER consisting of BTX, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (BTX, NTE)
    _c_name = ("BTX", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("blood_product_transfusion_or_disposition", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        blood_product_transfusion_or_disposition: BTX,  #  Required. BTX.14
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.15
    ):
        """
        None - `BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BTS_O31_ORDER_GROUP_PRODUCT_STATUS_GROUP>`_
        Segment group for BTS_O31_ORDER_GROUP - ORDER consisting of BTX, NTE|None

        :param blood_product_transfusion_or_disposition: Blood Product Transfusion/Disposition (id: BTX | seq: 14 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.blood_product_transfusion_or_disposition = (
            blood_product_transfusion_or_disposition
        )
        self.notes_and_comments = notes_and_comments

    @property  # get BTX.14
    def blood_product_transfusion_or_disposition(self) -> BTX:
        """
        id: BTX | use: R | rpt: 1 | seq: 14
        ---
        return_type: BTX.14: Blood Product Transfusion/Disposition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTX
        """
        return self._c_data[0][0]

    @blood_product_transfusion_or_disposition.setter  # set BTX.14
    def blood_product_transfusion_or_disposition(self, btx: BTX):
        """
        id: BTX | use: R | rpt: 1 | seq: 14
        ---
        param_type: BTX.14: Blood Product Transfusion/Disposition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BTX
        """
        self._c_data[0] = (btx,)

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
