from __future__ import annotations
from ...base import DataType
from .NM import NM


"""
DataType - NA
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::NA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NA,
    NM
)

na = NA(  # Numeric Array - This data type is used to represent a series (array) of numeric values
    value1=nm,  # NM(...)  # Required.
    value2=None,  # NM(...) 
    value3=None,  # NM(...) 
    value4=None,  # NM(...) 
    value5=None,  # NM(...) 
    value6=None,  # NM(...) 
    value7=None,  # NM(...) 
    value8=None,  # NM(...) 
    value9=None,  # NM(...) 
    value10=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::NA TEMPLATE-----
"""


class NA(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 65536
    _hl7_id = """NA"""
    _hl7_name = """Numeric Array"""
    _hl7_description = """This data type is used to represent a series (array) of numeric values"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA"
    _c_length = (16, 16, 16, 16, 0, 0, 0, 0, 0, 0,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_aliases = ("NA.1", "NA.2", "NA.3", "NA.4", "NA.5", "NA.6", "NA.7", "NA.8", "NA.9", "NA.10",)
    _c_components = (NM, NM, NM, NM, NM, NM, NM, NM, NM, NM,)
    _c_names = ("Value1", "Value2", "Value3", "Value4", "Value5", "Value6", "Value7", "Value8", "Value9", "Value10",)
    _c_attrs = ("value1", "value2", "value3", "value4", "value5", "value6", "value7", "value8", "value9", "value10",)
    # fmt: on

    def __init__(
        self,
        value1: NM | tuple[NM, ...],  # NA.1
        value2: NM | tuple[NM, ...] | None = None,  # NA.2
        value3: NM | tuple[NM, ...] | None = None,  # NA.3
        value4: NM | tuple[NM, ...] | None = None,  # NA.4
        value5: NM | tuple[NM, ...] | None = None,  # NA.5
        value6: NM | tuple[NM, ...] | None = None,  # NA.6
        value7: NM | tuple[NM, ...] | None = None,  # NA.7
        value8: NM | tuple[NM, ...] | None = None,  # NA.8
        value9: NM | tuple[NM, ...] | None = None,  # NA.9
        value10: NM | tuple[NM, ...] | None = None,  # NA.10
    ):
        """
                Numeric Array - `NA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NA>`_
                This data type is used to represent a series (array) of numeric values. A field of this type may contain a one-dimensional array (vector or row) of numbers. Also, by allowing the field to repeat, a two-dimensional array (table) of numbers may be transmitted using this format, with each row of the table represented as one repetition of the field. Arrays that have one or more values not present may be transmitted using this data type. "Not present" values are represented as two adjacent component delimiters. If the absent values occur at the end of a row, the trailing component delimiters may be omitted. If an entire row of a table has no values, no component delimiters are necessary (in this case, there will be two adjacent repetition delimiters).

        Example 1: vector of 8 numbers |125^34^-22^-234^569^442^-212^6|
        Example 2: 3 x 3 array of numbers  |1.2^-3.5^5.2~2.0^3.1^-6.2~3.5^7.8^-1.3|

                :param value1:  (id: NA.1 | len: 16 | use: R | rpt: 1)
                :param value2:  (id: NA.2 | len: 16 | use: O | rpt: 1)
                :param value3:  (id: NA.3 | len: 16 | use: O | rpt: 1)
                :param value4:  (id: NA.4 | len: 16 | use: O | rpt: 1)
                :param value5:  (id: NA.5 | len: 0 | use: O | rpt: 1)
                :param value6:  (id: NA.6 | len: 0 | use: O | rpt: 1)
                :param value7:  (id: NA.7 | len: 0 | use: O | rpt: 1)
                :param value8:  (id: NA.8 | len: 0 | use: O | rpt: 1)
                :param value9:  (id: NA.9 | len: 0 | use: O | rpt: 1)
                :param value10:  (id: NA.10 | len: 0 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5
        self.value6 = value6
        self.value7 = value7
        self.value8 = value8
        self.value9 = value9
        self.value10 = value10

    @property  # get NA.1
    def value1(self) -> NM:
        """
        id: NA.1 | len: 16 | use: R | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.1
        """
        return self._c_data[0][0]

    @value1.setter  # set NA.1
    def value1(self, nm: NM):
        """
        id: NA.1 | len: 16 | use: R | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.1
        """
        self._c_data[0] = (nm,)

    @property  # get NA.2
    def value2(self) -> NM | None:
        """
        id: NA.2 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.2
        """
        return self._c_data[1][0]

    @value2.setter  # set NA.2
    def value2(self, nm: NM | None):
        """
        id: NA.2 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.2
        """
        self._c_data[1] = (nm,)

    @property  # get NA.3
    def value3(self) -> NM | None:
        """
        id: NA.3 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.3
        """
        return self._c_data[2][0]

    @value3.setter  # set NA.3
    def value3(self, nm: NM | None):
        """
        id: NA.3 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.3
        """
        self._c_data[2] = (nm,)

    @property  # get NA.4
    def value4(self) -> NM | None:
        """
        id: NA.4 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.4
        """
        return self._c_data[3][0]

    @value4.setter  # set NA.4
    def value4(self, nm: NM | None):
        """
        id: NA.4 | len: 16 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.4
        """
        self._c_data[3] = (nm,)

    @property  # get NA.5
    def value5(self) -> NM | None:
        """
        id: NA.5 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.5
        """
        return self._c_data[4][0]

    @value5.setter  # set NA.5
    def value5(self, nm: NM | None):
        """
        id: NA.5 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.5
        """
        self._c_data[4] = (nm,)

    @property  # get NA.6
    def value6(self) -> NM | None:
        """
        id: NA.6 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.6
        """
        return self._c_data[5][0]

    @value6.setter  # set NA.6
    def value6(self, nm: NM | None):
        """
        id: NA.6 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.6
        """
        self._c_data[5] = (nm,)

    @property  # get NA.7
    def value7(self) -> NM | None:
        """
        id: NA.7 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.7
        """
        return self._c_data[6][0]

    @value7.setter  # set NA.7
    def value7(self, nm: NM | None):
        """
        id: NA.7 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.7
        """
        self._c_data[6] = (nm,)

    @property  # get NA.8
    def value8(self) -> NM | None:
        """
        id: NA.8 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.8
        """
        return self._c_data[7][0]

    @value8.setter  # set NA.8
    def value8(self, nm: NM | None):
        """
        id: NA.8 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.8
        """
        self._c_data[7] = (nm,)

    @property  # get NA.9
    def value9(self) -> NM | None:
        """
        id: NA.9 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.9
        """
        return self._c_data[8][0]

    @value9.setter  # set NA.9
    def value9(self, nm: NM | None):
        """
        id: NA.9 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.9
        """
        self._c_data[8] = (nm,)

    @property  # get NA.10
    def value10(self) -> NM | None:
        """
        id: NA.10 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.10
        """
        return self._c_data[9][0]

    @value10.setter  # set NA.10
    def value10(self, nm: NM | None):
        """
        id: NA.10 | len: 0 | use: O | rpt: 1
        ---
        None
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NA.10
        """
        self._c_data[9] = (nm,)
