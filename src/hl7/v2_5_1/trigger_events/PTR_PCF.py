from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.ERR import ERR
from ..segments.QRD import QRD
from ..segments.MSH import MSH
from ..segments.MSA import MSA
from ..segment_groups.PTR_PCF_PATIENT_GROUP import PTR_PCF_PATIENT_GROUP
from ..segments.QAK import QAK


"""
Pathway (problem-oriented) query response - PTR_PCF
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::PTR_PCF TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import PTR_PCF
from utils.hl7.v2_5_1.segments import (
    QAK, ERR, MSA, QRD, MSH, SFT
)
from utils.hl7.v2_5_1.segment_groups import (
    PTR_PCF_PATIENT_GROUP
)

ptr_pcf = PTR_PCF(  #  - The following trigger/message event is served by PTR (a response from the system responsible for maintaining the problem-oriented pathway information)
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    message_acknowledgment=msa,  # MSA(...)  # Required.
    error=None,  # ERR(...) 
    query_acknowledgment=None,  # QAK(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    patient=ptr_pcf_patient_group,  # PTR_PCF_PATIENT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::PTR_PCF TEMPLATE-----
"""


class PTR_PCF(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """PTR_PCF"""
    _hl7_name = """Pathway (problem-oriented) query response"""
    _hl7_description = """The following trigger/message event is served by PTR (a response from the system responsible for maintaining the problem-oriented pathway information)"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PTR_PCF"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 65535, 1, 1, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "R", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "None")
    _c_components = (MSH, SFT, MSA, ERR, QAK, QRD, PTR_PCF_PATIENT_GROUP)
    _c_name = ("MSH", "SFT", "MSA", "ERR", "QAK", "QRD", "PATIENT")
    _c_is_group = (False, False, False, False, False, False, True)
    _c_attrs = ("message_header", "software_segment", "message_acknowledgment", "error", "query_acknowledgment", "original_style_query_definition", "patient",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.3
        original_style_query_definition: QRD,  #  Required. QRD.6
        patient: PTR_PCF_PATIENT_GROUP
        | tuple[PTR_PCF_PATIENT_GROUP, ...],  #  Required. (PID.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        error: ERR | tuple[ERR, ...] | None = None,  #  ERR.4
        query_acknowledgment: QAK | None = None,  #  QAK.5
    ):
        """
         - `PTR_PCF <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/PTR_PCF>`_
        The following trigger/message event is served by PTR (a response from the system responsible for maintaining the problem-oriented pathway information).

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 3 | use: R | rpt: 1)
        :param error: Error (id: ERR | seq: 4 | use: O | rpt: *)
        :param query_acknowledgment: Query Acknowledgment (id: QAK | seq: 5 | use: O | rpt: 1)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 6 | use: R | rpt: 1)
        :param patient: Patient segment group: [PID, PATIENT VISIT|None, PATHWAY] (id: PATIENT | seq: 7, None, None | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 7
        self.message_header = message_header
        self.software_segment = software_segment
        self.message_acknowledgment = message_acknowledgment
        self.error = error
        self.query_acknowledgment = query_acknowledgment
        self.original_style_query_definition = original_style_query_definition
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

    @property  # get ERR
    def error(self) -> tuple[ERR, ...] | tuple[None]:
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        return_type: tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        return self._c_data[3]

    @error.setter  # set ERR
    def error(self, err: ERR | tuple[ERR, ...] | None):
        """
        id: ERR SEGMENT GROUP | use: O | rpt: * | seq: 4
        ---
        param_type: ERR.4 | tuple[ERR, ...]: (Error, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ERR
        """
        if isinstance(err, tuple):
            self._c_data[3] = err
        else:
            self._c_data[3] = (err,)

    @property  # get QAK.5
    def query_acknowledgment(self) -> QAK | None:
        """
        id: QAK | use: O | rpt: 1 | seq: 5
        ---
        return_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        return self._c_data[4][0]

    @query_acknowledgment.setter  # set QAK.5
    def query_acknowledgment(self, qak: QAK | None):
        """
        id: QAK | use: O | rpt: 1 | seq: 5
        ---
        param_type: QAK.5: Query Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QAK
        """
        self._c_data[4] = (qak,)

    @property  # get QRD.6
    def original_style_query_definition(self) -> QRD:
        """
        id: QRD | use: R | rpt: 1 | seq: 6
        ---
        return_type: QRD.6: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        return self._c_data[5][0]

    @original_style_query_definition.setter  # set QRD.6
    def original_style_query_definition(self, qrd: QRD):
        """
        id: QRD | use: R | rpt: 1 | seq: 6
        ---
        param_type: QRD.6: Original-Style Query Definition
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/QRD
        """
        self._c_data[5] = (qrd,)

    @property  # get PATIENT
    def patient(self) -> tuple[PTR_PCF_PATIENT_GROUP, ...]:
        """
        id: PTR_PCF_PATIENT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[PTR_PCF_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP
        """
        return self._c_data[6]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: PTR_PCF_PATIENT_GROUP | tuple[PTR_PCF_PATIENT_GROUP, ...]
    ):
        """
        id: PATIENT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: PTR_PCF_PATIENT_GROUP.None | tuple[PTR_PCF_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PTR_PCF_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[6] = patient
        else:
            self._c_data[6] = (patient,)
