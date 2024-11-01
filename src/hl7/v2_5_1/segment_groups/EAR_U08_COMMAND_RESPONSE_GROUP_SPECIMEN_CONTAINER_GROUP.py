from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SAC import SAC
from ..segments.SPM import SPM


"""
SPECIMEN CONTAINER - EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, SPM
)

ear_u08_command_response_group_specimen_container_group = EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP(  # SPECIMEN CONTAINER - Segment group for EAR_U08_COMMAND_RESPONSE_GROUP - COMMAND RESPONSE consisting of SAC, SPM|None
    specimen_container_detail=sac,  # SAC(...)  # Required.
    specimen=None,  # SPM(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP TEMPLATE-----
"""


class EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP"""
    _hl7_name = """SPECIMEN CONTAINER"""
    _hl7_description = """Segment group for EAR_U08_COMMAND_RESPONSE_GROUP - COMMAND RESPONSE consisting of SAC, SPM|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("5", "6")
    _c_components = (SAC, SPM)
    _c_name = ("SAC", "SPM")
    _c_is_group = (False, False)
    _c_attrs = ("specimen_container_detail", "specimen",)
    # fmt: on

    def __init__(
        self,
        specimen_container_detail: SAC,  #  Required. SAC.5
        specimen: SPM | tuple[SPM, ...] | None = None,  #  SPM.6
    ):
        """
        None - `EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/EAR_U08_COMMAND_RESPONSE_GROUP_SPECIMEN_CONTAINER_GROUP>`_
        Segment group for EAR_U08_COMMAND_RESPONSE_GROUP - COMMAND RESPONSE consisting of SAC, SPM|None

        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 5 | use: R | rpt: 1)
        :param specimen: Specimen (id: SPM | seq: 6 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen_container_detail = specimen_container_detail
        self.specimen = specimen

    @property  # get SAC.5
    def specimen_container_detail(self) -> SAC:
        """
        id: SAC | use: R | rpt: 1 | seq: 5
        ---
        return_type: SAC.5: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[0][0]

    @specimen_container_detail.setter  # set SAC.5
    def specimen_container_detail(self, sac: SAC):
        """
        id: SAC | use: R | rpt: 1 | seq: 5
        ---
        param_type: SAC.5: Specimen Container detail
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        self._c_data[0] = (sac,)

    @property  # get SPM
    def specimen(self) -> tuple[SPM, ...] | tuple[None]:
        """
        id: SPM SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[SPM, ...]: (Specimen, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[1]

    @specimen.setter  # set SPM
    def specimen(self, spm: SPM | tuple[SPM, ...] | None):
        """
        id: SPM SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: SPM.6 | tuple[SPM, ...]: (Specimen, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        if isinstance(spm, tuple):
            self._c_data[1] = spm
        else:
            self._c_data[1] = (spm,)
