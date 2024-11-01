from __future__ import annotations
from ...base import DataType
from .IS import IS
from .NM import NM
from ..tables.DayType import DayType


"""
DataType - DTN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DTN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DTN,
    IS, NM
)

dtn = DTN(  # Day Type and Number - This data type specifies the type and number of days for which a certification is valid
    day_type=_is,  # IS(...)  # Required.
    number_of_days=nm,  # NM(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::DTN TEMPLATE-----
"""


class DTN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 6
    _hl7_id = """DTN"""
    _hl7_name = """Day Type and Number"""
    _hl7_description = """This data type specifies the type and number of days for which a certification is valid"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTN"
    _c_length = (2, 3,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "R",)
    _c_aliases = ("DTN.1", "DTN.2",)
    _c_components = (IS, NM,)
    _c_names = ("Day Type", "Number Of Days",)
    _c_attrs = ("day_type", "number_of_days",)
    # fmt: on

    def __init__(
        self,
        day_type: DayType | IS | tuple[DayType | IS, ...],  # DTN.1
        number_of_days: NM | tuple[NM, ...],  # DTN.2
    ):
        """
        Day Type and Number - `DTN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DTN>`_
        This data type specifies the type and number of days for which a certification is valid.

        :param day_type: Specifies whether the days are denied, pending, or approved (id: DTN.1 | len: 2 | use: R | rpt: 1)
        :param number_of_days: Specifies the number of days for which the certification is valid (id: DTN.2 | len: 3 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.day_type = day_type
        self.number_of_days = number_of_days

    @property  # get DTN.1
    def day_type(self) -> DayType:
        """
        id: DTN.1 | len: 2 | use: R | rpt: 1
        ---
        Specifies whether the days are denied, pending, or approved.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTN.1
        """
        return self._c_data[0][0]

    @day_type.setter  # set DTN.1
    def day_type(self, day_type: DayType):
        """
        id: DTN.1 | len: 2 | use: R | rpt: 1
        ---
        Specifies whether the days are denied, pending, or approved.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTN.1
        """
        self._c_data[0] = (day_type,)

    @property  # get DTN.2
    def number_of_days(self) -> NM:
        """
        id: DTN.2 | len: 3 | use: R | rpt: 1
        ---
        Specifies the number of days for which the certification is valid.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTN.2
        """
        return self._c_data[1][0]

    @number_of_days.setter  # set DTN.2
    def number_of_days(self, nm: NM):
        """
        id: DTN.2 | len: 3 | use: R | rpt: 1
        ---
        Specifies the number of days for which the certification is valid.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DTN.2
        """
        self._c_data[1] = (nm,)
