from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP import (
    ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP,
)
from ..segments.OBR import OBR


"""
OBSERVATION REQUEST - ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP
from utils.hl7.v2_5_1.segments import (
    OBR
)
from utils.hl7.v2_5_1.segment_groups import (
    ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
)

orl_o34_response_group_patient_group_specimen_group_order_group_observation_request_group = ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(  # OBSERVATION REQUEST - Segment group for ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP - ORDER consisting of OBR, SPECIMEN|None
    observation_request=obr,  # OBR(...)  # Required.
    specimen=None,  # ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP TEMPLATE-----
"""


class ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP(
    HL7SegmentGroup
):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP"""
    _hl7_name = """OBSERVATION REQUEST"""
    _hl7_description = """Segment group for ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP - ORDER consisting of OBR, SPECIMEN|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("13", "None")
    _c_components = (OBR, ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP)
    _c_name = ("OBR", "SPECIMEN")
    _c_is_group = (False, True)
    _c_attrs = ("observation_request", "specimen",)
    # fmt: on

    def __init__(
        self,
        observation_request: OBR,  #  Required. OBR.13
        specimen: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
        | tuple[
            ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP,
            ...,
        ]
        | None = None,  #  (SPM.14, SAC.15, ...)
    ):
        """
        None - `ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP>`_
        Segment group for ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP - ORDER consisting of OBR, SPECIMEN|None

        :param observation_request: Observation Request (id: OBR | seq: 13 | use: R | rpt: 1)
        :param specimen: Specimen segment group: [SPM, SAC|None] (id: SPECIMEN | seq: 14, 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.observation_request = observation_request
        self.specimen = specimen

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

    @property  # get SPECIMEN
    def specimen(
        self,
    ) -> (
        tuple[
            ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP,
            ...,
        ]
        | tuple[None]
    ):
        """
        id: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
        """
        return self._c_data[1]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self,
        specimen: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
        | tuple[
            ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP,
            ...,
        ]
        | None,
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP.None | tuple[ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ORL_O34_RESPONSE_GROUP_PATIENT_GROUP_SPECIMEN_GROUP_ORDER_GROUP_OBSERVATION_REQUEST_GROUP_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[1] = specimen
        else:
            self._c_data[1] = (specimen,)
