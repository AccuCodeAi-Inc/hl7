from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.AIL import AIL
from ..segments.APR import APR


"""
LOCATION RESOURCE - SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, AIL, APR
)

srm_s02_resources_group_location_resource_group = SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(  # LOCATION RESOURCE - Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIL, APR|None, NTE|None
    appointment_information_location_resource=ail,  # AIL(...)  # Required.
    appointment_preferences=None,  # APR(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP TEMPLATE-----
"""


class SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP"""
    _hl7_name = """LOCATION RESOURCE"""
    _hl7_description = """Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIL, APR|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("17", "18", "19")
    _c_components = (AIL, APR, NTE)
    _c_name = ("AIL", "APR", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("appointment_information_location_resource", "appointment_preferences", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information_location_resource: AIL,  #  Required. AIL.17
        appointment_preferences: APR | None = None,  #  APR.18
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
    ):
        """
        None - `SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP>`_
        Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIL, APR|None, NTE|None

        :param appointment_information_location_resource: Appointment Information - Location Resource (id: AIL | seq: 17 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 18 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.appointment_information_location_resource = (
            appointment_information_location_resource
        )
        self.appointment_preferences = appointment_preferences
        self.notes_and_comments = notes_and_comments

    @property  # get AIL.17
    def appointment_information_location_resource(self) -> AIL:
        """
        id: AIL | use: R | rpt: 1 | seq: 17
        ---
        return_type: AIL.17: Appointment Information - Location Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL
        """
        return self._c_data[0][0]

    @appointment_information_location_resource.setter  # set AIL.17
    def appointment_information_location_resource(self, ail: AIL):
        """
        id: AIL | use: R | rpt: 1 | seq: 17
        ---
        param_type: AIL.17: Appointment Information - Location Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL
        """
        self._c_data[0] = (ail,)

    @property  # get APR.18
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 18
        ---
        return_type: APR.18: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.18
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 18
        ---
        param_type: APR.18: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: NTE.19 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)
