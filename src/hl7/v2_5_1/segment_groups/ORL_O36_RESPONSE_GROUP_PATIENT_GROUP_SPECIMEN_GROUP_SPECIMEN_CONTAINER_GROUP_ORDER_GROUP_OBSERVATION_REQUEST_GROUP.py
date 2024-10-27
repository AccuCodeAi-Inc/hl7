from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBR import OBR


"""
OBSERVATION REQUEST - ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR
)

orl_o36_response_group_patient_group_specimen_group_specimen_container_group_order_group_observation_request_group = ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(  # OBSERVATION REQUEST - Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP - ORDER consisting of OBR
    observation_request=obr,  # OBR(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP TEMPLATE-----
"""


class ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP"""
    _hl7_name = """OBSERVATION REQUEST"""
    _hl7_description = """Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP - ORDER consisting of OBR"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP"""
    _c_length = (-1,)
    _c_rpt = (1)
    _c_usage = ("R")
    _c_aliases = ("13")
    _c_components = (OBR)
    _c_name = ("OBR")
    _c_is_group = (False)
    _c_attrs = ("observation_request",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.13
    ):
        """
        None - `ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP>`_
        Segment group for ORL_O36_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_SPECIMEN_CONTAINER_GROUP_ORDER_GROUP - ORDER consisting of OBR

        :param observation_request: Observation Request (id: OBR | seq: 13 | use: R | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 1
        self.observation_request = observation_request

    @property  # get OBR.13
    def observation_request(self) -> OBR:
        """
        id: OBR | use: R | rpt: 1 | seq: 13
        ---
        return_type: OBR.13: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        return self._c_data[0][0]

    @observation_request.setter  # set OBR.13
    def observation_request(self, obr: OBR):
        """
        id: OBR | use: R | rpt: 1 | seq: 13
        ---
        param_type: OBR.13: Observation Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBR
        """
        self._c_data[0] = (obr,)
