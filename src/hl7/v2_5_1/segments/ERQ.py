from __future__ import annotations
from ...base import HL7Segment
from ..data_types.CE import CE
from ..data_types.ST import ST
from ..data_types.QIP import QIP


"""
Event replay query - ERQ
HL7 Version: 2.5.1

-----BEGIN SEGMENT::ERQ TEMPLATE-----

from utils.hl7.v2_5_1.data_type import (
    ERQ,
    CE, ST, QIP
)

erq = ERQ(  #  - This segment is not carried forward to the recommended queries for v 2
    query_tag=None,  # ST(...) 
    event_identifier=ce,  # CE(...)  # Required.
    input_parameter_list=None,  # QIP(...) 
)

-----END SEGMENT::ERQ TEMPLATE-----
"""


class ERQ(HL7Segment):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = "SEGMENT"
    _hl7_length = -1
    _hl7_id = """ERQ"""
    _hl7_name = """Event replay query"""
    _hl7_description = """This segment is not carried forward to the recommended queries for v 2"""
    _hl7_ref_url = "https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERQ"
    _c_length = (32, 250, 256,)
    _c_rpt = (1, 1, 65535,)
    _c_usage = ("O", "R", "O",)
    _c_components = (ST, CE, QIP,)
    _c_aliases = ("ERQ.1", "ERQ.2", "ERQ.3",)
    _c_names = ("Query Tag", "Event Identifier", "Input Parameter List",)
    _c_attrs = ("query_tag", "event_identifier", "input_parameter_list",)
    # fmt: on

    def __init__(
        self,
        event_identifier: CE,  # ERQ.2
        query_tag: ST | None = None,  # ERQ.1
        input_parameter_list: QIP | None = None,  # ERQ.3
    ):
        """
        Event replay query - `ERQ <https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERQ>`_
        This segment is not carried forward to the recommended queries for v 2.4.

        :param query_tag: String Data (id: ERQ.1 | len: 32 | use: O | rpt: 1)
        :param event_identifier: Coded Element (id: ERQ.2 | len: 250 | use: R | rpt: 1)
        :param input_parameter_list: Query Input Parameter List (id: ERQ.3 | len: 256 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.query_tag = query_tag
        self.event_identifier = event_identifier
        self.input_parameter_list = input_parameter_list

    @property  # get ERQ.1
    def query_tag(self) -> ST | None:
        """
        id: ERQ.1 | len: 32 | use: O | rpt: 1
        ---
        return_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERQ.1
        """
        return self._c_data[0][0]

    @query_tag.setter  # set ERQ.1
    def query_tag(self, st: ST | None):
        """
        id: ERQ.1 | len: 32 | use: O | rpt: 1
        ---
        param_type: ST: String Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERQ.1
        """
        self._c_data[0] = (st,)

    @property  # get ERQ.2
    def event_identifier(self) -> CE:
        """
        id: ERQ.2 | len: 250 | use: R | rpt: 1
        ---
        return_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERQ.2
        """
        return self._c_data[1][0]

    @event_identifier.setter  # set ERQ.2
    def event_identifier(self, ce: CE):
        """
        id: ERQ.2 | len: 250 | use: R | rpt: 1
        ---
        param_type: CE: Coded Element
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERQ.2
        """
        self._c_data[1] = (ce,)

    @property
    def input_parameter_list(self) -> tuple[QIP, ...] | tuple[None]:
        """
        id: ERQ.3 | len: 256 | use: O | rpt: *
        ---
        return_type: tuple[QIP, ...]: (Query Input Parameter List, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERQ.3
        """
        return self._c_data[2]

    @input_parameter_list.setter  # set ERQ.3
    def input_parameter_list(self, qip: QIP | tuple[QIP] | None):
        """
        id: ERQ.3 | len: 256 | use: O | rpt: *
        ---
        param_type: QIP | tuple[QIP, ...]: (Query Input Parameter List, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/DataTypes/ERQ.3
        """
        if isinstance(qip, tuple):
            self._c_data[2] = qip
        else:
            self._c_data[2] = (qip,)
