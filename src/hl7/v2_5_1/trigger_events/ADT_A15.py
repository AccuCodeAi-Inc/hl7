from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.EVN import EVN
from ..segments.DB1 import DB1
from ..segments.SFT import SFT
from ..segments.ROL import ROL
from ..segments.DG1 import DG1
from ..segments.PV1 import PV1
from ..segments.OBX import OBX
from ..segments.PV2 import PV2
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PD1 import PD1


"""
Pending Transfer - ADT_A15
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A15 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A15
from utils.hl7.v2_5_1.segments import (
    DG1, PV1, ROL, PD1, DB1, MSH, SFT, PID, EVN, OBX, PV2
)

adt_a15 = ADT_A15(  #  - An A15 event notifies other systems of a plan to transfer a patient to a new location when the patient has not yet left the old location
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    role=None,  # ROL(...) 
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
    role_9=None,  # ROL(...) 
    disability=None,  # DB1(...) 
    observation_or_result=None,  # OBX(...) 
    diagnosis=None,  # DG1(...) 
)

-----END TRIGGER_EVENT::ADT_A15 TEMPLATE-----
"""


class ADT_A15(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A15"""
    _hl7_name = """Pending Transfer"""
    _hl7_description = """An A15 event notifies other systems of a plan to transfer a patient to a new location when the patient has not yet left the old location"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A15"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 1, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "O", "R", "O", "O", "O", "O", "B")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    _c_components = (MSH, SFT, EVN, PID, PD1, ROL, PV1, PV2, ROL, DB1, OBX, DG1)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "ROL", "PV1", "PV2", "ROL", "DB1", "OBX", "DG1")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "role", "patient_visit", "patient_visit_additional_information", "role_9", "disability", "observation_or_result", "diagnosis",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.7
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.6
        patient_visit_additional_information: PV2 | None = None,  #  PV2.8
        role_9: ROL | tuple[ROL, ...] | None = None,  #  ROL.9
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.10
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.11
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.12
    ):
        """
                 - `ADT_A15 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A15>`_
                An A15 event notifies other systems of a plan to transfer a patient to a new location when the patient has not yet left the old location.  It is used when advanced notification of a transfer is required in order to prepare for the patient’s location change.  For example, this transaction could be sent so that staff will be on hand to move the patient or so that dietary services can route the next meal to the new location.

        The fields included when this message is sent should be the fields pertinent to communicate this event.  When other important fields change, it is recommended that the A08 (update patient information) event be used in addition.

        The DG1 segment remains in this message for backward compatibility only.

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
                :param role: Role (id: ROL | seq: 6 | use: O | rpt: *)
                :param patient_visit: Patient Visit (id: PV1 | seq: 7 | use: R | rpt: 1)
                :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 8 | use: O | rpt: 1)
                :param role_9: Role (id: ROL | seq: 9 | use: O | rpt: *)
                :param disability: Disability (id: DB1 | seq: 10 | use: O | rpt: *)
                :param observation_or_result: Observation/Result (id: OBX | seq: 11 | use: O | rpt: *)
                :param diagnosis: Diagnosis (id: DG1 | seq: 12 | use: B | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.role = role
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.role_9 = role_9
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

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[5]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: ROL.6 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[5] = rol
        else:
            self._c_data[5] = (rol,)

    @property  # get PV1.7
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 7
        ---
        return_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[6][0]

    @patient_visit.setter  # set PV1.7
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 7
        ---
        param_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[6] = (pv1,)

    @property  # get PV2.8
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        return_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[7][0]

    @patient_visit_additional_information.setter  # set PV2.8
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        param_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[7] = (pv2,)

    @property  # get ROL
    def role_9(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[8]

    @role_9.setter  # set ROL
    def role_9(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: ROL.9 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[8] = rol
        else:
            self._c_data[8] = (rol,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[9]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: DB1.10 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[9] = db1
        else:
            self._c_data[9] = (db1,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[10]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: OBX.11 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[10] = obx
        else:
            self._c_data[10] = (obx,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: B | rpt: * | seq: 12
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[11]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: B | rpt: * | seq: 12
        ---
        param_type: DG1.12 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[11] = dg1
        else:
            self._c_data[11] = (dg1,)
