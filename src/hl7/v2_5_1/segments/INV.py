from __future__ import annotations
from ...base import HL7Segment
from ..data_types.TQ import TQ
from ..data_types.TS import TS
from ..data_types.CQ import CQ
from ..data_types.NM import NM
from ..data_types.ST import ST
from ..data_types.CE import CE
from ..tables.SubstanceIdentifier import SubstanceIdentifier
from ..tables.SubstanceType import SubstanceType
from ..tables.SubstanceStatus import SubstanceStatus
from ..tables.ManufacturerIdentifier import ManufacturerIdentifier
from ..tables.SupplierIdentifier import SupplierIdentifier


"""
Inventory Detail - INV
HL7 Version: 2.5.1

-----BEGIN SEGMENT::INV TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    INV,
    TQ, TS, CQ, NM, ST, CE
)

inv = INV(  #  - The inventory detail segment is the data necessary to track the inventory of substances (e
    substance_identifier=ce,  # CE(...)  # Required.
    substance_status=ce,  # CE(...)  # Required.
    substance_type=None,  # CE(...) 
    inventory_container_identifier=None,  # CE(...) 
    container_carrier_identifier=None,  # CE(...) 
    position_on_carrier=None,  # CE(...) 
    initial_quantity=None,  # NM(...) 
    current_quantity=None,  # NM(...) 
    available_quantity=None,  # NM(...) 
    consumption_quantity=None,  # NM(...) 
    quantity_units=None,  # CE(...) 
    expiration_date_or_time=None,  # TS(...) 
    first_used_date_or_time=None,  # TS(...) 
    on_board_stability_duration=None,  # TQ(...) 
    test_or_fluid_identifier=None,  # CE(...) 
    manufacturer_lot_number=None,  # ST(...) 
    manufacturer_identifier=None,  # CE(...) 
    supplier_identifier=None,  # CE(...) 
    on_board_stability_time=None,  # CQ(...) 
    target_value=None,  # CQ(...) 
)

-----END SEGMENT::INV TEMPLATE-----
"""


