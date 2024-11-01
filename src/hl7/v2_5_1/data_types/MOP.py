from __future__ import annotations
from ...base import DataType
from .ID import ID
from .NM import NM
from ..tables.MoneyOrPercentageIndicator import MoneyOrPercentageIndicator
from ..tables.CurrencyCodes import CurrencyCodes


"""
DataType - MOP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::MOP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MOP,
    ID, NM
)

mop = MOP(  # Money or Percentage - This data type specifies an amount that may be either currency or a percentage
    money_or_percentage_indicator=id,  # ID(...)  # Required.
    money_or_percentage_quantity=nm,  # NM(...)  # Required.
    currency_denomination=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::MOP TEMPLATE-----
"""


class MOP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 23
    _hl7_id = """MOP"""
    _hl7_name = """Money or Percentage"""
    _hl7_description = """This data type specifies an amount that may be either currency or a percentage"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP"
    _c_length = (2, 16, 3,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("R", "R", "O",)
    _c_aliases = ("MOP.1", "MOP.2", "MOP.3",)
    _c_components = (ID, NM, ID,)
    _c_names = ("Money Or Percentage Indicator", "Money Or Percentage Quantity", "Currency Denomination",)
    _c_attrs = ("money_or_percentage_indicator", "money_or_percentage_quantity", "currency_denomination",)
    # fmt: on

    def __init__(
        self,
        money_or_percentage_indicator: MoneyOrPercentageIndicator | ID,  # MOP.1
        money_or_percentage_quantity: NM,  # MOP.2
        currency_denomination: CurrencyCodes | ID | None = None,  # MOP.3
    ):
        """
                Money or Percentage - `MOP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MOP>`_
                This data type specifies an amount that may be either currency or a percentage. It is a variation on the MO data type that is limited to currency.

        Example: USD is the ISO 4217 code for the U.S. American dollar. |AT^99.50^USD|

                :param money_or_percentage_indicator: Specifies whether the amount is currency or a percentage (id: MOP.1 | len: 2 | use: R | rpt: 1)
                :param money_or_percentage_quantity: Specifies the currency or percentage quantity (id: MOP.2 | len: 16 | use: R | rpt: 1)
                :param currency_denomination: the denomination in which the quantity is expressed where the amount is currency (id: MOP.3 | len: 3 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.money_or_percentage_indicator = money_or_percentage_indicator
        self.money_or_percentage_quantity = money_or_percentage_quantity
        self.currency_denomination = currency_denomination

    @property  # get MOP.1
    def money_or_percentage_indicator(self) -> MoneyOrPercentageIndicator:
        """
        id: MOP.1 | len: 2 | use: R | rpt: 1
        ---
        Specifies whether the amount is currency or a percentage.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP.1
        """
        return self._c_data[0][0]

    @money_or_percentage_indicator.setter  # set MOP.1
    def money_or_percentage_indicator(
        self, money_or_percentage_indicator: MoneyOrPercentageIndicator
    ):
        """
        id: MOP.1 | len: 2 | use: R | rpt: 1
        ---
        Specifies whether the amount is currency or a percentage.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP.1
        """
        self._c_data[0] = (money_or_percentage_indicator,)

    @property  # get MOP.2
    def money_or_percentage_quantity(self) -> NM:
        """
        id: MOP.2 | len: 16 | use: R | rpt: 1
        ---
        Specifies the currency or percentage quantity.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP.2
        """
        return self._c_data[1][0]

    @money_or_percentage_quantity.setter  # set MOP.2
    def money_or_percentage_quantity(self, nm: NM):
        """
        id: MOP.2 | len: 16 | use: R | rpt: 1
        ---
        Specifies the currency or percentage quantity.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP.2
        """
        self._c_data[1] = (nm,)

    @property  # get MOP.3
    def currency_denomination(self) -> CurrencyCodes | None:
        """
        id: MOP.3 | len: 3 | use: O | rpt: 1
        ---
        the denomination in which the quantity is expressed where the amount is currency. The values for the denomination component are those specified in ISO-4217. If the denomination is not specified, the context of the message or MSH-17-country code is used to determine the default.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP.3
        """
        return self._c_data[2][0]

    @currency_denomination.setter  # set MOP.3
    def currency_denomination(self, currency_codes: CurrencyCodes | None):
        """
        id: MOP.3 | len: 3 | use: O | rpt: 1
        ---
        the denomination in which the quantity is expressed where the amount is currency. The values for the denomination component are those specified in ISO-4217. If the denomination is not specified, the context of the message or MSH-17-country code is used to determine the default.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOP.3
        """
        self._c_data[2] = (currency_codes,)
