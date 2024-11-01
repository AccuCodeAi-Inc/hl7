from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ID import ID
from ..data_types.ST import ST
from ..tables.ContinuationStyleCode import ContinuationStyleCode


"""
Continuation Pointer - DSC
HL7 Version: 2.5.1

-----BEGIN SEGMENT::DSC TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    DSC,
    ID, ST
)

dsc = DSC(  #  - The DSC segment is used in the continuation protocol
    continuation_pointer=None,  # ST(...) 
    continuation_style=None,  # ID(...) 
)

-----END SEGMENT::DSC TEMPLATE-----
"""


class DSC(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """DSC"""
    _hl7_name = """Continuation Pointer"""
    _hl7_description = """The DSC segment is used in the continuation protocol"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC"
    _c_length = (180, 1,)
    _c_rpt = (1, 1,)
    _c_usage = ("O", "O",)
    _c_components = (ST, ID,)
    _c_aliases = ("DSC.1", "DSC.2",)
    _c_names = ("Continuation Pointer", "Continuation Style",)
    _c_attrs = ("continuation_pointer", "continuation_style",)
    # fmt: on

    def __init__(
        self,
        continuation_pointer: ST | tuple[ST] | None = None,  # DSC.1
        continuation_style: ContinuationStyleCode
        | ID
        | tuple[ContinuationStyleCode | ID]
        | None = None,  # DSC.2
    ):
        """
        Continuation Pointer - `DSC <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC>`_
        The DSC segment is used in the continuation protocol.

        :param continuation_pointer: String Data (id: DSC.1 | len: 180 | use: O | rpt: 1)
        :param continuation_style: Coded values for HL7 tables (id: DSC.2 | len: 1 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.continuation_pointer = continuation_pointer
        self.continuation_style = continuation_style

    @property  # get DSC.1
    def continuation_pointer(self) -> ST | None:
        """
        id: DSC.1 | len: 180 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSC.1
        """
        return self._c_data[0][0]

    @continuation_pointer.setter  # set DSC.1
    def continuation_pointer(self, st: ST | None):
        """
        id: DSC.1 | len: 180 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSC.1
        """
        self._c_data[0] = (st,)

    @property  # get DSC.2
    def continuation_style(self) -> ContinuationStyleCode | None:
        """
        id: DSC.2 | len: 1 | use: O | rpt: 1
        ---
        return_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSC.2
        """
        return self._c_data[1][0]

    @continuation_style.setter  # set DSC.2
    def continuation_style(self, continuation_style_code: ContinuationStyleCode | None):
        """
        id: DSC.2 | len: 1 | use: O | rpt: 1
        ---
        param_type: ID: Coded values for HL7 tables
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/DSC.2
        """
        self._c_data[1] = (continuation_style_code,)
