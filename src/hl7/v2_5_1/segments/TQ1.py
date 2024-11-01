from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TM import TM
from ..data_types.TX import TX
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.RPT import RPT
from ..data_types.CWE import CWE
from ..data_types.SI import SI
from ..data_types.TS import TS
from ..tables.ExtendedPriorityCodes import ExtendedPriorityCodes
from ..tables.RiskManagementIncidentCode import RiskManagementIncidentCode


"""
Timing/Quantity - TQ1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::TQ1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TQ1,
    TM, TX, CQ, ID, NM, RPT, CWE, SI, TS
)

tq1 = TQ1(  #  - The TQ1 segment is used to specify the complex timing of events and actions such as those that occur in order management and scheduling systems
    set_id_tq1=None,  # SI(...) 
    quantity=None,  # CQ(...) 
    repeat_pattern=None,  # RPT(...) 
    explicit_time=None,  # TM(...) 
    relative_time_and_units=None,  # CQ(...) 
    service_duration=None,  # CQ(...) 
    start_date_or_time=None,  # TS(...) 
    end_date_or_time=None,  # TS(...) 
    priority=None,  # CWE(...) 
    condition_text=None,  # TX(...) 
    text_instruction=None,  # TX(...) 
    conjunction=None,  # ID(...) 
    occurrence_duration=None,  # CQ(...) 
    total_occurrences=None,  # NM(...) 
)

-----END SEGMENT::TQ1 TEMPLATE-----
"""


