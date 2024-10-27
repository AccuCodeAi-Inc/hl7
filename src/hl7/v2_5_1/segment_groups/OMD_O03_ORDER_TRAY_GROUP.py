from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ODT import ODT
from ..segment_groups.OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP import (
    OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP,
)
from ..segments.NTE import NTE
from ..segments.ORC import ORC


"""
ORDER TRAY - OMD_O03_ORDER_TRAY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMD_O03_ORDER_TRAY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMD_O03_ORDER_TRAY_GROUP
from utils.hl7.v2_5_1.segments import (
    ODT, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
)

omd_o03_order_tray_group = OMD_O03_ORDER_TRAY_GROUP(  # ORDER TRAY - Segment group for OMD_O03 - Dietary Order consisting of ORC, TIMING TRAY|None, ODT, NTE|None
    common_order=orc,  # ORC(...)  # Required.
    timing_tray=None,  # OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP(...) 
    diet_tray_instructions=odt,  # ODT(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMD_O03_ORDER_TRAY_GROUP TEMPLATE-----
"""


class OMD_O03_ORDER_TRAY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMD_O03_ORDER_TRAY_GROUP"""
    _hl7_name = """ORDER TRAY"""
    _hl7_description = """Segment group for OMD_O03 - Dietary Order consisting of ORC, TIMING TRAY|None, ODT, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03_ORDER_TRAY_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("21", "None", "24", "25")
    _c_components = (ORC, OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ODT, NTE)
    _c_name = ("ORC", "TIMING TRAY", "ODT", "NTE")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "timing_tray", "diet_tray_instructions", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.21
        diet_tray_instructions: ODT | tuple[ODT, ...],  #  Required. ODT.24
        timing_tray: OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        | tuple[OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]
        | None = None,  #  (TQ1.22, TQ2.23, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.25
    ):
        """
        None - `OMD_O03_ORDER_TRAY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMD_O03_ORDER_TRAY_GROUP>`_
        Segment group for OMD_O03 - Dietary Order consisting of ORC, TIMING TRAY|None, ODT, NTE|None

        :param common_order: Common Order (id: ORC | seq: 21 | use: R | rpt: 1)
        :param timing_tray: Timing Tray segment group: [TQ1, TQ2|None] (id: TIMING TRAY | seq: 22, 23 | use: O | rpt: *)
        :param diet_tray_instructions: Diet Tray Instructions (id: ODT | seq: 24 | use: R | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 25 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.timing_tray = timing_tray
        self.diet_tray_instructions = diet_tray_instructions
        self.notes_and_comments = notes_and_comments

    @property  # get ORC.21
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 21
        ---
        return_type: ORC.21: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.21
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 21
        ---
        param_type: ORC.21: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get TIMING TRAY
    def timing_tray(
        self,
    ) -> tuple[OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...] | tuple[None]:
        """
        id: OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        """
        return self._c_data[1]

    @timing_tray.setter  # set TIMING TRAY
    def timing_tray(
        self,
        timing_tray: OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        | tuple[OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING TRAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP.None | tuple[OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMD_O03_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        """
        if isinstance(timing_tray, tuple):
            self._c_data[1] = timing_tray
        else:
            self._c_data[1] = (timing_tray,)

    @property  # get ODT
    def diet_tray_instructions(self) -> tuple[ODT, ...]:
        """
        id: ODT SEGMENT GROUP | use: R | rpt: * | seq: 24
        ---
        return_type: tuple[ODT, ...]: (Diet Tray Instructions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT
        """
        return self._c_data[2]

    @diet_tray_instructions.setter  # set ODT
    def diet_tray_instructions(self, odt: ODT | tuple[ODT, ...]):
        """
        id: ODT SEGMENT GROUP | use: R | rpt: * | seq: 24
        ---
        param_type: ODT.24 | tuple[ODT, ...]: (Diet Tray Instructions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT
        """
        if isinstance(odt, tuple):
            self._c_data[2] = odt
        else:
            self._c_data[2] = (odt,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        param_type: NTE.25 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)
