from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.DLT import DLT
from ..data_types.TX import TX
from ..data_types.RFR import RFR
from ..data_types.NM import NM


"""
Numeric Observation - OM2
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM2 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM2,
    CE, DLT, TX, RFR, NM
)

om2 = OM2(  #  - This segment contains the attributes of observations with continuous values (including those with data types of numeric, date, or time stamp)
    sequence_number_test_or_observation_master_file=None,  # NM(...) 
    units_of_measure=None,  # CE(...) 
    range_of_decimal_precision=None,  # NM(...) 
    corresponding_si_units_of_measure=None,  # CE(...) 
    si_conversion_factor=None,  # TX(...) 
    reference=None,  # RFR(...) 
    critical_range_for_ordinal_and_continuous_observations=None,  # RFR(...) 
    absolute_range_for_ordinal_and_continuous_observations=None,  # RFR(...) 
    delta_check_criteria=None,  # DLT(...) 
    minimum_meaningful_increments=None,  # NM(...) 
)

-----END SEGMENT::OM2 TEMPLATE-----
"""


class OM2(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM2"""
    _hl7_name = """Numeric Observation"""
    _hl7_description = """This segment contains the attributes of observations with continuous values (including those with data types of numeric, date, or time stamp)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM2"
    _c_length = (4, 250, 10, 250, 60, 250, 205, 250, 250, 20,)
    _c_rpt = (1, 1, 65535, 1, 1, 65535, 65535, 1, 65535, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, CE, NM, CE, TX, RFR, RFR, RFR, DLT, NM,)
    _c_aliases = ("OM2.1", "OM2.2", "OM2.3", "OM2.4", "OM2.5", "OM2.6", "OM2.7", "OM2.8", "OM2.9", "OM2.10",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Units of Measure", "Range of Decimal Precision", "Corresponding SI Units of Measure", "SI Conversion Factor", "Reference (Normal) Range - Ordinal and Continuous Observations", "Critical Range for Ordinal and Continuous Observations", "Absolute Range for Ordinal and Continuous Observations", "Delta Check Criteria", "Minimum Meaningful Increments",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "units_of_measure", "range_of_decimal_precision", "corresponding_si_units_of_measure", "si_conversion_factor", "reference", "critical_range_for_ordinal_and_continuous_observations", "absolute_range_for_ordinal_and_continuous_observations", "delta_check_criteria", "minimum_meaningful_increments",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM | None = None,  # OM2.1
        units_of_measure: CE | None = None,  # OM2.2
        range_of_decimal_precision: NM | None = None,  # OM2.3
        corresponding_si_units_of_measure: CE | None = None,  # OM2.4
        si_conversion_factor: TX | None = None,  # OM2.5
        reference: RFR | None = None,  # OM2.6
        critical_range_for_ordinal_and_continuous_observations: RFR
        | None = None,  # OM2.7
        absolute_range_for_ordinal_and_continuous_observations: RFR
        | None = None,  # OM2.8
        delta_check_criteria: DLT | None = None,  # OM2.9
        minimum_meaningful_increments: NM | None = None,  # OM2.10
    ):
        """
        Numeric Observation - `OM2 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM2>`_
        This segment contains the attributes of observations with continuous values (including those with data types of numeric, date, or time stamp).  It can be applied to observation batteries of type A and C (see OM1-18 - Nature of Service/Test/Observation)

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM2.1 | len: 4 | use: O | rpt: 1)
        :param units_of_measure: Coded Element (id: OM2.2 | len: 250 | use: O | rpt: 1)
        :param range_of_decimal_precision: Numeric (id: OM2.3 | len: 10 | use: O | rpt: *)
        :param corresponding_si_units_of_measure: Coded Element (id: OM2.4 | len: 250 | use: O | rpt: 1)
        :param si_conversion_factor: Text Data (id: OM2.5 | len: 60 | use: O | rpt: 1)
        :param reference: Reference Range (id: OM2.6 | len: 250 | use: O | rpt: *)
        :param critical_range_for_ordinal_and_continuous_observations: Reference Range (id: OM2.7 | len: 205 | use: O | rpt: *)
        :param absolute_range_for_ordinal_and_continuous_observations: Reference Range (id: OM2.8 | len: 250 | use: O | rpt: 1)
        :param delta_check_criteria: Delta (id: OM2.9 | len: 250 | use: O | rpt: *)
        :param minimum_meaningful_increments: Numeric (id: OM2.10 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.units_of_measure = units_of_measure
        self.range_of_decimal_precision = range_of_decimal_precision
        self.corresponding_si_units_of_measure = corresponding_si_units_of_measure
        self.si_conversion_factor = si_conversion_factor
        self.reference = reference
        self.critical_range_for_ordinal_and_continuous_observations = (
            critical_range_for_ordinal_and_continuous_observations
        )
        self.absolute_range_for_ordinal_and_continuous_observations = (
            absolute_range_for_ordinal_and_continuous_observations
        )
        self.delta_check_criteria = delta_check_criteria
        self.minimum_meaningful_increments = minimum_meaningful_increments

    @property  # get OM2.1
    def sequence_number_test_or_observation_master_file(self) -> NM | None:
        """
        id: OM2.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM2.1
    def sequence_number_test_or_observation_master_file(self, nm: NM | None):
        """
        id: OM2.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.1
        """
        self._c_data[0] = (nm,)

    @property  # get OM2.2
    def units_of_measure(self) -> CE | None:
        """
        id: OM2.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.2
        """
        return self._c_data[1][0]

    @units_of_measure.setter  # set OM2.2
    def units_of_measure(self, ce: CE | None):
        """
        id: OM2.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.2
        """
        self._c_data[1] = (ce,)

    @property
    def range_of_decimal_precision(self) -> tuple[NM, ...] | tuple[None]:
        """
        id: OM2.3 | len: 10 | use: O | rpt: *
        ---
        return_type: tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.3
        """
        return self._c_data[2]

    @range_of_decimal_precision.setter  # set OM2.3
    def range_of_decimal_precision(self, nm: NM | tuple[NM] | None):
        """
        id: OM2.3 | len: 10 | use: O | rpt: *
        ---
        param_type: NM | tuple[NM, ...]: (Numeric, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.3
        """
        if isinstance(nm, tuple):
            self._c_data[2] = nm
        else:
            self._c_data[2] = (nm,)

    @property  # get OM2.4
    def corresponding_si_units_of_measure(self) -> CE | None:
        """
        id: OM2.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.4
        """
        return self._c_data[3][0]

    @corresponding_si_units_of_measure.setter  # set OM2.4
    def corresponding_si_units_of_measure(self, ce: CE | None):
        """
        id: OM2.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.4
        """
        self._c_data[3] = (ce,)

    @property  # get OM2.5
    def si_conversion_factor(self) -> TX | None:
        """
        id: OM2.5 | len: 60 | use: O | rpt: 1
        ---
        return_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.5
        """
        return self._c_data[4][0]

    @si_conversion_factor.setter  # set OM2.5
    def si_conversion_factor(self, tx: TX | None):
        """
        id: OM2.5 | len: 60 | use: O | rpt: 1
        ---
        param_type: TX: Text Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.5
        """
        self._c_data[4] = (tx,)

    @property
    def reference(self) -> tuple[RFR, ...] | tuple[None]:
        """
        id: OM2.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[RFR, ...]: (Reference Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.6
        """
        return self._c_data[5]

    @reference.setter  # set OM2.6
    def reference(self, rfr: RFR | tuple[RFR] | None):
        """
        id: OM2.6 | len: 250 | use: O | rpt: *
        ---
        param_type: RFR | tuple[RFR, ...]: (Reference Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.6
        """
        if isinstance(rfr, tuple):
            self._c_data[5] = rfr
        else:
            self._c_data[5] = (rfr,)

    @property
    def critical_range_for_ordinal_and_continuous_observations(
        self,
    ) -> tuple[RFR, ...] | tuple[None]:
        """
        id: OM2.7 | len: 205 | use: O | rpt: *
        ---
        return_type: tuple[RFR, ...]: (Reference Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.7
        """
        return self._c_data[6]

    @critical_range_for_ordinal_and_continuous_observations.setter  # set OM2.7
    def critical_range_for_ordinal_and_continuous_observations(
        self, rfr: RFR | tuple[RFR] | None
    ):
        """
        id: OM2.7 | len: 205 | use: O | rpt: *
        ---
        param_type: RFR | tuple[RFR, ...]: (Reference Range, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.7
        """
        if isinstance(rfr, tuple):
            self._c_data[6] = rfr
        else:
            self._c_data[6] = (rfr,)

    @property  # get OM2.8
    def absolute_range_for_ordinal_and_continuous_observations(self) -> RFR | None:
        """
        id: OM2.8 | len: 250 | use: O | rpt: 1
        ---
        return_type: RFR: Reference Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.8
        """
        return self._c_data[7][0]

    @absolute_range_for_ordinal_and_continuous_observations.setter  # set OM2.8
    def absolute_range_for_ordinal_and_continuous_observations(self, rfr: RFR | None):
        """
        id: OM2.8 | len: 250 | use: O | rpt: 1
        ---
        param_type: RFR: Reference Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.8
        """
        self._c_data[7] = (rfr,)

    @property
    def delta_check_criteria(self) -> tuple[DLT, ...] | tuple[None]:
        """
        id: OM2.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[DLT, ...]: (Delta, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.9
        """
        return self._c_data[8]

    @delta_check_criteria.setter  # set OM2.9
    def delta_check_criteria(self, dlt: DLT | tuple[DLT] | None):
        """
        id: OM2.9 | len: 250 | use: O | rpt: *
        ---
        param_type: DLT | tuple[DLT, ...]: (Delta, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.9
        """
        if isinstance(dlt, tuple):
            self._c_data[8] = dlt
        else:
            self._c_data[8] = (dlt,)

    @property  # get OM2.10
    def minimum_meaningful_increments(self) -> NM | None:
        """
        id: OM2.10 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.10
        """
        return self._c_data[9][0]

    @minimum_meaningful_increments.setter  # set OM2.10
    def minimum_meaningful_increments(self, nm: NM | None):
        """
        id: OM2.10 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM2.10
        """
        self._c_data[9] = (nm,)
