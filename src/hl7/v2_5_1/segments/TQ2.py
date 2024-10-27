from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.CQ import CQ
from ..data_types.SI import SI
from ..data_types.NM import NM
from ..data_types.EI import EI
from ..tables.CyclicEntryOrExitIndicator import CyclicEntryOrExitIndicator
from ..tables.SequenceOrResultsFlag import SequenceOrResultsFlag
from ..tables.SequenceConditionCode import SequenceConditionCode
from ..tables.ServiceRequestRelationship import ServiceRequestRelationship


"""
Timing/Quantity Relationship - TQ2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::TQ2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    TQ2,
    ID, CQ, SI, NM, EI
)

tq2 = TQ2(  #  - The TQ2 segment is used to form a relationship between the service request the TQ1/TQ2 segments are associated with, and other service requests
    set_id_tq2=None,  # SI(...) 
    sequence_or_results_flag=None,  # ID(...) 
    related_placer_number=None,  # EI(...) 
    related_filler_number=None,  # EI(...) 
    related_placer_group_number=None,  # EI(...) 
    sequence_condition_code=None,  # ID(...) 
    cyclic_entry_or_exit_indicator=None,  # ID(...) 
    sequence_condition_time_interval=None,  # CQ(...) 
    cyclic_group_maximum_number_of_repeats=None,  # NM(...) 
    special_service_request_relationship=None,  # ID(...) 
)

-----END SEGMENT::TQ2 TEMPLATE-----
"""


