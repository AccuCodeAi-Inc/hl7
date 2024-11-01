from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AIL import AIL
from ..segments.APR import APR


"""
LOCATION RESOURCE - SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    AIL, APR
)

sqm_s25_request_group_resources_group_location_resource_group = SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(  # LOCATION RESOURCE - Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIL, APR|None
    appointment_information_location_resource=ail,  # AIL(...)  # Required.
    appointment_preferences=None,  # APR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP TEMPLATE-----
"""


class SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP"""
    _hl7_name = """LOCATION RESOURCE"""
    _hl7_description = """Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIL, APR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (AIL, APR)
    _c_name = ("AIL", "APR")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information_location_resource", "appointment_preferences",)
    # fmt: on

    def __init__(
        self,
        appointment_information_location_resource: AIL,  #  Required. AIL.14
        appointment_preferences: APR | None = None,  #  APR.15
    ):
        """
        None - `SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP>`_
        Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIL, APR|None

        :param appointment_information_location_resource: Appointment Information - Location Resource (id: AIL | seq: 14 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 15 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information_location_resource = (
            appointment_information_location_resource
        )
        self.appointment_preferences = appointment_preferences

    @property  # get AIL.14
    def appointment_information_location_resource(self) -> AIL:
        """
        id: AIL | use: R | rpt: 1 | seq: 14
        ---
        return_type: AIL.14: Appointment Information - Location Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL
        """
        return self._c_data[0][0]

    @appointment_information_location_resource.setter  # set AIL.14
    def appointment_information_location_resource(self, ail: AIL):
        """
        id: AIL | use: R | rpt: 1 | seq: 14
        ---
        param_type: AIL.14: Appointment Information - Location Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL
        """
        self._c_data[0] = (ail,)

    @property  # get APR.15
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 15
        ---
        return_type: APR.15: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.15
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 15
        ---
        param_type: APR.15: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)
