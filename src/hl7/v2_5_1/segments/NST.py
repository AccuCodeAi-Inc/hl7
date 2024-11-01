from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.NM import NM
from ..tables.SourceType import SourceType
from ..tables.YesOrNoIndicator import YesOrNoIndicator


"""
Application control level statistics - NST
HL7 Version: 2.5.1

-----BEGIN SEGMENT::NST TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NST,
    ST, ID, TS, NM
)

nst = NST(  #  - The NST segment allows application control-level statistical information to be passed between the various systems on the network
    statistics_available=id,  # ID(...)  # Required.
    source_identifier=None,  # ST(...) 
    source_type=None,  # ID(...) 
    statistics_start=None,  # TS(...) 
    statistics_end=None,  # TS(...) 
    receive_character_count=None,  # NM(...) 
    send_character_count=None,  # NM(...) 
    messages_received=None,  # NM(...) 
    messages_sent=None,  # NM(...) 
    checksum_errors_received=None,  # NM(...) 
    length_errors_received=None,  # NM(...) 
    other_errors_received=None,  # NM(...) 
    connect_timeouts=None,  # NM(...) 
    receive_timeouts=None,  # NM(...) 
    application_control_level_errors=None,  # NM(...) 
)

-----END SEGMENT::NST TEMPLATE-----
"""