class TQ2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """TQ2"""
    _hl7_name = """Timing/Quantity Relationship"""
    _hl7_description = """The TQ2 segment is used to form a relationship between the service request the TQ1/TQ2 segments are associated with, and other service requests"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ2"
    _c_length = (4, 1, 22, 22, 22, 2, 1, 20, 10, 1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "O", "C", "C", "C", "C", "C", "O", "O", "C",)
    _c_components = (SI, ID, EI, EI, EI, ID, ID, CQ, NM, ID,)
    _c_aliases = ("TQ2.1", "TQ2.2", "TQ2.3", "TQ2.4", "TQ2.5", "TQ2.6", "TQ2.7", "TQ2.8", "TQ2.9", "TQ2.10",)
    _c_names = ("Set ID - TQ2", "Sequence/Results Flag", "Related Placer Number", "Related Filler Number", "Related Placer Group Number", "Sequence Condition Code", "Cyclic Entry/Exit Indicator", "Sequence Condition Time Interval", "Cyclic Group Maximum Number of Repeats", "Special Service Request Relationship",)
    _c_attrs = ("set_id_tq2", "sequence_or_results_flag", "related_placer_number", "related_filler_number", "related_placer_group_number", "sequence_condition_code", "cyclic_entry_or_exit_indicator", "sequence_condition_time_interval", "cyclic_group_maximum_number_of_repeats", "special_service_request_relationship",)
    # fmt: on

    def __init__(
        self,
        set_id_tq2: SI | None = None,  # TQ2.1
        sequence_or_results_flag: SequenceOrResultsFlag | ID | None = None,  # TQ2.2
        related_placer_number: EI | None = None,  # TQ2.3
        related_filler_number: EI | None = None,  # TQ2.4
        related_placer_group_number: EI | None = None,  # TQ2.5
        sequence_condition_code: SequenceConditionCode | ID | None = None,  # TQ2.6
        cyclic_entry_or_exit_indicator: CyclicEntryOrExitIndicator
        | ID
        | None = None,  # TQ2.7
        sequence_condition_time_interval: CQ | None = None,  # TQ2.8
        cyclic_group_maximum_number_of_repeats: NM | None = None,  # TQ2.9
        special_service_request_relationship: ServiceRequestRelationship
        | ID
        | None = None,  # TQ2.10
    ):
        """
        Timing/Quantity Relationship - `TQ2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ2>`_
        The TQ2 segment is used to form a relationship between the service request the TQ1/TQ2 segments are associated with, and other service requests. The TQ2 segment will link the current service request with one or more other service requests.

        :param set_id_tq2: Sequence ID (id: TQ2.1 | len: 4 | use: O | rpt: 1)
        :param sequence_or_results_flag: Coded values for HL7 tables (id: TQ2.2 | len: 1 | use: O | rpt: 1)
        :param related_placer_number: Entity Identifier (id: TQ2.3 | len: 22 | use: C | rpt: *)
        :param related_filler_number: Entity Identifier (id: TQ2.4 | len: 22 | use: C | rpt: *)
        :param related_placer_group_number: Entity Identifier (id: TQ2.5 | len: 22 | use: C | rpt: *)
        :param sequence_condition_code: Coded values for HL7 tables (id: TQ2.6 | len: 2 | use: C | rpt: 1)
        :param cyclic_entry_or_exit_indicator: Coded values for HL7 tables (id: TQ2.7 | len: 1 | use: C | rpt: 1)
        :param sequence_condition_time_interval: Composite Quantity with Units (id: TQ2.8 | len: 20 | use: O | rpt: 1)
        :param cyclic_group_maximum_number_of_repeats: Numeric (id: TQ2.9 | len: 10 | use: O | rpt: 1)
        :param special_service_request_relationship: Coded values for HL7 tables (id: TQ2.10 | len: 1 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.set_id_tq2 = set_id_tq2
        self.sequence_or_results_flag = sequence_or_results_flag
        self.related_placer_number = related_placer_number
        self.related_filler_number = related_filler_number
        self.related_placer_group_number = related_placer_group_number
        self.sequence_condition_code = sequence_condition_code
        self.cyclic_entry_or_exit_indicator = cyclic_entry_or_exit_indicator
        self.sequence_condition_time_interval = sequence_condition_time_interval
        self.cyclic_group_maximum_number_of_repeats = (
            cyclic_group_maximum_number_of_repeats
        )
        self.special_service_request_relationship = special_service_request_relationship

    @property  # get TQ2.1
    def set_id_tq2(self) -> SI | None:
        """
        id: TQ2.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.1
        """
        return self._c_data[0][0]

    @set_id_tq2.setter  # set TQ2.1
    def set_id_tq2(self, si: SI | None):
        """
        id: TQ2.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.1
        """
        self._c_data[0] = (si,)

    @property  # get TQ2.2
    def sequence_or_results_flag(self) -> SequenceOrResultsFlag | None:
        """
        id: TQ2.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.2
        """
        return self._c_data[1][0]

    @sequence_or_results_flag.setter  # set TQ2.2
    def sequence_or_results_flag(
        self, sequence_or_results_flag: SequenceOrResultsFlag | None
    ):
        """
        id: TQ2.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.2
        """
        self._c_data[1] = (sequence_or_results_flag,)

    @property
    def related_placer_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: TQ2.3 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.3
        """
        return self._c_data[2]

    @related_placer_number.setter  # set TQ2.3
    def related_placer_number(self, ei: EI | tuple[EI] | None):
        """
        id: TQ2.3 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.3
        """
        if isinstance(ei, tuple):
            self._c_data[2] = ei
        else:
            self._c_data[2] = (ei,)

    @property
    def related_filler_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: TQ2.4 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.4
        """
        return self._c_data[3]

    @related_filler_number.setter  # set TQ2.4
    def related_filler_number(self, ei: EI | tuple[EI] | None):
        """
        id: TQ2.4 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.4
        """
        if isinstance(ei, tuple):
            self._c_data[3] = ei
        else:
            self._c_data[3] = (ei,)

    @property
    def related_placer_group_number(self) -> tuple[EI, ...] | tuple[None]:
        """
        id: TQ2.5 | len: 22 | use: C | rpt: *
        ---
        return_type: tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.5
        """
        return self._c_data[4]

    @related_placer_group_number.setter  # set TQ2.5
    def related_placer_group_number(self, ei: EI | tuple[EI] | None):
        """
        id: TQ2.5 | len: 22 | use: C | rpt: *
        ---
        param_type: EI | tuple[EI, ...]: (Entity Identifier, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.5
        """
        if isinstance(ei, tuple):
            self._c_data[4] = ei
        else:
            self._c_data[4] = (ei,)

    @property  # get TQ2.6
    def sequence_condition_code(self) -> SequenceConditionCode | None:
        """
        id: TQ2.6 | len: 2 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.6
        """
        return self._c_data[5][0]

    @sequence_condition_code.setter  # set TQ2.6
    def sequence_condition_code(
        self, sequence_condition_code: SequenceConditionCode | None
    ):
        """
        id: TQ2.6 | len: 2 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.6
        """
        self._c_data[5] = (sequence_condition_code,)

    @property  # get TQ2.7
    def cyclic_entry_or_exit_indicator(self) -> CyclicEntryOrExitIndicator | None:
        """
        id: TQ2.7 | len: 1 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.7
        """
        return self._c_data[6][0]

    @cyclic_entry_or_exit_indicator.setter  # set TQ2.7
    def cyclic_entry_or_exit_indicator(
        self, cyclic_entry_or_exit_indicator: CyclicEntryOrExitIndicator | None
    ):
        """
        id: TQ2.7 | len: 1 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.7
        """
        self._c_data[6] = (cyclic_entry_or_exit_indicator,)

    @property  # get TQ2.8
    def sequence_condition_time_interval(self) -> CQ | None:
        """
        id: TQ2.8 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.8
        """
        return self._c_data[7][0]

    @sequence_condition_time_interval.setter  # set TQ2.8
    def sequence_condition_time_interval(self, cq: CQ | None):
        """
        id: TQ2.8 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.8
        """
        self._c_data[7] = (cq,)

    @property  # get TQ2.9
    def cyclic_group_maximum_number_of_repeats(self) -> NM | None:
        """
        id: TQ2.9 | len: 10 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.9
        """
        return self._c_data[8][0]

    @cyclic_group_maximum_number_of_repeats.setter  # set TQ2.9
    def cyclic_group_maximum_number_of_repeats(self, nm: NM | None):
        """
        id: TQ2.9 | len: 10 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.9
        """
        self._c_data[8] = (nm,)

    @property  # get TQ2.10
    def special_service_request_relationship(self) -> ServiceRequestRelationship | None:
        """
        id: TQ2.10 | len: 1 | use: C | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.10
        """
        return self._c_data[9][0]

    @special_service_request_relationship.setter  # set TQ2.10
    def special_service_request_relationship(
        self, service_request_relationship: ServiceRequestRelationship | None
    ):
        """
        id: TQ2.10 | len: 1 | use: C | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/TQ2.10
        """
        self._c_data[9] = (service_request_relationship,)
