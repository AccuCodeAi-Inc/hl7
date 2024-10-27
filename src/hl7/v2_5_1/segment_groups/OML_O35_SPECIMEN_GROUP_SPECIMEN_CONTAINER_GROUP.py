from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SAC import SAC
from ..segment_groups.OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP,
)


"""
SPECIMEN CONTAINER - OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
)

oml_o35_specimen_group_specimen_container_group = OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP(  # SPECIMEN CONTAINER - Segment group for OML_O35_SPECIMEN_GROUP - SPECIMEN consisting of SAC, ORDER
    specimen_container_detail=sac,  # SAC(...)  # Required.
    order=oml_o35_specimen_group_specimen_container_group_order_group,  # OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP TEMPLATE-----
"""


class OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP"""
    _hl7_name = """SPECIMEN CONTAINER"""
    _hl7_description = """Segment group for OML_O35_SPECIMEN_GROUP - SPECIMEN consisting of SAC, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "R")
    _c_aliases = ("17", "None")
    _c_components = (SAC, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP)
    _c_name = ("SAC", "ORDER")
    _c_is_group = (False, True)
    _c_attrs = ("specimen_container_detail", "order",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.17
        order: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...
        ],  #  Required. (ORC.18, FT1.40, CTI.41, BLG.42, ...)
    ):
        """
        None - `OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP>`_
        Segment group for OML_O35_SPECIMEN_GROUP - SPECIMEN consisting of SAC, ORDER

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 17 | use: R | rpt: 1)
        :param order: Order segment group: [ORC, TIIMING|None, OBSERVATION REQUEST|None, FT1|None, CTI|None, BLG|None] (id: ORDER | seq: 18, None, None, 40, 41, 42 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen_container_detail = specimen_container_detail
        self.order = order

    @property  # get SAC.17
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 17
        ---
        return_type: SAC.17: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.17
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 17
        ---
        param_type: SAC.17: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get ORDER
    def order(
        self,
    ) -> tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...]:
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP.None | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
