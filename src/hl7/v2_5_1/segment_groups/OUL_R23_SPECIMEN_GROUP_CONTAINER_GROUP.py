from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.INV import INV
from ..segment_groups.OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP import (
    OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP,
)
from ..segments.SAC import SAC


"""
CONTAINER - OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, INV
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP
)

oul_r23_specimen_group_container_group = OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP(  # CONTAINER - Segment group for OUL_R23_SPECIMEN_GROUP - SPECIMEN consisting of SAC, INV|None, ORDER
    specimen_container_detail=sac,  # SAC(...)  # Required.
    inventory_detail=None,  # INV(...) 
    order=oul_r23_specimen_group_container_group_order_group,  # OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP TEMPLATE-----
"""


class OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP"""
    _hl7_name = """CONTAINER"""
    _hl7_description = """Segment group for OUL_R23_SPECIMEN_GROUP - SPECIMEN consisting of SAC, INV|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("11", "12", "None")
    _c_components = (SAC, INV, OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP)
    _c_name = ("SAC", "INV", "ORDER")
    _c_is_group = (False, False, True)
    _c_attrs = ("specimen_container_detail", "inventory_detail", "order",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.11
        order: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP
        | tuple[
            OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP, ...
        ],  #  Required. (OBR.13, ORC.14, NTE.15, CTI.22, ...)
        inventory_detail: INV | None = None,  #  INV.12
    ):
        """
        None - `OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP>`_
        Segment group for OUL_R23_SPECIMEN_GROUP - SPECIMEN consisting of SAC, INV|None, ORDER

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 11 | use: R | rpt: 1)
        :param inventory_detail: Inventory Detail (id: INV | seq: 12 | use: O | rpt: 1)
        :param order: Order segment group: [OBR, ORC|None, NTE|None, TIMING QTY|None, RESULT|None, CTI|None] (id: ORDER | seq: 13, 14, 15, None, None, 22 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.specimen_container_detail = specimen_container_detail
        self.inventory_detail = inventory_detail
        self.order = order

    @property  # get SAC.11
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 11
        ---
        return_type: SAC.11: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.11
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 11
        ---
        param_type: SAC.11: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get INV.12
    def inventory_detail(self) -> INV | None:
        """
        id: INV | use: O | rpt: 1 | seq: 12
        ---
        return_type: INV.12: Inventory Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/INV
        """
        return self._c_data[1][0]

    @inventory_detail.setter  # set INV.12
    def inventory_detail(self, inv: INV | None):
        """
        id: INV | use: O | rpt: 1 | seq: 12
        ---
        param_type: INV.12: Inventory Detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/INV
        """
        self._c_data[1] = (inv,)

    @property  # get ORDER
    def order(self) -> tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP, ...]:
        """
        id: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP
        """
        return self._c_data[2]

    @order.setter  # set ORDER
    def order(
        self,
        order: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP
        | tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP.None | tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[2] = order
        else:
            self._c_data[2] = (order,)
