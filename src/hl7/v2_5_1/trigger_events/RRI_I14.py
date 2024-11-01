from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.RF1 import RF1
from ..segment_groups.RRI_I14_PROVIDER_CONTACT_GROUP import (
    RRI_I14_PROVIDER_CONTACT_GROUP,
)
from ..segments.ACC import ACC
from ..segments.DG1 import DG1
from ..segments.NTE import NTE
from ..segments.DRG import DRG
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segment_groups.RRI_I14_PROCEDURE_GROUP import RRI_I14_PROCEDURE_GROUP
from ..segment_groups.RRI_I14_PATIENT_VISIT_GROUP import RRI_I14_PATIENT_VISIT_GROUP
from ..segment_groups.RRI_I14_OBSERVATION_GROUP import RRI_I14_OBSERVATION_GROUP
from ..segment_groups.RRI_I14_AUTHORIZATION_CONTACT_GROUP import (
    RRI_I14_AUTHORIZATION_CONTACT_GROUP,
)
from ..segments.AL1 import AL1


"""
Cancel patient referral acknowledgement - RRI_I14
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RRI_I14 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RRI_I14
from utils.hl7.v2_5_1.segments import (
    RF1, NTE, MSA, SFT, ACC, DG1, PID, AL1, MSH, DRG
)
from utils.hl7.v2_5_1.segment_groups import (
    RRI_I14_PATIENT_VISIT_GROUP, RRI_I14_AUTHORIZATION_CONTACT_GROUP, RRI_I14_OBSERVATION_GROUP, RRI_I14_PROVIDER_CONTACT_GROUP, RRI_I14_PROCEDURE_GROUP
)

rri_i14 = RRI_I14(  #  - This event triggers a message to be sent from one healthcare provider to another canceling a referral
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=None,  # MSA(...) 
    referral_information=None,  # RF1(...) 
    authorization_contact=None,  # RRI_I14_AUTHORIZATION_CONTACT_GROUP(...) 
    provider_contact=rri_i14_provider_contact_group,  # RRI_I14_PROVIDER_CONTACT_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    accident=None,  # ACC(...) 
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    patient_allergy_information=None,  # AL1(...) 
    procedure=None,  # RRI_I14_PROCEDURE_GROUP(...) 
    observation=None,  # RRI_I14_OBSERVATION_GROUP(...) 
    patient_visit=None,  # RRI_I14_PATIENT_VISIT_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::RRI_I14 TEMPLATE-----
"""


