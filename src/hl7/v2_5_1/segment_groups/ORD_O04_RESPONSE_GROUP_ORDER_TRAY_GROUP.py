from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.ODT import ODT
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segment_groups.ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP import (
    ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP,
)


"""
ORDER TRAY - ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP
from utils.hl7.v2_5_1.segments import (
    ODT, NTE, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
)

ord_o04_response_group_order_tray_group = ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP(  # ORDER TRAY - Segment group for ORD_O04_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING TRAY|None, ODT|None, NTE|None
    common_order=orc,  # ORC(...)  # Required.
    timing_tray=None,  # ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP(...) 
    diet_tray_instructions=None,  # ODT(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP TEMPLATE-----
"""


class ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP"""
    _hl7_name = """ORDER TRAY"""
    _hl7_description = """Segment group for ORD_O04_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING TRAY|None, ODT|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O")
    _c_aliases = ("13", "None", "16", "17")
    _c_components = (ORC, ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ODT, NTE)
    _c_name = ("ORC", "TIMING TRAY", "ODT", "NTE")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "timing_tray", "diet_tray_instructions", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.13
        timing_tray: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]
        | None = None,  #  (TQ1.14, TQ2.15, ...)
        diet_tray_instructions: ODT | tuple[ODT, ...] | None = None,  #  ODT.16
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.17
    ):
        """
        None - `ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP>`_
        Segment group for ORD_O04_RESPONSE_GROUP - RESPONSE consisting of ORC, TIMING TRAY|None, ODT|None, NTE|None

        :param common_order: Common Order (id: ORC | seq: 13 | use: R | rpt: 1)
        :param timing_tray: Timing Tray segment group: [TQ1, TQ2|None] (id: TIMING TRAY | seq: 14, 15 | use: O | rpt: *)
        :param diet_tray_instructions: Diet Tray Instructions (id: ODT | seq: 16 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 17 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.timing_tray = timing_tray
        self.diet_tray_instructions = diet_tray_instructions
        self.notes_and_comments = notes_and_comments

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

    @property  # get TIMING TRAY
    def timing_tray(
        self,
    ) -> (
        tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]
        | tuple[None]
    ):
        """
        id: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        """
        return self._c_data[1]

    @timing_tray.setter  # set TIMING TRAY
    def timing_tray(
        self,
        timing_tray: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        | tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]
        | None,
    ):
        """
        id: TIMING TRAY SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP.None | tuple[ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORD_O04_RESPONSE_GROUP_ORDER_TRAY_GROUP_TIMING_TRAY_GROUP
        """
        if isinstance(timing_tray, tuple):
            self._c_data[1] = timing_tray
        else:
            self._c_data[1] = (timing_tray,)

    @property  # get ODT
    def diet_tray_instructions(self) -> tuple[ODT, ...] | tuple[None]:
        """
        id: ODT SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[ODT, ...]: (Diet Tray Instructions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ODT
        """
        return self._c_data[2]

    @diet_tray_instructions.setter  # set ODT
    def diet_tray_instructions(self, odt: ODT | tuple[ODT, ...] | None):
        """
        id: ODT SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: ODT.16 | tuple[ODT, ...]: (Diet Tray Instructions, ...)
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
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: NTE.17 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)
