from __future__ import annotations
from ...base import DataType
from .CE import CE
from .ID import ID
from .NM import NM
from .MO import MO
from ..tables.CpRangeType import CpRangeType
from ..tables.PriceType import PriceType


"""
DataType - CP
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CP TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CP,
    CE, ID, NM, MO
)

cp = CP(  # Composite Price - Example: |100
    price=mo,  # MO(...)  # Required.
    price_type=None,  # ID(...) 
    from_value=None,  # NM(...) 
    to_value=None,  # NM(...) 
    range_units=None,  # CE(...) 
    range_type=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::CP TEMPLATE-----
"""


class CP(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 543
    _hl7_id = """CP"""
    _hl7_name = """Composite Price"""
    _hl7_description = """Example: |100"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP"
    _c_length = (20, 2, 16, 16, 483, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "O", "O",)
    _c_aliases = ("CP.1", "CP.2", "CP.3", "CP.4", "CP.5", "CP.6",)
    _c_components = (MO, ID, NM, NM, CE, ID,)
    _c_names = ("Price", "Price Type", "From Value", "To Value", "Range Units", "Range Type",)
    _c_attrs = ("price", "price_type", "from_value", "to_value", "range_units", "range_type",)
    # fmt: on

    def __init__(
        self,
        price: MO | tuple[MO, ...],  # CP.1
        price_type: PriceType | ID | tuple[PriceType | ID, ...] | None = None,  # CP.2
        from_value: NM | tuple[NM, ...] | None = None,  # CP.3
        to_value: NM | tuple[NM, ...] | None = None,  # CP.4
        range_units: CE | tuple[CE, ...] | None = None,  # CP.5
        range_type: CpRangeType
        | ID
        | tuple[CpRangeType | ID, ...]
        | None = None,  # CP.6
    ):
        """
        Composite Price - `CP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CP>`_
        Example: |100.00&USD^UP^0^9^min^P~50.00&USD^UP^10^59^min^P~10.00&USD^UP^60^999^P~ 50.00&USD^AP~200.00&USD^PF ~80.00&USD^DC|

        :param price: The only required component; usually containing a decimal point (id: CP.1 | len: 20 | use: R | rpt: 1)
        :param price_type: A coded value, data type ID (id: CP.2 | len: 2 | use: O | rpt: 1)
        :param from_value: Each is a NM data type; together they specify the range (id: CP.3 | len: 16 | use: O | rpt: 1)
        :param to_value: See <from value> above (id: CP.4 | len: 16 | use: O | rpt: 1)
        :param range_units: A coded value, data type CE, defined by the standard table of units for either time or quantity (see for example, the tables in Section 7 (id: CP.5 | len: 483 | use: O | rpt: 1)
        :param range_type: Refer to HL7 Table 0298 - CP range type for valid values (id: CP.6 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.price = price
        self.price_type = price_type
        self.from_value = from_value
        self.to_value = to_value
        self.range_units = range_units
        self.range_type = range_type

    @property  # get CP.1
    def price(self) -> MO:
        """
        id: CP.1 | len: 20 | use: R | rpt: 1
        ---
        The only required component; usually containing a decimal point. Note that each component of the MO data type (Section 2.A.41, "MO - money") is a subcomponent here.
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.1
        """
        return self._c_data[0][0]

    @price.setter  # set CP.1
    def price(self, mo: MO):
        """
        id: CP.1 | len: 20 | use: R | rpt: 1
        ---
        The only required component; usually containing a decimal point. Note that each component of the MO data type (Section 2.A.41, "MO - money") is a subcomponent here.
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.1
        """
        self._c_data[0] = (mo,)

    @property  # get CP.2
    def price_type(self) -> PriceType | None:
        """
        id: CP.2 | len: 2 | use: O | rpt: 1
        ---
        A coded value, data type ID. Refer to HL7 Table 0205 - Price type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.2
        """
        return self._c_data[1][0]

    @price_type.setter  # set CP.2
    def price_type(self, price_type: PriceType | None):
        """
        id: CP.2 | len: 2 | use: O | rpt: 1
        ---
        A coded value, data type ID. Refer to HL7 Table 0205 - Price type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.2
        """
        self._c_data[1] = (price_type,)

    @property  # get CP.3
    def from_value(self) -> NM | None:
        """
        id: CP.3 | len: 16 | use: O | rpt: 1
        ---
        Each is a NM data type; together they specify the "range". The range can be defined as either time or quantity. For example, the range can indicate that the first 10 minutes of the procedure has one price. Another repetition of the data type can use the range to specify that the following 10 to 60 minutes of the procedure is charged at another price per; a final repetition can specify that the final 60 to N minutes of the procedure at a third price.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.3
        """
        return self._c_data[2][0]

    @from_value.setter  # set CP.3
    def from_value(self, nm: NM | None):
        """
        id: CP.3 | len: 16 | use: O | rpt: 1
        ---
        Each is a NM data type; together they specify the "range". The range can be defined as either time or quantity. For example, the range can indicate that the first 10 minutes of the procedure has one price. Another repetition of the data type can use the range to specify that the following 10 to 60 minutes of the procedure is charged at another price per; a final repetition can specify that the final 60 to N minutes of the procedure at a third price.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.3
        """
        self._c_data[2] = (nm,)

    @property  # get CP.4
    def to_value(self) -> NM | None:
        """
        id: CP.4 | len: 16 | use: O | rpt: 1
        ---
        See <from value> above.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.4
        """
        return self._c_data[3][0]

    @to_value.setter  # set CP.4
    def to_value(self, nm: NM | None):
        """
        id: CP.4 | len: 16 | use: O | rpt: 1
        ---
        See <from value> above.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.4
        """
        self._c_data[3] = (nm,)

    @property  # get CP.5
    def range_units(self) -> CE | None:
        """
        id: CP.5 | len: 483 | use: O | rpt: 1
        ---
        A coded value, data type CE, defined by the standard table of units for either time or quantity (see for example, the tables in Section 7.1.4, "Coding schemes"). This describes the units associated with the range, e.g., seconds, minutes, hours, days, quantity (i.e., count); it is required if <from value> and <to value> are present.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.5
        """
        return self._c_data[4][0]

    @range_units.setter  # set CP.5
    def range_units(self, ce: CE | None):
        """
        id: CP.5 | len: 483 | use: O | rpt: 1
        ---
        A coded value, data type CE, defined by the standard table of units for either time or quantity (see for example, the tables in Section 7.1.4, "Coding schemes"). This describes the units associated with the range, e.g., seconds, minutes, hours, days, quantity (i.e., count); it is required if <from value> and <to value> are present.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.5
        """
        self._c_data[4] = (ce,)

    @property  # get CP.6
    def range_type(self) -> CpRangeType | None:
        """
        id: CP.6 | len: 1 | use: O | rpt: 1
        ---
        Refer to HL7 Table 0298 - CP range type for valid values.
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.6
        """
        return self._c_data[5][0]

    @range_type.setter  # set CP.6
    def range_type(self, cp_range_type: CpRangeType | None):
        """
        id: CP.6 | len: 1 | use: O | rpt: 1
        ---
        Refer to HL7 Table 0298 - CP range type for valid values.
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CP.6
        """
        self._c_data[5] = (cp_range_type,)
