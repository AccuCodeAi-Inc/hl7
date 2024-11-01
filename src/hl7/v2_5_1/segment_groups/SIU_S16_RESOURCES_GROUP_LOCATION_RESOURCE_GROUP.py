from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.AIL import AIL
from ..segments.NTE import NTE


"""
LOCATION RESOURCE - SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    AIL, NTE
)

siu_s16_resources_group_location_resource_group = SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(  # LOCATION RESOURCE - Segment group for SIU_S16_RESOURCES_GROUP - RESOURCES consisting of AIL, NTE|None
    appointment_information_location_resource=ail,  # AIL(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP TEMPLATE-----
"""


class SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP"""
    _hl7_name = """LOCATION RESOURCE"""
    _hl7_description = """Segment group for SIU_S16_RESOURCES_GROUP - RESOURCES consisting of AIL, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("16", "17")
    _c_components = (AIL, NTE)
    _c_name = ("AIL", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information_location_resource", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information_location_resource: AIL,  #  Required. AIL.16
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.17
    ):
        """
        None - `SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S16_RESOURCES_GROUP_LOCATION_RESOURCE_GROUP>`_
        Segment group for SIU_S16_RESOURCES_GROUP - RESOURCES consisting of AIL, NTE|None

        :param appointment_information_location_resource: Appointment Information - Location Resource (id: AIL | seq: 16 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 17 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information_location_resource = (
            appointment_information_location_resource
        )
        self.notes_and_comments = notes_and_comments

    @property  # get AIL.16
    def appointment_information_location_resource(self) -> AIL:
        """
        id: AIL | use: R | rpt: 1 | seq: 16
        ---
        return_type: AIL.16: Appointment Information - Location Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL
        """
        return self._c_data[0][0]

    @appointment_information_location_resource.setter  # set AIL.16
    def appointment_information_location_resource(self, ail: AIL):
        """
        id: AIL | use: R | rpt: 1 | seq: 16
        ---
        param_type: AIL.16: Appointment Information - Location Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIL
        """
        self._c_data[0] = (ail,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: NTE.17 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
