from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segment_groups.BAR_P12_PROCEDURE_GROUP import BAR_P12_PROCEDURE_GROUP
from ..segments.PID import PID
from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.DRG import DRG


"""
Update Diagnosis/Procedure - BAR_P12
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::BAR_P12 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P12
from utils.hl7.v2_5_1.segments import (
    PID, MSH, PV1, DG1, SFT, DRG, EVN
)
from utils.hl7.v2_5_1.segment_groups import (
    BAR_P12_PROCEDURE_GROUP
)

bar_p12 = BAR_P12(  #  - The P12 event is used to communicate diagnosis and/or procedures in update mode
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=pv1,  # PV1(...)  # Required.
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    procedure=None,  # BAR_P12_PROCEDURE_GROUP(...) 
)

-----END TRIGGER_EVENT::BAR_P12 TEMPLATE-----
"""


class BAR_P12(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """BAR_P12"""
    _hl7_name = """Update Diagnosis/Procedure"""
    _hl7_description = """The P12 event is used to communicate diagnosis and/or procedures in update mode"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P12"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "R", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "None")
    _c_components = (MSH, SFT, EVN, PID, PV1, DG1, DRG, BAR_P12_PROCEDURE_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PV1", "DG1", "DRG", "PROCEDURE")
    _c_is_group = (False, False, False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_visit", "diagnosis", "diagnosis_related_group", "procedure",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.5
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.6
        diagnosis_related_group: DRG | None = None,  #  DRG.7
        procedure: BAR_P12_PROCEDURE_GROUP
        | tuple[BAR_P12_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.8, ROL.9, ...)
    ):
        """
         - `BAR_P12 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P12>`_
        The P12 event is used to communicate diagnosis and/or procedures in update mode.  The newly created fields in DG1 and PR1, i.e. identifiers and action codes, must be populated to indicate which change should be applied.  When other patient or visit related fields change, use the A08 (update patient information) event.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 5 | use: R | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 6 | use: O | rpt: *)
        :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 7 | use: O | rpt: 1)
        :param procedure: Procedure segment group: [PR1, ROL|None] (id: PROCEDURE | seq: 8, 9 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.procedure = procedure

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

    @property  # get PV1.5
    def patient_visit(self) -> PV1:
        """
        id: PV1 | use: R | rpt: 1 | seq: 5
        ---
        return_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[4][0]

    @patient_visit.setter  # set PV1.5
    def patient_visit(self, pv1: PV1):
        """
        id: PV1 | use: R | rpt: 1 | seq: 5
        ---
        param_type: PV1.5: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[4] = (pv1,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[5]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: DG1.6 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[5] = dg1
        else:
            self._c_data[5] = (dg1,)

    @property  # get DRG.7
    def diagnosis_related_group(self) -> DRG | None:
        """
        id: DRG | use: O | rpt: 1 | seq: 7
        ---
        return_type: DRG.7: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[6][0]

    @diagnosis_related_group.setter  # set DRG.7
    def diagnosis_related_group(self, drg: DRG | None):
        """
        id: DRG | use: O | rpt: 1 | seq: 7
        ---
        param_type: DRG.7: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        self._c_data[6] = (drg,)

    @property  # get PROCEDURE
    def procedure(self) -> tuple[BAR_P12_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: BAR_P12_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BAR_P12_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P12_PROCEDURE_GROUP
        """
        return self._c_data[7]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: BAR_P12_PROCEDURE_GROUP | tuple[BAR_P12_PROCEDURE_GROUP, ...] | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BAR_P12_PROCEDURE_GROUP.None | tuple[BAR_P12_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P12_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[7] = procedure
        else:
            self._c_data[7] = (procedure,)
