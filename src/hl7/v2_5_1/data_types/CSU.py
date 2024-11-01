from __future__ import annotations
from ...base import DataType
from .ST import ST
from .ID import ID
from .NM import NM
from ..tables.CodingSystem import CodingSystem


"""
DataType - CSU
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CSU TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CSU,
    ST, ID, NM
)

csu = CSU(  # Channel Sensitivity - This data type defines the channel sensitivity (gain) and the units in which it is measured in a waveform result
    channel_sensitivity=nm,  # NM(...)  # Required.
    unit_of_measure_identifier=None,  # ST(...) 
    unit_of_measure_description=None,  # ST(...) 
    unit_of_measure_coding_system=None,  # ID(...) 
    alternate_unit_of_measure_identifier=None,  # ST(...) 
    alternate_unit_of_measure_description=None,  # ST(...) 
    alternate_unit_of_measure_coding_system=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::CSU TEMPLATE-----
"""


class CSU(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 490
    _hl7_id = """CSU"""
    _hl7_name = """Channel Sensitivity"""
    _hl7_description = """This data type defines the channel sensitivity (gain) and the units in which it is measured in a waveform result"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU"
    _c_length = (60, 20, 199, 20, 20, 199, 20,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "C", "C", "C", "O", "O", "O",)
    _c_aliases = ("CSU.1", "CSU.2", "CSU.3", "CSU.4", "CSU.5", "CSU.6", "CSU.7",)
    _c_components = (NM, ST, ST, ID, ST, ST, ID,)
    _c_names = ("Channel Sensitivity", "Unit Of Measure Identifier", "Unit Of Measure Description", "Unit Of Measure Coding System", "Alternate Unit Of Measure Identifier", "Alternate Unit Of Measure Description", "Alternate Unit Of Measure Coding System",)
    _c_attrs = ("channel_sensitivity", "unit_of_measure_identifier", "unit_of_measure_description", "unit_of_measure_coding_system", "alternate_unit_of_measure_identifier", "alternate_unit_of_measure_description", "alternate_unit_of_measure_coding_system",)
    # fmt: on

    def __init__(
        self,
        channel_sensitivity: NM | tuple[NM, ...],  # CSU.1
        unit_of_measure_identifier: ST | tuple[ST, ...] | None = None,  # CSU.2
        unit_of_measure_description: ST | tuple[ST, ...] | None = None,  # CSU.3
        unit_of_measure_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID, ...]
        | None = None,  # CSU.4
        alternate_unit_of_measure_identifier: ST
        | tuple[ST, ...]
        | None = None,  # CSU.5
        alternate_unit_of_measure_description: ST
        | tuple[ST, ...]
        | None = None,  # CSU.6
        alternate_unit_of_measure_coding_system: CodingSystem
        | ID
        | tuple[CodingSystem | ID, ...]
        | None = None,  # CSU.7
    ):
        """
        Channel Sensitivity - `CSU <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU>`_
        This data type defines the channel sensitivity (gain) and the units in which it is measured in a waveform result.

        :param channel_sensitivity: This component transmits the nominal value that corresponds to one unit in the waveform data, that is, the effective resolution of the least significant bit of the ADC, and the polarity of the channel (id: CSU.1 | len: 60 | use: R | rpt: 1)
        :param unit_of_measure_identifier: The unit designation for the channel sensitivity (id: CSU.2 | len: 20 | use: C | rpt: 1)
        :param unit_of_measure_description: The full text name of the unit of measure identifier (id: CSU.3 | len: 199 | use: C | rpt: 1)
        :param unit_of_measure_coding_system: Specifies the designated system of units (id: CSU.4 | len: 20 | use: C | rpt: 1)
        :param alternate_unit_of_measure_identifier: An alternate units designation for the channel sensitivity (id: CSU.5 | len: 20 | use: O | rpt: 1)
        :param alternate_unit_of_measure_description: The full text name of the alternate unit of measure identifier (id: CSU.6 | len: 199 | use: O | rpt: 1)
        :param alternate_unit_of_measure_coding_system: Specifies the coding system for the alternate unit of measure (id: CSU.7 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.channel_sensitivity = channel_sensitivity
        self.unit_of_measure_identifier = unit_of_measure_identifier
        self.unit_of_measure_description = unit_of_measure_description
        self.unit_of_measure_coding_system = unit_of_measure_coding_system
        self.alternate_unit_of_measure_identifier = alternate_unit_of_measure_identifier
        self.alternate_unit_of_measure_description = (
            alternate_unit_of_measure_description
        )
        self.alternate_unit_of_measure_coding_system = (
            alternate_unit_of_measure_coding_system
        )

    @property  # get CSU.1
    def channel_sensitivity(self) -> NM:
        """
        id: CSU.1 | len: 60 | use: R | rpt: 1
        ---
        This component transmits the nominal value that corresponds to one unit in the waveform data, that is, the effective resolution of the least significant bit of the ADC, and the polarity of the channel.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.1
        """
        return self._c_data[0][0]

    @channel_sensitivity.setter  # set CSU.1
    def channel_sensitivity(self, nm: NM):
        """
        id: CSU.1 | len: 60 | use: R | rpt: 1
        ---
        This component transmits the nominal value that corresponds to one unit in the waveform data, that is, the effective resolution of the least significant bit of the ADC, and the polarity of the channel.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.1
        """
        self._c_data[0] = (nm,)

    @property  # get CSU.2
    def unit_of_measure_identifier(self) -> ST | None:
        """
        id: CSU.2 | len: 20 | use: C | rpt: 1
        ---
        The unit designation for the channel sensitivity. This field is required if the unit of measure description is not present.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.2
        """
        return self._c_data[1][0]

    @unit_of_measure_identifier.setter  # set CSU.2
    def unit_of_measure_identifier(self, st: ST | None):
        """
        id: CSU.2 | len: 20 | use: C | rpt: 1
        ---
        The unit designation for the channel sensitivity. This field is required if the unit of measure description is not present.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.2
        """
        self._c_data[1] = (st,)

    @property  # get CSU.3
    def unit_of_measure_description(self) -> ST | None:
        """
        id: CSU.3 | len: 199 | use: C | rpt: 1
        ---
        The full text name of the unit of measure identifier. This field is required if the unit of measure identifier is not present.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.3
        """
        return self._c_data[2][0]

    @unit_of_measure_description.setter  # set CSU.3
    def unit_of_measure_description(self, st: ST | None):
        """
        id: CSU.3 | len: 199 | use: C | rpt: 1
        ---
        The full text name of the unit of measure identifier. This field is required if the unit of measure identifier is not present.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.3
        """
        self._c_data[2] = (st,)

    @property  # get CSU.4
    def unit_of_measure_coding_system(self) -> CodingSystem | None:
        """
        id: CSU.4 | len: 20 | use: C | rpt: 1
        ---
        Specifies the designated system of units. Refer to HL7 table 0396 - Coding System in section 2.17.5 for suggested values. This field is required if the unit of measure identifier is present.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.4
        """
        return self._c_data[3][0]

    @unit_of_measure_coding_system.setter  # set CSU.4
    def unit_of_measure_coding_system(self, coding_system: CodingSystem | None):
        """
        id: CSU.4 | len: 20 | use: C | rpt: 1
        ---
        Specifies the designated system of units. Refer to HL7 table 0396 - Coding System in section 2.17.5 for suggested values. This field is required if the unit of measure identifier is present.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.4
        """
        self._c_data[3] = (coding_system,)

    @property  # get CSU.5
    def alternate_unit_of_measure_identifier(self) -> ST | None:
        """
        id: CSU.5 | len: 20 | use: O | rpt: 1
        ---
        An alternate units designation for the channel sensitivity.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.5
        """
        return self._c_data[4][0]

    @alternate_unit_of_measure_identifier.setter  # set CSU.5
    def alternate_unit_of_measure_identifier(self, st: ST | None):
        """
        id: CSU.5 | len: 20 | use: O | rpt: 1
        ---
        An alternate units designation for the channel sensitivity.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.5
        """
        self._c_data[4] = (st,)

    @property  # get CSU.6
    def alternate_unit_of_measure_description(self) -> ST | None:
        """
        id: CSU.6 | len: 199 | use: O | rpt: 1
        ---
        The full text name of the alternate unit of measure identifier
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.6
        """
        return self._c_data[5][0]

    @alternate_unit_of_measure_description.setter  # set CSU.6
    def alternate_unit_of_measure_description(self, st: ST | None):
        """
        id: CSU.6 | len: 199 | use: O | rpt: 1
        ---
        The full text name of the alternate unit of measure identifier
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.6
        """
        self._c_data[5] = (st,)

    @property  # get CSU.7
    def alternate_unit_of_measure_coding_system(self) -> CodingSystem | None:
        """
        id: CSU.7 | len: 20 | use: O | rpt: 1
        ---
        Specifies the coding system for the alternate unit of measure. Refer to HL7 table 0396 - Coding System in section 2.17.5 for suggested values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.7
        """
        return self._c_data[6][0]

    @alternate_unit_of_measure_coding_system.setter  # set CSU.7
    def alternate_unit_of_measure_coding_system(
        self, coding_system: CodingSystem | None
    ):
        """
        id: CSU.7 | len: 20 | use: O | rpt: 1
        ---
        Specifies the coding system for the alternate unit of measure. Refer to HL7 table 0396 - Coding System in section 2.17.5 for suggested values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CSU.7
        """
        self._c_data[6] = (coding_system,)
