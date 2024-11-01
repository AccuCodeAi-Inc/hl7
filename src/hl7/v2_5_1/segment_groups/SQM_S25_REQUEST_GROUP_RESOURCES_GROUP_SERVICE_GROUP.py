from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AIS import AIS
from ..segments.APR import APR


"""
SERVICE - SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP
from utils.hl7.v2_5_1.segments import (
    APR, AIS
)

sqm_s25_request_group_resources_group_service_group = SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP(  # SERVICE - Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIS, APR|None
    appointment_information=ais,  # AIS(...)  # Required.
    appointment_preferences=None,  # APR(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP TEMPLATE-----
"""


class SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP"""
    _hl7_name = """SERVICE"""
    _hl7_description = """Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIS, APR|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 1)
    _c_usage = ("R", "O")
    _c_aliases = ("8", "9")
    _c_components = (AIS, APR)
    _c_name = ("AIS", "APR")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information", "appointment_preferences",)
    # fmt: on

    def __init__(
        self,
        appointment_information: AIS,  #  Required. AIS.8
        appointment_preferences: APR | None = None,  #  APR.9
    ):
        """
        None - `SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP_SERVICE_GROUP>`_
        Segment group for SQM_S25_REQUEST_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIS, APR|None

        :param appointment_information: Appointment Information (id: AIS | seq: 8 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 9 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information = appointment_information
        self.appointment_preferences = appointment_preferences

    @property  # get AIS.8
    def appointment_information(self) -> AIS:
        """
        id: AIS | use: R | rpt: 1 | seq: 8
        ---
        return_type: AIS.8: Appointment Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS
        """
        return self._c_data[0][0]

    @appointment_information.setter  # set AIS.8
    def appointment_information(self, a_is: AIS):
        """
        id: AIS | use: R | rpt: 1 | seq: 8
        ---
        param_type: AIS.8: Appointment Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS
        """
        self._c_data[0] = (a_is,)

    @property  # get APR.9
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 9
        ---
        return_type: APR.9: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.9
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 9
        ---
        param_type: APR.9: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)
