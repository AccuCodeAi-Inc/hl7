from __future__ import annotations
from ...base import HL7Segment
from ..data_types.RCD import RCD
from ..data_types.NM import NM


"""
Table Row Definition - RDF
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RDF TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RDF,
    RCD, NM
)

rdf = RDF(  #  - The RDF segment defines the content of the row data segments (RDT) in the tabular response (RTB)
    number_of_columns_per_row=nm,  # NM(...)  # Required.
    column_description=rcd,  # RCD(...)  # Required.
)

-----END SEGMENT::RDF TEMPLATE-----
"""


class RDF(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RDF"""
    _hl7_name = """Table Row Definition"""
    _hl7_description = """The RDF segment defines the content of the row data segments (RDT) in the tabular response (RTB)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF"
    _c_length = (3, 40,)
    _c_rpt = (1, 65535,)
    _c_usage = ("R", "R",)
    _c_components = (NM, RCD,)
    _c_aliases = ("RDF.1", "RDF.2",)
    _c_names = ("Number of Columns per Row", "Column Description",)
    _c_attrs = ("number_of_columns_per_row", "column_description",)
    # fmt: on

    def __init__(
        self,
        number_of_columns_per_row: NM,  # RDF.1
        column_description: RCD,  # RDF.2
    ):
        """
        Table Row Definition - `RDF <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDF>`_
        The RDF segment defines the content of the row data segments (RDT) in the tabular response (RTB).

        :param number_of_columns_per_row: Numeric (id: RDF.1 | len: 3 | use: R | rpt: 1)
        :param column_description: Row Column Definition (id: RDF.2 | len: 40 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.number_of_columns_per_row = number_of_columns_per_row
        self.column_description = column_description

    @property  # get RDF.1
    def number_of_columns_per_row(self) -> NM:
        """
        id: RDF.1 | len: 3 | use: R | rpt: 1
        ---
        return_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RDF.1
        """
        return self._c_data[0][0]

    @number_of_columns_per_row.setter  # set RDF.1
    def number_of_columns_per_row(self, nm: NM):
        """
        id: RDF.1 | len: 3 | use: R | rpt: 1
        ---
        param_type: NM: Numeric
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RDF.1
        """
        self._c_data[0] = (nm,)

    @property
    def column_description(self) -> tuple[RCD, ...]:
        """
        id: RDF.2 | len: 40 | use: R | rpt: *
        ---
        return_type: tuple[RCD, ...]: (Row Column Definition, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RDF.2
        """
        return self._c_data[1]

    @column_description.setter  # set RDF.2
    def column_description(self, rcd: RCD | tuple[RCD]):
        """
        id: RDF.2 | len: 40 | use: R | rpt: *
        ---
        param_type: RCD | tuple[RCD, ...]: (Row Column Definition, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RDF.2
        """
        if isinstance(rcd, tuple):
            self._c_data[1] = rcd
        else:
            self._c_data[1] = (rcd,)
