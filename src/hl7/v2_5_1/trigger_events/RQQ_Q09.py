from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.DSC import DSC
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.ERQ import ERQ


"""
Event replay query - RQQ_Q09
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RQQ_Q09 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RQQ_Q09
from utils.hl7.v2_5_1.segments import (
    ERQ, DSC, SFT, MSH
)

rqq_q09 = RQQ_Q09(  #  - The Event Replay Query under version 2
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_replay_query=erq,  # ERQ(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::RQQ_Q09 TEMPLATE-----
"""


class RQQ_Q09(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RQQ_Q09"""
    _hl7_name = """Event replay query"""
    _hl7_description = """The Event Replay Query under version 2"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQQ_Q09"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4")
    _c_components = (MSH, SFT, ERQ, DSC)
    _c_name = ("MSH", "SFT", "ERQ", "DSC")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_replay_query", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_replay_query: ERQ,  #  Required. ERQ.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        continuation_pointer: DSC | None = None,  #  DSC.4
    ):
        """
                 - `RQQ_Q09 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RQQ_Q09>`_
                The Event Replay Query under version 2.3 provides a way for the querying system to request data formatted very similar to the format that would have been used were this data to be sent as an update in response to a trigger event.

        The RQQ is used to request data formatted as an event replay response.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_replay_query: Event replay query (id: ERQ | seq: 3 | use: R | rpt: 1)
                :param continuation_pointer: Continuation Pointer (id: DSC | seq: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_replay_query = event_replay_query
        self.continuation_pointer = continuation_pointer

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

    @property  # get ERQ.3
    def event_replay_query(self) -> ERQ:
        """
        id: ERQ | use: R | rpt: 1 | seq: 3
        ---
        return_type: ERQ.3: Event replay query
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERQ
        """
        return self._c_data[2][0]

    @event_replay_query.setter  # set ERQ.3
    def event_replay_query(self, erq: ERQ):
        """
        id: ERQ | use: R | rpt: 1 | seq: 3
        ---
        param_type: ERQ.3: Event replay query
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERQ
        """
        self._c_data[2] = (erq,)

    @property  # get DSC.4
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 4
        ---
        return_type: DSC.4: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[3][0]

    @continuation_pointer.setter  # set DSC.4
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 4
        ---
        param_type: DSC.4: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[3] = (dsc,)
