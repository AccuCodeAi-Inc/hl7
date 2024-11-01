from __future__ import annotations
from ...base import HL7TriggerEvent
from ..segments.PD1 import PD1
from ..segments.ACC import ACC
from ..segments.ROL import ROL
from ..segments.MSH import MSH
from ..segments.PV2 import PV2
from ..segments.EVN import EVN
from ..segment_groups.DFT_P03_INSURANCE_GROUP import DFT_P03_INSURANCE_GROUP
from ..segments.DB1 import DB1
from ..segments.PV1 import PV1
from ..segments.GT1 import GT1
from ..segments.DRG import DRG
from ..segments.PID import PID
from ..segments.DG1 import DG1
from ..segment_groups.DFT_P03_FINANCIAL_GROUP import DFT_P03_FINANCIAL_GROUP
from ..segments.SFT import SFT
from ..segment_groups.DFT_P03_COMMON_ORDER_GROUP import DFT_P03_COMMON_ORDER_GROUP


"""
Post Detail Financial Transactions - DFT_P03
HL7 Version: 2.5.1

-----BEGIN TRIGGER_EVENT::DFT_P03 TEMPLATE-----

from utils.hl7.v2_5_1.trigger_events import DFT_P03
from utils.hl7.v2_5_1.segments import (
    DG1, DRG, DB1, ACC, PID, SFT, EVN, MSH, PD1, ROL, PV1, PV2, GT1
)
from utils.hl7.v2_5_1.segment_groups import (
    DFT_P03_FINANCIAL_GROUP, DFT_P03_INSURANCE_GROUP, DFT_P03_COMMON_ORDER_GROUP
)

dft_p03 = DFT_P03(  #  - The Detail Financial Transaction (DFT) message is used to describe a financial transaction transmitted between systems, that is, to the billing system for ancillary charges, ADT to billing system for patient deposits, etc
    message_header=msh,  # MSH(...)  # Required.
    software_segment=None,  # SFT(...) 
    event_type=evn,  # EVN(...)  # Required.
    patient_identification=pid,  # PID(...)  # Required.
    patient_additional_demographic=None,  # PD1(...) 
    role=None,  # ROL(...) 
    patient_visit=None,  # PV1(...) 
    patient_visit_additional_information=None,  # PV2(...) 
    role_9=None,  # ROL(...) 
    disability=None,  # DB1(...) 
    common_order=None,  # DFT_P03_COMMON_ORDER_GROUP(...) 
    financial=dft_p03_financial_group,  # DFT_P03_FINANCIAL_GROUP(...)  # Required.
    diagnosis=None,  # DG1(...) 
    diagnosis_related_group=None,  # DRG(...) 
    guarantor=None,  # GT1(...) 
    insurance=None,  # DFT_P03_INSURANCE_GROUP(...) 
    accident=None,  # ACC(...) 
)

-----END TRIGGER_EVENT::DFT_P03 TEMPLATE-----
"""


