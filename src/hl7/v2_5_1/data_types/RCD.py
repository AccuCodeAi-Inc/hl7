from __future__ import annotations
from ...base import DataType
from .ST import ST
from .ID import ID
from .NM import NM
from ..tables.DataTypes import DataTypes


"""
DataType - RCD
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::RCD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RCD,
    ST, ID, NM
)

rcd = RCD(  # Row Column Definition - This specifies the format of a column in terms of a segment field name, a data type, and a maximum length
    segment_field_name=None,  # ST(...) 
    hl7_data_type=None,  # ID(...) 
    maximum_column_width=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::RCD TEMPLATE-----
"""


class RCD(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 19
    _hl7_id = """RCD"""
    _hl7_name = """Row Column Definition"""
    _hl7_description = """This specifies the format of a column in terms of a segment field name, a data type, and a maximum length"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD"
    _c_length = (12, 3, 2,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "O", "O",)
    _c_aliases = ("RCD.1", "RCD.2", "RCD.3",)
    _c_components = (ST, ID, NM,)
    _c_names = ("Segment Field Name", "Hl7 Data Type", "Maximum Column Width",)
    _c_attrs = ("segment_field_name", "hl7_data_type", "maximum_column_width",)
    # fmt: on

    def __init__(
        self,
        segment_field_name: ST | None = None,  # RCD.1
        hl7_data_type: DataTypes | ID | None = None,  # RCD.2
        maximum_column_width: NM | None = None,  # RCD.3
    ):
        """
                Row Column Definition - `RCD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCD>`_
                This specifies the format of a column in terms of a segment field name, a data type, and a maximum length.

        Example: This defines a column containing the value of the "last name" component of PID-5, expressed as a ST data type with a maximum width of 20. |@PID.5.1^ST^20|

                :param segment_field_name: The HL7 segment field name, which identifies the field occupying the column (id: RCD.1 | len: 12 | use: O | rpt: 1)
                :param hl7_data_type: The two or three character HL7 data type (id: RCD.2 | len: 3 | use: O | rpt: 1)
                :param maximum_column_width: The maximum width of the column, as dictated by the responding system (id: RCD.3 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.segment_field_name = segment_field_name
        self.hl7_data_type = hl7_data_type
        self.maximum_column_width = maximum_column_width

    @property  # get RCD.1
    def segment_field_name(self) -> ST | None:
        """
        id: RCD.1 | len: 12 | use: O | rpt: 1
        ---
        The HL7 segment field name, which identifies the field occupying the column. Refer to Section 2.A.59.1, "Segment Field Name (ST)," for segment field name definition conventions.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD.1
        """
        return self._c_data[0][0]

    @segment_field_name.setter  # set RCD.1
    def segment_field_name(self, st: ST | None):
        """
        id: RCD.1 | len: 12 | use: O | rpt: 1
        ---
        The HL7 segment field name, which identifies the field occupying the column. Refer to Section 2.A.59.1, "Segment Field Name (ST)," for segment field name definition conventions.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD.1
        """
        self._c_data[0] = (st,)

    @property  # get RCD.2
    def hl7_data_type(self) -> DataTypes | None:
        """
        id: RCD.2 | len: 3 | use: O | rpt: 1
        ---
        The two or three character HL7 data type. Refer to HL7 Table 0440 - Data Types in section 2.16 for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD.2
        """
        return self._c_data[1][0]

    @hl7_data_type.setter  # set RCD.2
    def hl7_data_type(self, data_types: DataTypes | None):
        """
        id: RCD.2 | len: 3 | use: O | rpt: 1
        ---
        The two or three character HL7 data type. Refer to HL7 Table 0440 - Data Types in section 2.16 for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD.2
        """
        self._c_data[1] = (data_types,)

    @property  # get RCD.3
    def maximum_column_width(self) -> NM | None:
        """
        id: RCD.3 | len: 2 | use: O | rpt: 1
        ---
        The maximum width of the column, as dictated by the responding system. This may vary from the HL7-defined maximum field length.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD.3
        """
        return self._c_data[2][0]

    @maximum_column_width.setter  # set RCD.3
    def maximum_column_width(self, nm: NM | None):
        """
        id: RCD.3 | len: 2 | use: O | rpt: 1
        ---
        The maximum width of the column, as dictated by the responding system. This may vary from the HL7-defined maximum field length.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RCD.3
        """
        self._c_data[2] = (nm,)
