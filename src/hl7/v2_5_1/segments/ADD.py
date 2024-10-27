from __future__ import annotations
from ...base import HL7Segment
from ..data_types.ST import ST


"""
Addendum - ADD
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ADD TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ADD,
    ST
)

add = ADD(  #  - The ADD segment is used to define the continuation of the prior segment in a continuation message
    addendum_continuation_pointer=None,  # ST(...) 
)

-----END SEGMENT::ADD TEMPLATE-----
"""


class ADD(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ADD"""
    _hl7_name = """Addendum"""
    _hl7_description = """The ADD segment is used to define the continuation of the prior segment in a continuation message"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADD"
    _c_length = (65536,)
    _c_rpt = (1,)
    _c_usage = ("O",)
    _c_components = (ST,)
    _c_aliases = ("ADD.1",)
    _c_names = ("Addendum Continuation Pointer",)
    _c_attrs = ("addendum_continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        addendum_continuation_pointer: ST | None = None,  # ADD.1
    ):
        """
        Addendum - `ADD <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADD>`_
        The ADD segment is used to define the continuation of the prior segment in a continuation message.

        :param addendum_continuation_pointer: String Data (id: ADD.1 | len: 65536 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 1
        self.addendum_continuation_pointer = addendum_continuation_pointer

    @property  # get ADD.1
    def addendum_continuation_pointer(self) -> ST | None:
        """
        id: ADD.1 | len: 65536 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ADD.1
        """
        return self._c_data[0][0]

    @addendum_continuation_pointer.setter  # set ADD.1
    def addendum_continuation_pointer(self, st: ST | None):
        """
        id: ADD.1 | len: 65536 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ADD.1
        """
        self._c_data[0] = (st,)
