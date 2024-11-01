from __future__ import annotations
from ...base import DataType
from .NM import NM
from .CE import CE


"""
DataType - CQ
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::CQ TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CQ,
    NM, CE
)

cq = CQ(  # Composite Quantity with Units - Note: CQ cannot be legally expressed when embedded within another data type
    quantity=None,  # NM(...) 
    units=None,  # CE(...) 
)

-----END COMPOSITE_DATA_TYPE::CQ TEMPLATE-----
"""


class CQ(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 500
    _hl7_id = """CQ"""
    _hl7_name = """Composite Quantity with Units"""
    _hl7_description = """Note: CQ cannot be legally expressed when embedded within another data type"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CQ"
    _c_length = (16, 483,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("CQ.1", "CQ.2",)
    _c_components = (NM, CE,)
    _c_names = ("Quantity", "Units",)
    _c_attrs = ("quantity", "units",)
    # fmt: on

    def __init__(
        self,
        quantity: NM | tuple[NM] | None = None,  # CQ.1
        units: CE | tuple[CE] | None = None,  # CQ.2
    ):
        """
                Composite Quantity with Units - `CQ <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CQ>`_
                Note: CQ cannot be legally expressed when embedded within another data type. Its use is constrained to a segment field.

        Examples:
        |123.7^kg|  kilograms is an ISO unit
        |150^lb&&ANSI+| weight in pounds is a customary US unit defined within ANSI+.

                :param quantity: This component specifies the numeric quantity or amount of an entity (id: CQ.1 | len: 16 | use: O | rpt: 1)
                :param units: This component species the units in which the quantity is expressed (id: CQ.2 | len: 483 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.quantity = quantity
        self.units = units

    @property  # get CQ.1
    def quantity(self) -> NM | None:
        """
        id: CQ.1 | len: 16 | use: O | rpt: 1
        ---
        This component specifies the numeric quantity or amount of an entity.
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CQ.1
        """
        return self._c_data[0][0]

    @quantity.setter  # set CQ.1
    def quantity(self, nm: NM | None):
        """
        id: CQ.1 | len: 16 | use: O | rpt: 1
        ---
        This component specifies the numeric quantity or amount of an entity.
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CQ.1
        """
        self._c_data[0] = (nm,)

    @property  # get CQ.2
    def units(self) -> CE | None:
        """
        id: CQ.2 | len: 483 | use: O | rpt: 1
        ---
        This component species the units in which the quantity is expressed. Field-by-field, default units may be defined within the specifications. When the quantity is measured in the default units, the units need not be transmitted. If the quantity is recorded in units different from the default, the units must be transmitted.
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CQ.2
        """
        return self._c_data[1][0]

    @units.setter  # set CQ.2
    def units(self, ce: CE | None):
        """
        id: CQ.2 | len: 483 | use: O | rpt: 1
        ---
        This component species the units in which the quantity is expressed. Field-by-field, default units may be defined within the specifications. When the quantity is measured in the default units, the units need not be transmitted. If the quantity is recorded in units different from the default, the units must be transmitted.
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CQ.2
        """
        self._c_data[1] = (ce,)
