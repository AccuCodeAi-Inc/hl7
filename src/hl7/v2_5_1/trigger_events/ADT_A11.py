from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.EVN import EVN
from ..segments.DB1 import DB1
from ..segments.SFT import SFT
from ..segments.DG1 import DG1
from ..segments.PV1 import PV1
from ..segments.OBX import OBX
from ..segments.PV2 import PV2
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PD1 import PD1


"""
Cancel Admit/Visit Notification - ADT_A11
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A11 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A11
from utils.hl7.v2_5_1.segments import (
    DG1, PV1, PD1, DB1, MSH, SFT, PID, EVN, OBX, PV2
)

adt_a11 = ADT_A11(  #  - For “admitted” patients, the A11 event is sent when an A01 (admit/visit notification) event is cancelled, either because of an erroneous entry of the A01 event, or because of a decision not to admit the patient after all
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
    disability=None,  # DB1(...) 
    observation_or_result=None,  # OBX(...) 
    diagnosis=None,  # DG1(...) 
)

-----END TRIGGER_EVENT::ADT_A11 TEMPLATE-----
"""


class ADT_A11(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A11"""
    _hl7_name = """Cancel Admit/Visit Notification"""
    _hl7_description = """For “admitted” patients, the A11 event is sent when an A01 (admit/visit notification) event is cancelled, either because of an erroneous entry of the A01 event, or because of a decision not to admit the patient after all"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A11"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 1, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "R", "O", "O", "O", "B")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    _c_components = (MSH, SFT, EVN, PID, PD1, PV1, PV2, DB1, OBX, DG1)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "PV1", "PV2", "DB1", "OBX", "DG1")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "patient_visit", "patient_visit_additional_information", "disability", "observation_or_result", "diagnosis",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.6
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        patient_visit_additional_information: PV2 | None = None,  #  PV2.7
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.8
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.9
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.10
    ):
        """
                 - `ADT_A11 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A11>`_
                For “admitted” patients, the A11 event is sent when an A01 (admit/visit notification) event is cancelled, either because of an erroneous entry of the A01 event, or because of a decision not to admit the patient after all.

        For “non-admitted” patients, the A11 event is sent when an A04 (register a patient) event is cancelled, either because of an erroneous entry of the A04 event, or because of a decision not to check the patient in for the visit after all.  To cancel an A05 (pre-admit a patient) event, use the A38 (cancel pre-admit), which was new for Version 2.3 of this Standard.

        The fields included when this message is sent should be the fields pertinent to communicate this event.  When other important fields change, it is recommended that the A08 (update patient information) event be used in addition

        The DG1 segment remains in this message for backward compatibility only.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
                :param patient_visit: Patient Visit (id: PV1 | seq: 6 | use: R | rpt: 1)
                :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 7 | use: O | rpt: 1)
                :param disability: Disability (id: DB1 | seq: 8 | use: O | rpt: *)
                :param observation_or_result: Observation/Result (id: OBX | seq: 9 | use: O | rpt: *)
                :param diagnosis: Diagnosis (id: DG1 | seq: 10 | use: B | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 10
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.disability = disability
        self.observation_or_result = observation_or_result
        self.diagnosis = diagnosis

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

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[1]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 2
        ---
        param_type: SFT.2 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[1] = sft
        else:
            self._c_data[1] = (sft,)

    @property  # get EVN.3
    def event_type(self) -> EVN:
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        return_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[2][0]

    @event_type.setter  # set EVN.3
    def event_type(self, evn: EVN):
        """
        id: EVN | use: R | rpt: 1 | seq: 3
        ---
        param_type: EVN.3: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[2] = (evn,)

    @property  # get PID.4
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        return_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[3][0]

    @patient_identification.setter  # set PID.4
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 4
        ---
        param_type: PID.4: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[3] = (pid,)

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[4][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[4] = (pd1,)

    @property  # get PV1.6
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 6
        ---
        return_type: PV1.6: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[5][0]

    @patient_visit.setter  # set PV1.6
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 6
        ---
        param_type: PV1.6: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[5] = (pv1,)

    @property  # get PV2.7
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PV2.7: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[6][0]

    @patient_visit_additional_information.setter  # set PV2.7
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PV2.7: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[6] = (pv2,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[7]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: DB1.8 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[7] = db1
        else:
            self._c_data[7] = (db1,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[8]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: OBX.9 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[8] = obx
        else:
            self._c_data[8] = (obx,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: B | rpt: * | seq: 10
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[9]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: B | rpt: * | seq: 10
        ---
        param_type: DG1.10 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[9] = dg1
        else:
            self._c_data[9] = (dg1,)
