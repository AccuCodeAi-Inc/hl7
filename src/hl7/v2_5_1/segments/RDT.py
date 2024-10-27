from __future__ import annotations
from ...base import HL7Segment
from ..data_types.VARIES import VARIES


"""
Table Row Data - RDT
HL7 Version: 2.5.1

-----BEGIN SEGMENT::RDT TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    RDT,
    VARIES
)

rdt = RDT(  #  - The RDT segment contains the row data of the tabular data response message (TBR)
    column_value=varies,  # VARIES(...)  # Required.
)

-----END SEGMENT::RDT TEMPLATE-----
"""


class RDT(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """RDT"""
    _hl7_name = """Table Row Data"""
    _hl7_description = """The RDT segment contains the row data of the tabular data response message (TBR)"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDT"
    _c_length = (99999,)
    _c_rpt = (1,)
    _c_usage = ("R",)
    _c_components = (VARIES,)
    _c_aliases = ("RDT.1",)
    _c_names = ("Column Value",)
    _c_attrs = ("column_value",)
    # fmt: on

    def __init__(
        self,
        column_value: VARIES,  # RDT.1
    ):
        """
        Table Row Data - `RDT <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDT>`_
        The RDT segment contains the row data of the tabular data response message (TBR).

        :param column_value: Variable Datatype (id: RDT.1 | len: 99999 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 1
        self.column_value = column_value

    @property  # get RDT.1
    def column_value(self) -> VARIES:
        """
        id: RDT.1 | len: 99999 | use: R | rpt: 1
        ---
        return_type: VARIES: Variable Datatype
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RDT.1
        """
        return self._c_data[0][0]

    @column_value.setter  # set RDT.1
    def column_value(self, varies: VARIES):
        """
        id: RDT.1 | len: 99999 | use: R | rpt: 1
        ---
        param_type: VARIES: Variable Datatype
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/RDT.1
        """
        self._c_data[0] = (varies,)
