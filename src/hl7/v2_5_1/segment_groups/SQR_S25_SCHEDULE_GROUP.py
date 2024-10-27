from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP,
)
from ..segments.SCH import SCH
from ..segment_groups.SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP import (
    SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP,
)
from ..segments.NTE import NTE
from ..segments.TQ1 import TQ1


"""
SCHEDULE - SQR_S25_SCHEDULE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::SQR_S25_SCHEDULE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SQR_S25_SCHEDULE_GROUP
from utils.hl7.v2_5_1.segments import (
    SCH, TQ1, NTE
)
from utils.hl7.v2_5_1.segment_groups import (
    SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP, SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP
)

sqr_s25_schedule_group = SQR_S25_SCHEDULE_GROUP(  # SCHEDULE - Segment group for SQR_S25 - Schedule query message and response consisting of SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES
    scheduling_activity_information=sch,  # SCH(...)  # Required.
    timing_or_quantity=None,  # TQ1(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP(...) 
    resources=sqr_s25_schedule_group_resources_group,  # SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::SQR_S25_SCHEDULE_GROUP TEMPLATE-----
"""


class SQR_S25_SCHEDULE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """SQR_S25_SCHEDULE_GROUP"""
    _hl7_name = """SCHEDULE"""
    _hl7_description = """Segment group for SQR_S25 - Schedule query message and response consisting of SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25_SCHEDULE_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R")
    _c_aliases = ("5", "6", "7", "None", "None")
    _c_components = (SCH, TQ1, NTE, SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP, SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP)
    _c_name = ("SCH", "TQ1", "NTE", "PATIENT", "RESOURCES")
    _c_is_group = (False, False, False, True, True)
    _c_attrs = ("scheduling_activity_information", "timing_or_quantity", "notes_and_comments", "patient", "resources",)
    # fmt: on

    def __init__(
        self,
        scheduling_activity_information: SCH,  #  Required. SCH.5
        resources: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP
        | tuple[
            SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP, ...
        ],  #  Required. (RGS.12, ...)
        timing_or_quantity: TQ1 | tuple[TQ1, ...] | None = None,  #  TQ1.6
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.7
        patient: SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP
        | None = None,  #  PID.8, PV1.9, PV2.10, DG1.11
    ):
        """
        None - `SQR_S25_SCHEDULE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SQR_S25_SCHEDULE_GROUP>`_
        Segment group for SQR_S25 - Schedule query message and response consisting of SCH, TQ1|None, NTE|None, PATIENT|None, RESOURCES

        :param scheduling_activity_information: Scheduling Activity Information (id: SCH | seq: 5 | use: R | rpt: 1)
        :param timing_or_quantity: Timing/Quantity (id: TQ1 | seq: 6 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 7 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PV1|None, PV2|None, DG1|None] (id: PATIENT | seq: 8, 9, 10, 11 | use: O | rpt: 1)
        :param resources: Resources segment group: [RGS, SERVICE|None, GENERAL RESOURCE|None, PERSONNEL RESOURCE|None, LOCATION RESOURCE|None] (id: RESOURCES | seq: 12, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 5
        self.scheduling_activity_information = scheduling_activity_information
        self.timing_or_quantity = timing_or_quantity
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.resources = resources

    @property  # get SCH.5
    def scheduling_activity_information(self) -> SCH:
        """
        id: SCH | use: R | rpt: 1 | seq: 5
        ---
        return_type: SCH.5: Scheduling Activity Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH
        """
        return self._c_data[0][0]

    @scheduling_activity_information.setter  # set SCH.5
    def scheduling_activity_information(self, sch: SCH):
        """
        id: SCH | use: R | rpt: 1 | seq: 5
        ---
        param_type: SCH.5: Scheduling Activity Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH
        """
        self._c_data[0] = (sch,)

    @property  # get TQ1
    def timing_or_quantity(self) -> tuple[TQ1, ...] | tuple[None]:
        """
        id: TQ1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[TQ1, ...]: (Timing/Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        return self._c_data[1]

    @timing_or_quantity.setter  # set TQ1
    def timing_or_quantity(self, tq1: TQ1 | tuple[TQ1, ...] | None):
        """
        id: TQ1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: TQ1.6 | tuple[TQ1, ...]: (Timing/Quantity, ...)
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
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NTE.7 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[2] = nte
        else:
            self._c_data[2] = (nte,)

    @property  # get SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP.None
    def patient(self) -> SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP | None:
        """
        id: SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP.None
    def patient(self, patient: SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP | None):
        """
        id: SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get RESOURCES
    def resources(self) -> tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP, ...]:
        """
        id: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP
        """
        return self._c_data[4]

    @resources.setter  # set RESOURCES
    def resources(
        self,
        resources: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP
        | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP, ...],
    ):
        """
        id: RESOURCES SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP.None | tuple[SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SQR_S25_SCHEDULE_GROUP_RESOURCES_GROUP
        """
        if isinstance(resources, tuple):
            self._c_data[4] = resources
        else:
            self._c_data[4] = (resources,)
