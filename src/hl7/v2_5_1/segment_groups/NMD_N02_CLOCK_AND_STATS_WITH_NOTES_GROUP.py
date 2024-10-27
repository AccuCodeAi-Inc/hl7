from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP import (
    NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP,
)
from ..segment_groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP import (
    NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP,
)
from ..segment_groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP import (
    NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP,
)


"""
CLOCK AND STATS WITH NOTES - NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
from utils.hl7.v2_5_1.segments import (
    
)
from utils.hl7.v2_5_1.segment_groups import (
    NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP, NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP, NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP
)

nmd_n02_clock_and_stats_with_notes_group = NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP(  # CLOCK AND STATS WITH NOTES - Segment group for NMD_N02 - Application management data message consisting of CLOCK|None, APP STATS|None, APP STATUS|None
    clock=None,  # NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP(...) 
    app_stats=None,  # NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP(...) 
    app_status=None,  # NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP TEMPLATE-----
"""


class NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP"""
    _hl7_name = """CLOCK AND STATS WITH NOTES"""
    _hl7_description = """Segment group for NMD_N02 - Application management data message consisting of CLOCK|None, APP STATS|None, APP STATUS|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("O", "O", "O")
    _c_aliases = ("None", "None", "None")
    _c_components = (NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP, NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP, NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP)
    _c_name = ("CLOCK", "APP STATS", "APP STATUS")
    _c_is_group = (True, True, True)
    _c_attrs = ("clock", "app_stats", "app_status",)
    # fmt: on

    def __init__(
        self,
        clock: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP
        | None = None,  #  NCK.3, NTE.4
        app_stats: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP
        | None = None,  #  NST.5, NTE.6
        app_status: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP
        | None = None,  #  NSC.7, NTE.8
    ):
        """
        None - `NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP>`_
        Segment group for NMD_N02 - Application management data message consisting of CLOCK|None, APP STATS|None, APP STATUS|None

        :param clock: Clock segment group: [NCK, NTE|None] (id: CLOCK | seq: 3, 4 | use: O | rpt: 1)
        :param app_stats: App Stats segment group: [NST, NTE|None] (id: APP STATS | seq: 5, 6 | use: O | rpt: 1)
        :param app_status: App Status segment group: [NSC, NTE|None] (id: APP STATUS | seq: 7, 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.clock = clock
        self.app_stats = app_stats
        self.app_status = app_status

    @property  # get NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP.None
    def clock(self) -> NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP | None:
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP
        """
        return self._c_data[0][0]

    @clock.setter  # set NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP.None
    def clock(self, clock: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP | None):
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_CLOCK_GROUP
        """
        self._c_data[0] = (clock,)

    @property  # get NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP.None
    def app_stats(
        self,
    ) -> NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP | None:
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP
        """
        return self._c_data[1][0]

    @app_stats.setter  # set NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP.None
    def app_stats(
        self, app_stats: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP | None
    ):
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATS_GROUP
        """
        self._c_data[1] = (app_stats,)

    @property  # get NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP.None
    def app_status(
        self,
    ) -> NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP | None:
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP
        """
        return self._c_data[2][0]

    @app_status.setter  # set NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP.None
    def app_status(
        self,
        app_status: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP | None,
    ):
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP
        """
        self._c_data[2] = (app_status,)
