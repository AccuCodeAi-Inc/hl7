from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.AIS import AIS


"""
SERVICE - SIU_S12_RESOURCES_GROUP_SERVICE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SIU_S12_RESOURCES_GROUP_SERVICE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SIU_S12_RESOURCES_GROUP_SERVICE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, AIS
)

siu_s12_resources_group_service_group = SIU_S12_RESOURCES_GROUP_SERVICE_GROUP(  # SERVICE - Segment group for SIU_S12_RESOURCES_GROUP - RESOURCES consisting of AIS, NTE|None
    appointment_information=ais,  # AIS(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SIU_S12_RESOURCES_GROUP_SERVICE_GROUP TEMPLATE-----
"""


class SIU_S12_RESOURCES_GROUP_SERVICE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SIU_S12_RESOURCES_GROUP_SERVICE_GROUP"""
    _hl7_name = """SERVICE"""
    _hl7_description = """Segment group for SIU_S12_RESOURCES_GROUP - RESOURCES consisting of AIS, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S12_RESOURCES_GROUP_SERVICE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("12", "13")
    _c_components = (AIS, NTE)
    _c_name = ("AIS", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information: AIS,  #  Required. AIS.12
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.13
    ):
        """
        None - `SIU_S12_RESOURCES_GROUP_SERVICE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S12_RESOURCES_GROUP_SERVICE_GROUP>`_
        Segment group for SIU_S12_RESOURCES_GROUP - RESOURCES consisting of AIS, NTE|None

        :param appointment_information: Appointment Information (id: AIS | seq: 12 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 13 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information = appointment_information
        self.notes_and_comments = notes_and_comments

    @property  # get AIS.12
    def appointment_information(self) -> AIS:
        """
        id: AIS | use: R | rpt: 1 | seq: 12
        ---
        return_type: AIS.12: Appointment Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS
        """
        return self._c_data[0][0]

    @appointment_information.setter  # set AIS.12
    def appointment_information(self, a_is: AIS):
        """
        id: AIS | use: R | rpt: 1 | seq: 12
        ---
        param_type: AIS.12: Appointment Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIS
        """
        self._c_data[0] = (a_is,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

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
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
