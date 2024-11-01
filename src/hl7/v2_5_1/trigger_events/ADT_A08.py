from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.UB2 import UB2
from ..segments.PV2 import PV2
from ..segments.EVN import EVN
from ..segments.UB1 import UB1
from ..segments.PID import PID
from ..segments.NK1 import NK1
from ..segments.DG1 import DG1
from ..segments.ACC import ACC
from ..segments.PD1 import PD1
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segment_groups.ADT_A08_PROCEDURE_GROUP import ADT_A08_PROCEDURE_GROUP
from ..segments.OBX import OBX
from ..segment_groups.ADT_A08_INSURANCE_GROUP import ADT_A08_INSURANCE_GROUP
from ..segments.ROL import ROL
from ..segments.DB1 import DB1
from ..segments.PDA import PDA
from ..segments.PV1 import PV1
from ..segments.GT1 import GT1
from ..segments.DRG import DRG
from ..segments.AL1 import AL1


"""
Update Patient Information - ADT_A08
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::ADT_A08 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADT_A08
from utils.hl7.v2_5_1.segments import (
    PV1, EVN, DG1, ROL, PID, NK1, MSH, PV2, AL1, UB1, DB1, PD1, OBX, DRG, UB2, SFT, ACC, GT1, PDA
)
from utils.hl7.v2_5_1.segment_groups import (
    ADT_A08_PROCEDURE_GROUP, ADT_A08_INSURANCE_GROUP
)

adt_a08 = ADT_A08(  #  - This trigger event is used when any patient information has changed but when no other trigger event has occurred
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    role=None,  # ROL(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
    role_10=None,  # ROL(...) 
    disability=None,  # DB1(...) 
    observation_or_result=None,  # OBX(...) 
    patient_allergy_information=None,  # AL1(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    procedure=None,  # ADT_A08_PROCEDURE_GROUP(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # ADT_A08_INSURANCE_GROUP(...) 
    accident=None,  # ACC(...) 
    ub82_data=None,  # UB1(...) 
    ub92_data=None,  # UB2(...) 
    patient_death_and_autopsy=None,  # PDA(...) 
)

-----END TRIGGER_EVENT::ADT_A08 TEMPLATE-----
"""


