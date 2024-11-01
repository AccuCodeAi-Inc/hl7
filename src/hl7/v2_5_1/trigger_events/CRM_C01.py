from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segment_groups.CRM_C01_PATIENT_GROUP import CRM_C01_PATIENT_GROUP


"""
Register a patient on a clinical trial - CRM_C01
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::CRM_C01 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import CRM_C01
from utils.hl7.v2_5_1.segments import (
    SFT, MSH
)
from utils.hl7.v2_5_1.segment_groups import (
    CRM_C01_PATIENT_GROUP
)

crm_c01 = CRM_C01(  #  - The data are entered in a clinical trials or other patient data system and broadcast to other facility systems such as order entry, pharmacy, accounting, and nursing systems
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient=crm_c01_patient_group,  # CRM_C01_PATIENT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::CRM_C01 TEMPLATE-----
"""


class CRM_C01(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """CRM_C01"""
    _hl7_name = """Register a patient on a clinical trial"""
    _hl7_description = """The data are entered in a clinical trials or other patient data system and broadcast to other facility systems such as order entry, pharmacy, accounting, and nursing systems"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CRM_C01"""
    _c_length = (-1,-1,-1,)
    _c_rpt = (1, 65535, 65535)
    _c_usage = ("R", "O", "R")
    _c_aliases = ("1", "2", "None")
    _c_components = (MSH, SFT, CRM_C01_PATIENT_GROUP)
    _c_name = ("MSH", "SFT", "PATIENT")
    _c_is_group = (False, False, True)
    _c_attrs = ("message_header", "software_segment", "patient",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient: CRM_C01_PATIENT_GROUP
        | tuple[
            CRM_C01_PATIENT_GROUP, ...
        ],  #  Required. (PID.3, PV1.4, CSR.5, CSP.6, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
    ):
        """
         - `CRM_C01 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/CRM_C01>`_
        The data are entered in a clinical trials or other patient data system and broadcast to other facility systems such as order entry, pharmacy, accounting, and nursing systems.  They can be transmitted in batch mode or broadcast to outside-facility computer systems, including diagnostic and patient management systems.  It is assumed that proper routing and security mechanisms are in place.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient: Patient segment group: [PID, PV1|None, CSR, CSP|None] (id: PATIENT | seq: 3, 4, 5, 6 | use: R | rpt: *)
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
    def patient(self) -> tuple[CRM_C01_PATIENT_GROUP, ...]:
        """
        id: CRM_C01_PATIENT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[CRM_C01_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CRM_C01_PATIENT_GROUP
        """
        return self._c_data[2]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: CRM_C01_PATIENT_GROUP | tuple[CRM_C01_PATIENT_GROUP, ...]
    ):
        """
        id: PATIENT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: CRM_C01_PATIENT_GROUP.None | tuple[CRM_C01_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/CRM_C01_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[2] = patient
        else:
            self._c_data[2] = (patient,)
