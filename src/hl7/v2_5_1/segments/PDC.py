from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.XON import XON
from ..data_types.CQ import CQ
from ..data_types.ID import ID
from ..data_types.ST import ST
from ..data_types.TS import TS
from ..tables.MarketingBasis import MarketingBasis


"""
Product Detail Country - PDC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::PDC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    PDC,
    CE, XON, CQ, ID, ST, TS
)

pdc = PDC(  #  - 
    manufacturer_or_distributor=xon,  # XON(...)  # Required.
    country=ce,  # CE(...)  # Required.
    brand_name=st,  # ST(...)  # Required.
    device_family_name=None,  # ST(...) 
    generic_name=None,  # CE(...) 
    model_identifier=None,  # ST(...) 
    catalogue_identifier=None,  # ST(...) 
    other_identifier=None,  # ST(...) 
    product_code=None,  # CE(...) 
    marketing_basis=None,  # ID(...) 
    marketing_approval_id=None,  # ST(...) 
    labeled_shelf_life=None,  # CQ(...) 
    expected_shelf_life=None,  # CQ(...) 
    date_first_marketed=None,  # TS(...) 
    date_last_marketed=None,  # TS(...) 
)

-----END SEGMENT::PDC TEMPLATE-----
"""


class PDC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """PDC"""
    _hl7_name = """Product Detail Country"""
    _hl7_description = """"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDC"
    _c_length = (250, 250, 60, 60, 250, 60, 60, 60, 250, 4, 60, 12, 12, 26, 26,)
    _c_rpt = (65535, 1, 1, 1, 1, 65535, 1, 65535, 1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("R", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",)
    _c_components = (XON, CE, ST, ST, CE, ST, ST, ST, CE, ID, ST, CQ, CQ, TS, TS,)
    _c_aliases = ("PDC.1", "PDC.2", "PDC.3", "PDC.4", "PDC.5", "PDC.6", "PDC.7", "PDC.8", "PDC.9", "PDC.10", "PDC.11", "PDC.12", "PDC.13", "PDC.14", "PDC.15",)
    _c_names = ("Manufacturer/Distributor", "Country", "Brand Name", "Device Family Name", "Generic Name", "Model Identifier", "Catalogue Identifier", "Other Identifier", "Product Code", "Marketing Basis", "Marketing Approval ID", "Labeled Shelf Life", "Expected Shelf Life", "Date First Marketed", "Date Last Marketed",)
    _c_attrs = ("manufacturer_or_distributor", "country", "brand_name", "device_family_name", "generic_name", "model_identifier", "catalogue_identifier", "other_identifier", "product_code", "marketing_basis", "marketing_approval_id", "labeled_shelf_life", "expected_shelf_life", "date_first_marketed", "date_last_marketed",)
    # fmt: on

    def __init__(
        self,
        manufacturer_or_distributor: XON,  # PDC.1
        country: CE,  # PDC.2
        brand_name: ST,  # PDC.3
        device_family_name: ST | None = None,  # PDC.4
        generic_name: CE | None = None,  # PDC.5
        model_identifier: ST | None = None,  # PDC.6
        catalogue_identifier: ST | None = None,  # PDC.7
        other_identifier: ST | None = None,  # PDC.8
        product_code: CE | None = None,  # PDC.9
        marketing_basis: MarketingBasis | ID | None = None,  # PDC.10
        marketing_approval_id: ST | None = None,  # PDC.11
        labeled_shelf_life: CQ | None = None,  # PDC.12
        expected_shelf_life: CQ | None = None,  # PDC.13
        date_first_marketed: TS | None = None,  # PDC.14
        date_last_marketed: TS | None = None,  # PDC.15
    ):
        """
        Product Detail Country - `PDC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDC>`_


        :param manufacturer_or_distributor: Extended Composite Name and Identification Number for Organizations (id: PDC.1 | len: 250 | use: R | rpt: *)
        :param country: Coded Element (id: PDC.2 | len: 250 | use: R | rpt: 1)
        :param brand_name: String Data (id: PDC.3 | len: 60 | use: R | rpt: 1)
        :param device_family_name: String Data (id: PDC.4 | len: 60 | use: O | rpt: 1)
        :param generic_name: Coded Element (id: PDC.5 | len: 250 | use: O | rpt: 1)
        :param model_identifier: String Data (id: PDC.6 | len: 60 | use: O | rpt: *)
        :param catalogue_identifier: String Data (id: PDC.7 | len: 60 | use: O | rpt: 1)
        :param other_identifier: String Data (id: PDC.8 | len: 60 | use: O | rpt: *)
        :param product_code: Coded Element (id: PDC.9 | len: 250 | use: O | rpt: 1)
        :param marketing_basis: Coded values for HL7 tables (id: PDC.10 | len: 4 | use: O | rpt: 1)
        :param marketing_approval_id: String Data (id: PDC.11 | len: 60 | use: O | rpt: 1)
        :param labeled_shelf_life: Composite Quantity with Units (id: PDC.12 | len: 12 | use: O | rpt: 1)
        :param expected_shelf_life: Composite Quantity with Units (id: PDC.13 | len: 12 | use: O | rpt: 1)
        :param date_first_marketed: Time Stamp (id: PDC.14 | len: 26 | use: O | rpt: 1)
        :param date_last_marketed: Time Stamp (id: PDC.15 | len: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 15
        self.manufacturer_or_distributor = manufacturer_or_distributor
        self.country = country
        self.brand_name = brand_name
        self.device_family_name = device_family_name
        self.generic_name = generic_name
        self.model_identifier = model_identifier
        self.catalogue_identifier = catalogue_identifier
        self.other_identifier = other_identifier
        self.product_code = product_code
        self.marketing_basis = marketing_basis
        self.marketing_approval_id = marketing_approval_id
        self.labeled_shelf_life = labeled_shelf_life
        self.expected_shelf_life = expected_shelf_life
        self.date_first_marketed = date_first_marketed
        self.date_last_marketed = date_last_marketed

    @property
    def manufacturer_or_distributor(self) -> tuple[XON, ...]:
        """
        id: PDC.1 | len: 250 | use: R | rpt: *
        ---
        return_type: tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.1
        """
        return self._c_data[0]

    @manufacturer_or_distributor.setter  # set PDC.1
    def manufacturer_or_distributor(self, xon: XON | tuple[XON]):
        """
        id: PDC.1 | len: 250 | use: R | rpt: *
        ---
        param_type: XON | tuple[XON, ...]: (Extended Composite Name and Identification Number for Organizations, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.1
        """
        if isinstance(xon, tuple):
            self._c_data[0] = xon
        else:
            self._c_data[0] = (xon,)

    @property  # get PDC.2
    def country(self) -> CE:
        """
        id: PDC.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.2
        """
        return self._c_data[1][0]

    @country.setter  # set PDC.2
    def country(self, ce: CE):
        """
        id: PDC.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.2
        """
        self._c_data[1] = (ce,)

    @property  # get PDC.3
    def brand_name(self) -> ST:
        """
        id: PDC.3 | len: 60 | use: R | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.3
        """
        return self._c_data[2][0]

    @brand_name.setter  # set PDC.3
    def brand_name(self, st: ST):
        """
        id: PDC.3 | len: 60 | use: R | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.3
        """
        self._c_data[2] = (st,)

    @property  # get PDC.4
    def device_family_name(self) -> ST | None:
        """
        id: PDC.4 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.4
        """
        return self._c_data[3][0]

    @device_family_name.setter  # set PDC.4
    def device_family_name(self, st: ST | None):
        """
        id: PDC.4 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.4
        """
        self._c_data[3] = (st,)

    @property  # get PDC.5
    def generic_name(self) -> CE | None:
        """
        id: PDC.5 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.5
        """
        return self._c_data[4][0]

    @generic_name.setter  # set PDC.5
    def generic_name(self, ce: CE | None):
        """
        id: PDC.5 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.5
        """
        self._c_data[4] = (ce,)

    @property
    def model_identifier(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: PDC.6 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.6
        """
        return self._c_data[5]

    @model_identifier.setter  # set PDC.6
    def model_identifier(self, st: ST | tuple[ST] | None):
        """
        id: PDC.6 | len: 60 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.6
        """
        if isinstance(st, tuple):
            self._c_data[5] = st
        else:
            self._c_data[5] = (st,)

    @property  # get PDC.7
    def catalogue_identifier(self) -> ST | None:
        """
        id: PDC.7 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.7
        """
        return self._c_data[6][0]

    @catalogue_identifier.setter  # set PDC.7
    def catalogue_identifier(self, st: ST | None):
        """
        id: PDC.7 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.7
        """
        self._c_data[6] = (st,)

    @property
    def other_identifier(self) -> tuple[ST, ...] | tuple[None]:
        """
        id: PDC.8 | len: 60 | use: O | rpt: *
        ---
        return_type: tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.8
        """
        return self._c_data[7]

    @other_identifier.setter  # set PDC.8
    def other_identifier(self, st: ST | tuple[ST] | None):
        """
        id: PDC.8 | len: 60 | use: O | rpt: *
        ---
        param_type: ST | tuple[ST, ...]: (String Data, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.8
        """
        if isinstance(st, tuple):
            self._c_data[7] = st
        else:
            self._c_data[7] = (st,)

    @property  # get PDC.9
    def product_code(self) -> CE | None:
        """
        id: PDC.9 | len: 250 | use: O | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.9
        """
        return self._c_data[8][0]

    @product_code.setter  # set PDC.9
    def product_code(self, ce: CE | None):
        """
        id: PDC.9 | len: 250 | use: O | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.9
        """
        self._c_data[8] = (ce,)

    @property  # get PDC.10
    def marketing_basis(self) -> MarketingBasis | None:
        """
        id: PDC.10 | len: 4 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.10
        """
        return self._c_data[9][0]

    @marketing_basis.setter  # set PDC.10
    def marketing_basis(self, marketing_basis: MarketingBasis | None):
        """
        id: PDC.10 | len: 4 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.10
        """
        self._c_data[9] = (marketing_basis,)

    @property  # get PDC.11
    def marketing_approval_id(self) -> ST | None:
        """
        id: PDC.11 | len: 60 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.11
        """
        return self._c_data[10][0]

    @marketing_approval_id.setter  # set PDC.11
    def marketing_approval_id(self, st: ST | None):
        """
        id: PDC.11 | len: 60 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.11
        """
        self._c_data[10] = (st,)

    @property  # get PDC.12
    def labeled_shelf_life(self) -> CQ | None:
        """
        id: PDC.12 | len: 12 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.12
        """
        return self._c_data[11][0]

    @labeled_shelf_life.setter  # set PDC.12
    def labeled_shelf_life(self, cq: CQ | None):
        """
        id: PDC.12 | len: 12 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.12
        """
        self._c_data[11] = (cq,)

    @property  # get PDC.13
    def expected_shelf_life(self) -> CQ | None:
        """
        id: PDC.13 | len: 12 | use: O | rpt: 1
        ---
        return_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.13
        """
        return self._c_data[12][0]

    @expected_shelf_life.setter  # set PDC.13
    def expected_shelf_life(self, cq: CQ | None):
        """
        id: PDC.13 | len: 12 | use: O | rpt: 1
        ---
        param_type: CQ: Composite Quantity with Units
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.13
        """
        self._c_data[12] = (cq,)

    @property  # get PDC.14
    def date_first_marketed(self) -> TS | None:
        """
        id: PDC.14 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.14
        """
        return self._c_data[13][0]

    @date_first_marketed.setter  # set PDC.14
    def date_first_marketed(self, ts: TS | None):
        """
        id: PDC.14 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.14
        """
        self._c_data[13] = (ts,)

    @property  # get PDC.15
    def date_last_marketed(self) -> TS | None:
        """
        id: PDC.15 | len: 26 | use: O | rpt: 1
        ---
        return_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.15
        """
        return self._c_data[14][0]

    @date_last_marketed.setter  # set PDC.15
    def date_last_marketed(self, ts: TS | None):
        """
        id: PDC.15 | len: 26 | use: O | rpt: 1
        ---
        param_type: TS: Time Stamp
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/PDC.15
        """
        self._c_data[14] = (ts,)
