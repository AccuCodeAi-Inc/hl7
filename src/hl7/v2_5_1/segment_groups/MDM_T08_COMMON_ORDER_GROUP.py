from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segment_groups.MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP import (
    MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP,
)
from ..segments.OBR import OBR
from ..segments.ORC import ORC


"""
COMMON ORDER - MDM_T08_COMMON_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::MDM_T08_COMMON_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import MDM_T08_COMMON_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP
)

mdm_t08_common_order_group = MDM_T08_COMMON_ORDER_GROUP(  # COMMON ORDER - Segment group for MDM_T08 - Document edit notification and content  consisting of ORC, TIMING|None, OBR, NTE|None
    common_order=orc,  # ORC(...)  # Required.
    timing=None,  # MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP(...) 
    observation_request=obr,  # OBR(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::MDM_T08_COMMON_ORDER_GROUP TEMPLATE-----
"""


class MDM_T08_COMMON_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """MDM_T08_COMMON_ORDER_GROUP"""
    _hl7_name = """COMMON ORDER"""
    _hl7_description = """Segment group for MDM_T08 - Document edit notification and content  consisting of ORC, TIMING|None, OBR, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MDM_T08_COMMON_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("6", "None", "9", "10")
    _c_components = (ORC, MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP, OBR, NTE)
    _c_name = ("ORC", "TIMING", "OBR", "NTE")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "timing", "observation_request", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.6
        observation_request: OBR,  #  Required. OBR.9
        timing: MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP
        | tuple[MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | None = None,  #  (TQ1.7, TQ2.8, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.10
    ):
        """
        None - `MDM_T08_COMMON_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/MDM_T08_COMMON_ORDER_GROUP>`_
        Segment group for MDM_T08 - Document edit notification and content  consisting of ORC, TIMING|None, OBR, NTE|None

        :param common_order: Common Order (id: ORC | seq: 6 | use: R | rpt: 1)
        :param timing: Timing segment group: [TQ1, TQ2|None] (id: TIMING | seq: 7, 8 | use: O | rpt: *)
        :param observation_request: Observation Request (id: OBR | seq: 9 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 10 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.timing = timing
        self.observation_request = observation_request
        self.notes_and_comments = notes_and_comments

    @property  # get ORC.6
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 6
        ---
        return_type: ORC.6: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.6
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 6
        ---
        param_type: ORC.6: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING
    def timing(
        self,
    ) -> tuple[MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP, ...] | tuple[None]:
        """
        id: MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP
        """
        return self._c_data[1]

    @timing.setter  # set TIMING
    def timing(
        self,
        timing: MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP
        | tuple[MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP, ...]
        | None,
    ):
        """
        id: TIMING SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP.None | tuple[MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MDM_T08_COMMON_ORDER_GROUP_TIMING_GROUP
        """
        if isinstance(timing, tuple):
            self._c_data[1] = timing
        else:
            self._c_data[1] = (timing,)

    @property  # get OBR.9
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 9
        ---
        return_type: OBR.9: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[2][0]

    @observation_request.setter  # set OBR.9
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 9
        ---
        param_type: OBR.9: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[2] = (obr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: NTE.10 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)
