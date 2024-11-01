from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segment_groups.OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP import (
    OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP,
)
from ..segments.SPM import SPM
from ..segment_groups.OUL_R22_SPECIMEN_GROUP_ORDER_GROUP import (
    OUL_R22_SPECIMEN_GROUP_ORDER_GROUP,
)


"""
SPECIMEN - OUL_R22_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R22_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R22_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, SPM
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
)

oul_r22_specimen_group = OUL_R22_SPECIMEN_GROUP(  # SPECIMEN - Segment group for OUL_R22 - Unsolicited Specimen Oriented Observation Message consisting of SPM, OBX|None, CONTAINER|None, ORDER
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    container=None,  # OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP(...) 
    order=oul_r22_specimen_group_order_group,  # OUL_R22_SPECIMEN_GROUP_ORDER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R22_SPECIMEN_GROUP TEMPLATE-----
"""


class OUL_R22_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R22_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for OUL_R22 - Unsolicited Specimen Oriented Observation Message consisting of SPM, OBX|None, CONTAINER|None, ORDER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R22_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "R")
    _c_aliases = ("9", "10", "None", "None")
    _c_components = (SPM, OBX, OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, OUL_R22_SPECIMEN_GROUP_ORDER_GROUP)
    _c_name = ("SPM", "OBX", "CONTAINER", "ORDER")
    _c_is_group = (False, False, True, True)
    _c_attrs = ("specimen", "observation_or_result", "container", "order",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.9
        order: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
        | tuple[
            OUL_R22_SPECIMEN_GROUP_ORDER_GROUP, ...
        ],  #  Required. (OBR.13, ORC.14, NTE.15, CTI.22, ...)
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.10
        container: OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, ...]
        | None = None,  #  (SAC.11, INV.12, ...)
    ):
        """
        None - `OUL_R22_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R22_SPECIMEN_GROUP>`_
        Segment group for OUL_R22 - Unsolicited Specimen Oriented Observation Message consisting of SPM, OBX|None, CONTAINER|None, ORDER

        :param specimen: Specimen (id: SPM | seq: 9 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 10 | use: O | rpt: *)
        :param container: Container segment group: [SAC, INV|None] (id: CONTAINER | seq: 11, 12 | use: O | rpt: *)
        :param order: Order segment group: [OBR, ORC|None, NTE|None, TIMING QTY|None, RESULT|None, CTI|None] (id: ORDER | seq: 13, 14, 15, None, None, 22 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.container = container
        self.order = order

    @property  # get SPM.9
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 9
        ---
        return_type: SPM.9: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.9
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 9
        ---
        param_type: SPM.9: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: OBX.10 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)

    @property  # get CONTAINER
    def container(
        self,
    ) -> tuple[OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, ...] | tuple[None]:
        """
        id: OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP
        """
        return self._c_data[2]

    @container.setter  # set CONTAINER
    def container(
        self,
        container: OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, ...]
        | None,
    ):
        """
        id: CONTAINER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP.None | tuple[OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_CONTAINER_GROUP
        """
        if isinstance(container, tuple):
            self._c_data[2] = container
        else:
            self._c_data[2] = (container,)

    @property  # get ORDER
    def order(self) -> tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP, ...]:
        """
        id: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
        """
        return self._c_data[3]

    @order.setter  # set ORDER
    def order(
        self,
        order: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
        | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP, ...],
    ):
        """
        id: ORDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OUL_R22_SPECIMEN_GROUP_ORDER_GROUP.None | tuple[OUL_R22_SPECIMEN_GROUP_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R22_SPECIMEN_GROUP_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[3] = order
        else:
            self._c_data[3] = (order,)
