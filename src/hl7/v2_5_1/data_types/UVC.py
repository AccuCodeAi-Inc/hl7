from __future__ import annotations
from ...base import DataType
from .MO import MO
from .CNE import CNE
from ..tables.ValueCode import ValueCode


"""
DataType - UVC
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::UVC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    UVC,
    MO, CNE
)

uvc = UVC(  # UB Value Code and Amount - A code structure to relate amounts or values to identified data elements necessary to process this claim as qualified by the payer organization
    value_code=cne,  # CNE(...)  # Required.
    value_amount=None,  # MO(...) 
)

-----END COMPOSITE_DATA_TYPE::UVC TEMPLATE-----
"""


class UVC(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 41
    _hl7_id = """UVC"""
    _hl7_name = """UB Value Code and Amount"""
    _hl7_description = """A code structure to relate amounts or values to identified data elements necessary to process this claim as qualified by the payer organization"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UVC"
    _c_length = (20, 20,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("UVC.1", "UVC.2",)
    _c_components = (CNE, MO,)
    _c_names = ("Value Code", "Value Amount",)
    _c_attrs = ("value_code", "value_amount",)
    # fmt: on

    def __init__(
        self,
        value_code: ValueCode | CNE,  # UVC.1
        value_amount: MO | None = None,  # UVC.2
    ):
        """
        UB Value Code and Amount - `UVC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UVC>`_
        A code structure to relate amounts or values to identified data elements necessary to process this claim as qualified by the payer organization.

        :param value_code: Specifies the National Uniform Billing Committee (NUBC) code itself (id: UVC.1 | len: 20 | use: R | rpt: 1)
        :param value_amount: Specifies the numeric amount when needed to pair with the value (id: UVC.2 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.value_code = value_code
        self.value_amount = value_amount

    @property  # get UVC.1
    def value_code(self) -> CNE:
        """
        id: UVC.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the National Uniform Billing Committee (NUBC) code itself.
        ---
        return_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UVC.1
        """
        return self._c_data[0][0]

    @value_code.setter  # set UVC.1
    def value_code(self, cne: CNE):
        """
        id: UVC.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the National Uniform Billing Committee (NUBC) code itself.
        ---
        param_type: CNE: Coded with No Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UVC.1
        """
        self._c_data[0] = (cne,)

    @property  # get UVC.2
    def value_amount(self) -> MO | None:
        """
        id: UVC.2 | len: 20 | use: O | rpt: 1
        ---
        Specifies the numeric amount when needed to pair with the value.
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UVC.2
        """
        return self._c_data[1][0]

    @value_amount.setter  # set UVC.2
    def value_amount(self, mo: MO | None):
        """
        id: UVC.2 | len: 20 | use: O | rpt: 1
        ---
        Specifies the numeric amount when needed to pair with the value.
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/UVC.2
        """
        self._c_data[1] = (mo,)
