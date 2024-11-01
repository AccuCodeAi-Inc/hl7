from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segment_groups.OUL_R23_SPECIMEN_GROUP import OUL_R23_SPECIMEN_GROUP
from ..segment_groups.OUL_R23_PATIENT_GROUP import OUL_R23_PATIENT_GROUP
from ..segment_groups.OUL_R23_VISIT_GROUP import OUL_R23_VISIT_GROUP
from ..segments.NTE import NTE
from ..segments.DSC import DSC
from ..segments.SFT import SFT


"""
Unsolicited Specimen Container Oriented Observation Message - OUL_R23
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::OUL_R23 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import OUL_R23
from utils.hl7.v2_5_1.segments import (
    SFT, DSC, NTE, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    OUL_R23_PATIENT_GROUP, OUL_R23_SPECIMEN_GROUP, OUL_R23_VISIT_GROUP
)

oul_r23 = OUL_R23(  #  - This message was designed to accommodate specimen oriented testing
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    notes_and_comments=None,  # NTE(...) 
    patient=None,  # OUL_R23_PATIENT_GROUP(...) 
    visit=None,  # OUL_R23_VISIT_GROUP(...) 
    specimen=oul_r23_specimen_group,  # OUL_R23_SPECIMEN_GROUP(...)  # Required.
    continuation_pointer=None,  # DSC(...) 
)

-----END TRIGGER_EVENT::OUL_R23 TEMPLATE-----
"""


class OUL_R23(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """OUL_R23"""
    _hl7_name = """Unsolicited Specimen Container Oriented Observation Message"""
    _hl7_description = """This message was designed to accommodate specimen oriented testing"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1)
    _c_usage = ("R", "O", "O", "O", "O", "R", "O")
    _c_aliases = ("1", "2", "3", "None", "None", "None", "23")
    _c_components = (MSH, SFT, NTE, OUL_R23_PATIENT_GROUP, OUL_R23_VISIT_GROUP, OUL_R23_SPECIMEN_GROUP, DSC)
    _c_name = ("MSH", "SFT", "NTE", "PATIENT", "VISIT", "SPECIMEN", "DSC")
    _c_is_group = (False, False, False, True, True, True, False)
    _c_attrs = ("message_header", "software_segment", "notes_and_comments", "patient", "visit", "specimen", "continuation_pointer",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        specimen: OUL_R23_SPECIMEN_GROUP
        | tuple[OUL_R23_SPECIMEN_GROUP, ...],  #  Required. (SPM.9, OBX.10, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        notes_and_comments: NTE | None = None,  #  NTE.3
        patient: OUL_R23_PATIENT_GROUP | None = None,  #  PID.4, PD1.5, NTE.6
        visit: OUL_R23_VISIT_GROUP | None = None,  #  PV1.7, PV2.8
        continuation_pointer: DSC | None = None,  #  DSC.23
    ):
        """
         - `OUL_R23 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/OUL_R23>`_
        This message was designed to accommodate specimen oriented testing. It should be applicable to, e.g.,  laboratory automation systems requiring container

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param notes_and_comments: Notes and Comments (id: NTE | seq: 3 | use: O | rpt: 1)
        :param patient: Patient segment group: [PID, PD1|None, NTE|None] (id: PATIENT | seq: 4, 5, 6 | use: O | rpt: 1)
        :param visit: Visit segment group: [PV1, PV2|None] (id: VISIT | seq: 7, 8 | use: O | rpt: 1)
        :param specimen: Specimen segment group: [SPM, OBX|None, CONTAINER] (id: SPECIMEN | seq: 9, 10, None | use: R | rpt: *)
        :param continuation_pointer: Continuation Pointer (id: DSC | seq: 23 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.notes_and_comments = notes_and_comments
        self.patient = patient
        self.visit = visit
        self.specimen = specimen
        self.continuation_pointer = continuation_pointer

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

    @property  # get NTE.3
    def notes_and_comments(self) -> NTE | None:
        """
        id: NTE | use: O | rpt: 1 | seq: 3
        ---
        return_type: NTE.3: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        return self._c_data[2][0]

    @notes_and_comments.setter  # set NTE.3
    def notes_and_comments(self, nte: NTE | None):
        """
        id: NTE | use: O | rpt: 1 | seq: 3
        ---
        param_type: NTE.3: Notes and Comments
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NTE
        """
        self._c_data[2] = (nte,)

    @property  # get OUL_R23_PATIENT_GROUP.None
    def patient(self) -> OUL_R23_PATIENT_GROUP | None:
        """
        id: OUL_R23_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OUL_R23_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_PATIENT_GROUP
        """
        return self._c_data[3][0]

    @patient.setter  # set OUL_R23_PATIENT_GROUP.None
    def patient(self, patient: OUL_R23_PATIENT_GROUP | None):
        """
        id: OUL_R23_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OUL_R23_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_PATIENT_GROUP
        """
        self._c_data[3] = (patient,)

    @property  # get OUL_R23_VISIT_GROUP.None
    def visit(self) -> OUL_R23_VISIT_GROUP | None:
        """
        id: OUL_R23_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: OUL_R23_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_VISIT_GROUP
        """
        return self._c_data[4][0]

    @visit.setter  # set OUL_R23_VISIT_GROUP.None
    def visit(self, v_isit: OUL_R23_VISIT_GROUP | None):
        """
        id: OUL_R23_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: OUL_R23_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_VISIT_GROUP
        """
        self._c_data[4] = (v_isit,)

    @property  # get SPECIMEN
    def specimen(self) -> tuple[OUL_R23_SPECIMEN_GROUP, ...]:
        """
        id: OUL_R23_SPECIMEN_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[OUL_R23_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_SPECIMEN_GROUP
        """
        return self._c_data[5]

    @specimen.setter  # set SPECIMEN
    def specimen(
        self, specimen: OUL_R23_SPECIMEN_GROUP | tuple[OUL_R23_SPECIMEN_GROUP, ...]
    ):
        """
        id: SPECIMEN SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: OUL_R23_SPECIMEN_GROUP.None | tuple[OUL_R23_SPECIMEN_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/OUL_R23_SPECIMEN_GROUP
        """
        if isinstance(specimen, tuple):
            self._c_data[5] = specimen
        else:
            self._c_data[5] = (specimen,)

    @property  # get DSC.23
    def continuation_pointer(self) -> DSC | None:
        """
        id: DSC | use: O | rpt: 1 | seq: 23
        ---
        return_type: DSC.23: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        return self._c_data[6][0]

    @continuation_pointer.setter  # set DSC.23
    def continuation_pointer(self, dsc: DSC | None):
        """
        id: DSC | use: O | rpt: 1 | seq: 23
        ---
        param_type: DSC.23: Continuation Pointer
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DSC
        """
        self._c_data[6] = (dsc,)
