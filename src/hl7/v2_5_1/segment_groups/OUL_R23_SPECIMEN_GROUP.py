from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SPM import SPM
from ..segment_groups.OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP import (
    OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP,
)
from ..segments.OBX import OBX


"""
SPECIMEN - OUL_R23_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OUL_R23_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R23_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SPM, OBX
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
)

oul_r23_specimen_group = OUL_R23_SPECIMEN_GROUP(  # SPECIMEN - Segment group for OUL_R23 - Unsolicited Specimen Container Oriented Observation Message consisting of SPM, OBX|None, CONTAINER
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    container=oul_r23_specimen_group_container_group,  # OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OUL_R23_SPECIMEN_GROUP TEMPLATE-----
"""


class OUL_R23_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OUL_R23_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for OUL_R23 - Unsolicited Specimen Container Oriented Observation Message consisting of SPM, OBX|None, CONTAINER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("9", "10", "None")
    _c_components = (SPM, OBX, OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP)
    _c_name = ("SPM", "OBX", "CONTAINER")
    _c_is_group = (False, False, True)
    _c_attrs = ("specimen", "observation_or_result", "container",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.9
        container: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
        | tuple[
            OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP, ...
        ],  #  Required. (SAC.11, INV.12, ...)
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.10
    ):
        """
        None - `OUL_R23_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23_SPECIMEN_GROUP>`_
        Segment group for OUL_R23 - Unsolicited Specimen Container Oriented Observation Message consisting of SPM, OBX|None, CONTAINER

        :param specimen: Specimen (id: SPM | seq: 9 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 10 | use: O | rpt: *)
        :param container: Container segment group: [SAC, INV|None, ORDER] (id: CONTAINER | seq: 11, 12, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.container = container

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
    def container(self) -> tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP, ...]:
        """
        id: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
        """
        return self._c_data[2]

    @container.setter  # set CONTAINER
    def container(
        self,
        container: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
        | tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP, ...],
    ):
        """
        id: CONTAINER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP.None | tuple[OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_SPECIMEN_GROUP_CONTAINER_GROUP
        """
        if isinstance(container, tuple):
            self._c_data[2] = container
        else:
            self._c_data[2] = (container,)
