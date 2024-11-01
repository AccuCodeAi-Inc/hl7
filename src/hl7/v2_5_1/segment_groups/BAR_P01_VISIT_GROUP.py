from __future__ import annotations
from ...base import HL7SegmentGroup
from ..segments.OBX import OBX
from ..segments.DG1 import DG1
from ..segments.ACC import ACC
from ..segment_groups.BAR_P01_VISIT_GROUP_INSURANCE_GROUP import (
    BAR_P01_VISIT_GROUP_INSURANCE_GROUP,
)
from ..segments.UB2 import UB2
from ..segments.GT1 import GT1
from ..segments.PV2 import PV2
from ..segments.DRG import DRG
from ..segments.UB1 import UB1
from ..segment_groups.BAR_P01_VISIT_GROUP_PROCEDURE_GROUP import (
    BAR_P01_VISIT_GROUP_PROCEDURE_GROUP,
)
from ..segments.ROL import ROL
from ..segments.NK1 import NK1
from ..segments.DB1 import DB1
from ..segments.PV1 import PV1
from ..segments.AL1 import AL1


"""
VISIT - BAR_P01_VISIT_GROUP
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT_SEGMENT_GROUP::BAR_P01_VISIT_GROUP TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P01_VISIT_GROUP
from utils.hl7.v2_5_1.segments import (
    PV2, PV1, UB2, ACC, AL1, DG1, ROL, UB1, GT1, DB1, NK1, OBX, DRG
)
from utils.hl7.v2_5_1.segment_groups import (
    BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, BAR_P01_VISIT_GROUP_INSURANCE_GROUP
)

bar_p01_visit_group = BAR_P01_VISIT_GROUP(  # VISIT - Segment group for BAR_P01 - Add Patient Accounts consisting of PV1|None, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, NK1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None
    patient_visit=None,  # PV1(...) 
    patient_visit_additional_information=None,  # PV2(...) 
    role=None,  # ROL(...) 
    disability=None,  # DB1(...) 
    observation_or_result=None,  # OBX(...) 
    patient_allergy_information=None,  # AL1(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    procedure=None,  # BAR_P01_VISIT_GROUP_PROCEDURE_GROUP(...) 
    guarantor=None,  # GT1(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    insurance=None,  # BAR_P01_VISIT_GROUP_INSURANCE_GROUP(...) 
    accident=None,  # ACC(...) 
    ub82_data=None,  # UB1(...) 
    ub92_data=None,  # UB2(...) 
)

-----END TRIGGER_EVENT_SEGMENT_GROUP::BAR_P01_VISIT_GROUP TEMPLATE-----
"""


