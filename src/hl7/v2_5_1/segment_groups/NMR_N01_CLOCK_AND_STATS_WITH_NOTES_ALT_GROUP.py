from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NSC import NSC
from ..segments.NST import NST
from ..segments.NTE import NTE
from ..segments.NCK import NCK


"""
CLOCK AND STATS WITH NOTES ALT - NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
from utils.hl7.v2_5_1.segments import (
    NST, NTE, NCK, NSC
)

nmr_n01_clock_and_stats_with_notes_alt_group = NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP(  # CLOCK AND STATS WITH NOTES ALT - Segment group for NMR_N01 - Application management response consisting of NCK|None, NTE|None, NST|None, NTE|None, NSC|None, NTE|None
    system_clock=None,  # NCK(...) 
    notes_and_comments=None,  # NTE(...) 
    application_control_level_statistics=None,  # NST(...) 
    notes_and_comments_9=None,  # NTE(...) 
    application_status_change=None,  # NSC(...) 
    notes_and_comments_11=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP TEMPLATE-----
"""


class NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP"""
    _hl7_name = """CLOCK AND STATS WITH NOTES ALT"""
    _hl7_description = """Segment group for NMR_N01 - Application management response consisting of NCK|None, NTE|None, NST|None, NTE|None, NSC|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535)
    _c_usage = ("O", "O", "O", "O", "O", "O")
    _c_aliases = ("6", "7", "8", "9", "10", "11")
    _c_components = (NCK, NTE, NST, NTE, NSC, NTE)
    _c_name = ("NCK", "NTE", "NST", "NTE", "NSC", "NTE")
    _c_is_group = (False, False, False, False, False, False)
    _c_attrs = ("system_clock", "notes_and_comments", "application_control_level_statistics", "notes_and_comments_9", "application_status_change", "notes_and_comments_11",)
    # fmt: on

    def __init__(
        self,
        system_clock: NCK | None = None,  #  NCK.6
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.7
        application_control_level_statistics: NST | None = None,  #  NST.8
        notes_and_comments_9: NTE | tuple[NTE, ...] | None = None,  #  NTE.9
        application_status_change: NSC | None = None,  #  NSC.10
        notes_and_comments_11: NTE | tuple[NTE, ...] | None = None,  #  NTE.11
    ):
        """
        None - `NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP>`_
        Segment group for NMR_N01 - Application management response consisting of NCK|None, NTE|None, NST|None, NTE|None, NSC|None, NTE|None

        :param system_clock: System Clock (id: NCK | seq: 6 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 7 | use: O | rpt: *)
        :param application_control_level_statistics: Application control level statistics (id: NST | seq: 8 | use: O | rpt: 1)
        :param notes_and_comments_9: Notes and Comments (id: NTE | seq: 9 | use: O | rpt: *)
        :param application_status_change: Application Status Change (id: NSC | seq: 10 | use: O | rpt: 1)
        :param notes_and_comments_11: Notes and Comments (id: NTE | seq: 11 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.system_clock = system_clock
        self.notes_and_comments = notes_and_comments
        self.application_control_level_statistics = application_control_level_statistics
        self.notes_and_comments_9 = notes_and_comments_9
        self.application_status_change = application_status_change
        self.notes_and_comments_11 = notes_and_comments_11

    @property  # get NCK.6
    def system_clock(self) -> NCK | None:
        """
        id: NCK | use: O | rpt: 1 | seq: 6
        ---
        return_type: NCK.6: System Clock
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK
        """
        return self._c_data[0][0]

    @system_clock.setter  # set NCK.6
    def system_clock(self, nck: NCK | None):
        """
        id: NCK | use: O | rpt: 1 | seq: 6
        ---
        param_type: NCK.6: System Clock
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK
        """
        self._c_data[0] = (nck,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NTE.7 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get NST.8
    def application_control_level_statistics(self) -> NST | None:
        """
        id: NST | use: O | rpt: 1 | seq: 8
        ---
        return_type: NST.8: Application control level statistics
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST
        """
        return self._c_data[2][0]

    @application_control_level_statistics.setter  # set NST.8
    def application_control_level_statistics(self, nst: NST | None):
        """
        id: NST | use: O | rpt: 1 | seq: 8
        ---
        param_type: NST.8: Application control level statistics
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST
        """
        self._c_data[2] = (nst,)

    @property  # get NTE
    def notes_and_comments_9(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments_9.setter  # set NTE
    def notes_and_comments_9(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: NTE.9 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get NSC.10
    def application_status_change(self) -> NSC | None:
        """
        id: NSC | use: O | rpt: 1 | seq: 10
        ---
        return_type: NSC.10: Application Status Change
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC
        """
        return self._c_data[4][0]

    @application_status_change.setter  # set NSC.10
    def application_status_change(self, nsc: NSC | None):
        """
        id: NSC | use: O | rpt: 1 | seq: 10
        ---
        param_type: NSC.10: Application Status Change
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC
        """
        self._c_data[4] = (nsc,)

    @property  # get NTE
    def notes_and_comments_11(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[5]

    @notes_and_comments_11.setter  # set NTE
    def notes_and_comments_11(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: NTE.11 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[5] = nte
        else:
            self._c_data[5] = (nte,)
