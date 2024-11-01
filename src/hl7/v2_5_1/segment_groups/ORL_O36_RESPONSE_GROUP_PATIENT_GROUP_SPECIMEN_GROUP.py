from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SPM import SPM
from ..segments.OBX import OBX
from ..segment_groups.ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP,
)


"""
SPECIMEN - ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, SPM
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
)

orl_o36_response_group_patient_group_specimen_group = ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of SPM, OBX|None, SPECIMEN CONTAINER
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
    specimen_container=orl_o36_response_group_patient_group_specimen_group_specimen_container_group,  # ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of SPM, OBX|None, SPECIMEN CONTAINER"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("7", "8", "None")
    _c_components = (SPM, OBX, ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP)
    _c_name = ("SPM", "OBX", "SPECIMEN CONTAINER")
    _c_is_group = (False, False, True)
    _c_attrs = ("specimen", "observation_or_result", "specimen_container",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.7
        specimen_container: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP,
            ...,
        ],  #  Required. (SAC.9, ...)
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.8
    ):
        """
        None - `ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP>`_
        Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP - PATIENT consisting of SPM, OBX|None, SPECIMEN CONTAINER

        :param specimen: Specimen (id: SPM | seq: 7 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 8 | use: O | rpt: *)
        :param specimen_container: Specimen Container segment group: [SAC, ORDER|None] (id: SPECIMEN CONTAINER | seq: 9, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.specimen = specimen
        self.observation_or_result = observation_or_result
        self.specimen_container = specimen_container

    @property  # get SPM.7
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 7
        ---
        return_type: SPM.7: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.7
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 7
        ---
        param_type: SPM.7: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: OBX.8 | tuple[OBX, ...]: (Observation/Result, ...)
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
    ) -> tuple[
        ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP,
        ...,
    ]:
        """
        id: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        return self._c_data[2]

    @specimen_container.setter  # set SPECIMEN CONTAINER
    def specimen_container(
        self,
        specimen_container: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        | tuple[
            ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP,
            ...,
        ],
    ):
        """
        id: SPECIMEN CONTAINER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP.None | tuple[ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP
        """
        if isinstance(specimen_container, tuple):
            self._c_data[2] = specimen_container
        else:
            self._c_data[2] = (specimen_container,)
