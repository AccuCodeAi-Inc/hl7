from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..data_types.IS import IS
from ..data_types.CX import CX
from ..data_types.ID import ID
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..tables.ActiveOrInactive import ActiveOrInactive
from ..tables.TransactionCode import TransactionCode
from ..tables.ProcedureCode import ProcedureCode
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.InventoryNumber import InventoryNumber
from ..tables.Override import Override


"""
Charge Description Master - CDM
HL7 Version: 2.5.1

-----BEGIN SEGMENT::CDM TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    CDM,
    CE, XON, IS, CX, ID, NM, ST
)

cdm = CDM(  #  - The CDM segment contains the fields for identifying anything which is charged to patient accounts, including procedures, services, supplies
    primary_key_value_cdm=ce,  # CE(...)  # Required.
    charge_code_alias=None,  # CE(...) 
    charge_description_short=st,  # ST(...)  # Required.
    charge_description_long=None,  # ST(...) 
    description_override_indicator=None,  # IS(...) 
    exploding_charges=None,  # CE(...) 
    procedure_code=None,  # CE(...) 
    active_or_inactive_flag=None,  # ID(...) 
    inventory_number=None,  # CE(...) 
    resource_load=None,  # NM(...) 
    contract_number=None,  # CX(...) 
    contract_organization=None,  # XON(...) 
    room_fee_indicator=None,  # ID(...) 
)

-----END SEGMENT::CDM TEMPLATE-----
"""


