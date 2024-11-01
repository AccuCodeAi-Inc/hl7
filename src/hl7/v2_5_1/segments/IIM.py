from __future__ import annotations
from ...base import HL7Segment
from ..data_types.MO import MO
from ..data_types.TS import TS
from ..data_types.NM import NM
from ..data_types.CWE import CWE
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..tables.ProcedureCode import ProcedureCode
from ..tables.ProcedureCodeModifier import ProcedureCodeModifier


"""
Inventory Item Master - IIM
HL7 Version: 2.5.1

-----BEGIN SEGMENT::IIM TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    IIM,
    MO, TS, NM, CWE, ST, CE
)

iim = IIM(  #  - The Inventory Item Master segment (IIM) contains information about the stock of product that can be used to fulfill an ordered test/service
    primary_key_value_iim=cwe,  # CWE(...)  # Required.
    service_item_code=cwe,  # CWE(...)  # Required.
    inventory_lot_number=None,  # ST(...) 
    inventory_expiration_date=None,  # TS(...) 
    inventory_manufacturer_name=None,  # CWE(...) 
    inventory_location=None,  # CWE(...) 
    inventory_received_date=None,  # TS(...) 
    inventory_received_quantity=None,  # NM(...) 
    inventory_received_quantity_unit=None,  # CWE(...) 
    inventory_received_item_cost=None,  # MO(...) 
    inventory_on_hand_date=None,  # TS(...) 
    inventory_on_hand_quantity=None,  # NM(...) 
    inventory_on_hand_quantity_unit=None,  # CWE(...) 
    procedure_code=None,  # CE(...) 
    procedure_code_modifier=None,  # CE(...) 
)

-----END SEGMENT::IIM TEMPLATE-----
"""


