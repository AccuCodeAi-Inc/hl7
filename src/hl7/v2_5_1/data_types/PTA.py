from __future__ import annotations
from ...base import DataType
from .NM import NM
from .MOP import MOP
from .IS import IS
from ..tables.PolicyType import PolicyType
from ..tables.AmountClass import AmountClass


"""
DataType - PTA
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::PTA TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PTA,
    NM, MOP, IS
)

pta = PTA(  # Policy Type and Amount - This data type specifies the policy type and amount covered by the insurance
    policy_type=_is,  # IS(...)  # Required.
    amount_class=None,  # IS(...) 
    money_or_percentage_quantity=None,  # NM(...) 
    money_or_percentage=mop,  # MOP(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::PTA TEMPLATE-----
"""


class PTA(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 56
    _hl7_id = """PTA"""
    _hl7_name = """Policy Type and Amount"""
    _hl7_description = """This data type specifies the policy type and amount covered by the insurance"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA"
    _c_length = (5, 9, 16, 23,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "O", "B", "R",)
    _c_aliases = ("PTA.1", "PTA.2", "PTA.3", "PTA.4",)
    _c_components = (IS, IS, NM, MOP,)
    _c_names = ("Policy Type", "Amount Class", "Money Or Percentage Quantity", "Money Or Percentage",)
    _c_attrs = ("policy_type", "amount_class", "money_or_percentage_quantity", "money_or_percentage",)
    # fmt: on

    def __init__(
        self,
        policy_type: PolicyType | IS,  # PTA.1
        money_or_percentage: MOP,  # PTA.4
        amount_class: AmountClass | IS | None = None,  # PTA.2
        money_or_percentage_quantity: NM | None = None,  # PTA.3
    ):
        """
        Policy Type and Amount - `PTA <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTA>`_
        This data type specifies the policy type and amount covered by the insurance.

        :param policy_type: Specifies the policy type (id: PTA.1 | len: 5 | use: R | rpt: 1)
        :param amount_class: Specifies the amount quantity class (id: PTA.2 | len: 9 | use: O | rpt: 1)
        :param money_or_percentage_quantity: Specifies the currency or percentage quantity (id: PTA.3 | len: 16 | use: B | rpt: 1)
        :param money_or_percentage: specifies an amount that may be either currency or a percentage (id: PTA.4 | len: 23 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.policy_type = policy_type
        self.amount_class = amount_class
        self.money_or_percentage_quantity = money_or_percentage_quantity
        self.money_or_percentage = money_or_percentage

    @property  # get PTA.1
    def policy_type(self) -> PolicyType:
        """
        id: PTA.1 | len: 5 | use: R | rpt: 1
        ---
        Specifies the policy type.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.1
        """
        return self._c_data[0][0]

    @policy_type.setter  # set PTA.1
    def policy_type(self, policy_type: PolicyType):
        """
        id: PTA.1 | len: 5 | use: R | rpt: 1
        ---
        Specifies the policy type.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.1
        """
        self._c_data[0] = (policy_type,)

    @property  # get PTA.2
    def amount_class(self) -> AmountClass | None:
        """
        id: PTA.2 | len: 9 | use: O | rpt: 1
        ---
        Specifies the amount quantity class.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.2
        """
        return self._c_data[1][0]

    @amount_class.setter  # set PTA.2
    def amount_class(self, amount_class: AmountClass | None):
        """
        id: PTA.2 | len: 9 | use: O | rpt: 1
        ---
        Specifies the amount quantity class.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.2
        """
        self._c_data[1] = (amount_class,)

    @property  # get PTA.3
    def money_or_percentage_quantity(self) -> NM | None:
        """
                id: PTA.3 | len: 16 | use: B | rpt: 1
                ---
                Specifies the currency or percentage quantity.

        Retained for backward compatibility only as of v 2.5. Refer to PTA.4 instead.
                ---
                return_type: NM: Numeric
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.3
        """
        return self._c_data[2][0]

    @money_or_percentage_quantity.setter  # set PTA.3
    def money_or_percentage_quantity(self, nm: NM | None):
        """
                id: PTA.3 | len: 16 | use: B | rpt: 1
                ---
                Specifies the currency or percentage quantity.

        Retained for backward compatibility only as of v 2.5. Refer to PTA.4 instead.
                ---
                param_type: NM: Numeric
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.3
        """
        self._c_data[2] = (nm,)

    @property  # get PTA.4
    def money_or_percentage(self) -> MOP:
        """
        id: PTA.4 | len: 23 | use: R | rpt: 1
        ---
        specifies an amount that may be either currency or a percentage.
        ---
        return_type: MOP: Money or Percentage
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.4
        """
        return self._c_data[3][0]

    @money_or_percentage.setter  # set PTA.4
    def money_or_percentage(self, mop: MOP):
        """
        id: PTA.4 | len: 23 | use: R | rpt: 1
        ---
        specifies an amount that may be either currency or a percentage.
        ---
        param_type: MOP: Money or Percentage
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PTA.4
        """
        self._c_data[3] = (mop,)
