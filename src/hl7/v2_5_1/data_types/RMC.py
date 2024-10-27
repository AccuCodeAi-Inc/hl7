from __future__ import annotations
from ...base import DataType
from .NM import NM
from .MOP import MOP
from .IS import IS
from ..tables.RoomType import RoomType
from ..tables.AmountType import AmountType


"""
DataType - RMC
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::RMC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RMC,
    NM, MOP, IS
)

rmc = RMC(  # Room Coverage - This data type specifies insurance coverage detail for a room
    room_type=_is,  # IS(...)  # Required.
    amount_type=None,  # IS(...) 
    coverage_amount=None,  # NM(...) 
    money_or_percentage=mop,  # MOP(...)  # Required.
)

-----END COMPOSITE_DATA_TYPE::RMC TEMPLATE-----
"""


class RMC(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 82
    _hl7_id = """RMC"""
    _hl7_name = """Room Coverage"""
    _hl7_description = """This data type specifies insurance coverage detail for a room"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC"
    _c_length = (20, 20, 16, 23,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("R", "O", "B", "R",)
    _c_aliases = ("RMC.1", "RMC.2", "RMC.3", "RMC.4",)
    _c_components = (IS, IS, NM, MOP,)
    _c_names = ("Room Type", "Amount Type", "Coverage Amount", "Money Or Percentage",)
    _c_attrs = ("room_type", "amount_type", "coverage_amount", "money_or_percentage",)
    # fmt: on

    def __init__(
        self,
        room_type: RoomType | IS,  # RMC.1
        money_or_percentage: MOP,  # RMC.4
        amount_type: AmountType | IS | None = None,  # RMC.2
        coverage_amount: NM | None = None,  # RMC.3
    ):
        """
        Room Coverage - `RMC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RMC>`_
        This data type specifies insurance coverage detail for a room.

        :param room_type: Specifies the room type (id: RMC.1 | len: 20 | use: R | rpt: 1)
        :param amount_type: Specifies amount quantity type (id: RMC.2 | len: 20 | use: O | rpt: 1)
        :param coverage_amount: Specifies amount covered by the insurance as a currency or percentage quantity (id: RMC.3 | len: 16 | use: B | rpt: 1)
        :param money_or_percentage: specifies an amount that may be either currency or a percentage (id: RMC.4 | len: 23 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.room_type = room_type
        self.amount_type = amount_type
        self.coverage_amount = coverage_amount
        self.money_or_percentage = money_or_percentage

    @property  # get RMC.1
    def room_type(self) -> RoomType:
        """
        id: RMC.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the room type.
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.1
        """
        return self._c_data[0][0]

    @room_type.setter  # set RMC.1
    def room_type(self, room_type: RoomType):
        """
        id: RMC.1 | len: 20 | use: R | rpt: 1
        ---
        Specifies the room type.
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.1
        """
        self._c_data[0] = (room_type,)

    @property  # get RMC.2
    def amount_type(self) -> AmountType | None:
        """
        id: RMC.2 | len: 20 | use: O | rpt: 1
        ---
        Specifies amount quantity type
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.2
        """
        return self._c_data[1][0]

    @amount_type.setter  # set RMC.2
    def amount_type(self, amount_type: AmountType | None):
        """
        id: RMC.2 | len: 20 | use: O | rpt: 1
        ---
        Specifies amount quantity type
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.2
        """
        self._c_data[1] = (amount_type,)

    @property  # get RMC.3
    def coverage_amount(self) -> NM | None:
        """
                id: RMC.3 | len: 16 | use: B | rpt: 1
                ---
                Specifies amount covered by the insurance as a currency or percentage quantity.

        Retained for backward compatibility only as of v 2.5. Refer to Money or Percentage.
                ---
                return_type: NM: Numeric
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.3
        """
        return self._c_data[2][0]

    @coverage_amount.setter  # set RMC.3
    def coverage_amount(self, nm: NM | None):
        """
                id: RMC.3 | len: 16 | use: B | rpt: 1
                ---
                Specifies amount covered by the insurance as a currency or percentage quantity.

        Retained for backward compatibility only as of v 2.5. Refer to Money or Percentage.
                ---
                param_type: NM: Numeric
                ---
                https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.3
        """
        self._c_data[2] = (nm,)

    @property  # get RMC.4
    def money_or_percentage(self) -> MOP:
        """
        id: RMC.4 | len: 23 | use: R | rpt: 1
        ---
        specifies an amount that may be either currency or a percentage.
        ---
        return_type: MOP: Money or Percentage
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.4
        """
        return self._c_data[3][0]

    @money_or_percentage.setter  # set RMC.4
    def money_or_percentage(self, mop: MOP):
        """
        id: RMC.4 | len: 23 | use: R | rpt: 1
        ---
        specifies an amount that may be either currency or a percentage.
        ---
        param_type: MOP: Money or Percentage
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RMC.4
        """
        self._c_data[3] = (mop,)
