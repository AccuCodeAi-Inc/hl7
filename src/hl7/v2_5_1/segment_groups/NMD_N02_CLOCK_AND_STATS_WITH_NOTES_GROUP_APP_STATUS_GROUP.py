from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.NSC import NSC


"""
APP STATUS - NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, NSC
)

nmd_n02_clock_and_stats_with_notes_group_app_status_group = NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP(  # APP STATUS - Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NSC, NTE|None
    application_status_change=nsc,  # NSC(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP TEMPLATE-----
"""


class NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP"""
    _hl7_name = """APP STATUS"""
    _hl7_description = """Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NSC, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("7", "8")
    _c_components = (NSC, NTE)
    _c_name = ("NSC", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("application_status_change", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        application_status_change: NSC,  #  Required. NSC.7
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.8
    ):
        """
        None - `NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP_APP_STATUS_GROUP>`_
        Segment group for NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP - CLOCK AND STATS WITH NOTES consisting of NSC, NTE|None

        :param application_status_change: Application Status Change (id: NSC | seq: 7 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 8 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.application_status_change = application_status_change
        self.notes_and_comments = notes_and_comments

    @property  # get NSC.7
    def application_status_change(self) -> NSC:
        """
        id: NSC | use: R | rpt: 1 | seq: 7
        ---
        return_type: NSC.7: Application Status Change
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC
        """
        return self._c_data[0][0]

    @application_status_change.setter  # set NSC.7
    def application_status_change(self, nsc: NSC):
        """
        id: NSC | use: R | rpt: 1 | seq: 7
        ---
        param_type: NSC.7: Application Status Change
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC
        """
        self._c_data[0] = (nsc,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: NTE.8 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
