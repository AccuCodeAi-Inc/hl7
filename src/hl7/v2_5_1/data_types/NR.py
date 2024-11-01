from __future__ import annotations
from ...base import DataType
from .NM import NM


"""
DataType - NR
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::NR TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    NR,
    NM
)

nr = NR(  # Numeric Range - Specifies the interval between the lowest and the highest values in a series of data
    low_value=None,  # NM(...) 
    high_value=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::NR TEMPLATE-----
"""


class NR(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 33
    _hl7_id = """NR"""
    _hl7_name = """Numeric Range"""
    _hl7_description = """Specifies the interval between the lowest and the highest values in a series of data"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NR"
    _c_length = (16, 16,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("NR.1", "NR.2",)
    _c_components = (NM, NM,)
    _c_names = ("Low Value", "High Value",)
    _c_attrs = ("low_value", "high_value",)
    # fmt: on

    def __init__(
        self,
        low_value: NM | tuple[NM] | None = None,  # NR.1
        high_value: NM | tuple[NM] | None = None,  # NR.2
    ):
        """
        Numeric Range - `NR <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NR>`_
        Specifies the interval between the lowest and the highest values in a series of data. In the case where a numeric range is unbounded on one side, the component of the unbounded side is null. Whether the end points are included in the range is defined in the usage note for the field.

        :param low_value: The number specifying the lower limit or boundary of the range (id: NR.1 | len: 16 | use: O | rpt: 1)
        :param high_value: The number specifying the high limit or boundary of the range (id: NR.2 | len: 16 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.low_value = low_value
        self.high_value = high_value

    @property  # get NR.1
    def low_value(self) -> NM | None:
        """
        id: NR.1 | len: 16 | use: O | rpt: 1
        ---
        The number specifying the lower limit or boundary of the range.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NR.1
        """
        return self._c_data[0][0]

    @low_value.setter  # set NR.1
    def low_value(self, nm: NM | None):
        """
        id: NR.1 | len: 16 | use: O | rpt: 1
        ---
        The number specifying the lower limit or boundary of the range.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NR.1
        """
        self._c_data[0] = (nm,)

    @property  # get NR.2
    def high_value(self) -> NM | None:
        """
        id: NR.2 | len: 16 | use: O | rpt: 1
        ---
        The number specifying the high limit or boundary of the range.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NR.2
        """
        return self._c_data[1][0]

    @high_value.setter  # set NR.2
    def high_value(self, nm: NM | None):
        """
        id: NR.2 | len: 16 | use: O | rpt: 1
        ---
        The number specifying the high limit or boundary of the range.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/NR.2
        """
        self._c_data[1] = (nm,)
