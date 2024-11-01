from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.NMQ_N01_CLOCK_AND_STATISTICS_GROUP import (
    NMQ_N01_CLOCK_AND_STATISTICS_GROUP,
)
from ..segment_groups.NMQ_N01_QRY_WITH_DETAIL_GROUP import NMQ_N01_QRY_WITH_DETAIL_GROUP
from ..segments.MSH import MSH
from ..segments.SFT import SFT


"""
Application management query message - NMQ_N01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::NMQ_N01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import NMQ_N01
from utils.hl7.v2_5_1.segments import (
    SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    NMQ_N01_CLOCK_AND_STATISTICS_GROUP, NMQ_N01_QRY_WITH_DETAIL_GROUP
)

nmq_n01 = NMQ_N01(  #  - The N01 event signifies when the NMQ (Application Management Query) message is used by one application to make application control-level requests for information or action to another application
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    qry_with_detail=None,  # NMQ_N01_QRY_WITH_DETAIL_GROUP(...) 
    clock_and_statistics=nmq_n01_clock_and_statistics_group,  # NMQ_N01_CLOCK_AND_STATISTICS_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::NMQ_N01 TEMPLATE-----
"""


class NMQ_N01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """NMQ_N01"""
    _hl7_name = """Application management query message"""
    _hl7_description = """The N01 event signifies when the NMQ (Application Management Query) message is used by one application to make application control-level requests for information or action to another application"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMQ_N01"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "R")
    _c_aliases = ("1", "2", "None", "None")
    _c_components = (MSH, SFT, NMQ_N01_QRY_WITH_DETAIL_GROUP, NMQ_N01_CLOCK_AND_STATISTICS_GROUP)
    _c_name = ("MSH", "SFT", "QRY WITH DETAIL", "CLOCK AND STATISTICS")
    _c_is_group = (False, False, True, True)
    _c_attrs = ("message_header", "software_segment", "qry_with_detail", "clock_and_statistics",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        clock_and_statistics: NMQ_N01_CLOCK_AND_STATISTICS_GROUP
        | tuple[
            NMQ_N01_CLOCK_AND_STATISTICS_GROUP, ...
        ],  #  Required. (NCK.5, NST.6, NSC.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        qry_with_detail: NMQ_N01_QRY_WITH_DETAIL_GROUP | None = None,  #  QRD.3, QRF.4
    ):
        """
         - `NMQ_N01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/NMQ_N01>`_
        The N01 event signifies when the NMQ (Application Management Query) message is used by one application to make application control-level requests for information or action to another application.  It has three segments, the NCK segment (system clock), the NST segment (application control-level statistics), and the NSC segment (application control-level status change). At least one of these three segments must be present in the NMQ message. If a segment is present in the NMQ message, the corresponding segment needs to be present in the NMR message to return the requested data or status.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param qry_with_detail: Qry With Detail segment group: [QRD, QRF|None] (id: QRY WITH DETAIL | seq: 3, 4 | use: O | rpt: 1)
        :param clock_and_statistics: Clock And Statistics segment group: [NCK|None, NST|None, NSC|None] (id: CLOCK AND STATISTICS | seq: 5, 6, 7 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.qry_with_detail = qry_with_detail
        self.clock_and_statistics = clock_and_statistics

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

    @property  # get NMQ_N01_QRY_WITH_DETAIL_GROUP.None
    def qry_with_detail(self) -> NMQ_N01_QRY_WITH_DETAIL_GROUP | None:
        """
        id: NMQ_N01_QRY_WITH_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: NMQ_N01_QRY_WITH_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMQ_N01_QRY_WITH_DETAIL_GROUP
        """
        return self._c_data[2][0]

    @qry_with_detail.setter  # set NMQ_N01_QRY_WITH_DETAIL_GROUP.None
    def qry_with_detail(self, qry_with_detail: NMQ_N01_QRY_WITH_DETAIL_GROUP | None):
        """
        id: NMQ_N01_QRY_WITH_DETAIL_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: NMQ_N01_QRY_WITH_DETAIL_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMQ_N01_QRY_WITH_DETAIL_GROUP
        """
        self._c_data[2] = (qry_with_detail,)

    @property  # get CLOCK AND STATISTICS
    def clock_and_statistics(self) -> tuple[NMQ_N01_CLOCK_AND_STATISTICS_GROUP, ...]:
        """
        id: NMQ_N01_CLOCK_AND_STATISTICS_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[NMQ_N01_CLOCK_AND_STATISTICS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMQ_N01_CLOCK_AND_STATISTICS_GROUP
        """
        return self._c_data[3]

    @clock_and_statistics.setter  # set CLOCK AND STATISTICS
    def clock_and_statistics(
        self,
        clock_and_stat_istics: NMQ_N01_CLOCK_AND_STATISTICS_GROUP
        | tuple[NMQ_N01_CLOCK_AND_STATISTICS_GROUP, ...],
    ):
        """
        id: CLOCK AND STATISTICS SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: NMQ_N01_CLOCK_AND_STATISTICS_GROUP.None | tuple[NMQ_N01_CLOCK_AND_STATISTICS_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NMQ_N01_CLOCK_AND_STATISTICS_GROUP
        """
        if isinstance(clock_and_stat_istics, tuple):
            self._c_data[3] = clock_and_stat_istics
        else:
            self._c_data[3] = (clock_and_stat_istics,)
