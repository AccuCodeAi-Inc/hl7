from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segment_groups.CSU_C10_PATIENT_GROUP import CSU_C10_PATIENT_GROUP


"""
Patient completes the clinical trial - CSU_C10
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::CSU_C10 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CSU_C10
from utils.hl7.v2_5_1.segments import (
    SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    CSU_C10_PATIENT_GROUP
)

csu_c10 = CSU_C10(  #  - Data are entered in the clinical trials system or may reside in laboratory, pathology, radiology, pharmacy and/or other clinical applications
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient=csu_c10_patient_group,  # CSU_C10_PATIENT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::CSU_C10 TEMPLATE-----
"""


class CSU_C10(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """CSU_C10"""
    _hl7_name = """Patient completes the clinical trial"""
    _hl7_description = """Data are entered in the clinical trials system or may reside in laboratory, pathology, radiology, pharmacy and/or other clinical applications"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C10"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("1", "2", "None")
    _c_components = (MSH, SFT, CSU_C10_PATIENT_GROUP)
    _c_name = ("MSH", "SFT", "PATIENT")
    _c_is_group = (False, False, True)
    _c_attrs = ("message_header", "software_segment", "patient",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient: CSU_C10_PATIENT_GROUP
        | tuple[
            CSU_C10_PATIENT_GROUP, ...
        ],  #  Required. (PID.3, PD1.4, NTE.5, CSR.8, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `CSU_C10 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CSU_C10>`_
        Data are entered in the clinical trials system or may reside in laboratory, pathology, radiology, pharmacy and/or other clinical applications.  Most clinical trials data - clinical observations and study variables - will be communicated in OBR and OBX segments.  The CSR, CSP, and CSS segments will identify the specific association these OBR and OBX have to the clinical trial.  Data can be broadcast or transmitted in batch mode to study sponsors or the data management center for collaborative studies.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PD1|None, NTE|None, VISIT|None, CSR, STUDY PHASE] (id: PATIENT | seq: 3, 4, 5, None, 8, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 3
        self.message_header = message_header
        self.software_segment = software_segment
        self.patient = patient

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

    @property  # get PATIENT
    def patient(self) -> tuple[CSU_C10_PATIENT_GROUP, ...]:
        """
        id: CSU_C10_PATIENT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CSU_C10_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C10_PATIENT_GROUP
        """
        return self._c_data[2]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: CSU_C10_PATIENT_GROUP | tuple[CSU_C10_PATIENT_GROUP, ...]
    ):
        """
        id: PATIENT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CSU_C10_PATIENT_GROUP.None | tuple[CSU_C10_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CSU_C10_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[2] = patient
        else:
            self._c_data[2] = (patient,)
