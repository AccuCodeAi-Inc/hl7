from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.NCK import NCK


"""
CLOCK - NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP
from utils.hl7.v2_5_1.segments import (
    NCK, NTE
)

nmd_n02_clock_and_stats_with_notes_group_clock_group = NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP(  # CLOCK - Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NCK, NTE|None
    system_clock=nck,  # NCK(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP TEMPLATE-----
"""


class NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP"""
    _hl7_name = """CLOCK"""
    _hl7_description = """Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NCK, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("3", "4")
    _c_components = (NCK, NTE)
    _c_name = ("NCK", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("system_clock", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        system_clock: NCK,  #  Required. NCK.3
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.4
    ):
        """
        None - `NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP>`_
        Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NCK, NTE|None

        :param system_clock: System Clock (id: NCK | seq: 3 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 4 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.system_clock = system_clock
        self.notes_and_comments = notes_and_comments

    @property  # get NCK.3
    def system_clock(self) -> NCK:
        """
        id: NCK | use: R | rpt: 1 | seq: 3
        ---
        return_type: NCK.3: System Clock
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK
        """
        return self._c_data[0][0]

    @system_clock.setter  # set NCK.3
    def system_clock(self, nck: NCK):
        """
        id: NCK | use: R | rpt: 1 | seq: 3
        ---
        param_type: NCK.3: System Clock
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK
        """
        self._c_data[0] = (nck,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: NTE.4 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
