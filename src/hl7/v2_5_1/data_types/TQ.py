from __future__ import annotations
from ...base import DataType
from .CE import CE
from .CQ import CQ
from .RI import RI
from .TS import TS
from .NM import NM
from .OSD import OSD
from .ST import ST
from .ID import ID
from .TX import TX
from ..tables.TqConjunctionId import TqConjunctionId


"""
DataType - TQ
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::TQ TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TQ,
    CE, CQ, RI, TS, NM, OSD, ST, ID, TX
)

tq = TQ(  # Timing Quantity - Describes when a service should be performed and how frequently
    quantity=None,  # CQ(...) 
    interval=None,  # RI(...) 
    duration=None,  # ST(...) 
    start_date_or_time=None,  # TS(...) 
    end_date_or_time=None,  # TS(...) 
    priority=None,  # ST(...) 
    condition=None,  # ST(...) 
    text=None,  # TX(...) 
    conjunction=None,  # ID(...) 
    order_sequencing=None,  # OSD(...) 
    occurrence_duration=None,  # CE(...) 
    total_occurrences=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::TQ TEMPLATE-----
"""


class TQ(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 1545
    _hl7_id = """TQ"""
    _hl7_name = """Timing Quantity"""
    _hl7_description = """Describes when a service should be performed and how frequently"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ"
    _c_length = (267, 206, 6, 26, 26, 6, 199, 200, 1, 110, 483, 4,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("TQ.1", "TQ.2", "TQ.3", "TQ.4", "TQ.5", "TQ.6", "TQ.7", "TQ.8", "TQ.9", "TQ.10", "TQ.11", "TQ.12",)
    _c_components = (CQ, RI, ST, TS, TS, ST, ST, TX, ID, OSD, CE, NM,)
    _c_names = ("Quantity", "Interval", "Duration", "Start Date/Time", "End Date/Time", "Priority", "Condition", "Text", "Conjunction", "Order Sequencing", "Occurrence Duration", "Total Occurrences",)
    _c_attrs = ("quantity", "interval", "duration", "start_date_or_time", "end_date_or_time", "priority", "condition", "text", "conjunction", "order_sequencing", "occurrence_duration", "total_occurrences",)
    # fmt: on

    def __init__(
        self,
        quantity: CQ | tuple[CQ, ...] | None = None,  # TQ.1
        interval: RI | tuple[RI, ...] | None = None,  # TQ.2
        duration: ST | tuple[ST, ...] | None = None,  # TQ.3
        start_date_or_time: TS | tuple[TS, ...] | None = None,  # TQ.4
        end_date_or_time: TS | tuple[TS, ...] | None = None,  # TQ.5
        priority: ST | tuple[ST, ...] | None = None,  # TQ.6
        condition: ST | tuple[ST, ...] | None = None,  # TQ.7
        text: TX | tuple[TX, ...] | None = None,  # TQ.8
        conjunction: TqConjunctionId
        | ID
        | tuple[TqConjunctionId | ID, ...]
        | None = None,  # TQ.9
        order_sequencing: OSD | tuple[OSD, ...] | None = None,  # TQ.10
        occurrence_duration: CE | tuple[CE, ...] | None = None,  # TQ.11
        total_occurrences: NM | tuple[NM, ...] | None = None,  # TQ.12
    ):
        """
                Timing Quantity - `TQ <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ>`_
                Describes when a service should be performed and how frequently.

        Note: The TQ data type is retained for backward compatibility only as of v 2.5. Refer to the TQ1 and TQ2 segments defined in chapter 4.

                :param quantity: This component specifies the quantity of the service that should be provided at each service interval (id: TQ.1 | len: 267 | use: O | rpt: 1)
                :param interval: Determines the interval between repeated services (id: TQ.2 | len: 206 | use: O | rpt: 1)
                :param duration: This component indicates how long the service should continue after it is started (id: TQ.3 | len: 6 | use: O | rpt: 1)
                :param start_date_or_time: This component may be specified by the orderer, in which case it indicates the earliest date/time at which the services should be started (id: TQ.4 | len: 26 | use: O | rpt: 1)
                :param end_date_or_time: When filled in by the requester of the service, this component should contain the latest date/time that the service should be performed (id: TQ.5 | len: 26 | use: O | rpt: 1)
                :param priority: This component describes the urgency of the request (id: TQ.6 | len: 6 | use: O | rpt: 1)
                :param condition: This is a free text component that describes the conditions under which the drug is to be given (id: TQ.7 | len: 199 | use: O | rpt: 1)
                :param text: This component is a full text version of the instruction (optional) (id: TQ.8 | len: 200 | use: O | rpt: 1)
                :param conjunction: This non-null component indicates that a second timing specification is to follow using the repeat delimiter (id: TQ.9 | len: 1 | use: O | rpt: 1)
                :param order_sequencing:  (id: TQ.10 | len: 110 | use: O | rpt: 1)
                :param occurrence_duration: This component contains the duration for a single performance of a service, e (id: TQ.11 | len: 483 | use: O | rpt: 1)
                :param total_occurrences: This component contains the total number of occurrences of a service that should result from this order (id: TQ.12 | len: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.quantity = quantity
        self.interval = interval
        self.duration = duration
        self.start_date_or_time = start_date_or_time
        self.end_date_or_time = end_date_or_time
        self.priority = priority
        self.condition = condition
        self.text = text
        self.conjunction = conjunction
        self.order_sequencing = order_sequencing
        self.occurrence_duration = occurrence_duration
        self.total_occurrences = total_occurrences

    @property  # get TQ.1
    def quantity(self) -> CQ | None:
        """
        id: TQ.1 | len: 267 | use: O | rpt: 1
        ---
        This component specifies the quantity of the service that should be provided at each service interval. For example, if two blood cultures are to be obtained every 4 hours, the quantity would be 2. If three units of blood are to be typed and cross-matched, the quantity would be 3. The default value is 1. When units are required, they can be added, specified by a subcomponent delimiter.
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.1
        """
        return self._c_data[0][0]

    @quantity.setter  # set TQ.1
    def quantity(self, cq: CQ | None):
        """
        id: TQ.1 | len: 267 | use: O | rpt: 1
        ---
        This component specifies the quantity of the service that should be provided at each service interval. For example, if two blood cultures are to be obtained every 4 hours, the quantity would be 2. If three units of blood are to be typed and cross-matched, the quantity would be 3. The default value is 1. When units are required, they can be added, specified by a subcomponent delimiter.
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.1
        """
        self._c_data[0] = (cq,)

    @property  # get TQ.2
    def interval(self) -> RI | None:
        """
        id: TQ.2 | len: 206 | use: O | rpt: 1
        ---
        Determines the interval between repeated services.
        ---
        return_type: RI: Repeat Interval
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.2
        """
        return self._c_data[1][0]

    @interval.setter  # set TQ.2
    def interval(self, ri: RI | None):
        """
        id: TQ.2 | len: 206 | use: O | rpt: 1
        ---
        Determines the interval between repeated services.
        ---
        param_type: RI: Repeat Interval
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.2
        """
        self._c_data[1] = (ri,)

    @property  # get TQ.3
    def duration(self) -> ST | None:
        """
        id: TQ.3 | len: 6 | use: O | rpt: 1
        ---
        This component indicates how long the service should continue after it is started. The default is INDEF (do indefinitely). This component is coded as follows:
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.3
        """
        return self._c_data[2][0]

    @duration.setter  # set TQ.3
    def duration(self, st: ST | None):
        """
        id: TQ.3 | len: 6 | use: O | rpt: 1
        ---
        This component indicates how long the service should continue after it is started. The default is INDEF (do indefinitely). This component is coded as follows:
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.3
        """
        self._c_data[2] = (st,)

    @property  # get TQ.4
    def start_date_or_time(self) -> TS | None:
        """
        id: TQ.4 | len: 26 | use: O | rpt: 1
        ---
        This component may be specified by the orderer, in which case it indicates the earliest date/time at which the services should be started. In many cases, however, the start date/time will be implied or will be defined by other fields in the order record (e.g., urgency - STAT). In such a case, this field will be empty.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.4
        """
        return self._c_data[3][0]

    @start_date_or_time.setter  # set TQ.4
    def start_date_or_time(self, ts: TS | None):
        """
        id: TQ.4 | len: 26 | use: O | rpt: 1
        ---
        This component may be specified by the orderer, in which case it indicates the earliest date/time at which the services should be started. In many cases, however, the start date/time will be implied or will be defined by other fields in the order record (e.g., urgency - STAT). In such a case, this field will be empty.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.4
        """
        self._c_data[3] = (ts,)

    @property  # get TQ.5
    def end_date_or_time(self) -> TS | None:
        """
        id: TQ.5 | len: 26 | use: O | rpt: 1
        ---
        When filled in by the requester of the service, this component should contain the latest date/time that the service should be performed. If it has not been performed by the specified time, it should not be performed at all. The requester may not always fill in this value, yet the filling service may fill it in on the basis of the instruction it receives and the actual start time.
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.5
        """
        return self._c_data[4][0]

    @end_date_or_time.setter  # set TQ.5
    def end_date_or_time(self, ts: TS | None):
        """
        id: TQ.5 | len: 26 | use: O | rpt: 1
        ---
        When filled in by the requester of the service, this component should contain the latest date/time that the service should be performed. If it has not been performed by the specified time, it should not be performed at all. The requester may not always fill in this value, yet the filling service may fill it in on the basis of the instruction it receives and the actual start time.
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.5
        """
        self._c_data[4] = (ts,)

    @property  # get TQ.6
    def priority(self) -> ST | None:
        """
        id: TQ.6 | len: 6 | use: O | rpt: 1
        ---
        This component describes the urgency of the request. The following values are suggested (the default for Priority is R):
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.6
        """
        return self._c_data[5][0]

    @priority.setter  # set TQ.6
    def priority(self, st: ST | None):
        """
        id: TQ.6 | len: 6 | use: O | rpt: 1
        ---
        This component describes the urgency of the request. The following values are suggested (the default for Priority is R):
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.6
        """
        self._c_data[5] = (st,)

    @property  # get TQ.7
    def condition(self) -> ST | None:
        """
        id: TQ.7 | len: 199 | use: O | rpt: 1
        ---
        This is a free text component that describes the conditions under which the drug is to be given. For example, PRN pain , or to keep blood pressure below 110. The presence of text in this field should be taken to mean that human review is needed to determine the how and/or when this drug should be given.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.7
        """
        return self._c_data[6][0]

    @condition.setter  # set TQ.7
    def condition(self, st: ST | None):
        """
        id: TQ.7 | len: 199 | use: O | rpt: 1
        ---
        This is a free text component that describes the conditions under which the drug is to be given. For example, PRN pain , or to keep blood pressure below 110. The presence of text in this field should be taken to mean that human review is needed to determine the how and/or when this drug should be given.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.7
        """
        self._c_data[6] = (st,)

    @property  # get TQ.8
    def text(self) -> TX | None:
        """
        id: TQ.8 | len: 200 | use: O | rpt: 1
        ---
        This component is a full text version of the instruction (optional).
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.8
        """
        return self._c_data[7][0]

    @text.setter  # set TQ.8
    def text(self, tx: TX | None):
        """
        id: TQ.8 | len: 200 | use: O | rpt: 1
        ---
        This component is a full text version of the instruction (optional).
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.8
        """
        self._c_data[7] = (tx,)

    @property  # get TQ.9
    def conjunction(self) -> TqConjunctionId | None:
        """
        id: TQ.9 | len: 1 | use: O | rpt: 1
        ---
        This non-null component indicates that a second timing specification is to follow using the repeat delimiter. Refer to HL7 table 0472 - TQ Conjunction ID for valid values
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.9
        """
        return self._c_data[8][0]

    @conjunction.setter  # set TQ.9
    def conjunction(self, tq_conjunction_id: TqConjunctionId | None):
        """
        id: TQ.9 | len: 1 | use: O | rpt: 1
        ---
        This non-null component indicates that a second timing specification is to follow using the repeat delimiter. Refer to HL7 table 0472 - TQ Conjunction ID for valid values
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.9
        """
        self._c_data[8] = (tq_conjunction_id,)

    @property  # get TQ.10
    def order_sequencing(self) -> OSD | None:
        """
        id: TQ.10 | len: 110 | use: O | rpt: 1
        ---
        None
        ---
        return_type: OSD: Order Sequence Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.10
        """
        return self._c_data[9][0]

    @order_sequencing.setter  # set TQ.10
    def order_sequencing(self, osd: OSD | None):
        """
        id: TQ.10 | len: 110 | use: O | rpt: 1
        ---
        None
        ---
        param_type: OSD: Order Sequence Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.10
        """
        self._c_data[9] = (osd,)

    @property  # get TQ.11
    def occurrence_duration(self) -> CE | None:
        """
        id: TQ.11 | len: 483 | use: O | rpt: 1
        ---
        This component contains the duration for a single performance of a service, e.g., whirlpool twenty minutes three times per day for three days. It is optional within TQ and does not repeat.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.11
        """
        return self._c_data[10][0]

    @occurrence_duration.setter  # set TQ.11
    def occurrence_duration(self, ce: CE | None):
        """
        id: TQ.11 | len: 483 | use: O | rpt: 1
        ---
        This component contains the duration for a single performance of a service, e.g., whirlpool twenty minutes three times per day for three days. It is optional within TQ and does not repeat.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.11
        """
        self._c_data[10] = (ce,)

    @property  # get TQ.12
    def total_occurrences(self) -> NM | None:
        """
        id: TQ.12 | len: 4 | use: O | rpt: 1
        ---
        This component contains the total number of occurrences of a service that should result from this order. It is optional within TQ and does not repeat. If both the end date/time and the total occurrences are valued and the occurrences would extend beyond the end date/time, then the end date/time takes precedence. Otherwise the number of occurrences takes precedence.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.12
        """
        return self._c_data[11][0]

    @total_occurrences.setter  # set TQ.12
    def total_occurrences(self, nm: NM | None):
        """
        id: TQ.12 | len: 4 | use: O | rpt: 1
        ---
        This component contains the total number of occurrences of a service that should result from this order. It is optional within TQ and does not repeat. If both the end date/time and the total occurrences are valued and the occurrences would extend beyond the end date/time, then the end date/time takes precedence. Otherwise the number of occurrences takes precedence.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ.12
        """
        self._c_data[11] = (nm,)
