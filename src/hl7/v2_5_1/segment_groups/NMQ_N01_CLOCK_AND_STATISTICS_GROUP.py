from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NSC import NSC
from ..segments.NST import NST
from ..segments.NCK import NCK


"""
CLOCK AND STATISTICS - NMQ_N01_CLOCK_AND_STATISTICS_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::NMQ_N01_CLOCK_AND_STATISTICS_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMQ_N01_CLOCK_AND_STATISTICS_GROUP
from utils.hl7.v2_5_1.segments import (
    NST, NSC, NCK
)

nmq_n01_clock_and_statistics_group = NMQ_N01_CLOCK_AND_STATISTICS_GROUP(  # CLOCK AND STATISTICS - Segment group for NMQ_N01 - Application management query message consisting of NCK|None, NST|None, NSC|None
    system_clock=None,  # NCK(...) 
    application_control_level_statistics=None,  # NST(...) 
    application_status_change=None,  # NSC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::NMQ_N01_CLOCK_AND_STATISTICS_GROUP TEMPLATE-----
"""


class NMQ_N01_CLOCK_AND_STATISTICS_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """NMQ_N01_CLOCK_AND_STATISTICS_GROUP"""
    _hl7_name = """CLOCK AND STATISTICS"""
    _hl7_description = """Segment group for NMQ_N01 - Application management query message consisting of NCK|None, NST|None, NSC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMQ_N01_CLOCK_AND_STATISTICS_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 1)
    _c_usage = ("O", "O", "O")
    _c_aliases = ("5", "6", "7")
    _c_components = (NCK, NST, NSC)
    _c_name = ("NCK", "NST", "NSC")
    _c_is_group = (False, False, False)
    _c_attrs = ("system_clock", "application_control_level_statistics", "application_status_change",)
    # fmt: on

    def __init__(
        self,
        system_clock: NCK | None = None,  #  NCK.5
        application_control_level_statistics: NST | None = None,  #  NST.6
        application_status_change: NSC | None = None,  #  NSC.7
    ):
        """
        None - `NMQ_N01_CLOCK_AND_STATISTICS_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMQ_N01_CLOCK_AND_STATISTICS_GROUP>`_
        Segment group for NMQ_N01 - Application management query message consisting of NCK|None, NST|None, NSC|None

        :param system_clock: System Clock (id: NCK | seq: 5 | use: O | rpt: 1)
        :param application_control_level_statistics: Application control level statistics (id: NST | seq: 6 | use: O | rpt: 1)
        :param application_status_change: Application Status Change (id: NSC | seq: 7 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.system_clock = system_clock
        self.application_control_level_statistics = application_control_level_statistics
        self.application_status_change = application_status_change

    @property  # get NCK.5
    def system_clock(self) -> NCK | None:
        """
        id: NCK | use: O | rpt: 1 | seq: 5
        ---
        return_type: NCK.5: System Clock
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK
        """
        return self._c_data[0][0]

    @system_clock.setter  # set NCK.5
    def system_clock(self, nck: NCK | None):
        """
        id: NCK | use: O | rpt: 1 | seq: 5
        ---
        param_type: NCK.5: System Clock
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NCK
        """
        self._c_data[0] = (nck,)

    @property  # get NST.6
    def application_control_level_statistics(self) -> NST | None:
        """
        id: NST | use: O | rpt: 1 | seq: 6
        ---
        return_type: NST.6: Application control level statistics
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST
        """
        return self._c_data[1][0]

    @application_control_level_statistics.setter  # set NST.6
    def application_control_level_statistics(self, nst: NST | None):
        """
        id: NST | use: O | rpt: 1 | seq: 6
        ---
        param_type: NST.6: Application control level statistics
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST
        """
        self._c_data[1] = (nst,)

    @property  # get NSC.7
    def application_status_change(self) -> NSC | None:
        """
        id: NSC | use: O | rpt: 1 | seq: 7
        ---
        return_type: NSC.7: Application Status Change
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC
        """
        return self._c_data[2][0]

    @application_status_change.setter  # set NSC.7
    def application_status_change(self, nsc: NSC | None):
        """
        id: NSC | use: O | rpt: 1 | seq: 7
        ---
        param_type: NSC.7: Application Status Change
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NSC
        """
        self._c_data[2] = (nsc,)
