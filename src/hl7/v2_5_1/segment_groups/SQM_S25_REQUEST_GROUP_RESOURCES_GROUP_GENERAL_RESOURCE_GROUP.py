from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.APR import APR
from ..segments.AIG import AIG


"""
GENERAL RESOURCE - SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    AIG, APR
)

sqm_s25_request_group_resources_group_general_resource_group = SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(  # GENERAL RESOURCE - Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIG, APR|None
    appointment_information_general_resource=aig,  # AIG(...)  # Required.
    appointment_preferences=None,  # APR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP TEMPLATE-----
"""


class SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP"""
    _hl7_name = """GENERAL RESOURCE"""
    _hl7_description = """Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIG, APR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("10", "11")
    _c_components = (AIG, APR)
    _c_name = ("AIG", "APR")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information_general_resource", "appointment_preferences",)
    # fmt: on

    def __init__(
        self,
        appointment_information_general_resource: AIG,  #  Required. AIG.10
        appointment_preferences: APR | None = None,  #  APR.11
    ):
        """
        None - `SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP>`_
        Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIG, APR|None

        :param appointment_information_general_resource: Appointment Information - General Resource (id: AIG | seq: 10 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 11 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information_general_resource = (
            appointment_information_general_resource
        )
        self.appointment_preferences = appointment_preferences

    @property  # get AIG.10
    def appointment_information_general_resource(self) -> AIG:
        """
        id: AIG | use: R | rpt: 1 | seq: 10
        ---
        return_type: AIG.10: Appointment Information - General Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIG
        """
        return self._c_data[0][0]

    @appointment_information_general_resource.setter  # set AIG.10
    def appointment_information_general_resource(self, aig: AIG):
        """
        id: AIG | use: R | rpt: 1 | seq: 10
        ---
        param_type: AIG.10: Appointment Information - General Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIG
        """
        self._c_data[0] = (aig,)

    @property  # get APR.11
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 11
        ---
        return_type: APR.11: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.11
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 11
        ---
        param_type: APR.11: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)