class IIM(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """IIM"""
    _hl7_name = """Inventory Item Master"""
    _hl7_description = """The Inventory Item Master segment (IIM) contains information about the stock of product that can be used to fulfill an ordered test/service"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IIM"
    _c_length = (250, 250, 250, 26, 250, 250, 26, 12, 250, 12, 26, 12, 250, 250, 250,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CWE, CWE, ST, TS, CWE, CWE, TS, NM, CWE, MO, TS, NM, CWE, CE, CE,)
    _c_aliases = ("IIM.1", "IIM.2", "IIM.3", "IIM.4", "IIM.5", "IIM.6", "IIM.7", "IIM.8", "IIM.9", "IIM.10", "IIM.11", "IIM.12", "IIM.13", "IIM.14", "IIM.15",)
    _c_names = ("Primary Key Value - IIM", "Service Item Code", "Inventory Lot Number", "Inventory Expiration Date", "Inventory Manufacturer Name", "Inventory Location", "Inventory Received Date", "Inventory Received Quantity", "Inventory Received Quantity Unit", "Inventory Received Item Cost", "Inventory On Hand Date", "Inventory On Hand Quantity", "Inventory On Hand Quantity Unit", "Procedure Code", "Procedure Code Modifier",)
    _c_attrs = ("primary_key_value_iim", "service_item_code", "inventory_lot_number", "inventory_expiration_date", "inventory_manufacturer_name", "inventory_location", "inventory_received_date", "inventory_received_quantity", "inventory_received_quantity_unit", "inventory_received_item_cost", "inventory_on_hand_date", "inventory_on_hand_quantity", "inventory_on_hand_quantity_unit", "procedure_code", "procedure_code_modifier",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_iim: CWE | tuple[CWE],  # IIM.1
        service_item_code: CWE | tuple[CWE],  # IIM.2
        inventory_lot_number: ST | tuple[ST] | None = None,  # IIM.3
        inventory_expiration_date: TS | tuple[TS] | None = None,  # IIM.4
        inventory_manufacturer_name: CWE | tuple[CWE] | None = None,  # IIM.5
        inventory_location: CWE | tuple[CWE] | None = None,  # IIM.6
        inventory_received_date: TS | tuple[TS] | None = None,  # IIM.7
        inventory_received_quantity: NM | tuple[NM] | None = None,  # IIM.8
        inventory_received_quantity_unit: CWE | tuple[CWE] | None = None,  # IIM.9
        inventory_received_item_cost: MO | tuple[MO] | None = None,  # IIM.10
        inventory_on_hand_date: TS | tuple[TS] | None = None,  # IIM.11
        inventory_on_hand_quantity: NM | tuple[NM] | None = None,  # IIM.12
        inventory_on_hand_quantity_unit: CWE | tuple[CWE] | None = None,  # IIM.13
        procedure_code: ProcedureCode
        | CE
        | tuple[ProcedureCode | CE]
        | None = None,  # IIM.14
        procedure_code_modifier: ProcedureCodeModifier
        | CE
        | tuple[ProcedureCodeModifier | CE]
        | None = None,  # IIM.15
    ):
        """
                Inventory Item Master - `IIM <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/IIM>`_
                The Inventory Item Master segment (IIM) contains information about the stock of product that can be used to fulfill an ordered test/service. All of the fields in this segment describe the test/service and other basic attributes pertaining to Service Item defined within an Other Observation/Service Item master file. This segment is related to centrally stocked or supply management concerns.

        Note:  We recognize that the M15 Inventory Item Master File trigger event and the IIM inventory item master segment is a limited implementation.  There is a comprehensive Materials Management message in development for inclusion in the next release.  For further information contact the Scheduling and Logistics TC.  This will be coordinated with the Control/Query TC and the Orders and Observations TC.

                :param primary_key_value_iim: Coded with Exceptions (id: IIM.1 | len: 250 | use: R | rpt: 1)
                :param service_item_code: Coded with Exceptions (id: IIM.2 | len: 250 | use: R | rpt: 1)
                :param inventory_lot_number: String Data (id: IIM.3 | len: 250 | use: O | rpt: 1)
                :param inventory_expiration_date: Time Stamp (id: IIM.4 | len: 26 | use: O | rpt: 1)
                :param inventory_manufacturer_name: Coded with Exceptions (id: IIM.5 | len: 250 | use: O | rpt: 1)
                :param inventory_location: Coded with Exceptions (id: IIM.6 | len: 250 | use: O | rpt: 1)
                :param inventory_received_date: Time Stamp (id: IIM.7 | len: 26 | use: O | rpt: 1)
                :param inventory_received_quantity: Numeric (id: IIM.8 | len: 12 | use: O | rpt: 1)
                :param inventory_received_quantity_unit: Coded with Exceptions (id: IIM.9 | len: 250 | use: O | rpt: 1)
                :param inventory_received_item_cost: Money (id: IIM.10 | len: 12 | use: O | rpt: 1)
                :param inventory_on_hand_date: Time Stamp (id: IIM.11 | len: 26 | use: O | rpt: 1)
                :param inventory_on_hand_quantity: Numeric (id: IIM.12 | len: 12 | use: O | rpt: 1)
                :param inventory_on_hand_quantity_unit: Coded with Exceptions (id: IIM.13 | len: 250 | use: O | rpt: 1)
                :param procedure_code: Coded Element (id: IIM.14 | len: 250 | use: O | rpt: 1)
                :param procedure_code_modifier: Coded Element (id: IIM.15 | len: 250 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 15
        self.primary_key_value_iim = primary_key_value_iim
        self.service_item_code = service_item_code
        self.inventory_lot_number = inventory_lot_number
        self.inventory_expiration_date = inventory_expiration_date
        self.inventory_manufacturer_name = inventory_manufacturer_name
        self.inventory_location = inventory_location
        self.inventory_received_date = inventory_received_date
        self.inventory_received_quantity = inventory_received_quantity
        self.inventory_received_quantity_unit = inventory_received_quantity_unit
        self.inventory_received_item_cost = inventory_received_item_cost
        self.inventory_on_hand_date = inventory_on_hand_date
        self.inventory_on_hand_quantity = inventory_on_hand_quantity
        self.inventory_on_hand_quantity_unit = inventory_on_hand_quantity_unit
        self.procedure_code = procedure_code
        self.procedure_code_modifier = procedure_code_modifier

    @property  # get IIM.1
    def primary_key_value_iim(self) -> CWE:
        """
        id: IIM.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.1
        """
        return self._c_data[0][0]

    @primary_key_value_iim.setter  # set IIM.1
    def primary_key_value_iim(self, cwe: CWE):
        """
        id: IIM.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.1
        """
        self._c_data[0] = (cwe,)

    @property  # get IIM.2
    def service_item_code(self) -> CWE:
        """
        id: IIM.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.2
        """
        return self._c_data[1][0]

    @service_item_code.setter  # set IIM.2
    def service_item_code(self, cwe: CWE):
        """
        id: IIM.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.2
        """
        self._c_data[1] = (cwe,)

    @property  # get IIM.3
    def inventory_lot_number(self) -> ST | None:
        """
        id: IIM.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.3
        """
        return self._c_data[2][0]

    @inventory_lot_number.setter  # set IIM.3
    def inventory_lot_number(self, st: ST | None):
        """
        id: IIM.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.3
        """
        self._c_data[2] = (st,)

    @property  # get IIM.4
    def inventory_expiration_date(self) -> TS | None:
        """
        id: IIM.4 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.4
        """
        return self._c_data[3][0]

    @inventory_expiration_date.setter  # set IIM.4
    def inventory_expiration_date(self, ts: TS | None):
        """
        id: IIM.4 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.4
        """
        self._c_data[3] = (ts,)

    @property  # get IIM.5
    def inventory_manufacturer_name(self) -> CWE | None:
        """
        id: IIM.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.5
        """
        return self._c_data[4][0]

    @inventory_manufacturer_name.setter  # set IIM.5
    def inventory_manufacturer_name(self, cwe: CWE | None):
        """
        id: IIM.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.5
        """
        self._c_data[4] = (cwe,)

    @property  # get IIM.6
    def inventory_location(self) -> CWE | None:
        """
        id: IIM.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.6
        """
        return self._c_data[5][0]

    @inventory_location.setter  # set IIM.6
    def inventory_location(self, cwe: CWE | None):
        """
        id: IIM.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.6
        """
        self._c_data[5] = (cwe,)

    @property  # get IIM.7
    def inventory_received_date(self) -> TS | None:
        """
        id: IIM.7 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.7
        """
        return self._c_data[6][0]

    @inventory_received_date.setter  # set IIM.7
    def inventory_received_date(self, ts: TS | None):
        """
        id: IIM.7 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.7
        """
        self._c_data[6] = (ts,)

    @property  # get IIM.8
    def inventory_received_quantity(self) -> NM | None:
        """
        id: IIM.8 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.8
        """
        return self._c_data[7][0]

    @inventory_received_quantity.setter  # set IIM.8
    def inventory_received_quantity(self, nm: NM | None):
        """
        id: IIM.8 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.8
        """
        self._c_data[7] = (nm,)

    @property  # get IIM.9
    def inventory_received_quantity_unit(self) -> CWE | None:
        """
        id: IIM.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.9
        """
        return self._c_data[8][0]

    @inventory_received_quantity_unit.setter  # set IIM.9
    def inventory_received_quantity_unit(self, cwe: CWE | None):
        """
        id: IIM.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.9
        """
        self._c_data[8] = (cwe,)

    @property  # get IIM.10
    def inventory_received_item_cost(self) -> MO | None:
        """
        id: IIM.10 | len: 12 | use: O | rpt: 1
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.10
        """
        return self._c_data[9][0]

    @inventory_received_item_cost.setter  # set IIM.10
    def inventory_received_item_cost(self, mo: MO | None):
        """
        id: IIM.10 | len: 12 | use: O | rpt: 1
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.10
        """
        self._c_data[9] = (mo,)

    @property  # get IIM.11
    def inventory_on_hand_date(self) -> TS | None:
        """
        id: IIM.11 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.11
        """
        return self._c_data[10][0]

    @inventory_on_hand_date.setter  # set IIM.11
    def inventory_on_hand_date(self, ts: TS | None):
        """
        id: IIM.11 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.11
        """
        self._c_data[10] = (ts,)

    @property  # get IIM.12
    def inventory_on_hand_quantity(self) -> NM | None:
        """
        id: IIM.12 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.12
        """
        return self._c_data[11][0]

    @inventory_on_hand_quantity.setter  # set IIM.12
    def inventory_on_hand_quantity(self, nm: NM | None):
        """
        id: IIM.12 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.12
        """
        self._c_data[11] = (nm,)

    @property  # get IIM.13
    def inventory_on_hand_quantity_unit(self) -> CWE | None:
        """
        id: IIM.13 | len: 250 | use: O | rpt: 1
        ---
        return_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.13
        """
        return self._c_data[12][0]

    @inventory_on_hand_quantity_unit.setter  # set IIM.13
    def inventory_on_hand_quantity_unit(self, cwe: CWE | None):
        """
        id: IIM.13 | len: 250 | use: O | rpt: 1
        ---
        param_type: CWE: Coded with Exceptions
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.13
        """
        self._c_data[12] = (cwe,)

    @property  # get IIM.14
    def procedure_code(self) -> ProcedureCode | None:
        """
        id: IIM.14 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.14
        """
        return self._c_data[13][0]

    @procedure_code.setter  # set IIM.14
    def procedure_code(self, procedure_code: ProcedureCode | None):
        """
        id: IIM.14 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.14
        """
        self._c_data[13] = (procedure_code,)

    @property
    def procedure_code_modifier(
        self,
    ) -> tuple[ProcedureCodeModifier, ...] | tuple[None]:
        """
        id: IIM.15 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.15
        """
        return self._c_data[14]

    @procedure_code_modifier.setter  # set IIM.15
    def procedure_code_modifier(
        self,
        procedure_code_modifier: ProcedureCodeModifier
        | tuple[ProcedureCodeModifier]
        | None,
    ):
        """
        id: IIM.15 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/IIM.15
        """
        if isinstance(procedure_code_modifier, tuple):
            self._c_data[14] = procedure_code_modifier
        else:
            self._c_data[14] = (procedure_code_modifier,)