class ADT_A08(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """ADT_A08"""
    _hl7_name = """Update Patient Information"""
    _hl7_description = """This trigger event is used when any patient information has changed but when no other trigger event has occurred"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A08"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535, 65535, 65535, 1, 1, 1, 1)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "None", "18", "None", "23", "24", "25", "26")
    _c_components = (MSH, SFT, EVN, PID, PD1, ROL, NK1, PV1, PV2, ROL, DB1, OBX, AL1, DG1, DRG, ADT_A08_PROCEDURE_GROUP, GT1, ADT_A08_INSURANCE_GROUP, ACC, UB1, UB2, PDA)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "ROL", "NK1", "PV1", "PV2", "ROL", "DB1", "OBX", "AL1", "DG1", "DRG", "PROCEDURE", "GT1", "INSURANCE", "ACC", "UB1", "UB2", "PDA")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "role", "next_of_kin_or_associated_parties", "patient_visit", "patient_visit_additional_information", "role_10", "disability", "observation_or_result", "patient_allergy_information", "diagnosis", "diagnosis_related_group", "procedure", "guarantor", "insurance", "accident", "ub82_data", "ub92_data", "patient_death_and_autopsy",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.8
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.6
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.7
        patient_visit_additional_information: PV2 | None = None,  #  PV2.9
        role_10: ROL | tuple[ROL, ...] | None = None,  #  ROL.10
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.11
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.12
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.13
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.14
        diagnosis_related_group: DRG | None = None,  #  DRG.15
        procedure: ADT_A08_PROCEDURE_GROUP
        | tuple[ADT_A08_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.16, ROL.17, ...)
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.18
        insurance: ADT_A08_INSURANCE_GROUP
        | tuple[ADT_A08_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.19, IN2.20, IN3.21, ROL.22, ...)
        accident: ACC | None = None,  #  ACC.23
        ub82_data: UB1 | None = None,  #  UB1.24
        ub92_data: UB2 | None = None,  #  UB2.25
        patient_death_and_autopsy: PDA | None = None,  #  PDA.26
    ):
        """
         - `ADT_A08 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADT_A08>`_
        This trigger event is used when any patient information has changed but when no other trigger event has occurred.  For example, an A08 event can be used to notify the receiving systems of a change of address or a name change.  We strongly recommend that the A08 transaction be used to update fields that are not updated by any of the other trigger events.  If there are specific trigger events for this update, these trigger events should be used. For example, if a patient's address and location are to be changed, then an A08 is used to change the patient address and the appropriate patient location trigger event is used to change the patient location. The A08 event can include information specific to an episode of care, but it can also be used for demographic information only.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
        :param role: Role (id: ROL | seq: 6 | use: O | rpt: *)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 7 | use: O | rpt: *)
        :param patient_visit: Patient Visit (id: PV1 | seq: 8 | use: R | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 9 | use: O | rpt: 1)
        :param role_10: Role (id: ROL | seq: 10 | use: O | rpt: *)
        :param disability: Disability (id: DB1 | seq: 11 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 12 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 13 | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 14 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 15 | use: O | rpt: 1)
        :param procedure: Procedure segment group: [PR1, ROL|None] (id: PROCEDURE | seq: 16, 17 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 18 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None, ROL|None] (id: INSURANCE | seq: 19, 20, 21, 22 | use: O | rpt: *)
        :param accident: Accident (id: ACC | seq: 23 | use: O | rpt: 1)
        :param ub82_data: UB82 Data (id: UB1 | seq: 24 | use: O | rpt: 1)
        :param ub92_data: UB92 Data (id: UB2 | seq: 25 | use: O | rpt: 1)
        :param patient_death_and_autopsy: Patient Death and Autopsy (id: PDA | seq: 26 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 22
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.role = role
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.role_10 = role_10
        self.disability = disability
        self.observation_or_result = observation_or_result
        self.patient_allergy_information = patient_allergy_information
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.procedure = procedure
        self.guarantor = guarantor
        self.insurance = insurance
        self.accident = accident
        self.ub82_data = ub82_data
        self.ub92_data = ub92_data
        self.patient_death_and_autopsy = patient_death_and_autopsy

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

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[6]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 7
        ---
        param_type: NK1.7 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[6] = nk1
        else:
            self._c_data[6] = (nk1,)

    @property  # get PV1.8
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 8
        ---
        return_type: PV1.8: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[7][0]

    @patient_visit.setter  # set PV1.8
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 8
        ---
        param_type: PV1.8: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[7] = (pv1,)

    @property  # get PV2.9
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 9
        ---
        return_type: PV2.9: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[8][0]

    @patient_visit_additional_information.setter  # set PV2.9
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 9
        ---
        param_type: PV2.9: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[8] = (pv2,)

    @property  # get ROL
    def role_10(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[9]

    @role_10.setter  # set ROL
    def role_10(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: ROL.10 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[9] = rol
        else:
            self._c_data[9] = (rol,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[10]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: DB1.11 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[10] = db1
        else:
            self._c_data[10] = (db1,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[11]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: OBX.12 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[11] = obx
        else:
            self._c_data[11] = (obx,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[12]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: AL1.13 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[12] = al1
        else:
            self._c_data[12] = (al1,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[13]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 14
        ---
        param_type: DG1.14 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[13] = dg1
        else:
            self._c_data[13] = (dg1,)

    @property  # get DRG.15
    def diagnosis_related_group(self) -> DRG | None:
        """
        id: DRG | use: O | rpt: 1 | seq: 15
        ---
        return_type: DRG.15: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[14][0]

    @diagnosis_related_group.setter  # set DRG.15
    def diagnosis_related_group(self, drg: DRG | None):
        """
        id: DRG | use: O | rpt: 1 | seq: 15
        ---
        param_type: DRG.15: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        self._c_data[14] = (drg,)

    @property  # get PROCEDURE
    def procedure(self) -> tuple[ADT_A08_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: ADT_A08_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ADT_A08_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A08_PROCEDURE_GROUP
        """
        return self._c_data[15]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: ADT_A08_PROCEDURE_GROUP | tuple[ADT_A08_PROCEDURE_GROUP, ...] | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ADT_A08_PROCEDURE_GROUP.None | tuple[ADT_A08_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A08_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[15] = procedure
        else:
            self._c_data[15] = (procedure,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[16]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: GT1.18 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[16] = gt1
        else:
            self._c_data[16] = (gt1,)

    @property  # get INSURANCE
    def insurance(self) -> tuple[ADT_A08_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: ADT_A08_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ADT_A08_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A08_INSURANCE_GROUP
        """
        return self._c_data[17]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: ADT_A08_INSURANCE_GROUP | tuple[ADT_A08_INSURANCE_GROUP, ...] | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ADT_A08_INSURANCE_GROUP.None | tuple[ADT_A08_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADT_A08_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[17] = insurance
        else:
            self._c_data[17] = (insurance,)

    @property  # get ACC.23
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 23
        ---
        return_type: ACC.23: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[18][0]

    @accident.setter  # set ACC.23
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 23
        ---
        param_type: ACC.23: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[18] = (acc,)

    @property  # get UB1.24
    def ub82_data(self) -> UB1 | None:
        """
        id: UB1 | use: O | rpt: 1 | seq: 24
        ---
        return_type: UB1.24: UB82 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1
        """
        return self._c_data[19][0]

    @ub82_data.setter  # set UB1.24
    def ub82_data(self, ub1: UB1 | None):
        """
        id: UB1 | use: O | rpt: 1 | seq: 24
        ---
        param_type: UB1.24: UB82 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1
        """
        self._c_data[19] = (ub1,)

    @property  # get UB2.25
    def ub92_data(self) -> UB2 | None:
        """
        id: UB2 | use: O | rpt: 1 | seq: 25
        ---
        return_type: UB2.25: UB92 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2
        """
        return self._c_data[20][0]

    @ub92_data.setter  # set UB2.25
    def ub92_data(self, ub2: UB2 | None):
        """
        id: UB2 | use: O | rpt: 1 | seq: 25
        ---
        param_type: UB2.25: UB92 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2
        """
        self._c_data[20] = (ub2,)

    @property  # get PDA.26
    def patient_death_and_autopsy(self) -> PDA | None:
        """
        id: PDA | use: O | rpt: 1 | seq: 26
        ---
        return_type: PDA.26: Patient Death and Autopsy
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDA
        """
        return self._c_data[21][0]

    @patient_death_and_autopsy.setter  # set PDA.26
    def patient_death_and_autopsy(self, pda: PDA | None):
        """
        id: PDA | use: O | rpt: 1 | seq: 26
        ---
        param_type: PDA.26: Patient Death and Autopsy
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PDA
        """
        self._c_data[21] = (pda,)
