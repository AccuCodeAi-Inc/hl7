from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segment_groups.ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP import (
    ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP,
)
from ..segments.AL1 import AL1
from ..segments.EVN import EVN
from ..segments.DB1 import DB1
from ..segment_groups.ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP import (
    ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP,
)
from ..segments.ACC import ACC
from ..segments.ROL import ROL
from ..segments.DG1 import DG1
from ..segments.PV1 import PV1
from ..segments.OBX import OBX
from ..segments.PV2 import PV2
from ..segments.GT1 import GT1
from ..segments.PID import PID
from ..segments.UB1 import UB1
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.DRG import DRG
from ..segments.UB2 import UB2


"""
QUERY RESPONSE - ADR_A19_QUERY_RESPONSE_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::ADR_A19_QUERY_RESPONSE_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import ADR_A19_QUERY_RESPONSE_GROUP
from utils.hl7.v2_5_1.segments import (
    DG1, PV1, ROL, DRG, UB2, GT1, PD1, DB1, NK1, UB1, AL1, PID, EVN, ACC, OBX, PV2
)
from utils.hl7.v2_5_1.segment_groups import (
    ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP
)

adr_a19_query_response_group = ADR_A19_QUERY_RESPONSE_GROUP(  # QUERY RESPONSE - Segment group for ADR_A19 - Patient Query - Response consisting of EVN|None, PID, PD1|None, ROL|None, NK1|None, PV1, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None
    event_type=None,  # EVN(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    role=None,  # ROL(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    patient_visit=pv1,  # PV1(...)  # Required.
    patient_visit_additional_information=None,  # PV2(...) 
    role_15=None,  # ROL(...) 
    disability=None,  # DB1(...) 
    observation_or_result=None,  # OBX(...) 
    patient_allergy_information=None,  # AL1(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    procedure=None,  # ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP(...) 
    accident=None,  # ACC(...) 
    ub82_data=None,  # UB1(...) 
    ub92_data=None,  # UB2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::ADR_A19_QUERY_RESPONSE_GROUP TEMPLATE-----
"""


