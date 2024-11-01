from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.SAC import SAC


"""
CONTAINER - OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, OBX
)

oml_o21_order_group_observation_request_group_specimen_group_container_group = OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP(  # CONTAINER - Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP - SPECIMEN consisting of SAC, OBX|None
    specimen_container_detail=sac,  # SAC(...)  # Required.
    observation_or_result=None,  # OBX(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP TEMPLATE-----
"""


class OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP"""
    _hl7_name = """CONTAINER"""
    _hl7_description = """Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP - SPECIMEN consisting of SAC, OBX|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("28", "29")
    _c_components = (SAC, OBX)
    _c_name = ("SAC", "OBX")
    _c_is_group = (False, False)
    _c_attrs = ("specimen_container_detail", "observation_or_result",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.28
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.29
    ):
        """
        None - `OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP>`_
        Segment group for OML_O21_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP - SPECIMEN consisting of SAC, OBX|None

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 28 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 29 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen_container_detail = specimen_container_detail
        self.observation_or_result = observation_or_result

    @property  # get SAC.28
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 28
        ---
        return_type: SAC.28: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.28
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 28
        ---
        param_type: SAC.28: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        param_type: OBX.29 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)
