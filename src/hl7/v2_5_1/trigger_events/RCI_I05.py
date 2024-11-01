from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.NTE import NTE
from ..segment_groups.RCI_I05_PROVIDER_GROUP import RCI_I05_PROVIDER_GROUP
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.AL1 import AL1
from ..segments.MSA import MSA
from ..segments.QRF import QRF
from ..segment_groups.RCI_I05_OBSERVATION_GROUP import RCI_I05_OBSERVATION_GROUP
from ..segments.DRG import DRG
from ..segments.PID import PID
from ..segments.DG1 import DG1
from ..segments.SFT import SFT


"""
Request for patient clinical information acknowledgement - RCI_I05
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::RCI_I05 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import RCI_I05
from utils.hl7.v2_5_1.segments import (
    DG1, QRD, AL1, NTE, PID, SFT, QRF, MSA, MSH, DRG
)
from utils.hl7.v2_5_1.segment_groups import (
    RCI_I05_PROVIDER_GROUP, RCI_I05_OBSERVATION_GROUP
)

rci_i05 = RCI_I05(  #  - This event is used to request clinical information for a specific patient
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    provider=rci_i05_provider_group,  # RCI_I05_PROVIDER_GROUP(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    patient_allergy_information=None,  # AL1(...) 
    observation=None,  # RCI_I05_OBSERVATION_GROUP(...) 
    notes_and_comments=None,  # NTE(...) 
)

-----END TRIGGER_EVENT::RCI_I05 TEMPLATE-----
"""


