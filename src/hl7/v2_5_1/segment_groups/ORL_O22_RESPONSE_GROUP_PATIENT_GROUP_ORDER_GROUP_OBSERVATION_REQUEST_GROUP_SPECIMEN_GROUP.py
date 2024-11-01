from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.SAC import SAC
from ..segments.SPM import SPM


"""
SPECIMEN - ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
from utils.hl7.v2_5_1.segments import (
    SAC, SPM
)

orl_o22_response_group_patient_group_order_group_observation_request_group_specimen_group = ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP(  # SPECIMEN - Segment group for ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of SPM, SAC|None
    specimen=spm,  # SPM(...)  # Required.
    specimen_container_detail=None,  # SAC(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP TEMPLATE-----
"""


class ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP"""
    _hl7_name = """SPECIMEN"""
    _hl7_description = """Segment group for ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of SPM, SAC|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("11", "12")
    _c_components = (SPM, SAC)
    _c_name = ("SPM", "SAC")
    _c_is_group = (False, False)
    _c_attrs = ("specimen", "specimen_container_detail",)
    # fmt: on

    def __init__(
        self,
        specimen: SPM,  #  Required. SPM.11
        specimen_container_detail: SAC | tuple[SAC, ...] | None = None,  #  SAC.12
    ):
        """
        None - `ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP>`_
        Segment group for ORL_O22_RESPONSE_GROUP_PATIENT_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP - OBSERVATION REQUEST consisting of SPM, SAC|None

        :param specimen: Specimen (id: SPM | seq: 11 | use: R | rpt: 1)
        :param specimen_container_detail: Specimen Container detail (id: SAC | seq: 12 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.specimen = specimen
        self.specimen_container_detail = specimen_container_detail

    @property  # get SPM.11
    def specimen(self) -> SPM:
        """
        id: SPM | use: R | rpt: 1 | seq: 11
        ---
        return_type: SPM.11: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        return self._c_data[0][0]

    @specimen.setter  # set SPM.11
    def specimen(self, spm: SPM):
        """
        id: SPM | use: R | rpt: 1 | seq: 11
        ---
        param_type: SPM.11: Specimen
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SPM
        """
        self._c_data[0] = (spm,)

    @property  # get SAC
    def specimen_container_detail(self) -> tuple[SAC, ...] | tuple[None]:
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        return self._c_data[1]

    @specimen_container_detail.setter  # set SAC
    def specimen_container_detail(self, sac: SAC | tuple[SAC, ...] | None):
        """
        id: SAC SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: SAC.12 | tuple[SAC, ...]: (Specimen Container detail, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SAC
        """
        if isinstance(sac, tuple):
            self._c_data[1] = sac
        else:
            self._c_data[1] = (sac,)
