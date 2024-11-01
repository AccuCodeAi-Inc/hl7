from __future__ import annotations
from ...base import DataType
from .CE import CE
from .MO import MO


"""
DataType - MOC
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::MOC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    MOC,
    CE, MO
)

moc = MOC(  # Money and Code - Transmits monetary information and the associated charge code for services performed
    monetary_amount=None,  # MO(...) 
    charge_code=None,  # CE(...) 
)

-----END COMPOSITE_DATA_TYPE::MOC TEMPLATE-----
"""


class MOC(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 504
    _hl7_id = """MOC"""
    _hl7_name = """Money and Code"""
    _hl7_description = """Transmits monetary information and the associated charge code for services performed"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOC"
    _c_length = (20, 483,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_aliases = ("MOC.1", "MOC.2",)
    _c_components = (MO, CE,)
    _c_names = ("Monetary Amount", "Charge Code",)
    _c_attrs = ("monetary_amount", "charge_code",)
    # fmt: on

    def __init__(
        self,
        monetary_amount: MO | None = None,  # MOC.1
        charge_code: CE | None = None,  # MOC.2
    ):
        """
        Money and Code - `MOC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MOC>`_
        Transmits monetary information and the associated charge code for services performed.

        :param monetary_amount: The code identifying the charge to the ordering entity for the services performed (id: MOC.1 | len: 20 | use: O | rpt: 1)
        :param charge_code:  (id: MOC.2 | len: 483 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.monetary_amount = monetary_amount
        self.charge_code = charge_code

    @property  # get MOC.1
    def monetary_amount(self) -> MO | None:
        """
        id: MOC.1 | len: 20 | use: O | rpt: 1
        ---
        The code identifying the charge to the ordering entity for the services performed.
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOC.1
        """
        return self._c_data[0][0]

    @monetary_amount.setter  # set MOC.1
    def monetary_amount(self, mo: MO | None):
        """
        id: MOC.1 | len: 20 | use: O | rpt: 1
        ---
        The code identifying the charge to the ordering entity for the services performed.
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOC.1
        """
        self._c_data[0] = (mo,)

    @property  # get MOC.2
    def charge_code(self) -> CE | None:
        """
        id: MOC.2 | len: 483 | use: O | rpt: 1
        ---
        None
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOC.2
        """
        return self._c_data[1][0]

    @charge_code.setter  # set MOC.2
    def charge_code(self, ce: CE | None):
        """
        id: MOC.2 | len: 483 | use: O | rpt: 1
        ---
        None
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/MOC.2
        """
        self._c_data[1] = (ce,)
