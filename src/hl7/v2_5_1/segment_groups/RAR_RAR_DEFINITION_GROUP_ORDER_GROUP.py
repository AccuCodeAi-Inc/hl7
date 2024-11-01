from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segment_groups.RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP import (
    RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP,
)
from ..segments.RXA import RXA
from ..segments.ORC import ORC


"""
ORDER - RAR_RAR_DEFINITION_GROUP_ORDER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RAR_RAR_DEFINITION_GROUP_ORDER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RAR_RAR_DEFINITION_GROUP_ORDER_GROUP
from utils.hl7.v2_5_1.segments import (
    RXA, RXR, ORC
)
from utils.hl7.v2_5_1.segment_groups import (
    RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
)

rar_rar_definition_group_order_group = RAR_RAR_DEFINITION_GROUP_ORDER_GROUP(  # ORDER - Segment group for RAR_RAR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, RXA, RXR
    common_order=orc,  # ORC(...)  # Required.
    encoding=None,  # RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP(...) 
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RAR_RAR_DEFINITION_GROUP_ORDER_GROUP TEMPLATE-----
"""


class RAR_RAR_DEFINITION_GROUP_ORDER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RAR_RAR_DEFINITION_GROUP_ORDER_GROUP"""
    _hl7_name = """ORDER"""
    _hl7_description = """Segment group for RAR_RAR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, RXA, RXR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAR_RAR_DEFINITION_GROUP_ORDER_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1)
    _c_usage = ("R", "O", "R", "R")
    _c_aliases = ("9", "None", "13", "14")
    _c_components = (ORC, RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP, RXA, RXR)
    _c_name = ("ORC", "ENCODING", "RXA", "RXR")
    _c_is_group = (False, True, False, False)
    _c_attrs = ("common_order", "encoding", "pharmacy_or_treatment_administration", "pharmacy_or_treatment_route",)
    # fmt: on

    def __init__(
        self,
        common_order: ORC,  #  Required. ORC.9
        pharmacy_or_treatment_administration: RXA
        | tuple[RXA, ...],  #  Required. RXA.13
        pharmacy_or_treatment_route: RXR,  #  Required. RXR.14
        encoding: RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        | None = None,  #  RXE.10, RXR.11, RXC.12
    ):
        """
        None - `RAR_RAR_DEFINITION_GROUP_ORDER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RAR_RAR_DEFINITION_GROUP_ORDER_GROUP>`_
        Segment group for RAR_RAR_DEFINITION_GROUP - DEFINITION consisting of ORC, ENCODING|None, RXA, RXR

        :param common_order: Common Order (id: ORC | seq: 9 | use: R | rpt: 1)
        :param encoding: Encoding segment group: [RXE, RXR, RXC|None] (id: ENCODING | seq: 10, 11, 12 | use: O | rpt: 1)
        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 13 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 14 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.common_order = common_order
        self.encoding = encoding
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route

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

    @property  # get RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(self) -> RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | None:
        """
        id: RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        return self._c_data[1][0]

    @encoding.setter  # set RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None
    def encoding(
        self, encoding: RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | None
    ):
        """
        id: RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RAR_RAR_DEFINITION_GROUP_ORDER_GROUP_ENCODING_GROUP
        """
        self._c_data[1] = (encoding,)

    @property  # get RXA
    def pharmacy_or_treatment_administration(self) -> tuple[RXA, ...]:
        """
        id: RXA SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[RXA, ...]: (Pharmacy/Treatment Administration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[2]

    @pharmacy_or_treatment_administration.setter  # set RXA
    def pharmacy_or_treatment_administration(self, rxa: RXA | tuple[RXA, ...]):
        """
        id: RXA SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: RXA.13 | tuple[RXA, ...]: (Pharmacy/Treatment Administration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        if isinstance(rxa, tuple):
            self._c_data[2] = rxa
        else:
            self._c_data[2] = (rxa,)

    @property  # get RXR.14
    def pharmacy_or_treatment_route(self) -> RXR:
        """
        id: RXR | use: R | rpt: 1 | seq: 14
        ---
        return_type: RXR.14: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[3][0]

    @pharmacy_or_treatment_route.setter  # set RXR.14
    def pharmacy_or_treatment_route(self, rxr: RXR):
        """
        id: RXR | use: R | rpt: 1 | seq: 14
        ---
        param_type: RXR.14: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[3] = (rxr,)
