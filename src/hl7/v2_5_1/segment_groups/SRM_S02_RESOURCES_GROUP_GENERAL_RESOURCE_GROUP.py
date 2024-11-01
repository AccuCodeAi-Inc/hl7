from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.APR import APR
from ..segments.AIG import AIG
from ..segments.NTE import NTE


"""
GENERAL RESOURCE - SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, AIG, APR
)

srm_s02_resources_group_general_resource_group = SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(  # GENERAL RESOURCE - Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIG, APR|None, NTE|None
    appointment_information_general_resource=aig,  # AIG(...)  # Required.
    appointment_preferences=None,  # APR(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP TEMPLATE-----
"""


class SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP"""
    _hl7_name = """GENERAL RESOURCE"""
    _hl7_description = """Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIG, APR|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("14", "15", "16")
    _c_components = (AIG, APR, NTE)
    _c_name = ("AIG", "APR", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("appointment_information_general_resource", "appointment_preferences", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information_general_resource: AIG,  #  Required. AIG.14
        appointment_preferences: APR | None = None,  #  APR.15
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.16
    ):
        """
        None - `SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP>`_
        Segment group for SRM_S02_RESOURCES_GROUP - RESOURCES consisting of AIG, APR|None, NTE|None

        :param appointment_information_general_resource: Appointment Information - General Resource (id: AIG | seq: 14 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 15 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 16 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.appointment_information_general_resource = (
            appointment_information_general_resource
        )
        self.appointment_preferences = appointment_preferences
        self.notes_and_comments = notes_and_comments

    @property  # get AIG.14
    def appointment_information_general_resource(self) -> AIG:
        """
        id: AIG | use: R | rpt: 1 | seq: 14
        ---
        return_type: AIG.14: Appointment Information - General Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIG
        """
        return self._c_data[0][0]

    @appointment_information_general_resource.setter  # set AIG.14
    def appointment_information_general_resource(self, aig: AIG):
        """
        id: AIG | use: R | rpt: 1 | seq: 14
        ---
        param_type: AIG.14: Appointment Information - General Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIG
        """
        self._c_data[0] = (aig,)

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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: NTE.16 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)
