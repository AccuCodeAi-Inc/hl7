from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.QRF import QRF
from ..segment_groups.VXR_V03_PATIENT_VISIT_GROUP import VXR_V03_PATIENT_VISIT_GROUP
from ..segments.SFT import SFT
from ..segments.MSH import MSH
from ..segments.GT1 import GT1
from ..segments.MSA import MSA
from ..segment_groups.VXR_V03_ORDER_GROUP import VXR_V03_ORDER_GROUP
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.NK1 import NK1
from ..segments.QRD import QRD
from ..segment_groups.VXR_V03_INSURANCE_GROUP import VXR_V03_INSURANCE_GROUP


"""
Vaccination Record Response - VXR_V03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::VXR_V03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXR_V03
from utils.hl7.v2_5_1.segments import (
    MSH, PID, PD1, QRD, NK1, SFT, GT1, QRF, MSA
)
from utils.hl7.v2_5_1.segment_groups import (
    VXR_V03_INSURANCE_GROUP, VXR_V03_PATIENT_VISIT_GROUP, VXR_V03_ORDER_GROUP
)

vxr_v03 = VXR_V03(  #  - When the patient has been uniquely identified (there is only one match to the query), the response to the query (with a V03 event) will follow this format
    message_header=msh,  # MSH(...)  # Required.
    message_acknowledgment=msa,  # MSA(...)  # Required.
    software_segment=None,  # SFT(...) 
    original_style_query_definition=qrd,  # QRD(...)  # Required.
    original_style_query_filter=None,  # QRF(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    patient_visit=None,  # VXR_V03_PATIENT_VISIT_GROUP(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # VXR_V03_INSURANCE_GROUP(...) 
    order=None,  # VXR_V03_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT::VXR_V03 TEMPLATE-----
"""


class VXR_V03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """VXR_V03"""
    _hl7_name = """Vaccination Record Response"""
    _hl7_description = """When the patient has been uniquely identified (there is only one match to the query), the response to the query (with a V03 event) will follow this format"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXR_V03"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 1, 65535, 1, 1, 1, 1, 65535, 1, 65535, 65535, 65535)
    _c_usage = ("R", "R", "O", "R", "O", "R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "None", "11", "None", "None")
    _c_components = (MSH, MSA, SFT, QRD, QRF, PID, PD1, NK1, VXR_V03_PATIENT_VISIT_GROUP, GT1, VXR_V03_INSURANCE_GROUP, VXR_V03_ORDER_GROUP)
    _c_name = ("MSH", "MSA", "SFT", "QRD", "QRF", "PID", "PD1", "NK1", "PATIENT VISIT", "GT1", "INSURANCE", "ORDER")
    _c_is_group = (False, False, False, False, False, False, False, False, True, False, True, True)
    _c_attrs = ("message_header", "message_acknowledgment", "software_segment", "original_style_query_definition", "original_style_query_filter", "patient_identification", "patient_additional_demographic", "next_of_kin_or_associated_parties", "patient_visit", "guarantor", "insurance", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        message_acknowledgment: MSA,  #  Required. MSA.2
        original_style_query_definition: QRD,  #  Required. QRD.4
        patient_identification: PID,  #  Required. PID.6
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.3
        original_style_query_filter: QRF | None = None,  #  QRF.5
        patient_additional_demographic: PD1 | None = None,  #  PD1.7
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.8
        patient_visit: VXR_V03_PATIENT_VISIT_GROUP | None = None,  #  PV1.9, PV2.10
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.11
        insurance: VXR_V03_INSURANCE_GROUP
        | tuple[VXR_V03_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.12, IN2.13, IN3.14, ...)
        order: VXR_V03_ORDER_GROUP
        | tuple[VXR_V03_ORDER_GROUP, ...]
        | None = None,  #  (ORC.15, RXA.18, RXR.19, ...)
    ):
        """
         - `VXR_V03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXR_V03>`_
        When the patient has been uniquely identified (there is only one "match" to the query), the response to the query (with a V03 event) will follow this format.

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param message_acknowledgment: Message Acknowledgment (id: MSA | seq: 2 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 3 | use: O | rpt: *)
        :param original_style_query_definition: Original-Style Query Definition (id: QRD | seq: 4 | use: R | rpt: 1)
        :param original_style_query_filter: Original style query filter (id: QRF | seq: 5 | use: O | rpt: 1)
        :param patient_identification: Patient Identification (id: PID | seq: 6 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 7 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 8 | use: O | rpt: *)
        :param patient_visit: Patient Visit segment group: [PV1, PV2|None] (id: PATIENT VISIT | seq: 9, 10 | use: O | rpt: 1)
        :param guarantor: Guarantor (id: GT1 | seq: 11 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 12, 13, 14 | use: O | rpt: *)
        :param order: Order segment group: [ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None] (id: ORDER | seq: 15, None, 18, 19, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 12
        self.message_header = message_header
        self.message_acknowledgment = message_acknowledgment
        self.software_segment = software_segment
        self.original_style_query_definition = original_style_query_definition
        self.original_style_query_filter = original_style_query_filter
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.patient_visit = patient_visit
        self.guarantor = guarantor
        self.insurance = insurance
        self.order = order

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

    @property  # get PID.6
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        return_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[5][0]

    @patient_identification.setter  # set PID.6
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 6
        ---
        param_type: PID.6: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[5] = (pid,)

    @property  # get PD1.7
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PD1.7: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[6][0]

    @patient_additional_demographic.setter  # set PD1.7
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PD1.7: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[6] = (pd1,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[7]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: NK1.8 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[7] = nk1
        else:
            self._c_data[7] = (nk1,)

    @property  # get VXR_V03_PATIENT_VISIT_GROUP.None
    def patient_visit(self) -> VXR_V03_PATIENT_VISIT_GROUP | None:
        """
        id: VXR_V03_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: VXR_V03_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_PATIENT_VISIT_GROUP
        """
        return self._c_data[8][0]

    @patient_visit.setter  # set VXR_V03_PATIENT_VISIT_GROUP.None
    def patient_visit(self, patient_v_isit: VXR_V03_PATIENT_VISIT_GROUP | None):
        """
        id: VXR_V03_PATIENT_VISIT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: VXR_V03_PATIENT_VISIT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_PATIENT_VISIT_GROUP
        """
        self._c_data[8] = (patient_v_isit,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[9]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 11
        ---
        param_type: GT1.11 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[9] = gt1
        else:
            self._c_data[9] = (gt1,)

    @property  # get INSURANCE
    def insurance(self) -> tuple[VXR_V03_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: VXR_V03_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXR_V03_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_INSURANCE_GROUP
        """
        return self._c_data[10]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: VXR_V03_INSURANCE_GROUP | tuple[VXR_V03_INSURANCE_GROUP, ...] | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXR_V03_INSURANCE_GROUP.None | tuple[VXR_V03_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[10] = insurance
        else:
            self._c_data[10] = (insurance,)

    @property  # get ORDER
    def order(self) -> tuple[VXR_V03_ORDER_GROUP, ...] | tuple[None]:
        """
        id: VXR_V03_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXR_V03_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_ORDER_GROUP
        """
        return self._c_data[11]

    @order.setter  # set ORDER
    def order(
        self, order: VXR_V03_ORDER_GROUP | tuple[VXR_V03_ORDER_GROUP, ...] | None
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXR_V03_ORDER_GROUP.None | tuple[VXR_V03_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXR_V03_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[11] = order
        else:
            self._c_data[11] = (order,)
