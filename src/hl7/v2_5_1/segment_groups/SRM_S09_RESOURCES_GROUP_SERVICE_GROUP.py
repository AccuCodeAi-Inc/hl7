from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.AIS import AIS
from ..segments.APR import APR


"""
SERVICE - SRM_S09_RESOURCES_GROUP_SERVICE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRM_S09_RESOURCES_GROUP_SERVICE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRM_S09_RESOURCES_GROUP_SERVICE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, APR, AIS
)

srm_s09_resources_group_service_group = SRM_S09_RESOURCES_GROUP_SERVICE_GROUP(  # SERVICE - Segment group for SRM_S09_RESOURCES_GROUP - RESOURCES consisting of AIS, APR|None, NTE|None
    appointment_information=ais,  # AIS(...)  # Required.
    appointment_preferences=None,  # APR(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRM_S09_RESOURCES_GROUP_SERVICE_GROUP TEMPLATE-----
"""


class SRM_S09_RESOURCES_GROUP_SERVICE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRM_S09_RESOURCES_GROUP_SERVICE_GROUP"""
    _hl7_name = """SERVICE"""
    _hl7_description = """Segment group for SRM_S09_RESOURCES_GROUP - RESOURCES consisting of AIS, APR|None, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S09_RESOURCES_GROUP_SERVICE_GROUP"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 1, 65535)
    _c_usage = ("R", "O", "O")
    _c_aliases = ("11", "12", "13")
    _c_components = (AIS, APR, NTE)
    _c_name = ("AIS", "APR", "NTE")
    _c_is_group = (False, False, False)
    _c_attrs = ("appointment_information", "appointment_preferences", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information: AIS,  #  Required. AIS.11
        appointment_preferences: APR | None = None,  #  APR.12
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
    ):
        """
        None - `SRM_S09_RESOURCES_GROUP_SERVICE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S09_RESOURCES_GROUP_SERVICE_GROUP>`_
        Segment group for SRM_S09_RESOURCES_GROUP - RESOURCES consisting of AIS, APR|None, NTE|None

        :param appointment_information: Appointment Information (id: AIS | seq: 11 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 12 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.appointment_information = appointment_information
        self.appointment_preferences = appointment_preferences
        self.notes_and_comments = notes_and_comments

    @property  # get AIS.11
    def appointment_information(self) -> AIS:
        """
        id: AIS | use: R | rpt: 1 | seq: 11
        ---
        return_type: AIS.11: Appointment Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS
        """
        return self._c_data[0][0]

    @appointment_information.setter  # set AIS.11
    def appointment_information(self, a_is: AIS):
        """
        id: AIS | use: R | rpt: 1 | seq: 11
        ---
        param_type: AIS.11: Appointment Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS
        """
        self._c_data[0] = (a_is,)

    @property  # get APR.12
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 12
        ---
        return_type: APR.12: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[1][0]

    @appointment_preferences.setter  # set APR.12
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 12
        ---
        param_type: APR.12: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[1] = (apr,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: NTE.13 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)
