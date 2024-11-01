from __future__ import annotations
from ...base import DataType
from .NR import NR
from .ID import ID
from .NM import NM
from ..tables.ComputationType import ComputationType


"""
DataType - DLT
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DLT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DLT,
    NR, ID, NM
)

dlt = DLT(  # Delta - Describes the information that controls delta check warnings
    normal_range=None,  # NR(...) 
    numeric_threshold=None,  # NM(...) 
    change_computation=None,  # ID(...) 
    days_retained=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::DLT TEMPLATE-----
"""


class DLT(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 0
    _hl7_id = """DLT"""
    _hl7_name = """Delta"""
    _hl7_description = """Describes the information that controls delta check warnings"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT"
    _c_length = (33, 4, 1, 4,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("O", "O", "O", "O",)
    _c_aliases = ("DLT.1", "DLT.2", "DLT.3", "DLT.4",)
    _c_components = (NR, NM, ID, NM,)
    _c_names = ("Normal Range", "Numeric Threshold", "Change Computation", "Days Retained",)
    _c_attrs = ("normal_range", "numeric_threshold", "change_computation", "days_retained",)
    # fmt: on

    def __init__(
        self,
        normal_range: NR | None = None,  # DLT.1
        numeric_threshold: NM | None = None,  # DLT.2
        change_computation: ComputationType | ID | None = None,  # DLT.3
        days_retained: NM | None = None,  # DLT.4
    ):
        """
        Delta - `DLT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DLT>`_
        Describes the information that controls delta check warnings.

        :param normal_range: Specifies the normal interval of the reference data (id: DLT.1 | len: 33 | use: O | rpt: 1)
        :param numeric_threshold: The numeric threshold of the change that is detected (id: DLT.2 | len: 4 | use: O | rpt: 1)
        :param change_computation: Specifies if the change is computed as a percent change or as an absolute change (id: DLT.3 | len: 1 | use: O | rpt: 1)
        :param days_retained: The length of time in days that the value is retained for computing delta checks (id: DLT.4 | len: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.normal_range = normal_range
        self.numeric_threshold = numeric_threshold
        self.change_computation = change_computation
        self.days_retained = days_retained

    @property  # get DLT.1
    def normal_range(self) -> NR | None:
        """
        id: DLT.1 | len: 33 | use: O | rpt: 1
        ---
        Specifies the normal interval of the reference data
        ---
        return_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.1
        """
        return self._c_data[0][0]

    @normal_range.setter  # set DLT.1
    def normal_range(self, nr: NR | None):
        """
        id: DLT.1 | len: 33 | use: O | rpt: 1
        ---
        Specifies the normal interval of the reference data
        ---
        param_type: NR: Numeric Range
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.1
        """
        self._c_data[0] = (nr,)

    @property  # get DLT.2
    def numeric_threshold(self) -> NM | None:
        """
        id: DLT.2 | len: 4 | use: O | rpt: 1
        ---
        The numeric threshold of the change that is detected.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.2
        """
        return self._c_data[1][0]

    @numeric_threshold.setter  # set DLT.2
    def numeric_threshold(self, nm: NM | None):
        """
        id: DLT.2 | len: 4 | use: O | rpt: 1
        ---
        The numeric threshold of the change that is detected.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.2
        """
        self._c_data[1] = (nm,)

    @property  # get DLT.3
    def change_computation(self) -> ComputationType | None:
        """
        id: DLT.3 | len: 1 | use: O | rpt: 1
        ---
        Specifies if the change is computed as a percent change or as an absolute change. Refer to HL7 Table 0523 - Computation type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.3
        """
        return self._c_data[2][0]

    @change_computation.setter  # set DLT.3
    def change_computation(self, computation_type: ComputationType | None):
        """
        id: DLT.3 | len: 1 | use: O | rpt: 1
        ---
        Specifies if the change is computed as a percent change or as an absolute change. Refer to HL7 Table 0523 - Computation type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.3
        """
        self._c_data[2] = (computation_type,)

    @property  # get DLT.4
    def days_retained(self) -> NM | None:
        """
        id: DLT.4 | len: 4 | use: O | rpt: 1
        ---
        The length of time in days that the value is retained for computing delta checks.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.4
        """
        return self._c_data[3][0]

    @days_retained.setter  # set DLT.4
    def days_retained(self, nm: NM | None):
        """
        id: DLT.4 | len: 4 | use: O | rpt: 1
        ---
        The length of time in days that the value is retained for computing delta checks.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DLT.4
        """
        self._c_data[3] = (nm,)