class BAR_P01_VISIT_GROUP(HL7SegmentGroup):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT_SEGMENT_GROUP"""
    _hl7_length = -1
    _hl7_id = """BAR_P01_VISIT_GROUP"""
    _hl7_name = """VISIT"""
    _hl7_description = """Segment group for BAR_P01 - Add Patient Accounts consisting of PV1|None, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, NK1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P01_VISIT_GROUP"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535, 65535, 65535, 65535, 1, 1, 1)
    _c_usage = ("O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("7", "8", "9", "10", "11", "12", "13", "14", "None", "17", "18", "None", "23", "24", "25")
    _c_components = (PV1, PV2, ROL, DB1, OBX, AL1, DG1, DRG, BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, GT1, NK1, BAR_P01_VISIT_GROUP_INSURANCE_GROUP, ACC, UB1, UB2)
    _c_name = ("PV1", "PV2", "ROL", "DB1", "OBX", "AL1", "DG1", "DRG", "PROCEDURE", "GT1", "NK1", "INSURANCE", "ACC", "UB1", "UB2")
    _c_is_group = (False, False, False, False, False, False, False, False, True, False, False, True, False, False, False)
    _c_attrs = ("patient_visit", "patient_visit_additional_information", "role", "disability", "observation_or_result", "patient_allergy_information", "diagnosis", "diagnosis_related_group", "procedure", "guarantor", "next_of_kin_or_associated_parties", "insurance", "accident", "ub82_data", "ub92_data",)
    # fmt: on

    def __init__(
        self,
        patient_visit: PV1 | None = None,  #  PV1.7
        patient_visit_additional_information: PV2 | None = None,  #  PV2.8
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.9
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.10
        observation_or_result: OBX | tuple[OBX, ...] | None = None,  #  OBX.11
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.12
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.13
        diagnosis_related_group: DRG | None = None,  #  DRG.14
        procedure: BAR_P01_VISIT_GROUP_PROCEDURE_GROUP
        | tuple[BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.15, ROL.16, ...)
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.17
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.18
        insurance: BAR_P01_VISIT_GROUP_INSURANCE_GROUP
        | tuple[BAR_P01_VISIT_GROUP_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.19, IN2.20, IN3.21, ROL.22, ...)
        accident: ACC | None = None,  #  ACC.23
        ub82_data: UB1 | None = None,  #  UB1.24
        ub92_data: UB2 | None = None,  #  UB2.25
    ):
        """
        None - `BAR_P01_VISIT_GROUP <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P01_VISIT_GROUP>`_
        Segment group for BAR_P01 - Add Patient Accounts consisting of PV1|None, PV2|None, ROL|None, DB1|None, OBX|None, AL1|None, DG1|None, DRG|None, PROCEDURE|None, GT1|None, NK1|None, INSURANCE|None, ACC|None, UB1|None, UB2|None

        :param patient_visit: Patient Visit (id: PV1 | seq: 7 | use: O | rpt: 1)
        :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 8 | use: O | rpt: 1)
        :param role: Role (id: ROL | seq: 9 | use: O | rpt: *)
        :param disability: Disability (id: DB1 | seq: 10 | use: O | rpt: *)
        :param observation_or_result: Observation/Result (id: OBX | seq: 11 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 12 | use: O | rpt: *)
        :param diagnosis: Diagnosis (id: DG1 | seq: 13 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 14 | use: O | rpt: 1)
        :param procedure: Procedure segment group: [PR1, ROL|None] (id: PROCEDURE | seq: 15, 16 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 17 | use: O | rpt: *)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 18 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None, ROL|None] (id: INSURANCE | seq: 19, 20, 21, 22 | use: O | rpt: *)
        :param accident: Accident (id: ACC | seq: 23 | use: O | rpt: 1)
        :param ub82_data: UB82 Data (id: UB1 | seq: 24 | use: O | rpt: 1)
        :param ub92_data: UB92 Data (id: UB2 | seq: 25 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 15
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.role = role
        self.disability = disability
        self.observation_or_result = observation_or_result
        self.patient_allergy_information = patient_allergy_information
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.procedure = procedure
        self.guarantor = guarantor
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.insurance = insurance
        self.accident = accident
        self.ub82_data = ub82_data
        self.ub92_data = ub92_data

    @property  # get PV1.7
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[0][0]

    @patient_visit.setter  # set PV1.7
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[0] = (pv1,)

    @property  # get PV2.8
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        return_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[1][0]

    @patient_visit_additional_information.setter  # set PV2.8
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        param_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[1] = (pv2,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[2]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: ROL.9 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[2] = rol
        else:
            self._c_data[2] = (rol,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[3]

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
            self._c_data[3] = db1
        else:
            self._c_data[3] = (db1,)

    @property  # get OBX
    def observation_or_result(self) -> tuple[OBX, ...] | tuple[None]:
        """
        id: OBX SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[OBX, ...]: (Observation/Result, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OBX
        """
        return self._c_data[4]

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
            self._c_data[4] = obx
        else:
            self._c_data[4] = (obx,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[5]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: AL1.12 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[5] = al1
        else:
            self._c_data[5] = (al1,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[6]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        param_type: DG1.13 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[6] = dg1
        else:
            self._c_data[6] = (dg1,)

    @property  # get DRG.14
    def diagnosis_related_group(self) -> DRG | None:
        """
        id: DRG | use: O | rpt: 1 | seq: 14
        ---
        return_type: DRG.14: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[7][0]

    @diagnosis_related_group.setter  # set DRG.14
    def diagnosis_related_group(self, drg: DRG | None):
        """
        id: DRG | use: O | rpt: 1 | seq: 14
        ---
        param_type: DRG.14: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        self._c_data[7] = (drg,)

    @property  # get PROCEDURE
    def procedure(
        self,
    ) -> tuple[BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: BAR_P01_VISIT_GROUP_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P01_VISIT_GROUP_PROCEDURE_GROUP
        """
        return self._c_data[8]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: BAR_P01_VISIT_GROUP_PROCEDURE_GROUP
        | tuple[BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, ...]
        | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BAR_P01_VISIT_GROUP_PROCEDURE_GROUP.None | tuple[BAR_P01_VISIT_GROUP_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P01_VISIT_GROUP_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[8] = procedure
        else:
            self._c_data[8] = (procedure,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[9]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: GT1.17 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[9] = gt1
        else:
            self._c_data[9] = (gt1,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[10]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        param_type: NK1.18 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[10] = nk1
        else:
            self._c_data[10] = (nk1,)

    @property  # get INSURANCE
    def insurance(
        self,
    ) -> tuple[BAR_P01_VISIT_GROUP_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: BAR_P01_VISIT_GROUP_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BAR_P01_VISIT_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P01_VISIT_GROUP_INSURANCE_GROUP
        """
        return self._c_data[11]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: BAR_P01_VISIT_GROUP_INSURANCE_GROUP
        | tuple[BAR_P01_VISIT_GROUP_INSURANCE_GROUP, ...]
        | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BAR_P01_VISIT_GROUP_INSURANCE_GROUP.None | tuple[BAR_P01_VISIT_GROUP_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P01_VISIT_GROUP_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[11] = insurance
        else:
            self._c_data[11] = (insurance,)

    @property  # get ACC.23
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 23
        ---
        return_type: ACC.23: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[12][0]

    @accident.setter  # set ACC.23
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 23
        ---
        param_type: ACC.23: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[12] = (acc,)

    @property  # get UB1.24
    def ub82_data(self) -> UB1 | None:
        """
        id: UB1 | use: O | rpt: 1 | seq: 24
        ---
        return_type: UB1.24: UB82 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1
        """
        return self._c_data[13][0]

    @ub82_data.setter  # set UB1.24
    def ub82_data(self, ub1: UB1 | None):
        """
        id: UB1 | use: O | rpt: 1 | seq: 24
        ---
        param_type: UB1.24: UB82 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB1
        """
        self._c_data[13] = (ub1,)

    @property  # get UB2.25
    def ub92_data(self) -> UB2 | None:
        """
        id: UB2 | use: O | rpt: 1 | seq: 25
        ---
        return_type: UB2.25: UB92 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2
        """
        return self._c_data[14][0]

    @ub92_data.setter  # set UB2.25
    def ub92_data(self, ub2: UB2 | None):
        """
        id: UB2 | use: O | rpt: 1 | seq: 25
        ---
        param_type: UB2.25: UB92 Data
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/UB2
        """
        self._c_data[14] = (ub2,)