class TQ1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """TQ1"""
    _hl7_name = """Timing/Quantity"""
    _hl7_description = """The TQ1 segment is used to specify the complex timing of events and actions such as those that occur in order management and scheduling systems"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1"
    _c_length = (4, 20, 540, 20, 20, 20, 26, 26, 250, 250, 250, 10, 20, 10,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 1, 1, 1, 65535, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "C", "O", "O",)
    _c_components = (SI, CQ, RPT, TM, CQ, CQ, TS, TS, CWE, TX, TX, ID, CQ, NM,)
    _c_aliases = ("TQ1.1", "TQ1.2", "TQ1.3", "TQ1.4", "TQ1.5", "TQ1.6", "TQ1.7", "TQ1.8", "TQ1.9", "TQ1.10", "TQ1.11", "TQ1.12", "TQ1.13", "TQ1.14",)
    _c_names = ("Set ID - TQ1", "Quantity", "Repeat Pattern", "Explicit Time", "Relative Time and Units", "Service Duration", "Start date/time", "End date/time", "Priority", "Condition text", "Text instruction", "Conjunction", "Occurrence duration", "Total occurrences",)
    _c_attrs = ("set_id_tq1", "quantity", "repeat_pattern", "explicit_time", "relative_time_and_units", "service_duration", "start_date_or_time", "end_date_or_time", "priority", "condition_text", "text_instruction", "conjunction", "occurrence_duration", "total_occurrences",)
    # fmt: on

    def __init__(
        self,
        set_id_tq1: SI | None = None,  # TQ1.1
        quantity: CQ | None = None,  # TQ1.2
        repeat_pattern: RPT | None = None,  # TQ1.3
        explicit_time: TM | None = None,  # TQ1.4
        relative_time_and_units: CQ | None = None,  # TQ1.5
        service_duration: CQ | None = None,  # TQ1.6
        start_date_or_time: TS | None = None,  # TQ1.7
        end_date_or_time: TS | None = None,  # TQ1.8
        priority: ExtendedPriorityCodes | CWE | None = None,  # TQ1.9
        condition_text: TX | None = None,  # TQ1.10
        text_instruction: TX | None = None,  # TQ1.11
        conjunction: RiskManagementIncidentCode | ID | None = None,  # TQ1.12
        occurrence_duration: CQ | None = None,  # TQ1.13
        total_occurrences: NM | None = None,  # TQ1.14
    ):
        """
        Timing/Quantity - `TQ1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1>`_
        The TQ1 segment is used to specify the complex timing of events and actions such as those that occur in order management and scheduling systems. This segment determines the quantity, frequency, priority, and timing of a service. By allowing the segment to repeat, it is possible to have service requests that vary the quantity, frequency and priority of a service request over time.

        :param set_id_tq1: Sequence ID (id: TQ1.1 | len: 4 | use: O | rpt: 1)
        :param quantity: Composite Quantity with Units (id: TQ1.2 | len: 20 | use: O | rpt: 1)
        :param repeat_pattern: Repeat Pattern (id: TQ1.3 | len: 540 | use: O | rpt: *)
        :param explicit_time: Time (id: TQ1.4 | len: 20 | use: O | rpt: *)
        :param relative_time_and_units: Composite Quantity with Units (id: TQ1.5 | len: 20 | use: O | rpt: *)
        :param service_duration: Composite Quantity with Units (id: TQ1.6 | len: 20 | use: O | rpt: 1)
        :param start_date_or_time: Time Stamp (id: TQ1.7 | len: 26 | use: O | rpt: 1)
        :param end_date_or_time: Time Stamp (id: TQ1.8 | len: 26 | use: O | rpt: 1)
        :param priority: Coded with Exceptions (id: TQ1.9 | len: 250 | use: O | rpt: *)
        :param condition_text: Text Data (id: TQ1.10 | len: 250 | use: O | rpt: 1)
        :param text_instruction: Text Data (id: TQ1.11 | len: 250 | use: O | rpt: 1)
        :param conjunction: Coded values for HL7 tables (id: TQ1.12 | len: 10 | use: C | rpt: 1)
        :param occurrence_duration: Composite Quantity with Units (id: TQ1.13 | len: 20 | use: O | rpt: 1)
        :param total_occurrences: Numeric (id: TQ1.14 | len: 10 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 14
        self.set_id_tq1 = set_id_tq1
        self.quantity = quantity
        self.repeat_pattern = repeat_pattern
        self.explicit_time = explicit_time
        self.relative_time_and_units = relative_time_and_units
        self.service_duration = service_duration
        self.start_date_or_time = start_date_or_time
        self.end_date_or_time = end_date_or_time
        self.priority = priority
        self.condition_text = condition_text
        self.text_instruction = text_instruction
        self.conjunction = conjunction
        self.occurrence_duration = occurrence_duration
        self.total_occurrences = total_occurrences

    @property  # get TQ1.1
    def set_id_tq1(self) -> SI | None:
        """
        id: TQ1.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.1
        """
        return self._c_data[0][0]

    @set_id_tq1.setter  # set TQ1.1
    def set_id_tq1(self, si: SI | None):
        """
        id: TQ1.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.1
        """
        self._c_data[0] = (si,)

    @property  # get TQ1.2
    def quantity(self) -> CQ | None:
        """
        id: TQ1.2 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.2
        """
        return self._c_data[1][0]

    @quantity.setter  # set TQ1.2
    def quantity(self, cq: CQ | None):
        """
        id: TQ1.2 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.2
        """
        self._c_data[1] = (cq,)

    @property
    def repeat_pattern(self) -> tuple[RPT, ...] | tuple[None]:
        """
        id: TQ1.3 | len: 540 | use: O | rpt: *
        ---
        return_type: tuple[RPT, ...]: (Repeat Pattern, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.3
        """
        return self._c_data[2]

    @repeat_pattern.setter  # set TQ1.3
    def repeat_pattern(self, rpt: RPT | tuple[RPT] | None):
        """
        id: TQ1.3 | len: 540 | use: O | rpt: *
        ---
        param_type: RPT | tuple[RPT, ...]: (Repeat Pattern, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.3
        """
        if isinstance(rpt, tuple):
            self._c_data[2] = rpt
        else:
            self._c_data[2] = (rpt,)

    @property
    def explicit_time(self) -> tuple[TM, ...] | tuple[None]:
        """
        id: TQ1.4 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[TM, ...]: (Time, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.4
        """
        return self._c_data[3]

    @explicit_time.setter  # set TQ1.4
    def explicit_time(self, tm: TM | tuple[TM] | None):
        """
        id: TQ1.4 | len: 20 | use: O | rpt: *
        ---
        param_type: TM | tuple[TM, ...]: (Time, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.4
        """
        if isinstance(tm, tuple):
            self._c_data[3] = tm
        else:
            self._c_data[3] = (tm,)

    @property
    def relative_time_and_units(self) -> tuple[CQ, ...] | tuple[None]:
        """
        id: TQ1.5 | len: 20 | use: O | rpt: *
        ---
        return_type: tuple[CQ, ...]: (Composite Quantity with Units, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.5
        """
        return self._c_data[4]

    @relative_time_and_units.setter  # set TQ1.5
    def relative_time_and_units(self, cq: CQ | tuple[CQ] | None):
        """
        id: TQ1.5 | len: 20 | use: O | rpt: *
        ---
        param_type: CQ | tuple[CQ, ...]: (Composite Quantity with Units, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.5
        """
        if isinstance(cq, tuple):
            self._c_data[4] = cq
        else:
            self._c_data[4] = (cq,)

    @property  # get TQ1.6
    def service_duration(self) -> CQ | None:
        """
        id: TQ1.6 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.6
        """
        return self._c_data[5][0]

    @service_duration.setter  # set TQ1.6
    def service_duration(self, cq: CQ | None):
        """
        id: TQ1.6 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.6
        """
        self._c_data[5] = (cq,)

    @property  # get TQ1.7
    def start_date_or_time(self) -> TS | None:
        """
        id: TQ1.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.7
        """
        return self._c_data[6][0]

    @start_date_or_time.setter  # set TQ1.7
    def start_date_or_time(self, ts: TS | None):
        """
        id: TQ1.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.7
        """
        self._c_data[6] = (ts,)

    @property  # get TQ1.8
    def end_date_or_time(self) -> TS | None:
        """
        id: TQ1.8 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.8
        """
        return self._c_data[7][0]

    @end_date_or_time.setter  # set TQ1.8
    def end_date_or_time(self, ts: TS | None):
        """
        id: TQ1.8 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.8
        """
        self._c_data[7] = (ts,)

    @property
    def priority(self) -> tuple[ExtendedPriorityCodes, ...] | tuple[None]:
        """
        id: TQ1.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.9
        """
        return self._c_data[8]

    @priority.setter  # set TQ1.9
    def priority(
        self,
        extended_priority_codes: ExtendedPriorityCodes
        | tuple[ExtendedPriorityCodes]
        | None,
    ):
        """
        id: TQ1.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CWE | tuple[CWE, ...]: (Coded with Exceptions, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.9
        """
        if isinstance(extended_priority_codes, tuple):
            self._c_data[8] = extended_priority_codes
        else:
            self._c_data[8] = (extended_priority_codes,)

    @property  # get TQ1.10
    def condition_text(self) -> TX | None:
        """
        id: TQ1.10 | len: 250 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.10
        """
        return self._c_data[9][0]

    @condition_text.setter  # set TQ1.10
    def condition_text(self, tx: TX | None):
        """
        id: TQ1.10 | len: 250 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.10
        """
        self._c_data[9] = (tx,)

    @property  # get TQ1.11
    def text_instruction(self) -> TX | None:
        """
        id: TQ1.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.11
        """
        return self._c_data[10][0]

    @text_instruction.setter  # set TQ1.11
    def text_instruction(self, tx: TX | None):
        """
        id: TQ1.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.11
        """
        self._c_data[10] = (tx,)

    @property  # get TQ1.12
    def conjunction(self) -> RiskManagementIncidentCode | None:
        """
        id: TQ1.12 | len: 10 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.12
        """
        return self._c_data[11][0]

    @conjunction.setter  # set TQ1.12
    def conjunction(
        self, risk_management_incident_code: RiskManagementIncidentCode | None
    ):
        """
        id: TQ1.12 | len: 10 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.12
        """
        self._c_data[11] = (risk_management_incident_code,)

    @property  # get TQ1.13
    def occurrence_duration(self) -> CQ | None:
        """
        id: TQ1.13 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.13
        """
        return self._c_data[12][0]

    @occurrence_duration.setter  # set TQ1.13
    def occurrence_duration(self, cq: CQ | None):
        """
        id: TQ1.13 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.13
        """
        self._c_data[12] = (cq,)

    @property  # get TQ1.14
    def total_occurrences(self) -> NM | None:
        """
        id: TQ1.14 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.14
        """
        return self._c_data[13][0]

    @total_occurrences.setter  # set TQ1.14
    def total_occurrences(self, nm: NM | None):
        """
        id: TQ1.14 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ1.14
        """
        self._c_data[13] = (nm,)
