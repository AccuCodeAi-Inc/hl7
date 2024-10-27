from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.RF1 import RF1
from ..segment_groups.REF_I12_INSURANCE_GROUP import REF_I12_INSURANCE_GROUP
from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.SFT import SFT
from ..segment_groups.REF_I12_OBSERVATION_GROUP import REF_I12_OBSERVATION_GROUP
from ..segment_groups.REF_I12_AUTHORIZATION_CONTACT_GROUP import (
    REF_I12_AUTHORIZATION_CONTACT_GROUP,
)
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segment_groups.REF_I12_PATIENT_VISIT_GROUP import REF_I12_PATIENT_VISIT_GROUP
from ..segment_groups.REF_I12_PROVIDER_CONTACT_GROUP import (
    REF_I12_PROVIDER_CONTACT_GROUP,
)
from ..segment_groups.REF_I12_PROCEDURE_GROUP import REF_I12_PROCEDURE_GROUP
from ..segments.NK1 import NK1
from ..segments.DRG import DRG


"""
Patient referral - REF_I12
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::REF_I12 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import REF_I12
from utils.hl7.v2_5_1.segments import (
    DG1, NTE, RF1, DRG, GT1, NK1, AL1, MSH, SFT, PID, ACC
)
from utils.hl7.v2_5_1.segment_groups import (
    REF_I12_OBSERVATION_GROUP, REF_I12_PROVIDER_CONTACT_GROUP, REF_I12_AUTHORIZATION_CONTACT_GROUP, REF_I12_PATIENT_VISIT_GROUP, REF_I12_PROCEDURE_GROUP, REF_I12_INSURANCE_GROUP
)

ref_i12 = REF_I12(  #  - This event triggers a message to be sent from one healthcare provider to another regarding a specific patient
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    referral_information=None,  # RF1(...) 
    authorization_contact=None,  # REF_I12_AUTHORIZATION_CONTACT_GROUP(...) 
    provider_contact=ref_i12_provider_contact_group,  # REF_I12_PROVIDER_CONTACT_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # REF_I12_INSURANCE_GROUP(...) 
    accident=None,  # ACC(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    patient_allergy_information=None,  # AL1(...) 
    procedure=None,  # REF_I12_PROCEDURE_GROUP(...) 
    observation=None,  # REF_I12_OBSERVATION_GROUP(...) 
    patient_visit=None,  # REF_I12_PATIENT_VISIT_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::REF_I12 TEMPLATE-----
"""