class INV(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """INV"""
    _hl7_name = """Inventory Detail"""
    _hl7_description = """The inventory detail segment is the data necessary to track the inventory of substances (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/INV"
    _c_length = (250, 250, 250, 250, 250, 250, 20, 20, 20, 20, 250, 26, 26, 200, 250, 200, 250, 250, 20, 20,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 65535, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B", "O", "O", "O", "O", "O", "O",)
    _c_components = (CE, CE, CE, CE, CE, CE, NM, NM, NM, NM, CE, TS, TS, TQ, CE, ST, CE, CE, CQ, CQ,)
    _c_aliases = ("INV.1", "INV.2", "INV.3", "INV.4", "INV.5", "INV.6", "INV.7", "INV.8", "INV.9", "INV.10", "INV.11", "INV.12", "INV.13", "INV.14", "INV.15", "INV.16", "INV.17", "INV.18", "INV.19", "INV.20",)
    _c_names = ("Substance Identifier", "Substance Status", "Substance Type", "Inventory Container Identifier", "Container Carrier Identifier", "Position on Carrier", "Initial Quantity", "Current Quantity", "Available Quantity", "Consumption Quantity", "Quantity Units", "Expiration Date/Time", "First Used Date/Time", "On Board Stability Duration", "Test/Fluid Identifier(s)", "Manufacturer Lot Number", "Manufacturer Identifier", "Supplier Identifier", "On Board Stability Time", "Target Value",)
    _c_attrs = ("substance_identifier", "substance_status", "substance_type", "inventory_container_identifier", "container_carrier_identifier", "position_on_carrier", "initial_quantity", "current_quantity", "available_quantity", "consumption_quantity", "quantity_units", "expiration_date_or_time", "first_used_date_or_time", "on_board_stability_duration", "test_or_fluid_identifier", "manufacturer_lot_number", "manufacturer_identifier", "supplier_identifier", "on_board_stability_time", "target_value",)
    # fmt: on

    def __init__(
        self,
        substance_identifier: SubstanceIdentifier
        | CE
        | tuple[SubstanceIdentifier | CE],  # INV.1
        substance_status: SubstanceStatus | CE | tuple[SubstanceStatus | CE],  # INV.2
        substance_type: SubstanceType
        | CE
        | tuple[SubstanceType | CE]
        | None = None,  # INV.3
        inventory_container_identifier: CE | tuple[CE] | None = None,  # INV.4
        container_carrier_identifier: CE | tuple[CE] | None = None,  # INV.5
        position_on_carrier: CE | tuple[CE] | None = None,  # INV.6
        initial_quantity: NM | tuple[NM] | None = None,  # INV.7
        current_quantity: NM | tuple[NM] | None = None,  # INV.8
        available_quantity: NM | tuple[NM] | None = None,  # INV.9
        consumption_quantity: NM | tuple[NM] | None = None,  # INV.10
        quantity_units: CE | tuple[CE] | None = None,  # INV.11
        expiration_date_or_time: TS | tuple[TS] | None = None,  # INV.12
        first_used_date_or_time: TS | tuple[TS] | None = None,  # INV.13
        on_board_stability_duration: TQ | tuple[TQ] | None = None,  # INV.14
        test_or_fluid_identifier: CE | tuple[CE] | None = None,  # INV.15
        manufacturer_lot_number: ST | tuple[ST] | None = None,  # INV.16
        manufacturer_identifier: ManufacturerIdentifier
        | CE
        | tuple[ManufacturerIdentifier | CE]
        | None = None,  # INV.17
        supplier_identifier: SupplierIdentifier
        | CE
        | tuple[SupplierIdentifier | CE]
        | None = None,  # INV.18
        on_board_stability_time: CQ | tuple[CQ] | None = None,  # INV.19
        target_value: CQ | tuple[CQ] | None = None,  # INV.20
    ):
        """
        Inventory Detail - `INV <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/INV>`_
        The inventory detail segment is the data necessary to track the inventory of substances (e.g. reagent, tips, waste) on equipment.

        :param substance_identifier: Coded Element (id: INV.1 | len: 250 | use: R | rpt: 1)
        :param substance_status: Coded Element (id: INV.2 | len: 250 | use: R | rpt: *)
        :param substance_type: Coded Element (id: INV.3 | len: 250 | use: O | rpt: 1)
        :param inventory_container_identifier: Coded Element (id: INV.4 | len: 250 | use: O | rpt: 1)
        :param container_carrier_identifier: Coded Element (id: INV.5 | len: 250 | use: O | rpt: 1)
        :param position_on_carrier: Coded Element (id: INV.6 | len: 250 | use: O | rpt: 1)
        :param initial_quantity: Numeric (id: INV.7 | len: 20 | use: O | rpt: 1)
        :param current_quantity: Numeric (id: INV.8 | len: 20 | use: O | rpt: 1)
        :param available_quantity: Numeric (id: INV.9 | len: 20 | use: O | rpt: 1)
        :param consumption_quantity: Numeric (id: INV.10 | len: 20 | use: O | rpt: 1)
        :param quantity_units: Coded Element (id: INV.11 | len: 250 | use: O | rpt: 1)
        :param expiration_date_or_time: Time Stamp (id: INV.12 | len: 26 | use: O | rpt: 1)
        :param first_used_date_or_time: Time Stamp (id: INV.13 | len: 26 | use: O | rpt: 1)
        :param on_board_stability_duration: Timing Quantity (id: INV.14 | len: 200 | use: B | rpt: 1)
        :param test_or_fluid_identifier: Coded Element (id: INV.15 | len: 250 | use: O | rpt: *)
        :param manufacturer_lot_number: String Data (id: INV.16 | len: 200 | use: O | rpt: 1)
        :param manufacturer_identifier: Coded Element (id: INV.17 | len: 250 | use: O | rpt: 1)
        :param supplier_identifier: Coded Element (id: INV.18 | len: 250 | use: O | rpt: 1)
        :param on_board_stability_time: Composite Quantity with Units (id: INV.19 | len: 20 | use: O | rpt: 1)
        :param target_value: Composite Quantity with Units (id: INV.20 | len: 20 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 20
        self.substance_identifier = substance_identifier
        self.substance_status = substance_status
        self.substance_type = substance_type
        self.inventory_container_identifier = inventory_container_identifier
        self.container_carrier_identifier = container_carrier_identifier
        self.position_on_carrier = position_on_carrier
        self.initial_quantity = initial_quantity
        self.current_quantity = current_quantity
        self.available_quantity = available_quantity
        self.consumption_quantity = consumption_quantity
        self.quantity_units = quantity_units
        self.expiration_date_or_time = expiration_date_or_time
        self.first_used_date_or_time = first_used_date_or_time
        self.on_board_stability_duration = on_board_stability_duration
        self.test_or_fluid_identifier = test_or_fluid_identifier
        self.manufacturer_lot_number = manufacturer_lot_number
        self.manufacturer_identifier = manufacturer_identifier
        self.supplier_identifier = supplier_identifier
        self.on_board_stability_time = on_board_stability_time
        self.target_value = target_value

    @property  # get INV.1
    def substance_identifier(self) -> SubstanceIdentifier:
        """
        id: INV.1 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.1
        """
        return self._c_data[0][0]

    @substance_identifier.setter  # set INV.1
    def substance_identifier(self, substance_identifier: SubstanceIdentifier):
        """
        id: INV.1 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.1
        """
        self._c_data[0] = (substance_identifier,)

    @property
    def substance_status(self) -> tuple[SubstanceStatus, ...]:
        """
        id: INV.2 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.2
        """
        return self._c_data[1]

    @substance_status.setter  # set INV.2
    def substance_status(
        self, substance_status: SubstanceStatus | tuple[SubstanceStatus]
    ):
        """
        id: INV.2 | len: 250 | use: R | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.2
        """
        if isinstance(substance_status, tuple):
            self._c_data[1] = substance_status
        else:
            self._c_data[1] = (substance_status,)

    @property  # get INV.3
    def substance_type(self) -> SubstanceType | None:
        """
        id: INV.3 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.3
        """
        return self._c_data[2][0]

    @substance_type.setter  # set INV.3
    def substance_type(self, substance_type: SubstanceType | None):
        """
        id: INV.3 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.3
        """
        self._c_data[2] = (substance_type,)

    @property  # get INV.4
    def inventory_container_identifier(self) -> CE | None:
        """
        id: INV.4 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.4
        """
        return self._c_data[3][0]

    @inventory_container_identifier.setter  # set INV.4
    def inventory_container_identifier(self, ce: CE | None):
        """
        id: INV.4 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.4
        """
        self._c_data[3] = (ce,)

    @property  # get INV.5
    def container_carrier_identifier(self) -> CE | None:
        """
        id: INV.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.5
        """
        return self._c_data[4][0]

    @container_carrier_identifier.setter  # set INV.5
    def container_carrier_identifier(self, ce: CE | None):
        """
        id: INV.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.5
        """
        self._c_data[4] = (ce,)

    @property  # get INV.6
    def position_on_carrier(self) -> CE | None:
        """
        id: INV.6 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.6
        """
        return self._c_data[5][0]

    @position_on_carrier.setter  # set INV.6
    def position_on_carrier(self, ce: CE | None):
        """
        id: INV.6 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.6
        """
        self._c_data[5] = (ce,)

    @property  # get INV.7
    def initial_quantity(self) -> NM | None:
        """
        id: INV.7 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.7
        """
        return self._c_data[6][0]

    @initial_quantity.setter  # set INV.7
    def initial_quantity(self, nm: NM | None):
        """
        id: INV.7 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.7
        """
        self._c_data[6] = (nm,)

    @property  # get INV.8
    def current_quantity(self) -> NM | None:
        """
        id: INV.8 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.8
        """
        return self._c_data[7][0]

    @current_quantity.setter  # set INV.8
    def current_quantity(self, nm: NM | None):
        """
        id: INV.8 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.8
        """
        self._c_data[7] = (nm,)

    @property  # get INV.9
    def available_quantity(self) -> NM | None:
        """
        id: INV.9 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.9
        """
        return self._c_data[8][0]

    @available_quantity.setter  # set INV.9
    def available_quantity(self, nm: NM | None):
        """
        id: INV.9 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.9
        """
        self._c_data[8] = (nm,)

    @property  # get INV.10
    def consumption_quantity(self) -> NM | None:
        """
        id: INV.10 | len: 20 | use: O | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.10
        """
        return self._c_data[9][0]

    @consumption_quantity.setter  # set INV.10
    def consumption_quantity(self, nm: NM | None):
        """
        id: INV.10 | len: 20 | use: O | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.10
        """
        self._c_data[9] = (nm,)

    @property  # get INV.11
    def quantity_units(self) -> CE | None:
        """
        id: INV.11 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.11
        """
        return self._c_data[10][0]

    @quantity_units.setter  # set INV.11
    def quantity_units(self, ce: CE | None):
        """
        id: INV.11 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.11
        """
        self._c_data[10] = (ce,)

    @property  # get INV.12
    def expiration_date_or_time(self) -> TS | None:
        """
        id: INV.12 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.12
        """
        return self._c_data[11][0]

    @expiration_date_or_time.setter  # set INV.12
    def expiration_date_or_time(self, ts: TS | None):
        """
        id: INV.12 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.12
        """
        self._c_data[11] = (ts,)

    @property  # get INV.13
    def first_used_date_or_time(self) -> TS | None:
        """
        id: INV.13 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.13
        """
        return self._c_data[12][0]

    @first_used_date_or_time.setter  # set INV.13
    def first_used_date_or_time(self, ts: TS | None):
        """
        id: INV.13 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.13
        """
        self._c_data[12] = (ts,)

    @property  # get INV.14
    def on_board_stability_duration(self) -> TQ | None:
        """
        id: INV.14 | len: 200 | use: B | rpt: 1
        ---
        return_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.14
        """
        return self._c_data[13][0]

    @on_board_stability_duration.setter  # set INV.14
    def on_board_stability_duration(self, tq: TQ | None):
        """
        id: INV.14 | len: 200 | use: B | rpt: 1
        ---
        param_type: TQ: Timing Quantity
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.14
        """
        self._c_data[13] = (tq,)

    @property
    def test_or_fluid_identifier(self) -> tuple[CE, ...] | tuple[None]:
        """
        id: INV.15 | len: 250 | use: O | rpt: *
        ---
        return_type: tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.15
        """
        return self._c_data[14]

    @test_or_fluid_identifier.setter  # set INV.15
    def test_or_fluid_identifier(self, ce: CE | tuple[CE] | None):
        """
        id: INV.15 | len: 250 | use: O | rpt: *
        ---
        param_type: CE | tuple[CE, ...]: (Coded Element, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.15
        """
        if isinstance(ce, tuple):
            self._c_data[14] = ce
        else:
            self._c_data[14] = (ce,)

    @property  # get INV.16
    def manufacturer_lot_number(self) -> ST | None:
        """
        id: INV.16 | len: 200 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.16
        """
        return self._c_data[15][0]

    @manufacturer_lot_number.setter  # set INV.16
    def manufacturer_lot_number(self, st: ST | None):
        """
        id: INV.16 | len: 200 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.16
        """
        self._c_data[15] = (st,)

    @property  # get INV.17
    def manufacturer_identifier(self) -> ManufacturerIdentifier | None:
        """
        id: INV.17 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.17
        """
        return self._c_data[16][0]

    @manufacturer_identifier.setter  # set INV.17
    def manufacturer_identifier(
        self, manufacturer_identifier: ManufacturerIdentifier | None
    ):
        """
        id: INV.17 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.17
        """
        self._c_data[16] = (manufacturer_identifier,)

    @property  # get INV.18
    def supplier_identifier(self) -> SupplierIdentifier | None:
        """
        id: INV.18 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.18
        """
        return self._c_data[17][0]

    @supplier_identifier.setter  # set INV.18
    def supplier_identifier(self, supplier_identifier: SupplierIdentifier | None):
        """
        id: INV.18 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.18
        """
        self._c_data[17] = (supplier_identifier,)

    @property  # get INV.19
    def on_board_stability_time(self) -> CQ | None:
        """
        id: INV.19 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.19
        """
        return self._c_data[18][0]

    @on_board_stability_time.setter  # set INV.19
    def on_board_stability_time(self, cq: CQ | None):
        """
        id: INV.19 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.19
        """
        self._c_data[18] = (cq,)

    @property  # get INV.20
    def target_value(self) -> CQ | None:
        """
        id: INV.20 | len: 20 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.20
        """
        return self._c_data[19][0]

    @target_value.setter  # set INV.20
    def target_value(self, cq: CQ | None):
        """
        id: INV.20 | len: 20 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/INV.20
        """
        self._c_data[19] = (cq,)
