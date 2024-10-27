from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.SFT import SFT
from ..segments.QRF import QRF
from ..segment_groups.VXX_V02_PATIENT_GROUP import VXX_V02_PATIENT_GROUP
from ..segments.QRD import QRD
from ..segments.MSH import MSH
from ..segments.MSA import MSA


"""
Vaccination Record Query Returning Multiple PID Matches - VXX_V02
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::VXX_V02 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXX_V02
from utils.hl7.v2_5_1.segments import (
    MSA, QRD, MSH, SFT, QRF
)
from utils.hl7.v2_5_1.segment_groups import (
    VXX_V02_PATIENT_GROUP
)

vxx_v02 = VXX_V02(  #  - In response to a query for the definitive patient vaccination record, the registry holding the record will return it to the registry originating the query
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    software_segment=None,  # SFT(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    patient=vxx_v02_patient_group,  # VXX_V02_PATIENT_GROUP(...)  # Required.
)

-----END TRIGGER_EVENT::VXX_V02 TEMPLATE-----
"""


class VXX_V02(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """VXX_V02"""
    _hl7_name = """Vaccination Record Query Returning Multiple PID Matches"""
    _hl7_description = """In response to a query for the definitive patient vaccination record, the registry holding the record will return it to the registry originating the query"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXX_V02"""
    _c_length = (-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 1, 65535)
    _c_usage = ("R", "R", "O", "R", "O", "R")
    _c_aliases = ("1", "2", "3", "4", "5", "None")
    _c_components = (MSH, MSA, SFT, QRD, QRF, VXX_V02_PATIENT_GROUP)
    _c_name = ("MSH", "MSA", "SFT", "QRD", "QRF", "PATIENT")
    _c_is_group = (False, False, False, False, False, True)
    _c_attrs = ("message_header", "message_acknowledgment", "software_segment", "original_style_query_definition", "original_style_query_filter", "patient",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        original_style_query_definition: QRD,  #  Required. QRD.4
        patient: VXX_V02_PATIENT_GROUP
        | tuple[VXX_V02_PATIENT_GROUP, ...],  #  Required. (PID.6, NK1.7, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.3
        original_style_query_filter: QRF | None = None,  #  QRF.5
    ):
        """
         - `VXX_V02 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXX_V02>`_
        In response to a query for the definitive patient vaccination record, the registry holding the record will return it to the registry originating the query.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 3 | use: O | rpt: *)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 4 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 5 | use: O | rpt: 1)
        :param patient: Patient segment group: [PID, NK1|None] (id: PATIENT | seq: 6, 7 | use: R | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 6
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.software_segment = software_segment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
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

    @property  # get MSA.2
    def message_acknowledgment(self) -> MSA:
        """
        id: MSA | use: R | rpt: 1 | seq: 2
        ---
        return_type: MSA.2: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        return self._c_data[1][0]

    @message_acknowledgment.setter  # set MSA.2
    def message_acknowledgment(self, msa: MSA):
        """
        id: MSA | use: R | rpt: 1 | seq: 2
        ---
        param_type: MSA.2: Message Acknowledgment
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/MSA
        """
        self._c_data[1] = (msa,)

    @property  # get SFT
    def software_segment(self) -> tuple[SFT, ...] | tuple[None]:
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        return_type: tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        return self._c_data[2]

    @software_segment.setter  # set SFT
    def software_segment(self, sft: SFT | tuple[SFT, ...] | None):
        """
        id: SFT SEGMENT GROUP | use: O | rpt: * | seq: 3
        ---
        param_type: SFT.3 | tuple[SFT, ...]: (Software Segment, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/SFT
        """
        if isinstance(sft, tuple):
            self._c_data[2] = sft
        else:
            self._c_data[2] = (sft,)

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

    @property  # get PATIENT
    def patient(self) -> tuple[VXX_V02_PATIENT_GROUP, ...]:
        """
        id: VXX_V02_PATIENT_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[VXX_V02_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXX_V02_PATIENT_GROUP
        """
        return self._c_data[5]

    @patient.setter  # set PATIENT
    def patient(
        self, patient: VXX_V02_PATIENT_GROUP | tuple[VXX_V02_PATIENT_GROUP, ...]
    ):
        """
        id: PATIENT SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: VXX_V02_PATIENT_GROUP.None | tuple[VXX_V02_PATIENT_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXX_V02_PATIENT_GROUP
        """
        if isinstance(patient, tuple):
            self._c_data[5] = patient
        else:
            self._c_data[5] = (patient,)