class REF_I12(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """REF_I12"""
    _hl7_name = """Patient referral"""
    _hl7_description = """This event triggers a message to be sent from one healthcare provider to another regarding a specific patient"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I12"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 1, 65535, 65535, 65535, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "None", "None", "8", "9", "10", "None", "14", "15", "16", "17", "None", "None", "None", "27")
    _c_components = (MSH, SFT, RF1, REF_I12_AUTHORIZATION_CONTACT_GROUP, REF_I12_PROVIDER_CONTACT_GROUP, PID, NK1, GT1, REF_I12_INSURANCE_GROUP, ACC, DG1, DRG, AL1, REF_I12_PROCEDURE_GROUP, REF_I12_OBSERVATION_GROUP, REF_I12_PATIENT_VISIT_GROUP, NTE)
    _c_name = ("MSH", "SFT", "RF1", "AUTHORIZATION CONTACT", "PROVIDER CONTACT", "PID", "NK1", "GT1", "INSURANCE", "ACC", "DG1", "DRG", "AL1", "PROCEDURE", "OBSERVATION", "PATIENT VISIT", "NTE")
    _c_is_group = (False, False, False, True, True, False, False, False, True, False, False, False, False, True, True, True, False)
    _c_attrs = ("message_header", "software_segment", "referral_information", "authorization_contact", "provider_contact", "patient_identification", "next_of_kin_or_associated_parties", "guarantor", "insurance", "accident", "diagnosis", "diagnosis_related_group", "patient_allergy_information", "procedure", "observation", "patient_visit", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        provider_contact: REF_I12_PROVIDER_CONTACT_GROUP
        | tuple[REF_I12_PROVIDER_CONTACT_GROUP, ...],  #  Required. (PRD.6, CTD.7, ...)
        patient_identification: PID,  #  Required. PID.8
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        referral_information: RF1 | None = None,  #  RF1.3
        authorization_contact: REF_I12_AUTHORIZATION_CONTACT_GROUP
        | None = None,  #  AUT.4, CTD.5
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.9
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.10
        insurance: REF_I12_INSURANCE_GROUP
        | tuple[REF_I12_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.11, IN2.12, IN3.13, ...)
        accident: ACC | None = None,  #  ACC.14
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.15
        diagnosis_related_group: DRG | tuple[DRG, ...] | None = None,  #  DRG.16
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.17
        procedure: REF_I12_PROCEDURE_GROUP
        | tuple[REF_I12_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.18, ...)
        observation: REF_I12_OBSERVATION_GROUP
        | tuple[REF_I12_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBR.21, NTE.22, ...)
        patient_visit: REF_I12_PATIENT_VISIT_GROUP | None = None,  #  PV1.25, PV2.26
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.27
    ):
        """
         - `REF_I12 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/REF_I12>`_
        This event triggers a message to be sent from one healthcare provider to another regarding a specific patient.  The referral message may contain patient demographic information, specific medical procedures to be performed (accompanied by previously obtained authorizations) and relevant clinical information pertinent to the patient’s case.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param referral_information: Referral Information (id: RF1 | seq: 3 | use: O | rpt: 1)
        :param authorization_contact: Authorization Contact segment group: [AUT, CTD|None] (id: AUTHORIZATION CONTACT | seq: 4, 5 | use: O | rpt: 1)
        :param provider_contact: Provider Contact segment group: [PRD, CTD|None] (id: PROVIDER CONTACT | seq: 6, 7 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 8 | use: R | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 9 | use: O | rpt: *)
        :param guarantor: Guarantor (id: GT1 | seq: 10 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 11, 12, 13 | use: O | rpt: *)
        :param accident: Accident (id: ACC | seq: 14 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 15 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 16 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 17 | use: O | rpt: *)
        :param procedure: Procedure segment group: [PR1, AUTHORIZATION CONTACT|None] (id: PROCEDURE | seq: 18, None | use: O | rpt: *)
        :param observation: Observation segment group: [OBR, NTE|None, RESULTS NOTES|None] (id: OBSERVATION | seq: 21, 22, None | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 25, 26 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 27 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 17
        self.message_header = message_header
        self.software_segment = software_segment
        self.referral_information = referral_information
        self.authorization_contact = authorization_contact
        self.provider_contact = provider_contact
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
        self.patient_visit = patient_visit
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

    @property  # get RF1.3
    def referral_information(self) -> RF1 | None:
        """
        id: RF1 | use: O | rpt: 1 | seq: 3
        ---
        return_type: RF1.3: Referral Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RF1
        """
        return self._c_data[2][0]

    @referral_information.setter  # set RF1.3
    def referral_information(self, rf1: RF1 | None):
        """
        id: RF1 | use: O | rpt: 1 | seq: 3
        ---
        param_type: RF1.3: Referral Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RF1
        """
        self._c_data[2] = (rf1,)

    @property  # get REF_I12_AUTHORIZATION_CONTACT_GROUP.None
    def authorization_contact(self) -> REF_I12_AUTHORIZATION_CONTACT_GROUP | None:
        """
        id: REF_I12_AUTHORIZATION_CONTACT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: REF_I12_AUTHORIZATION_CONTACT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_AUTHORIZATION_CONTACT_GROUP
        """
        return self._c_data[3][0]

    @authorization_contact.setter  # set REF_I12_AUTHORIZATION_CONTACT_GROUP.None
    def authorization_contact(
        self, authorization_contact: REF_I12_AUTHORIZATION_CONTACT_GROUP | None
    ):
        """
        id: REF_I12_AUTHORIZATION_CONTACT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: REF_I12_AUTHORIZATION_CONTACT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_AUTHORIZATION_CONTACT_GROUP
        """
        self._c_data[3] = (authorization_contact,)

    @property  # get PROVIDER CONTACT
    def provider_contact(self) -> tuple[REF_I12_PROVIDER_CONTACT_GROUP, ...]:
        """
        id: REF_I12_PROVIDER_CONTACT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[REF_I12_PROVIDER_CONTACT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_PROVIDER_CONTACT_GROUP
        """
        return self._c_data[4]

    @provider_contact.setter  # set PROVIDER CONTACT
    def provider_contact(
        self,
        provider_contact: REF_I12_PROVIDER_CONTACT_GROUP
        | tuple[REF_I12_PROVIDER_CONTACT_GROUP, ...],
    ):
        """
        id: PROVIDER CONTACT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: REF_I12_PROVIDER_CONTACT_GROUP.None | tuple[REF_I12_PROVIDER_CONTACT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_PROVIDER_CONTACT_GROUP
        """
        if isinstance(provider_contact, tuple):
            self._c_data[4] = provider_contact
        else:
            self._c_data[4] = (provider_contact,)

    @property  # get PID.8
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        return_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[5][0]

    @patient_identification.setter  # set PID.8
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        param_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[5] = (pid,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[6]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: NK1.9 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[6] = nk1
        else:
            self._c_data[6] = (nk1,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[7]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: GT1.10 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[7] = gt1
        else:
            self._c_data[7] = (gt1,)

    @property  # get INSURANCE
    def insurance(self) -> tuple[REF_I12_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: REF_I12_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[REF_I12_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_INSURANCE_GROUP
        """
        return self._c_data[8]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: REF_I12_INSURANCE_GROUP | tuple[REF_I12_INSURANCE_GROUP, ...] | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: REF_I12_INSURANCE_GROUP.None | tuple[REF_I12_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[8] = insurance
        else:
            self._c_data[8] = (insurance,)

    @property  # get ACC.14
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 14
        ---
        return_type: ACC.14: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[9][0]

    @accident.setter  # set ACC.14
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 14
        ---
        param_type: ACC.14: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[9] = (acc,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[10]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 15
        ---
        param_type: DG1.15 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[10] = dg1
        else:
            self._c_data[10] = (dg1,)

    @property  # get DRG
    def diagnosis_related_group(self) -> tuple[DRG, ...] | tuple[None]:
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[11]

    @diagnosis_related_group.setter  # set DRG
    def diagnosis_related_group(self, drg: DRG | tuple[DRG, ...] | None):
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: DRG.16 | tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        if isinstance(drg, tuple):
            self._c_data[11] = drg
        else:
            self._c_data[11] = (drg,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[12]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 17
        ---
        param_type: AL1.17 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[12] = al1
        else:
            self._c_data[12] = (al1,)

    @property  # get PROCEDURE
    def procedure(self) -> tuple[REF_I12_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: REF_I12_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[REF_I12_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_PROCEDURE_GROUP
        """
        return self._c_data[13]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: REF_I12_PROCEDURE_GROUP | tuple[REF_I12_PROCEDURE_GROUP, ...] | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: REF_I12_PROCEDURE_GROUP.None | tuple[REF_I12_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[13] = procedure
        else:
            self._c_data[13] = (procedure,)

    @property  # get OBSERVATION
    def observation(self) -> tuple[REF_I12_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: REF_I12_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[REF_I12_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_OBSERVATION_GROUP
        """
        return self._c_data[14]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: REF_I12_OBSERVATION_GROUP
        | tuple[REF_I12_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: REF_I12_OBSERVATION_GROUP.None | tuple[REF_I12_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[14] = observation
        else:
            self._c_data[14] = (observation,)

    @property  # get REF_I12_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> REF_I12_PATIENT_VISIT_GROUP | None:
        """
        id: REF_I12_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: REF_I12_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_PATIENT_VISIT_GROUP
        """
        return self._c_data[15][0]

    @patient_visit.setter  # set REF_I12_PATIENT_VISIT_GROUP.None
    def patient_visit(self, patient_v_isit: REF_I12_PATIENT_VISIT_GROUP | None):
        """
        id: REF_I12_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: REF_I12_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/REF_I12_PATIENT_VISIT_GROUP
        """
        self._c_data[15] = (patient_v_isit,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[16]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 27
        ---
        param_type: NTE.27 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[16] = nte
        else:
            self._c_data[16] = (nte,)
