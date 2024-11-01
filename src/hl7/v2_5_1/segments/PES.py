from __future__ import annotations
from ...base import HL7Segment
from ..data_types.XON import XON
from ..data_types.TS import TS
from ..data_types.ID import ID
from ..data_types.XTN import XTN
from ..data_types.NM import NM
from ..data_types.XCN import XCN
from ..data_types.FT import FT
from ..data_types.EI import EI
from ..data_types.XAD import XAD
from ..tables.EventReportedTo import EventReportedTo
from ..tables.ReportSource import ReportSource
from ..tables.ReportTiming import ReportTiming


"""
Product Experience Sender - PES
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PES TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PES,
    XON, TS, ID, XTN, NM, XCN, FT, EI, XAD
)

pes = PES(  #  - 
    sender_organization_name=None,  # XON(...) 
    sender_individual_name=None,  # XCN(...) 
    sender_address=None,  # XAD(...) 
    sender_telephone=None,  # XTN(...) 
    sender_event_identifier=None,  # EI(...) 
    sender_sequence_number=None,  # NM(...) 
    sender_event_description=None,  # FT(...) 
    sender_comment=None,  # FT(...) 
    sender_aware_date_or_time=None,  # TS(...) 
    event_report_date=ts,  # TS(...)  # Required.
    event_report_timing_or_type=None,  # ID(...) 
    event_report_source=None,  # ID(...) 
    event_reported_to=None,  # ID(...) 
)

-----END SEGMENT::PES TEMPLATE-----
"""


