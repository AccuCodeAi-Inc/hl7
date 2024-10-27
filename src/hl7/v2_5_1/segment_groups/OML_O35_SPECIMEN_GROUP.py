from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.SPM import SPM
from ..segment_groups.OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP,
)


"""
SPECIMEN - OML_O35_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OML_O35_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SPM, OBX
)
from utils.hl7.v2_5_1.segment_groups import (
    OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
)

oml_o35_specimen_group = OML_O35_SPECIMEN_GROUP(  # SPECIMEN - Segment group for OML_O35 - Laboratory Order for Multiple Orders Related to a Single Container of a Specimen consisting of SPM, OBX|None, SPECIMEN CONTAINER
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    specimen_container=oml_o35_specimen_group_specimen_container_group,  # OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::OML_O35_SPECIMEN_GROUP TEMPLATE-----
"""


class OML_O35_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """OML_O35_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for OML_O35 - Laboratory Order for Multiple Orders Related to a Single Container of a Specimen consisting of SPM, OBX|None, SPECIMEN CONTAINER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("15", "16", "None")
    _c_components = (SPM, OBX, OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP)
    _c_name = ("SPM", "OBX", "SPECIMEN CONTAINER")
    _c_is_group = (False, False, True)
    _c_attrs = ("specimen", "observation_or_result", "specimen_container",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.15
        specimen_container: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        | tuple[
            OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...
        ],  #  Required. (SAC.17, ...)
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.16
    ):
        """
        None - `OML_O35_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OML_O35_SPECIMEN_GROUP>`_
        Segment group for OML_O35 - Laboratory Order for Multiple Orders Related to a Single Container of a Specimen consisting of SPM, OBX|None, SPECIMEN CONTAINER

        :param specimen: Specimen (id: SPM | seq: 15 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 16 | use: O | rpt: *)
        :param specimen_container: Specimen Container segment group: [SAC, ORDER] (id: SPECIMEN CONTAINER | seq: 17, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.specimen_container = specimen_container

    @property  # get SPM.15
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 15
        ---
        return_type: SPM.15: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.15
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 15
        ---
        param_type: SPM.15: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: OBX.16 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)

    @property  # get SPECIMEN CONTAINER
    def specimen_container(
        self,
    ) -> tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...]:
        """
        id: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        return self._c_data[2]

    @specimen_container.setter  # set SPECIMEN CONTAINER
    def specimen_container(
        self,
        specimen_container: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...],
    ):
        """
        id: SPECIMEN CONTAINER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP.None | tuple[OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OML_O35_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        if isinstance(specimen_container, tuple):
            self._c_data[2] = specimen_container
        else:
            self._c_data[2] = (specimen_container,)
