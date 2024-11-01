from __future__ import annotations
from ...base import DataType
from .ST import ST


"""
DataType - VR
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::VR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    VR,
    ST
)

vr = VR(  # Value Range - This data type contains the lower bound value and upper bound values that constitute a range
    first_data_code_value=None,  # ST(...) 
    last_data_code_value=None,  # ST(...) 
)

-----END COMPOSITE_DATA_TYPE::VR TEMPLATE-----
"""


class VR(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 0
    _hl7_id = """VR"""
    _hl7_name = """Value Range"""
    _hl7_description = """This data type contains the lower bound value and upper bound values that constitute a range"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VR"
    _c_length = (6, 6,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("VR.1", "VR.2",)
    _c_components = (ST, ST,)
    _c_names = ("First Data Code Value", "Last Data Code Value",)
    _c_attrs = ("first_data_code_value", "last_data_code_value",)
    # fmt: on

    def __init__(
        self,
        first_data_code_value: ST | tuple[ST] | None = None,  # VR.1
        last_data_code_value: ST | tuple[ST] | None = None,  # VR.2
    ):
        """
                Value Range - `VR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VR>`_
                This data type contains the lower bound value and upper bound values that constitute a range. Either or both components may be populated.

        Example 1  |+^+++|
        Example 2: Colors of the rainbow |violet^red|

                :param first_data_code_value: Specifies the lower bound value (id: VR.1 | len: 6 | use: O | rpt: 1)
                :param last_data_code_value: Specifies the upper bound value (id: VR.2 | len: 6 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.first_data_code_value = first_data_code_value
        self.last_data_code_value = last_data_code_value

    @property  # get VR.1
    def first_data_code_value(self) -> ST | None:
        """
        id: VR.1 | len: 6 | use: O | rpt: 1
        ---
        Specifies the lower bound value.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VR.1
        """
        return self._c_data[0][0]

    @first_data_code_value.setter  # set VR.1
    def first_data_code_value(self, st: ST | None):
        """
        id: VR.1 | len: 6 | use: O | rpt: 1
        ---
        Specifies the lower bound value.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VR.1
        """
        self._c_data[0] = (st,)

    @property  # get VR.2
    def last_data_code_value(self) -> ST | None:
        """
        id: VR.2 | len: 6 | use: O | rpt: 1
        ---
        Specifies the upper bound value.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VR.2
        """
        return self._c_data[1][0]

    @last_data_code_value.setter  # set VR.2
    def last_data_code_value(self, st: ST | None):
        """
        id: VR.2 | len: 6 | use: O | rpt: 1
        ---
        Specifies the upper bound value.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/VR.2
        """
        self._c_data[1] = (st,)
