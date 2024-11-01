from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.NST import NST


"""
APP STATS - NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP
from utils.hl7.v2_5_1.segments import (
    NST, NTE
)

nmd_n02_clock_and_stats_with_notes_group_app_stats_group = NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP(  # APP STATS - Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NST, NTE|None
    application_control_level_statistics=nst,  # NST(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP TEMPLATE-----
"""


class NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP"""
    _hl7_name = """APP STATS"""
    _hl7_description = """Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NST, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("5", "6")
    _c_components = (NST, NTE)
    _c_name = ("NST", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("application_control_level_statistics", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        application_control_level_statistics: NST,  #  Required. NST.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
    ):
        """
        None - `NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP>`_
        Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NST, NTE|None

        :param application_control_level_statistics: Application control level statistics (id: NST | seq: 5 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.application_control_level_statistics = application_control_level_statistics
        self.notes_and_comments = notes_and_comments

    @property  # get NST.5
    def application_control_level_statistics(self) -> NST:
        """
        id: NST | use: R | rpt: 1 | seq: 5
        ---
        return_type: NST.5: Application control level statistics
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST
        """
        return self._c_data[0][0]

    @application_control_level_statistics.setter  # set NST.5
    def application_control_level_statistics(self, nst: NST):
        """
        id: NST | use: R | rpt: 1 | seq: 5
        ---
        param_type: NST.5: Application control level statistics
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST
        """
        self._c_data[0] = (nst,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: NTE.6 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