class RCI_I05(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """RCI_I05"""
    _hl7_name = """Request for patient clinical information acknowledgement"""
    _hl7_description = """This event is used to request clinical information for a specific patient"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RCI_I05"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 65535, 65535, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "R", "O", "R", "R", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "None", "8", "9", "10", "11", "None", "16")
    _c_components = (MSH, SFT, MSA, QRD, QRF, RCI_I05_PROVIDER_GROUP, PID, DG1, DRG, AL1, RCI_I05_OBSERVATION_GROUP, NTE)
    _c_name = ("MSH", "SFT", "MSA", "QRD", "QRF", "PROVIDER", "PID", "DG1", "DRG", "AL1", "OBSERVATION", "NTE")
    _c_is_group = (False, False, False, False, False, True, False, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "original_style_query_definition", "original_style_query_filter", "provider", "patient_identification", "diagnosis", "diagnosis_related_group", "patient_allergy_information", "observation", "notes_and_comments",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        original_style_query_definition: QRD,  #  Required. QRD.4
        provider: RCI_I05_PROVIDER_GROUP
        | tuple[RCI_I05_PROVIDER_GROUP, ...],  #  Required. (PRD.6, CTD.7, ...)
        patient_identification: PID,  #  Required. PID.8
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        original_style_query_filter: QRF | None = None,  #  QRF.5
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.9
        diagnosis_related_group: DRG | tuple[DRG, ...] | None = None,  #  DRG.10
        patient_allergy_information: AL1 | tuple[AL1, ...] | None = None,  #  AL1.11
        observation: RCI_I05_OBSERVATION_GROUP
        | tuple[RCI_I05_OBSERVATION_GROUP, ...]
        | None = None,  #  (OBR.12, NTE.13, ...)
        notes_and_comments: NTE | tuple[NTE, ...] | None = None,  #  NTE.16
    ):
        """
         - `RCI_I05 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/RCI_I05>`_
        This event is used to request clinical information for a specific patient.  Generally, this transaction occurs between one provider and another (typically a laboratory or radiology, etc.).  However, it may also be very useful for a payor-to-provider request for clinical observation information to be used in considering a request for treatment authorization.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 4 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 5 | use: O | rpt: 1)
        :param provider: Provider segment group: [PRD, CTD|None] (id: PROVIDER | seq: 6, 7 | use: R | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 8 | use: R | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 9 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 10 | use: O | rpt: *)
        :param patient_allergy_information: Patient Allergy Information (id: AL1 | seq: 11 | use: O | rpt: *)
        :param observation: Observation segment group: [OBR, NTE|None, RESULTS|None] (id: OBSERVATION | seq: 12, 13, None | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 16 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.provider = provider
        self.patient_identification = patient_identification
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.patient_allergy_information = patient_allergy_information
        self.observation = observation
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

    @property  # get QRD.4
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 4
        ---
        return_type: QRD.4: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[3][0]

    @original_style_query_definition.setter  # set QRD.4
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 4
        ---
        param_type: QRD.4: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[3] = (qrd,)

    @property  # get QRF.5
    def original_style_query_filter(self) -> QRF | None:
        """
        id: QRF | use: O | rpt: 1 | seq: 5
        ---
        return_type: QRF.5: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        return self._c_data[4][0]

    @original_style_query_filter.setter  # set QRF.5
    def original_style_query_filter(self, qrf: QRF | None):
        """
        id: QRF | use: O | rpt: 1 | seq: 5
        ---
        param_type: QRF.5: Original style query filter
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRF
        """
        self._c_data[4] = (qrf,)

    @property  # get PROVIDER
    def provider(self) -> tuple[RCI_I05_PROVIDER_GROUP, ...]:
        """
        id: RCI_I05_PROVIDER_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[RCI_I05_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCI_I05_PROVIDER_GROUP
        """
        return self._c_data[5]

    @provider.setter  # set PROVIDER
    def provider(
        self, provider: RCI_I05_PROVIDER_GROUP | tuple[RCI_I05_PROVIDER_GROUP, ...]
    ):
        """
        id: PROVIDER SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: RCI_I05_PROVIDER_GROUP.None | tuple[RCI_I05_PROVIDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCI_I05_PROVIDER_GROUP
        """
        if isinstance(provider, tuple):
            self._c_data[5] = provider
        else:
            self._c_data[5] = (provider,)

    @property  # get PID.8
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        return_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[6][0]

    @patient_identification.setter  # set PID.8
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 8
        ---
        param_type: PID.8: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[6] = (pid,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[7]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: DG1.9 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[7] = dg1
        else:
            self._c_data[7] = (dg1,)

    @property  # get DRG
    def diagnosis_related_group(self) -> tuple[DRG, ...] | tuple[None]:
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[8]

    @diagnosis_related_group.setter  # set DRG
    def diagnosis_related_group(self, drg: DRG | tuple[DRG, ...] | None):
        """
        id: DRG SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: DRG.10 | tuple[DRG, ...]: (Diagnosis Related Group, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        if isinstance(drg, tuple):
            self._c_data[8] = drg
        else:
            self._c_data[8] = (drg,)

    @property  # get AL1
    def patient_allergy_information(self) -> tuple[AL1, ...] | tuple[None]:
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        return self._c_data[9]

    @patient_allergy_information.setter  # set AL1
    def patient_allergy_information(self, al1: AL1 | tuple[AL1, ...] | None):
        """
        id: AL1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: AL1.11 | tuple[AL1, ...]: (Patient Allergy Information, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/AL1
        """
        if isinstance(al1, tuple):
            self._c_data[9] = al1
        else:
            self._c_data[9] = (al1,)

    @property  # get OBSERVATION
    def observation(self) -> tuple[RCI_I05_OBSERVATION_GROUP, ...] | tuple[None]:
        """
        id: RCI_I05_OBSERVATION_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[RCI_I05_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCI_I05_OBSERVATION_GROUP
        """
        return self._c_data[10]

    @observation.setter  # set OBSERVATION
    def observation(
        self,
        observation: RCI_I05_OBSERVATION_GROUP
        | tuple[RCI_I05_OBSERVATION_GROUP, ...]
        | None,
    ):
        """
        id: OBSERVATION SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: RCI_I05_OBSERVATION_GROUP.None | tuple[RCI_I05_OBSERVATION_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/RCI_I05_OBSERVATION_GROUP
        """
        if isinstance(observation, tuple):
            self._c_data[10] = observation
        else:
            self._c_data[10] = (observation,)

    @property  # get NTE
    def notes_and_comments(self) -> tuple[NTE, ...] | tuple[None]:
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        return_type: tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[11]

    @notes_and_comments.setter  # set NTE
    def notes_and_comments(self, nte: NTE | tuple[NTE, ...] | None):
        """
        id: NTE SEGMENT GROUP | use: O | rpt: * | seq: 16
        ---
        param_type: NTE.16 | tuple[NTE, ...]: (Notes and Comments, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        if isinstance(nte, tuple):
            self._c_data[11] = nte
        else:
            self._c_data[11] = (nte,)
