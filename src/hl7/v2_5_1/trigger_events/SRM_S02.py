from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.ARQ import ARQ
from ..segments.APR import APR
from ..segments.MSH import MSH
from ..segment_groups.SRM_S02_RESOURCES_GROUP import SRM_S02_RESOURCES_GROUP
from ..segments.NTE import NTE
from ..segment_groups.SRM_S02_PATIENT_GROUP import SRM_S02_PATIENT_GROUP


"""
Schedule request - Appointment rescheduling - SRM_S02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::SRM_S02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import SRM_S02
from utils.hl7.v2_5_1.segments import (
    NTE, ARQ, APR, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    SRM_S02_RESOURCES_GROUP, SRM_S02_PATIENT_GROUP
)

srm_s02 = SRM_S02(  #  - A placer application uses this trigger event to request that an existing appointment be rescheduled
    message_header=msh,  # MSH(...)  # Required.
    appointment_request=arq,  # ARQ(...)  # Required.
    appointment_preferences=None,  # APR(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # SRM_S02_PATIENT_GROUP(...) 
    resources=srm_s02_resources_group,  # SRM_S02_RESOURCES_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::SRM_S02 TEMPLATE-----
"""


class SRM_S02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """SRM_S02"""
    _hl7_name = """Schedule request - Appointment rescheduling"""
    _hl7_description = """A placer application uses this trigger event to request that an existing appointment be rescheduled"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "R", "O", "O", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "None", "None")
    _c_components = (MSH, ARQ, APR, NTE, SRM_S02_PATIENT_GROUP, SRM_S02_RESOURCES_GROUP)
    _c_name = ("MSH", "ARQ", "APR", "NTE", "PATIENT", "RESOURCES")
    _c_is_group = (False, False, False, False, True, True)
    _c_attrs = ("message_header", "appointment_request", "appointment_preferences", "notes_and_comments", "patient", "resources",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        appointment_request: ARQ,  #  Required. ARQ.2
        resources: SRM_S02_RESOURCES_GROUP
        | tuple[SRM_S02_RESOURCES_GROUP, ...],  #  Required. (RGS.10, ...)
        appointment_preferences: APR | None = None,  #  APR.3
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.4
        patient: SRM_S02_PATIENT_GROUP
        | tuple[SRM_S02_PATIENT_GROUP, ...]
        | None = None,  #  (PID.5, PV1.6, PV2.7, OBX.8, DG1.9, ...)
    ):
        """
         - `SRM_S02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/SRM_S02>`_
        A placer application uses this trigger event to request that an existing appointment be rescheduled.  The new Requested Start Date and Time, Appointment Duration, Repeating Interval, Repeating Interval Duration, and/or Priority are provided in the ARQ segment, along with the existing placer and filler identification numbers.  If it is successful, an application acknowledgment is returned, optionally containing an SCH segment and related detail segments describing the new information for the rescheduled appointment.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param appointment_request: Appointment Request (id: ARQ | seq: 2 | use: R | rpt: 1)
        :param appointment_preferences: Appointment Preferences (id: APR | seq: 3 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 4 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PV1|None, PV2|None, OBX|None, DG1|None] (id: PATIENT | seq: 5, 6, 7, 8, 9 | use: O | rpt: *)
        :param resources: Resources segment group: [RGS, SERVICE|None, GENERAL RESOURCE|None, LOCATION RESOURCE|None, PERSONNEL RESOURCE|None] (id: RESOURCES | seq: 10, None, None, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.appointment_request = appointment_request
        self.appointment_preferences = appointment_preferences
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

    @property  # get ARQ.2
    def appointment_request(self) -> ARQ:
        """
        id: ARQ | use: R | rpt: 1 | seq: 2
        ---
        return_type: ARQ.2: Appointment Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ARQ
        """
        return self._c_data[1][0]

    @appointment_request.setter  # set ARQ.2
    def appointment_request(self, arq: ARQ):
        """
        id: ARQ | use: R | rpt: 1 | seq: 2
        ---
        param_type: ARQ.2: Appointment Request
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ARQ
        """
        self._c_data[1] = (arq,)

    @property  # get APR.3
    def appointment_preferences(self) -> APR | None:
        """
        id: APR | use: O | rpt: 1 | seq: 3
        ---
        return_type: APR.3: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        return self._c_data[2][0]

    @appointment_preferences.setter  # set APR.3
    def appointment_preferences(self, apr: APR | None):
        """
        id: APR | use: O | rpt: 1 | seq: 3
        ---
        param_type: APR.3: Appointment Preferences
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/APR
        """
        self._c_data[2] = (apr,)

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
    def patient(self) -> tuple[SRM_S02_PATIENT_GROUP, ...] | tuple[None]:
        """
        id: SRM_S02_PATIENT_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[SRM_S02_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S02_PATIENT_GROUP
        """
        return self._c_data[4]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: SRM_S02_PATIENT_GROUP | tuple[SRM_S02_PATIENT_GROUP, ...] | None
    ):
        """
        id: PATIENT SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: SRM_S02_PATIENT_GROUP.None | tuple[SRM_S02_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S02_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[4] = patient
        else:
            self._c_data[4] = (patient,)

    @property  # get RESOURCES
    def resources(self) -> tuple[SRM_S02_RESOURCES_GROUP, ...]:
        """
        id: SRM_S02_RESOURCES_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[SRM_S02_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S02_RESOURCES_GROUP
        """
        return self._c_data[5]

    @resources.setter  # set RESOURCES
    def resources(
        self, resources: SRM_S02_RESOURCES_GROUP | tuple[SRM_S02_RESOURCES_GROUP, ...]
    ):
        """
        id: RESOURCES SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: SRM_S02_RESOURCES_GROUP.None | tuple[SRM_S02_RESOURCES_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SRM_S02_RESOURCES_GROUP
        """
        if isinstance(resources, tuple):
            self._c_data[5] = resources
        else:
            self._c_data[5] = (resources,)
