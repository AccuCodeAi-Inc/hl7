from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.BLG import BLG
from ..segments.FT1 import FT1
from ..segments.CTI import CTI
from ..segment_groups.ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - ORM_O01_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORM_O01_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORM_O01_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    BLG, ORC, CTI, FT1
)
from utils.hl7.v2_5_1.segment_groups import (
    ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP
)

orm_o01_order_group = ORM_O01_ORDER_GROUP(  # ORDER - Segment group for ORM_O01 - General Order consisting of ORC, ORDER DETAIL|None, FT1|None, CTI|None, BLG|None
    common_order=orc,  # ORC(...)  # Required.
    order_detail=None,  # ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    financial_transaction=None,  # FT1(...) 
    clinical_trial_identification=None,  # CTI(...) 
    billing=None,  # BLG(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORM_O01_ORDER_GROUP TEMPLATE-----
"""


class ORM_O01_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORM_O01_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORM_O01 - General Order consisting of ORC, ORDER DETAIL|None, FT1|None, CTI|None, BLG|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORM_O01_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("13", "None", "25", "26", "27")
    _c_components = (ORC, ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP, FT1, CTI, BLG)
    _c_name = ("ORC", "ORDER DETAIL", "FT1", "CTI", "BLG")
    _c_is_group = (False, True, False, False, False)
    _c_attrs = ("common_order", "order_detail", "financial_transaction", "clinical_trial_identification", "billing",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.13
        order_detail: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP
        | None = None,  #  NTE.20, CTD.21, DG1.22
        financial_transaction: FT1 | tuple[FT1, ...] | None = None,  #  FT1.25
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.26
        billing: BLG | None = None,  #  BLG.27
    ):
        """
        None - `ORM_O01_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORM_O01_ORDER_GROUP>`_
        Segment group for ORM_O01 - General Order consisting of ORC, ORDER DETAIL|None, FT1|None, CTI|None, BLG|None

        :param common_order: Common Order (id: ORC | seq: 13 | use: R | rpt: 1)
        :param order_detail: Order Detail segment group: [ORDER DETAIL SEGMENT, NTE|None, CTD|None, DG1|None, OBSERVATION|None] (id: ORDER DETAIL | seq: None, 20, 21, 22, None | use: O | rpt: 1)
        :param financial_transaction: Financial Transaction (id: FT1 | seq: 25 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 26 | use: O | rpt: *)
        :param billing: Billing (id: BLG | seq: 27 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.order_detail = order_detail
        self.financial_transaction = financial_transaction
        self.clinical_trial_identification = clinical_trial_identification
        self.billing = billing

    @property  # get ORC.13
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 13
        ---
        return_type: ORC.13: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.13
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 13
        ---
        param_type: ORC.13: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self) -> ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[1][0]

    @order_detail.setter  # set ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self, order_detail: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP | None):
        """
        id: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORM_O01_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[1] = (order_detail,)

    @property  # get FT1
    def financial_transaction(self) -> tuple[FT1, ...] | tuple[None]:
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        return_type: tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        return self._c_data[2]

    @financial_transaction.setter  # set FT1
    def financial_transaction(self, ft1: FT1 | tuple[FT1, ...] | None):
        """
        id: FT1 SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        param_type: FT1.25 | tuple[FT1, ...]: (Financial Transaction, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/FT1
        """
        if isinstance(ft1, tuple):
            self._c_data[2] = ft1
        else:
            self._c_data[2] = (ft1,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 26
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[3]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 26
        ---
        param_type: CTI.26 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[3] = cti
        else:
            self._c_data[3] = (cti,)

    @property  # get BLG.27
    def billing(self) -> BLG | None:
        """
        id: BLG | use: O | rpt: 1 | seq: 27
        ---
        return_type: BLG.27: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        return self._c_data[4][0]

    @billing.setter  # set BLG.27
    def billing(self, blg: BLG | None):
        """
        id: BLG | use: O | rpt: 1 | seq: 27
        ---
        param_type: BLG.27: Billing
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLG
        """
        self._c_data[4] = (blg,)
