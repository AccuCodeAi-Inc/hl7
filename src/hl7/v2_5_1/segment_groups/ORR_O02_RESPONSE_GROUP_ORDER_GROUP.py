from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segment_groups.ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP import (
    ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - ORR_O02_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORR_O02_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORR_O02_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTI, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
)

orr_o02_response_group_order_group = ORR_O02_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for ORR_O02_RESPONSE_GROUP - RESPONSE consisting of ORC, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None
    common_order=orc,  # ORC(...)  # Required.
    order_detail_segment=None,  # ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORR_O02_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class ORR_O02_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORR_O02_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for ORR_O02_RESPONSE_GROUP - RESPONSE consisting of ORC, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORR_O02_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("7", "None", "14", "15")
    _c_components = (ORC, ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP, NTE, CTI)
    _c_name = ("ORC", "ORDER DETAIL SEGMENT", "NTE", "CTI")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "order_detail_segment", "notes_and_comments", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.7
        order_detail_segment: ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        | None = None,  #  OBR.8, RQD.9, RQ1.10, RXO.11, ODS.12, ODT.13
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.14
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.15
    ):
        """
        None - `ORR_O02_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORR_O02_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for ORR_O02_RESPONSE_GROUP - RESPONSE consisting of ORC, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None

        :param common_order: Common Order (id: ORC | seq: 7 | use: R | rpt: 1)
        :param order_detail_segment: Order Detail Segment segment group: [OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None] (id: ORDER DETAIL SEGMENT | seq: 8, 9, 10, 11, 12, 13 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 14 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.order_detail_segment = order_detail_segment
        self.notes_and_comments = notes_and_comments
        self.clinical_trial_identification = clinical_trial_identification

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

    @property  # get ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
    ) -> ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP | None:
        """
        id: ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        return self._c_data[1][0]

    @order_detail_segment.setter  # set ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
        order_detail_segment: ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        | None,
    ):
        """
        id: ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORR_O02_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        self._c_data[1] = (order_detail_segment,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: NTE.14 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[3]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: CTI.15 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[3] = cti
        else:
            self._c_data[3] = (cti,)
