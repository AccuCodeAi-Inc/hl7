from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AIP import AIP
from ..segments.APR import APR


"""
PERSONNEL RESOURCE - SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    AIP, APR
)

sqm_s25_request_group_resources_group_personnel_resource_group = SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(  # PERSONNEL RESOURCE - Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIP, APR|None
    appointment_information_personnel_resource=aip,  # AIP(...)  # Required.
    appointment_preferences=None,  # APR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP TEMPLATE-----
"""


class SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP"""
    _hl7_name = """PERSONNEL RESOURCE"""
    _hl7_description = """Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIP, APR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("12", "13")
    _c_components = (AIP, APR)
    _c_name = ("AIP", "APR")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information_personnel_resource", "appointment_preferences",)
    # fmt: on

    def __init__(
        self,
        appointment_information_personnel_resource: AIP,  #  Required. AIP.12
        appointment_preferences: APR | None = None,  #  APR.13
    ):
        """
        None - `SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP>`_
        Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIP, APR|None

        :param appointment_information_personnel_resource: Appointment Information - Personnel Resource (id: AIP | seq: 12 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 13 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information_personnel_resource = (
            appointment_information_personnel_resource
        )
        self.appointment_preferences = appointment_preferences

    @property  # get AIP.12
    def appointment_information_personnel_resource(self) -> AIP:
        """
        id: AIP | use: R | rpt: 1 | seq: 12
        ---
        return_type: AIP.12: Appointment Information - Personnel Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP
        """
        return self._c_data[0][0]

    @appointment_information_personnel_resource.setter  # set AIP.12
    def appointment_information_personnel_resource(self, aip: AIP):
        """
        id: AIP | use: R | rpt: 1 | seq: 12
        ---
        param_type: AIP.12: Appointment Information - Personnel Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP
        """
        self._c_data[0] = (aip,)

    @property  # get APR.13
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 13
        ---
        return_type: APR.13: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.13
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 13
        ---
        param_type: APR.13: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)
