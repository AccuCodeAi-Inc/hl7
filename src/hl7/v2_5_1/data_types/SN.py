from __future__ import annotations
from ...base import DataType
from .NM import NM
from .ST import ST


"""
DataType - SN
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::SN TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SN,
    NM, ST
)

sn = SN(  # Structured Numeric - The structured numeric data type is used to unambiguously express numeric clinical results along with qualifications
    comparator=None,  # ST(...) 
    num1=None,  # NM(...) 
    separator_or_suffix=None,  # ST(...) 
    num2=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::SN TEMPLATE-----
"""


class SN(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 36
    _hl7_id = """SN"""
    _hl7_name = """Structured Numeric"""
    _hl7_description = """The structured numeric data type is used to unambiguously express numeric clinical results along with qualifications"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN"
    _c_length = (2, 15, 1, 15,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_aliases = ("SN.1", "SN.2", "SN.3", "SN.4",)
    _c_components = (ST, NM, ST, NM,)
    _c_names = ("Comparator", "Num1", "Separator/Suffix", "Num2",)
    _c_attrs = ("comparator", "num1", "separator_or_suffix", "num2",)
    # fmt: on

    def __init__(
        self,
        comparator: ST | tuple[ST] | None = None,  # SN.1
        num1: NM | tuple[NM] | None = None,  # SN.2
        separator_or_suffix: ST | tuple[ST] | None = None,  # SN.3
        num2: NM | tuple[NM] | None = None,  # SN.4
    ):
        """
                Structured Numeric - `SN <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SN>`_
                The structured numeric data type is used to unambiguously express numeric clinical results along with qualifications. This enables receiving systems to store the components separately, and facilitates the use of numeric database queries. The corresponding sets of values indicated with the <comparator> and <separator/suffix> components are intended to be the authoritative and complete set of values. If additional values are needed for the <comparator> and <separator/suffix> components, they should be submitted to HL7 for inclusion in the Standard.

        Examples:
        |>^100|   (greater than 100)
        |^100^-^200|  (equal to range of 100 through 200)

                :param comparator: Defined as greater than, less than, greater than or equal, less than or equal, equal, and not equal, respectively (= > or < or >= or <= or = or <> (id: SN.1 | len: 2 | use: O | rpt: 1)
                :param num1: A number (id: SN.2 | len: 15 | use: O | rpt: 1)
                :param separator_or_suffix: - or + or / or  (id: SN.3 | len: 1 | use: O | rpt: 1)
                :param num2: A number or null depending on the measurement (id: SN.4 | len: 15 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.comparator = comparator
        self.num1 = num1
        self.separator_or_suffix = separator_or_suffix
        self.num2 = num2

    @property  # get SN.1
    def comparator(self) -> ST | None:
        """
        id: SN.1 | len: 2 | use: O | rpt: 1
        ---
        Defined as greater than, less than, greater than or equal, less than or equal, equal, and not equal, respectively (= ">" or "<" or ">=" or "<=" or "=" or "<>"
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.1
        """
        return self._c_data[0][0]

    @comparator.setter  # set SN.1
    def comparator(self, st: ST | None):
        """
        id: SN.1 | len: 2 | use: O | rpt: 1
        ---
        Defined as greater than, less than, greater than or equal, less than or equal, equal, and not equal, respectively (= ">" or "<" or ">=" or "<=" or "=" or "<>"
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.1
        """
        self._c_data[0] = (st,)

    @property  # get SN.2
    def num1(self) -> NM | None:
        """
        id: SN.2 | len: 15 | use: O | rpt: 1
        ---
        A number.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.2
        """
        return self._c_data[1][0]

    @num1.setter  # set SN.2
    def num1(self, nm: NM | None):
        """
        id: SN.2 | len: 15 | use: O | rpt: 1
        ---
        A number.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.2
        """
        self._c_data[1] = (nm,)

    @property  # get SN.3
    def separator_or_suffix(self) -> ST | None:
        """
        id: SN.3 | len: 1 | use: O | rpt: 1
        ---
        "-" or "+" or "/" or "." or ":"
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.3
        """
        return self._c_data[2][0]

    @separator_or_suffix.setter  # set SN.3
    def separator_or_suffix(self, st: ST | None):
        """
        id: SN.3 | len: 1 | use: O | rpt: 1
        ---
        "-" or "+" or "/" or "." or ":"
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.3
        """
        self._c_data[2] = (st,)

    @property  # get SN.4
    def num2(self) -> NM | None:
        """
        id: SN.4 | len: 15 | use: O | rpt: 1
        ---
        A number or null depending on the measurement.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.4
        """
        return self._c_data[3][0]

    @num2.setter  # set SN.4
    def num2(self, nm: NM | None):
        """
        id: SN.4 | len: 15 | use: O | rpt: 1
        ---
        A number or null depending on the measurement.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SN.4
        """
        self._c_data[3] = (nm,)
