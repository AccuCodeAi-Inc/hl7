from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.TS import TS
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..data_types.MO import MO
from ..data_types.NM import NM
from ..data_types.IS import IS
from ..data_types.CP import CP
from ..tables.PatientClass import PatientClass
from ..tables.BillingCategory import BillingCategory
from ..tables.ChargeOnIndicator import ChargeOnIndicator
from ..tables.TransactionCode import TransactionCode
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.Department import Department
from ..tables.Override import Override
from ..tables.FacilityId import FacilityId
from ..tables.ActiveOrInactive import ActiveOrInactive


"""
Pricing - PRC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PRC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PRC,
    ID, TS, ST, CE, MO, NM, IS, CP
)

prc = PRC(  #  - The PRC segment contains the pricing information for the preceding CDM segment’s chargeable item
    primary_key_value_prc=ce,  # CE(...)  # Required.
    facility_id_prc=None,  # CE(...) 
    department=None,  # CE(...) 
    valid_patient_classes=None,  # IS(...) 
    price=None,  # CP(...) 
    formula=None,  # ST(...) 
    minimum_quantity=None,  # NM(...) 
    maximum_quantity=None,  # NM(...) 
    minimum_price=None,  # MO(...) 
    maximum_price=None,  # MO(...) 
    effective_start_date=None,  # TS(...) 
    effective_end_date=None,  # TS(...) 
    price_override_flag=None,  # IS(...) 
    billing_category=None,  # CE(...) 
    chargeable_flag=None,  # ID(...) 
    active_or_inactive_flag=None,  # ID(...) 
    cost=None,  # MO(...) 
    charge_on_indicator=None,  # IS(...) 
)

-----END SEGMENT::PRC TEMPLATE-----
"""


