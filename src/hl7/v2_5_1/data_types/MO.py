from __future__ import annotations
from ...base import DataType
from .ID import ID
from .NM import NM
from ..tables.CurrencyCodes import CurrencyCodes


"""
DataType - MO
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::MO TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MO,
    ID, NM
)

mo = MO(  # Money - This data type specifies an amount of money and the denomination in which it is expressed
    quantity=None,  # NM(...) 
    denomination=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::MO TEMPLATE-----
"""


class MO(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 20
    _hl7_id = """MO"""
    _hl7_name = """Money"""
    _hl7_description = """This data type specifies an amount of money and the denomination in which it is expressed"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MO"
    _c_length = (16, 3,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("MO.1", "MO.2",)
    _c_components = (NM, ID,)
    _c_names = ("Quantity", "Denomination",)
    _c_attrs = ("quantity", "denomination",)
    # fmt: on

    def __init__(
        self,
        quantity: NM | tuple[NM, ...] | None = None,  # MO.1
        denomination: CurrencyCodes
        | ID
        | tuple[CurrencyCodes | ID, ...]
        | None = None,  # MO.2
    ):
        """
                Money - `MO <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MO>`_
                This data type specifies an amount of money and the denomination in which it is expressed.

        Example: |99.50^USD|

                :param quantity: The first component is a quantity (id: MO.1 | len: 16 | use: O | rpt: 1)
                :param denomination: The second component is the denomination in which the quantity is expressed (id: MO.2 | len: 3 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.quantity = quantity
        self.denomination = denomination

    @property  # get MO.1
    def quantity(self) -> NM | None:
        """
        id: MO.1 | len: 16 | use: O | rpt: 1
        ---
        The first component is a quantity.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MO.1
        """
        return self._c_data[0][0]

    @quantity.setter  # set MO.1
    def quantity(self, nm: NM | None):
        """
        id: MO.1 | len: 16 | use: O | rpt: 1
        ---
        The first component is a quantity.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MO.1
        """
        self._c_data[0] = (nm,)

    @property  # get MO.2
    def denomination(self) -> CurrencyCodes | None:
        """
        id: MO.2 | len: 3 | use: O | rpt: 1
        ---
        The second component is the denomination in which the quantity is expressed. The values for the denomination component are those specified in ISO-4217. If the denomination is not specified, MSH-17-country code is used to determine the default.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MO.2
        """
        return self._c_data[1][0]

    @denomination.setter  # set MO.2
    def denomination(self, currency_codes: CurrencyCodes | None):
        """
        id: MO.2 | len: 3 | use: O | rpt: 1
        ---
        The second component is the denomination in which the quantity is expressed. The values for the denomination component are those specified in ISO-4217. If the denomination is not specified, MSH-17-country code is used to determine the default.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MO.2
        """
        self._c_data[1] = (currency_codes,)
