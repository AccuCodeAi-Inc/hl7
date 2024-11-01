from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.SIU_S18_PATIENT_GROUP import SIU_S18_PATIENT_GROUP
from ..segments.SCH import SCH
from ..segments.MSH import MSH
from ..segments.TQ1 import TQ1
from ..segment_groups.SIU_S18_RESOURCES_GROUP import SIU_S18_RESOURCES_GROUP
from ..segments.NTE import NTE


"""
Notification of Addition of Service/Resource on Appointment - SIU_S18
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SIU_S18 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SIU_S18
from utils.hl7.v2_5_1.segments import (
    NTE, SCH, TQ1, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SIU_S18_RESOURCES_GROUP, SIU_S18_PATIENT_GROUP
)

siu_s18 = SIU_S18(  #  - The notification of addition of service/resource is triggered on the filler application when a new service or resource has been added to an existing appointment
    message_header=msh,  # MSH(...)  # Required.
    scheduling_activity_information=sch,  # SCH(...)  # Required.
    timing_or_quantity=None,  # TQ1(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # SIU_S18_PATIENT_GROUP(...) 
    resources=siu_s18_resources_group,  # SIU_S18_RESOURCES_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::SIU_S18 TEMPLATE-----
"""


class SIU_S18(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SIU_S18"""
    _hl7_name = """Notification of Addition of Service/Resource on Appointment"""
    _hl7_description = """The notification of addition of service/resource is triggered on the filler application when a new service or resource has been added to an existing appointment"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S18"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "None", "None")
    _c_components = (MSH, SCH, TQ1, NTE, SIU_S18_PATIENT_GROUP, SIU_S18_RESOURCES_GROUP)
    _c_name = ("MSH", "SCH", "TQ1", "NTE", "PATIENT", "RESOURCES")
    _c_is_group = (False, False, False, False, True, True)
    _c_attrs = ("message_header", "scheduling_activity_information", "timing_or_quantity", "notes_and_comments", "patient", "resources",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        scheduling_activity_information: SCH,  #  Required. SCH.2
        resources: SIU_S18_RESOURCES_GROUP
        | tuple[SIU_S18_RESOURCES_GROUP, ...],  #  Required. (RGS.11, ...)
        timing_or_quantity: TQ1 | tuple[TQ1, ...] | None = None,  #  TQ1.3
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.4
        patient: SIU_S18_PATIENT_GROUP
        | tuple[SIU_S18_PATIENT_GROUP, ...]
        | None = None,  #  (PID.5, PD1.6, PV1.7, PV2.8, OBX.9, DG1.10, ...)
    ):
        """
         - `SIU_S18 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SIU_S18>`_
        The notification of addition of service/resource is triggered on the filler application when a new service or resource has been added to an existing appointment.  Services and resources are represented by the AIS, AIG, AIL, and AIP segments on an HL7 scheduling interface transaction.  This trigger event should only be used for appointments that have not been completed, or for parent appointments whose children have not been completed.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param scheduling_activity_information: Scheduling Activity Information (id: SCH | seq: 2 | use: R | rpt: 1)
        :param timing_or_quantity: Timing/Quantity (id: TQ1 | seq: 3 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 4 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PD1|None, PV1|None, PV2|None, OBX|None, DG1|None] (id: PATIENT | seq: 5, 6, 7, 8, 9, 10 | use: O | rpt: *)
        :param resources: Resources segment group: [RGS, SERVICE|None, GENERAL RESOURCE|None, LOCATION RESOURCE|None, PERSONNEL RESOURCE|None] (id: RESOURCES | seq: 11, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.scheduling_activity_information = scheduling_activity_information
        self.timing_or_quantity = timing_or_quantity
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.resources = resources

    @property  # get MSH.1
    def message_header(self) -> MSH:
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        return_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        return self._c_data[0][0]

    @message_header.setter  # set MSH.1
    def message_header(self, msh: MSH):
        """
        id: MSH | use: R | rpt: 1 | seq: 1
        ---
        param_type: MSH.1: Message Header
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSH
        """
        self._c_data[0] = (msh,)

    @property  # get SCH.2
    def scheduling_activity_information(self) -> SCH:
        """
        id: SCH | use: R | rpt: 1 | seq: 2
        ---
        return_type: SCH.2: Scheduling Activity Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH
        """
        return self._c_data[1][0]

    @scheduling_activity_information.setter  # set SCH.2
    def scheduling_activity_information(self, sch: SCH):
        """
        id: SCH | use: R | rpt: 1 | seq: 2
        ---
        param_type: SCH.2: Scheduling Activity Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SCH
        """
        self._c_data[1] = (sch,)

    @property  # get TQ1
    def timing_or_quantity(self) -> tuple[TQ1, ...] | tuple[None]:
        """
        id: TQ1 SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        return_type: tuple[TQ1, ...]: (Timing/Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        return self._c_data[2]

    @timing_or_quantity.setter  # set TQ1
    def timing_or_quantity(self, tq1: TQ1 | tuple[TQ1, ...] | None):
        """
        id: TQ1 SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        param_type: TQ1.3 | tuple[TQ1, ...]: (Timing/Quantity, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/TQ1
        """
        if isinstance(tq1, tuple):
            self._c_data[2] = tq1
        else:
            self._c_data[2] = (tq1,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[3]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: NTE.4 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[3] = nte
        else:
            self._c_data[3] = (nte,)

    @property  # get PATIENT
    def patient(self) -> tuple[SIU_S18_PATIENT_GROUP, ...] | tuple[None]:
        """
        id: SIU_S18_PATIENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SIU_S18_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SIU_S18_PATIENT_GROUP
        """
        return self._c_data[4]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: SIU_S18_PATIENT_GROUP | tuple[SIU_S18_PATIENT_GROUP, ...] | None
    ):
        """
        id: PATIENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SIU_S18_PATIENT_GROUP.None | tuple[SIU_S18_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SIU_S18_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[4] = patient
        else:
            self._c_data[4] = (patient,)

    @property  # get RESOURCES
    def resources(self) -> tuple[SIU_S18_RESOURCES_GROUP, ...]:
        """
        id: SIU_S18_RESOURCES_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SIU_S18_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SIU_S18_RESOURCES_GROUP
        """
        return self._c_data[5]

    @resources.setter  # set RESOURCES
    def resources(
        self, resources: SIU_S18_RESOURCES_GROUP | tuple[SIU_S18_RESOURCES_GROUP, ...]
    ):
        """
        id: RESOURCES SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SIU_S18_RESOURCES_GROUP.None | tuple[SIU_S18_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SIU_S18_RESOURCES_GROUP
        """
        if isinstance(resources, tuple):
            self._c_data[5] = resources
        else:
            self._c_data[5] = (resources,)
