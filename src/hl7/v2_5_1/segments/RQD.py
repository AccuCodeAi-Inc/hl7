from __future__ import annotations
from ...base import HL7Segment
from ..data_types.SI import SI
from ..data_types.CE import CE
from ..data_types.DT import DT
from ..data_types.IS import IS
from ..data_types.NM import NM
from ..tables.ItemNaturalAccountCode import ItemNaturalAccountCode
from ..tables.DepartmentCostCenter import DepartmentCostCenter


"""
Requisition Detail - RQD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RQD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RQD,
    SI, CE, DT, IS, NM
)

rqd = RQD(  #  - RQD contains the detail for each requisitioned item
    requisition_line_number=None,  # SI(...) 
    item_code_internal=None,  # CE(...) 
    item_code_external=None,  # CE(...) 
    hospital_item_code=None,  # CE(...) 
    requisition_quantity=None,  # NM(...) 
    requisition_unit_of_measure=None,  # CE(...) 
    dept_cost_center=None,  # IS(...) 
    item_natural_account_code=None,  # IS(...) 
    deliver_to_id=None,  # CE(...) 
    date_needed=None,  # DT(...) 
)

-----END SEGMENT::RQD TEMPLATE-----
"""


class RQD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RQD"""
    _hl7_name = """Requisition Detail"""
    _hl7_description = """RQD contains the detail for each requisitioned item"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD"
    _c_length = (4, 250, 250, 250, 6, 250, 30, 30, 250, 8,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "C", "C", "C", "O", "O", "O", "O", "O", "O",)
    _c_components = (SI, CE, CE, CE, NM, CE, IS, IS, CE, DT,)
    _c_aliases = ("RQD.1", "RQD.2", "RQD.3", "RQD.4", "RQD.5", "RQD.6", "RQD.7", "RQD.8", "RQD.9", "RQD.10",)
    _c_names = ("Requisition Line Number", "Item Code - Internal", "Item Code - External", "Hospital Item Code", "Requisition Quantity", "Requisition Unit of Measure", "Dept. Cost Center", "Item Natural Account Code", "Deliver To ID", "Date Needed",)
    _c_attrs = ("requisition_line_number", "item_code_internal", "item_code_external", "hospital_item_code", "requisition_quantity", "requisition_unit_of_measure", "dept_cost_center", "item_natural_account_code", "deliver_to_id", "date_needed",)
    # fmt: on

    def __init__(
        self,
        requisition_line_number: SI | tuple[SI, ...] | None = None,  # RQD.1
        item_code_internal: CE | tuple[CE, ...] | None = None,  # RQD.2
        item_code_external: CE | tuple[CE, ...] | None = None,  # RQD.3
        hospital_item_code: CE | tuple[CE, ...] | None = None,  # RQD.4
        requisition_quantity: NM | tuple[NM, ...] | None = None,  # RQD.5
        requisition_unit_of_measure: CE | tuple[CE, ...] | None = None,  # RQD.6
        dept_cost_center: DepartmentCostCenter
        | IS
        | tuple[DepartmentCostCenter | IS, ...]
        | None = None,  # RQD.7
        item_natural_account_code: ItemNaturalAccountCode
        | IS
        | tuple[ItemNaturalAccountCode | IS, ...]
        | None = None,  # RQD.8
        deliver_to_id: CE | tuple[CE, ...] | None = None,  # RQD.9
        date_needed: DT | tuple[DT, ...] | None = None,  # RQD.10
    ):
        """
        Requisition Detail - `RQD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQD>`_
        RQD contains the detail for each requisitioned item.

        :param requisition_line_number: Sequence ID (id: RQD.1 | len: 4 | use: O | rpt: 1)
        :param item_code_internal: Coded Element (id: RQD.2 | len: 250 | use: C | rpt: 1)
        :param item_code_external: Coded Element (id: RQD.3 | len: 250 | use: C | rpt: 1)
        :param hospital_item_code: Coded Element (id: RQD.4 | len: 250 | use: C | rpt: 1)
        :param requisition_quantity: Numeric (id: RQD.5 | len: 6 | use: O | rpt: 1)
        :param requisition_unit_of_measure: Coded Element (id: RQD.6 | len: 250 | use: O | rpt: 1)
        :param dept_cost_center: Coded value for user-defined tables (id: RQD.7 | len: 30 | use: O | rpt: 1)
        :param item_natural_account_code: Coded value for user-defined tables (id: RQD.8 | len: 30 | use: O | rpt: 1)
        :param deliver_to_id: Coded Element (id: RQD.9 | len: 250 | use: O | rpt: 1)
        :param date_needed: Date (id: RQD.10 | len: 8 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.requisition_line_number = requisition_line_number
        self.item_code_internal = item_code_internal
        self.item_code_external = item_code_external
        self.hospital_item_code = hospital_item_code
        self.requisition_quantity = requisition_quantity
        self.requisition_unit_of_measure = requisition_unit_of_measure
        self.dept_cost_center = dept_cost_center
        self.item_natural_account_code = item_natural_account_code
        self.deliver_to_id = deliver_to_id
        self.date_needed = date_needed

    @property  # get RQD.1
    def requisition_line_number(self) -> SI | None:
        """
        id: RQD.1 | len: 4 | use: O | rpt: 1
        ---
        return_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.1
        """
        return self._c_data[0][0]

    @requisition_line_number.setter  # set RQD.1
    def requisition_line_number(self, si: SI | None):
        """
        id: RQD.1 | len: 4 | use: O | rpt: 1
        ---
        param_type: SI: Sequence ID
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.1
        """
        self._c_data[0] = (si,)

    @property  # get RQD.2
    def item_code_internal(self) -> CE | None:
        """
        id: RQD.2 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.2
        """
        return self._c_data[1][0]

    @item_code_internal.setter  # set RQD.2
    def item_code_internal(self, ce: CE | None):
        """
        id: RQD.2 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.2
        """
        self._c_data[1] = (ce,)

    @property  # get RQD.3
    def item_code_external(self) -> CE | None:
        """
        id: RQD.3 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.3
        """
        return self._c_data[2][0]

    @item_code_external.setter  # set RQD.3
    def item_code_external(self, ce: CE | None):
        """
        id: RQD.3 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.3
        """
        self._c_data[2] = (ce,)

    @property  # get RQD.4
    def hospital_item_code(self) -> CE | None:
        """
        id: RQD.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.4
        """
        return self._c_data[3][0]

    @hospital_item_code.setter  # set RQD.4
    def hospital_item_code(self, ce: CE | None):
        """
        id: RQD.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.4
        """
        self._c_data[3] = (ce,)

    @property  # get RQD.5
    def requisition_quantity(self) -> NM | None:
        """
        id: RQD.5 | len: 6 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.5
        """
        return self._c_data[4][0]

    @requisition_quantity.setter  # set RQD.5
    def requisition_quantity(self, nm: NM | None):
        """
        id: RQD.5 | len: 6 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.5
        """
        self._c_data[4] = (nm,)

    @property  # get RQD.6
    def requisition_unit_of_measure(self) -> CE | None:
        """
        id: RQD.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.6
        """
        return self._c_data[5][0]

    @requisition_unit_of_measure.setter  # set RQD.6
    def requisition_unit_of_measure(self, ce: CE | None):
        """
        id: RQD.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.6
        """
        self._c_data[5] = (ce,)

    @property  # get RQD.7
    def dept_cost_center(self) -> DepartmentCostCenter | None:
        """
        id: RQD.7 | len: 30 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.7
        """
        return self._c_data[6][0]

    @dept_cost_center.setter  # set RQD.7
    def dept_cost_center(self, department_cost_center: DepartmentCostCenter | None):
        """
        id: RQD.7 | len: 30 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.7
        """
        self._c_data[6] = (department_cost_center,)

    @property  # get RQD.8
    def item_natural_account_code(self) -> ItemNaturalAccountCode | None:
        """
        id: RQD.8 | len: 30 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.8
        """
        return self._c_data[7][0]

    @item_natural_account_code.setter  # set RQD.8
    def item_natural_account_code(
        self, item_natural_account_code: ItemNaturalAccountCode | None
    ):
        """
        id: RQD.8 | len: 30 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.8
        """
        self._c_data[7] = (item_natural_account_code,)

    @property  # get RQD.9
    def deliver_to_id(self) -> CE | None:
        """
        id: RQD.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.9
        """
        return self._c_data[8][0]

    @deliver_to_id.setter  # set RQD.9
    def deliver_to_id(self, ce: CE | None):
        """
        id: RQD.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.9
        """
        self._c_data[8] = (ce,)

    @property  # get RQD.10
    def date_needed(self) -> DT | None:
        """
        id: RQD.10 | len: 8 | use: O | rpt: 1
        ---
        return_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.10
        """
        return self._c_data[9][0]

    @date_needed.setter  # set RQD.10
    def date_needed(self, dt: DT | None):
        """
        id: RQD.10 | len: 8 | use: O | rpt: 1
        ---
        param_type: DT: Date
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQD.10
        """
        self._c_data[9] = (dt,)
