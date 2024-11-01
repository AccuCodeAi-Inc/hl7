from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.NTE import NTE
from ..segment_groups.RPA_I10_VISIT_GROUP import RPA_I10_VISIT_GROUP
from ..segments.ACC import ACC
from ..segments.NK1 import NK1
from ..segment_groups.RPA_I10_PROCEDURE_GROUP import RPA_I10_PROCEDURE_GROUP
from ..segments.MSH import MSH
from ..segment_groups.RPA_I10_AUTHORIZATION_GROUP import RPA_I10_AUTHORIZATION_GROUP
from ..segment_groups.RPA_I10_INSURANCE_GROUP import RPA_I10_INSURANCE_GROUP
from ..segments.AL1 import AL1
from ..segment_groups.RPA_I10_OBSERVATION_GROUP import RPA_I10_OBSERVATION_GROUP
from ..segments.MSA import MSA
from ..segments.RF1 import RF1
from ..segments.GT1 import GT1
from ..segments.DRG import DRG
from ..segments.PID import PID
from ..segment_groups.RPA_I10_PROVIDER_GROUP import RPA_I10_PROVIDER_GROUP
from ..segments.DG1 import DG1
from ..segments.SFT import SFT


"""
Request for resubmission of an authorization acknowledgement - RPA_I10
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RPA_I10 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RPA_I10
from utils.hl7.v2_5_1.segments import (
    NK1, DG1, ACC, AL1, NTE, PID, SFT, MSH, MSA, RF1, DRG, GT1
)
from utils.hl7.v2_5_1.segment_groups import (
    RPA_I10_PROCEDURE_GROUP, RPA_I10_PROVIDER_GROUP, RPA_I10_AUTHORIZATION_GROUP, RPA_I10_INSURANCE_GROUP, RPA_I10_VISIT_GROUP, RPA_I10_OBSERVATION_GROUP
)

rpa_i10 = RPA_I10(  #  - If a previously submitted request for treatment authorization is rejected or canceled, this event could trigger a resubmission message for a referenced authorization
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    referral_information=None,  # RF1(...) 
    authorization=None,  # RPA_I10_AUTHORIZATION_GROUP(...) 
    provider=rpa_i10_provider_group,  # RPA_I10_PROVIDER_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # RPA_I10_INSURANCE_GROUP(...) 
    accident=None,  # ACC(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    patient_allergy_information=None,  # AL1(...) 
    procedure=rpa_i10_procedure_group,  # RPA_I10_PROCEDURE_GROUP(...)  # Required.
    observation=None,  # RPA_I10_OBSERVATION_GROUP(...) 
    visit=None,  # RPA_I10_VISIT_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::RPA_I10 TEMPLATE-----
"""