class CDM(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """CDM"""
    _hl7_name = """Charge Description Master"""
    _hl7_description = """The CDM segment contains the fields for identifying anything which is charged to patient accounts, including procedures, services, supplies"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CDM"
    _c_length = (250, 250, 20, 250, 1, 250, 250, 1, 250, 12, 250, 250, 1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 65535, 1, 65535, 1, 65535, 65535, 1,)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, CE, ST, ST, IS, CE, CE, ID, CE, NM, CX, XON, ID,)
    _c_aliases = ("CDM.1", "CDM.2", "CDM.3", "CDM.4", "CDM.5", "CDM.6", "CDM.7", "CDM.8", "CDM.9", "CDM.10", "CDM.11", "CDM.12", "CDM.13",)
    _c_names = ("Primary Key Value - CDM", "Charge Code Alias", "Charge Description Short", "Charge Description Long", "Description Override Indicator", "Exploding Charges", "Procedure Code", "Active/Inactive Flag", "Inventory Number", "Resource Load", "Contract Number", "Contract Organization", "Room Fee Indicator",)
    _c_attrs = ("primary_key_value_cdm", "charge_code_alias", "charge_description_short", "charge_description_long", "description_override_indicator", "exploding_charges", "procedure_code", "active_or_inactive_flag", "inventory_number", "resource_load", "contract_number", "contract_organization", "room_fee_indicator",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_cdm: TransactionCode | CE,  # CDM.1
        charge_description_short: ST,  # CDM.3
        charge_code_alias: CE | None = None,  # CDM.2
        charge_description_long: ST | None = None,  # CDM.4
        description_override_indicator: Override | IS | None = None,  # CDM.5
        exploding_charges: CE | None = None,  # CDM.6
        procedure_code: ProcedureCode | CE | None = None,  # CDM.7
        active_or_inactive_flag: ActiveOrInactive | ID | None = None,  # CDM.8
        inventory_number: InventoryNumber | CE | None = None,  # CDM.9
        resource_load: NM | None = None,  # CDM.10
        contract_number: CX | None = None,  # CDM.11
        contract_organization: XON | None = None,  # CDM.12
        room_fee_indicator: YesOrNoIndicator | ID | None = None,  # CDM.13
    ):
        """
                Charge Description Master - `CDM <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CDM>`_
                The CDM segment contains the fields for identifying anything which is charged to patient accounts, including procedures, services, supplies.  It is intended to be used to maintain a list of valid chargeable utilization items.  Its purpose is to keep billing codes synchronized between HIS, Patient Accounting, and other departmental systems.  It is not intended to completely support materials management, inventory, or complex pricing structures for which additional complex fields would be required.  Given an identifying charge code, the associated fields in the charge description master file will provide basic pricing and billing data.  All the additional information necessary for patient accounting systems to do billing and claims is not intended to be included in this segment; those should be part of insurance or billing profile tables.

        The CDM segment contains the fields which, for one chargeable item, remain the same across facilities, departments, and patient types.  The following PRC segment contains the fields which, for the same chargeable item, vary depending upon facility or department or patient type.

                :param primary_key_value_cdm: Coded Element (id: CDM.1 | len: 250 | use: R | rpt: 1)
                :param charge_code_alias: Coded Element (id: CDM.2 | len: 250 | use: O | rpt: *)
                :param charge_description_short: String Data (id: CDM.3 | len: 20 | use: R | rpt: 1)
                :param charge_description_long: String Data (id: CDM.4 | len: 250 | use: O | rpt: 1)
                :param description_override_indicator: Coded value for user-defined tables (id: CDM.5 | len: 1 | use: O | rpt: 1)
                :param exploding_charges: Coded Element (id: CDM.6 | len: 250 | use: O | rpt: *)
                :param procedure_code: Coded Element (id: CDM.7 | len: 250 | use: O | rpt: *)
                :param active_or_inactive_flag: Coded values for HL7 tables (id: CDM.8 | len: 1 | use: O | rpt: 1)
                :param inventory_number: Coded Element (id: CDM.9 | len: 250 | use: O | rpt: *)
                :param resource_load: Numeric (id: CDM.10 | len: 12 | use: O | rpt: 1)
                :param contract_number: Extended Composite ID with Check Digit (id: CDM.11 | len: 250 | use: O | rpt: *)
                :param contract_organization: Extended Composite Name and Identification Number for Organizations (id: CDM.12 | len: 250 | use: O | rpt: *)
                :param room_fee_indicator: Coded values for HL7 tables (id: CDM.13 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 13
        self.primary_key_value_cdm = primary_key_value_cdm
        self.charge_code_alias = charge_code_alias
        self.charge_description_short = charge_description_short
        self.charge_description_long = charge_description_long
        self.description_override_indicator = description_override_indicator
        self.exploding_charges = exploding_charges
        self.procedure_code = procedure_code
        self.active_or_inactive_flag = active_or_inactive_flag
        self.inventory_number = inventory_number
        self.resource_load = resource_load
        self.contract_number = contract_number
        self.contract_organization = contract_organization
        self.room_fee_indicator = room_fee_indicator

    @property  # get CDM.1
    def primary_key_value_cdm(self) -> TransactionCode:
        """
        id: CDM.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.1
        """
        return self._c_data[0][0]

    @primary_key_value_cdm.setter  # set CDM.1
    def primary_key_value_cdm(self, transaction_code: TransactionCode):
        """
        id: CDM.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.1
        """
        self._c_data[0] = (transaction_code,)

    @property
    def charge_code_alias(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: CDM.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.2
        """
        return self._c_data[1]

    @charge_code_alias.setter  # set CDM.2
    def charge_code_alias(self, ce: CE | tuple[CE] | None):
        """
        id: CDM.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.2
        """
        if isinstance(ce, tuple):
            self._c_data[1] = ce
        else:
            self._c_data[1] = (ce,)

    @property  # get CDM.3
    def charge_description_short(self) -> ST:
        """
        id: CDM.3 | len: 20 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.3
        """
        return self._c_data[2][0]

    @charge_description_short.setter  # set CDM.3
    def charge_description_short(self, st: ST):
        """
        id: CDM.3 | len: 20 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.3
        """
        self._c_data[2] = (st,)

    @property  # get CDM.4
    def charge_description_long(self) -> ST | None:
        """
        id: CDM.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.4
        """
        return self._c_data[3][0]

    @charge_description_long.setter  # set CDM.4
    def charge_description_long(self, st: ST | None):
        """
        id: CDM.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.4
        """
        self._c_data[3] = (st,)

    @property  # get CDM.5
    def description_override_indicator(self) -> Override | None:
        """
        id: CDM.5 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.5
        """
        return self._c_data[4][0]

    @description_override_indicator.setter  # set CDM.5
    def description_override_indicator(self, override: Override | None):
        """
        id: CDM.5 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.5
        """
        self._c_data[4] = (override,)

    @property
    def exploding_charges(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: CDM.6 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.6
        """
        return self._c_data[5]

    @exploding_charges.setter  # set CDM.6
    def exploding_charges(self, ce: CE | tuple[CE] | None):
        """
        id: CDM.6 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.6
        """
        if isinstance(ce, tuple):
            self._c_data[5] = ce
        else:
            self._c_data[5] = (ce,)

    @property
    def procedure_code(self) -> tuple[ProcedureCode, ...] | tuple[None]:
        """
        id: CDM.7 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.7
        """
        return self._c_data[6]

    @procedure_code.setter  # set CDM.7
    def procedure_code(
        self, procedure_code: ProcedureCode | tuple[ProcedureCode] | None
    ):
        """
        id: CDM.7 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.7
        """
        if isinstance(procedure_code, tuple):
            self._c_data[6] = procedure_code
        else:
            self._c_data[6] = (procedure_code,)

    @property  # get CDM.8
    def active_or_inactive_flag(self) -> ActiveOrInactive | None:
        """
        id: CDM.8 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.8
        """
        return self._c_data[7][0]

    @active_or_inactive_flag.setter  # set CDM.8
    def active_or_inactive_flag(self, active_or_inactive: ActiveOrInactive | None):
        """
        id: CDM.8 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.8
        """
        self._c_data[7] = (active_or_inactive,)

    @property
    def inventory_number(self) -> tuple[InventoryNumber, ...] | tuple[None]:
        """
        id: CDM.9 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.9
        """
        return self._c_data[8]

    @inventory_number.setter  # set CDM.9
    def inventory_number(
        self, inventory_number: InventoryNumber | tuple[InventoryNumber] | None
    ):
        """
        id: CDM.9 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.9
        """
        if isinstance(inventory_number, tuple):
            self._c_data[8] = inventory_number
        else:
            self._c_data[8] = (inventory_number,)

    @property  # get CDM.10
    def resource_load(self) -> NM | None:
        """
        id: CDM.10 | len: 12 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.10
        """
        return self._c_data[9][0]

    @resource_load.setter  # set CDM.10
    def resource_load(self, nm: NM | None):
        """
        id: CDM.10 | len: 12 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.10
        """
        self._c_data[9] = (nm,)

    @property
    def contract_number(self) -> tuple[CX, ...] | tuple[None]:
        """
        id: CDM.11 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.11
        """
        return self._c_data[10]

    @contract_number.setter  # set CDM.11
    def contract_number(self, cx: CX | tuple[CX] | None):
        """
        id: CDM.11 | len: 250 | use: O | rpt: *
        ---
        param_type: CX | tuple[CX, ...]: (Extended Composite ID with Check Digit, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.11
        """
        if isinstance(cx, tuple):
            self._c_data[10] = cx
        else:
            self._c_data[10] = (cx,)

    @property
    def contract_organization(self) -> tuple[XON, ...] | tuple[None]:
        """
        id: CDM.12 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.12
        """
        return self._c_data[11]

    @contract_organization.setter  # set CDM.12
    def contract_organization(self, xon: XON | tuple[XON] | None):
        """
        id: CDM.12 | len: 250 | use: O | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.12
        """
        if isinstance(xon, tuple):
            self._c_data[11] = xon
        else:
            self._c_data[11] = (xon,)

    @property  # get CDM.13
    def room_fee_indicator(self) -> YesOrNoIndicator | None:
        """
        id: CDM.13 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.13
        """
        return self._c_data[12][0]

    @room_fee_indicator.setter  # set CDM.13
    def room_fee_indicator(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: CDM.13 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/CDM.13
        """
        self._c_data[12] = (yes_or_no_indicator,)
