from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.RXC import RXC
from ..segments.NTE import NTE
from ..segments.RXD import RXD
from ..segments.RXR import RXR


"""
DISPENSE - RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, RXD, RXR, RXC
)

rrd_o14_response_group_order_group_dispense_group = RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP(  # DISPENSE - Segment group for RRD_O14_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXD, NTE|None, RXR, RXC|None
    pharmacy_or_treatment_dispense=rxd,  # RXD(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
    pharmacy_or_treatment_route=rxr,  # RXR(...)  # Required.
    pharmacy_or_treatment_component_order=None,  # RXC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP TEMPLATE-----
"""


class RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP"""
    _hl7_name = """DISPENSE"""
    _hl7_description = """Segment group for RRD_O14_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXD, NTE|None, RXR, RXC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O")
    _c_aliases = ("11", "12", "13", "14")
    _c_components = (RXD, NTE, RXR, RXC)
    _c_name = ("RXD", "NTE", "RXR", "RXC")
    _c_is_group = (False, False, False, False)
    _c_attrs = ("pharmacy_or_treatment_dispense", "notes_and_comments", "pharmacy_or_treatment_route", "pharmacy_or_treatment_component_order",)
    # fmt: on

    def __init__(
        self,
        pharmacy_or_treatment_dispense: RXD,  #  Required. RXD.11
        pharmacy_or_treatment_route: RXR | tuple[RXR, ...],  #  Required. RXR.13
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.12
        pharmacy_or_treatment_component_order: RXC
        | tuple[RXC, ...]
        | None = None,  #  RXC.14
    ):
        """
        None - `RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRD_O14_RESPONSE_GROUP_ORDER_GROUP_DISPENSE_GROUP>`_
        Segment group for RRD_O14_RESPONSE_GROUP_ORDER_GROUP - ORDER consisting of RXD, NTE|None, RXR, RXC|None

        :param pharmacy_or_treatment_dispense: Pharmacy/Treatment Dispense (id: RXD | seq: 11 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 12 | use: O | rpt: *)
        :param pharmacy_or_treatment_route: Pharmacy/Treatment Route (id: RXR | seq: 13 | use: R | rpt: *)
        :param pharmacy_or_treatment_component_order: Pharmacy/Treatment Component Order (id: RXC | seq: 14 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.pharmacy_or_treatment_dispense = pharmacy_or_treatment_dispense
        self.notes_and_comments = notes_and_comments
        self.pharmacy_or_treatment_route = pharmacy_or_treatment_route
        self.pharmacy_or_treatment_component_order = (
            pharmacy_or_treatment_component_order
        )

    @property  # get RXD.11
    def pharmacy_or_treatment_dispense(self) -> RXD:
        """
        id: RXD | use: R | rpt: 1 | seq: 11
        ---
        return_type: RXD.11: Pharmacy/Treatment Dispense
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD
        """
        return self._c_data[0][0]

    @pharmacy_or_treatment_dispense.setter  # set RXD.11
    def pharmacy_or_treatment_dispense(self, rxd: RXD):
        """
        id: RXD | use: R | rpt: 1 | seq: 11
        ---
        param_type: RXD.11: Pharmacy/Treatment Dispense
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXD
        """
        self._c_data[0] = (rxd,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: NTE.12 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)

    @property  # get RXR
    def pharmacy_or_treatment_route(self) -> tuple[RXR, ...]:
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        return_type: tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        return self._c_data[2]

    @pharmacy_or_treatment_route.setter  # set RXR
    def pharmacy_or_treatment_route(self, rxr: RXR | tuple[RXR, ...]):
        """
        id: RXR SEGMENT GROUP | use: R | rpt: * | seq: 13
        ---
        param_type: RXR.13 | tuple[RXR, ...]: (Pharmacy/Treatment Route, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXR
        """
        if isinstance(rxr, tuple):
            self._c_data[2] = rxr
        else:
            self._c_data[2] = (rxr,)

    @property  # get RXC
    def pharmacy_or_treatment_component_order(self) -> tuple[RXC, ...] | tuple[None]:
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        return self._c_data[3]

    @pharmacy_or_treatment_component_order.setter  # set RXC
    def pharmacy_or_treatment_component_order(self, rxc: RXC | tuple[RXC, ...] | None):
        """
        id: RXC SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: RXC.14 | tuple[RXC, ...]: (Pharmacy/Treatment Component Order, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RXC
        """
        if isinstance(rxc, tuple):
            self._c_data[3] = rxc
        else:
            self._c_data[3] = (rxc,)
