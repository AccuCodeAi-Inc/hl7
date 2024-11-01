from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segment_groups.BAR_P10_PROCEDURE_GROUP import BAR_P10_PROCEDURE_GROUP
from ..segments.DG1 import DG1
from ..segments.GP1 import GP1
from ..segments.EVN import EVN
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH
from ..segments.PV1 import PV1


"""
Transmit Ambulatory Payment Classification (APC) Groups - BAR_P10
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::BAR_P10 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import BAR_P10
from utils.hl7.v2_5_1.segments import (
    PV1, EVN, GP1, SFT, DG1, PID, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    BAR_P10_PROCEDURE_GROUP
)

bar_p10 = BAR_P10(  #  - The P10 event is used to communicate Ambulatory Payment Classification (APC) grouping
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_visit=pv1,  # PV1(...)  # Required.
    diagnosis=None,  # DG1(...) 
    grouping_or_reimbursement_visit=gp1,  # GP1(...)  # Required.
    procedure=None,  # BAR_P10_PROCEDURE_GROUP(...) 
)

-----END TRIGGER_EVENT::BAR_P10 TEMPLATE-----
"""


class BAR_P10(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """BAR_P10"""
    _hl7_name = """Transmit Ambulatory Payment Classification (APC) Groups"""
    _hl7_description = """The P10 event is used to communicate Ambulatory Payment Classification (APC) grouping"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P10"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 65535)
    _c_usage = ("R", "O", "R", "R", "R", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "None")
    _c_components = (MSH, SFT, EVN, PID, PV1, DG1, GP1, BAR_P10_PROCEDURE_GROUP)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PV1", "DG1", "GP1", "PROCEDURE")
    _c_is_group = (False, False, False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_visit", "diagnosis", "grouping_or_reimbursement_visit", "procedure",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        patient_visit: PV1,  #  Required. PV1.5
        grouping_or_reimbursement_visit: GP1,  #  Required. GP1.7
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.6
        procedure: BAR_P10_PROCEDURE_GROUP
        | tuple[BAR_P10_PROCEDURE_GROUP, ...]
        | None = None,  #  (PR1.8, GP2.9, ...)
    ):
        """
         - `BAR_P10 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/BAR_P10>`_
        The P10 event is used to communicate Ambulatory Payment Classification (APC) grouping.  The grouping can be estimated or actual, based on the APC status indictor in GP1-1.  This information is mandated in the USA by the Centers for Medicare and Medicaid Services (CMS)  for reimbursement of outpatient services.  The PID and PV1 segments are included for identification purposes only. When other patient or visit related fields change, use the A08 (update patient information) event.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
        :param patient_visit: Patient Visit (id: PV1 | seq: 5 | use: R | rpt: 1)
        :param diagnosis: Diagnosis (id: DG1 | seq: 6 | use: O | rpt: *)
        :param grouping_or_reimbursement_visit: Grouping/Reimbursement - Visit (id: GP1 | seq: 7 | use: R | rpt: 1)
        :param procedure: Procedure segment group: [PR1, GP2|None] (id: PROCEDURE | seq: 8, 9 | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 8
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_visit = patient_visit
        self.diagnosis = diagnosis
        self.grouping_or_reimbursement_visit = grouping_or_reimbursement_visit
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

    @property  # get GP1.7
    def grouping_or_reimbursement_visit(self) -> GP1:
        """
        id: GP1 | use: R | rpt: 1 | seq: 7
        ---
        return_type: GP1.7: Grouping/Reimbursement - Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP1
        """
        return self._c_data[6][0]

    @grouping_or_reimbursement_visit.setter  # set GP1.7
    def grouping_or_reimbursement_visit(self, gp1: GP1):
        """
        id: GP1 | use: R | rpt: 1 | seq: 7
        ---
        param_type: GP1.7: Grouping/Reimbursement - Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GP1
        """
        self._c_data[6] = (gp1,)

    @property  # get PROCEDURE
    def procedure(self) -> tuple[BAR_P10_PROCEDURE_GROUP, ...] | tuple[None]:
        """
        id: BAR_P10_PROCEDURE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[BAR_P10_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P10_PROCEDURE_GROUP
        """
        return self._c_data[7]

    @procedure.setter  # set PROCEDURE
    def procedure(
        self,
        procedure: BAR_P10_PROCEDURE_GROUP | tuple[BAR_P10_PROCEDURE_GROUP, ...] | None,
    ):
        """
        id: PROCEDURE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: BAR_P10_PROCEDURE_GROUP.None | tuple[BAR_P10_PROCEDURE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/BAR_P10_PROCEDURE_GROUP
        """
        if isinstance(procedure, tuple):
            self._c_data[7] = procedure
        else:
            self._c_data[7] = (procedure,)
