from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXR import RXR
from ..segments.RXA import RXA


"""
ADMINISTRATION - RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP
from utils.hl7.v2_5_1.segments import (
    RXA, RXR
)

rra_o18_response_group_order_group_administration_group = RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP(  # ADMINISTRATION - Segment group for RRA_O18_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXA, RXR
    pharmacy_or_treatment_administration=rxa,  # RXA(...)  # Required.
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP TEMPLATE-----
"""


class RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP"""
    _hl7_name = """ADMINISTRATION"""
    _hl7_description = """Segment group for RRA_O18_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXA, RXR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (65535, 1)
    _c_usage = ("R", "R")
    _c_aliases = ("11", "12")
    _c_components = (RXA, RXR)
    _c_name = ("RXA", "RXR")
    _c_is_group = (False, False)
    _c_attrs = ("pharmacy_or_treatment_administration", "pharmacy_or_treatment_route",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_administration: RXA
        | tuple[RXA, ...],  #  Required. RXA.11
        pharmacy_or_treatment_route: RXR,  #  Required. RXR.12
    ):
        """
        None - `RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRA_O18_RESPONSE_GROUP_ORDER_GROUP_ADMINISTRATION_GROUP>`_
        Segment group for RRA_O18_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXA, RXR

        :param pharmacy_or_treatment_administration: Pharmacy/Treatment Administration (id: RXA | seq: 11 | use: R | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 12 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.pharmacy_or_treatment_administration = pharmacy_or_treatment_administration
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route

    @property  # get RXA
    def pharmacy_or_treatment_administration(self) -> tuple[RXA, ...]:
        """
        id: RXA SEGMENT GROUP | use: R | rpt: * | seq: 11
        ---
        return_type: tuple[RXA, ...]: (Pharmacy/Treatment Administration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        return self._c_data[0]

    @pharmacy_or_treatment_administration.setter  # set RXA
    def pharmacy_or_treatment_administration(self, rxa: RXA | tuple[RXA, ...]):
        """
        id: RXA SEGMENT GROUP | use: R | rpt: * | seq: 11
        ---
        param_type: RXA.11 | tuple[RXA, ...]: (Pharmacy/Treatment Administration, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXA
        """
        if isinstance(rxa, tuple):
            self._c_data[0] = rxa
        else:
            self._c_data[0] = (rxa,)

    @property  # get RXR.12
    def pharmacy_or_treatment_route(self) -> RXR:
        """
        id: RXR | use: R | rpt: 1 | seq: 12
        ---
        return_type: RXR.12: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[1][0]

    @pharmacy_or_treatment_route.setter  # set RXR.12
    def pharmacy_or_treatment_route(self, rxr: RXR):
        """
        id: RXR | use: R | rpt: 1 | seq: 12
        ---
        param_type: RXR.12: Pharmacy/Treatment Route
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        self._c_data[1] = (rxr,)