class RPA_I10(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RPA_I10"""
    _hl7_name = """Request for resubmission of an authorization acknowledgement"""
    _hl7_description = """If a previously submitted request for treatment authorization is rejected or canceled, this event could trigger a resubmission message for a referenced authorization"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPA_I10"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "R", "R", "O", "O", "O", "O", "O", "O", "O", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "None", "None", "9", "10", "11", "None", "15", "16", "17", "18", "None", "None", "None", "28")
    _c_components = (MSH, SFT, MSA, RF1, RPA_I10_AUTHORIZATION_GROUP, RPA_I10_PROVIDER_GROUP, PID, NK1, GT1, RPA_I10_INSURANCE_GROUP, ACC, DG1, DRG, AL1, RPA_I10_PROCEDURE_GROUP, RPA_I10_OBSERVATION_GROUP, RPA_I10_VISIT_GROUP, NTE)
    _c_name = ("MSH", "SFT", "MSA", "RF1", "AUTHORIZATION", "PROVIDER", "PID", "NK1", "GT1", "INSURANCE", "ACC", "DG1", "DRG", "AL1", "PROCEDURE", "OBSERVATION", "VISIT", "NTE")
    _c_is_group = (False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "referral_information", "authorization", "provider", "patient_identification", "next_of_kin_or_associated_parties", "guarantor", "insurance", "accident", "diagnosis", "diagnosis_related_group", "patient_allergy_information", "procedure", "observation", "visit", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        provider: RPA_I10_PROVIDER_GROUP
        | tuple[RPA_I10_PROVIDER_GROUP, ...],  #  Required. (PRD.7, CTD.8, ...)
        patient_identification: PID,  #  Required. PID.9
        procedure: RPA_I10_PROCEDURE_GROUP
        | tuple[RPA_I10_PROCEDURE_GROUP, ...],  #  Required. (PR1.19, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        referral_information: RF1 | None = None,  #  RF1.4
        authorization: RPA_I10_AUTHORIZATION_GROUP | None = None,  #  AUT.5, CTD.6
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.10
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.11
        insurance: RPA_I10_INSURANCE_GROUP
        | tuple[RPA_I10_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.12, IN2.13, IN3.14, ...)
        accident: ACC | None = None,  #  ACC.15
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.16
        diagnosis_related_group: DRG | tuple[DRG, ...] | None = None,  #  DRG.17
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.18
        observation: RPA_I10_OBSERVATION_GROUP
        | tuple[RPA_I10_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBR.22, NTE.23, ...)
        visit: RPA_I10_VISIT_GROUP | None = None,  #  PV1.26, PV2.27
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.28
    ):
        """
         - `RPA_I10 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RPA_I10>`_
        If a previously submitted request for treatment authorization is rejected or canceled, this event could trigger a resubmission message for a referenced authorization.  For example, the payor may have rejected a request until additional clinical information is sent to support the authorization request.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param referral_information: Referral Information (id: RF1 | seq: 4 | use: O | rpt: 1)
        :param authorization: Authorization segment group: [AUT, CTD|None] (id: AUTHORIZATION | seq: 5, 6 | use: O | rpt: 1)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 7, 8 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 9 | use: R | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 10 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 11 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 12, 13, 14 | use: O | rpt: *)
        :param accident: Accident (id: ACC | seq: 15 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 16 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 17 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 18 | use: O | rpt: *)
        :param procedure: Procedure segment group: [PR1, AUTHORIZATION|None] (id: PROCEDURE | seq: 19, None | use: R | rpt: *)
        :param observation: Observation segment group: [OBR, NTE|None, RESULTS|None] (id: OBSERVATION | seq: 22, 23, None | use: O | rpt: *)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 26, 27 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 28 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 18
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.referral_information = referral_information
        self.authorization = authorization
        self.provider = provider
        self.patient_identification = patient_identification
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.guarantor = guarantor
        self.insurance = insurance
        self.accident = accident
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.patient_allergy_information = patient_allergy_information
        self.procedure = procedure
        self.observation = observation
        self.visit = visit
        self.notes_and_comments = notes_and_comments

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

    @property  # get MSA.3
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 3
        ---
        param_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[2] = (msa,)

    @property  # get RF1.4
    def referral_information(self) -> RF1 | None:
        """
        id: RF1 | use: O | rpt: 1 | seq: 4
        ---
        return_type: RF1.4: Referral Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RF1
        """
        return self._c_data[3][0]

    @referral_information.setter  # set RF1.4
    def referral_information(self, rf1: RF1 | None):
        """
        id: RF1 | use: O | rpt: 1 | seq: 4
        ---
        param_type: RF1.4: Referral Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RF1
        """
        self._c_data[3] = (rf1,)

    @property  # get RPA_I10_AUTHORIZATION_GROUP.None
    def authorization(self) -> RPA_I10_AUTHORIZATION_GROUP | None:
        """
        id: RPA_I10_AUTHORIZATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RPA_I10_AUTHORIZATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_AUTHORIZATION_GROUP
        """
        return self._c_data[4][0]

    @authorization.setter  # set RPA_I10_AUTHORIZATION_GROUP.None
    def authorization(self, authorization: RPA_I10_AUTHORIZATION_GROUP | None):
        """
        id: RPA_I10_AUTHORIZATION_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RPA_I10_AUTHORIZATION_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_AUTHORIZATION_GROUP
        """
        self._c_data[4] = (authorization,)

    @property  # get PROVIDER
    def provider(self) -> tuple[RPA_I10_PROVIDER_GROUP, ...]:
        """
        id: RPA_I10_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RPA_I10_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_PROVIDER_GROUP
        """
        return self._c_data[5]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: RPA_I10_PROVIDER_GROUP | tuple[RPA_I10_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RPA_I10_PROVIDER_GROUP.None | tuple[RPA_I10_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[5] = provider
        else:
            self._c_data[5] = (provider,)

    @property  # get PID.9
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 9
        ---
        return_type: PID.9: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[6][0]

    @patient_identification.setter  # set PID.9
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 9
        ---
        param_type: PID.9: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[6] = (pid,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[7]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: NK1.10 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[7] = nk1
        else:
            self._c_data[7] = (nk1,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[8]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: GT1.11 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[8] = gt1
        else:
            self._c_data[8] = (gt1,)

    @property  # get INSURANCE
    def insurance(self) -> tuple[RPA_I10_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: RPA_I10_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RPA_I10_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_INSURANCE_GROUP
        """
        return self._c_data[9]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: RPA_I10_INSURANCE_GROUP | tuple[RPA_I10_INSURANCE_GROUP, ...] | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RPA_I10_INSURANCE_GROUP.None | tuple[RPA_I10_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[9] = insurance
        else:
            self._c_data[9] = (insurance,)

    @property  # get ACC.15
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 15
        ---
        return_type: ACC.15: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[10][0]

    @accident.setter  # set ACC.15
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 15
        ---
        param_type: ACC.15: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[10] = (acc,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[11]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: DG1.16 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[11] = dg1
        else:
            self._c_data[11] = (dg1,)

    @property  # get DRG
    def diagnosis_related_group(self) -> tuple[DRG, ...] | tuple[None]:
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[12]

    @diagnosis_related_group.setter  # set DRG
    def diagnosis_related_group(self, drg: DRG | tuple[DRG, ...] | None):
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: DRG.17 | tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        if isinstance(drg, tuple):
            self._c_data[12] = drg
        else:
            self._c_data[12] = (drg,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 18
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[13]

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
            self._c_data[13] = al1
        else:
            self._c_data[13] = (al1,)

    @property  # get PROCEDURE
    def procedure(self) -> tuple[RPA_I10_PROCEDURE_GROUP, ...]:
        """
        id: RPA_I10_PROCEDURE_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RPA_I10_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_PROCEDURE_GROUP
        """
        return self._c_data[14]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self, procedure: RPA_I10_PROCEDURE_GROUP | tuple[RPA_I10_PROCEDURE_GROUP, ...]
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RPA_I10_PROCEDURE_GROUP.None | tuple[RPA_I10_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[14] = procedure
        else:
            self._c_data[14] = (procedure,)

    @property  # get OBSERVATION
    def observation(self) -> tuple[RPA_I10_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: RPA_I10_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RPA_I10_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_OBSERVATION_GROUP
        """
        return self._c_data[15]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RPA_I10_OBSERVATION_GROUP
        | tuple[RPA_I10_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RPA_I10_OBSERVATION_GROUP.None | tuple[RPA_I10_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[15] = observation
        else:
            self._c_data[15] = (observation,)

    @property  # get RPA_I10_VISIT_GROUP.None
    def visit(self) -> RPA_I10_VISIT_GROUP | None:
        """
        id: RPA_I10_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RPA_I10_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_VISIT_GROUP
        """
        return self._c_data[16][0]

    @visit.setter  # set RPA_I10_VISIT_GROUP.None
    def visit(self, v_isit: RPA_I10_VISIT_GROUP | None):
        """
        id: RPA_I10_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RPA_I10_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RPA_I10_VISIT_GROUP
        """
        self._c_data[16] = (v_isit,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 28
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[17]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 28
        ---
        param_type: NTE.28 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[17] = nte
        else:
            self._c_data[17] = (nte,)
