from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP import (
    RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP,
)
from ..segment_groups.RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP import (
    RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP,
)
from ..segments.ORC import ORC


"""
ORDER - RDR_RDR_DEFINITION_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RDR_RDR_DEFINITION_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RDR_RDR_DEFINITION_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP, RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP
)

rdr_rdr_definition_group_order_group = RDR_RDR_DEFINITION_GROUP_ORDER_GROUP(  # ORDER - Segment group for RDR_RDR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, DISPENSE
    common_order=orc,  # ORC(...)  # Required.
    encoding=None,  # RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP(...) 
    dispense=rdr_rdr_definition_group_order_group_dispense_group,  # RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RDR_RDR_DEFINITION_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RDR_RDR_DEFINITION_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RDR_RDR_DEFINITION_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RDR_RDR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, DISPENSE"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("9", "None", "None")
    _c_components = (ORC, RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP, RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP)
    _c_name = ("ORC", "ENCODING", "DISPENSE")
    _c_is_group = (False, True, True)
    _c_attrs = ("common_order", "encoding", "dispense",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.9
        dispense: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP
        | tuple[
            RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP, ...
        ],  #  Required. (RXD.13, RXR.14, RXC.15, ...)
        encoding: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.10, RXR.11, RXC.12
    ):
        """
        None - `RDR_RDR_DEFINITION_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP>`_
        Segment group for RDR_RDR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, DISPENSE

        :param common_order: Common Order (id: ORC | seq: 9 | use: R | rpt: 1)
        :param encoding: Encoding segment group: [RXE, RXR, RXC|None] (id: ENCODING | seq: 10, 11, 12 | use: O | rpt: 1)
        :param dispense: Dispense segment group: [RXD, RXR, RXC|None] (id: DISPENSE | seq: 13, 14, 15 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.common_order = common_order
        self.encoding = encoding
        self.dispense = dispense

    @property  # get ORC.9
    def common_order(self) -> ORC:
        """
        id: ORC | use: R | rpt: 1 | seq: 9
        ---
        return_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        return self._c_data[0][0]

    @common_order.setter  # set ORC.9
    def common_order(self, orc: ORC):
        """
        id: ORC | use: R | rpt: 1 | seq: 9
        ---
        param_type: ORC.9: Common Order
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORC
        """
        self._c_data[0] = (orc,)

    @property  # get RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[1][0]

    @encoding.setter  # set RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(
        self, encoding: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | None
    ):
        """
        id: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[1] = (encoding,)

    @property  # get DISPENSE
    def dispense(
        self,
    ) -> tuple[RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP, ...]:
        """
        id: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP
        """
        return self._c_data[2]

    @dispense.setter  # set DISPENSE
    def dispense(
        self,
        d_ispense: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP
        | tuple[RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP, ...],
    ):
        """
        id: DISPENSE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP.None | tuple[RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RDR_RDR_DEFINITION_GROUP_ORDER_GROUP_DISPENSE_GROUP
        """
        if isinstance(d_ispense, tuple):
            self._c_data[2] = d_ispense
        else:
            self._c_data[2] = (d_ispense,)
