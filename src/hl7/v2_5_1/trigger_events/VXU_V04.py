from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.PD1 import PD1
from ..segments.GT1 import GT1
from ..segment_groups.VXU_V04_PATIENT_GROUP import VXU_V04_PATIENT_GROUP
from ..segments.SFT import SFT
from ..segments.PID import PID
from ..segments.MSH import MSH
from ..segment_groups.VXU_V04_INSURANCE_GROUP import VXU_V04_INSURANCE_GROUP
from ..segments.NK1 import NK1
from ..segment_groups.VXU_V04_ORDER_GROUP import VXU_V04_ORDER_GROUP


"""
Unsolicited Vaccination Record Update - VXU_V04
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::VXU_V04 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import VXU_V04
from utils.hl7.v2_5_1.segments import (
    SFT, PID, GT1, NK1, MSH, PD1
)
from utils.hl7.v2_5_1.segment_groups import (
    VXU_V04_PATIENT_GROUP, VXU_V04_ORDER_GROUP, VXU_V04_INSURANCE_GROUP
)

vxu_v04 = VXU_V04(  #  - When a provider wishes to update the patient's vaccination record being held in a registry, he will transmit an unsolicited update of the record (a V04 trigger event)
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    next_of_kin_or_associated_parties=None,  # NK1(...) 
    patient=None,  # VXU_V04_PATIENT_GROUP(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # VXU_V04_INSURANCE_GROUP(...) 
    order=None,  # VXU_V04_ORDER_GROUP(...) 
)

-----END TRIGGER_EVENT::VXU_V04 TEMPLATE-----
"""


