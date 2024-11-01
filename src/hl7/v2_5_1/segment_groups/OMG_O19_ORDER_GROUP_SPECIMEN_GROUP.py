from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.SPM import SPM
from ..segment_groups.OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP import (
    OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP,
)


"""
SPECIMEN - OMG_O19_ORDER_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OMG_O19_ORDER_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, SPM
)
from utils.hl7.v2_5_1.segment_groups import (
    OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
)

omg_o19_order_group_specimen_group = OMG_O19_ORDER_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for OMG_O19_ORDER_GROUP - ORDER consisting of SPM, OBX|None, CONTAINER|None
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    container=None,  # OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OMG_O19_ORDER_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class OMG_O19_ORDER_GROUP_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OMG_O19_ORDER_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for OMG_O19_ORDER_GROUP - ORDER consisting of SPM, OBX|None, CONTAINER|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("24", "25", "None")
    _c_components = (SPM, OBX, OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP)
    _c_name = ("SPM", "OBX", "CONTAINER")
    _c_is_group = (False, False, True)
    _c_attrs = ("specimen", "observation_or_result", "container",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.24
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.25
        container: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
        | tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP, ...]
        | None = None,  #  (SAC.26, OBX.27, ...)
    ):
        """
        None - `OMG_O19_ORDER_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OMG_O19_ORDER_GROUP_SPECIMEN_GROUP>`_
        Segment group for OMG_O19_ORDER_GROUP - ORDER consisting of SPM, OBX|None, CONTAINER|None

        :param specimen: Specimen (id: SPM | seq: 24 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 25 | use: O | rpt: *)
        :param container: Container segment group: [SAC, OBX|None] (id: CONTAINER | seq: 26, 27 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.container = container

    @property  # get SPM.24
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 24
        ---
        return_type: SPM.24: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.24
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 24
        ---
        param_type: SPM.24: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 25
        ---
        param_type: OBX.25 | tuple[OBX, ...]: (Observation/Result, ...)
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
    ) -> tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP, ...] | tuple[None]:
        """
        id: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
        """
        return self._c_data[2]

    @container.setter  # set CONTAINER
    def container(
        self,
        container: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
        | tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP, ...]
        | None,
    ):
        """
        id: CONTAINER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP.None | tuple[OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OMG_O19_ORDER_GROUP_SPECIMEN_GROUP_CONTAINER_GROUP
        """
        if isinstance(container, tuple):
            self._c_data[2] = container
        else:
            self._c_data[2] = (container,)