class PES(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PES"""
    _hl7_name = """Product Experience Sender"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PES"
    _c_length = (250, 250, 250, 250, 75, 2, 600, 600, 26, 26, 3, 1, 1,)
    _c_rpt = (65535, 65535, 65535, 65535, 1, 1, 65535, 1, 1, 1, 2, 1, 65535,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "R", "O", "O", "O",)
    _c_components = (XON, XCN, XAD, XTN, EI, NM, FT, FT, TS, TS, ID, ID, ID,)
    _c_aliases = ("PES.1", "PES.2", "PES.3", "PES.4", "PES.5", "PES.6", "PES.7", "PES.8", "PES.9", "PES.10", "PES.11", "PES.12", "PES.13",)
    _c_names = ("Sender Organization Name", "Sender Individual Name", "Sender Address", "Sender Telephone", "Sender Event Identifier", "Sender Sequence Number", "Sender Event Description", "Sender Comment", "Sender Aware Date/Time", "Event Report Date", "Event Report Timing/Type", "Event Report Source", "Event Reported To",)
    _c_attrs = ("sender_organization_name", "sender_individual_name", "sender_address", "sender_telephone", "sender_event_identifier", "sender_sequence_number", "sender_event_description", "sender_comment", "sender_aware_date_or_time", "event_report_date", "event_report_timing_or_type", "event_report_source", "event_reported_to",)
    # fmt: on

    def __init__(
        self,
        event_report_date: TS,  # PES.10
        sender_organization_name: XON | None = None,  # PES.1
        sender_individual_name: XCN | None = None,  # PES.2
        sender_address: XAD | None = None,  # PES.3
        sender_telephone: XTN | None = None,  # PES.4
        sender_event_identifier: EI | None = None,  # PES.5
        sender_sequence_number: NM | None = None,  # PES.6
        sender_event_description: FT | None = None,  # PES.7
        sender_comment: FT | None = None,  # PES.8
        sender_aware_date_or_time: TS | None = None,  # PES.9
        event_report_timing_or_type: ReportTiming | ID | None = None,  # PES.11
        event_report_source: ReportSource | ID | None = None,  # PES.12
        event_reported_to: EventReportedTo | ID | None = None,  # PES.13
    ):
        """
        Product Experience Sender - `PES <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PES>`_


        :param sender_organization_name: Extended Composite Name and Identification Number for Organizations (id: PES.1 | len: 250 | use: O | rpt: *)
        :param sender_individual_name: Extended Composite ID Number and Name for Persons (id: PES.2 | len: 250 | use: O | rpt: *)
        :param sender_address: Extended Address (id: PES.3 | len: 250 | use: O | rpt: *)
        :param sender_telephone: Extended Telecommunication Number (id: PES.4 | len: 250 | use: O | rpt: *)
        :param sender_event_identifier: Entity Identifier (id: PES.5 | len: 75 | use: O | rpt: 1)
        :param sender_sequence_number: Numeric (id: PES.6 | len: 2 | use: O | rpt: 1)
        :param sender_event_description: Formatted Text Data (id: PES.7 | len: 600 | use: O | rpt: *)
        :param sender_comment: Formatted Text Data (id: PES.8 | len: 600 | use: O | rpt: 1)
        :param sender_aware_date_or_time: Time Stamp (id: PES.9 | len: 26 | use: O | rpt: 1)
        :param event_report_date: Time Stamp (id: PES.10 | len: 26 | use: R | rpt: 1)
        :param event_report_timing_or_type: Coded values for HL7 tables (id: PES.11 | len: 3 | use: O | rpt: 2)
        :param event_report_source: Coded values for HL7 tables (id: PES.12 | len: 1 | use: O | rpt: 1)
        :param event_reported_to: Coded values for HL7 tables (id: PES.13 | len: 1 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 13
        self.sender_organization_name = sender_organization_name
        self.sender_individual_name = sender_individual_name
        self.sender_address = sender_address
        self.sender_telephone = sender_telephone
        self.sender_event_identifier = sender_event_identifier
        self.sender_sequence_number = sender_sequence_number
        self.sender_event_description = sender_event_description
        self.sender_comment = sender_comment
        self.sender_aware_date_or_time = sender_aware_date_or_time
        self.event_report_date = event_report_date
        self.event_report_timing_or_type = event_report_timing_or_type
        self.event_report_source = event_report_source
        self.event_reported_to = event_reported_to

    @property
    def sender_organization_name(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: PES.1 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.1
        """
        return self._c_data[0]

    @sender_organization_name.setter  # set PES.1
    def sender_organization_name(self, xon: XON | tuple[XON] | None):
        """
        id: PES.1 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.1
        """
        if isinstance(xon, tuple):
            self._c_data[0] = xon
        else:
            self._c_data[0] = (xon,)

    @property
    def sender_individual_name(self) -> tuple[XCN, ...] | tuple[None]:
        """
        id: PES.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.2
        """
        return self._c_data[1]

    @sender_individual_name.setter  # set PES.2
    def sender_individual_name(self, xcn: XCN | tuple[XCN] | None):
        """
        id: PES.2 | len: 250 | use: O | rpt: *
        ---
        param_type: XCN | tuple[XCN, ...]: (Extended Composite ID Number and Name for Persons, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.2
        """
        if isinstance(xcn, tuple):
            self._c_data[1] = xcn
        else:
            self._c_data[1] = (xcn,)

    @property
    def sender_address(self) -> tuple[XAD, ...] | tuple[None]:
        """
        id: PES.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.3
        """
        return self._c_data[2]

    @sender_address.setter  # set PES.3
    def sender_address(self, xad: XAD | tuple[XAD] | None):
        """
        id: PES.3 | len: 250 | use: O | rpt: *
        ---
        param_type: XAD | tuple[XAD, ...]: (Extended Address, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.3
        """
        if isinstance(xad, tuple):
            self._c_data[2] = xad
        else:
            self._c_data[2] = (xad,)

    @property
    def sender_telephone(self) -> tuple[XTN, ...] | tuple[None]:
        """
        id: PES.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.4
        """
        return self._c_data[3]

    @sender_telephone.setter  # set PES.4
    def sender_telephone(self, xtn: XTN | tuple[XTN] | None):
        """
        id: PES.4 | len: 250 | use: O | rpt: *
        ---
        param_type: XTN | tuple[XTN, ...]: (Extended Telecommunication Number, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.4
        """
        if isinstance(xtn, tuple):
            self._c_data[3] = xtn
        else:
            self._c_data[3] = (xtn,)

    @property  # get PES.5
    def sender_event_identifier(self) -> EI | None:
        """
        id: PES.5 | len: 75 | use: O | rpt: 1
        ---
        return_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.5
        """
        return self._c_data[4][0]

    @sender_event_identifier.setter  # set PES.5
    def sender_event_identifier(self, ei: EI | None):
        """
        id: PES.5 | len: 75 | use: O | rpt: 1
        ---
        param_type: EI: Entity Identifier
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.5
        """
        self._c_data[4] = (ei,)

    @property  # get PES.6
    def sender_sequence_number(self) -> NM | None:
        """
        id: PES.6 | len: 2 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.6
        """
        return self._c_data[5][0]

    @sender_sequence_number.setter  # set PES.6
    def sender_sequence_number(self, nm: NM | None):
        """
        id: PES.6 | len: 2 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.6
        """
        self._c_data[5] = (nm,)

    @property
    def sender_event_description(self) -> tuple[FT, ...] | tuple[None]:
        """
        id: PES.7 | len: 600 | use: O | rpt: *
        ---
        return_type: tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.7
        """
        return self._c_data[6]

    @sender_event_description.setter  # set PES.7
    def sender_event_description(self, ft: FT | tuple[FT] | None):
        """
        id: PES.7 | len: 600 | use: O | rpt: *
        ---
        param_type: FT | tuple[FT, ...]: (Formatted Text Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.7
        """
        if isinstance(ft, tuple):
            self._c_data[6] = ft
        else:
            self._c_data[6] = (ft,)

    @property  # get PES.8
    def sender_comment(self) -> FT | None:
        """
        id: PES.8 | len: 600 | use: O | rpt: 1
        ---
        return_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.8
        """
        return self._c_data[7][0]

    @sender_comment.setter  # set PES.8
    def sender_comment(self, ft: FT | None):
        """
        id: PES.8 | len: 600 | use: O | rpt: 1
        ---
        param_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.8
        """
        self._c_data[7] = (ft,)

    @property  # get PES.9
    def sender_aware_date_or_time(self) -> TS | None:
        """
        id: PES.9 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.9
        """
        return self._c_data[8][0]

    @sender_aware_date_or_time.setter  # set PES.9
    def sender_aware_date_or_time(self, ts: TS | None):
        """
        id: PES.9 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.9
        """
        self._c_data[8] = (ts,)

    @property  # get PES.10
    def event_report_date(self) -> TS:
        """
        id: PES.10 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.10
        """
        return self._c_data[9][0]

    @event_report_date.setter  # set PES.10
    def event_report_date(self, ts: TS):
        """
        id: PES.10 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.10
        """
        self._c_data[9] = (ts,)

    @property
    def event_report_timing_or_type(self) -> tuple[ReportTiming, ...] | tuple[None]:
        """
        id: PES.11 | len: 3 | use: O | rpt: 2
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.11
        """
        return self._c_data[10]

    @event_report_timing_or_type.setter  # set PES.11
    def event_report_timing_or_type(
        self, report_timing: ReportTiming | tuple[ReportTiming] | None
    ):
        """
        id: PES.11 | len: 3 | use: O | rpt: 2
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.11
        """
        if isinstance(report_timing, tuple):
            self._c_data[10] = report_timing
        else:
            self._c_data[10] = (report_timing,)

    @property  # get PES.12
    def event_report_source(self) -> ReportSource | None:
        """
        id: PES.12 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.12
        """
        return self._c_data[11][0]

    @event_report_source.setter  # set PES.12
    def event_report_source(self, report_source: ReportSource | None):
        """
        id: PES.12 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.12
        """
        self._c_data[11] = (report_source,)

    @property
    def event_reported_to(self) -> tuple[EventReportedTo, ...] | tuple[None]:
        """
        id: PES.13 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.13
        """
        return self._c_data[12]

    @event_reported_to.setter  # set PES.13
    def event_reported_to(
        self, event_reported_to: EventReportedTo | tuple[EventReportedTo] | None
    ):
        """
        id: PES.13 | len: 1 | use: O | rpt: *
        ---
        param_type: ID | tuple[ID, ...]: (Coded values for HL7 tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PES.13
        """
        if isinstance(event_reported_to, tuple):
            self._c_data[12] = event_reported_to
        else:
            self._c_data[12] = (event_reported_to,)