class VXU_V04(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """VXU_V04"""
    _hl7_name = """Unsolicited Vaccination Record Update"""
    _hl7_description = """When a provider wishes to update the patient's vaccination record being held in a registry, he will transmit an unsolicited update of the record (a V04 trigger event)"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXU_V04"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 65535, 1, 65535, 65535, 65535)
    _c_usage = ("R", "O", "R", "O", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "None", "8", "None", "None")
    _c_components = (MSH, SFT, PID, PD1, NK1, VXU_V04_PATIENT_GROUP, GT1, VXU_V04_INSURANCE_GROUP, VXU_V04_ORDER_GROUP)
    _c_name = ("MSH", "SFT", "PID", "PD1", "NK1", "PATIENT", "GT1", "INSURANCE", "ORDER")
    _c_is_group = (False, False, False, False, False, True, False, True, True)
    _c_attrs = ("message_header", "software_segment", "patient_identification", "patient_additional_demographic", "next_of_kin_or_associated_parties", "patient", "guarantor", "insurance", "order",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        patient_identification: PID,  #  Required. PID.3
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.4
        next_of_kin_or_associated_parties: NK1
        | tuple[NK1, ...]
        | None = None,  #  NK1.5
        patient: VXU_V04_PATIENT_GROUP | None = None,  #  PV1.6, PV2.7
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.8
        insurance: VXU_V04_INSURANCE_GROUP
        | tuple[VXU_V04_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.9, IN2.10, IN3.11, ...)
        order: VXU_V04_ORDER_GROUP
        | tuple[VXU_V04_ORDER_GROUP, ...]
        | None = None,  #  (ORC.12, RXA.15, RXR.16, ...)
    ):
        """
         - `VXU_V04 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/VXU_V04>`_
        When a provider wishes to update the patient's vaccination record being held in a registry, he will transmit an unsolicited update of the record (a V04 trigger event).

        :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
        :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
        :param patient_identification: Patient Identification (id: PID | seq: 3 | use: R | rpt: 1)
        :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 4 | use: O | rpt: 1)
        :param next_of_kin_or_associated_parties: Next of Kin / Associated Parties (id: NK1 | seq: 5 | use: O | rpt: *)
        :param patient: Patient segment group: [PV1, PV2|None] (id: PATIENT | seq: 6, 7 | use: O | rpt: 1)
        :param guarantor: Guarantor (id: GT1 | seq: 8 | use: O | rpt: *)
        :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None] (id: INSURANCE | seq: 9, 10, 11 | use: O | rpt: *)
        :param order: Order segment group: [ORC, TIMING|None, RXA, RXR|None, OBSERVATION|None] (id: ORDER | seq: 12, None, 15, 16, None | use: O | rpt: *)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 9
        self.message_header = message_header
        self.software_segment = software_segment
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.next_of_kin_or_associated_parties = next_of_kin_or_associated_parties
        self.patient = patient
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

    @property  # get PID.3
    def patient_identification(self) -> PID:
        """
        id: PID | use: R | rpt: 1 | seq: 3
        ---
        return_type: PID.3: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        return self._c_data[2][0]

    @patient_identification.setter  # set PID.3
    def patient_identification(self, pid: PID):
        """
        id: PID | use: R | rpt: 1 | seq: 3
        ---
        param_type: PID.3: Patient Identification
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PID
        """
        self._c_data[2] = (pid,)

    @property  # get PD1.4
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 4
        ---
        return_type: PD1.4: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[3][0]

    @patient_additional_demographic.setter  # set PD1.4
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 4
        ---
        param_type: PD1.4: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[3] = (pd1,)

    @property  # get NK1
    def next_of_kin_or_associated_parties(self) -> tuple[NK1, ...] | tuple[None]:
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        return_type: tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        return self._c_data[4]

    @next_of_kin_or_associated_parties.setter  # set NK1
    def next_of_kin_or_associated_parties(self, nk1: NK1 | tuple[NK1, ...] | None):
        """
        id: NK1 SEGMENT GROUP | use: O | rpt: * | seq: 5
        ---
        param_type: NK1.5 | tuple[NK1, ...]: (Next of Kin / Associated Parties, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/NK1
        """
        if isinstance(nk1, tuple):
            self._c_data[4] = nk1
        else:
            self._c_data[4] = (nk1,)

    @property  # get VXU_V04_PATIENT_GROUP.None
    def patient(self) -> VXU_V04_PATIENT_GROUP | None:
        """
        id: VXU_V04_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        return_type: VXU_V04_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_PATIENT_GROUP
        """
        return self._c_data[5][0]

    @patient.setter  # set VXU_V04_PATIENT_GROUP.None
    def patient(self, patient: VXU_V04_PATIENT_GROUP | None):
        """
        id: VXU_V04_PATIENT_GROUP | use: O | rpt: 1 | seq: None
        ---
        param_type: VXU_V04_PATIENT_GROUP.None: None
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_PATIENT_GROUP
        """
        self._c_data[5] = (patient,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[6]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 8
        ---
        param_type: GT1.8 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[6] = gt1
        else:
            self._c_data[6] = (gt1,)

    @property  # get INSURANCE
    def insurance(self) -> tuple[VXU_V04_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: VXU_V04_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXU_V04_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_INSURANCE_GROUP
        """
        return self._c_data[7]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: VXU_V04_INSURANCE_GROUP | tuple[VXU_V04_INSURANCE_GROUP, ...] | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXU_V04_INSURANCE_GROUP.None | tuple[VXU_V04_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[7] = insurance
        else:
            self._c_data[7] = (insurance,)

    @property  # get ORDER
    def order(self) -> tuple[VXU_V04_ORDER_GROUP, ...] | tuple[None]:
        """
        id: VXU_V04_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[VXU_V04_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_ORDER_GROUP
        """
        return self._c_data[8]

    @order.setter  # set ORDER
    def order(
        self, order: VXU_V04_ORDER_GROUP | tuple[VXU_V04_ORDER_GROUP, ...] | None
    ):
        """
        id: ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: VXU_V04_ORDER_GROUP.None | tuple[VXU_V04_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/VXU_V04_ORDER_GROUP
        """
        if isinstance(order, tuple):
            self._c_data[8] = order
        else:
            self._c_data[8] = (order,)
