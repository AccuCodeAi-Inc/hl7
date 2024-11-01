from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP import (
    RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP,
)
from ..segment_groups.RAS_O17_ORDER_GROUP_TIMING_GROUP import (
    RAS_O17_ORDER_GROUP_TIMING_GROUP,
)
from ..segment_groups.RAS_O17_ORDER_GROUP_ENCODING_GROUP import (
    RAS_O17_ORDER_GROUP_ENCODING_GROUP,
)
from ..segment_groups.RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP import (
    RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP,
)
from ..segments.CTI import CTI
from ..segments.ORC import ORC


"""
ORDER - RAS_O17_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RAS_O17_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RAS_O17_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC, CTI
)
from utils.hl7.v2_5_1.segment_groups import (
    RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP, RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, RAS_O17_ORDER_GROUP_TIMING_GROUP, RAS_O17_ORDER_GROUP_ENCODING_GROUP
)

ras_o17_order_group = RAS_O17_ORDER_GROUP(  # ORDER - Segment group for RAS_O17 - Pharmacy/Treatment Administration consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, ADMINISTRATION, CTI|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # RAS_O17_ORDER_GROUP_TIMING_GROUP(...) 
    order_detail=None,  # RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP(...) 
    encoding=None,  # RAS_O17_ORDER_GROUP_ENCODING_GROUP(...) 
    administration=ras_o17_order_group_administration_group,  # RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP(...)  # Required.
    clinical_trial_identification=None,  # CTI(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RAS_O17_ORDER_GROUP TEMPLATE-----
"""


class RAS_O17_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RAS_O17_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RAS_O17 - Pharmacy/Treatment Administration consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, ADMINISTRATION, CTI|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "R", "O")
    _c_aliases = ("10", "None", "None", "None", "None", "27")
    _c_components = (ORC, RAS_O17_ORDER_GROUP_TIMING_GROUP, RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP, RAS_O17_ORDER_GROUP_ENCODING_GROUP, RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, CTI)
    _c_name = ("ORC", "TIMING", "ORDER DETAIL", "ENCODING", "ADMINISTRATION", "CTI")
    _c_is_group = (False, True, True, True, True, False)
    _c_attrs = ("common_order", "timing", "order_detail", "encoding", "administration", "clinical_trial_identification",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.10
        administration: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP
        | tuple[
            RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, ...
        ],  #  Required. (RXA.23, RXR.24, ...)
        timing: RAS_O17_ORDER_GROUP_TIMING_GROUP
        | tuple[RAS_O17_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.11, TQ2.12, ...)
        order_detail: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP | None = None,  #  RXO.13
        encoding: RAS_O17_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.18, RXR.21, RXC.22
        clinical_trial_identification: CTI | tuple[CTI, ...] | None = None,  #  CTI.27
    ):
        """
        None - `RAS_O17_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAS_O17_ORDER_GROUP>`_
        Segment group for RAS_O17 - Pharmacy/Treatment Administration consisting of ORC, TIMING|None, ORDER DETAIL|None, ENCODING|None, ADMINISTRATION, CTI|None

        :param common_order: Common Order (id: ORC | seq: 10 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 11, 12 | use: O | rpt: *)
        :param order_detail: Order Detail segment group: [RXO, ORDER DETAIL SUPPLEMENT|None] (id: ORDER DETAIL | seq: 13, None | use: O | rpt: 1)
        :param encoding: Encoding segment group: [RXE, TIMING ENCODED, RXR, RXC|None] (id: ENCODING | seq: 18, None, 21, 22 | use: O | rpt: 1)
        :param administration: Administration segment group: [RXA, RXR, OBSERVATION|None] (id: ADMINISTRATION | seq: 23, 24, None | use: R | rpt: *)
        :param clinical_trial_identification: Clinical Trial Identification (id: CTI | seq: 27 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.common_order = common_order
        self.timing = timing
        self.order_detail = order_detail
        self.encoding = encoding
        self.administration = administration
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
    def timing(self) -> tuple[RAS_O17_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: RAS_O17_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RAS_O17_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: RAS_O17_ORDER_GROUP_TIMING_GROUP
        | tuple[RAS_O17_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP_TIMING_GROUP.None | tuple[RAS_O17_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self) -> RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP | None:
        """
        id: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @order_detail.setter  # set RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP.None
    def order_detail(self, order_detail: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP | None):
        """
        id: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ORDER_DETAIL_GROUP
        """
        self._c_data[2] = (order_detail,)

    @property  # get RAS_O17_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RAS_O17_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RAS_O17_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RAS_O17_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[3][0]

    @encoding.setter  # set RAS_O17_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self, encoding: RAS_O17_ORDER_GROUP_ENCODING_GROUP | None):
        """
        id: RAS_O17_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[3] = (encoding,)

    @property  # get ADMINISTRATION
    def administration(self) -> tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, ...]:
        """
        id: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP
        """
        return self._c_data[4]

    @administration.setter  # set ADMINISTRATION
    def administration(
        self,
        admin_istration: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP
        | tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, ...],
    ):
        """
        id: ADMINISTRATION SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP.None | tuple[RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAS_O17_ORDER_GROUP_ADMINISTRATION_GROUP
        """
        if isinstance(admin_istration, tuple):
            self._c_data[4] = admin_istration
        else:
            self._c_data[4] = (admin_istration,)

    @property  # get CTI
    def clinical_trial_identification(self) -> tuple[CTI, ...] | tuple[None]:
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        return_type: tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        return self._c_data[5]

    @clinical_trial_identification.setter  # set CTI
    def clinical_trial_identification(self, cti: CTI | tuple[CTI, ...] | None):
        """
        id: CTI SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        param_type: CTI.27 | tuple[CTI, ...]: (Clinical Trial Identification, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CTI
        """
        if isinstance(cti, tuple):
            self._c_data[5] = cti
        else:
            self._c_data[5] = (cti,)