class ADR_A19_QUERY_RESPONSE_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """ADR_A19_QUERY_RESPONSE_GROUP"""
    _hl7_name = """QUERY RESPONSE"""
    _hl7_description = """Segment group for ADR_A19 - Patient Query - Response consisting of EVN|None, PID, PD1|None, ROL|None, NK1|None, PV1, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADR_A19_QUERY_RESPONSE_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 1, 65535, 65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535, 65535, 65535, 1, 1, 1)
    _c_usage = ("O", "R", "O", "O", "O", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "None", "23", "None", "28", "29", "30")
    _c_components = (EVN, PID, PD1, ROL, NK1, PV1, PV2, ROL, DB1, OBX, AL1, DG1, DRG, ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, GT1, ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP, ACC, UB1, UB2)
    _c_name = ("EVN", "PID", "PD1", "ROL", "NK1", "PV1", "PV2", "ROL", "DB1", "OBX", "AL1", "DG1", "DRG", "PROCEDURE", "GT1", "INSURANCE", "ACC", "UB1", "UB2")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False)
    _c_attrs = ("event_type", "patient_identification", "patient_additional_demographic", "role", "next_of_kin_or_associated_parties", "patient_visit", "patient_visit_additional_information", "role_15", "disability", "observation_or_result", "patient_allergy_information", "diagnosis", "diagnosis_related_group", "procedure", "guarantor", "insurance", "accident", "ub82_data", "ub92_data",)
    # fmt: on

    def __init__(
        self,
        patient_identification: PID,  #  Required. PID.9
        patient_visit: PV1,  #  Required. PV1.13
        event_type: EVN | None = None,  #  EVN.8
        patient_additional_demographic: PD1 | None = None,  #  PD1.10
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.11
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.12
        patient_visit_additional_information: PV2 | None = None,  #  PV2.14
        role_15: ROL | tuple[ROL, ...] | None = None,  #  ROL.15
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.16
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.17
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.18
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.19
        diagnosis_related_group: DRG | None = None,  #  DRG.20
        procedure: ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP
        | tuple[ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.21, ROL.22, ...)
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.23
        insurance: ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP
        | tuple[ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.24, IN2.25, IN3.26, ROL.27, ...)
        accident: ACC | None = None,  #  ACC.28
        ub82_data: UB1 | None = None,  #  UB1.29
        ub92_data: UB2 | None = None,  #  UB2.30
    ):
        """
        None - `ADR_A19_QUERY_RESPONSE_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/ADR_A19_QUERY_RESPONSE_GROUP>`_
        Segment group for ADR_A19 - Patient Query - Response consisting of EVN|None, PID, PD1|None, ROL|None, NK1|None, PV1, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None

        :param event_type: Event Type (id: EVN | seq: 8 | use: O | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 9 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 10 | use: O | rpt: 1)
        :param role: Role (id: ROL | seq: 11 | use: O | rpt: *)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 12 | use: O | rpt: *)
        :param patient_visit: Patient Visit (id: PV1 | seq: 13 | use: R | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 14 | use: O | rpt: 1)
        :param role_15: Role (id: ROL | seq: 15 | use: O | rpt: *)
        :param disability: Disability (id: DB1 | seq: 16 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 17 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 18 | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 19 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 20 | use: O | rpt: 1)
        :param procedure: Procedure segment group: [PR1, ROL|None] (id: PROCEDURE | seq: 21, 22 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 23 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None, ROL|None] (id: INSURANCE | seq: 24, 25, 26, 27 | use: O | rpt: *)
        :param accident: Accident (id: ACC | seq: 28 | use: O | rpt: 1)
        :param ub82_data: UB82 Data (id: UB1 | seq: 29 | use: O | rpt: 1)
        :param ub92_data: UB92 Data (id: UB2 | seq: 30 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 19
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.role = role
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.role_15 = role_15
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

    @property  # get EVN.8
    def event_type(self) -> EVN | None:
        """
        id: EVN | use: O | rpt: 1 | seq: 8
        ---
        return_type: EVN.8: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        return self._c_data[0][0]

    @event_type.setter  # set EVN.8
    def event_type(self, evn: EVN | None):
        """
        id: EVN | use: O | rpt: 1 | seq: 8
        ---
        param_type: EVN.8: Event Type
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/EVN
        """
        self._c_data[0] = (evn,)

    @property  # get PID.9
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 9
        ---
        return_type: PID.9: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[1][0]

    @patient_identification.setter  # set PID.9
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 9
        ---
        param_type: PID.9: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[1] = (pid,)

    @property  # get PD1.10
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 10
        ---
        return_type: PD1.10: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[2][0]

    @patient_additional_demographic.setter  # set PD1.10
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 10
        ---
        param_type: PD1.10: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[2] = (pd1,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[3]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: ROL.11 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[3] = rol
        else:
            self._c_data[3] = (rol,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[4]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: NK1.12 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[4] = nk1
        else:
            self._c_data[4] = (nk1,)

    @property  # get PV1.13
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 13
        ---
        return_type: PV1.13: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[5][0]

    @patient_visit.setter  # set PV1.13
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 13
        ---
        param_type: PV1.13: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[5] = (pv1,)

    @property  # get PV2.14
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 14
        ---
        return_type: PV2.14: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[6][0]

    @patient_visit_additional_information.setter  # set PV2.14
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 14
        ---
        param_type: PV2.14: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[6] = (pv2,)

    @property  # get ROL
    def role_15(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[7]

    @role_15.setter  # set ROL
    def role_15(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: ROL.15 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[7] = rol
        else:
            self._c_data[7] = (rol,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[8]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: DB1.16 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[8] = db1
        else:
            self._c_data[8] = (db1,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[9]

    @observation_or_result.setter  # set OBX
    def observation_or_result(self, obx: OBX | tuple[OBX, ...] | None):
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: OBX.17 | tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        if isinstance(obx, tuple):
            self._c_data[9] = obx
        else:
            self._c_data[9] = (obx,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[10]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: AL1.18 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[10] = al1
        else:
            self._c_data[10] = (al1,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[11]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 19
        ---
        param_type: DG1.19 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[11] = dg1
        else:
            self._c_data[11] = (dg1,)

    @property  # get DRG.20
    def diagnosis_related_group(self) -> DRG | None:
        """
        id: DRG | use: O | rpt: 1 | seq: 20
        ---
        return_type: DRG.20: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[12][0]

    @diagnosis_related_group.setter  # set DRG.20
    def diagnosis_related_group(self, drg: DRG | None):
        """
        id: DRG | use: O | rpt: 1 | seq: 20
        ---
        param_type: DRG.20: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        self._c_data[12] = (drg,)

    @property  # get PROCEDURE
    def procedure(
        self,
    ) -> tuple[ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP
        """
        return self._c_data[13]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP
        | tuple[ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, ...]
        | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP.None | tuple[ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADR_A19_QUERY_RESPONSE_GROUP_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[13] = procedure
        else:
            self._c_data[13] = (procedure,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[14]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: GT1.23 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[14] = gt1
        else:
            self._c_data[14] = (gt1,)

    @property  # get INSURANCE
    def insurance(
        self,
    ) -> tuple[ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP
        """
        return self._c_data[15]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP
        | tuple[ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP, ...]
        | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP.None | tuple[ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ADR_A19_QUERY_RESPONSE_GROUP_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[15] = insurance
        else:
            self._c_data[15] = (insurance,)

    @property  # get ACC.28
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 28
        ---
        return_type: ACC.28: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[16][0]

    @accident.setter  # set ACC.28
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 28
        ---
        param_type: ACC.28: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[16] = (acc,)

    @property  # get UB1.29
    def ub82_data(self) -> UB1 | None:
        """
        id: UB1 | use: O | rpt: 1 | seq: 29
        ---
        return_type: UB1.29: UB82 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1
        """
        return self._c_data[17][0]

    @ub82_data.setter  # set UB1.29
    def ub82_data(self, ub1: UB1 | None):
        """
        id: UB1 | use: O | rpt: 1 | seq: 29
        ---
        param_type: UB1.29: UB82 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1
        """
        self._c_data[17] = (ub1,)

    @property  # get UB2.30
    def ub92_data(self) -> UB2 | None:
        """
        id: UB2 | use: O | rpt: 1 | seq: 30
        ---
        return_type: UB2.30: UB92 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2
        """
        return self._c_data[18][0]

    @ub92_data.setter  # set UB2.30
    def ub92_data(self, ub2: UB2 | None):
        """
        id: UB2 | use: O | rpt: 1 | seq: 30
        ---
        param_type: UB2.30: UB92 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2
        """
        self._c_data[18] = (ub2,)
