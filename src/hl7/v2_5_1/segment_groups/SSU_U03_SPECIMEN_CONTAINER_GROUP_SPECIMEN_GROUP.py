from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.SPM import SPM


"""
SPECIMEN - SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SPM, OBX
)

ssu_u03_specimen_container_group_specimen_group = SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for SSU_U03_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of SPM, OBX|None
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for SSU_U03_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of SPM, OBX|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("6", "7")
    _c_components = (SPM, OBX)
    _c_name = ("SPM", "OBX")
    _c_is_group = (False, False)
    _c_attrs = ("specimen", "observation_or_result",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.6
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.7
    ):
        """
        None - `SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SSU_U03_SPECIMEN_CONTAINER_GROUP_SPECIMEN_GROUP>`_
        Segment group for SSU_U03_SPECIMEN_CONTAINER_GROUP - SPECIMEN CONTAINER consisting of SPM, OBX|None

        :param specimen: Specimen (id: SPM | seq: 6 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 7 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen = specimen
        self.observation_or_result = observation_or_result

    @property  # get SPM.6
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 6
        ---
        return_type: SPM.6: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.6
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 6
        ---
        param_type: SPM.6: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: OBX.7 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)
