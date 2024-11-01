from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.ID import ID
from ..tables.YesOrNoIndicator import YesOrNoIndicator
from ..tables.ManufacturerIdentifier import ManufacturerIdentifier


"""
Requisition Detail-1 - RQ1
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RQ1 TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RQ1,
    CE, ST, ID
)

rq1 = RQ1(  #  - RQ1 contains additional detail for each nonstock requisitioned item
    anticipated_price=None,  # ST(...) 
    manufacturer_identifier=None,  # CE(...) 
    manufacturers_catalog=None,  # ST(...) 
    vendor_id=None,  # CE(...) 
    vendor_catalog=None,  # ST(...) 
    taxable=None,  # ID(...) 
    substitute_allowed=None,  # ID(...) 
)

-----END SEGMENT::RQ1 TEMPLATE-----
"""


class RQ1(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RQ1"""
    _hl7_name = """Requisition Detail-1"""
    _hl7_description = """RQ1 contains additional detail for each nonstock requisitioned item"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1"
    _c_length = (10, 250, 16, 250, 16, 1, 1,)
    _c_rpt = (1, 1, 1, 1, 1, 1, 1,)
    _c_usage = ("O", "C", "C", "C", "C", "O", "O",)
    _c_components = (ST, CE, ST, CE, ST, ID, ID,)
    _c_aliases = ("RQ1.1", "RQ1.2", "RQ1.3", "RQ1.4", "RQ1.5", "RQ1.6", "RQ1.7",)
    _c_names = ("Anticipated Price", "Manufacturer Identifier", "Manufacturer's Catalog", "Vendor ID", "Vendor Catalog", "Taxable", "Substitute Allowed",)
    _c_attrs = ("anticipated_price", "manufacturer_identifier", "manufacturers_catalog", "vendor_id", "vendor_catalog", "taxable", "substitute_allowed",)
    # fmt: on

    def __init__(
        self,
        anticipated_price: ST | None = None,  # RQ1.1
        manufacturer_identifier: ManufacturerIdentifier | CE | None = None,  # RQ1.2
        manufacturers_catalog: ST | None = None,  # RQ1.3
        vendor_id: CE | None = None,  # RQ1.4
        vendor_catalog: ST | None = None,  # RQ1.5
        taxable: YesOrNoIndicator | ID | None = None,  # RQ1.6
        substitute_allowed: YesOrNoIndicator | ID | None = None,  # RQ1.7
    ):
        """
        Requisition Detail-1 - `RQ1 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RQ1>`_
        RQ1 contains additional detail for each nonstock requisitioned item. This segment definition is paired with a preceding RQD segment.

        :param anticipated_price: String Data (id: RQ1.1 | len: 10 | use: O | rpt: 1)
        :param manufacturer_identifier: Coded Element (id: RQ1.2 | len: 250 | use: C | rpt: 1)
        :param manufacturers_catalog: String Data (id: RQ1.3 | len: 16 | use: C | rpt: 1)
        :param vendor_id: Coded Element (id: RQ1.4 | len: 250 | use: C | rpt: 1)
        :param vendor_catalog: String Data (id: RQ1.5 | len: 16 | use: C | rpt: 1)
        :param taxable: Coded values for HL7 tables (id: RQ1.6 | len: 1 | use: O | rpt: 1)
        :param substitute_allowed: Coded values for HL7 tables (id: RQ1.7 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.anticipated_price = anticipated_price
        self.manufacturer_identifier = manufacturer_identifier
        self.manufacturers_catalog = manufacturers_catalog
        self.vendor_id = vendor_id
        self.vendor_catalog = vendor_catalog
        self.taxable = taxable
        self.substitute_allowed = substitute_allowed

    @property  # get RQ1.1
    def anticipated_price(self) -> ST | None:
        """
        id: RQ1.1 | len: 10 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.1
        """
        return self._c_data[0][0]

    @anticipated_price.setter  # set RQ1.1
    def anticipated_price(self, st: ST | None):
        """
        id: RQ1.1 | len: 10 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.1
        """
        self._c_data[0] = (st,)

    @property  # get RQ1.2
    def manufacturer_identifier(self) -> ManufacturerIdentifier | None:
        """
        id: RQ1.2 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.2
        """
        return self._c_data[1][0]

    @manufacturer_identifier.setter  # set RQ1.2
    def manufacturer_identifier(
        self, manufacturer_identifier: ManufacturerIdentifier | None
    ):
        """
        id: RQ1.2 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.2
        """
        self._c_data[1] = (manufacturer_identifier,)

    @property  # get RQ1.3
    def manufacturers_catalog(self) -> ST | None:
        """
        id: RQ1.3 | len: 16 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.3
        """
        return self._c_data[2][0]

    @manufacturers_catalog.setter  # set RQ1.3
    def manufacturers_catalog(self, st: ST | None):
        """
        id: RQ1.3 | len: 16 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.3
        """
        self._c_data[2] = (st,)

    @property  # get RQ1.4
    def vendor_id(self) -> CE | None:
        """
        id: RQ1.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.4
        """
        return self._c_data[3][0]

    @vendor_id.setter  # set RQ1.4
    def vendor_id(self, ce: CE | None):
        """
        id: RQ1.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.4
        """
        self._c_data[3] = (ce,)

    @property  # get RQ1.5
    def vendor_catalog(self) -> ST | None:
        """
        id: RQ1.5 | len: 16 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.5
        """
        return self._c_data[4][0]

    @vendor_catalog.setter  # set RQ1.5
    def vendor_catalog(self, st: ST | None):
        """
        id: RQ1.5 | len: 16 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.5
        """
        self._c_data[4] = (st,)

    @property  # get RQ1.6
    def taxable(self) -> YesOrNoIndicator | None:
        """
        id: RQ1.6 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.6
        """
        return self._c_data[5][0]

    @taxable.setter  # set RQ1.6
    def taxable(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RQ1.6 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.6
        """
        self._c_data[5] = (yes_or_no_indicator,)

    @property  # get RQ1.7
    def substitute_allowed(self) -> YesOrNoIndicator | None:
        """
        id: RQ1.7 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.7
        """
        return self._c_data[6][0]

    @substitute_allowed.setter  # set RQ1.7
    def substitute_allowed(self, yes_or_no_indicator: YesOrNoIndicator | None):
        """
        id: RQ1.7 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RQ1.7
        """
        self._c_data[6] = (yes_or_no_indicator,)