class NST(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """NST"""
    _hl7_name = """Application control level statistics"""
    _hl7_description = """The NST segment allows application control-level statistical information to be passed between the various systems on the network"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST"
    _c_length = (1, 30, 3, 26, 26, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (ID, ST, ID, TS, TS, NM, NM, NM, NM, NM, NM, NM, NM, NM, NM,)
    _c_aliases = ("NST.1", "NST.2", "NST.3", "NST.4", "NST.5", "NST.6", "NST.7", "NST.8", "NST.9", "NST.10", "NST.11", "NST.12", "NST.13", "NST.14", "NST.15",)
    _c_names = ("Statistics Available", "Source Identifier", "Source Type", "Statistics Start", "Statistics End", "Receive Character Count", "Send Character Count", "Messages Received", "Messages Sent", "Checksum Errors Received", "Length Errors Received", "Other Errors Received", "Connect Timeouts", "Receive Timeouts", "Application control-level Errors",)
    _c_attrs = ("statistics_available", "source_identifier", "source_type", "statistics_start", "statistics_end", "receive_character_count", "send_character_count", "messages_received", "messages_sent", "checksum_errors_received", "length_errors_received", "other_errors_received", "connect_timeouts", "receive_timeouts", "application_control_level_errors",)
    # fmt: on

    def __init__(
        self,
        statistics_available: YesOrNoIndicator
        | ID
        | tuple[YesOrNoIndicator | ID, ...],  # NST.1
        source_identifier: ST | tuple[ST, ...] | None = None,  # NST.2
        source_type: SourceType
        | ID
        | tuple[SourceType | ID, ...]
        | None = None,  # NST.3
        statistics_start: TS | tuple[TS, ...] | None = None,  # NST.4
        statistics_end: TS | tuple[TS, ...] | None = None,  # NST.5
        receive_character_count: NM | tuple[NM, ...] | None = None,  # NST.6
        send_character_count: NM | tuple[NM, ...] | None = None,  # NST.7
        messages_received: NM | tuple[NM, ...] | None = None,  # NST.8
        messages_sent: NM | tuple[NM, ...] | None = None,  # NST.9
        checksum_errors_received: NM | tuple[NM, ...] | None = None,  # NST.10
        length_errors_received: NM | tuple[NM, ...] | None = None,  # NST.11
        other_errors_received: NM | tuple[NM, ...] | None = None,  # NST.12
        connect_timeouts: NM | tuple[NM, ...] | None = None,  # NST.13
        receive_timeouts: NM | tuple[NM, ...] | None = None,  # NST.14
        application_control_level_errors: NM | tuple[NM, ...] | None = None,  # NST.15
    ):
        """
                Application control level statistics - `NST <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NST>`_
                The NST segment allows application control-level statistical information to be passed between the various systems on the network. Some fields in this segment refer to portions of lower level protocols; they contain information that can be used by application management applications monitoring the state of various network links.

        Usage Notes: Fields 2-15.  These are all marked optional since the statistics kept on a particular link and negotiated between the two systems in question will vary.  Not all values will apply to each system.  Some values are concerned with the type of port, and some values pertain to the lower level protocol.

                :param statistics_available: Coded values for HL7 tables (id: NST.1 | len: 1 | use: R | rpt: 1)
                :param source_identifier: String Data (id: NST.2 | len: 30 | use: O | rpt: 1)
                :param source_type: Coded values for HL7 tables (id: NST.3 | len: 3 | use: O | rpt: 1)
                :param statistics_start: Time Stamp (id: NST.4 | len: 26 | use: O | rpt: 1)
                :param statistics_end: Time Stamp (id: NST.5 | len: 26 | use: O | rpt: 1)
                :param receive_character_count: Numeric (id: NST.6 | len: 10 | use: O | rpt: 1)
                :param send_character_count: Numeric (id: NST.7 | len: 10 | use: O | rpt: 1)
                :param messages_received: Numeric (id: NST.8 | len: 10 | use: O | rpt: 1)
                :param messages_sent: Numeric (id: NST.9 | len: 10 | use: O | rpt: 1)
                :param checksum_errors_received: Numeric (id: NST.10 | len: 10 | use: O | rpt: 1)
                :param length_errors_received: Numeric (id: NST.11 | len: 10 | use: O | rpt: 1)
                :param other_errors_received: Numeric (id: NST.12 | len: 10 | use: O | rpt: 1)
                :param connect_timeouts: Numeric (id: NST.13 | len: 10 | use: O | rpt: 1)
                :param receive_timeouts: Numeric (id: NST.14 | len: 10 | use: O | rpt: 1)
                :param application_control_level_errors: Numeric (id: NST.15 | len: 10 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 15
        self.statistics_available = statistics_available
        self.source_identifier = source_identifier
        self.source_type = source_type
        self.statistics_start = statistics_start
        self.statistics_end = statistics_end
        self.receive_character_count = receive_character_count
        self.send_character_count = send_character_count
        self.messages_received = messages_received
        self.messages_sent = messages_sent
        self.checksum_errors_received = checksum_errors_received
        self.length_errors_received = length_errors_received
        self.other_errors_received = other_errors_received
        self.connect_timeouts = connect_timeouts
        self.receive_timeouts = receive_timeouts
        self.application_control_level_errors = application_control_level_errors

    @property  # get NST.1
    def statistics_available(self) -> YesOrNoIndicator:
        """
        id: NST.1 | len: 1 | use: R | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.1
        """
        return self._c_data[0][0]

    @statistics_available.setter  # set NST.1
    def statistics_available(self, yes_or_no_indicator: YesOrNoIndicator):
        """
        id: NST.1 | len: 1 | use: R | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.1
        """
        self._c_data[0] = (yes_or_no_indicator,)

    @property  # get NST.2
    def source_identifier(self) -> ST | None:
        """
        id: NST.2 | len: 30 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.2
        """
        return self._c_data[1][0]

    @source_identifier.setter  # set NST.2
    def source_identifier(self, st: ST | None):
        """
        id: NST.2 | len: 30 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.2
        """
        self._c_data[1] = (st,)

    @property  # get NST.3
    def source_type(self) -> SourceType | None:
        """
        id: NST.3 | len: 3 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.3
        """
        return self._c_data[2][0]

    @source_type.setter  # set NST.3
    def source_type(self, source_type: SourceType | None):
        """
        id: NST.3 | len: 3 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.3
        """
        self._c_data[2] = (source_type,)

    @property  # get NST.4
    def statistics_start(self) -> TS | None:
        """
        id: NST.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.4
        """
        return self._c_data[3][0]

    @statistics_start.setter  # set NST.4
    def statistics_start(self, ts: TS | None):
        """
        id: NST.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.4
        """
        self._c_data[3] = (ts,)

    @property  # get NST.5
    def statistics_end(self) -> TS | None:
        """
        id: NST.5 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.5
        """
        return self._c_data[4][0]

    @statistics_end.setter  # set NST.5
    def statistics_end(self, ts: TS | None):
        """
        id: NST.5 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.5
        """
        self._c_data[4] = (ts,)

    @property  # get NST.6
    def receive_character_count(self) -> NM | None:
        """
        id: NST.6 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.6
        """
        return self._c_data[5][0]

    @receive_character_count.setter  # set NST.6
    def receive_character_count(self, nm: NM | None):
        """
        id: NST.6 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.6
        """
        self._c_data[5] = (nm,)

    @property  # get NST.7
    def send_character_count(self) -> NM | None:
        """
        id: NST.7 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.7
        """
        return self._c_data[6][0]

    @send_character_count.setter  # set NST.7
    def send_character_count(self, nm: NM | None):
        """
        id: NST.7 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.7
        """
        self._c_data[6] = (nm,)

    @property  # get NST.8
    def messages_received(self) -> NM | None:
        """
        id: NST.8 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.8
        """
        return self._c_data[7][0]

    @messages_received.setter  # set NST.8
    def messages_received(self, nm: NM | None):
        """
        id: NST.8 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.8
        """
        self._c_data[7] = (nm,)

    @property  # get NST.9
    def messages_sent(self) -> NM | None:
        """
        id: NST.9 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.9
        """
        return self._c_data[8][0]

    @messages_sent.setter  # set NST.9
    def messages_sent(self, nm: NM | None):
        """
        id: NST.9 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.9
        """
        self._c_data[8] = (nm,)

    @property  # get NST.10
    def checksum_errors_received(self) -> NM | None:
        """
        id: NST.10 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.10
        """
        return self._c_data[9][0]

    @checksum_errors_received.setter  # set NST.10
    def checksum_errors_received(self, nm: NM | None):
        """
        id: NST.10 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.10
        """
        self._c_data[9] = (nm,)

    @property  # get NST.11
    def length_errors_received(self) -> NM | None:
        """
        id: NST.11 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.11
        """
        return self._c_data[10][0]

    @length_errors_received.setter  # set NST.11
    def length_errors_received(self, nm: NM | None):
        """
        id: NST.11 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.11
        """
        self._c_data[10] = (nm,)

    @property  # get NST.12
    def other_errors_received(self) -> NM | None:
        """
        id: NST.12 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.12
        """
        return self._c_data[11][0]

    @other_errors_received.setter  # set NST.12
    def other_errors_received(self, nm: NM | None):
        """
        id: NST.12 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.12
        """
        self._c_data[11] = (nm,)

    @property  # get NST.13
    def connect_timeouts(self) -> NM | None:
        """
        id: NST.13 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.13
        """
        return self._c_data[12][0]

    @connect_timeouts.setter  # set NST.13
    def connect_timeouts(self, nm: NM | None):
        """
        id: NST.13 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.13
        """
        self._c_data[12] = (nm,)

    @property  # get NST.14
    def receive_timeouts(self) -> NM | None:
        """
        id: NST.14 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.14
        """
        return self._c_data[13][0]

    @receive_timeouts.setter  # set NST.14
    def receive_timeouts(self, nm: NM | None):
        """
        id: NST.14 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.14
        """
        self._c_data[13] = (nm,)

    @property  # get NST.15
    def application_control_level_errors(self) -> NM | None:
        """
        id: NST.15 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.15
        """
        return self._c_data[14][0]

    @application_control_level_errors.setter  # set NST.15
    def application_control_level_errors(self, nm: NM | None):
        """
        id: NST.15 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NST.15
        """
        self._c_data[14] = (nm,)