class PRC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PRC"""
    _hl7_name = """Pricing"""
    _hl7_description = """The PRC segment contains the pricing information for the preceding CDM segment’s chargeable item"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRC"
    _c_length = (250, 250, 250, 1, 12, 200, 4, 4, 12, 12, 26, 26, 1, 250, 1, 1, 12, 1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535, 65535, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1,)
    _c_usage = ("R", "O", "O", "O", "C", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, CE, CE, IS, CP, ST, NM, NM, MO, MO, TS, TS, IS, CE, ID, ID, MO, IS,)
    _c_aliases = ("PRC.1", "PRC.2", "PRC.3", "PRC.4", "PRC.5", "PRC.6", "PRC.7", "PRC.8", "PRC.9", "PRC.10", "PRC.11", "PRC.12", "PRC.13", "PRC.14", "PRC.15", "PRC.16", "PRC.17", "PRC.18",)
    _c_names = ("Primary Key Value - PRC", "Facility ID - PRC", "Department", "Valid Patient Classes", "Price", "Formula", "Minimum Quantity", "Maximum Quantity", "Minimum Price", "Maximum Price", "Effective Start Date", "Effective End Date", "Price Override Flag", "Billing Category", "Chargeable Flag", "Active/Inactive Flag", "Cost", "Charge On Indicator",)
    _c_attrs = ("primary_key_value_prc", "facility_id_prc", "department", "valid_patient_classes", "price", "formula", "minimum_quantity", "maximum_quantity", "minimum_price", "maximum_price", "effective_start_date", "effective_end_date", "price_override_flag", "billing_category", "chargeable_flag", "active_or_inactive_flag", "cost", "charge_on_indicator",)
    # fmt: on

    def __init__(
        self,
        primary_key_value_prc: TransactionCode | CE,  # PRC.1
        facility_id_prc: FacilityId | CE | None = None,  # PRC.2
        department: Department | CE | None = None,  # PRC.3
        valid_patient_classes: PatientClass | IS | None = None,  # PRC.4
        price: CP | None = None,  # PRC.5
        formula: ST | None = None,  # PRC.6
        minimum_quantity: NM | None = None,  # PRC.7
        maximum_quantity: NM | None = None,  # PRC.8
        minimum_price: MO | None = None,  # PRC.9
        maximum_price: MO | None = None,  # PRC.10
        effective_start_date: TS | None = None,  # PRC.11
        effective_end_date: TS | None = None,  # PRC.12
        price_override_flag: Override | IS | None = None,  # PRC.13
        billing_category: BillingCategory | CE | None = None,  # PRC.14
        chargeable_flag: YesOrNoIndicator | ID | None = None,  # PRC.15
        active_or_inactive_flag: ActiveOrInactive | ID | None = None,  # PRC.16
        cost: MO | None = None,  # PRC.17
        charge_on_indicator: ChargeOnIndicator | IS | None = None,  # PRC.18
    ):
        """
        Pricing - `PRC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PRC>`_
        The PRC segment contains the pricing information for the preceding CDM segment’s chargeable item.  It contains the fields which, for the same chargeable item, might vary depending upon facility or department or patient type.  The preceding CDM segment contains the fields which, for one chargeable item, remain the same across facilities, departments, and patient types.

        :param primary_key_value_prc: Coded Element (id: PRC.1 | len: 250 | use: R | rpt: 1)
        :param facility_id_prc: Coded Element (id: PRC.2 | len: 250 | use: O | rpt: *)
        :param department: Coded Element (id: PRC.3 | len: 250 | use: O | rpt: *)
        :param valid_patient_classes: Coded value for user-defined tables (id: PRC.4 | len: 1 | use: O | rpt: *)
        :param price: Composite Price (id: PRC.5 | len: 12 | use: C | rpt: *)
        :param formula: String Data (id: PRC.6 | len: 200 | use: O | rpt: *)
        :param minimum_quantity: Numeric (id: PRC.7 | len: 4 | use: O | rpt: 1)
        :param maximum_quantity: Numeric (id: PRC.8 | len: 4 | use: O | rpt: 1)
        :param minimum_price: Money (id: PRC.9 | len: 12 | use: O | rpt: 1)
        :param maximum_price: Money (id: PRC.10 | len: 12 | use: O | rpt: 1)
        :param effective_start_date: Time Stamp (id: PRC.11 | len: 26 | use: O | rpt: 1)
        :param effective_end_date: Time Stamp (id: PRC.12 | len: 26 | use: O | rpt: 1)
        :param price_override_flag: Coded value for user-defined tables (id: PRC.13 | len: 1 | use: O | rpt: 1)
        :param billing_category: Coded Element (id: PRC.14 | len: 250 | use: O | rpt: *)
        :param chargeable_flag: Coded values for HL7 tables (id: PRC.15 | len: 1 | use: O | rpt: 1)
        :param active_or_inactive_flag: Coded values for HL7 tables (id: PRC.16 | len: 1 | use: O | rpt: 1)
        :param cost: Money (id: PRC.17 | len: 12 | use: O | rpt: 1)
        :param charge_on_indicator: Coded value for user-defined tables (id: PRC.18 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 18
        self.primary_key_value_prc = primary_key_value_prc
        self.facility_id_prc = facility_id_prc
        self.department = department
        self.valid_patient_classes = valid_patient_classes
        self.price = price
        self.formula = formula
        self.minimum_quantity = minimum_quantity
        self.maximum_quantity = maximum_quantity
        self.minimum_price = minimum_price
        self.maximum_price = maximum_price
        self.effective_start_date = effective_start_date
        self.effective_end_date = effective_end_date
        self.price_override_flag = price_override_flag
        self.billing_category = billing_category
        self.chargeable_flag = chargeable_flag
        self.active_or_inactive_flag = active_or_inactive_flag
        self.cost = cost
        self.charge_on_indicator = charge_on_indicator

    @property  # get PRC.1
    def primary_key_value_prc(self) -> TransactionCode:
        """
        id: PRC.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.1
        """
        return self._c_data[0][0]

    @primary_key_value_prc.setter  # set PRC.1
    def primary_key_value_prc(self, transaction_code: TransactionCode):
        """
        id: PRC.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.1
        """
        self._c_data[0] = (transaction_code,)

    @property
    def facility_id_prc(self) -> tuple[FacilityId, ...] | tuple[None]:
        """
        id: PRC.2 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.2
        """
        return self._c_data[1]

    @facility_id_prc.setter  # set PRC.2
    def facility_id_prc(self, facility_id: FacilityId | tuple[FacilityId] | None):
        """
        id: PRC.2 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.2
        """
        if isinstance(facility_id, tuple):
            self._c_data[1] = facility_id
        else:
            self._c_data[1] = (facility_id,)

    @property
    def department(self) -> tuple[Department, ...] | tuple[None]:
        """
        id: PRC.3 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.3
        """
        return self._c_data[2]

    @department.setter  # set PRC.3
    def department(self, department: Department | tuple[Department] | None):
        """
        id: PRC.3 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.3
        """
        if isinstance(department, tuple):
            self._c_data[2] = department
        else:
            self._c_data[2] = (department,)

    @property
    def valid_patient_classes(self) -> tuple[PatientClass, ...] | tuple[None]:
        """
        id: PRC.4 | len: 1 | use: O | rpt: *
        ---
        return_type: tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.4
        """
        return self._c_data[3]

    @valid_patient_classes.setter  # set PRC.4
    def valid_patient_classes(
        self, patient_class: PatientClass | tuple[PatientClass] | None
    ):
        """
        id: PRC.4 | len: 1 | use: O | rpt: *
        ---
        param_type: IS | tuple[IS, ...]: (Coded value for user-defined tables, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.4
        """
        if isinstance(patient_class, tuple):
            self._c_data[3] = patient_class
        else:
            self._c_data[3] = (patient_class,)

    @property
    def price(self) -> tuple[CP, ...] | tuple[None]:
        """
        id: PRC.5 | len: 12 | use: C | rpt: *
        ---
        return_type: tuple[CP, ...]: (Composite Price, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.5
        """
        return self._c_data[4]

    @price.setter  # set PRC.5
    def price(self, cp: CP | tuple[CP] | None):
        """
        id: PRC.5 | len: 12 | use: C | rpt: *
        ---
        param_type: CP | tuple[CP, ...]: (Composite Price, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.5
        """
        if isinstance(cp, tuple):
            self._c_data[4] = cp
        else:
            self._c_data[4] = (cp,)

    @property
    def formula(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: PRC.6 | len: 200 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.6
        """
        return self._c_data[5]

    @formula.setter  # set PRC.6
    def formula(self, st: ST | tuple[ST] | None):
        """
        id: PRC.6 | len: 200 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.6
        """
        if isinstance(st, tuple):
            self._c_data[5] = st
        else:
            self._c_data[5] = (st,)

    @property  # get PRC.7
    def minimum_quantity(self) -> NM | None:
        """
        id: PRC.7 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.7
        """
        return self._c_data[6][0]

    @minimum_quantity.setter  # set PRC.7
    def minimum_quantity(self, nm: NM | None):
        """
        id: PRC.7 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.7
        """
        self._c_data[6] = (nm,)

    @property  # get PRC.8
    def maximum_quantity(self) -> NM | None:
        """
        id: PRC.8 | len: 4 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.8
        """
        return self._c_data[7][0]

    @maximum_quantity.setter  # set PRC.8
    def maximum_quantity(self, nm: NM | None):
        """
        id: PRC.8 | len: 4 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.8
        """
        self._c_data[7] = (nm,)

    @property  # get PRC.9
    def minimum_price(self) -> MO | None:
        """
        id: PRC.9 | len: 12 | use: O | rpt: 1
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.9
        """
        return self._c_data[8][0]

    @minimum_price.setter  # set PRC.9
    def minimum_price(self, mo: MO | None):
        """
        id: PRC.9 | len: 12 | use: O | rpt: 1
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.9
        """
        self._c_data[8] = (mo,)

    @property  # get PRC.10
    def maximum_price(self) -> MO | None:
        """
        id: PRC.10 | len: 12 | use: O | rpt: 1
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.10
        """
        return self._c_data[9][0]

    @maximum_price.setter  # set PRC.10
    def maximum_price(self, mo: MO | None):
        """
        id: PRC.10 | len: 12 | use: O | rpt: 1
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.10
        """
        self._c_data[9] = (mo,)

    @property  # get PRC.11
    def effective_start_date(self) -> TS | None:
        """
        id: PRC.11 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.11
        """
        return self._c_data[10][0]

    @effective_start_date.setter  # set PRC.11
    def effective_start_date(self, ts: TS | None):
        """
        id: PRC.11 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.11
        """
        self._c_data[10] = (ts,)

    @property  # get PRC.12
    def effective_end_date(self) -> TS | None:
        """
        id: PRC.12 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.12
        """
        return self._c_data[11][0]

    @effective_end_date.setter  # set PRC.12
    def effective_end_date(self, ts: TS | None):
        """
        id: PRC.12 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.12
        """
        self._c_data[11] = (ts,)

    @property  # get PRC.13
    def price_override_flag(self) -> Override | None:
        """
        id: PRC.13 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.13
        """
        return self._c_data[12][0]

    @price_override_flag.setter  # set PRC.13
    def price_override_flag(self, override: Override | None):
        """
        id: PRC.13 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.13
        """
        self._c_data[12] = (override,)

    @property
    def billing_category(self) -> tuple[BillingCategory, ...] | tuple[None]:
        """
        id: PRC.14 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.14
        """
        return self._c_data[13]

    @billing_category.setter  # set PRC.14
    def billing_category(
        self, billing_category: BillingCategory | tuple[BillingCategory] | None
    ):
        """
        id: PRC.14 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.14
        """
        if isinstance(billing_category, tuple):
            self._c_data[13] = billing_category
        else:
            self._c_data[13] = (billing_category,)

    @property  # get PRC.15
    def chargeable_flag(self) -> YesOrNoIndicator | None:
        """
        id: PRC.15 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.15
        """
        return self._c_data[14][0]

    @chargeable_flag.setter  # set PRC.15
    def chargeable_flag(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: PRC.15 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.15
        """
        self._c_data[14] = (yes_or_no_indicator,)

    @property  # get PRC.16
    def active_or_inactive_flag(self) -> ActiveOrInactive | None:
        """
        id: PRC.16 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.16
        """
        return self._c_data[15][0]

    @active_or_inactive_flag.setter  # set PRC.16
    def active_or_inactive_flag(self, active_or_inactive: ActiveOrInactive | None):
        """
        id: PRC.16 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.16
        """
        self._c_data[15] = (active_or_inactive,)

    @property  # get PRC.17
    def cost(self) -> MO | None:
        """
        id: PRC.17 | len: 12 | use: O | rpt: 1
        ---
        return_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.17
        """
        return self._c_data[16][0]

    @cost.setter  # set PRC.17
    def cost(self, mo: MO | None):
        """
        id: PRC.17 | len: 12 | use: O | rpt: 1
        ---
        param_type: MO: Money
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.17
        """
        self._c_data[16] = (mo,)

    @property  # get PRC.18
    def charge_on_indicator(self) -> ChargeOnIndicator | None:
        """
        id: PRC.18 | len: 1 | use: O | rpt: 1
        ---
        return_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.18
        """
        return self._c_data[17][0]

    @charge_on_indicator.setter  # set PRC.18
    def charge_on_indicator(self, charge_on_indicator: ChargeOnIndicator | None):
        """
        id: PRC.18 | len: 1 | use: O | rpt: 1
        ---
        param_type: IS: Coded value for user-defined tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PRC.18
        """
        self._c_data[17] = (charge_on_indicator,)
