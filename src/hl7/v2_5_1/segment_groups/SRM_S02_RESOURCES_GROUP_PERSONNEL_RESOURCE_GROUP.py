from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.AIP import AIP
from ..segments.APR import APR


"""
PERSONNEL RESOURCE - SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, APR, AIP
)

srm_s02_resources_group_personnel_resource_group = SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(  # PERSONNEL RESOURCE - Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIP, APR|None, NTE|None
    appointment_information_personnel_resource=aip,  # AIP(...)  # Required.
    appointment_preferences=None,  # APR(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP TEMPLATE-----
"""


class SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP"""
    _hl7_name = """PERSONNEL RESOURCE"""
    _hl7_description = """Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIP, APR|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("20", "21", "22")
    _c_components = (AIP, APR, NTE)
    _c_name = ("AIP", "APR", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("appointment_information_personnel_resource", "appointment_preferences", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information_personnel_resource: AIP,  #  Required. AIP.20
        appointment_preferences: APR | None = None,  #  APR.21
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.22
    ):
        """
        None - `SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP>`_
        Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIP, APR|None, NTE|None

        :param appointment_information_personnel_resource: Appointment Information - Personnel Resource (id: AIP | seq: 20 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 21 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 22 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.appointment_information_personnel_resource = (
            appointment_information_personnel_resource
        )
        self.appointment_preferences = appointment_preferences
        self.notes_and_comments = notes_and_comments

    @property  # get AIP.20
    def appointment_information_personnel_resource(self) -> AIP:
        """
        id: AIP | use: R | rpt: 1 | seq: 20
        ---
        return_type: AIP.20: Appointment Information - Personnel Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP
        """
        return self._c_data[0][0]

    @appointment_information_personnel_resource.setter  # set AIP.20
    def appointment_information_personnel_resource(self, aip: AIP):
        """
        id: AIP | use: R | rpt: 1 | seq: 20
        ---
        param_type: AIP.20: Appointment Information - Personnel Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP
        """
        self._c_data[0] = (aip,)

    @property  # get APR.21
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 21
        ---
        return_type: APR.21: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.21
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 21
        ---
        param_type: APR.21: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 22
        ---
        param_type: NTE.22 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)
