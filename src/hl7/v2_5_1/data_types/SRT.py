from __future__ import annotations
from ...base import DataType
from .ID import ID
from .ST import ST
from ..tables.Sequencing import Sequencing


"""
DataType - SRT
HL7 Version: 2.5.1

-----BEGIN COMPOSITE_DATA_TYPE::SRT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    SRT,
    ID, ST
)

srt = SRT(  # Sort Order - Specifies those parameters by which the response will be sorted and by what method
    sort_by_field=st,  # ST(...)  # Required.
    sequencing=None,  # ID(...) 
)

-----END COMPOSITE_DATA_TYPE::SRT TEMPLATE-----
"""


class SRT(DataType):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """COMPOSITE_DATA_TYPE"""
    _hl7_length = 15
    _hl7_id = """SRT"""
    _hl7_name = """Sort Order"""
    _hl7_description = """Specifies those parameters by which the response will be sorted and by what method"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SRT"
    _c_length = (12, 2,)
    _c_rpt = (1, 1,)
    _c_usage = ("R", "O",)
    _c_aliases = ("SRT.1", "SRT.2",)
    _c_components = (ST, ID,)
    _c_names = ("Sort-by Field", "Sequencing",)
    _c_attrs = ("sort_by_field", "sequencing",)
    # fmt: on

    def __init__(
        self,
        sort_by_field: ST,  # SRT.1
        sequencing: Sequencing | ID | None = None,  # SRT.2
    ):
        """
                Sort Order - `SRT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRT>`_
                Specifies those parameters by which the response will be sorted and by what method.

        Example: In a tabular response query, where the return data is known by column name, the SRT might look like
        |LastName^A~FirstName^A|

                :param sort_by_field: Identifies the field by which the response will be sorted (id: SRT.1 | len: 12 | use: R | rpt: 1)
                :param sequencing: Identifies how the field or parameter will be sorted; and, if sorted, whether the sort will be case sensitive (the default) or not (id: SRT.2 | len: 2 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.sort_by_field = sort_by_field
        self.sequencing = sequencing

    @property  # get SRT.1
    def sort_by_field(self) -> ST:
        """
        id: SRT.1 | len: 12 | use: R | rpt: 1
        ---
        Identifies the field by which the response will be sorted. In a tabular response, this will be the column name to sort by. In the Segment Pattern and the Display Response, this will be the segment field name to sort by. See QIP in Section 2.A.59.1, "Segment Field Name (ST)" for segment field name definition.
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SRT.1
        """
        return self._c_data[0][0]

    @sort_by_field.setter  # set SRT.1
    def sort_by_field(self, st: ST):
        """
        id: SRT.1 | len: 12 | use: R | rpt: 1
        ---
        Identifies the field by which the response will be sorted. In a tabular response, this will be the column name to sort by. In the Segment Pattern and the Display Response, this will be the segment field name to sort by. See QIP in Section 2.A.59.1, "Segment Field Name (ST)" for segment field name definition.
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SRT.1
        """
        self._c_data[0] = (st,)

    @property  # get SRT.2
    def sequencing(self) -> Sequencing | None:
        """
        id: SRT.2 | len: 2 | use: O | rpt: 1
        ---
        Identifies how the field or parameter will be sorted; and, if sorted, whether the sort will be case sensitive (the default) or not. Refer to HL7 Table 0397 - Sequencing for valid values
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SRT.2
        """
        return self._c_data[1][0]

    @sequencing.setter  # set SRT.2
    def sequencing(self, sequencing: Sequencing | None):
        """
        id: SRT.2 | len: 2 | use: O | rpt: 1
        ---
        Identifies how the field or parameter will be sorted; and, if sorted, whether the sort will be case sensitive (the default) or not. Refer to HL7 Table 0397 - Sequencing for valid values
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/SRT.2
        """
        self._c_data[1] = (sequencing,)
