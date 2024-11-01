from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.NTE import NTE
from ..segments.AIG import AIG


"""
GENERAL RESOURCE - SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP
from utils.hl7.v2_5_1.segments import (
    NTE, AIG
)

srr_s04_schedule_group_resources_group_general_resource_group = SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(  # GENERAL RESOURCE - Segment group for SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIG, NTE|None
    appointment_information_general_resource=aig,  # AIG(...)  # Required.
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP TEMPLATE-----
"""


class SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP"""
    _hl7_name = """GENERAL RESOURCE"""
    _hl7_description = """Segment group for SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIG, NTE|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP"""
    _c_length = (-1,-1,)
    _c_rpt = (1, 65535)
    _c_usage = ("R", "O")
    _c_aliases = ("14", "15")
    _c_components = (AIG, NTE)
    _c_name = ("AIG", "NTE")
    _c_is_group = (False, False)
    _c_attrs = ("appointment_information_general_resource", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        appointment_information_general_resource: AIG,  #  Required. AIG.14
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.15
    ):
        """
        None - `SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP_GENERAL_RESOURCE_GROUP>`_
        Segment group for SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP - RESOURCES consisting of AIG, NTE|None

        :param appointment_information_general_resource: Appointment Information - General Resource (id: AIG | seq: 14 | use: R | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 15 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 2
        self.appointment_information_general_resource = (
            appointment_information_general_resource
        )
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

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[1]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: NTE.15 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[1] = nte
        else:
            self._c_data[1] = (nte,)
