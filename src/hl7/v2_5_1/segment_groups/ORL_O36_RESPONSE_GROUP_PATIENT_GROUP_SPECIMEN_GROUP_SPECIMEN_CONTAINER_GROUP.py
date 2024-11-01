from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP,
)
from ..segments.SAC import SAC


"""
SPECIMEN CONTAINER - ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
)

orl_o36_response_group_patient_group_specimen_group_specimen_container_group = ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP(  # SPECIMEN CONTAINER - Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP - SPECIMEN consisting of SAC, ORDER|None
    specimen_container_detail=sac,  # SAC(...)  # Required.
    order=None,  # ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP TEMPLATE-----
"""


class ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP"""
    _hl7_name = """SPECIMEN CONTAINER"""
    _hl7_description = """Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP - SPECIMEN consisting of SAC, ORDER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("9", "None")
    _c_components = (SAC, ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP)
    _c_name = ("SAC", "ORDER")
    _c_is_group = (False, True)
    _c_attrs = ("specimen_container_detail", "order",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.9
        order: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP,
            ...,
        ]
        | None = None,  #  (ORC.10, ...)
    ):
        """
        None - `ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP>`_
        Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP - SPECIMEN consisting of SAC, ORDER|None

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 9 | use: R | rpt: 1)
        :param order: Order segment group: [ORC, TIMING|None, OBSERVATION REQUEST|None] (id: ORDER | seq: 10, None, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen_container_detail = specimen_container_detail
        self.order = order

    @property  # get SAC.9
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 9
        ---
        return_type: SAC.9: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.9
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 9
        ---
        param_type: SAC.9: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get ORDER
    def order(
        self,
    ) -> (
        tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        """
        return self._c_data[1]

    @order.setter  # set ORDER
    def order(
        self,
        order: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP.None | tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[1] = order
        else:
            self._c_data[1] = (order,)
