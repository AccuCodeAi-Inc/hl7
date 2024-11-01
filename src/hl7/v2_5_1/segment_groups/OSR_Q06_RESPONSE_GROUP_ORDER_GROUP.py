from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segment_groups.OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP import (
    OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP,
)
from ..segment_groups.OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP import (
    OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.NTE import NTE


"""
ORDER - OSR_Q06_RESPONSE_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OSR_Q06_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OSR_Q06_RESPONSE_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    CTI, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP, OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
)

osr_q06_response_group_order_group = OSR_Q06_RESPONSE_GROUP_ORDER_GROUP(  # ORDER - Segment group for OSR_Q06_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail_segment=None,  # OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OSR_Q06_RESPONSE_GROUP_ORDER_GROUP TEMPLATE-----
"""


class OSR_Q06_RESPONSE_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OSR_Q06_RESPONSE_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for OSR_Q06_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "O")
    _c_aliases = ("10", "None", "None", "19", "20")
    _c_components = (ORC, OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP, NTE, CTI)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL SEGMENT", "NTE", "CTI")
    _c_is_group = (False, True, True, False, False)
    _c_attrs = ("common_order", "timing", "order_detail_segment", "notes_and_comments", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.10
        timing: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.11, TQ2.12, ...)
        order_detail_segment: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        | None = None,  #  OBR.13, RQD.14, RQ1.15, RXO.16, ODS.17, ODT.18
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.20
    ):
        """
        None - `OSR_Q06_RESPONSE_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP>`_
        Segment group for OSR_Q06_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING|None, ORDER DETAIL SEGMENT|None, NTE|None, CTI|None

        :param common_order: Common Order (id: ORC | seq: 10 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 11, 12 | use: O | rpt: *)
        :param order_detail_segment: Order Detail Segment segment group: [OBR|None, RQD|None, RQ1|None, RXO|None, ODS|None, ODT|None] (id: ORDER DETAIL SEGMENT | seq: 13, 14, 15, 16, 17, 18 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 20 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.timing = timing
        self.order_detail_segment = order_detail_segment
        self.notes_and_comments = notes_and_comments
        self.clinical_trial_identification = clinical_trial_identification

    @property  # get ORC.10
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 10
        ---
        return_type: ORC.10: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.10
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 10
        ---
        param_type: ORC.10: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        | tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP.None | tuple[OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
    ) -> OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP | None:
        """
        id: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        return self._c_data[2][0]

    @order_detail_segment.setter  # set OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None
    def order_detail_segment(
        self,
        order_detail_segment: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        | None,
    ):
        """
        id: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OSR_Q06_RESPONSE_GROUP_ORDER_GROUP_ORDER_DETAIL_SEGMENT_GROUP
        """
        self._c_data[2] = (order_detail_segment,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: NTE.19 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[4]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 20
        ---
        param_type: CTI.20 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[4] = cti
        else:
            self._c_data[4] = (cti,)
