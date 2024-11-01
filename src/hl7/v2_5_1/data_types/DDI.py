from __future__ import annotations
from ...base import DataType
from .MO import MO
from .NM import NM


"""
DataType - DDI
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::DDI TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DDI,
    MO, NM
)

ddi = DDI(  # Daily Deductible Information - This data type specifies the detail information for the daily deductible
    delay_days=None,  # NM(...) 
    monetary_amount=mo,  # MO(...)  # Required.
    number_of_days=None,  # NM(...) 
)

-----END COMPOSITE_DATA_TYPE::DDI TEMPLATE-----
"""


class DDI(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 25
    _hl7_id = """DDI"""
    _hl7_name = """Daily Deductible Information"""
    _hl7_description = """This data type specifies the detail information for the daily deductible"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI"
    _c_length = (3, 16, 4,)
    _c_rpt = (1, 1, 1,)
    _c_usage = ("O", "R", "O",)
    _c_aliases = ("DDI.1", "DDI.2", "DDI.3",)
    _c_components = (NM, MO, NM,)
    _c_names = ("Delay Days", "Monetary Amount", "Number Of Days",)
    _c_attrs = ("delay_days", "monetary_amount", "number_of_days",)
    # fmt: on

    def __init__(
        self,
        monetary_amount: MO | tuple[MO, ...],  # DDI.2
        delay_days: NM | tuple[NM, ...] | None = None,  # DDI.1
        number_of_days: NM | tuple[NM, ...] | None = None,  # DDI.3
    ):
        """
        Daily Deductible Information - `DDI <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DDI>`_
        This data type specifies the detail information for the daily deductible.

        :param delay_days: The number of days after which the daily deductible begins (id: DDI.1 | len: 3 | use: O | rpt: 1)
        :param monetary_amount: The monetary amount of the deductible (id: DDI.2 | len: 16 | use: R | rpt: 1)
        :param number_of_days: The number of days to apply the deductible (id: DDI.3 | len: 4 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.delay_days = delay_days
        self.monetary_amount = monetary_amount
        self.number_of_days = number_of_days

    @property  # get DDI.1
    def delay_days(self) -> NM | None:
        """
        id: DDI.1 | len: 3 | use: O | rpt: 1
        ---
        The number of days after which the daily deductible begins
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI.1
        """
        return self._c_data[0][0]

    @delay_days.setter  # set DDI.1
    def delay_days(self, nm: NM | None):
        """
        id: DDI.1 | len: 3 | use: O | rpt: 1
        ---
        The number of days after which the daily deductible begins
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI.1
        """
        self._c_data[0] = (nm,)

    @property  # get DDI.2
    def monetary_amount(self) -> MO:
        """
        id: DDI.2 | len: 16 | use: R | rpt: 1
        ---
        The monetary amount of the deductible
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI.2
        """
        return self._c_data[1][0]

    @monetary_amount.setter  # set DDI.2
    def monetary_amount(self, mo: MO):
        """
        id: DDI.2 | len: 16 | use: R | rpt: 1
        ---
        The monetary amount of the deductible
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI.2
        """
        self._c_data[1] = (mo,)

    @property  # get DDI.3
    def number_of_days(self) -> NM | None:
        """
        id: DDI.3 | len: 4 | use: O | rpt: 1
        ---
        The number of days to apply the deductible. If this component is not populated, it means that the number of days is indefinite.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI.3
        """
        return self._c_data[2][0]

    @number_of_days.setter  # set DDI.3
    def number_of_days(self, nm: NM | None):
        """
        id: DDI.3 | len: 4 | use: O | rpt: 1
        ---
        The number of days to apply the deductible. If this component is not populated, it means that the number of days is indefinite.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DDI.3
        """
        self._c_data[2] = (nm,)
