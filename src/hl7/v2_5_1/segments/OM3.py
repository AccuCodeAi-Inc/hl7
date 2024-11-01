from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..tables.ValueType import ValueType


"""
Categorical Service/Test/Observation - OM3
HL7 Version: 2.5.1

-----BEGIN SEGMENT::OM3 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    OM3,
    CE, ID, NM
)

om3 = OM3(  #  - This segment applies to free text and other non-numeric data types
    sequence_number_test_or_observation_master_file=None,  # NM(...) 
    preferred_coding_system=None,  # CE(...) 
    valid_coded_answers=None,  # CE(...) 
    normal_text_or_codes_for_categorical_observations=None,  # CE(...) 
    abnormal_text_or_codes_for_categorical_observations=None,  # CE(...) 
    critical_text_or_codes_for_categorical_observations=None,  # CE(...) 
    value_type=None,  # ID(...) 
)

-----END SEGMENT::OM3 TEMPLATE-----
"""


class OM3(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """OM3"""
    _hl7_name = """Categorical Service/Test/Observation"""
    _hl7_description = """This segment applies to free text and other non-numeric data types"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM3"
    _c_length = (4, 250, 250, 250, 250, 250, 2,)
    _c_rpt = (1, 1, 1, 65535, 65535, 65535, 1,)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O",)
    _c_components = (NM, CE, CE, CE, CE, CE, ID,)
    _c_aliases = ("OM3.1", "OM3.2", "OM3.3", "OM3.4", "OM3.5", "OM3.6", "OM3.7",)
    _c_names = ("Sequence Number - Test/Observation Master File", "Preferred Coding System", "Valid Coded 'Answers'", "Normal Text/Codes for Categorical Observations", "Abnormal Text/Codes for Categorical Observations", "Critical Text/Codes for Categorical Observations", "Value Type",)
    _c_attrs = ("sequence_number_test_or_observation_master_file", "preferred_coding_system", "valid_coded_answers", "normal_text_or_codes_for_categorical_observations", "abnormal_text_or_codes_for_categorical_observations", "critical_text_or_codes_for_categorical_observations", "value_type",)
    # fmt: on

    def __init__(
        self,
        sequence_number_test_or_observation_master_file: NM | None = None,  # OM3.1
        preferred_coding_system: CE | None = None,  # OM3.2
        valid_coded_answers: CE | None = None,  # OM3.3
        normal_text_or_codes_for_categorical_observations: CE | None = None,  # OM3.4
        abnormal_text_or_codes_for_categorical_observations: CE | None = None,  # OM3.5
        critical_text_or_codes_for_categorical_observations: CE | None = None,  # OM3.6
        value_type: ValueType | ID | None = None,  # OM3.7
    ):
        """
        Categorical Service/Test/Observation - `OM3 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OM3>`_
        This segment applies to free text and other non-numeric data types.

        :param sequence_number_test_or_observation_master_file: Numeric (id: OM3.1 | len: 4 | use: O | rpt: 1)
        :param preferred_coding_system: Coded Element (id: OM3.2 | len: 250 | use: O | rpt: 1)
        :param valid_coded_answers: Coded Element (id: OM3.3 | len: 250 | use: O | rpt: 1)
        :param normal_text_or_codes_for_categorical_observations: Coded Element (id: OM3.4 | len: 250 | use: O | rpt: *)
        :param abnormal_text_or_codes_for_categorical_observations: Coded Element (id: OM3.5 | len: 250 | use: O | rpt: *)
        :param critical_text_or_codes_for_categorical_observations: Coded Element (id: OM3.6 | len: 250 | use: O | rpt: *)
        :param value_type: Coded values for HL7 tables (id: OM3.7 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.sequence_number_test_or_observation_master_file = (
            sequence_number_test_or_observation_master_file
        )
        self.preferred_coding_system = preferred_coding_system
        self.valid_coded_answers = valid_coded_answers
        self.normal_text_or_codes_for_categorical_observations = (
            normal_text_or_codes_for_categorical_observations
        )
        self.abnormal_text_or_codes_for_categorical_observations = (
            abnormal_text_or_codes_for_categorical_observations
        )
        self.critical_text_or_codes_for_categorical_observations = (
            critical_text_or_codes_for_categorical_observations
        )
        self.value_type = value_type

    @property  # get OM3.1
    def sequence_number_test_or_observation_master_file(self) -> NM | None:
        """
        id: OM3.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.1
        """
        return self._c_data[0][0]

    @sequence_number_test_or_observation_master_file.setter  # set OM3.1
    def sequence_number_test_or_observation_master_file(self, nm: NM | None):
        """
        id: OM3.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.1
        """
        self._c_data[0] = (nm,)

    @property  # get OM3.2
    def preferred_coding_system(self) -> CE | None:
        """
        id: OM3.2 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.2
        """
        return self._c_data[1][0]

    @preferred_coding_system.setter  # set OM3.2
    def preferred_coding_system(self, ce: CE | None):
        """
        id: OM3.2 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.2
        """
        self._c_data[1] = (ce,)

    @property  # get OM3.3
    def valid_coded_answers(self) -> CE | None:
        """
        id: OM3.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.3
        """
        return self._c_data[2][0]

    @valid_coded_answers.setter  # set OM3.3
    def valid_coded_answers(self, ce: CE | None):
        """
        id: OM3.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.3
        """
        self._c_data[2] = (ce,)

    @property
    def normal_text_or_codes_for_categorical_observations(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM3.4 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.4
        """
        return self._c_data[3]

    @normal_text_or_codes_for_categorical_observations.setter  # set OM3.4
    def normal_text_or_codes_for_categorical_observations(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: OM3.4 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.4
        """
        if isinstance(ce, tuple):
            self._c_data[3] = ce
        else:
            self._c_data[3] = (ce,)

    @property
    def abnormal_text_or_codes_for_categorical_observations(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM3.5 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.5
        """
        return self._c_data[4]

    @abnormal_text_or_codes_for_categorical_observations.setter  # set OM3.5
    def abnormal_text_or_codes_for_categorical_observations(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: OM3.5 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.5
        """
        if isinstance(ce, tuple):
            self._c_data[4] = ce
        else:
            self._c_data[4] = (ce,)

    @property
    def critical_text_or_codes_for_categorical_observations(
        self,
    ) -> tuple[CE, ...] | tuple[None]:
        """
        id: OM3.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.6
        """
        return self._c_data[5]

    @critical_text_or_codes_for_categorical_observations.setter  # set OM3.6
    def critical_text_or_codes_for_categorical_observations(
        self, ce: CE | tuple[CE] | None
    ):
        """
        id: OM3.6 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.6
        """
        if isinstance(ce, tuple):
            self._c_data[5] = ce
        else:
            self._c_data[5] = (ce,)

    @property  # get OM3.7
    def value_type(self) -> ValueType | None:
        """
        id: OM3.7 | len: 2 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.7
        """
        return self._c_data[6][0]

    @value_type.setter  # set OM3.7
    def value_type(self, value_type: ValueType | None):
        """
        id: OM3.7 | len: 2 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/OM3.7
        """
        self._c_data[6] = (value_type,)
