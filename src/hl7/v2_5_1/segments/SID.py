from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..tables.ManufacturerIdentifier import ManufacturerIdentifier


"""
Substance Identifier - SID
HL7 Version: 2.5.1

-----BEGIN SEGMENT::SID TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SID,
    CE, ST
)

sid = SID(  #  - The Substance Identifier segment contains data necessary to identify the substance (e
    application_or_method_identifier=None,  # CE(...) 
    substance_lot_number=None,  # ST(...) 
    substance_container_identifier=None,  # ST(...) 
    substance_manufacturer_identifier=None,  # CE(...) 
)

-----END SEGMENT::SID TEMPLATE-----
"""


class SID(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """SID"""
    _hl7_name = """Substance Identifier"""
    _hl7_description = """The Substance Identifier segment contains data necessary to identify the substance (e"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SID"
    _c_length = (250, 20, 200, 250,)
    _c_rpt = (1, 1, 1, 1,)
    _c_usage = ("C", "C", "C", "C",)
    _c_components = (CE, ST, ST, CE,)
    _c_aliases = ("SID.1", "SID.2", "SID.3", "SID.4",)
    _c_names = ("Application / Method Identifier", "Substance Lot Number", "Substance Container Identifier", "Substance Manufacturer Identifier",)
    _c_attrs = ("application_or_method_identifier", "substance_lot_number", "substance_container_identifier", "substance_manufacturer_identifier",)
    # fmt: on

    def __init__(
        self,
        application_or_method_identifier: CE | None = None,  # SID.1
        substance_lot_number: ST | None = None,  # SID.2
        substance_container_identifier: ST | None = None,  # SID.3
        substance_manufacturer_identifier: ManufacturerIdentifier
        | CE
        | None = None,  # SID.4
    ):
        """
                Substance Identifier - `SID <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SID>`_
                The Substance Identifier segment contains data necessary to identify the substance (e.g., reagents) used in the production of analytical test results. The combination of these fields must uniquely identify the substance, i.e., depending on the manufacturer all or some fields are required (this is the reason the optionality is 'C' (conditional)). If the analysis requires multiple substances, this segment is repeated for each substance. The segment(s) should be attached to the TCD segment.

        Another purpose of this segment is to transfer the control manufacturer, lot, etc. information for control specimens. In this case the SID segment should be attached to the SAC segment describing the container with the control specimen.

                :param application_or_method_identifier: Coded Element (id: SID.1 | len: 250 | use: C | rpt: 1)
                :param substance_lot_number: String Data (id: SID.2 | len: 20 | use: C | rpt: 1)
                :param substance_container_identifier: String Data (id: SID.3 | len: 200 | use: C | rpt: 1)
                :param substance_manufacturer_identifier: Coded Element (id: SID.4 | len: 250 | use: C | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.application_or_method_identifier = application_or_method_identifier
        self.substance_lot_number = substance_lot_number
        self.substance_container_identifier = substance_container_identifier
        self.substance_manufacturer_identifier = substance_manufacturer_identifier

    @property  # get SID.1
    def application_or_method_identifier(self) -> CE | None:
        """
        id: SID.1 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.1
        """
        return self._c_data[0][0]

    @application_or_method_identifier.setter  # set SID.1
    def application_or_method_identifier(self, ce: CE | None):
        """
        id: SID.1 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.1
        """
        self._c_data[0] = (ce,)

    @property  # get SID.2
    def substance_lot_number(self) -> ST | None:
        """
        id: SID.2 | len: 20 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.2
        """
        return self._c_data[1][0]

    @substance_lot_number.setter  # set SID.2
    def substance_lot_number(self, st: ST | None):
        """
        id: SID.2 | len: 20 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.2
        """
        self._c_data[1] = (st,)

    @property  # get SID.3
    def substance_container_identifier(self) -> ST | None:
        """
        id: SID.3 | len: 200 | use: C | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.3
        """
        return self._c_data[2][0]

    @substance_container_identifier.setter  # set SID.3
    def substance_container_identifier(self, st: ST | None):
        """
        id: SID.3 | len: 200 | use: C | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.3
        """
        self._c_data[2] = (st,)

    @property  # get SID.4
    def substance_manufacturer_identifier(self) -> ManufacturerIdentifier | None:
        """
        id: SID.4 | len: 250 | use: C | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.4
        """
        return self._c_data[3][0]

    @substance_manufacturer_identifier.setter  # set SID.4
    def substance_manufacturer_identifier(
        self, manufacturer_identifier: ManufacturerIdentifier | None
    ):
        """
        id: SID.4 | len: 250 | use: C | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SID.4
        """
        self._c_data[3] = (manufacturer_identifier,)
