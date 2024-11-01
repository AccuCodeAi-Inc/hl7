from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.CQ import CQ
from ..tables.BloodProductCode import BloodProductCode


"""
Blood Code - BLC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::BLC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    BLC,
    CE, CQ
)

blc = BLC(  #  - The BLC segment contains data necessary to communicate patient abstract blood information used for billing and reimbursement purposes
    blood_product_code=None,  # CE(...) 
    blood_amount=None,  # CQ(...) 
)

-----END SEGMENT::BLC TEMPLATE-----
"""


class BLC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """BLC"""
    _hl7_name = """Blood Code"""
    _hl7_description = """The BLC segment contains data necessary to communicate patient abstract blood information used for billing and reimbursement purposes"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLC"
    _c_length = (250, 267,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_components = (CE, CQ,)
    _c_aliases = ("BLC.1", "BLC.2",)
    _c_names = ("Blood Product Code", "Blood Amount",)
    _c_attrs = ("blood_product_code", "blood_amount",)
    # fmt: on

    def __init__(
        self,
        blood_product_code: BloodProductCode
        | CE
        | tuple[BloodProductCode | CE, ...]
        | None = None,  # BLC.1
        blood_amount: CQ | tuple[CQ, ...] | None = None,  # BLC.2
    ):
        """
        Blood Code - `BLC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BLC>`_
        The BLC segment contains data necessary to communicate patient abstract blood information used for billing and reimbursement purposes. This segment is repeating to report blood product codes and the associated blood units.

        :param blood_product_code: Coded Element (id: BLC.1 | len: 250 | use: O | rpt: 1)
        :param blood_amount: Composite Quantity with Units (id: BLC.2 | len: 267 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.blood_product_code = blood_product_code
        self.blood_amount = blood_amount

    @property  # get BLC.1
    def blood_product_code(self) -> BloodProductCode | None:
        """
        id: BLC.1 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLC.1
        """
        return self._c_data[0][0]

    @blood_product_code.setter  # set BLC.1
    def blood_product_code(self, blood_product_code: BloodProductCode | None):
        """
        id: BLC.1 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLC.1
        """
        self._c_data[0] = (blood_product_code,)

    @property  # get BLC.2
    def blood_amount(self) -> CQ | None:
        """
        id: BLC.2 | len: 267 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLC.2
        """
        return self._c_data[1][0]

    @blood_amount.setter  # set BLC.2
    def blood_amount(self, cq: CQ | None):
        """
        id: BLC.2 | len: 267 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/BLC.2
        """
        self._c_data[1] = (cq,)
