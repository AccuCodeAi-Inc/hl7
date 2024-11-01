from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP import (
    SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP,
)
from ..segments.OBX import OBX
from ..segments.SAC import SAC


"""
SPECIMEN CONTAINER - SSU_U03_SPECIMEN_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SSU_U03_SPECIMEN_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SSU_U03_SPECIMEN_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, OBX
)
from utils.hl7.v2_5_1.segment_groups import (
    SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
)

ssu_u03_specimen_container_group = SSU_U03_SPECIMEN_CONTAINER_GROUP(  # SPECIMEN CONTAINER - Segment group for SSU_U03 - Specimen status update consisting of SAC, OBX|None, SPECIMEN|None
    specimen_container_detail=sac,  # SAC(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    specimen=None,  # SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SSU_U03_SPECIMEN_CONTAINER_GROUP TEMPLATE-----
"""


class SSU_U03_SPECIMEN_CONTAINER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SSU_U03_SPECIMEN_CONTAINER_GROUP"""
    _hl7_name = """SPECIMEN CONTAINER"""
    _hl7_description = """Segment group for SSU_U03 - Specimen status update consisting of SAC, OBX|None, SPECIMEN|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SSU_U03_SPECIMEN_CONTAINER_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("4", "5", "None")
    _c_components = (SAC, OBX, SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP)
    _c_name = ("SAC", "OBX", "SPECIMEN")
    _c_is_group = (False, False, True)
    _c_attrs = ("specimen_container_detail", "observation_or_result", "specimen",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.4
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.5
        specimen: SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
        | tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP, ...]
        | None = None,  #  (SPM.6, OBX.7, ...)
    ):
        """
        None - `SSU_U03_SPECIMEN_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SSU_U03_SPECIMEN_CONTAINER_GROUP>`_
        Segment group for SSU_U03 - Specimen status update consisting of SAC, OBX|None, SPECIMEN|None

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 4 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 5 | use: O | rpt: *)
        :param specimen: Specimen segment group: [SPM, OBX|None] (id: SPECIMEN | seq: 6, 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.specimen_container_detail = specimen_container_detail
        self.observation_or_result = observation_or_result
        self.specimen = specimen

    @property  # get SAC.4
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 4
        ---
        return_type: SAC.4: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.4
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 4
        ---
        param_type: SAC.4: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: OBX.5 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP, ...] | tuple[None]:
        """
        id: SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[2]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
        | tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP, ...]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP.None | tuple[SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[2] = specimen
        else:
            self._c_data[2] = (specimen,)
