from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP import (
    SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP,
)
from ..segments.SCH import SCH
from ..segments.TQ1 import TQ1
from ..segments.NTE import NTE
from ..segment_groups.SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP import (
    SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP,
)


"""
SCHEDULE - SRR_S04_SCHEDULE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SRR_S04_SCHEDULE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRR_S04_SCHEDULE_GROUP
from utils.hl7.v2_5_1.segments import (
    TQ1, NTE, SCH
)
from utils.hl7.v2_5_1.segment_groups import (
    SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP
)

srr_s04_schedule_group = SRR_S04_SCHEDULE_GROUP(  # SCHEDULE - Segment group for SRR_S04 - Scheduled request response - Appointment cancellation consisting of SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES
    scheduling_activity_information=sch,  # SCH(...)  # Required.
    timing_or_quantity=None,  # TQ1(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP(...) 
    resources=srr_s04_schedule_group_resources_group,  # SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SRR_S04_SCHEDULE_GROUP TEMPLATE-----
"""


class SRR_S04_SCHEDULE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SRR_S04_SCHEDULE_GROUP"""
    _hl7_name = """SCHEDULE"""
    _hl7_description = """Segment group for SRR_S04 - Scheduled request response - Appointment cancellation consisting of SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRR_S04_SCHEDULE_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("4", "5", "6", "None", "None")
    _c_components = (SCH, TQ1, NTE, SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP)
    _c_name = ("SCH", "TQ1", "NTE", "PATIENT", "RESOURCES")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("scheduling_activity_information", "timing_or_quantity", "notes_and_comments", "patient", "resources",)
    # fmt: on

    def __init__(
        self,
        scheduling_activity_information: SCH,  #  Required. SCH.4
        resources: SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP
        | tuple[
            SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP, ...
        ],  #  Required. (RGS.11, ...)
        timing_or_quantity: TQ1 | tuple[TQ1, ...] | None = None,  #  TQ1.5
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.6
        patient: SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP
        | tuple[SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, ...]
        | None = None,  #  (PID.7, PV1.8, PV2.9, DG1.10, ...)
    ):
        """
        None - `SRR_S04_SCHEDULE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRR_S04_SCHEDULE_GROUP>`_
        Segment group for SRR_S04 - Scheduled request response - Appointment cancellation consisting of SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES

        :param scheduling_activity_information: Scheduling Activity Information (id: SCH | seq: 4 | use: R | rpt: 1)
        :param timing_or_quantity: Timing/Quantity (id: TQ1 | seq: 5 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 6 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PV1|None, PV2|None, DG1|None] (id: PATIENT | seq: 7, 8, 9, 10 | use: O | rpt: *)
        :param resources: Resources segment group: [RGS, SERVICE|None, GENERAL RESOURCE|None, LOCATION RESOURCE|None, PERSONNEL RESOURCE|None] (id: RESOURCES | seq: 11, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.scheduling_activity_information = scheduling_activity_information
        self.timing_or_quantity = timing_or_quantity
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.resources = resources

    @property  # get SCH.4
    def scheduling_activity_information(self) -> SCH:
        """
        id: SCH | use: R | rpt: 1 | seq: 4
        ---
        return_type: SCH.4: Scheduling Activity Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH
        """
        return self._c_data[0][0]

    @scheduling_activity_information.setter  # set SCH.4
    def scheduling_activity_information(self, sch: SCH):
        """
        id: SCH | use: R | rpt: 1 | seq: 4
        ---
        param_type: SCH.4: Scheduling Activity Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH
        """
        self._c_data[0] = (sch,)

    @property  # get TQ1
    def timing_or_quantity(self) -> tuple[TQ1, ...] | tuple[None]:
        """
        id: TQ1 SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[TQ1, ...]: (Timing/Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        return self._c_data[1]

    @timing_or_quantity.setter  # set TQ1
    def timing_or_quantity(self, tq1: TQ1 | tuple[TQ1, ...] | None):
        """
        id: TQ1 SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: TQ1.5 | tuple[TQ1, ...]: (Timing/Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        if isinstance(tq1, tuple):
            self._c_data[1] = tq1
        else:
            self._c_data[1] = (tq1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: NTE.6 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get PATIENT
    def patient(self) -> tuple[SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, ...] | tuple[None]:
        """
        id: SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP
        """
        return self._c_data[3]

    @patient.setter  # set PATIENT
    def patient(
        self,
        patient: SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP
        | tuple[SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, ...]
        | None,
    ):
        """
        id: PATIENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP.None | tuple[SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRR_S04_SCHEDULE_GROUP_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[3] = patient
        else:
            self._c_data[3] = (patient,)

    @property  # get RESOURCES
    def resources(self) -> tuple[SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP, ...]:
        """
        id: SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP
        """
        return self._c_data[4]

    @resources.setter  # set RESOURCES
    def resources(
        self,
        resources: SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP
        | tuple[SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP, ...],
    ):
        """
        id: RESOURCES SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP.None | tuple[SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRR_S04_SCHEDULE_GROUP_RESOURCES_GROUP
        """
        if isinstance(resources, tuple):
            self._c_data[4] = resources
        else:
            self._c_data[4] = (resources,)
