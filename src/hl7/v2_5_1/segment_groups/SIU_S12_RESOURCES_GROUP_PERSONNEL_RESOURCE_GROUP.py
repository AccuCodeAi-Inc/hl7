from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.AIP import AIP


"""
PERSONNEL RESOURCE - SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, AIP
)

siu_s12_resources_group_personnel_resource_group = SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(  # PERSONNEL RESOURCE - Segment group for SIU_S12_RESOURCES_GROUP - RESOURCES consisting of AIP, NTE|None
    appointment_information_personnel_resource=aip,  # AIP(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP TEMPLATE-----
"""


class SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP"""
    _hl7_name = """PERSONNEL RESOURCE"""
    _hl7_description = """Segment group for SIU_S12_RESOURCES_GROUP - RESOURCES consisting of AIP, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("18", "19")
    _c_components = (AIP, NTE)
    _c_name = ("AIP", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information_personnel_resource", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information_personnel_resource: AIP,  #  Required. AIP.18
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.19
    ):
        """
        None - `SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S12_RESOURCES_GROUP_PERSONNEL_RESOURCE_GROUP>`_
        Segment group for SIU_S12_RESOURCES_GROUP - RESOURCES consisting of AIP, NTE|None

        :param appointment_information_personnel_resource: Appointment Information - Personnel Resource (id: AIP | seq: 18 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 19 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information_personnel_resource = (
            appointment_information_personnel_resource
        )
        self.notes_and_comments = notes_and_comments

    @property  # get AIP.18
    def appointment_information_personnel_resource(self) -> AIP:
        """
        id: AIP | use: R | rpt: 1 | seq: 18
        ---
        return_type: AIP.18: Appointment Information - Personnel Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP
        """
        return self._c_data[0][0]

    @appointment_information_personnel_resource.setter  # set AIP.18
    def appointment_information_personnel_resource(self, aip: AIP):
        """
        id: AIP | use: R | rpt: 1 | seq: 18
        ---
        param_type: AIP.18: Appointment Information - Personnel Resource
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AIP
        """
        self._c_data[0] = (aip,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

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
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
