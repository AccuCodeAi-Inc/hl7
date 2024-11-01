from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.FT import FT
from ..data_types.TS import TS
from ..tables.EventType import EventType


"""
Equipment/log Service - EQP
HL7 Version: 2.5.1

-----BEGIN SEGMENT::EQP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    EQP,
    CE, ST, FT, TS
)

eqp = EQP(  #  - The equipment log/service segment is the data necessary to maintain an adequate audit trail of events that have occurred on a particular piece of equipment
    event_type=ce,  # CE(...)  # Required.
    file_name=None,  # ST(...) 
    start_date_or_time=ts,  # TS(...)  # Required.
    end_date_or_time=None,  # TS(...) 
    transaction_data=ft,  # FT(...)  # Required.
)

-----END SEGMENT::EQP TEMPLATE-----
"""


class EQP(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """EQP"""
    _hl7_name = """Equipment/log Service"""
    _hl7_description = """The equipment log/service segment is the data necessary to maintain an adequate audit trail of events that have occurred on a particular piece of equipment"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQP"
    _c_length = (250, 20, 26, 26, 65536,)
    _c_rpt = (1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "R", "O", "R",)
    _c_components = (CE, ST, TS, TS, FT,)
    _c_aliases = ("EQP.1", "EQP.2", "EQP.3", "EQP.4", "EQP.5",)
    _c_names = ("Event type", "File Name", "Start Date/Time", "End Date/Time", "Transaction Data",)
    _c_attrs = ("event_type", "file_name", "start_date_or_time", "end_date_or_time", "transaction_data",)
    # fmt: on

    def __init__(
        self,
        event_type: EventType | CE,  # EQP.1
        start_date_or_time: TS,  # EQP.3
        transaction_data: FT,  # EQP.5
        file_name: ST | None = None,  # EQP.2
        end_date_or_time: TS | None = None,  # EQP.4
    ):
        """
        Equipment/log Service - `EQP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EQP>`_
        The equipment log/service segment is the data necessary to maintain an adequate audit trail of events that have occurred on a particular piece of equipment.

        :param event_type: Coded Element (id: EQP.1 | len: 250 | use: R | rpt: 1)
        :param file_name: String Data (id: EQP.2 | len: 20 | use: O | rpt: 1)
        :param start_date_or_time: Time Stamp (id: EQP.3 | len: 26 | use: R | rpt: 1)
        :param end_date_or_time: Time Stamp (id: EQP.4 | len: 26 | use: O | rpt: 1)
        :param transaction_data: Formatted Text Data (id: EQP.5 | len: 65536 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.event_type = event_type
        self.file_name = file_name
        self.start_date_or_time = start_date_or_time
        self.end_date_or_time = end_date_or_time
        self.transaction_data = transaction_data

    @property  # get EQP.1
    def event_type(self) -> EventType:
        """
        id: EQP.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.1
        """
        return self._c_data[0][0]

    @event_type.setter  # set EQP.1
    def event_type(self, event_type: EventType):
        """
        id: EQP.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.1
        """
        self._c_data[0] = (event_type,)

    @property  # get EQP.2
    def file_name(self) -> ST | None:
        """
        id: EQP.2 | len: 20 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.2
        """
        return self._c_data[1][0]

    @file_name.setter  # set EQP.2
    def file_name(self, st: ST | None):
        """
        id: EQP.2 | len: 20 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.2
        """
        self._c_data[1] = (st,)

    @property  # get EQP.3
    def start_date_or_time(self) -> TS:
        """
        id: EQP.3 | len: 26 | use: R | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.3
        """
        return self._c_data[2][0]

    @start_date_or_time.setter  # set EQP.3
    def start_date_or_time(self, ts: TS):
        """
        id: EQP.3 | len: 26 | use: R | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.3
        """
        self._c_data[2] = (ts,)

    @property  # get EQP.4
    def end_date_or_time(self) -> TS | None:
        """
        id: EQP.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.4
        """
        return self._c_data[3][0]

    @end_date_or_time.setter  # set EQP.4
    def end_date_or_time(self, ts: TS | None):
        """
        id: EQP.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.4
        """
        self._c_data[3] = (ts,)

    @property  # get EQP.5
    def transaction_data(self) -> FT:
        """
        id: EQP.5 | len: 65536 | use: R | rpt: 1
        ---
        return_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.5
        """
        return self._c_data[4][0]

    @transaction_data.setter  # set EQP.5
    def transaction_data(self, ft: FT):
        """
        id: EQP.5 | len: 65536 | use: R | rpt: 1
        ---
        param_type: FT: Formatted Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/EQP.5
        """
        self._c_data[4] = (ft,)
