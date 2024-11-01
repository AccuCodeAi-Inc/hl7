from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.SQM_S25_REQUEST_GROUP_RESOURCES_GROUP import (
    SQM_S25_REQUEST_GROUP_RESOURCES_GROUP,
)
from ..segments.PID import PID
from ..segments.ARQ import ARQ
from ..segments.APR import APR


"""
REQUEST - SQM_S25_REQUEST_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQM_S25_REQUEST_GROUP
from utils.hl7.v2_5_1.segments import (
    ARQ, APR, PID
)
from utils.hl7.v2_5_1.segment_groups import (
    SQM_S25_REQUEST_GROUP_RESOURCES_GROUP
)

sqm_s25_request_group = SQM_S25_REQUEST_GROUP(  # REQUEST - Segment group for SQM_S25 - Schedule query message and response consisting of ARQ, APR|None, PID|None, RESOURCES
    appointment_request=arq,  # ARQ(...)  # Required.
    appointment_preferences=None,  # APR(...) 
    patient_identification=None,  # PID(...) 
    resources=sqm_s25_request_group_resources_group,  # SQM_S25_REQUEST_GROUP_RESOURCES_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQM_S25_REQUEST_GROUP TEMPLATE-----
"""


class SQM_S25_REQUEST_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQM_S25_REQUEST_GROUP"""
    _hl7_name = """REQUEST"""
    _hl7_description = """Segment group for SQM_S25 - Schedule query message and response consisting of ARQ, APR|None, PID|None, RESOURCES"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP"""
    _c_length = (-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 65535)
    _c_usage = ("R", "O", "O", "R")
    _c_aliases = ("4", "5", "6", "None")
    _c_components = (ARQ, APR, PID, SQM_S25_REQUEST_GROUP_RESOURCES_GROUP)
    _c_name = ("ARQ", "APR", "PID", "RESOURCES")
    _c_is_group = (False, False, False, True)
    _c_attrs = ("appointment_request", "appointment_preferences", "patient_identification", "resources",)
    # fmt: on

    def __init__(
        self,
        appointment_request: ARQ,  #  Required. ARQ.4
        resources: SQM_S25_REQUEST_GROUP_RESOURCES_GROUP
        | tuple[SQM_S25_REQUEST_GROUP_RESOURCES_GROUP, ...],  #  Required. (RGS.7, ...)
        appointment_preferences: APR | None = None,  #  APR.5
        patient_identification: PID | None = None,  #  PID.6
    ):
        """
        None - `SQM_S25_REQUEST_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQM_S25_REQUEST_GROUP>`_
        Segment group for SQM_S25 - Schedule query message and response consisting of ARQ, APR|None, PID|None, RESOURCES

        :param appointment_request: Appointment Request (id: ARQ | seq: 4 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 5 | use: O | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: O | rpt: 1)
        :param resources: Resources segment group: [RGS, SERVICE|None, GENERAL RESOURCE|None, PERSONNEL RESOURCE|None, LOCATION RESOURCE|None] (id: RESOURCES | seq: 7, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 4
        self.appointment_request = appointment_request
        self.appointment_preferences = appointment_preferences
        self.patient_identification = patient_identification
        self.resources = resources

    @property  # get ARQ.4
    def appointment_request(self) -> ARQ:
        """
        id: ARQ | use: R | rpt: 1 | seq: 4
        ---
        return_type: ARQ.4: Appointment Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ARQ
        """
        return self._c_data[0][0]

    @appointment_request.setter  # set ARQ.4
    def appointment_request(self, arq: ARQ):
        """
        id: ARQ | use: R | rpt: 1 | seq: 4
        ---
        param_type: ARQ.4: Appointment Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ARQ
        """
        self._c_data[0] = (arq,)

    @property  # get APR.5
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 5
        ---
        return_type: APR.5: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.5
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 5
        ---
        param_type: APR.5: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)

    @property  # get PID.6
    def patient_identification(self) -> PID | None:
        """
        id: PID | use: O | rpt: 1 | seq: 6
        ---
        return_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[2][0]

    @patient_identification.setter  # set PID.6
    def patient_identification(self, pid: PID | None):
        """
        id: PID | use: O | rpt: 1 | seq: 6
        ---
        param_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[2] = (pid,)

    @property  # get RESOURCES
    def resources(self) -> tuple[SQM_S25_REQUEST_GROUP_RESOURCES_GROUP, ...]:
        """
        id: SQM_S25_REQUEST_GROUP_RESOURCES_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SQM_S25_REQUEST_GROUP_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP
        """
        return self._c_data[3]

    @resources.setter  # set RESOURCES
    def resources(
        self,
        resources: SQM_S25_REQUEST_GROUP_RESOURCES_GROUP
        | tuple[SQM_S25_REQUEST_GROUP_RESOURCES_GROUP, ...],
    ):
        """
        id: RESOURCES SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SQM_S25_REQUEST_GROUP_RESOURCES_GROUP.None | tuple[SQM_S25_REQUEST_GROUP_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQM_S25_REQUEST_GROUP_RESOURCES_GROUP
        """
        if isinstance(resources, tuple):
            self._c_data[3] = resources
        else:
            self._c_data[3] = (resources,)
