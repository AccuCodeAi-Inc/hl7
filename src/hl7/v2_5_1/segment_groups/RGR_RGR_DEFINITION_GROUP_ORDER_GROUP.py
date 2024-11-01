from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXG import RXG
from ..segments.RXR import RXR
from ..segment_groups.RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP import (
    RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP,
)
from ..segments.RXC import RXC
from ..segments.ORC import ORC


"""
ORDER - RGR_RGR_DEFINITION_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RGR_RGR_DEFINITION_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RGR_RGR_DEFINITION_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXR, RXC, ORC, RXG
)
from utils.hl7.v2_5_1.segment_groups import (
    RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
)

rgr_rgr_definition_group_order_group = RGR_RGR_DEFINITION_GROUP_ORDER_GROUP(  # ORDER - Segment group for RGR_RGR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, RXG, RXR, RXC|None
    common_order=orc,  # ORC(...)  # Required.
    encoding=None,  # RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP(...) 
    pharmacy_or_treatment_give=rxg,  # RXG(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RGR_RGR_DEFINITION_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RGR_RGR_DEFINITION_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RGR_RGR_DEFINITION_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RGR_RGR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, RXG, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGR_RGR_DEFINITION_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O")
    _c_aliases = ("9", "None", "13", "14", "15")
    _c_components = (ORC, RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP, RXG, RXR, RXC)
    _c_name = ("ORC", "ENCODING", "RXG", "RXR", "RXC")
    _c_is_group = (False, True, False, False, False)
    _c_attrs = ("common_order", "encoding", "pharmacy_or_treatment_give", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.9
        pharmacy_or_treatment_give: RXG | tuple[RXG, ...],  #  Required. RXG.13
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.14
        encoding: RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.10, RXR.11, RXC.12
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.15
    ):
        """
        None - `RGR_RGR_DEFINITION_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RGR_RGR_DEFINITION_GROUP_ORDER_GROUP>`_
        Segment group for RGR_RGR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, RXG, RXR, RXC|None

        :param common_order: Common Order (id: ORC | seq: 9 | use: R | rpt: 1)
        :param encoding: Encoding segment group: [RXE, RXR, RXC|None] (id: ENCODING | seq: 10, 11, 12 | use: O | rpt: 1)
        :param pharmacy_or_treatment_give: Pharmacy/Treatment Give (id: RXG | seq: 13 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 14 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.common_order = common_order
        self.encoding = encoding
        self.pharmacy_or_treatment_give = pharmacy_or_treatment_give
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

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

    @property  # get RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[1][0]

    @encoding.setter  # set RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(
        self, encoding: RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | None
    ):
        """
        id: RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RGR_RGR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[1] = (encoding,)

    @property  # get RXG
    def pharmacy_or_treatment_give(self) -> tuple[RXG, ...]:
        """
        id: RXG SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[RXG, ...]: (Pharmacy/Treatment Give, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        return self._c_data[2]

    @pharmacy_or_treatment_give.setter  # set RXG
    def pharmacy_or_treatment_give(self, rxg: RXG | tuple[RXG, ...]):
        """
        id: RXG SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: RXG.13 | tuple[RXG, ...]: (Pharmacy/Treatment Give, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXG
        """
        if isinstance(rxg, tuple):
            self._c_data[2] = rxg
        else:
            self._c_data[2] = (rxg,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[3]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 14
        ---
        param_type: RXR.14 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[3] = rxr
        else:
            self._c_data[3] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[4]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: RXC.15 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[4] = rxc
        else:
            self._c_data[4] = (rxc,)
