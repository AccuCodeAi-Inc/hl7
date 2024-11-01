from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP import (
    NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP,
)
from ..segments.SFT import SFT
from ..segments.MSH import MSH


"""
Application management data message - NMD_N02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::NMD_N02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMD_N02
from utils.hl7.v2_5_1.segments import (
    SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
)

nmd_n02 = NMD_N02(  #  - The N02 event signifies when an unsolicited update (UU) Application Management Data message (NMD) is created by on application to transmit application management information to other applications
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    clock_and_stats_with_notes=nmd_n02_clock_and_stats_with_notes_group,  # NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::NMD_N02 TEMPLATE-----
"""


class NMD_N02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """NMD_N02"""
    _hl7_name = """Application management data message"""
    _hl7_description = """The N02 event signifies when an unsolicited update (UU) Application Management Data message (NMD) is created by on application to transmit application management information to other applications"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("1", "2", "None")
    _c_components = (MSH, SFT, NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP)
    _c_name = ("MSH", "SFT", "CLOCK AND STATS WITH NOTES")
    _c_is_group = (False, False, True)
    _c_attrs = ("message_header", "software_segment", "clock_and_stats_with_notes",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        clock_and_stats_with_notes: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
        | tuple[NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP, ...],  #  Required. (, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `NMD_N02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMD_N02>`_
        The N02 event signifies when an unsolicited update (UU) Application Management Data message (NMD) is created by on application to transmit application management information to other applications.  In this case, the initiating application sends an NMD message as an unsolicited update (UU) containing application management information to a receiving application, which responds with a generic acknowledgement message (ACK).

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param clock_and_stats_with_notes: Clock And Stats With Notes segment group: [CLOCK|None, APP STATS|None, APP STATUS|None] (id: CLOCK AND STATS WITH NOTES | seq: None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.message_header = message_header
        self.software_segment = software_segment
        self.clock_and_stats_with_notes = clock_and_stats_with_notes

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get CLOCK AND STATS WITH NOTES
    def clock_and_stats_with_notes(
        self,
    ) -> tuple[NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP, ...]:
        """
        id: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
        """
        return self._c_data[2]

    @clock_and_stats_with_notes.setter  # set CLOCK AND STATS WITH NOTES
    def clock_and_stats_with_notes(
        self,
        clock_and_stats_with_notes: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
        | tuple[NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP, ...],
    ):
        """
        id: CLOCK AND STATS WITH NOTES SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP.None | tuple[NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMD_N02_CLOCK_AND_STATS_WITH_NOTES_GROUP
        """
        if isinstance(clock_and_stats_with_notes, tuple):
            self._c_data[2] = clock_and_stats_with_notes
        else:
            self._c_data[2] = (clock_and_stats_with_notes,)