class DFT_P03(HL7TriggerEvent):
    # fmt: off
    _hl7_version = """2.5.1"""
    _hl7_type = """TRIGGER_EVENT"""
    _hl7_length = -1
    _hl7_id = """DFT_P03"""
    _hl7_name = """Post Detail Financial Transactions"""
    _hl7_description = """The Detail Financial Transaction (DFT) message is used to describe a financial transaction transmitted between systems, that is, to the billing system for ancillary charges, ADT to billing system for patient deposits, etc"""
    _hl7_ref_url = """https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03"""
    _c_length = (-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,)
    _c_rpt = (1, 65535, 1, 1, 1, 65535, 1, 1, 65535, 65535, 65535, 65535, 65535, 1, 65535, 65535, 1)
    _c_usage = ("R", "O", "R", "R", "O", "O", "O", "O", "O", "O", "O", "R", "O", "O", "O", "O", "O")
    _c_aliases = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "None", "None", "29", "30", "31", "None", "36")
    _c_components = (MSH, SFT, EVN, PID, PD1, ROL, PV1, PV2, ROL, DB1, DFT_P03_COMMON_ORDER_GROUP, DFT_P03_FINANCIAL_GROUP, DG1, DRG, GT1, DFT_P03_INSURANCE_GROUP, ACC)
    _c_name = ("MSH", "SFT", "EVN", "PID", "PD1", "ROL", "PV1", "PV2", "ROL", "DB1", "COMMON ORDER", "FINANCIAL", "DG1", "DRG", "GT1", "INSURANCE", "ACC")
    _c_is_group = (False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, False)
    _c_attrs = ("message_header", "software_segment", "event_type", "patient_identification", "patient_additional_demographic", "role", "patient_visit", "patient_visit_additional_information", "role_9", "disability", "common_order", "financial", "diagnosis", "diagnosis_related_group", "guarantor", "insurance", "accident",)
    # fmt: on

    def __init__(
        self,
        message_header: MSH,  #  Required. MSH.1
        event_type: EVN,  #  Required. EVN.3
        patient_identification: PID,  #  Required. PID.4
        financial: DFT_P03_FINANCIAL_GROUP
        | tuple[DFT_P03_FINANCIAL_GROUP, ...],  #  Required. (FT1.18, NTE.19, ...)
        software_segment: SFT | tuple[SFT, ...] | None = None,  #  SFT.2
        patient_additional_demographic: PD1 | None = None,  #  PD1.5
        role: ROL | tuple[ROL, ...] | None = None,  #  ROL.6
        patient_visit: PV1 | None = None,  #  PV1.7
        patient_visit_additional_information: PV2 | None = None,  #  PV2.8
        role_9: ROL | tuple[ROL, ...] | None = None,  #  ROL.9
        disability: DB1 | tuple[DB1, ...] | None = None,  #  DB1.10
        common_order: DFT_P03_COMMON_ORDER_GROUP
        | tuple[DFT_P03_COMMON_ORDER_GROUP, ...]
        | None = None,  #  (ORC.11, ...)
        diagnosis: DG1 | tuple[DG1, ...] | None = None,  #  DG1.29
        diagnosis_related_group: DRG | None = None,  #  DRG.30
        guarantor: GT1 | tuple[GT1, ...] | None = None,  #  GT1.31
        insurance: DFT_P03_INSURANCE_GROUP
        | tuple[DFT_P03_INSURANCE_GROUP, ...]
        | None = None,  #  (IN1.32, IN2.33, IN3.34, ROL.35, ...)
        accident: ACC | None = None,  #  ACC.36
    ):
        """
                 - `DFT_P03 <https://hl7-definition.caristix.com/v2/HL7v2.5.1/TriggerEvents/DFT_P03>`_
                The Detail Financial Transaction (DFT) message is used to describe a financial transaction transmitted between systems, that is, to the billing system for ancillary charges, ADT to billing system for patient deposits, etc.

        Note:  The ROL segment is optionally included after the PD1 to transmit information for patient level primary care providers, after the PV2 for additional information on the physicians whose information is sent there (i.e. Attending Doctor, Referring Doctor, Consulting Doctor), and within the insurance construct to transmit information for insurance level primary care providers.

        Note:  There is an information overlap between the FT1, DG1 and PR1 segments.  If diagnosis information is sent in an FT1 segment, it should be consistent with the information contained in any DG1 segments present within its hierarchy. Since the procedure code field within the FT1 does not repeat, if procedure information is sent on an FT1 it is recommended that the single occurrence of the code in FT1 equates to the primary procedure (PR1-14 - Procedure Priority code value 1).

        Note:  The extra set of DG1/DRG/GT1/IN1/IN2/IN3/ROL segments added in V2.4 has been withdrawn as a technical correction

                :param message_header: Message Header (id: MSH | seq: 1 | use: R | rpt: 1)
                :param software_segment: Software Segment (id: SFT | seq: 2 | use: O | rpt: *)
                :param event_type: Event Type (id: EVN | seq: 3 | use: R | rpt: 1)
                :param patient_identification: Patient Identification (id: PID | seq: 4 | use: R | rpt: 1)
                :param patient_additional_demographic: Patient Additional Demographic (id: PD1 | seq: 5 | use: O | rpt: 1)
                :param role: Role (id: ROL | seq: 6 | use: O | rpt: *)
                :param patient_visit: Patient Visit (id: PV1 | seq: 7 | use: O | rpt: 1)
                :param patient_visit_additional_information: Patient Visit - Additional Information (id: PV2 | seq: 8 | use: O | rpt: 1)
                :param role_9: Role (id: ROL | seq: 9 | use: O | rpt: *)
                :param disability: Disability (id: DB1 | seq: 10 | use: O | rpt: *)
                :param common_order: Common Order segment group: [ORC|None, TIMING QUANTITY|None, ORDER|None, OBSERVATION|None] (id: COMMON ORDER | seq: 11, None, None, None | use: O | rpt: *)
                :param financial: Financial segment group: [FT1, NTE|None, FINANCIAL PROCEDURE|None, FINANCIAL COMMON ORDER|None] (id: FINANCIAL | seq: 18, 19, None, None | use: R | rpt: *)
                :param diagnosis: Diagnosis (id: DG1 | seq: 29 | use: O | rpt: *)
                :param diagnosis_related_group: Diagnosis Related Group (id: DRG | seq: 30 | use: O | rpt: 1)
                :param guarantor: Guarantor (id: GT1 | seq: 31 | use: O | rpt: *)
                :param insurance: Insurance segment group: [IN1, IN2|None, IN3|None, ROL|None] (id: INSURANCE | seq: 32, 33, 34, 35 | use: O | rpt: *)
                :param accident: Accident (id: ACC | seq: 36 | use: O | rpt: 1)
        """
        super().__init__()
        self._c_data: list[tuple] = [(None,)] * 17
        self.message_header = message_header
        self.software_segment = software_segment
        self.event_type = event_type
        self.patient_identification = patient_identification
        self.patient_additional_demographic = patient_additional_demographic
        self.role = role
        self.patient_visit = patient_visit
        self.patient_visit_additional_information = patient_visit_additional_information
        self.role_9 = role_9
        self.disability = disability
        self.common_order = common_order
        self.financial = financial
        self.diagnosis = diagnosis
        self.diagnosis_related_group = diagnosis_related_group
        self.guarantor = guarantor
        self.insurance = insurance
        self.accident = accident

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

    @property  # get PD1.5
    def patient_additional_demographic(self) -> PD1 | None:
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        return_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        return self._c_data[4][0]

    @patient_additional_demographic.setter  # set PD1.5
    def patient_additional_demographic(self, pd1: PD1 | None):
        """
        id: PD1 | use: O | rpt: 1 | seq: 5
        ---
        param_type: PD1.5: Patient Additional Demographic
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PD1
        """
        self._c_data[4] = (pd1,)

    @property  # get ROL
    def role(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[5]

    @role.setter  # set ROL
    def role(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 6
        ---
        param_type: ROL.6 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[5] = rol
        else:
            self._c_data[5] = (rol,)

    @property  # get PV1.7
    def patient_visit(self) -> PV1 | None:
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        return_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        return self._c_data[6][0]

    @patient_visit.setter  # set PV1.7
    def patient_visit(self, pv1: PV1 | None):
        """
        id: PV1 | use: O | rpt: 1 | seq: 7
        ---
        param_type: PV1.7: Patient Visit
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV1
        """
        self._c_data[6] = (pv1,)

    @property  # get PV2.8
    def patient_visit_additional_information(self) -> PV2 | None:
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        return_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        return self._c_data[7][0]

    @patient_visit_additional_information.setter  # set PV2.8
    def patient_visit_additional_information(self, pv2: PV2 | None):
        """
        id: PV2 | use: O | rpt: 1 | seq: 8
        ---
        param_type: PV2.8: Patient Visit - Additional Information
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/PV2
        """
        self._c_data[7] = (pv2,)

    @property  # get ROL
    def role_9(self) -> tuple[ROL, ...] | tuple[None]:
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        return_type: tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        return self._c_data[8]

    @role_9.setter  # set ROL
    def role_9(self, rol: ROL | tuple[ROL, ...] | None):
        """
        id: ROL SEGMENT GROUP | use: O | rpt: * | seq: 9
        ---
        param_type: ROL.9 | tuple[ROL, ...]: (Role, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ROL
        """
        if isinstance(rol, tuple):
            self._c_data[8] = rol
        else:
            self._c_data[8] = (rol,)

    @property  # get DB1
    def disability(self) -> tuple[DB1, ...] | tuple[None]:
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        return_type: tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        return self._c_data[9]

    @disability.setter  # set DB1
    def disability(self, db1: DB1 | tuple[DB1, ...] | None):
        """
        id: DB1 SEGMENT GROUP | use: O | rpt: * | seq: 10
        ---
        param_type: DB1.10 | tuple[DB1, ...]: (Disability, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DB1
        """
        if isinstance(db1, tuple):
            self._c_data[9] = db1
        else:
            self._c_data[9] = (db1,)

    @property  # get COMMON ORDER
    def common_order(self) -> tuple[DFT_P03_COMMON_ORDER_GROUP, ...] | tuple[None]:
        """
        id: DFT_P03_COMMON_ORDER_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP
        """
        return self._c_data[10]

    @common_order.setter  # set COMMON ORDER
    def common_order(
        self,
        common_order: DFT_P03_COMMON_ORDER_GROUP
        | tuple[DFT_P03_COMMON_ORDER_GROUP, ...]
        | None,
    ):
        """
        id: COMMON ORDER SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P03_COMMON_ORDER_GROUP.None | tuple[DFT_P03_COMMON_ORDER_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_COMMON_ORDER_GROUP
        """
        if isinstance(common_order, tuple):
            self._c_data[10] = common_order
        else:
            self._c_data[10] = (common_order,)

    @property  # get FINANCIAL
    def financial(self) -> tuple[DFT_P03_FINANCIAL_GROUP, ...]:
        """
        id: DFT_P03_FINANCIAL_GROUP SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_FINANCIAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_FINANCIAL_GROUP
        """
        return self._c_data[11]

    @financial.setter  # set FINANCIAL
    def financial(
        self, financial: DFT_P03_FINANCIAL_GROUP | tuple[DFT_P03_FINANCIAL_GROUP, ...]
    ):
        """
        id: FINANCIAL SEGMENT GROUP | use: R | rpt: * | seq: None
        ---
        param_type: DFT_P03_FINANCIAL_GROUP.None | tuple[DFT_P03_FINANCIAL_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_FINANCIAL_GROUP
        """
        if isinstance(financial, tuple):
            self._c_data[11] = financial
        else:
            self._c_data[11] = (financial,)

    @property  # get DG1
    def diagnosis(self) -> tuple[DG1, ...] | tuple[None]:
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        return_type: tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        return self._c_data[12]

    @diagnosis.setter  # set DG1
    def diagnosis(self, dg1: DG1 | tuple[DG1, ...] | None):
        """
        id: DG1 SEGMENT GROUP | use: O | rpt: * | seq: 29
        ---
        param_type: DG1.29 | tuple[DG1, ...]: (Diagnosis, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DG1
        """
        if isinstance(dg1, tuple):
            self._c_data[12] = dg1
        else:
            self._c_data[12] = (dg1,)

    @property  # get DRG.30
    def diagnosis_related_group(self) -> DRG | None:
        """
        id: DRG | use: O | rpt: 1 | seq: 30
        ---
        return_type: DRG.30: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        return self._c_data[13][0]

    @diagnosis_related_group.setter  # set DRG.30
    def diagnosis_related_group(self, drg: DRG | None):
        """
        id: DRG | use: O | rpt: 1 | seq: 30
        ---
        param_type: DRG.30: Diagnosis Related Group
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DRG
        """
        self._c_data[13] = (drg,)

    @property  # get GT1
    def guarantor(self) -> tuple[GT1, ...] | tuple[None]:
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 31
        ---
        return_type: tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        return self._c_data[14]

    @guarantor.setter  # set GT1
    def guarantor(self, gt1: GT1 | tuple[GT1, ...] | None):
        """
        id: GT1 SEGMENT GROUP | use: O | rpt: * | seq: 31
        ---
        param_type: GT1.31 | tuple[GT1, ...]: (Guarantor, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/GT1
        """
        if isinstance(gt1, tuple):
            self._c_data[14] = gt1
        else:
            self._c_data[14] = (gt1,)

    @property  # get INSURANCE
    def insurance(self) -> tuple[DFT_P03_INSURANCE_GROUP, ...] | tuple[None]:
        """
        id: DFT_P03_INSURANCE_GROUP SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        return_type: tuple[DFT_P03_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_INSURANCE_GROUP
        """
        return self._c_data[15]

    @insurance.setter  # set INSURANCE
    def insurance(
        self,
        insurance: DFT_P03_INSURANCE_GROUP | tuple[DFT_P03_INSURANCE_GROUP, ...] | None,
    ):
        """
        id: INSURANCE SEGMENT GROUP | use: O | rpt: * | seq: None
        ---
        param_type: DFT_P03_INSURANCE_GROUP.None | tuple[DFT_P03_INSURANCE_GROUP, ...]: (None, ...)
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/DFT_P03_INSURANCE_GROUP
        """
        if isinstance(insurance, tuple):
            self._c_data[15] = insurance
        else:
            self._c_data[15] = (insurance,)

    @property  # get ACC.36
    def accident(self) -> ACC | None:
        """
        id: ACC | use: O | rpt: 1 | seq: 36
        ---
        return_type: ACC.36: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        return self._c_data[16][0]

    @accident.setter  # set ACC.36
    def accident(self, acc: ACC | None):
        """
        id: ACC | use: O | rpt: 1 | seq: 36
        ---
        param_type: ACC.36: Accident
        ---
        https://hl7-definition.caristix.com/v2/HL7v2.5.1/Segments/ACC
        """
        self._c_data[16] = (acc,)
