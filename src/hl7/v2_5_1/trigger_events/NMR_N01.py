from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.ERR import ERR
from ..segment_groups.NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP import (
    NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP,
)
from ..segments.QRD import QRD
from ..segments.MSH import MSH
from ..segments.MSA import MSA


"""
Application management response - NMR_N01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::NMR_N01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMR_N01
from utils.hl7.v2_5_1.segments import (
    ERR, MSA, QRD, MSH, SFT
)
from utils.hl7.v2_5_1.segment_groups import (
    NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
)

nmr_n01 = NMR_N01(  #  - The N01 event signifies when the NMQ (Application Management Query) message is used by one application to make application control-level requests for information or action to another application
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    original_style_query_definition=None,  # QRD(...) 
    clock_and_stats_with_notes_alt=nmr_n01_clock_and_stats_with_notes_alt_group,  # NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::NMR_N01 TEMPLATE-----
"""


class NMR_N01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """NMR_N01"""
    _hl7_name = """Application management response"""
    _hl7_description = """The N01 event signifies when the NMQ (Application Management Query) message is used by one application to make application control-level requests for information or action to another application"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMR_N01"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "None")
    _c_components = (MSH, SFT, MSA, ERR, QRD, NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QRD", "CLOCK AND STATS WITH NOTES ALT")
    _c_is_group = (False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "original_style_query_definition", "clock_and_stats_with_notes_alt",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        clock_and_stats_with_notes_alt: NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
        | tuple[
            NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP, ...
        ],  #  Required. (NCK.6, NTE.7, NST.8, NTE.9, NSC.10, NTE.11, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.4
        original_style_query_definition: QRD | None = None,  #  QRD.5
    ):
        """
         - `NMR_N01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMR_N01>`_
        The N01 event signifies when the NMQ (Application Management Query) message is used by one application to make application control-level requests for information or action to another application.  It has three segments, the NCK segment (system clock), the NST segment (application control-level statistics), and the NSC segment (application control-level status change). At least one of these three segments must be present in the NMQ message. If a segment is present in the NMQ message, the corresponding segment needs to be present in the NMR message to return the requested data or status.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: *)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 5 | use: O | rpt: 1)
        :param clock_and_stats_with_notes_alt: Clock And Stats With Notes Alt segment group: [NCK|None, NTE|None, NST|None, NTE|None, NSC|None, NTE|None] (id: CLOCK AND STATS WITH NOTES ALT | seq: 6, 7, 8, 9, 10, 11 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.original_style_query_definition = original_style_query_definition
        self.clock_and_stats_with_notes_alt = clock_and_stats_with_notes_alt

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

    @property  # get MSA.3
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        param_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[2] = (msa,)

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[3]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: ERR.4 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[3] = err
        else:
            self._c_data[3] = (err,)

    @property  # get QRD.5
    def original_style_query_definition(self) -> QRD | None:
        """
        id: QRD | use: O | rpt: 1 | seq: 5
        ---
        return_type: QRD.5: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[4][0]

    @original_style_query_definition.setter  # set QRD.5
    def original_style_query_definition(self, qrd: QRD | None):
        """
        id: QRD | use: O | rpt: 1 | seq: 5
        ---
        param_type: QRD.5: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[4] = (qrd,)

    @property  # get CLOCK AND STATS WITH NOTES ALT
    def clock_and_stats_with_notes_alt(
        self,
    ) -> tuple[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP, ...]:
        """
        id: NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
        """
        return self._c_data[5]

    @clock_and_stats_with_notes_alt.setter  # set CLOCK AND STATS WITH NOTES ALT
    def clock_and_stats_with_notes_alt(
        self,
        clock_and_stats_with_notes_alt: NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
        | tuple[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP, ...],
    ):
        """
        id: CLOCK AND STATS WITH NOTES ALT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP.None | tuple[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT_GROUP
        """
        if isinstance(clock_and_stats_with_notes_alt, tuple):
            self._c_data[5] = clock_and_stats_with_notes_alt
        else:
            self._c_data[5] = (clock_and_stats_with_notes_alt,)