class RRI_I14(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RRI_I14"""
    _hl7_name = """Cancel patient referral acknowledgement"""
    _hl7_description = """This event triggers a message to be sent from one healthcare provider to another canceling a referral"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I14"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535)
    _c_usage = ("R", "O", "O", "O", "O", "R", "R", "O", "O", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "None", "None", "9", "10", "11", "12", "13", "None", "None", "None", "23")
    _c_components = (MSH, SFT, MSA, RF1, RRI_I14_AUTHORIZATION_CONTACT_GROUP, RRI_I14_PROVIDER_CONTACT_GROUP, PID, ACC, DG1, DRG, AL1, RRI_I14_PROCEDURE_GROUP, RRI_I14_OBSERVATION_GROUP, RRI_I14_PATIENT_VISIT_GROUP, NTE)
    _c_name = ("MSH", "SFT", "MSA", "RF1", "AUTHORIZATION CONTACT", "PROVIDER CONTACT", "PID", "ACC", "DG1", "DRG", "AL1", "PROCEDURE", "OBSERVATION", "PATIENT VISIT", "NTE")
    _c_is_group = (False, False, False, False, True, True, False, False, False, False, False, True, True, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "referral_information", "authorization_contact", "provider_contact", "patient_identification", "accident", "diagnosis", "diagnosis_related_group", "patient_allergy_information", "procedure", "observation", "patient_visit", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        provider_contact: RRI_I14_PROVIDER_CONTACT_GROUP
        | tuple[RRI_I14_PROVIDER_CONTACT_GROUP, ...],  #  Required. (PRD.7, CTD.8, ...)
        patient_identification: PID,  #  Required. PID.9
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        message_acknowledgment: MSA | None = None,  #  MSA.3
        referral_information: RF1 | None = None,  #  RF1.4
        authorization_contact: RRI_I14_AUTHORIZATION_CONTACT_GROUP
        | None = None,  #  AUT.5, CTD.6
        accident: ACC | None = None,  #  ACC.10
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.11
        diagnosis_related_group: DRG | tuple[DRG, ...] | None = None,  #  DRG.12
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.13
        procedure: RRI_I14_PROCEDURE_GROUP
        | tuple[RRI_I14_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.14, ...)
        observation: RRI_I14_OBSERVATION_GROUP
        | tuple[RRI_I14_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBR.17, NTE.18, ...)
        patient_visit: RRI_I14_PATIENT_VISIT_GROUP | None = None,  #  PV1.21, PV2.22
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.23
    ):
        """
         - `RRI_I14 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RRI_I14>`_
        This event triggers a message to be sent from one healthcare provider to another canceling a referral.  A previous referral may have been made in error, or perhaps the cancellation has come from the patient.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: O | rpt: 1)
        :param referral_information: Referral Information (id: RF1 | seq: 4 | use: O | rpt: 1)
        :param authorization_contact: Authorization Contact segment group: [AUT, CTD|None] (id: AUTHORIZATION CONTACT | seq: 5, 6 | use: O | rpt: 1)
        :param provider_contact: Provider Contact segment group: [PRD, CTD|None] (id: PROVIDER CONTACT | seq: 7, 8 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 9 | use: R | rpt: 1)
        :param accident: Accident (id: ACC | seq: 10 | use: O | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 11 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 12 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 13 | use: O | rpt: *)
        :param procedure: Procedure segment group: [PR1, AUTHORIZATION CONTACT|None] (id: PROCEDURE | seq: 14, None | use: O | rpt: *)
        :param observation: Observation segment group: [OBR, NTE|None, RESULTS NOTES|None] (id: OBSERVATION | seq: 17, 18, None | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 21, 22 | use: O | rpt: 1)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 23 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 15
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.referral_information = referral_information
        self.authorization_contact = authorization_contact
        self.provider_contact = provider_contact
        self.patient_identification = patient_identification
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

    @property  # get MSA.3
    def message_acknowledgment(self) -> MSA | None:
        """
        id: MSA | use: O | rpt: 1 | seq: 3
        ---
        return_type: MSA.3: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[2][0]

    @message_acknowledgment.setter  # set MSA.3
    def message_acknowledgment(self, msa: MSA | None):
        """
        id: MSA | use: O | rpt: 1 | seq: 3
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

    @property  # get RRI_I14_AUTHORIZATION_CONTACT_GROUP.None
    def authorization_contact(self) -> RRI_I14_AUTHORIZATION_CONTACT_GROUP | None:
        """
        id: RRI_I14_AUTHORIZATION_CONTACT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRI_I14_AUTHORIZATION_CONTACT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_AUTHORIZATION_CONTACT_GROUP
        """
        return self._c_data[4][0]

    @authorization_contact.setter  # set RRI_I14_AUTHORIZATION_CONTACT_GROUP.None
    def authorization_contact(
        self, authorization_contact: RRI_I14_AUTHORIZATION_CONTACT_GROUP | None
    ):
        """
        id: RRI_I14_AUTHORIZATION_CONTACT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRI_I14_AUTHORIZATION_CONTACT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_AUTHORIZATION_CONTACT_GROUP
        """
        self._c_data[4] = (authorization_contact,)

    @property  # get PROVIDER CONTACT
    def provider_contact(self) -> tuple[RRI_I14_PROVIDER_CONTACT_GROUP, ...]:
        """
        id: RRI_I14_PROVIDER_CONTACT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RRI_I14_PROVIDER_CONTACT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_PROVIDER_CONTACT_GROUP
        """
        return self._c_data[5]

    @provider_contact.setter  # set PROVIDER CONTACT
    def provider_contact(
        self,
        provider_contact: RRI_I14_PROVIDER_CONTACT_GROUP
        | tuple[RRI_I14_PROVIDER_CONTACT_GROUP, ...],
    ):
        """
        id: PROVIDER CONTACT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RRI_I14_PROVIDER_CONTACT_GROUP.None | tuple[RRI_I14_PROVIDER_CONTACT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_PROVIDER_CONTACT_GROUP
        """
        if isinstance(provider_contact, tuple):
            self._c_data[5] = provider_contact
        else:
            self._c_data[5] = (provider_contact,)

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

    @property  # get ACC.10
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 10
        ---
        return_type: ACC.10: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[7][0]

    @accident.setter  # set ACC.10
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 10
        ---
        param_type: ACC.10: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[7] = (acc,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[8]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: DG1.11 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[8] = dg1
        else:
            self._c_data[8] = (dg1,)

    @property  # get DRG
    def diagnosis_related_group(self) -> tuple[DRG, ...] | tuple[None]:
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        return_type: tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[9]

    @diagnosis_related_group.setter  # set DRG
    def diagnosis_related_group(self, drg: DRG | tuple[DRG, ...] | None):
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 12
        ---
        param_type: DRG.12 | tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        if isinstance(drg, tuple):
            self._c_data[9] = drg
        else:
            self._c_data[9] = (drg,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 13
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[10]

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
            self._c_data[10] = al1
        else:
            self._c_data[10] = (al1,)

    @property  # get PROCEDURE
    def procedure(self) -> tuple[RRI_I14_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: RRI_I14_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RRI_I14_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_PROCEDURE_GROUP
        """
        return self._c_data[11]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: RRI_I14_PROCEDURE_GROUP | tuple[RRI_I14_PROCEDURE_GROUP, ...] | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RRI_I14_PROCEDURE_GROUP.None | tuple[RRI_I14_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[11] = procedure
        else:
            self._c_data[11] = (procedure,)

    @property  # get OBSERVATION
    def observation(self) -> tuple[RRI_I14_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: RRI_I14_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RRI_I14_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_OBSERVATION_GROUP
        """
        return self._c_data[12]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RRI_I14_OBSERVATION_GROUP
        | tuple[RRI_I14_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RRI_I14_OBSERVATION_GROUP.None | tuple[RRI_I14_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[12] = observation
        else:
            self._c_data[12] = (observation,)

    @property  # get RRI_I14_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> RRI_I14_PATIENT_VISIT_GROUP | None:
        """
        id: RRI_I14_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: RRI_I14_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_PATIENT_VISIT_GROUP
        """
        return self._c_data[13][0]

    @patient_visit.setter  # set RRI_I14_PATIENT_VISIT_GROUP.None
    def patient_visit(self, patient_v_isit: RRI_I14_PATIENT_VISIT_GROUP | None):
        """
        id: RRI_I14_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: RRI_I14_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RRI_I14_PATIENT_VISIT_GROUP
        """
        self._c_data[13] = (patient_v_isit,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[14]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 23
        ---
        param_type: NTE.23 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[14] = nte
        else:
            self._c_data[14] = (nte,)
