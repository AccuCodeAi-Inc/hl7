from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.SPM import SPM


"""
SPECIMEN - RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    OBX, SPM
)

rsp_z90_query_response_group_specimen_group = RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of SPM, OBX|None
    specimen=spm,  # SPM(...)  # Required.
    observation_or_result=None,  # OBX(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of SPM, OBX|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("22", "23")
    _c_components = (SPM, OBX)
    _c_name = ("SPM", "OBX")
    _c_is_group = (False, False)
    _c_attrs = ("specimen", "observation_or_result",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.22
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.23
    ):
        """
        None - `RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RSP_Z90_QUERY_RESPONSE_GROUP_SPECIMEN_GROUP>`_
        Segment group for RSP_Z90_QUERY_RESPONSE_GROUP - QUERY RESPONSE consisting of SPM, OBX|None

        :param specimen: Specimen (id: SPM | seq: 22 | use: R | rpt: 1)
        :param observation_or_result: Observation/Result (id: OBX | seq: 23 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen = specimen
        self.observation_or_result = observation_or_result

    @property  # get SPM.22
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 22
        ---
        return_type: SPM.22: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.22
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 22
        ---
        param_type: SPM.22: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[1]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: OBX.23 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[1] = obx
        else:
            self._c_data[1] = (obx,)
